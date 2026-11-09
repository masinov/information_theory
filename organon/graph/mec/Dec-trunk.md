---
id: mec/Dec-trunk
type: decision
role: decision
title: Trunk and branches for C
status: taken
by: both
basis: method
about: [C]
layer: 2
since: 2026-10-23
where: 5
order: 51
---
Keep the dependence in C primitive (C-prim) and characterize it by its properties, instead of choosing one analysis of it; keep every compatible analysis open as a branch.

## Reasons
The author's image: at the base of a tree we know the trunk, roots and branches, but not where the fruit is; a conflict may show only far along a branch. A primitive with stated properties is not a rival to the analyses but what they share, so keeping it primitive keeps the branches open. Claude had first recommended choosing generic dependence over capacities; the author asked why one must choose, and the answer is that one need not.

## Correction recorded
Claude first claimed singularism follows from Reading A. It does not: Reading A excludes non-actual alternatives, not other actual instances. Hence C-local (what does follow) and the pair B-single / B-reg.
