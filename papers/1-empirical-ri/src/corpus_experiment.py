"""corpus_experiment.py — paper §7.2 corpus pilot, per INSTRUCTIONS.md §3.

Reuses ri_text/ri_pilot estimators but drives covering/selection/certificates
from ESTIMATED channels (INSTRUCTIONS §3.2: "replace the planted CH/LAM by the
estimated channels and empirical type frequencies").

Refusal + coarsening discipline. The refusal rule n_min >= 20*alphabet is real on
SemCor: the rarest kept sense of most words has < 160 tokens, so alphabet-8
context types refuse. Rather than decline, the pipeline COARSENS (design §3): per
word/type we pick the largest alphabet a in [2..8] with a <= n_min/20, merging to
the top-(a-1) symbols + OTHER (frequencies frozen on the whole word set; feature
VOCAB was already frozen on the train split in prepare_corpus). Types that cannot
reach a=2 are refused and logged.

Covering model. Every SemCor token carries all context types at once, whereas §4's
i.i.d. model draws one view type per usage. We reconcile them by modeling each
usage as exposing one context type drawn from lambda_t = empirical informativeness
(fraction of tokens where type t is a non-OTHER, non-boundary symbol), normalized
over the type family — the "empirical type frequencies" §3.2 asks for. Per-type
channels are the estimated ones; BC_e is taken over the estimated channels.
"""
import os, sys, json, itertools
from collections import Counter, defaultdict
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "shared"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # paper folder: ri_text.py
sys.path.insert(0, os.path.dirname(__file__))
from ri_pilot import q_info, ledger_table, deficiency, h2
from math import log2

RNG = np.random.default_rng(7)
BC = lambda p, q: float(np.sqrt(np.asarray(p) * np.asarray(q)).sum())
REFUSAL_FACTOR = 20
DELTA = 0.05
BOUNDARY = {"OTHER", "BOS", "EOS"}


def estimate_channel(codes, labels, k, n_class, alpha=0.5):
    codes = np.asarray(codes); labels = np.asarray(labels)
    flat = codes * n_class + labels
    counts = np.bincount(flat, minlength=k * n_class).reshape(k, n_class).astype(float)
    P = counts + alpha
    return P / P.sum(0, keepdims=True)


# ---------------- load + per-word structures ----------------
def load(path):
    by_word = defaultdict(list)
    for line in open(path):
        t = json.loads(line)
        by_word[t["word"]].append(t)
    return by_word


def adaptive_channel(tokens, ft, senses, sidx):
    """Estimate a channel for feature type ft with the largest refusal-passing
    alphabet. Returns dict(P, a, symbols, refused, lam)."""
    labels = np.array([sidx[t["sense"]] for t in tokens])
    nc = np.bincount(labels, minlength=len(senses))
    n_min = nc.min()
    a = min(8, int(n_min // REFUSAL_FACTOR))
    vals = [t["features"][ft] for t in tokens]
    lam_inform = np.mean([v not in BOUNDARY for v in vals])  # informativeness mass
    if a < 2:
        return dict(refused=True, reason=f"n_min={n_min} < {2*REFUSAL_FACTOR}", lam=lam_inform)
    # top-(a-1) symbols + OTHER (frequency on the whole word set)
    freq = Counter(vals)
    top = [v for v, _ in freq.most_common(a - 1)]
    symmap = {v: i for i, v in enumerate(top)}
    codes = np.array([symmap.get(v, a - 1) for v in vals])  # last bin = merged OTHER
    P = estimate_channel(codes, labels, a, len(senses))
    return dict(refused=False, P=P, a=a, symbols=top + ["<OTHER>"], lam=lam_inform,
               n_min=int(n_min))


# ---------------- covering (estimated channels) ----------------
def covering_prediction(channels, lam, pairs, delta=DELTA):
    E = len(pairs); out = {}
    for (i, j) in pairs:
        seps = [t for t, P in channels.items() if BC(P[:, i], P[:, j]) < 1 - 1e-9]
        if not seps:
            out[(i, j)] = float("inf"); continue
        # CORRECTED per-type bound (paper Thm 4.2, fixed after the corpus run;
        # INSTRUCTIONS.md §5): the test may restrict to looks of ONE type t, so for
        # each separating t the bound (1/lam_t)*max(1, ln(2E/delta)/ln(1/BC_t)) is
        # valid; take the min. The earlier form paired TOTAL separating mass with the
        # BEST per-look BC and is not a valid bound when weak separators dominate.
        def per_type(t):
            b = max(BC(channels[t][:, i], channels[t][:, j]), 1e-9)
            return (1 / lam[t]) * max(1.0, np.log(2 * E / delta) / np.log(1 / b))
        out[(i, j)] = min(per_type(t) for t in seps)
    return out


def empirical_covering_stream(type_stream, channels, pairs, delta=DELTA):
    """N_hat(e): first n at which 0.5*prod BC^{n_t} <= delta, accumulating a look of
    type t (with its per-pair BC) each time type t appears in the stream."""
    logB = {e: 0.0 for e in pairs}; resolved = {}
    for n, t in enumerate(type_stream, 1):
        P = channels.get(t)
        if P is None:
            continue
        for e in pairs:
            if e in resolved:
                continue
            b = max(BC(P[:, e[0]], P[:, e[1]]), 1e-12)
            if b < 1 - 1e-9:
                logB[e] += np.log(b)
                if 0.5 * np.exp(logB[e]) <= delta:
                    resolved[e] = n
    return resolved


def run_covering(tokens, channels, lam, pairs, n_runs=30):
    types = list(channels)
    lam_vec = np.array([lam[t] for t in types])
    lam_vec = lam_vec / lam_vec.sum()
    Ns = defaultdict(list)
    for r in range(n_runs):
        rng = np.random.default_rng(100 + r)
        stream = rng.choice(types, size=len(tokens), p=lam_vec)
        res = empirical_covering_stream(stream, channels, pairs)
        for e in pairs:
            Ns[e].append(res.get(e, len(tokens) + 1))  # unresolved -> censored
    med = {e: float(np.median(Ns[e])) for e in pairs}
    # prediction's lambda_t must be the SAME normalized per-type arrival rate the
    # stream samples with (lam_vec), so the per-type bound uses the true 1/lambda_t.
    lam_norm = {t: float(lam_vec[k]) for k, t in enumerate(types)}
    pred = covering_prediction(channels, lam_norm, pairs)
    return med, pred


# ---------------- selection (greedy + coupling audit) ----------------
def I_of_types(sel, channels, n_senses):
    if not sel:
        return 0.0
    J = channels[sel[0]]
    for t in sel[1:]:
        J = np.einsum("as,bs->abs", J, channels[t]).reshape(-1, n_senses)
    prior = np.full(n_senses, 1.0 / n_senses)  # replaced by caller's prior via q_info
    return J


def greedy_select(channels, prior, q_of_s, n_senses, k=3):
    """Greedy over context types; stall-audit per INSTRUCTIONS §3.3 (relative
    threshold 1e-3 * H(q)). Always records the most super-additive remaining pair
    for reporting, whether or not the audit fires."""
    types = list(channels)
    Hq = float(-sum(p * log2(p) for p in prior if p > 1e-12))  # q = identity on senses
    stall = 1e-3 * Hq
    def I(sel):
        if not sel:
            return 0.0
        J = channels[sel[0]]
        for t in sel[1:]:
            J = np.einsum("as,bs->abs", J, channels[t]).reshape(-1, n_senses)
        return q_info(J, prior, q_of_s)
    S, log = [], []
    for step in range(k):
        gains = {t: I(S + [t]) - I(S) for t in types if t not in S}
        if not gains:
            break
        best = max(gains, key=gains.get)
        entry = dict(step=step + 1, pick=best, gain=float(gains[best]),
                     gains={t: float(g) for t, g in gains.items()})
        # best super-additive pair among remaining (coupling candidate)
        best_pair, best_excess = None, 0.0
        for t1, t2 in itertools.combinations([t for t in types if t not in S], 2):
            pg = I(S + [t1, t2]) - I(S)
            excess = pg - (gains[t1] + gains[t2])
            if excess > best_excess:
                best_pair, best_excess = (t1, t2, float(pg)), float(excess)
        entry["best_superadditive_pair"] = best_pair
        entry["best_superadditivity"] = best_excess
        entry["stalled"] = bool(gains[best] < stall)
        if entry["stalled"] and best_pair is not None and best_excess > 1e-3:
            entry["audit"] = best_pair
        S.append(best); log.append(entry)
    return S, log


# ---------------- certificates ----------------
def certificate(tokens, channels, lam, pairs, budget):
    types = list(channels)
    lam_vec = np.array([lam[t] for t in types]); lam_vec /= lam_vec.sum()
    rng = np.random.default_rng(42)
    stream = rng.choice(types, size=budget, p=lam_vec)
    res = empirical_covering_stream(stream, channels, pairs)
    unresolved = [e for e in pairs if e not in res]
    fixes = {e: sorted(types, key=lambda t: BC(channels[t][:, e[0]], channels[t][:, e[1]]))[:2]
             for e in unresolved}
    return dict(budget=budget, resolved={f"{e}": res[e] for e in res},
                residual=[list(e) for e in unresolved],
                recommended={f"{e}": fixes[e] for e in unresolved})


# ---------------- driver ----------------
def run_word(word, tokens, out):
    senses = sorted({t["sense"] for t in tokens})
    sidx = {s: i for i, s in enumerate(senses)}
    labels = np.array([sidx[t["sense"]] for t in tokens])
    nc = np.bincount(labels, minlength=len(senses))
    prior = nc / nc.sum()
    ftypes = sorted({ft for t in tokens for ft in t["features"]})

    channels, lam, per_type, refusals = {}, {}, {}, []
    for ft in ftypes:
        r = adaptive_channel(tokens, ft, senses, sidx)
        lam[ft] = r["lam"]
        if r["refused"]:
            refusals.append(dict(type=ft, reason=r["reason"]))
            continue
        channels[ft] = r["P"]
        I = q_info(r["P"], prior, list(range(len(senses))))
        per_type[ft] = dict(I=float(I), alphabet=r["a"], symbols=r["symbols"],
                            n_min=r["n_min"])

    pairs = list(itertools.combinations(range(len(senses)), 2))
    rec = dict(word=word, n_tokens=len(tokens), n_senses=len(senses),
               senses=senses, prior=prior.tolist(),
               per_type=per_type, refusals=refusals)

    if channels:
        med, pred = run_covering(tokens, channels, lam, pairs)
        hardest_emp = max(med, key=med.get)
        finite_pred = {e: v for e, v in pred.items() if np.isfinite(v)}
        hardest_pred = max(finite_pred, key=finite_pred.get) if finite_pred else None
        rec["covering"] = dict(
            median_N={f"{e}": med[e] for e in pairs},
            prediction={f"{e}": (None if not np.isfinite(pred[e]) else pred[e]) for e in pairs},
            hardest_empirical=list(hardest_emp),
            hardest_predicted=list(hardest_pred) if hardest_pred else None,
            prediction_correct=(hardest_emp == hardest_pred))
        S, log = greedy_select(channels, prior, list(range(len(senses))), len(senses), k=3)
        rec["selection"] = dict(picked=S, log=log,
                                audit_fired=any("audit" in e for e in log))
        rec["certificates"] = [certificate(tokens, channels, lam, pairs, b)
                               for b in (25, 50, 100)]
    else:
        rec["covering"] = None
        rec["note"] = "all context types refused; no estimable channel"

    out[word] = rec
    # print compact
    print(f"\n=== {word} ({len(tokens)} tok, {len(senses)} senses) ===")
    for ft, d in sorted(per_type.items(), key=lambda kv: -kv[1]["I"]):
        print(f"  I(q;{ft}) = {d['I']:.4f}  [alphabet {d['alphabet']}, n_min {d['n_min']}]")
    for r in refusals:
        print(f"  [refused] {r['type']}: {r['reason']}")
    if channels:
        c = rec["covering"]
        print(f"  covering: hardest empirical={c['hardest_empirical']} "
              f"predicted={c['hardest_predicted']} correct={c['prediction_correct']}")
        print(f"  selection picks={rec['selection']['picked']} "
              f"audit_fired={rec['selection']['audit_fired']}")
        for e in log:
            if "audit" in e:
                print(f"    AUDIT at step {e['step']}: {e['audit']}")


def annotator_audit_note():
    """SemCor is single-annotated: no double annotations -> corpus annotator Fano
    audit is not available (a refusal/finding). The planted SynthSense audit
    (paper §7.2) validates the estimator; we re-run it for the record in
    ri_text.annotator_fano()."""
    import ri_text
    f = ri_text.annotator_fano()
    return dict(available_on_semcor=False,
                reason="SemCor tokens are single-annotated (no sense2 field)",
                synthsense_validation={k: (float(v) if isinstance(v, (int, float, np.floating)) else
                                           [float(x) for x in v]) for k, v in f.items()})


def main():
    os.makedirs("results", exist_ok=True)
    by_word = load(sys.argv[1] if len(sys.argv) > 1 else "data/tokens.jsonl")
    out = {}
    for word in by_word:
        run_word(word, by_word[word], out)
    ann = annotator_audit_note()
    print("\n=== annotator audit ===")
    print("  SemCor single-annotated -> corpus Fano audit N/A (finding).")
    print(f"  SynthSense validated: H_residual={ann['synthsense_validation']['H_residual']:.4f}"
          f" <= bound {ann['synthsense_validation']['fano_bound']:.4f}; "
          f"true_err {ann['synthsense_validation']['true_error']:.4f} in bracket "
          f"{ann['synthsense_validation']['err_bracket']}")
    results = dict(words=out, annotator_audit=ann,
                   config=dict(refusal_factor=REFUSAL_FACTOR, delta=DELTA))
    with open("results/corpus_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nwrote results/corpus_results.json")


if __name__ == "__main__":
    main()
