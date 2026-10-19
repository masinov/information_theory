# Reading guide: impossibility and possibility of an optimal decision theory

Companion to `raw/` (three rounds of prompts and agent outputs). Source references are given as
`R1:§n` / `R2:§n` / `R3:§n` for the outputs (`raw/outputs/output_round_k.md`) and `P1..P3` for the
prompts (`raw/agent_prompts/prompt_round_k.md`). Proof checks are logged in `verification.md`.

---

## 1. The thread in one page

**Starting thesis (P1 §0).** "No decision theory is optimal on all fair decision problems", where a
decision theory is *any* assignment of policies to problems (lookup tables allowed) and fairness
means payoffs depend on the agent only through its prescribed actions.

**Round 1 — within a single problem.** The thesis is *false as stated*: since every finite problem
has finitely many deterministic policies, picking an ex-ante maximiser per problem is a decision
theory satisfying ex-ante optimality (C1) everywhere (R1:§2 Thm 1). What is true is that particular
*pairs* of criteria conflict:
- C1 (ex-ante) vs C2 (structural causal dominance): noisy Newcomb, ε < 1/4 (Nozick 1969).
- Exact characterisation: for one always-reached choice, the conflict is possible for some bounded
  payoff iff the induced state laws μ_a are not all equal (R1:§3 Thm 3).
- C3 (ratifiability) is individually unsatisfiable for deterministic policies (Death in Damascus).
- C2 vs C4 (commitment stability) conflict in exact Newcomb.
- Complete map C1–C5: minimal inconsistent {C3}, {C1,C2}, {C2,C4}; maximal consistent
  {C1,C4,C5}, {C2,C5}. With an evidential C6^κ: add {C1,C6}, {C2,C6}, {C4,C6}; maximal {C6,C5}.
- Hence within-problem criteria produce only singleton or pairwise obstructions: no Arrow-style
  family. Briggs (2010) flagged as prior Arrow-style result.

**Round 2 — across problems.** Reduce every problem to its *causal matrix*
M[π,σ] = Σ_s μ_π(s) U(s,σ) (row = beliefs induced by π, column = option evaluated; diagonal = ex-ante
value). Every real square matrix is realisable (R1:§8.2), so rules on matrices have an unrestricted
domain. Cross-problem axioms N, F, R, P, L, D, J, B, S, C, O, Q.
- With common affine invariance F only: every inconsistency has a singleton/pair core:
  {L}, {J}, {P,D}, {P,B}, {P,S}, {P,C}. {P,S} is Briggs's theorem.
- Adding row-translation invariance R: a genuine **four-axiom minimal impossibility**
  {N, R, C, Q} (circulant embedding), and {N, R, B, Q}; plus {R, D}.
- Commitment couplings: every row of the commitment matrix equals V_D, for every coupling; A3–C4
  reversal iff g = m(1−2ε) − c > 0; structural C2–C4 reversal only at ε = 0.
- Taxonomy: 2^𝔠 rules under N,F,O (no finite parameterisation, finite benchmarks fail); under
  N,F,B,O exactly three rules (increasing/decreasing diagonal, indifference).
- Mixed and evidential extensions.

**Round 3 — the semantics of a smaller menu.** Working thesis ("dichotomy"): menu-coherent
evaluation forces ex-ante evaluation; causal evaluation cannot be menu-coherent without triviality.
**Verdict: false as stated.** What survives:
1. Principal binary independence + N + F + O + Q + Mon ⇒ increasing-diagonal (ex-ante) ranking
   (core = Podgorski's Self-Esteem Theorem, 2022).
2. Principal contraction + N + R ⇒ choose everything, on any domain satisfying (DR) — an exact
   necessary-and-sufficient domain condition.
3. Under column (or fixed-reference) restriction, uniform column averaging (fixed-prior CDT)
   satisfies N,F,R,P,B_col,C_col,O,Q,Mon: the impossibility disappears.
4. Contraction (any semantics) + N,F,O,Q,Mon does *not* force diagonal ranking (λ-family; 2^𝔠).
Key lesson: "preserving choices when options disappear" ≠ "preserving comparisons when their
associated belief perspectives disappear"; the impossibilities need the latter.

**Final thesis (to defend in the paper).**
(i) An ex-ante-optimal decision theory exists on every class of well-defined fair finite problems.
(ii) Within a problem, conflicts are shallow (singletons, pairs), the central pair being Nozick's.
(iii) Across problems, ex-ante evaluation is *characterised* by principal binary independence plus
symmetry/invariance/ordering/monotonicity; and row-baseline-invariant (causal-style) evaluation
cannot be nontrivial, neutral and contraction-consistent under principal restriction on rich
domains — but this depends on the menu semantics and on the domain.

---

## 2. Glossary (fixed notation for the paper)

| Symbol | Meaning | Source |
|---|---|---|
| D | finite extensive-form problem, no info set repeated on a path | R1:§1.1 |
| H_D, A_h | agent information sets; finite nonempty action sets | P1 §1 |
| Π_D = ∏ A_h | deterministic policies | R1:§1.1 |
| S_D | finite set of structural environment plans (responses incl. off-path) | R1:§1.1 |
| μ_π | law on S_D induced by policy π (predictive dependence) | R1:§1.1 |
| U_D(s,π) | payoff from traversing with plan s and policy π | R1:§1.1 |
| V_D(π) | ex-ante value Σ μ_π(s)U(s,π) | R1:§1.1 |
| R_h(π), r_π(h) | structural states reaching h; reach probability | R1:§1.3 |
| π[h←a] | local deviation | R1:§1.3 |
| Q_π(h,a) | causal value of a at h, beliefs frozen at μ_π | R1:§1.3 |
| K(D) | commitment extension (choose policy before prediction) | R1:§1.5; coupling λ in R2:§5 |
| T, T_D | decision theory (total map), its policy on D | P1 §2 |
| M_D | causal matrix, M[π,σ] = Σ μ_π(s)U(s,σ) | P2 §3 |
| ≽_M, ≻_M, G(M) | output relation, strict part, maximal elements (nonempty) | R2:§2.1 |
| Z(M) | row-normalised matrix Z_ij = M_ij − M_ii | R2:§4, R3:§8.1 |
| (J,A,M) | rectangular input: belief rows J ⊇ options A | R3:§1.2 |
| d_i | diagonal entry M_ii | R3:§5 |
| 𝔠 | cardinality of the continuum | R2:§6 |

### Within-problem criteria (R1:§1.4–1.6, §6.1)
- **C1** ex-ante optimality: T_D ∈ argmax V_D.
- **C2** structural causal dominance at positively reached h, quantifying over *all* structural
  states reaching h (including μ_π-null ones).
- **C3** ratifiability: π(h) ∈ argmax_a Q_π(h,a) at positively reached h. C3 ⇒ C2.
- **C4** commitment stability: T's commitment in K(D) agrees with T_D on positively reached h.
- **C5** existence/totality — redundant (built into "theory").
- **C6^κ** evidential optimality under a reference-policy law J_D(π,s) = κ(π)μ_π(s).

### Cross-problem axioms (R2:§2.2, R3:§2; P2 names A0–A9 in brackets)
- **A0** reduction to labelled M. **N** [A1] neutrality. **F** [A2] common positive affine.
  **R** row translations M + b1ᵀ. **P** [A3] column Pareto (all rows). **L** [A3r] restricted
  Pareto (rows of the two candidates). **D** [A4] diagonal optimality. **J** [A5] global
  ratifiability. **B** [A6] principal binary independence (across sizes). **S** [A6b] Briggs's
  self-sovereignty (same index set, both full rows preserved). **C** [A7] contraction (Sen α).
  **O** [A8] ordering (complete, transitive at each input). **Q** [A9] nontriviality.
  **Mon** diagonal monotonicity (R3:§4). **Q_J** nontriviality on a fixed universe J, |J| ≥ 3.
- Menu semantics: **C_pr** principal; **C_col** column (rectangular); **C_ref** fixed reference.
  **B_pr**, **B_col** correspondingly.

---

## 3. Catalogue of results (IDs used in verification.md and in the paper plan)

Status: ✔ checked, proof complete in source or completed by me; ⚠ needs care/ stipulation; ✎ my
addition or repair.

### Within one problem
| ID | Statement | Src | Status |
|---|---|---|---|
| W1 | C3 ⇒ C2 | R1:§1.4 | ✔ |
| W2 | Structural vs supported compatibility: with supported-only C2, exact DiD makes C2 unsatisfiable | R1:§1.4 | ✔ |
| W3 | V_{K(D)}(q) = V_D(q) (product coupling) | R1:§1.5 | ✔ |
| W4 | Universal ex-ante selection T^ex | R1:§2 Thm 1 | ✔ |
| W5 | Newcomb: C1 ⇒ O iff ε<1/4; C2,C3 ⇒ B | R1:§2 Thm 2 | ✔ |
| W6 | Local criteria: ∃T ∀D ∧C_i ⟺ ∀D ∩A_i(D) ≠ ∅ | R1:§2 | ✔ |
| W7 | Dominance–optimality conflict possible (payoffs in [0,1]) iff μ_a not all equal | R1:§3 Thm 3 | ✔ |
| W8 | Twin PD: C1 ⇒ C, C2/C3 ⇒ D | R1:§4.1 | ✔ |
| W9 | DiD: no deterministic C3 (also with ε<1/2); structural C2 OK | R1:§4.2 | ✔ |
| W10 | Bomb: inconsistent as stated; repaired: C1 ⇒ (L,L), C2/C3 ⇒ (R,L) for 0<ε<1/(M+1) | R1:§4.3 | ✔ |
| W11 | Fixed full-support structural measure selector T^ν satisfies C2 | R1:§5.1 | ✔ |
| W12 | C1+C4 theory (coherent ex-ante selector); C1 ⇏ C4 | R1:§5.1 | ✔ |
| W13 | C2, C4 inconsistent (exact Newcomb, product coupling) | R1:§5.2 | ✔ |
| W14 | Map C1–C5: min-inc {C3},{C1,C2},{C2,C4}; max {C1,C4,C5},{C2,C5} | R1:§5.3 | ✔ |
| W15 | C6^κ: Newcomb ⇒ one-box; counterfactual mugging ⇒ Refuse vs C1 Pay; C4 conflict | R1:§6 | ✔ |
| W16 | Map C1–C6^κ | R1:§6.3 | ✔ |
| W17 | Randomised Newcomb: V(p)=1+2ε+(1−4ε)p; R₁/g + R_causal = 1; feasibility δ₁/g+δ₂ ≥ 1 | R1:§7.2 | ✔ |
| W18 | Mixed: C1 may fail (discontinuous q(p)); C3 may fail (threshold Death); continuity ⇒ both exist (compactness, Kakutani) | R1:§7.3 | ✔ |
| W19 | Predicting realised samples needs extra semantics | R1:§7.3 | ⚠ informal |
| W20 | Restrictions on prediction targets: Newcomb survives all but "already reached"; in causal trees ex-ante optimum ⇒ C3 | R1:§7.4 | ✔ |
| W21 | Boolean profiles finite (≤ 2^{2^k}) | R1:§8.1 | ✔ |
| W22 | Mixed: infinitely many inequivalent problems (polynomial with n roots) | R1:§8.2 | ✔ |
| W23 | Deterministic: arbitrary matrices realisable (M_ij via exact prediction) | R1:§8.2 | ✔ (= realisability) |
| W24 | No finite benchmark suite certifies C1 for lookup tables | R1:§8.3 | ✔ |
| W25 | Skalse's diagonal requires a fixed point that does not exist for ex-ante optimisers | R1:§9.2, R2:§1.2 | ✔ |

### Commitment couplings (R2:§5)
| ID | Statement | Status |
|---|---|---|
| K1 | Every row of M_{K(D)} equals V_D, for every coupling λ | ✔ |
| K2 | Newcomb: A3–C4 reversal iff g = m(1−2ε)−c > 0, any λ | ✔ |
| K3 | Structural: O dominates B in K iff ε=0; B dominates iff ε≥1/2 and t=1−ε (S_K = supp λ) | ✔ |
| K4 | With S_K = product of supports: no dominance for 0<ε<1 | ✔ |
| K5 | Couplings: t ranges in [0, min(ε,1−ε)]; product, shared-bit, comonotone values | ✔ |
| K6 | Coupling with U ≥ W a.s. iff F_U ≤ F_W; with U > W a.s. iff F_U(x) ≤ F_W(x⁻) on supp ν_U | ✔ (Strassen/quantile) |

### Matrix rules (R2, R3)
| ID | Statement | Src | Status |
|---|---|---|---|
| X1 | Realisability: every finite real square matrix is some M_D | R1:§8.2 | ✔ |
| X2 | B ⇒ S, B ⇒ C (principal) | R2:§2.2 | ✔ |
| X3 | Map with N,F (no R): min-inc {L},{J},{P,D},{P,B},{P,S},{P,C}; max {N,F,P,O,Q} (column sums), {N,F,D,B,S,C,O,Q} (diagonal) | R2:§3 Thm 1 | ✔ |
| X4 | Maximin over rows fails P; uniform structural selector not an A0 rule | R2:§3 | ✔ |
| X5 | **N+R+C_pr ⇒ G(M)=I** (circulant embedding); {N,R,C,Q} minimal | R2:§4 Thm 2; R3:§3.1 | ✔ |
| X6 | {N,R,B,Q} minimal inconsistent (3-cycle) | R2:§4 | ✔ |
| X7 | Augmented map with R: + {R,D}, {N,R,B,Q}, {N,R,C,Q}; five maximal sets | R2:§4 | ✔ |
| X8 | Size ceiling defeats X5 | R2:§4, R3:§7.4 | ✔ |
| X9 | R ⟺ factorisation through Z | R3:§8.1 | ✔ |
| X10 | Classification of theories w.r.t. R; regret rule shows R ≠ causal rationality | R3:§8.2 | ✔ |
| X11 | Single-valued neutral selector impossible (zero 2×2) | R2:§2.1 | ✔ |

### Menu semantics (R3)
| ID | Statement | Status |
|---|---|---|
| Y1 | Law-preserving policy removal ⇒ principal restriction; arbitrary K realisable as macro-actions | ✔ ⚠ stipulation |
| Y2 | Weight-preservation theorem (fixed reference ⇔ w'=w) | ✔ |
| Y3 | Map under C_col with B_pr: min-inc {P,D},{P,B_pr},{P,S},{R,D},{N,R,B_pr,Q}; five maximal | ✔ |
| Y4 | Map under C_col with B_col: min-inc {P,D},{P,S},{R,D}; three maximal | ✔ |
| Y5 | {N,R,B_col,S,Q_J} minimal five-axiom family | ✔ |
| Y6 | Uniform column averaging satisfies N,F,R,P,B_col,C_col,O,Q,Mon | ✔ |
| Y7 | Self-Esteem (relational): N+B_pr+O ⟺ ranking by a weak order of diagonal values (Podgorski) | ✔ |
| Y8 | + F: three rules; + Q + Mon: increasing diagonal | ✔ |
| Y9 | Domain threshold: sizes ≤2 insufficient; sizes 1–3 sufficient | ✔ |
| Y10 | λ-family: N,F,C_pr,C_col,O,Q,Mon without D | ✔ |
| Y11 | 2^𝔠 such rules (boundary set E) | ✔ |
| Y12 | Fixed-reference score vectors: top-k; 2^𝔠 via triples | ✔ |
| Y13 | **Exact domain criterion (DR)** for inconsistency of N+R+C_pr+Q | ✔ |
| Y14 | Bounded payoffs: N+R+C_pr+Q consistent; adding F restores triviality | ✔ |
| Y15 | Imperfect prediction: P_n invertible ⇒ full realisability; bounded with F | ✔ |
| Y16 | ≤k actions per info set: binary trees give transitive symmetric extensions | ✔ ⚠ needs principal restriction to non-product sets |
| Y17 | One info set + bounded actions: size ceiling, consistent | ✔ |

### Taxonomy (R2:§6)
| ID | Statement | Status |
|---|---|---|
| Z1 | N,F,O: 2^𝔠 rules (orbits of N_t); finite benchmarks cannot certify P or D | ✔ |
| Z2 | N,F,B without O: 2^𝔠 (ratio set E) | ✔ |
| Z3 | N,F,S,O: 2^𝔠 rules identical on all binary problems | ✔ |

### Mixed & evidential (R2:§7–8)
| ID | Statement | Status |
|---|---|---|
| M1 | Canonical mixed extension: g(p)=pᵀM, V(p)=pᵀMp | ✔ stipulation |
| M2 | P_m + J_m jointly satisfiable (trembling Kakutani, η ↓ 0) | ✔ |
| M3 | {P_m,D_m}, {J_m,D_m} inconsistent | ✔ |
| M4 | N + D_m inconsistent for single lotteries (identity matrix) | ✔ |
| M5 | {N,R,C_m,Q} minimal with conditional-renormalisation contraction; support contraction allows a nonconstant rule | ✔ |
| M6 | Two evidential semantics: reference-policy (gives diagonal) vs conditioning on realised action under known mix (gives ratifiability) | ✔ |

---

## 4. Corrections ledger (what changed between rounds)

1. P1 thesis "no theory optimal on all fair problems" → false (W4).
2. P1 "CDT ≈ C2+C3", "EDT ≈ C6", "FDT ≈ C1" → too strong / need semantics (R1:§9.4).
3. P1 Bomb (agent sees bomb) → inconsistent predictor unless it targets π(h_bomb); four policies (W10).
4. P1 T3 hope (Arrow-style family among C1–C6) → none: only singletons/pairs (W14, W16).
5. R1 R6 used product coupling and exact prediction → R2: C2–C4 Newcomb reversal holds only at ε=0
   under every coupling; A3–C4 reversal holds whenever g>0 (K2–K3).
6. R1 cited Briggs §6 generally → R2/R3: Briggs's theorem is exactly P+S (pp. 21–24).
7. P2 lead "A3r + A8 on cyclic matrix" → sharpened: L alone is inconsistent with nonempty choice.
8. R2 T3 (three rules) → R3: core is Podgorski's Self-Esteem Theorem (attribution).
9. P3 dichotomy → false as stated; depends on menu semantics (R3 verdict).
10. R2 "B ⇒ S" holds for B_pr, not B_col (R3:§2).
11. R2 E2 "needs unbounded menus" → R3 makes exact: (DR) criterion; bounded payoffs need F.
12. Bell et al. title: "Reinforcement Learning in Newcomblike Environments" (not "Problems").
13. Basu Mallik & Bhattacharya 2026: only abstract verified.

---

## 5. Plan of the paper (constructive order, not chronological)

1. Introduction & history.  2. Decision problems with prediction (model, fairness,
well-definedness, local deviations, stipulations).  3. Within-problem criteria; the possibility
theorem (W4) and the local-criteria lemma (W6).  4. The witnesses (Newcomb + characterisation W7,
Twin PD, DiD, Bomb, mugging).  5. Commitment and the within-problem consistency map (W12–W16,
K1–K6).  6. Robustness (W17–W20).  7. The causal matrix and cross-problem axioms (X1, X2, X9–X11).
8. Pairwise reduction theorem (X3).  9. Row-baseline invariance and contraction: circulant
theorem, augmented map, exact domain criterion and physical restrictions (X5–X8, Y13–Y17).
10. Menu semantics (Y1–Y6). 11. What characterises ex-ante evaluation (Y7–Y12).  12. Types and
certification (W21–W24, Z1–Z3).  13. Mixed policies and evidential semantics (M1–M6).
14. Discussion: what is known, what is new, final thesis, open questions.
Appendix A: register of stipulations. Appendix B: table of all results with provenance.

---

## 6. Map from this catalogue to the LaTeX paper (`latex/decision_theory.pdf`)

| Catalogue IDs | Paper |
|---|---|
| model, Lemma R_h / idle prescription | §2, Def. 2.1–2.5, Lemma 2.6 |
| W1, W2, W4, W6 | Prop. 3.5, §3.1 remark, Thm. 3.6, Lemma 3.7 |
| W5, W7, W8, W9, W10, mugging | Prop. 4.1, Thm. 4.2, §4.2, Prop. 4.3, Props. 4.4–4.5, §4.5 |
| W3/K1, W11–W16 | Prop. 5.2, Props. 5.4–5.6, Thm. 5.7, Prop. 5.9, Thm. 5.10 |
| K2–K6 | Prop. 5.11 (noisy commitment), Prop. 5.12 (Strassen criterion) |
| W17–W20 | Prop. 6.1, Prop. 6.2, Thm. 6.3, Remark 6.4, Prop. 6.5 |
| X1, W25, X11, X2, X9, X10 | Thm. 7.2, Remark 7.3, §7.2, Lemma 7.6, Thm. 7.8, Prop. 7.9 |
| X3, X4 | Thm. 8.1, Props. 8.2–8.6 |
| X5–X8, Y13–Y17 | Lemmas 9.1–9.2, Thm. 9.3, Props. 9.4–9.5, Thm. 9.6, Thm. 9.7, Props. 9.8–9.11 |
| Y1–Y6 | Prop. 10.1, Def. 10.2, Thm. 10.3, Thms. 10.4–10.6, Prop. 10.7 |
| Y7–Y12 | Thm. 11.1, Cor. 11.2, Prop. 11.3, Thm. 11.4, Props. 11.5–11.6 |
| W21–W24, Z1–Z3 | §12, Props. 12.1–12.5 |
| M1–M6 | §13, Props. 13.1–13.4, §13.3 |
| final thesis, open questions, provenance table | §14, Table 1 |
| stipulations | Appendix A |

Corrections made while typesetting (beyond the ledger in §4):
- Podgorski's Self-Esteem Theorem is about *overall-value* theories satisfying IIA; his tournament
  theory escapes it (R3 had called it "the Self-Esteem Theorem of his tournament decision theory").
- Briggs's P+S conflict needs ≥ 3 options (benchmark theory satisfies both with two); CDT satisfies P
  and violates S; EDT and benchmark theory satisfy S and violate P.
- The "absent-minded driver" vocabulary: "modified multiself consistency" is Piccione–Rubinstein's,
  "action-optimality" is Aumann–Hart–Perry's.
- Cooper, Oesterheld & Conitzer (2024) is arXiv:2411.04462, "Can CDT rationalise the ex ante optimal
  policy via modified anthropics?"; distinct from Oesterheld & Conitzer's de se working paper.

Literature verification records (per entry, with sources) are in `notes/literature/`; the
non-printing `verification` field in `latex/refs.bib` keeps the provenance of every entry.
