# Plan: integrating rounds 4 and 5 into the paper

## 1. What rounds 4–5 do, and why they belong in the paper

Rounds 1–3 answered the opening question cheaply. A problem *supplies* μ_π for every policy, so the
counterfactual dependence that CDT, EDT and FDT disagree about is part of the input. A lookup table
then picks an ex-ante maximiser (Thm `thm:universal`), and every later impossibility lives in the
cross-problem axioms and the semantics of menus.

Round 4 removes the supplied dependence. An agent is a computable function on descriptions (source
code), and it must work out for itself what would happen under its other outputs. Round 5 then
isolates the remaining question: whether a coherent operator assigning values to the non-actual
outputs of a computation (a "logical counterfactual") exists at all.

| Round | Result | What it shows |
|---|---|---|
| 4 | Theorem 1 | With a fixed substitution semantics (oracle or designated slot) and a termination promise, there is a computable optimiser, the computable analogue of `thm:universal`. |
| 4 | Theorems 2–3 | Two impossibilities are trivial: foreign queries, and fixed copies of the agent combined with global totality. The second is Skalse's diagonal, which becomes well defined here although it was not in the matrix model. |
| 4 | Theorem 4 | Exact argmax over computable expected values is uncomputable. This is independent of any decision theory and is the strongest clean negative result. |
| 4 | Theorems 5–7 | Extensional matching as a semantics fails in several distinct ways. |
| 4 | Modal and logical results | Spurious counterfactuals and modal UDT, stated with their exact quantifiers. |
| 5 | Projection lemma | Calibration plus *grounded* extensionality forces the action-port (causal) kernel. |
| 5 | Theorem A | Transport cannot factor through grounded equivalence. |
| 5 | Theorem B | {calibration, grounded extensionality, ratifiability} is a minimal inconsistent triple. |
| 5 | Theorem C | Complete map: 6 minimal inconsistent sets, 4 maximal consistent sets. |
| 5 | Positive model | Under *parametric* extensionality, the slot kernel satisfies everything. |

## 2. The organising idea: a ladder of what a "decision theory" must be

The finished paper should climb three rungs. Each rung strengthens what counts as a decision theory,
and each relocates the obstruction.

1. **An assignment.** Any map from problems to policies, lookup tables included (Part I, current
   Sections 2–6). Ex-ante optimality is free, and conflicts are singleton or pairwise.
2. **A rule.** One rule on a common reduced form (the causal matrix), constrained by cross-problem
   axioms (Part II, current Sections 7–13). The deep results hinge on what a smaller menu's
   alternatives are.
3. **A procedure.** A computable function that reads a description and must construct the
   alternatives itself (Part III, new). The results hinge on what the alternatives to one's own
   output are.

The rung-3 results map onto earlier ones:

- Round 5's two kernels are the two halves of the causal matrix:
  - V_E(a) = M[a,a] is the diagonal, i.e. ex-ante value.
  - W_{E,b}(a) = M[b,a] is row b, i.e. causal evaluation at baseline b.
- The **projection lemma** therefore says that calibration plus grounded extensionality forces row
  (causal) evaluation, while parametric extensionality yields diagonal (ex-ante) evaluation.
- Part I's "one subscript" contrast (μ_π versus μ_{π[h←a]}) reappears as a choice between two
  extensionality principles.
- **Theorem B** is Death in Damascus (Prop `prop:did`) re-derived from semantic axioms.

The unifying final thesis: every impossibility in the paper is located in the *specification of the
alternatives*, not in choosing among them:

- Part I: which law is averaged.
- Part II: which belief perspectives survive menu removal.
- Part III: how dependence is transported to non-actual outputs.

## 3. Placement: append as Part III, but rewire the earlier parts

The new material goes *after* the cross-problem part and before the conclusion, because it takes
Parts I–II as input. It discharges stipulation 9 ("the same computation" is a stipulated
dependence) and the supplied-μ_π assumption that everything earlier rests on. It is not simply
appended, though: the earlier sections must point forward to it and be reshaped.

Proposed order (sections are grouped under `\part` headings, or under a short opening paragraph
per part if `\part` looks heavy in scrartcl):

### Part I, single problems with supplied dependence

Sections as now: model, criteria, witnesses, commitment, robustness.

### Part II, rules across problems

Sections as now: matrix, pairwise, translations, menus, exante, taxonomy, mixed.

### Part III, when the dependence is not supplied (new)

**14. Problems as programs** (new file `programs.tex`, from round 4 §1, §2 and §8):

- Agents as computable functions; promise-total versus globally total.
- Owned queries; payoff representations.
- Common payoff U(E,A) versus the anchored kernel U_K(E,T;A).
- Replacement conventions: const, oracle, syn, ext, log.
- Fairness classes F_self, F_any, F_ext, F_const.
- The non-implication lemma between conventions.
- Bridge: a terminating finite-policy oracle environment compiles to a §2 problem with Π_E and V_E.

**15. Computable optimisation and its limits** (`computation.tex`, round 4 §§2–4 and §10):

- Thm 1: uniform optimiser on the promise class, the computable analogue of `thm:universal`. Plus
  the König-lemma remark and the divergence-semantics caveat.
- Thm 2: F_any.
- Thm 3: the fixed-copy diagonal. This resolves Remark `rem:skalse`: global totality supplies the
  fixed point that the matrix model lacked.
- The double-call O_const baseline, identified as Death in Damascus.
- Thm 4: exact-selection impossibility, with the positive replacements (ε-optimality, a promised
  unique maximiser, exactly comparable values).
- Resource bounds (SAT).

**16. Inferring dependence from source** (`inference.tex`, round 4 §§5–7):

- Syntactic substitution and the encoded-copy diagonal.
- Extensional matching:
  - undefinedness under the counterfactual trace;
  - Thm 5, local equality;
  - rematching does not compose;
  - Thm 6, global matching misses 1−T;
  - Thm 7, halting reduction (with the corrected co-c.e. direction);
  - positive subclasses, and why no largest subclass exists.
- Logical counterfactuals:
  - ground proof-based evaluation (positive);
  - material implication and spuriousness;
  - the computable 5-and-10 (Löb);
  - Fallenstein's guarded semantics;
  - the modal diagonal and modal-UDT optimality, with the ∀P∃φ quantifiers;
  - logical induction.

Section ending: "once a semantics is fixed, optimisation is (promise-)computable, so the question is
the semantics". This must include round 5's correction §1.1: a baseline-dependent kernel raises a
separate fixed-point question, so "fixed semantics ⇒ finite computation" is false as round 4's
summary put it.

**17. Axioms for counterfactual operators** (`operators.tex`, round 5 §§1–6):

- Domain repairs: termination of transported contexts, raw-source extensionality, single-input
  versus policy-level transport.
- The finite context domain; D1–D10, with D9 ⇔ D2+D4 and D7 deliberately weak.
- The witnesses Slot, Port, Base and Flat, explicitly identified with the diagonal, a row of M, and
  so on.
- Projection lemma; Theorems A and B; Theorem C (complete map); the parametric positive model.
- Map variants:
  - conditional realisability (an alternative map with a 4-element core);
  - fixed-constant realisability;
  - the program domain, where global totality adds four pairwise cores.
- Leads L1–L6, merged with §16 rather than repeated:
  - L1: surjectivity, not injectivity;
  - L2–L4 classify the §16 matchings within the axioms;
  - L5: vacuism gives a relation, not an operator;
  - L6: fixed copies.
- W6 (arithmetic guarded semantics collapses to K_base) and W7 (logical induction plus exploration).

**18. Test cases and counterpossibles** (`counterpossibles.tex`, round 4 §9 and round 5 §§8, 10):

- The operator × problem table: Newcomb, twin, 5-and-10, fixed-copy diagonal. This links back to
  Section 4's witnesses. The Anti-Newcomb example from the raw prompts is dropped as irrelevant. It
  entered the prompts from an unrelated earlier conversation and adds nothing beyond Newcomb, the
  twin and the diagonal; see `raw/NOTE_rounds_4_5.md`.
- Counterpossibles:
  - Williamson's collapse argument;
  - Berto–French–Priest–Ripley;
  - impossible worlds as a representation of any kernel, but not a derivation of one;
  - Lewis's 1976 triviality theorem;
  - Taylor 2020.

**19. Conclusion** (rewritten).

**Appendix: register of stipulations** (extended).

## 4. Rewrites to existing material

- **Title and subtitle:** the subtitle must cover Part III. Candidate: "Within-Problem Conflicts,
  Menus, and the Semantics of Counterfactual Alternatives".
- **Abstract:** add a third movement, and end on the unified thesis.
- **Introduction:**
  - New history subsection, "Programs, proofs, and logical counterfactuals":
    - Tennenholtz's program equilibrium; Bárász et al.; Critch;
    - Dai and Yudkowsky; Soares–Fallenstein; modal UDT; Benson-Tilsen;
    - the 5-and-10 problem and the chicken rule;
    - logical induction; Demski–Garrabrant;
    - Rice and Kleene; Leike–Hutter;
    - counterpossibles: Lewis 1973 vacuism, Nolan, Williamson, Berto et al.
  - Rewrite "The question and the answer" around the three rungs, so that the cheap first answer is
    framed from the start as the consequence of supplied counterfactuals.
  - Extend the novelty paragraph and the roadmap.
- **Section 2 (model):** after Def `def:fair`, add a note that fixed algorithms are harmless here
  only because their outputs are numbers fixed by the problem, with a forward reference to §15.
  After Def `def:theory`, note that the permissive definition is the first rung.
- **Section 3 (criteria):** the sentence "No difficulty about general rules, computability, or
  self-reference is involved" should point forward to Part III.
- **Section 4 (twin):** "the same computation enters only as a stipulated dependence" should point
  forward to §§16–17.
- **Remark `rem:skalse`:** move it from matrix.tex to criteria.tex, after `thm:universal`, where it
  logically belongs. Shorten it and forward-reference Thm 3. It currently says the construction is
  ill-defined; it should say "ill-defined when dependence is supplied; well defined and decisive for
  globally total programs (§15)".
- **Section 13 (mixed) end, or start of Part III:** a transition paragraph explaining why the
  supplied μ_π must now go.
- **Conclusion:**
  - a fourth part of the answer;
  - a unified thesis quote;
  - new rows in Table `tab:results`;
  - revised open questions. The question "a richer reduced form might find obstructions" is partly
    answered: the context model is such a form. New open questions: extracting dependency graphs;
    the computability of parametric matching on unrestricted programs; the novelty of the D-maps.
- **Register of stipulations:** new items 21 onwards:
  - promise versus global totality;
  - disjoint owned-query namespaces;
  - frozen descriptions and the input-preservation repair;
  - atomic component boundaries;
  - intervention-total domains;
  - the local kernel interface;
  - the D9 realisation benchmark;
  - the D10 treatment of undefined alternatives;
  - the independence definition (invariance in the live parameter).
- **Notes:** extend guide.md (thread, glossary, result catalogue, map) and verification.md (proof
  checks of Theorems 1–7 and A–C, including an exhaustiveness check of the maps).

## 5. Bibliography (verify each, as with clusters A–C)

**New entries:**

- Computability: Rice 1953; Kleene 1938; Moschovakis 2010.
- Program equilibrium and cooperation: Tennenholtz 2004; Bárász et al. 2014; Critch 2019.
- MIRI and Alignment Forum work:
  - Benson-Tilsen 2014;
  - Fallenstein ×4 (evil problems, modal-UDT optimality, the improvement, third-person
    counterfactuals) plus "odd counterfactuals of playing chicken";
  - Garrabrant et al. 2016; Garrabrant 2017; Demski & Garrabrant 2019.
- Other: Leike & Hutter 2015; Taylor 2020.
- Counterpossibles: Nolan 1997 (correct the title); Williamson 2018 and the 2015 Amsterdam
  Colloquium paper; Berto et al. 2018; Lewis 1976; Lewis 1973 (Counterfactuals).
- König 1927 (or a textbook source).

**Already present:** soaresfallenstein2015, yudkowskysoares2017, skalse2021, dai2009, yudkowsky2010.

**Unresolved:**

- Origin of the 5-and-10 problem: verify an attribution, or cite Benson-Tilsen and Demski–Garrabrant
  only.

## 6. Size

About +22–28 pages, bringing the paper from 52 to roughly 75–80 pages. The five new section files
sit under `latex/sections/`.
