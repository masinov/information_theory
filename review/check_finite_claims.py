"""Independent finite checks for the 2026-10-01 mathematical review.

Run: /usr/bin/python3 docs/information_theory/review/check_finite_claims.py
Requires numpy/scipy. No imports from the research implementation, no network.
Numerical checks supplement the proofs; they are not universal proofs.
"""
import itertools as it
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def parts(n):
    def visit(a):
        if len(a) == n:
            yield tuple(a)
        else:
            for k in range(max(a, default=-1) + 2):
                yield from visit(a + [k])
    yield from visit([])


def canon(a):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in a)


def join(a, b):
    return canon(list(zip(a, b)))


def meet(a, b):
    root = list(range(len(a)))
    def find(i):
        while root[i] != i:
            i = root[i]
        return i
    for i, j in it.combinations(range(len(a)), 2):
        if a[i] == a[j] or b[i] == b[j]:
            root[find(i)] = find(j)
    return canon([find(i) for i in range(len(a))])


def leq(a, b):
    return all(b[i] != b[j] or a[i] == a[j]
               for i, j in it.combinations(range(len(a)), 2))


def sat(p, e):
    labels = {p[i] for i in e}
    return frozenset(i for i, x in enumerate(p) if x in labels)


def channel(p):
    return np.eye(max(p)+1)[list(p)]  # state x outcome, unlike ri_pilot


def deficiency(e, f):
    """Row-stochastic independent LP; return value and primal residual."""
    nz, ne = e.shape
    assert nz == f.shape[0]
    nf = f.shape[1]
    nm = ne*nf
    size = nm + nz*nf + 1
    objective = np.zeros(size)
    objective[-1] = 1
    eq, rhs = [], []
    for x in range(ne):
        row = np.zeros(size)
        row[x*nf:(x+1)*nf] = 1
        eq.append(row)
        rhs.append(1)
    ub, bounds = [], []
    for z in range(nz):
        for y in range(nf):
            for sign in (-1, 1):
                row = np.zeros(size)
                row[y:nm:nf] = sign*e[z]
                row[nm+z*nf+y] = -1
                ub.append(row)
                bounds.append(sign*f[z, y])
        row = np.zeros(size)
        row[nm+z*nf:nm+(z+1)*nf] = .5
        row[-1] = -1
        ub.append(row)
        bounds.append(0)
    res = linprog(objective, A_ub=ub, b_ub=bounds, A_eq=eq, b_eq=rhs,
                  bounds=[(0, None)]*size, method='highs')
    assert res.success, res.message
    m = res.x[:nm].reshape(ne, nf)
    actual = np.abs(e @ m-f).sum(axis=1).max()/2
    assert actual <= res.fun + 1e-8
    assert np.max(np.abs(m.sum(axis=1)-1)) < 1e-8
    return float(res.fun)


def info(p, prior):
    m = prior @ p
    total = 0.
    for z, y in it.product(range(len(prior)), range(p.shape[1])):
        if p[z, y] > 0:
            total += prior[z]*p[z, y]*np.log2(p[z, y]/m[y])
    return float(total)


def close(x, y):
    assert abs(x-y) < 1e-8, (x, y)


def main():
    out = {'scope': 'Finite examples and exhaustive small-domain checks; not a proof assistant.'}
    pp = list(parts(4))
    subsets = [frozenset(i for i in range(4) if mask & (1 << i)) for mask in range(16)]
    count = 0
    for a, b in it.product(pp, repeat=2):
        assert leq(a, join(a, b)) and leq(meet(a, b), a)
        for e, f in it.product(subsets, repeat=2):
            assert sat(a, e & sat(a, f)) == sat(a, e) & sat(a, f)
            if leq(a, b):
                assert sat(a, sat(b, e)) == sat(a, e)
            count += 1
    out['saturation_checks'] = count

    # Ach has two incomparable supporting labels but no least one.
    a, b = (0, 0, 1, 2), (0, 1, 1, 2)
    ach = {(0,)*4, a, b, join(a, b)}
    assert meet(a, b) == (0, 0, 0, 1) and meet(a, b) not in ach
    e = frozenset({3})
    supports = [p for p in ach if sat(p, e) == e]
    assert not any(all(leq(p, q) for q in supports) for p in supports)
    out['no_least_achievable_support'] = {'a': a, 'b': b, 'ambient_meet': meet(a, b), 'piece': [3]}

    p, q = (0, 0, 1), (0, 1, 1)
    assert sat(p, sat(q, {0})) != sat(q, sat(p, {0}))
    out['noncommuting_focusing'] = True

    # Exhaustively verify all exact interval deficiencies through four states.
    exact = 0
    for n in range(1, 5):
        ps = list(parts(n))
        for a, b in it.product(ps, repeat=2):
            if leq(a, b):
                k = max(len({b[i] for i in range(n) if a[i] == label}) for label in set(a))
                close(deficiency(channel(a), channel(b)), 1-1/k)
                exact += 1
    out['partition_formula_lp_checks'] = exact
    e0, em, ef = channel((0, 0, 0)), channel((0, 1, 1)), np.eye(3)
    out['triangle'] = [deficiency(e0, em), deficiency(em, ef), deficiency(e0, ef)]

    n = np.array([[.7, .3], [.3, .7]])
    nn = np.array([np.kron(row, row) for row in n])
    out['bsc_03_replication'] = deficiency(n, nn)
    close(out['bsc_03_replication'], .084)
    close(deficiency(nn, n), 0)
    # Independent exact upper/lower certificates, Appendix B.6.
    simulator = np.array([[.58, .21, .21, 0], [0, .21, .21, .58]])
    upper = np.abs(n @ simulator - nn).sum(axis=1).max()/2
    prior = np.array([.3, .7])
    risk_one = np.min(prior[:, None]*n, axis=0).sum()
    risk_two = np.min(prior[:, None]*nn, axis=0).sum()
    close(upper, .084)
    close(risk_one-risk_two, .084)
    out['bsc_03_certificate'] = {'simulator_upper': float(upper),
                               'decision_lower': float(risk_one-risk_two)}

    # Partial replacement with positive no-intrusion mass preserves certainty.
    d = .2
    erasure = np.array([[1-d, 0, d], [0, 1-d, d]])
    double = np.array([np.kron(row, row) for row in erasure])
    anti = np.zeros((2, 9))
    for z in range(2):
        anti[z, 3*z+z] = 1-2*d
        anti[z, 3*z+2] = anti[z, 6+z] = d
    close(deficiency(anti, np.eye(2)), 0)
    close(deficiency(double, anti), d*d/2)
    out['selective_replacement_counterexample'] = True

    # Binary antichain admits a common upper bound; source theorem supplies leastness.
    pair = np.array([[.5, 0, 0, .5], [.25, .25, .25, .25]])
    mirror = pair[::-1]
    out['binary_mirror_deficiencies'] = [deficiency(pair, mirror), deficiency(mirror, pair)]

    # Gate and small-signal laws independently checked.
    and_joint = np.array([[1/3, 1/3, 1/3, 0], [0, 0, 0, 1]])
    and_ci = np.array([[4/9, 2/9, 2/9, 1/9], [0, 0, 0, 1]])
    close(deficiency(and_ci, and_joint), .1)
    out['and_synergy'] = .1
    eps_rows = []
    for eps in (.1, .2, .4):
        p = np.array([[(1+eps)/4, (1-eps)/4, (1-eps)/4, (1+eps)/4], [.25]*4])
        ci = np.full((2, 4), .25)
        sd, si = deficiency(ci, p), info(p, np.array([.5, .5]))
        close(sd, eps/4)
        eps_rows.append({'eps': eps, 'S_delta': sd, 'S_I': si, 'ratio': si/eps**2})
    out['epsilon_family'] = eps_rows

    # Policy exhibit 76.2, all four memoryless policies and adaptive one.
    states = list(it.product((1, 2), (0, 1), (0, 1)))
    orbit = canon([(k, b1 ^ b2) for k, b1, b2 in states])
    base = canon([(k, b1) for k, b1, b2 in states])
    contexts = [int((k == 1 and b2 == 1) or (k == 2 and b1 == 0)) for k, b1, b2 in states]
    target = [b1 ^ b2 for k, b1, b2 in states]
    def policy_value(verdict):
        ceiling = meet(orbit, join(base, canon(verdict)))
        law = np.zeros((2, max(ceiling)+1))
        for z, block in enumerate(ceiling):
            law[target[z], block] += .25
        return info(law, np.array([.5, .5]))
    frontier = []
    for pol in it.product((0, 1), repeat=2):
        v = [pol[c] for c in contexts]
        frontier.append([sum(v)/8, policy_value(v)])
    adaptive = [int(k == 1 and c == 1) for (k, _, _), c in zip(states, contexts)]
    close(policy_value(adaptive), .5)
    close(sum(adaptive)/8, .25)
    out['memoryless_frontier'] = frontier
    out['adaptive_point'] = [.25, .5]

    # A zero witness interval can hide a missing edge and a nontrivial nerve.
    # Two views on three 2-point orbits. Edges AB and BC have common witnesses;
    # AC has one witness per view, but none jointly.
    orbit = (0, 0, 1, 1, 2, 2)
    v = (0, 1, 0, 2, 2, 1)  # a0=b0, b1=c0, a1=c1
    w = (0, 1, 0, 1, 1, 2)  # a0=b0, b1=c0=a1
    # Seek an exhibit by enumeration if this simple candidate has extra witnesses.
    def edges(p):
        return {(orbit[i], orbit[j]) for i, j in it.combinations(range(6), 2)
                if orbit[i] != orbit[j] and p[i] == p[j]}
    def comp(edgeset):
        p = tuple(range(3))
        for i, j in edgeset:
            edge = list(range(3)); edge[j] = edge[i]
            p = meet(p, canon(edge))
        return p
    found = None
    for a, b in it.product(parts(6), repeat=2):
        inter = edges(a) & edges(b)
        joint = edges(join(a, b))
        if inter != joint and comp(inter) == comp(joint):
            found = {'v': a, 'w': b, 'intersection_edges': sorted(inter), 'joint_edges': sorted(joint)}
            break
    assert found
    out['absorbed_witness_edge'] = found

    for prob in (0, .1, .5, .9, 1):
        honest = np.array([.5, 0, 0, .5])
        forged = np.kron([.5, .5], [prob, 1-prob])
        close(np.abs(honest-forged).sum()/2, .5)
        assert np.sqrt(honest*forged).sum() <= 2**-.5 + 1e-12
    out['committed_detection_minimax_risk_n20'] = 2**-21

    path = Path(__file__).with_name('finite-check-results.json')
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
