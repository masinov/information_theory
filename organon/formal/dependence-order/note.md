# Asymmetry, transitivity and loops of dependence

Test entry: `mec/Test-formal-dep`. Protocol: `method/T-formal`.

- **Encoding**: `model.py`. One relation D(x, y): contrast x holds at least partly in virtue of
  contrast y. Exhaustive search over every binary relation on 1 to 4 contrasts.
- **Command**: `python model.py > output.txt`
- **Output**: `output.txt`

## What was asked
1. Does asymmetry (mec/C-asym) entail that nothing holds in virtue of itself? Yes, no countermodel.
2. Does asymmetry exclude loops through a third contrast? No: from three contrasts on there are
   asymmetric relations with a loop.
3. Does asymmetry with transitivity exclude loops? Yes, no countermodel; the relation is then a strict
   partial order.
4. Can one field register one of its own contrasts through a second contrast? Yes, consistently.
5. Does a contrast register what the registered contrast itself depends on? Only if the dependence is
   transitive.

## Alternative formalizations considered
- Two relations, "partly" and "wholly in virtue of". Not run: since the repairs of 2026-11-10 the core
  uses only "at least partly".
- Fields as a labelling of contrasts only. The core says nothing about how fields are individuated,
  so no constraint on the labelling was imposed.

## Limits
A search of this kind checks the form of the conditions, not whether any dependence in any domain
satisfies them.
