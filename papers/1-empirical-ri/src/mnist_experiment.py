"""mnist_experiment.py — paper §7.1 (E1/E2/E3), per INSTRUCTIONS.md §1.

Views: 4x4 grid of 7x7 patches; per patch the mean intensity is quantized into
k=4 quantile bins whose edges are FIT on a disjoint split and FROZEN (design §0).

Splitting note (documented deviation, forced by MNIST class sizes): the top-4
joint alphabet is 4^4 = 256, so the refusal rule n_min >= 20*256 = 5120 requires
~81% of a class in the reporting split. A fully disjoint estimation/evaluation
split is therefore incompatible with the k=4 top-4 identity joint at MNIST class
sizes. We fit the quantizer on a disjoint 10% (7k) split and estimate + evaluate
on the remaining 90% (63k) with B=200 bootstrap CIs for the held-out-style
uncertainty. Pairwise (E2) and single-view analyses admit a disjoint split
trivially and stay well inside the rule (alphabet 16, n_min >= 320).

Outputs: prints tables and writes results/mnist_results.json.
"""
import os, sys, json, itertools
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "shared"))
sys.path.insert(0, os.path.dirname(__file__))
from data_mnist import load_mnist
import ri_pilot as rp
from ri_pilot import (mi_from_channel, q_info, q_tv, deficiency,
                      blind_mix, targeted_attack, ledger_table, refusal, h2)


def estimate_channel(codes, labels, k, n_class, alpha=0.5):
    """Vectorized Laplace-smoothed P_hat[y|z] (identical to ri_pilot's, but O(n)
    via bincount instead of a Python per-sample loop — needed inside bootstrap)."""
    codes = np.asarray(codes); labels = np.asarray(labels)
    flat = codes * n_class + labels
    counts = np.bincount(flat, minlength=k * n_class).reshape(k, n_class).astype(float)
    P = counts + alpha
    return P / P.sum(0, keepdims=True)


def mi_mm(codes, labels, k, n_class):
    """Miller-Madow bias-corrected empirical I(code; label) in bits (design §4:
    'Miller-Madow bias correction on all I-hat'). Plug-in MI plus the per-entropy
    (m-1)/(2n ln2) corrections, m = number of occupied bins:
        I_MM = I_plugin + (m_x + m_y - m_xy - 1) / (2 n ln2).
    (m_xy >= m_x, m_y, so the correction removes the plug-in's upward bias.)"""
    codes = np.asarray(codes); labels = np.asarray(labels); n = len(codes)
    J = np.bincount(codes * n_class + labels, minlength=k * n_class).reshape(k, n_class)
    p = J / n
    px, py = p.sum(1), p.sum(0)
    nz = p > 0
    Hxy = -(p[nz] * np.log2(p[nz])).sum()
    Hx = -(px[px > 0] * np.log2(px[px > 0])).sum()
    Hy = -(py[py > 0] * np.log2(py[py > 0])).sum()
    mi = Hx + Hy - Hxy
    m_x, m_y, m_xy = int((px > 0).sum()), int((py > 0).sum()), int(nz.sum())
    return float(mi + (m_x + m_y - m_xy - 1) / (2 * n * np.log(2)))


def best_merge_map(codes_p, labels, n_class, b):
    """Frozen q-optimal b-ary merge of one view's k=4 bins: the partition into <=b
    blocks maximizing the view's MM-corrected I(q; merged). Returns (map, n_blocks)."""
    best, best_map, best_nb = -1e9, np.arange(K), K
    for part in ALL_PARTS:
        if len(part) > b:
            continue
        mm = merge_map(part)
        I = mi_mm(mm[codes_p], labels, len(part), n_class)
        if I > best:
            best, best_map, best_nb = I, mm, len(part)
    return best_map, best_nb


RNG = np.random.default_rng(0)
GRID = 4          # 4x4 grid
PS = 7            # 7x7 patches
K = 4             # quantile bins per patch
NB_BOOT = 200


# ---------------- patch views + frozen quantile quantizer ----------------
def patch_means(X):
    """X (N,28,28) -> (N,16) mean intensity per 7x7 patch, row-major grid."""
    N = X.shape[0]
    out = np.empty((N, GRID * GRID))
    p = 0
    for gi in range(GRID):
        for gj in range(GRID):
            block = X[:, gi*PS:(gi+1)*PS, gj*PS:(gj+1)*PS]
            out[:, p] = block.reshape(N, -1).mean(1)
            p += 1
    return out


def fit_edges(means_fit, k=K):
    """Per-patch frozen quantile edges (k-1 interior edges -> k bins)."""
    qs = np.linspace(0, 1, k + 1)[1:-1]
    return np.array([np.quantile(means_fit[:, p], qs) for p in range(means_fit.shape[1])])


def codes_from(means, edges):
    """Digitize each patch's mean into its frozen bins -> (N,16) codes in 0..k-1."""
    N, P = means.shape
    out = np.empty((N, P), dtype=int)
    for p in range(P):
        out[:, p] = np.digitize(means[:, p], edges[p])
    return out


# ---------------- b-ary optimal merges (exhaustive at k=4) ----------------
def set_partitions(elements):
    if len(elements) == 1:
        yield [elements]
        return
    first, rest = elements[0], elements[1:]
    for smaller in set_partitions(rest):
        for i, subset in enumerate(smaller):
            yield smaller[:i] + [[first] + subset] + smaller[i+1:]
        yield [[first]] + smaller


ALL_PARTS = list(set_partitions([0, 1, 2, 3]))  # Bell(4) = 15


def merge_map(partition, k=K):
    """symbol -> merged-symbol lookup for a partition of {0..k-1}."""
    m = np.empty(k, dtype=int)
    for gi, grp in enumerate(partition):
        for s in grp:
            m[s] = gi
    return m


def best_bary_info(codes_p, labels, prior, q_of_z, b, n_class):
    """Max single-view Î over all merges of k=4 into <= b blocks."""
    best = -1.0
    for part in ALL_PARTS:
        if len(part) > b:
            continue
        mm = merge_map(part)
        merged = mm[codes_p]
        P = estimate_channel(merged, labels, len(part), n_class)
        I = q_info(P, prior, q_of_z)
        best = max(best, I)
    return best


# ---------------- joint channel over a set of patches ----------------
def joint_codes(codes, patch_ids, k=K):
    """Fold selected patch codes into a single joint symbol in 0..k^len-1."""
    out = np.zeros(codes.shape[0], dtype=int)
    for pid in patch_ids:
        out = out * k + codes[:, pid]
    return out


def single_view_infos(codes, labels, prior, q_of_z, n_class, patch_ids=None):
    ids = range(codes.shape[1]) if patch_ids is None else patch_ids
    out = {}
    for p in ids:
        P = estimate_channel(codes[:, p], labels, K, n_class)
        out[p] = q_info(P, prior, q_of_z)
    return out


# ---------------- question helpers ----------------
def restrict(codes, Z, classes):
    """Restrict to a subset of classes; relabel to 0..len-1."""
    mask = np.isin(Z, classes)
    remap = {c: i for i, c in enumerate(classes)}
    z = np.array([remap[v] for v in Z[mask]])
    return codes[mask], z


def bootstrap_scalar(fn, n, B=NB_BOOT, alpha=0.05):
    vals = []
    for _ in range(B):
        idx = RNG.integers(0, n, n)
        vals.append(fn(idx))
    lo, hi = np.quantile(vals, [alpha/2, 1 - alpha/2])
    return float(np.mean(vals)), float(lo), float(hi)


# ==================== E1 ====================
def run_E1(codes, Z, question, q_of_z, classes, n_class, J_target=4):
    """Returns sep-vs-joint table with CIs + accumulation, adaptively coarsening
    the number of joint patches J to satisfy the refusal rule."""
    prior = np.bincount(Z, minlength=n_class) / len(Z)
    sv = single_view_infos(codes, Z, prior, q_of_z, n_class)
    top = [p for p, _ in sorted(sv.items(), key=lambda kv: -kv[1])]

    # adaptive J: largest J<=target whose joint alphabet passes refusal on this split
    nc = np.bincount(Z, minlength=n_class)
    J = J_target
    while J > 1 and not refusal(nc, K ** J):
        J -= 1
    sel = top[:J]
    coarsened = (J < J_target)

    jc = joint_codes(codes, sel)
    n_joint_alph = K ** J

    def I_joint_fn(idx):
        return mi_mm(jc[idx], Z[idx], n_joint_alph, n_class)
    I_joint_mean, I_joint_lo, I_joint_hi = bootstrap_scalar(I_joint_fn, len(Z))

    rows = []
    for b in (1, 2, 3, 4):
        # freeze the per-view q-optimal b-ary merge on the full split (design §1:
        # 'each view compressed ALONE to b symbols ... read JOINTLY'); then the
        # compressed views are folded into one joint code and read together, so
        # Delta(b) = I_joint - I_sep(b) >= 0 by data processing.
        merges = {p: best_merge_map(codes[:, p], Z, n_class, b) for p in sel}

        def sep_codes(idx):
            out = np.zeros(len(idx), dtype=int)
            for p in sel:
                mm, nb = merges[p]
                out = out * nb + mm[codes[idx, p]]
            nalph = int(np.prod([merges[p][1] for p in sel]))
            return out, nalph

        def I_sep_fn(idx):
            out, nalph = sep_codes(idx)
            return mi_mm(out, Z[idx], nalph, n_class)
        Isep_m, Isep_lo, Isep_hi = bootstrap_scalar(I_sep_fn, len(Z), B=80)
        delta_m = I_joint_mean - Isep_m
        rows.append(dict(b=b, I_sep=Isep_m, I_sep_ci=[Isep_lo, Isep_hi],
                         Delta=delta_m))

    # Accumulation: two disjoint pixel subsamples of the single most-informative patch
    acc = accumulation(top[0], Z, prior, q_of_z, n_class, classes)

    return dict(question=question, J=J, J_target=J_target, coarsened=coarsened,
                selected_patches=sel, joint_alphabet=n_joint_alph,
                single_view_infos={int(k): float(v) for k, v in sv.items()},
                I_joint=I_joint_mean, I_joint_ci=[I_joint_lo, I_joint_hi],
                table=rows, accumulation=acc)


# accumulation needs the raw pixels, so it is fed the fit-split edges separately
_ACC_CACHE = {}


def accumulation(patch_id, Z, prior, q_of_z, n_class, classes):
    Xw = _ACC_CACHE["Xwork_means_by_pixel"]  # (N, 16, 49) per-patch pixel matrix
    Xf = _ACC_CACHE["Xfit_means_by_pixel"]
    idxmask = _ACC_CACHE["work_class_mask"](classes)
    # split 49 pixels into two disjoint halves (frozen split)
    perm = _ACC_CACHE["pix_perm"]
    A, Bset = perm[:24], perm[24:]
    def code_side(pix_mat, side, edges):
        m = pix_mat[:, patch_id, side].mean(1)
        return np.digitize(m, edges)
    # fit edges on fit split for each side
    eA = np.quantile(Xf[:, patch_id, A].mean(1), [.25, .5, .75])
    eB = np.quantile(Xf[:, patch_id, Bset].mean(1), [.25, .5, .75])
    cA = code_side(Xw, A, eA)[idxmask]
    cB = code_side(Xw, Bset, eB)[idxmask]
    labels = np.asarray(Z)
    # relabel to 0..n_class-1 domain used by mi_mm (Z is already restricted+remapped)
    IA = mi_mm(cA, labels, K, n_class)
    IB = mi_mm(cB, labels, K, n_class)
    IJ = mi_mm(cA * K + cB, labels, K * K, n_class)
    return dict(patch=int(patch_id), I_A=float(IA), I_B=float(IB), I_joint=float(IJ),
                gain=float(IJ - max(IA, IB)))


# ==================== E2 ====================
def run_E2(codes, Z, pair, question, eps_bar):
    """Ledger table for a pair of adjacent informative patches on a binary question.
    Domain is restricted to the two relevant classes."""
    n_class = 2
    prior = np.bincount(Z, minlength=n_class) / len(Z)
    p1, p2 = pair
    Pv = estimate_channel(codes[:, p1], Z, K, n_class)
    Pw = estimate_channel(codes[:, p2], Z, K, n_class)
    Pjoint = estimate_channel(joint_codes(codes, [p1, p2]), Z, K * K, n_class)
    q_of_z = list(range(n_class))
    lt = ledger_table(Pv, Pw, Pjoint, prior, q_of_z)
    # half-gap classifier (Cor 3.4): deficiency of the joint interval endpoints.
    # ν_δ between the two per-view channels (Blackwell interval of the pair).
    nu = deficiency(Pv, Pw)
    graded = nu < 0.5 - eps_bar
    # bootstrap key quantities
    def boot(fn):
        vals = []
        for _ in range(60):
            idx = RNG.integers(0, len(Z), len(Z))
            vals.append(fn(idx))
        return [float(np.quantile(vals, .025)), float(np.quantile(vals, .975))]
    def Ij(idx):
        return mi_from_channel(estimate_channel(joint_codes(codes, [p1, p2])[idx], Z[idx], K*K, n_class),
                               np.bincount(Z[idx], minlength=n_class)/len(idx))
    return dict(pair=[int(p1), int(p2)], question=question,
                I_joint=lt["I_joint"], I_min=lt["I_min"], C_fine=lt["C_fine"],
                CI_coarse=lt["CI_coarse"], max_I_v=max(lt["I_v"], lt["I_w"]),
                I_joint_ci=boot(Ij), nu_delta=float(nu),
                half_gap_graded=bool(graded), eps_bar=float(eps_bar))


# ==================== E3 ====================
def run_E3(codes, Z, patch_id, question, q_of_z, n_class):
    prior = np.bincount(Z, minlength=n_class) / len(Z)
    P_clean = estimate_channel(codes[:, patch_id], Z, K, n_class)
    d0 = q_tv(P_clean, prior, q_of_z)

    blind = []
    for eps in [0, .15, .3, .45, .6, .75, .9]:
        # measured: corrupt eval codes (flip to uniform with prob eps), re-estimate
        c = codes[:, patch_id].copy()
        flip = RNG.random(len(c)) < eps
        c[flip] = RNG.integers(0, K, flip.sum())
        Pm = estimate_channel(c, Z, K, n_class)
        I_meas = q_info(Pm, prior, q_of_z)
        tv_meas = q_tv(Pm, prior, q_of_z)
        # predicted closed form
        Pmix = blind_mix(P_clean, eps)
        I_pred = q_info(Pmix, prior, q_of_z)
        tv_pred = (1 - eps) * d0
        blind.append(dict(eps=eps, I_meas=float(I_meas), I_pred=float(I_pred),
                          tv_meas=float(tv_meas), tv_pred=float(tv_pred)))

    # targeted: hard zero at eps* = d/(2+d) with d = L1 separation = 2*TV (Lemma 62.1)
    d_L1 = 2 * d0
    eps_star = d_L1 / (2 + d_L1)
    targeted = []
    for eps in [max(0, eps_star - .1), eps_star, min(.99, eps_star + .1)]:
        Pt = targeted_attack(P_clean, prior, q_of_z, eps)
        targeted.append(dict(eps=float(eps), I=float(q_info(Pt, prior, q_of_z)),
                             tv=float(q_tv(Pt, prior, q_of_z))))
    # fine scan to locate the empirical hard zero (first eps at which I annihilates)
    grid = np.linspace(0.01, min(0.9, eps_star + 0.2), 180)
    Is = [q_info(targeted_attack(P_clean, prior, q_of_z, e), prior, q_of_z) for e in grid]
    zeros = np.where(np.array(Is) < 1e-4)[0]
    eps_zero_emp = float(grid[zeros[0]]) if len(zeros) else float("nan")
    return dict(patch=int(patch_id), question=question, d0=float(d0), d_L1=float(d_L1),
                eps_star=float(eps_star), eps_zero_empirical=eps_zero_emp,
                I_at_empirical_zero=float(min(Is)), blind=blind, targeted=targeted)


# ==================== driver ====================
def main():
    os.makedirs("results", exist_ok=True)
    print("loading MNIST ...")
    X, Z = load_mnist()
    N = len(Z)
    perm = np.random.default_rng(0).permutation(N)
    fit_idx, work_idx = perm[:10000], perm[10000:]

    means_all = patch_means(X)
    edges = fit_edges(means_all[fit_idx])
    codes_work = codes_from(means_all[work_idx], edges)
    Zw = Z[work_idx]

    # cache pixel matrices for accumulation (per-patch 49-pixel columns)
    def pixel_matrix(Xsub):
        N2 = Xsub.shape[0]
        M = np.empty((N2, GRID*GRID, PS*PS))
        p = 0
        for gi in range(GRID):
            for gj in range(GRID):
                M[:, p, :] = Xsub[:, gi*PS:(gi+1)*PS, gj*PS:(gj+1)*PS].reshape(N2, -1)
                p += 1
        return M
    _ACC_CACHE["Xwork_means_by_pixel"] = pixel_matrix(X[work_idx])
    _ACC_CACHE["Xfit_means_by_pixel"] = pixel_matrix(X[fit_idx])
    _ACC_CACHE["pix_perm"] = np.random.default_rng(1).permutation(PS*PS)
    _ACC_CACHE["work_class_mask"] = lambda classes: np.isin(Zw, classes)

    results = {"protocol": dict(fit_n=len(fit_idx), work_n=len(work_idx),
                                grid=GRID, patch=PS, k=K, B=NB_BOOT,
                                per_class_work=np.bincount(Zw).tolist())}
    eps_bar = 0.02  # conservative TV concentration budget at n~6k, k=4 (Lemma 3.1)

    # ---- E1 ----
    print("\n=== E1 ===")
    E1 = {}
    # identity (all 10 classes)
    E1["identity"] = run_E1(codes_work, Zw, "identity", list(range(10)),
                            list(range(10)), 10)
    # 3v5 and 4v9 (restrict domain to the two classes)
    for name, cls in [("3v5", [3, 5]), ("4v9", [4, 9])]:
        cw, zc = restrict(codes_work, Zw, cls)
        # accumulation cache mask must match restricted order:
        _ACC_CACHE["work_class_mask"] = (lambda classes=cls: np.isin(Zw, classes))
        E1[name] = run_E1(cw, zc, name, [0, 1], cls, 2)
    results["E1"] = E1
    for name, r in E1.items():
        print(f"[{name}] J={r['J']} (target {r['J_target']}, coarsened={r['coarsened']}) "
              f"patches={r['selected_patches']} I_joint={r['I_joint']:.4f} "
              f"CI={_fmt(r['I_joint_ci'])}")
        for row in r["table"]:
            print(f"    b={row['b']} I_sep={row['I_sep']:.4f} {_fmt(row['I_sep_ci'])} "
                  f"Delta={row['Delta']:+.4f}")
        a = r["accumulation"]
        print(f"    accumulation patch {a['patch']}: I_A={a['I_A']:.4f} I_B={a['I_B']:.4f} "
              f"I_joint={a['I_joint']:.4f} gain={a['gain']:+.4f}")

    # ---- E2 ----
    print("\n=== E2 ===")
    E2 = {}
    for name, cls in [("3v5", [3, 5]), ("4v9", [4, 9])]:
        cw, zc = restrict(codes_work, Zw, cls)
        # pick two adjacent informative patches by single-view info
        pr = np.bincount(zc, minlength=2) / len(zc)
        sv = single_view_infos(cw, zc, pr, [0, 1], 2)
        top = [p for p, _ in sorted(sv.items(), key=lambda kv: -kv[1])]
        pair = pick_adjacent_pair(top)
        E2[name] = run_E2(cw, zc, pair, name, eps_bar)
        r = E2[name]
        print(f"[{name}] pair={r['pair']} I_joint={r['I_joint']:.4f} I_min={r['I_min']:.4f} "
              f"C_fine={r['C_fine']:.4f} CI_coarse={r['CI_coarse']:.4f} "
              f"maxI_v={r['max_I_v']:.4f} nu_delta={r['nu_delta']:.4f} "
              f"graded={r['half_gap_graded']}")
    results["E2"] = E2

    # ---- E3 ----
    print("\n=== E3 ===")
    E3 = {}
    for name, cls in [("3v5", [3, 5]), ("4v9", [4, 9])]:
        cw, zc = restrict(codes_work, Zw, cls)
        pr = np.bincount(zc, minlength=2) / len(zc)
        sv = single_view_infos(cw, zc, pr, [0, 1], 2)
        patch = max(sv, key=sv.get)
        E3[name] = run_E3(cw, zc, patch, name, [0, 1], 2)
        r = E3[name]
        print(f"[{name}] patch={r['patch']} d0(TV)={r['d0']:.4f} d(L1)={r['d_L1']:.4f} "
              f"eps*={r['eps_star']:.4f} empirical_zero={r['eps_zero_empirical']:.4f} "
              f"(I={r['I_at_empirical_zero']:.4f})")
        for row in r["blind"]:
            print(f"    blind eps={row['eps']:.2f} I_meas={row['I_meas']:.4f} "
                  f"I_pred={row['I_pred']:.4f} tv_meas={row['tv_meas']:.4f} "
                  f"tv_pred={row['tv_pred']:.4f}")
        for row in r["targeted"]:
            print(f"    targeted eps={row['eps']:.4f} I={row['I']:.4f} tv={row['tv']:.4f}")
    results["E3"] = E3

    with open("results/mnist_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nwrote results/mnist_results.json")


def pick_adjacent_pair(top_patches):
    """Return the two most-informative patches that are grid-adjacent, else top-2."""
    pos = {p: (p // GRID, p % GRID) for p in range(GRID * GRID)}
    for i in range(len(top_patches)):
        for j in range(i + 1, len(top_patches)):
            a, b = top_patches[i], top_patches[j]
            (ra, ca), (rb, cb) = pos[a], pos[b]
            if abs(ra - rb) + abs(ca - cb) == 1:
                return (a, b)
    return (top_patches[0], top_patches[1])


def _fmt(ci):
    return f"[{ci[0]:.4f},{ci[1]:.4f}]"


if __name__ == "__main__":
    main()
