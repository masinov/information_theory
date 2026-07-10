"""ri_text.py — text instantiation of Empirical Registered Information.
Contrast domain D = sense inventory; views = context types as channels.
Implements: SynthSense (planted ground truth), covering estimator + hardest-pair
prediction, greedy definition selection with the coarse-coupling audit (paper
Thm 5.2/5.3), characterization certificates (Thm 4.4), the fiberwise leak demo
and annotator Fano audit (paper §6), and the corpus-runner interface (§7.3).

Corpus mode input format (JSONL, one token per line):
    {"word": str, "sense": str, "features": {"<type>": <symbol>, ...}}
Run:  python3 ri_text.py corpus <file.jsonl> <word> <question-spec>
where question-spec is "all" or "senseA|senseB". See INSTRUCTIONS.md.
"""
import numpy as np, json, sys, itertools
from math import log2
from ri_pilot import estimate_channel, mi_from_channel, deficiency, ledger_table, q_info, h2

RNG = np.random.default_rng(7)
BC = lambda p, q: float(np.sqrt(np.asarray(p)*np.asarray(q)).sum())

# ---------------- SynthSense: planted polysemy world ----------------
# Senses s0..s3, prior (0.4,0.3,0.2,0.1). Bit a(s) = s in {s1,s3}.
# Context types (view family) with sampling distribution lambda:
#  t1 (lam .30): deterministic frame separating {s0,s1} vs {s2,s3}
#  t2 (lam .25): noisy frame for s0 vs s1: P(0|s0)=.9, P(0|s1)=.2; s2,s3 uniform
#  t3 (lam .20): noisy frame for s2 vs s3: P(0|s2)=.85, P(0|s3)=.25; s0,s1 uniform
#  t4,t5 (lam .05 each): marginal features of the coupled pair (a-blind alone)
#  t45 (lam .15): the JOINT coupled view (RI Prop 22.4(2) keyed to bit a):
#       a=0 -> two symbols equal fair coin; a=1 -> independent fair coins.
PRIOR = np.array([.4, .3, .2, .1])
A_BIT = np.array([0, 1, 0, 1])
LAM = dict(t1=.30, t2=.25, t3=.20, t4=.05, t5=.05, t45=.15)
CH = {  # planted channels P(y|s), columns = senses
 't1': np.array([[1,1,0,0],[0,0,1,1]], float),
 't2': np.array([[.9,.2,.5,.5],[.1,.8,.5,.5]]),
 't3': np.array([[.5,.5,.85,.25],[.5,.5,.15,.75]]),
 't4': np.array([[.5,.5,.5,.5],[.5,.5,.5,.5]]),
 't5': np.array([[.5,.5,.5,.5],[.5,.5,.5,.5]]),
}
def ch_t45():
    P = np.zeros((4, 4))
    for s in range(4):
        if A_BIT[s] == 0: P[0, s] = P[3, s] = .5            # equal coins (00,11)
        else: P[:, s] = .25                                  # independent
    return P
CH['t45'] = ch_t45()

def sample_usages(n):
    types = list(LAM); lam = np.array([LAM[t] for t in types])
    ts = RNG.choice(len(types), n, p=lam)
    senses = RNG.choice(4, n, p=PRIOR)
    out = []
    for i in range(n):
        t = types[ts[i]]; s = senses[i]
        y = RNG.choice(CH[t].shape[0], p=CH[t][:, s])
        out.append((t, int(y), int(s)))
    return out

# ---------------- §4: covering estimator + hardest-pair prediction ----------
def pair_bc(t, i, j): return BC(CH[t][:, i], CH[t][:, j])

def covering_prediction(pairs, delta=0.05):
    """Thm 4.3 upper-bound scale: max_e log(E/delta)/(lam_e * log(1/BC_e)),
    lam_e = usage mass of types separating e, BC_e = best per-look BC."""
    E = len(pairs); out = {}
    for (i, j) in pairs:
        seps = [t for t in LAM if pair_bc(t, i, j) < 1 - 1e-9]
        # CORRECTED per-type bound (paper Thm 4.2, fixed after the corpus run):
        # the test may restrict to looks of ONE type t, so for each separating t
        # the bound (1/lam_t)*max(1, ln(2E/delta)/ln(1/BC_t)) is valid; take the min.
        # (The earlier form paired total separating mass with the BEST per-look BC
        #  and is NOT a valid bound when weak separators dominate arrivals.)
        def per_type(t):
            b = max(pair_bc(t, i, j), 1e-9)
            return (1/LAM[t]) * max(1.0, np.log(2*E/delta)/np.log(1/b))
        out[(i, j)] = min(per_type(t) for t in seps)
    return out

def empirical_covering(usages, pairs, delta=0.05):
    """N_hat(e): first n at which the accumulated per-pair BC bound <= delta.
    Test-error bound after looks {(t,y)}: (1/2) prod_t BC_t^{n_t} via RI 78.3."""
    logB = {e: 0.0 for e in pairs}; resolved = {}
    for n, (t, y, s) in enumerate(usages, 1):
        for e in pairs:
            if e in resolved: continue
            b = max(pair_bc(t, e[0], e[1]), 1e-12)
            if b < 1 - 1e-9:
                logB[e] += np.log(b)
                if 0.5*np.exp(logB[e]) <= delta: resolved[e] = n
    return resolved

def certificate(usages_prefix, pairs, delta=0.05):
    res = empirical_covering(usages_prefix, pairs, delta)
    unresolved = [e for e in pairs if e not in res]
    fixes = {e: sorted(LAM, key=lambda t: pair_bc(t, *e))[:2] for e in unresolved}
    return res, unresolved, fixes

# ---------------- §5: greedy selection with the coarse-coupling audit --------
def _component(t45, which):
    """Marginal feature channel of the joint type: 'v' = first symbol, 'w' = second."""
    if which == 'v':
        return np.array([t45[0]+t45[1], t45[2]+t45[3]])
    return np.array([t45[0]+t45[2], t45[1]+t45[3]])

def I_of_set(types, q_of_s, exact=True, n_est=20000):
    """I(q; joint of selected items). Items are type names or (type, 'v'|'w')
    components; two components of the SAME type combine via that type's JOINT
    channel (shared usage tokens -> the coupling is live); distinct types are
    conditionally independent given the sense (distinct usages)."""
    if not types: return 0.0
    # group components of shared joint types
    grouped, singles = {}, []
    for it in types:
        if isinstance(it, tuple): grouped.setdefault(it[0], set()).add(it[1])
        else: singles.append(it)
    chans = []
    for base, comps in grouped.items():
        chans.append(CH[base] if comps == {'v','w'} else _component(CH[base], next(iter(comps))))
    for t in singles:
        P = CH[t]
        if not exact:
            s = RNG.choice(4, n_est, p=PRIOR)
            y = np.array([RNG.choice(P.shape[0], p=P[:, si]) for si in s])
            P = estimate_channel(y, s, P.shape[0], 4)
        chans.append(P)
    if not chans: return 0.0
    # product channel across types (CI given sense: separate usages)
    J = chans[0]
    for P in chans[1:]:
        J = np.einsum('as,bs->abs', J, P).reshape(-1, 4)
    return q_info(J, PRIOR, list(q_of_s))

def greedy(universe, q_of_s, k, audit=True, exact=True):
    S, log = [], []
    for step in range(k):
        gains = {t: I_of_set(S+[t], q_of_s, exact) - I_of_set(S, q_of_s, exact)
                 for t in universe if t not in S}
        best = max(gains, key=gains.get)
        entry = dict(step=step+1, pick=best, gain=gains[best], gains=dict(gains))
        if audit and gains[best] < 1e-3:
            # coarse-coupling audit: any PAIR whose joint gain >> marginal gains?
            for t1, t2 in itertools.combinations([t for t in universe if t not in S], 2):
                pair_gain = I_of_set(S+[t1, t2], q_of_s, exact) - I_of_set(S, q_of_s, exact)
                if pair_gain > gains[t1] + gains[t2] + 1e-3:
                    entry['audit'] = (t1, t2, pair_gain)
        S.append(best); log.append(entry)
    return S, log

# ---------------- §6: anchoring demos --------------------------------------
def leak_demo():
    """Fiberwise criterion (RI Prop 45.2 corrected): presentation y0, contexts
    c1..c3, eta pairwise-compatible, globally incompatible -> every policy leaks."""
    eta = {1: {'s0','s1'}, 2: {'s1','s2'}, 3: {'s0','s2'}}
    forced = any(len(eta[i] & eta[j]) == 0 for i, j in itertools.combinations(eta, 2))
    total = set.intersection(*eta.values())
    leaks = all(len(set(p)) > 1 for p in itertools.product(*[sorted(eta[c]) for c in eta]))
    return forced, total, leaks

def annotator_fano(n=30000, disagree=0.18):
    """Prop 6.1 (identity reading): tags are sufficient up to a Fano residual —
    H(sense | tag) <= h(err) + err*log2(m-1); the unobservable per-annotator err
    is bracketed by observable disagreement E under conditional independence:
    E/2 <= max(err_i) <= E (small-rate regime)."""
    s = RNG.choice(4, n, p=PRIOR)
    tagger = lambda: np.where(RNG.random(n) < disagree, RNG.choice(4, n), s)
    t1, t2 = tagger(), tagger()
    E = (t1 != t2).mean()
    err = (t1 != s).mean()
    joint = np.zeros((4, 4))
    for si, ti in zip(s, t1): joint[si, ti] += 1/n
    Hs_given_tag = -(joint[joint > 1e-12] * np.log2(joint[joint > 1e-12])).sum() +                    (lambda pt: -(pt[pt > 1e-12]*np.log2(pt[pt > 1e-12])).sum())(joint.sum(0)) * -1
    Hs_given_tag = (lambda J: -(J[J>1e-12]*np.log2(J[J>1e-12])).sum() -
                    (lambda pt: -(pt[pt>1e-12]*np.log2(pt[pt>1e-12])).sum())(J.sum(0)))(joint)
    bound = h2(min(err, .75)) + err*log2(3)
    return dict(disagreement=E, true_error=err, H_residual=Hs_given_tag,
                fano_bound=bound, err_bracket=(E/2, E))

# ---------------- corpus mode (user-executed; see INSTRUCTIONS.md) ----------
def corpus_run(path, word, qspec, delta=0.05, alpha=0.5, refusal_factor=20):
    toks = [json.loads(l) for l in open(path) if json.loads(l)["word"] == word]
    senses = sorted({t["sense"] for t in toks}); sidx = {s: i for i, s in enumerate(senses)}
    types = sorted({ft for t in toks for ft in t["features"]})
    print(f"word={word}: {len(toks)} tokens, {len(senses)} senses, {len(types)} context types")
    labels = np.array([sidx[t["sense"]] for t in toks])
    nc = np.bincount(labels, minlength=len(senses))
    chans, alph = {}, {}
    for ft in types:
        pairs_ = [(i, t["features"][ft]) for i, t in enumerate(toks) if ft in t["features"]]
        syms = sorted({v for _, v in pairs_}); m = {v: j for j, v in enumerate(syms)}
        idx = np.array([i for i, _ in pairs_]); codes = np.array([m[v] for _, v in pairs_])
        if nc.min() < refusal_factor*len(syms):
            print(f"  [refused] type {ft}: alphabet {len(syms)} vs n_min {nc.min()}"); continue
        chans[ft] = estimate_channel(codes, labels[idx], len(syms), len(senses), alpha)
        alph[ft] = len(syms)
    q = list(range(len(senses))) if qspec == "all" else \
        [0 if s == qspec.split("|")[0] else 1 for s in senses]
    prior = nc/nc.sum()
    rows = [(ft, q_info(P, prior, q)) for ft, P in chans.items()]
    for ft, I in sorted(rows, key=lambda r: -r[1]):
        print(f"  I(q; {ft}) = {I:.4f} bits")
    print("  -> feed chans into greedy()/ledger_table() per INSTRUCTIONS.md §3.")
    return chans, prior, q

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "corpus":
    corpus_run(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "all")
