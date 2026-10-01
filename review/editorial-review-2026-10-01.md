# Editorial and mathematical review of the monograph (full read, 2026-10-01)

Scope: Parts I–XI and Appendices A–D of `monograph/`, read end to end. The review covers
(1) the architecture, especially the notion of "relaxing" the kernel's assumptions; (2) internal inconsistencies and
dangling cross-references; (3) theoretical gaps and leaps; (4) prose and register; (5) formatting.
Locations are section/statement numbers of the Markdown sources. Each item gives a suggested repair.

**Progress (first revision pass).** Done: §1.3 (new Part I §8 "How the theory grows from the kernel", with the assumption
ledger and the kernel-theorem template; §4.1 and §3.4 updated); §1.4 contextuality wording (Lemma 38.1, §38.4,
Remark 42.2) and the tracked-coordinate count (Remark 24.6 now defines representability; §84 names the algebra
coordinate); §2 items 1–15 and 17–24 (Remark 24.6 and its nine dependents; §40's measure now stated as a deliberately
weak proxy); §5 items 1–4 and 6 (statements in blockquotes throughout, Appendices A and D in proper math, broken `$`
spans, list/heading spacing via `latex/tools/normalize_md.py`, numbered §24 subsections). Second pass: §4.1, §4.2 and §4.3 done (new overview and summary sections for Parts II–XI; the six
"Mathematical scope" paragraphs folded into remarks and surrounding text); §2 item 16 resolved by defining
"reflection" once as a descriptive name (§22.2). Open: §1.4 P3 justification and categorical vocabulary; §2 items 25,
26; all of §3 except §40; §4.4–4.7 (vocabulary, process language, forward pointers, notation table); §5 items 5, 7.

Severity tags: **[A]** affects correctness or the reader's ability to follow the theory; **[B]** visible inconsistency or
missing detail; **[C]** style/formatting.

---

## 1. The central architectural issue: what "relaxing an assumption" means

### 1.1 What the manuscript actually does

The kernel (Part I) is never modified after it is written. No later part redefines $\sigma$, answerability, or the
partition lattice. What the later parts do is **generalize a primitive** and then show that the kernel reappears as a
special case:

| Part | primitive generalized | kernel objects embed as | recovery statement |
|---|---|---|---|
| II | one canonical registration → a class of admissible registrations (ceiling $\gamma_K$) | full admissibility $K^{\mathrm{can}}$, $\gamma = \sigma$ | Prop 14.6 (collapse), §15 |
| III | view = function → view = channel; family = joint channels | deterministic channels | Thm 24.2 |
| IV | pre-anchored view → emission + correspondence + policy | sound unique anchoring **and** sterile context | Thm 32.1 |
| V | (no assumption) local-to-global structure of all the above | deterministic, fully admissible, anchored | Thm 42.1 |
| VI, VIII | combinations of II–IV | each pure theory as a fibre | Thm 50.1, 65.1 |
| VII, IX | (no assumption) numerical evaluations of the intervals | — | — |
| X | single-record corruption (A7) → streams | horizon one | Thm 80.1 |
| XI | one domain (A5) → domain family | singleton family | Thm 88.1 |

So the correct reading is: *the kernel is a fixed reference model; every extension is a larger model containing the
kernel as a distinguished sub-model, and each part asks which kernel theorems (T1 adjunction, T2 principal ideal,
T3 marginal value, T4 terminal consolidation) survive in the larger model, survive laxly, or fail.* The kernel is used
in three ways: as the **target of recovery** (what the extension must reduce to), as a **template** (the "fate of
T1–T4" sections), and as an **ingredient** (e.g. $\sigma(T)$ is the upper bound in (K1); $\mathrm{Ach}(V)$ labels the
algebra in Parts V and XI).

### 1.2 Why the text makes this hard to see **[A]**

1. **"Relaxation" is never defined.** The text uses at least eight words for the same relationship — relaxation, hook,
   attachment point, fibre, collapse, recovery, "executed in", "discharged", "cashed". A reader naturally hears
   "relaxing an assumption of the kernel" as "changing the kernel", which contradicts "the kernel is fixed".
2. **The assumption ledger is incomplete and scattered.** Part I lists five assumptions (A1–A5) and says each has a
   designated relaxation (§4.1, §8). In fact:
   - (A1) is never relaxed (stated in §4.1), so "each with a designated relaxation" is false for A1.
   - New assumptions appear later without a ledger: the **finiteness of view sets** convention (§14), **(A4′)** sound
     unique anchoring (Def 19.7), **(A6)** finiteness of $D$ and presentation spaces (§20), **(A7)** reduced-form
     corruption (§29). A6 is only partially relaxed (Appendix A); A7 is relaxed in Part X.
   - Parts relax one assumption while installing another (III relaxes A2 but adds A4′ and A6; IV relaxes A4′ but adds
     A7). The reader is never shown this.
3. **H4 is not a relaxation.** §8 closes with "Each extension is a controlled relaxation of a named assumption", but H4
   (local-to-global semantics) relaxes no assumption; it is a new *question* asked of all layers. Parts V, VII, IX are
   of the same kind.
4. **Recovery sometimes needs more than the negated assumption.** Part IV recovers the kernel only under sound unique
   anchoring *plus* sterile context (Thm 32.1); §8 H1 and Def 19.7 mention this only in passing. The relaxation is
   therefore not "drop A4 and get back the kernel by re-imposing A4".
5. **§8 H4 and H5 were rewritten as summaries of later results** (Theorems 37.3, 37.5, D.8, D.10 …) instead of
   describing the hook. A reader at the end of Part I cannot understand them.

### 1.3 Suggested repair

Add, at the start of §8 (or as a new §7.5 "How the theory grows from the kernel"), a short formal paragraph and a table:

> **Definition (extension of the kernel).** An *extension* consists of (i) generalized primitives (e.g. channels instead
> of functions), (ii) an embedding of kernel data into them (a function is a point-mass channel), and (iii) a
> *recovery theorem*: on embedded data, every construction of the extension coincides with its kernel counterpart.
> An extension *relaxes* a standing assumption when the embedded data are exactly the data satisfying that assumption.
> Each part then classifies the kernel theorems T1–T4 as surviving exactly, laxly (an inequality replaces an equation),
> or failing.

Then one **assumption ledger** table for the whole book (assumption · introduced in · relaxed in · recovery theorem ·
extra conditions for recovery), including the finiteness convention, A4′, A6, A7, and a separate row type for the
"questions" H4 / evaluation (Parts V, VII, IX) that are not relaxations. A diagram of Parts as nodes with arrows
"generalizes" vs "analyzes" would help considerably. Move all forward pointers ("Executed in Part XI, Theorem 83.5")
out of the kernel into this roadmap.

### 1.4 Related architectural inconsistencies

- **[A] P3 is justified by a role it does not play.** §4.2 promotes the refinement preorder $(V,\preceq)$ to a primitive
  "because it is the designated future base site". Part V instead uses $\mathcal F(V)$ with the union coverage
  (Lemma 35.2 shows the determination system is not a coverage), and Appendix D.8 shows join covers on $\mathrm{Ach}(V)$
  form a site only for distributive lattices. Either rewrite the justification of P3 (it is used through $\mathrm{Ach}(V)$
  and Lemma 24.1) or demote it to a derived notion.
- **[A] The "tracked coordinates" are never defined as a mathematical object.** Their number drifts: §24 has two
  (codomain, compositionality); §32.2 adds fidelity and lists "representability"; §42.2 calls descent "a fifth";
  §50.2 says "Part VI adds no sixth coordinate"; §84 is titled "The algebra coordinate"; Appendix C lists six;
  Theorem 85.1 says they are "an organizing taxonomy". Either define them (e.g. as the columns of one table with
  explicit values per layer) or present them only as an informal reading guide in one place.
- **[A] Contextuality claims survive their own retraction.** Lemma 38.1 states that the witness anomaly is "precisely
  the … pattern that Abramsky–Brandenburger identify as the logical form of contextuality"; its own scope note, §39,
  §43, and Appendix D.12 say the witness presheaf is *not* the event/support presheaf and witness anomalies do not imply
  contextuality. §38.4 still calls the hierarchy "the exact-case analogue of the logical/strong contextuality
  hierarchy", and Remark 42.2 claims "a fully classical theory of contextual evidence". Rewrite all of these to say
  "a possibilistic all-local/no-global pattern analogous in form to …" or remove.
- **[B] "Cosheaf/sheaf" and "functor" vocabulary is stronger than what is proved.** The content level is called a
  "cosheaf chirality" object (Rem 36.1), the exact addresses "cosheaf addresses" (Thm 54.1, Ex I), Def 56.1 a "ledger
  functor" — but no category of families/morphisms is defined for the functor, and Def 24.5 itself says the join
  equation "is distinct from the contravariant Set-valued sheaf axiom". Either define the categories or use plainer
  terms ("join-type gluing", "marginalization map").
- **[B] Promised theorem vs delivered theorem in Part XI.** §82 announces "the theorem toward which every part has been
  aimed"; Theorem 85.1 is a hedged scope statement ("No unrestricted assertion … is made"). Reframe §82 or strengthen
  85.1 into a precise recovery theorem.

---

## 2. Inconsistencies and dangling references (left by revisions)

Each of these is a concrete fix.

1. **[A] Def 4.6 / §9 table:** the soundness axiom is tagged `(Appendix D.1)` and referred to as "(Appendix D.1) is the one
   substantive axiom". This is a find-and-replace artifact; restore a name such as (S) or (Sound).
2. **[A] §12:** the "Mathematical scope" paragraph says completeness of Armstrong's rules is *not* proved; the very next
   paragraph begins "Thus the completeness of Armstrong's system … reflects …". Delete or rewrite the second paragraph.
3. **[A] Remark 24.6 was rewritten, but eight places still rely on its old content** (an "ideal completion" that
   consolidates non-principal classes and a coordinate called "representability"): §16.2 ("the consolidation is made in
   Part III, §24"), §22.1 ("consolidated by the ideal completion of §24 (Remark 24.6)"), Def 24.5, §32.2, §40 ("the
   ideal-valued full-stratum content of Remark 24.6"), Prop 48.2 ("dissolves in the ideal completion of Remark 24.6"),
   §50.2 table, Remark 69.5, §65 ("the ideal completion absorbs, at representability"), Appendix C. The current Remark
   24.6 says the down-set completion does *not* supply such a repair. Decide which is true and make all nine agree.
4. **[A] Theorem 30.4** says "sterility is exactly what the theorem needs"; the scope note after it says sterility is
   sufficient, not necessary. Remove "exactly".
5. **[A] §65** says "No canonical repair exists on the principal side (Proposition 61.2)"; the revised Proposition 61.2
   says non-existence is **not** proved. Fix §65.
6. **[A] §82** quotes §8's brief for H5 ("reintroduce the ambient class … functoriality of $\sigma$ … extending
   Theorem 6.2"). That text no longer exists in §8. Restore it in §8 or rewrite §82.
7. **[B] (A1), §4.1:** "never relaxed, by design — see Part XI, Theorem 85.1". Theorem 85.1 does not discuss totality.
8. **[B] §32.2 table** cites "Theorem 32.1(1)"; Theorem 32.1 has no numbered items.
9. **[B] Prop 69.2** cites "Theorem 69.4(2)"; Theorem 69.4 has no numbered items. **Appendix B.2** cites "Thm 84.1(2)";
   Theorem 84.1 has no items.
10. **[B] §45.2** ("Question (a) of §43"), **Theorem 46.3** ("answer to §43(b)"), **Remark 69.5** ("The program of §43
    closes"): §43 no longer contains these questions.
11. **[B] §47** refers to "the typing decision of §44"; §44 no longer contains one.
12. **[B] §49** uses "the structure $K_\varnothing$ of Corollary 45.5(3)"; Corollary 45.5 has no item (3), and
    $K_\varnothing$ is not defined. Corollary 45.5 also uses $\mathcal N$ (set of presentation atoms) without definition.
13. **[B] Remark 62.4** refers to "Proposition 61.2's creation exhibit"; the creation exhibit is Theorem 61.1(2).
14. **[B] Theorem 65.1:** "the frontier is the point $(0, V_o)$" — $V_o$ is undefined.
15. **[B] §50.3 "The discharged cell"** no longer describes a discharged cell; §65's "discharge annotations are entered
    at §50.2 and §48" is editorial bookkeeping. Retitle/remove.
16. **[B] Reflection vs right adjoint.** Prop 22.3′'s scope note proves component formation is a *right* adjoint
    (a coreflection in the information order) and says "reflection" is only a mechanism name; the following paragraph,
    Theorem 37.7, Lemma 83.2(2) and Prop 83.3 continue to call it "the reflection of tolerances onto equivalence
    relations". Rename the mechanism (e.g. "component collapse") and keep "reflector" only where the adjoint really is
    a left adjoint (saturation $s_\rho$ in inclusion order, Prop 83.3).
17. **[B] Worked example I** reports "Total admissible synergy ≈ 2.230 bits" as a sum of a witness evaluation, a
    reflection evaluation, and a coupling excess; §52, Theorem 57.1 and Remark 57.2 state that no universal sum of these
    terms is defined. Either define the total for the product construction (and prove additivity there) or drop it.
18. **[B] Prop 68.3** says every value "has additionally been verified by direct solution of the linear program";
    Appendix B.5 says the historical counts were not re-run. Align the provenance statements.
19. **[B] §38.4** "computed here on six-element domains by hand" — the hierarchy $C_{k+1}$ lives on $2(k+1)$ elements.
20. **[B] Example D (§31)** calls the tie-break policy a "loyalty anomaly in miniature", but loyalty is defined only for
    the tracked-target reading and Example D is the identity reading.
21. **[B] Example J (§64)** calls policy $(d,d)$ "reject everything"; it attributes to the distractor, not to $\bot$.
22. **[B] Example K (§72)**: "Down a noisy column the zero-error rung and the other two rungs **do disagree** about whether
    … survive; they disagree — this is the part's point — about the geometry of its dying." The sentence contradicts
    itself (a negation was lost in revision).
23. **[C] §20.3** "Three standard facts are used repeatedly" — four are listed.
24. **[C] Remark 21.3** "Vorob'ev's theorem characterizes, in the exact case, …" — Vorob'ev's theorem concerns
    probability measures; "exact case" is the wrong qualifier.
25. **[B] Prop 46.2(2)** claims the two factors are independent coordinates and that "§46.2 realizes every combination";
    Theorem 46.3 exhibits some combinations, not all four. Prove or weaken.
26. **[B] Corollary 15.4 proof**: "Grounding follows from the raw-content bound at the empty set" and the last sentence
    on $\mathcal F(V)$ are compressed to the point of being unclear; write out (ii)⇒(iv) and the empty-union case.

---

## 3. Theoretical gaps and leaps (missing levels of detail)

### Part I
- **[B] Prop 6.11** is presented as a labeled information algebra "in the generalized set-algebra sense of Kohlas 2017",
  but $\mathrm{Ach}(V)$ is not meet-closed (noted only in the scope paragraph) and the combination axiom used is a
  restricted form ($\rho \le \pi$). State exactly which axioms hold and which domain-lattice hypotheses of Kohlas'
  definition are weakened, in the statement rather than afterwards.
- **[C] §7** last paragraph mixes a list of absences with "single-domain extraction is already provided by Proposition
  6.11" — grammatically and logically out of place.

### Part II
- **[A] Def 14.3 defines admissibility by its ceiling.** (K2) ("every $\rho \le \gamma_K(T)$ is admissible") is then a
  definition, not an axiom, and non-principal admissible classes (the budget example of §16.2) are excluded by fiat.
  Prop 14.4′ even reconstructs the classes $\mathcal K(T)$ from $\gamma_K$. Cleaner: make the primitive a family of
  coarsening-closed registration classes $\mathcal K(T)$; define $\gamma_K(T)$ as its top when it exists; state
  principality as an explicit hypothesis ("principal admissibility structure").
- **[B] Def 15.3** promises that intervals "restrict, intersect, and compose", the raw material of an obstruction
  theory. No interval algebra is ever defined; concatenation "$[a,m]\cdot[m,b]$" is used in Thm 37.7, Prop 46.2,
  Prop 53.2 without definition. Add a short definition (intervals of $\mathrm{Part}(D)$ as a category with composition
  by concatenation; restriction along monotone maps) or drop the promise.
- **[B] §16.1** "an admissible registered partition must have $G$-stable blocks" is ambiguous: "$G$-stable" usually
  means $G$ permutes the blocks (then $\ker v$ qualifies), whereas the construction needs blocks that are unions of
  orbits. Say "every block is a union of $G$-orbits (equivalently the reading is $G$-invariant)".
- **[C] §16.4 and §17** are now too compressed to be read at that point (forward references to Prop 36.3, D.8, D.12).

### Part III
- **[A] Def 19.6–19.7: the context mechanism is untyped.** The generalized view has a context space $C_v$ but no law
  generating contexts; Def 19.7 then quantifies over "every context $c$ arising with $e_v(Z)$" and requires
  $C \perp Z \mid Y$. Joint emission of $(y,c)$ is only introduced in Def 27.2. Add the emission of context (deterministic
  $D \to Y_v \times C_v$ in the exact case) to Def 19.6.
- **[B] §22.1** asserts that $\varepsilon$-answerability is "not a principal ideal in general" with no example. Give one
  (three candidates, two questions each $\varepsilon$-answerable whose join is not).
- **[B] Thm 22.2 proof:** $\delta$ is introduced and never used; the a.s. argument plus "standard concentration" for
  uniformity should be one explicit Hoeffding bound with the minimum TV gap $\delta$.
- **[B] Prop 22.5:** the claim that the common-refinement pairing is the Blackwell *join* of two deterministic
  experiments among **all** experiments is credited to Lemma 24.1, which only compares deterministic channels. The
  missing step (any upper bound $H$ must determine both values on its realized outputs) is short; add it.
- **[B] §22.4** identifies the information bottleneck with "the graded form of budget-type admissibility" without an
  argument. Present as a remark/analogy.
- **[B] Remark 24.7** (Le Cam deficiency makes an "ideal-valued content system metrically enriched") is unsupported
  after the rewrite of Remark 24.6.

### Part IV
- **[B] Notation collision.** $S$ is both a view set and the standard record; $T$ both a view set and the verdict;
  this makes Prop 27.8 and Thm 32.1 hard to parse.
- **[B] Prop 29.8(1)** contains cryptic patch sentences ("anti-correlated erasures of two identity copies can always
  leave one reveal"; "A positive common full-support replacement … is sufficient") and a forward reference to Lemma 41.1
  for a basic property. Expand into a short proof or a remark with the example.
- **[B] Thm 30.4** hypothesis "no clutter" is not defined in the accepted-record model of Def 30.1.

### Part V
- **[A] §40's "enriched cell defect"** $d(\mathcal U;T)=\min_i \delta(P_{T_i},P_T)$ measures how well the *best single*
  cover member simulates the whole; it does not depend on the cover's members jointly and is therefore not a gluing
  defect in the sense of Def 24.5 (Appendix D.6's "order caution" says as much). Either justify it as a deliberately
  weak proxy or replace it with a defect that uses an amalgamation (e.g. the minimum deficiency over the coupling fibre).
- **[B] Prop 38.3(4) proof** ("the converse direction only needs …") is garbled; Prop 38.5 later restates it better —
  merge.
- **[B] Theorem 39.2:** necessity needs alphabets of size ≥ 2; "for every choice of finite outcome alphabets" should
  say so. The "Le Cam diameter of a fibre" (Prop 39.3, Rem 55.5) is never defined.

### Part VI
- **[B] Prop 45.2 proof** uses "forced-possible" where "avoidable"/"optional" is meant.
- **[B] Prop 48.2** relies on "form-restricted (pointed) classes" and the ideal completion; neither is defined.

### Part VII
- **[B] Worked example I** combines exact admissible readings on two factors with arbitrary channels on the graded
  factor. A mixed exact/graded admissibility structure is not defined anywhere; define it for products or restrict the
  example.

### Part IX
- **[B] Example K, targeted columns:** the adversary that minimizes TV (enriched rung) need not minimize mutual
  information (Shannon rung). The table's Shannon entries assume the TV-optimal attack. State this or optimize each
  rung separately.
- **[B] §72 last paragraph** ("adjoin a third context class … reproduces Theorem 69.3's triple") is asserted without
  construction; the notation "$\{c_0\mid c_1c_2\}$-lift" is undefined.

### Part X
- **[B] Theorem 77.1** opens with an unclear hypothesis ("two nested closed feasible classes of attacks … with a
  compact rate parameter and an attainable annihilation constraint"). State the feasibility programs explicitly
  (they are in Appendix B.1).
- **[B] Worked example L** is three sentences summarizing other results; it is not a worked example. Expand or merge
  into §78.

### Part XI
- **[B] Def 83.1 vs Def 83.4:** 83.1 allows arbitrary finite diagrams with restrictions; 83.4 requires surjections
  from a common scene and says restrictions "are treated as morphisms below". How a restriction $D' \hookrightarrow D$
  sits in the common-scene picture is not stated. Give the precise category.
- **[C] Prop 83.3:** broken sentence ("… $\Phi_\rho \hookrightarrow \mathcal P(D)$ — In the reversed information order
  …").

---

## 4. Prose and register

1. **Part-opening sections read as errata summaries.** §§10, 18, 26, 34, 44, 52, 60, 67, 74 are each one dense
   paragraph using terms not yet defined (e.g. "memberwise N-completeness", "positive subset site", "coupling gap"),
   and their titles do not match the parts they open (§10 "Admissible exact readings" opens Part II's worked examples).
   Replace each with a proper introduction: motivation, which assumption is relaxed (or which question is asked), the
   main results in words, and a roadmap.
2. **"Mathematical scope." paragraphs** (after Prop 6.11, §12, Prop 22.3′, Thm 30.4, Lemma 38.1, Lemma 83.2) are
   corrections appended after the statement in a terse register. Fold the hypotheses into the statements and turn the
   rest into remarks; a reader should not meet an overclaim followed by its retraction.
3. **"Established results and scope" sections** (§§17, 25, 33, 43, 51, 59, 66, 73, 81) are 3–5 terse sentences. Expand
   into real summaries (what was proved, what fails, what is open), or merge into the part introductions.
4. **Metaphorical vocabulary.** Words such as *price receipts, dividend, cashed, lever, dial, currency, quantum,
   ledger, address, smuggled, immortality, panic policy, famous anomaly, vindicated, consuming its own capital* carry
   real technical content in places (ledger, address) and none in others. Keep the technical ones, define each once
   (Appendix C does this partially), and remove the rhetorical ones.
5. **Process language** should go from the published text: "the audit preceding this part", "the original proof",
   "the earlier claim … is too strong", "this review", "the original manuscript", "References added in Part X: none —
   … consuming its own capital".
6. **Forward pointers inside statements** (e.g. "(Executed in Part XI, Theorem 83.5.)" in §3.4; the long parenthetical
   at the end of Remark 21.3; "Part V develops it into …" in Remark 29.5) break the reading flow. Move to footnotes or
   to the roadmap.
7. **Notation overloading** (a notation table is needed):
   - $S$: view set / standard record; $T$: view set / verdict variable;
   - $\tau$: upper adjoint (Def 6.1) / verdict view $\tau_v$ / TV separation (Prop 71.1);
   - $N$: forgetful record / BSC $N$ (Prop 23.3) / presentation atom $N_v$;
   - $\delta$: deficiency / erasure probability (Thm 61.1) / point mass $\delta_y$ / cover defect $\delta_K$ / minimum TV gap;
   - $\Delta$: registration anomaly / Le Cam distance / simplex $\Delta^k$ / BROJA set $\Delta_P$;
   - $d$: distractor / $L_1$ distance (Lemma 62.1) / label map $d(E,\pi)$;
   - $K$: admissibility structure / regular conditional kernel (Appendix A); $m$: minimal statistic / alphabet size /
     fibre minima $m_D$; $\varepsilon$: corruption rate / error threshold.

---

## 5. Formatting

1. **[A]** `(Appendix D.1)` as an equation tag (Def 4.6, §9) — see §2.1.
2. **[B]** `---` directly after the last paragraph of §16.4: in Markdown this turns the paragraph into a heading.
3. **[B]** Appendix A and D.1–D.7 write mathematics in backticks and Unicode (`sπ(E)`, `E≼B F`, `σ⁰`); D.8–D.13 use
   LaTeX. Statements in Appendix D are bold paragraphs, not the blockquote form used elsewhere; proofs end with `∎`
   elsewhere `$\square$`. (The LaTeX edition already hand-typesets A and D.1–D.7; the Markdown should follow.)
4. **[B]** Three math spans have a space before the closing `$` and do not parse: `$\sigma^= $` (Thm 29.6 proof),
   `$v = $`, `$w = $` (Thm 46.3 proof).
5. **[C]** Primed and lettered numbers (Prop 14.4′, 22.3′, Remark 30.4′, Prop D.2a, Lemma D.4a) and "Definition 22.0";
   renumber in the final edition.
6. **[C]** Unnumbered subsection headings inside §24 ("The structural collapse", "The content-system schema") and §42.3.
7. **[C]** Citations: per-part "References added" lists; "[Fisher; Halmos & Savage 1949.]" (no Fisher entry); Appendix A
   cites Fritz by hyperlink; "[Bertschinger–Rauh 2014, Proposition 16]" mixed style. A single bibliography (as in the
   LaTeX edition) resolves this.
8. **[C]** Appendix B.2 lists the erasure geodesic as $(\lambda'-\lambda)/2$ (the $k=2$ case) while Thm 69.4 states
   $(\lambda'-\lambda)(1-1/k)$.

---

## 6. Suggested order of work

1. Write the "how the theory grows" section and the assumption ledger (§1.3) — this resolves most of the reader's
   difficulty and fixes the frame for everything else.
2. Fix the [A] inconsistencies of §2 (items 1–6) and decide the status of Remark 24.6 (item 3), since many later
   passages depend on it.
3. Rewrite the part introductions and closing summaries (§4.1, §4.3), folding the "Mathematical scope" paragraphs into
   statements.
4. Fill the gaps of §3, starting with Def 14.3, Def 19.6, and §40.
5. Notation table and renaming; then formatting.
