<!-- out: minimal_epistemic_core/commitments.md -->
# Register of commitments

This register lists everything the theory assumes, defines, or leaves open, one entry per item.
Each later paper adds its own entries in a new layer and cites the register for what it builds on.
A result in any layer should be traceable, through the **Requires** fields, to the entries it rests on.

The register is generated from the entries in `organon/graph/mec/` (one file per entry) and
`organon/method/`; the entry with id X is in the file `X.md` there.

**Entry kinds.**
*Premise*: the starting point that motivates the commitments.
*Commitment*: admitted, not derived; each must be argued for where it is introduced.
*Definition*: introduces a term in terms of existing entries; adds nothing new.
*Convention*: a feature of the presentation, not a claim about what is described.
*Exclusion*: a view the commitments rule out as a precondition of registration.
*Presupposition*: assumed by the text without being stated as a commitment; to be examined.
*Open*: a question the layer raises and does not answer.
*Consequence*: follows from the entries it requires; recorded so that it can be cited, adds nothing new.
*Branch*: a further analysis compatible with every entry it builds on; kept open, not adopted.
*Closed*: an analysis that contradicts an entry; recorded with the entry it contradicts.
*Decision*: a choice between readings, with its reasons and whether it rests on a claim or on method.
*Objection*: an attack on an entry, with its current status.
*Friction*: anything that blocks progress or prompts revision, with its kind, the entries between
which it arises, and how it was resolved, if it was (see `organon/method/schema.md`).

Section numbers refer to *A Minimal Epistemic Core* (`latex/epistemic_core.tex`).

---

## Method (all layers)

The method is itself a set of assumptions. It is recorded here so that it can be examined and
revised like any other entry, and so that a result can be checked for features that come from the
method rather than from what it describes. It applies to every investigation in the repository;
test protocols are in `organon/method/`.

### Rules

<!-- table filter="ns=method role=rule" ns="mec" cols="Id:id|Rule:statement" -->

### Methodological presuppositions

<!-- table filter="ns=method role=presupposition" ns="mec" cols="Id:id|Presupposition:statement|What it may cost:#Cost" -->

---

## Layer 1: the minimal epistemic core

### Question

<!-- table filter="ns=mec role=main" ns="mec" cols="Id:id!b|Question:statement|Notes:#Notes" -->

### Premise

<!-- table filter="ns=mec role=premise" ns="mec" cols="Id:id!b|Statement:statement|Notes:#Notes|§:where" -->

### Commitments

<!-- table filter="ns=mec layer=1 role=commitment" ns="mec" cols="Id:id!b|Statement:titled|Requires:requires|Does not establish:#Does not establish|§:where" -->

<!-- arguments filter="ns=mec type=argument" ns="mec" -->

### Definitions

<!-- table filter="ns=mec role=definition" ns="mec" empty="none" cols="Id:id|Term:title|Definition:statement|Requires:requires|§:where" -->

### Conventions

<!-- table filter="ns=mec role=convention" ns="mec" cols="Id:id|Convention:statement|§:where" -->

### Exclusions (as preconditions of registration)

<!-- table filter="ns=mec role=exclusion" ns="mec" cols="Id:id|Excluded view:statement|Excluded by:#Excluded by?excluded_by|§:where" -->

None of these denies that the excluded structures occur in particular epistemic relations; wherever
they are needed, they must enter as further commitments.

### Presuppositions (used but not yet stated as commitments)

These are assumed by the text of Layer 1 and are to be examined, accepted as commitments, or removed.

<!-- table filter="ns=mec role=presupposition" ns="mec" cols="Id:id|Presupposition:statement|Where it appears:where|Status:status" -->

### Open questions

<!-- table filter="ns=mec role=open" ns="mec" cols="Id:id|Question:statement|§:where" -->

### Decisions

<!-- table filter="ns=mec layer=1 type=decision" ns="mec" cols="Id:id|Decision:titled|Reasons:#Reasons|Basis (M4):basis" -->

### Dependencies

Each item, with the items it requires:

<!-- deps filter="ns=mec layer=1" ns="mec" -->

---

## Layer 2: ontology of the core

This layer examines the presuppositions of Layer 1, taking a position only where the core forces one.
It has no paper yet; § refers to the passage of Layer 1 it reads.

Layer 2 does not choose among analyses of the core's notions. It states what every analysis must
satisfy (the *trunk*) and keeps each compatible analysis open as a *branch*, following the rules
M1–M5 under **Method** above.

### The dependence in C: trunk

<!-- table filter="ns=mec layer=2 type=claim" ns="mec" cols="Id:id|Kind:role|Statement:titled|Requires:requires|§:where" -->

C-local leaves one question open: whether C in an instance can depend on *other actual instances*,
as in a pattern across cases. Reading A excludes alternatives, which are non-actual; other instances
are actual, so Reading A does not settle this. B-single and B-reg below answer it in opposite ways.

### The dependence in C: branches

<!-- table filter="ns=mec role=branch" ns="mec" cols="Id:id|Analysis:titled|Adds:#Adds|Compatible because:#Compatible because|Closed if:#Closed if" -->

### The dependence in C: closed

<!-- table filter="ns=mec role=closed" ns="mec" cols="Id:id|Analysis:statement|Contradicts:#Contradicts|Closed by (M4):#Closed by" -->

Closed analyses are closed *as analyses of C*. As in Layer 1, the structures they describe may enter
later layers as further commitments.

### Decisions

<!-- table filter="ns=mec layer=2 type=decision" ns="mec" cols="Id:id|Decision:titled|Reasons:#Reasons|Basis (M4):basis" -->

### Proposals

<!-- table filter="ns=mec role=proposal" ns="mec" cols="Id:id|Proposal:titled|Open:#Open|By:by|Status:status" -->

### Objections

<!-- table filter="ns=mec type=objection" ns="mec" cols="Id:id|Objection:titled|Attacks:attacks|Status:status" -->

### Tests

The first result expected to separate the branches is Q3: whether registration of *which way* F is
can be reconstructed from contrasts between actual terms. A branch that answers Q3 without
readmitting alternatives gains; one that can answer it only by readmitting them is closed by M2.

### Still to examine

Ps-modal (in part answered by B-power), Ps-relata, Ps-individ, Ps-logic.

### Literature

Records checked on 2026-10-23, texts not yet read for this layer: Anscombe, *Causality and
Determination* (1971), for singular causation (B-single, B-cause); Mumford and Anjum, *Getting Causes
from Powers* (2011), for B-power; Fine, "Guide to Ground" (2012), and Bennett, *Making Things Up*
(2017), for B-ground and for dependence as a generic notion with kinds (C-kind); Stroud,
"Transcendental Arguments" (1968), for Obj-stroud. Keys in `organon/library/refs.bib`.

---

## Frictions (all layers)

<!-- table filter="ns=mec type=friction" ns="mec" cols="Id:id|Friction:titled|Kind:kind|Between:between|Effect:effect|Status:status|Resolution:resolution|Resolved by:resolved_by" -->

### Withdrawn claims

<!-- table filter="ns=mec status=withdrawn" ns="mec" cols="Id:id|Claim:titled|Why withdrawn:#Why withdrawn" -->

---

*Later layers (order and retention; the epistemic apparatus) will be added below as they are
written, each with the same sections.*
