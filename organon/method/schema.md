# Schema

The schema is part of the method: it is revisable, and a revision is recorded in the journal with its
reason. It is named as an entry by `method/Mp-schema`, so that frictions can attach to it. Kept
deliberately small. When something does not fit any type, write it in `notebook/` first; add a type
only when several notes need it.

## Entries

An entry is one Markdown file that starts with a front-matter block:

```
---
id: mec/C-asym
type: claim
role: commitment
title: Asymmetry
status: adopted
requires: [C, Df-roles]
---
First paragraph: the statement itself.

## Any section
Further text, read by views under its heading.
```

Front matter is restricted YAML: one `key: value` per line; a value is a plain string or a list
`[a, b]`. The first paragraph of the body is the entry's statement.

**Ids and files.** An id is `namespace/local`. Entries of namespace `ns` live in `graph/ns/local.md`;
method entries in `method/local.md` (namespace `method`); notes on sources in
`library/sources/key.md` (namespace `src`, where `key` is the bibliography key). Within a namespace,
links may use the local part alone. File names are case-insensitive on some systems: no two ids, and
no id and a prose file such as this one, may differ only in case (the checker enforces it).

| Namespace | Contents |
|---|---|
| `mec` | the minimal epistemic core (`minimal_epistemic_core/`) |
| `mec.process` | the core in process philosophy (a frame) |
| `meta` | questions about how to do philosophy, common to all investigations |
| `method` | rules, methodological presuppositions, test protocols |
| `src` | notes on sources |

Every namespace in `graph/` is opened by one entry: `_investigation.md` for an investigation, or
`_frame.md` for a frame (below). A frame's namespace is named after its investigation's:
`err.process` for a process-philosophy frame on the investigation `err`.

## Investigations and frames

An **investigation** is one question pursued to a result. Its opener (`type: investigation`) names the
`question`, the `folder` holding its papers, and what it `builds_on`. Statuses: exploring, deciding,
paused, finished; a finished investigation states its result, negative results included, in a
`## Result` section.

A **frame** is another system of thought applied to the same question, alongside the investigation's
own. Its opener (`type: frame`) names its `investigation` and states its relation to the entries of
other namespaces:

| Field | Meaning |
|---|---|
| `accepts` | entries the frame takes over unchanged |
| `rejects` | entries the frame denies |
| `reinterprets` | entries the frame keeps in other terms; each needs an entry of the frame that `translates` or `corresponds` to it |
| `divided` | entries on which the frame's own branches disagree; each branch states its stance with `accepts` / `rejects` |
| `overrides` | method entries suspended in the frame (for example `method/Mp-classical` for a paraconsistent frame) |
| `holds_fixed` | on any opener, investigation or frame: the entries it keeps out of examination for the moment (see below) |

Entries not mentioned are neither accepted nor rejected: the frame has to say. The checker warns about
every claim, concept, decision and position of the investigation (not withdrawn) that the frame leaves
unaddressed. Method entries local to a frame live in its own namespace. `python tools/q.py --method
<ns>` lists the method in force in a namespace; the checker reports links to method entries that are
not in force there, and rules that `require` a suspended entry. Frames are namespaces, not git
branches, so that they can be compared side by side; comparing what survives across frames is rule M5
at full scale.

An investigation's own namespace is a frame too, not a neutral default. Following `method/Mp-separable`,
frame and content differ by role, not by kind: what an opener lists in `holds_fixed` is what it keeps
fixed while the rest is examined, and content can force a change in it. `method/T-reflexive` applies an
investigation's content to organon itself.

`translates` says the same thing in other terms; `corresponds` marks an entry that plays the same
role. An entry that translates should say what is lost in a `## Lost` section.

## Frictions

A **friction** (`type: friction`) is anything that blocks progress or prompts revision. Fields: `kind`,
`between` (the entries in conflict), `effect` (`blocks` or `prompts`), `status` (open, resolved), and,
when resolved, `resolution` and `resolved_by`.

| Kind | What it is |
|---|---|
| contradiction | A and not-A follow |
| tension | not contradictory, but held together only at a cost |
| collapse | a distinction that is needed disappears |
| underdetermination | two options fit everything available |
| gap | something needed cannot be supplied |
| regress | justification never ends, or returns to its start |
| triviality | true but empty |
| anomaly | a case that resists without refuting |
| ambiguity | a term or claim can be read in incompatible ways |
| overreach | a claim stronger than its support |

| Resolution | What it does |
|---|---|
| reject | gives up one side |
| distinguish | in one respect A, in another not-A |
| restrict | narrows the scope of a claim |
| accept | keeps both sides and states the cost |
| dissolve | shows the question was badly posed |
| sublate | a new position that keeps what was right on each side and goes beyond both |

A sublation is an entry with a `sublates` link to the entries it overcomes and three sections:
`## Kept` (what survives from each side), `## Dropped` (what is given up from each), `## Raised` (the
new element that makes them one). Without them the word is not used.

Frictions are recorded, not detected: the checker sees broken links, not conflicts of meaning. Finding
frictions is the work of the protocols (counterexample search, cold reader, countermodel search,
reflexive test).

## Types and statuses

| Type | What it is | Statuses |
|---|---|---|
| claim | a proposition, ours or attributed | unexamined, proposed, adopted, examined, withdrawn, refuted |
| concept | a term and its definition | proposed, adopted, withdrawn |
| argument | premises leading to a conclusion (`supports`) | proposed, accepted, rejected |
| position | a coherent analysis kept open or closed (branches) | open, adopted, closed |
| objection | an attack on an entry (`attacks`) | open, answered, conceded |
| question | an open problem | open, answered, dissolved |
| decision | a choice, with reasons and `basis` | taken, revised |
| dissent | a recorded disagreement with a decision (`against`, `by`) | standing, withdrawn, vindicated, overruled |
| prediction | an expected result written before a test (`test`, `by`) | pending, right, wrong, mixed |
| test | a run of a protocol (`protocol`, `result`) | planned, run, abandoned |
| method | a rule, presupposition or protocol | in-force, revised, retired |
| convention | a feature of presentation | in-force, retired |
| excerpt | a passage of a source (`cites`, `location`, `verified`) | recorded |
| source | notes on one work | to-read, reading, read |
| investigation | one question pursued to a result | exploring, deciding, paused, finished |
| frame | a system of thought applied to an investigation's question | active, paused, abandoned, concluded |
| friction | what blocks progress or prompts revision | open, resolved |

Nothing is deleted. An idea that fails keeps its file and changes status, with the reason in its body.

## Fields

| Field | Meaning |
|---|---|
| `id`, `type`, `title`, `status` | required on every entry |
| `role` | the entry's place in an investigation's register: premise, commitment, definition, convention, exclusion, presupposition, consequence, proposal, branch, closed, open, decision, argument; for method entries: rule, presupposition, protocol |
| `layer`, `where`, `order` | layer of the investigation, section of its paper, position in views |
| `since` | date the entry was introduced, when known |
| `by` | `mario`, `claude` or `both`: whose position, decision, dissent or prediction it is |
| `basis` | for decisions and closed positions (rule M4): `commitment`, `method` or `both` |
| `cites` | bibliography keys in `library/refs.bib` |
| `verified` | for excerpts and attributed claims: see below |
| `untitled` | `true` if views should not print the title before the statement |

**Presentational fields.** `order`, `where`, `since`, `untitled`, and a `title` equal to the id present
an entry; they register nothing about what the entry records, like the conventions of an investigation
(meta/FR-presentation).

**Link fields** take entry ids: `requires`, `supports`, `attacks`, `refines`, `contradicts`, `answers`,
`about`, `excluded_by`, `closed_by`, `against`, `test`, `reopens`, `closes`, `see`, `revises`, `question`,
`builds_on`, `investigation`, `accepts`, `rejects`, `reinterprets`, `divided`, `holds_fixed`, `overrides`,
`corresponds`, `translates`, `between`, `resolved_by`, `sublates`. In a body, `[[id]]` is a link too.
The checker resolves all of them. `requires` is reserved for dependence: the entry rests on the target.
A decision or proposal names what it concerns with `about` (meta/FR-requires).

## Verification levels

Used in the bibliography (`verified` field) and on excerpts and attributed claims.

| Level | Meaning |
|---|---|
| `text` | checked against the work itself: the passage, page, or quotation |
| `secondary` | a claim about a work's content, checked against secondary literature but not the work itself |
| `record` | metadata checked against a catalogue, publisher, or database record |
| `memory` | entered from memory, not checked |
| `unknown` | imported without a record of how it was checked |

Nothing sent to readers cites at level `memory`. A quotation or page-specific claim needs `text`.

## Views

A view is a Markdown template in `views/`; `tools/register.py` fills its tables from the entries and
writes the result where the template's first line says. Generated files say so in their first line
and are not edited by hand.
