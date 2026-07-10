"""ri_pid.py — Le Cam synergy and the PID experiment suite.
S_delta(T; Y1, Y2) = deficiency of the conditional-independence surrogate for
the actual joint experiment about T. Prior-free (deficiency's sup ranges over
priors and losses). Companion Shannon shadow S_I; comparisons: BROJA-CI (via
the coarse-fiber minimizer of ri_pilot) and whole-minus-sum (co-information).
"""
import os, sys
import numpy as np
from math import log2
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from ri_pilot import deficiency, q_info, fiber_min_I, mi_from_channel

RNG = np.random.default_rng(11)

# ---------- gates as joint pmfs p[t, y1, y2] ----------
def gate(name, eps=0.2):
    p = np.zeros((2, 2, 2))
    if name == "XOR":
        for y1 in (0,1):
            for y2 in (0,1): p[y1^y2, y1, y2] = .25
    elif name == "AND":
        for y1 in (0,1):
            for y2 in (0,1): p[y1&y2, y1, y2] = .25
    elif name == "RDN":
        p[0,0,0] = p[1,1,1] = .5
    elif name == "UNQ":
        for t in (0,1):
            for y2 in (0,1): p[t,t,y2] = .25
    elif name == "EPS":   # T-blind marginals; coupling correlated at eps iff T=0
        for y1 in (0,1):
            for y2 in (0,1):
                p[0,y1,y2] = (1+eps)/8 if y1==y2 else (1-eps)/8
                p[1,y1,y2] = 1/8
    return p

def channels(p):
    """(E_P, E_CI, per-source channels, prior) from joint pmf."""
    pt = p.sum((1,2)); nz = pt > 0
    P_joint = (p / pt[:,None,None]).reshape(2, 4).T          # 4 x |T|
    P1 = (p.sum(2) / pt[:,None]).T                            # 2 x |T|
    P2 = (p.sum(1) / pt[:,None]).T
    E_CI = np.einsum('at,bt->abt', P1, P2).reshape(4, 2)
    return P_joint, E_CI, P1, P2, pt

def S_delta(p):
    E_P, E_CI, *_ = channels(p)
    return deficiency(E_CI, E_P)

def S_I(p):
    E_P, E_CI, _, _, pt = channels(p)
    q = [0,1]
    return q_info(E_P, pt, q) - q_info(E_CI, pt, q)

def broja_CI(p):
    E_P, _, P1, P2, pt = channels(p)
    return max(0.0, q_info(E_P, pt, [0,1]) - fiber_min_I(P1, P2, pt))

def whole_minus_sum(p):
    E_P, _, P1, P2, pt = channels(p)
    q = [0,1]
    return q_info(E_P, pt, q) - q_info(P1, pt, q) - q_info(P2, pt, q)

# ---------- estimation ----------
def sample(p, n):
    flat = p.ravel(); idx = RNG.choice(8, n, p=flat)
    return np.stack([idx>>2 & 1, idx>>1 & 1, idx & 1], 1)   # t, y1, y2

def estimate_joint(data, alpha=0.5):
    p = np.full((2,2,2), alpha)
    for t,a,b in data: p[t,a,b] += 1
    return p / p.sum()

def S_delta_hat(data): return S_delta(estimate_joint(data))
def S_I_hat(data):     return S_I(estimate_joint(data))
