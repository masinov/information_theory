"""ri_pilot.py — reference implementation of the Registered Information pilot.
Contrast domain = classes; views = quantized statistics as estimated channels.
Implements: channel estimation with hygiene, Shannon/enriched evaluations,
fine-ledger fiber minimization + coarse-ledger BROJA (Prop 55.4), corruption
operators with the closed-form laws (Lemma 62.1, Thm 62.2), bootstrap CIs,
refusal rule, and the Synth-8 planted-ground-truth validation (design §6)."""
import numpy as np
from scipy.optimize import linprog, minimize
from math import log2

RNG = np.random.default_rng(0)
H = lambda p: -sum(x*log2(x) for x in np.ravel(p) if x > 1e-12)
h2 = lambda p: 0.0 if p in (0, 1) else -p*log2(p)-(1-p)*log2(1-p)

# ---------- estimation with hygiene ----------
def estimate_channel(codes, labels, k, n_class, alpha=0.5):
    """Laplace-smoothed P_hat[y|z]; returns (k x nZ) column-stochastic."""
    P = np.full((k, n_class), alpha)
    for c, z in zip(codes, labels): P[c, z] += 1
    return P / P.sum(0, keepdims=True)

def mi(joint):
    """I(Z;Y) in bits, plug-in on the (smoothed) joint p(z,y); bias is handled
    by smoothing + bootstrap here — add Miller–Madow (+(K-1)/(2n ln2)) at pilot
    scale where raw counts are available, per design §4."""
    pz, py = joint.sum(1), joint.sum(0)
    I = H(pz) + H(py) - H(joint)
    return I

def mi_from_channel(P, prior):
    joint = P * prior[None, :]      # p(y,z)
    return mi(joint.T)

def refusal(n_class_counts, joint_alphabet, factor=20):
    return n_class_counts.min() >= factor * joint_alphabet

# ---------- enriched rung: deficiency LP (Part IX §68, Appendix B.1) ----------
def deficiency(E, F):
    nE, nZ = E.shape; nF = F.shape[0]
    nM, nU = nF*nE, nZ*nF
    c = np.zeros(nM+nU+1); c[-1] = 1.0
    A_ub, b_ub = [], []
    for z in range(nZ):
        for y in range(nF):
            for sgn in (1, -1):
                row = np.zeros(nM+nU+1)
                row[[y*nE+x for x in range(nE)]] = sgn*E[:, z]
                row[nM+z*nF+y] = -1.0
                A_ub.append(row); b_ub.append(sgn*F[y, z])
        row = np.zeros(nM+nU+1); row[nM+z*nF:nM+(z+1)*nF] = 0.5; row[-1] = -1.0
        A_ub.append(row); b_ub.append(0.0)
    A_eq = [np.concatenate([np.eye(nE)[x].repeat(nF).reshape(nE,-1).T.ravel(), np.zeros(nU+1)]) for x in range(nE)]
    # column-stochastic constraint rebuilt explicitly:
    A_eq = []
    for x in range(nE):
        row = np.zeros(nM+nU+1)
        for y in range(nF): row[y*nE+x] = 1.0
        A_eq.append(row)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.ones(nE),
                  bounds=[(0, None)]*(nM+nU)+[(None, None)], method='highs')
    return res.fun

# ---------- E2: fiber minimization (fine ledger) & BROJA (coarse) ----------
def fiber_min_I(Pv, Pw, prior):
    """min over couplings Q_z of the per-class marginals (Pv[:,z], Pw[:,z]) of
    I(Z; Yv,Yw). Convex in the joint channel; SLSQP over transportation polytopes."""
    kv, nZ = Pv.shape; kw = Pw.shape[0]
    dim = kv*kw
    def unpack(x): return x.reshape(nZ, kv, kw)
    def obj(x):
        Q = np.clip(unpack(x), 1e-12, 1)
        joint = (Q * prior[:, None, None]).reshape(nZ, dim)   # p(z, y)
        return mi(joint)
    cons = []
    for z in range(nZ):
        for a in range(kv):
            cons.append({'type': 'eq',
                'fun': (lambda x, z=z, a=a: unpack(x)[z, a, :].sum() - Pv[a, z])})
        for b in range(kw-1):
            cons.append({'type': 'eq',
                'fun': (lambda x, z=z, b=b: unpack(x)[z, :, b].sum() - Pw[b, z])})
    x0 = np.einsum('az,bz->zab', Pv, Pw).ravel()              # CI coupling start
    best = None
    for x_init in [x0, x0*0.5 + 0.5*RNG.dirichlet(np.ones(dim), nZ).ravel()]:
        r = minimize(obj, x_init, constraints=cons, bounds=[(0,1)]*(nZ*dim),
                     method='SLSQP', options={'maxiter': 300, 'ftol': 1e-10})
        if r.success and (best is None or r.fun < best): best = r.fun
    return best

def ledger_table(Pv, Pw, Pjoint, prior, q_of_z):
    """Fine-ledger C, coarse-ledger CI (BROJA via Prop 55.4), residual, baselines."""
    I_joint = mi_from_channel(Pjoint, prior)
    I_min = fiber_min_I(Pv, Pw, prior)
    C_fine = max(0.0, I_joint - I_min)
    # coarse ledger: q-marginalized family (prior-averaged channels given q)
    qs = sorted(set(q_of_z)); nq = len(qs)
    prior_q = np.array([prior[[q_of_z[z]==qv for z in range(len(prior))]].sum() for qv in qs])
    def marg(P):
        M = np.zeros((P.shape[0], nq))
        for j, qv in enumerate(qs):
            w = np.array([prior[z] if q_of_z[z]==qv else 0 for z in range(len(prior))])
            M[:, j] = P @ (w/w.sum())
        return M
    Pv_q, Pw_q, Pj_q = marg(Pv), marg(Pw), marg(Pjoint)
    CI_coarse = max(0.0, mi_from_channel(Pj_q, prior_q) - fiber_min_I(Pv_q, Pw_q, prior_q))
    return dict(I_joint=I_joint, I_min=I_min, C_fine=C_fine, CI_coarse=CI_coarse,
                I_v=mi_from_channel(Pv, prior), I_w=mi_from_channel(Pw, prior))

# ---------- E3: corruption operators and closed-form laws ----------
def blind_mix(P, eps, Q=None):
    Q = np.full(P.shape[0], 1/P.shape[0]) if Q is None else Q
    return (1-eps)*P + eps*Q[:, None]

def targeted_attack(P, prior, q_of_z, eps):
    """Lemma 62.1's optimal clutter (s^+/s^- construction) on class averages."""
    qs = sorted(set(q_of_z))
    w = [np.array([prior[z] if q_of_z[z]==qv else 0 for z in range(len(prior))]) for qv in qs]
    pbar = [P @ (wi/wi.sum()) for wi in w]
    s = (1-eps)/max(eps, 1e-9) * (pbar[0]-pbar[1])
    sp, sm = np.maximum(s, 0), np.maximum(-s, 0)
    if sp.sum() > 1:  # below threshold: best effort scaling (partial annihilation)
        sp, sm = sp/sp.sum(), sm/sm.sum()
    rest = 1 - sp.sum()
    rho = np.full(P.shape[0], 1/P.shape[0])
    Q = {qs[0]: sm + rest*rho, qs[1]: sp + rest*rho}
    Pt = P.copy()
    for z in range(P.shape[1]):
        Pt[:, z] = (1-eps)*P[:, z] + eps*Q[q_of_z[z]]
    return Pt

def q_info(P, prior, q_of_z):
    qs = sorted(set(q_of_z))
    joint = np.zeros((len(qs), P.shape[0]))
    for z in range(P.shape[1]):
        joint[qs.index(q_of_z[z])] += prior[z]*P[:, z]
    return mi(joint)

def q_tv(P, prior, q_of_z):
    qs = sorted(set(q_of_z))
    w = [np.array([prior[z] if q_of_z[z]==qv else 0 for z in range(len(prior))]) for qv in qs]
    pbar = [P @ (wi/wi.sum()) for wi in w]
    return 0.5*np.abs(pbar[0]-pbar[1]).sum()

# ---------- bootstrap ----------
def bootstrap_ci(fn, data, B=200, alpha=0.05):
    n = len(data[0]); vals = []
    for _ in range(B):
        idx = RNG.integers(0, n, n)
        vals.append(fn(*[d[idx] for d in data]))
    lo, hi = np.quantile(vals, [alpha/2, 1-alpha/2])
    return lo, hi

# ---------- Synth-8: planted ground truth (design §6) ----------
def synth8(n=40000):
    """Classes = (b1,b2,b3) uniform. Views:
    v1=b1 (det), v2=b2 (det)  -> parity transport plant;
    v3,v4 coupled pair on b3 per Prop 22.4(2): b3=0 -> equal fair coin, b3=1 -> indep;
    v5,v6 = independent BSC(0.15) looks at b1 (accumulation / corruption plants)."""
    Z = RNG.integers(0, 8, n)
    b = [(Z >> i) & 1 for i in range(3)]
    v1, v2 = b[0], b[1]
    coin = RNG.integers(0, 2, n); coin2 = RNG.integers(0, 2, n)
    v3 = coin
    v4 = np.where(b[2] == 0, coin, coin2)
    flip = lambda x: np.where(RNG.random(n) < 0.15, 1-x, x)
    v5, v6 = flip(b[0]), flip(b[0])
    return Z, dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5, v6=v6)
