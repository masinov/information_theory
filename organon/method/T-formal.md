---
id: method/T-formal
since: 2026-10-23
type: method
role: protocol
title: Countermodel search
status: in-force
cites: [oppenheimer2011, benzmuller2014]
order: 75
---
Formalize a claim of entailment or necessity and search mechanically for a countermodel.

## Procedure
Write the premises and the conclusion in a formal language. Run a model finder (for instance Z3 or Alloy) for structures satisfying the premises and not the conclusion, up to a stated size. Record every alternative formalization considered: finding that a sentence can be formalized in two ways is often the main result.

## Record
The encoding and output in formal/, and a test entry with the result and its size bound.
