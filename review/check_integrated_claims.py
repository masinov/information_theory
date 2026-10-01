"""Finite checks for Appendix D.8-D.13; run with system Python 3.

Uses the independently implemented partition and LP helpers from this review,
not the companion papers' research solvers. General claims rest on proofs.
"""
import itertools as it
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from check_finite_claims import parts, meet, join, leq, sat


def component_sets(n, edges):
    remaining = set(range(n))
    out = []
    while remaining:
        found = {next(iter(remaining))}
        while True:
            enlarged = found | {b for a, b in edges if a in found} | {a for a, b in edges if b in found}
            if enlarged == found:
                break
            found = enlarged
        out.append(frozenset(found))
        remaining -= found
    return frozenset(out)


def check_sites():
    ps = list(parts(3))
    checked = 0
    for mask in range(1, 1 << len(ps)):
        lattice = [p for i, p in enumerate(ps) if mask & (1 << i)]
        family = set(lattice)
        if not all(meet(a, b) in family and join(a, b) in family for a, b in it.product(lattice, repeat=2)):
            continue
        distributive = all(meet(c, join(a, b)) == join(meet(c, a), meet(c, b))
                           for a, b, c in it.product(lattice, repeat=3))
        stable = True
        for cover_mask in range(1, 1 << len(lattice)):
            cover = [p for i, p in enumerate(lattice) if cover_mask & (1 << i)]
            top = cover[0]
            for p in cover[1:]:
                top = join(top, p)
            for y in lattice:
                if leq(y, top):
                    pulled = meet(cover[0], y)
                    for p in cover[1:]:
                        pulled = join(pulled, meet(p, y))
                    stable &= pulled == y
        assert stable == distributive
        checked += 1
    a, b, c = (0, 0, 1), (0, 1, 0), (0, 1, 1)
    assert join(a, b) == (0, 1, 2)
    assert join(meet(a, c), meet(b, c)) != c
    return checked


def check_commuting_extractions():
    ps = list(parts(4))
    subsets = [{i for i in range(4) if mask & (1 << i)} for mask in range(16)]
    checked = 0
    for a, b in it.product(ps, repeat=2):
        c = meet(a, b)
        ablocks = [{i for i in range(4) if a[i] == label} for label in set(a)]
        bblocks = [{i for i in range(4) if b[i] == label} for label in set(b)]
        rectangular = all(bool(x & y) for x, y in it.product(ablocks, bblocks)
                          if c[next(iter(x))] == c[next(iter(y))])
        commute = all(sat(a, sat(b, e)) == sat(b, sat(a, e)) for e in subsets)
        meet_law = all(sat(a, sat(b, e)) == sat(c, e) and sat(b, sat(a, e)) == sat(c, e)
                       for e in subsets)
        assert rectangular == commute == meet_law
        checked += 1
    return checked


def check_cuts():
    edges = list(it.combinations(range(4), 2))
    checked = 0
    for states in it.product(range(3), repeat=len(edges)):
        # 0: absent, 1: deleted, 2: retained.
        h = {edge for edge, state in zip(edges, states) if state}
        j = {edge for edge, state in zip(edges, states) if state == 2}
        hc, jc = component_sets(4, h), component_sets(4, j)
        cut = False
        for component in hc:
            vertices = sorted(component)
            for mask in range(1, (1 << len(vertices))-1):
                a = {v for i, v in enumerate(vertices) if mask & (1 << i)}
                crossing = {e for e in h if e[0] in component and ((e[0] in a) != (e[1] in a))}
                if crossing and not (crossing & j):
                    cut = True
        assert (hc != jc) == cut
        checked += 1
    return checked


def check_propagation():
    pairs = list(it.product(range(2), repeat=2))
    constraints = [{p for i, p in enumerate(pairs) if mask & (1 << i)} for mask in range(16)]
    checked = 0
    # Three bags {0,1}, {1,2}, {2,3}; root is the middle bag.
    for left, middle, right in it.product(constraints, repeat=3):
        left_message = {b for a, b in left}
        right_message = {a for a, b in right}
        local = {(b, c) for b, c in middle if b in left_message and c in right_message}
        exhaustive = {(b, c) for a, b, c, d in it.product(range(2), repeat=4)
                      if (a, b) in left and (b, c) in middle and (c, d) in right}
        assert local == exhaustive
        checked += 1
    # Empty separator: impossible component must send the empty relation.
    for left in (set(), {0}, {1}, {0, 1}):
        for right in (set(), {0}, {1}, {0, 1}):
            message = {()} if left else set()
            root = right if message else set()
            assert root == {b for a, b in it.product(left, right)}
    return checked


def check_witness_hierarchy():
    checked = 0
    for n in range(2, 6):
        # Candidate i in the first or second orbit; view m splits only pair m.
        def value(i, side, view):
            return (i, side if i == view else 2)
        for mask in range(1 << n):
            context = [v for v in range(n) if mask & (1 << v)]
            actual = {(i, j) for i in range(n) for j in range(n)
                      if all(value(i, 0, v) == value(j, 1, v) for v in context)}
            expected = ({(i, i) for i in range(n) if i not in context}
                        if context else set(it.product(range(n), repeat=2)))
            assert actual == expected
            assert bool(actual) == (len(context) < n)
            checked += 1
    return checked


def check_coherence_counterexample():
    states = list(it.product(range(2), repeat=2))
    # Uniform global distribution yields uniform coordinate marginals.
    assert all(sum(z[k] == bit for z in states) == 2 for k in (0, 1) for bit in (0, 1))
    orbits = [[z for z in states if (z[0] ^ z[1]) == parity] for parity in (0, 1)]
    witnesses = [{(a, b) for a in orbits[0] for b in orbits[1] if a[k] == b[k]} for k in (0, 1)]
    assert all(witnesses) and not set.intersection(*witnesses)
    return True


if __name__ == '__main__':
    results = {
        'scope': 'Exhaustive finite instances supplement Appendix D proofs.',
        'join_cover_sublattices': check_sites(),
        'graph_cut_pairs': check_cuts(),
        'commuting_extraction_partition_pairs': check_commuting_extractions(),
        'constraint_tree_configurations': check_propagation(),
        'globally_coherent_witness_anomaly': check_coherence_counterexample(),
        'witness_hierarchy_contexts': check_witness_hierarchy(),
    }
    Path(__file__).with_name('integrated-check-results.json').write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps(results, indent=2))
