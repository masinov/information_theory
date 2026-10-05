# Register of commitments

This register lists everything the theory assumes, defines, or leaves open, one entry per item.
Each later paper adds its own entries in a new layer and cites the register for what it builds on.
A result in any layer should be traceable, through the **Requires** fields, to the entries it rests on.

**Entry kinds.**
*Premise*: the starting point that motivates the commitments.
*Commitment*: admitted, not derived; each must be argued for where it is introduced.
*Definition*: introduces a term in terms of existing entries; adds nothing new.
*Convention*: a feature of the presentation, not a claim about what is described.
*Exclusion*: a view the commitments rule out as a precondition of registration.
*Presupposition*: assumed by the text without being stated as a commitment; to be examined.
*Open*: a question the layer raises and does not answer.

Section numbers refer to *A Minimal Epistemic Core* (`latex/epistemic_core.tex`).

---

## Layer 1: the minimal epistemic core

### Premise

| Id | Statement | Notes | § |
|---|---|---|---|
| **P** | An epistemic relation is always a relation to something in particular. To perceive or claim anything about X, X must be distinguishable from what it is not, and that distinguishing must depend on X; otherwise what is perceived or claimed would not be about X. | Motivates D, R and C. The core claims necessity only: P yields necessary conditions, not sufficient ones. | 1 |

### Commitments

| Id | Statement | Requires | Does not establish | § |
|---|---|---|---|---|
| **D** | *Differentiability.* F admits differentiation, although no particular differentiation is thereby realized or specified. | P | Any particular articulation, or its realization. | 2 |
| **R** | *Second relatum.* There is a second relatum R, distinct from F, that admits differentiation of its own. | P, D | A knowing subject, or any dependence on F. | 4 |
| **C** | *Receptive dependence.* Through C, the contrast of a specified articulation realized in F is matched by a contrast between conditions of R, and the latter contrast obtains partly in virtue of the former. | D, R, Df-articulation, Df-conditions | Which way F is; understanding, representation, order, acquisition, retention. | 5 |

Argument for **D** (§2): if every differentiation were supplied by the receiver, registering a difference in F could not be distinguished from the receiver's merely differing within itself, and by P what was registered would not be about F.

Argument for **R** (§4): a contrast in F and a contrast in a second relatum are not the same fact; without a differentiation of its own, nothing in R could distinguish registration from non-registration.

Argument for **C** (§5): D and R leave F and R unconnected; matching alone is symmetric (resemblance, correspondence), so registration needs an asymmetric dependence, which no description of the relata supplies.

### Definitions

| Id | Term | Definition | Requires | § |
|---|---|---|---|---|
| Df-field | field F | Whatever is under consideration; fixes the scope of the inquiry. Implies no region, objects, boundary, or presentation to a subject. | none | 2 |
| Df-articulation | articulation ⟨a,δ,b⟩_F | A particular differentiation of F; a, b are its *terms*, δ its *contrast* (the respect in which the terms differ). Terms are positions, not prior objects. | D | 3 |
| Df-realized | realized articulation | F exhibits it: its terms are both actual and differ in δ. The terms are not alternatives. | Df-articulation | 3 |
| Df-specified | specified articulation | Its terms and contrast are fixed, by the account, not by F. Specification selects without creating, and can fail. | Df-articulation | 3 |
| Df-conditions | conditions r, r′ of R | The terms of a realized differentiation of R; both actual, co-present, neither alternatives nor stages. Need not share the form of an articulation of F. | R | 4 |
| Df-matching | matching | The terms of an articulation are paired with distinct conditions of R (a with r, b with r′). Symmetric. | Df-articulation, Df-conditions | 5 |
| Df-roles | target, receiver | In an instance of C: the target is the relatum whose contrast is depended upon; the receiver, the relatum whose contrast depends. Roles are positions in C, not natures of relata. | C | 5 |
| Df-registration | registration | A specified articulation realized in F is registered by R when C holds between them. Always registration *of* a specified articulation; an actual relation, not a disposition. | C, Df-specified, Df-realized | 6 |

### Conventions

| Id | Convention | § |
|---|---|---|
| Cv-two | Articulations are written with two terms; the account requires only at least two. | 3 |
| Cv-letters | F and R are named for the positions they occupy in the instances considered; nothing in R or C uses the notion of a receiver. | 5 |
| Cv-arrow | If C is written as an arrow, the same symbol must not also denote order. | 7 |
| Cv-figures | In figures, terms are marks, never areas; F and R are column headings, never enclosures; one arrow style is reserved for C; grey marks what belongs only to the theorist's description. | 3, 5, 6 |

### Exclusions (as preconditions of registration)

| Id | Excluded view | Excluded by | § |
|---|---|---|---|
| E1 | All differentiation is supplied by the receiver (pure constructivism). | D, P | 2 |
| E2 | Registration consists in resemblance or term-by-term correspondence. | C (second clause) | 5 |
| E3 | Registration is a transfer from target to receiver. | Df-registration | 6 |
| E4 | A repertoire of alternatives, in F, in R, or elsewhere, is a precondition of registration. | Df-realized, Df-conditions | 3, 6 |
| E5 | Time, or order of any kind, is a precondition of registration. | Df-registration (defined without order) | 7 |
| E6 | A knowing subject, concepts, or representations precede registration. | D, R, C (none involves them) | 4, 6 |

None of these denies that the excluded structures occur in particular epistemic relations; wherever they are needed, they must enter as further commitments.

### Presuppositions (used but not yet stated as commitments)

These are assumed by the text of Layer 1 and are to be examined, accepted as commitments, or removed.

| Id | Presupposition | Where it appears |
|---|---|---|
| Ps-modal | "Admits" expresses a capacity of F (and of R) itself, not a stock of possibilities held anywhere. | D, R; §2 |
| Ps-actual | Contrasts hold between actual terms only. | Df-realized, Df-conditions |
| Ps-relata | Terms are positions within an articulation; whether relations are prior to relata, or the theory is neutral, is not settled. | Df-articulation; §3 |
| Ps-ground | "In virtue of" is an asymmetric dependence that relates what actually obtains and need not be counterfactual; it is not analysed further. | C; §5 |
| Ps-individ | Enough individuation to distinguish F from R and to take r, r′ as conditions of one relatum; no more. | R; §4 |
| Ps-logic | The exposition uses identity, distinction, relation, and inference without attributing them to what it describes. | §1 |

### Open questions

| Id | Question | § |
|---|---|---|
| Q1 | What grounds the asymmetry of C in a given domain? | 5, 8 |
| Q2 | Can receptive dependence be explained in terms of more elementary relations? | 8 |
| Q3 | Can registration of *which way* F is be reconstructed from contrasts between actual terms, without admitting alternatives? | 6, 8 |
| Q4 | What order do acquisition and retention require, and is anything stronger than an asymmetric relation needed? | 7, 8 |

### Dependencies

Each item, with the items it requires:

- **D** ← P
- **R** ← P, D
- **Df-articulation** ← D; **Df-realized**, **Df-specified** ← Df-articulation
- **Df-conditions** ← R
- **Df-matching** ← Df-articulation, Df-conditions
- **C** ← D, R, Df-articulation, Df-conditions
- **Df-roles** ← C
- **Df-registration** ← C, Df-specified, Df-realized

---

*Later layers (ontology of the core; order and retention; the epistemic apparatus) will be added
below as they are written, each with the same sections.*
