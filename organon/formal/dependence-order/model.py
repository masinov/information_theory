"""Exhaustive search over binary relations on n contrasts (protocol method/T-formal).

D(x, y) reads: contrast x holds at least partly in virtue of contrast y.
Run: python model.py > output.txt
"""
from itertools import product


def relations(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for bits in product((0, 1), repeat=len(pairs)):
        yield {p for p, b in zip(pairs, bits) if b}


def asymmetric(r):
    return all((y, x) not in r for (x, y) in r)


def irreflexive(r):
    return all(x != y for (x, y) in r)


def transitive(r):
    return all((x, w) in r for (x, y) in r for (z, w) in r if y == z)


def closure(r, n):
    c = set(r)
    changed = True
    while changed:
        changed = False
        for (x, y) in list(c):
            for (z, w) in list(c):
                if y == z and (x, w) not in c:
                    c.add((x, w))
                    changed = True
    return c


def has_loop(r, n):
    return any((x, x) in closure(r, n) for x in range(n))


def main():
    for n in range(1, 5):
        total = asym = asym_refl = asym_loop = asym_trans = asym_trans_loop = 0
        first_loop = None
        for r in relations(n):
            total += 1
            if not asymmetric(r):
                continue
            asym += 1
            if not irreflexive(r):
                asym_refl += 1
            if has_loop(r, n):
                asym_loop += 1
                if first_loop is None:
                    first_loop = sorted(r)
            if transitive(r):
                asym_trans += 1
                if has_loop(r, n):
                    asym_trans_loop += 1
        print(f'n={n}: relations={total} asymmetric={asym}')
        print(f'  asymmetric but something holds in virtue of itself: {asym_refl}')
        print(f'  asymmetric with a loop: {asym_loop}' + (f'  e.g. {first_loop}' if first_loop else ''))
        print(f'  asymmetric and transitive: {asym_trans}, of which with a loop: {asym_trans_loop}')

    # One field bearing two contrasts, one registering the other: K1 in virtue of K0, both borne by field f.
    r = {(1, 0)}
    print('own contrast: D(K1,K0), both borne by one field; asymmetric:', asymmetric(r), 'irreflexive:', irreflexive(r))

    # Indiscriminate registration along a chain K2 -> K1 -> K0.
    chain = {(2, 1), (1, 0)}
    print('chain without transitivity: K2 registers K0?', (2, 0) in chain)
    print('chain with transitivity:    K2 registers K0?', (2, 0) in closure(chain, 3))


if __name__ == '__main__':
    main()
