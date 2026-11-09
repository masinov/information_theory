---
id: mec/Test-formal-dep
since: 2026-11-10
type: test
title: Asymmetry, transitivity and loops of dependence
status: run
protocol: method/T-formal
result: asymmetry alone admits loops; with transitivity none
about: [C-asym, F-transorder, Dec-indiscriminate, R]
order: 137
---
The properties of the dependence in C checked by exhaustive search over all binary relations on up to four contrasts (organon/formal/dependence-order/).

## Results
- Asymmetry entails that nothing holds in virtue of itself: no countermodel up to four contrasts.
- Asymmetry does not exclude loops through a third contrast: countermodels exist from three contrasts on (K1 → K2 → K3 → K1).
- Asymmetry with transitivity excludes every loop and gives a strict partial order: no countermodel up to four contrasts.
- A field registering one of its own contrasts through a second contrast is consistent with asymmetry.
- With transitivity, a contrast registers every contrast upstream of the one it depends on; without it, it need not.

## Alternative formalizations
One relation "holds at least partly in virtue of" was used. A second formalization with two relations (partly, wholly) was considered and not run: nothing in the core distinguishes them since Dec-repairs. Fields were modelled only as a labelling of contrasts, since the core says nothing about how fields are individuated.

## Size bound
All relations on 1 to 4 elements (65,536 at size 4).
