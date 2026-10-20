# Verification log

Every result in the catalogue of `guide.md` was re-derived line by line. This file records (a) the
checks that needed more than reading, and (b) the places where the paper must be more precise than
the raw outputs. No result was found to be false; several needed a sharper statement.

## A. Points the paper must make precise

1. **Neutrality across label sets.** The circulant proof (X5) and the five-axiom proof (Y5)
   transport choices between *different* label sets. N must be stated as equivariance under every
   bijection σ : I → I′ (G(σ·M) = σ(G(M)), and likewise for the relation), not only permutations
   of a fixed I.
2. **Invariances act on the relation.** {N,R,B,Q} (X6) normalises the diagonal of a *strict
   comparison*; R and F must therefore be imposed on ≽_M, not only on G(M).
3. **C4 is a cross-problem criterion.** It relates D and K(D); the class must be closed under the
   (tagged, well-founded) commitment constructor. Say so where C4 is defined.
4. **R_h(π) vs R_h(π[h←a]).** Equal because h is not repeated on a path (the deviation at h cannot
   change whether h is reached when the plan is fixed). Used in Q_π and in the T^ν proof.
5. **The T^ν proof (W11)** uses: for s ∉ R_h(π), U(s, π[h←a]) = U(s, π) (h is off the path, so its
   prescription is idle). State it.
6. **C6^κ conventions.** −∞ on null action-conditioning events; information sets that are null
   under J_D impose no constraint. Full support of κ makes every information set reachable under
   some policy non-null.
7. **K(D) with a coupling.** R1 uses the product coupling with S_K = ∏ supp μ_q; R2 generalises to
   any coupling λ and distinguishes S_K = supp λ from S_K = ∏ supp μ_q. The paper defines K_λ(D)
   once and states which convention each result uses. R1's C2–C4 conflict (exact prediction) holds
   under every coupling since at ε = 0 all supports are singletons.
8. **Strict coupling criterion (K6).** Sufficiency via the common-quantile coupling: for v ∈ (0,1],
   x = F_U^{-1}(v) satisfies F_W(x⁻) ≥ F_U(x) ≥ v, so F_W^{-1}(v) < x (finite support). Write it out.
9. **Equivariant transport in Z1** is well defined because N_t has trivial stabiliser under
   relabelling × positive affine maps (checked: identity forces b=0, a=1; the swap forces a=−s/t<0).
10. **Mixed uniform-over-winners witnesses for M5.** C_m (conditional renormalisation) requires
    G(M|_K) = G(M) ∩ K whenever the latter is nonempty (Arrow's choice axiom), not only Sen's α.
    Checked for: diagonal maximisation, fixed-label rule (both binary-independent weak orders), and
    the all-tied rule. Row-range maximisation is used only as the witness *omitting* C_m. ✔
11. **(DR) graph.** Reach(x) is reflexive. Q in the converse direction uses closure of the domain
    under relabelling: a nonempty proper G(M₀) is moved by some permutation.
12. **Bounded-payoff rule (Y14).** Acyclicity: an edge i→j forces M_ii > r ≥ ½ ≥ 1−r > M_jj, so no
    vertex has both an in- and an out-edge; all paths have length ≤ 1.
13. **F restoring triviality on [0,1].** Decompose M ↦ αM (F, stays in [0,1]) ↦ αM + row shifts
    (R, stays in [½−α, ½+α]); each step stays inside the domain, as required by restricted
    invariance. Fill unused circulant entries with ½.
14. **Inverse of P_n.** P_n = (1−η)I + (η/n)J; P_n^{-1} = (1−η)^{-1} I − η((1−η)n)^{-1} J (checked by
    multiplication). Row-absolute-sum bound (1+η)/(1−η), uniform in n.
15. **Binary-tree count.** Depth-m perfect-recall binary tree: 2^m − 1 information sets, 2^m paths,
    L = 2^{2^m−1−m} policies per path.
16. **Briggs matrices.** In M⁺ column 1 = (0,0,1)ᵀ weakly dominates column 2 = 0 (strict in row 3); in
    M⁻ the reverse. Rows 1, 2 and the principal {1,2} block coincide.
17. **Self-Esteem proof.** The constant principal pair {1,3} forces 1∼3 by N + B + completeness
    (swap fixes the 2×2 block, so a strict comparison would be reversed). The pair {3,2} in H has
    principal block [[p,t],[u,s]] (ordered 3,2). ✔
18. **λ-family Mon.** Raising d_i removes only incoming edges to i, adds only outgoing edges from i;
    other vertices' in-edges can only increase, so the "chosen ≻ rejected" pattern is monotone.
19. **2^𝔠 boundary family (Y11).** Raising d_i never creates an incoming edge at the boundary: the
    gap d_k − d_i only decreases; equality from above may delete the edge (allowed). ✔
20. **Score triples (Y12).** Raising v_j lowers every gap sum for j, so a zero-sum boundary rejection
    can only become a negative-sum non-rejection.
21. **Randomised Newcomb (W17).** Both the distribution-observing and the sample-predicting
    predictors give V(p) = 1 + 2ε + (1−4ε)p (checked by expansion).

## B. Arithmetic re-checks (all ✔)

- Newcomb: V(O) − V(B) = 2(1−ε) − (1+2ε) = 1 − 4ε.
- W7: V(b) − V(a) = (1−c)δ − c > 0 ⟺ c < δ/(1+δ); V(a) ≥ c > 0 so b is the unique maximiser.
- Bomb values (L,L) −Mε, (L,R) −Mε−(1−ε), (R,L) −(1−ε), (R,R) −1; C1 unique (L,L) ⟺ ε < 1/(M+1).
- Mugging: V(Pay) = (r−c)/2; e(Pay) = −c, e(Refuse) = 0.
- Circulant distinct differences: 2^j − 2^i = 2^i(2^{j−i} − 1) identifies (i, j−i); |d| ≤ 2^{k−1} − 1;
  m > 2(2^{k−1}−1) separates residues.
- {L} cycle on K: 1≻2 (rows 1,2), 2≻3 (rows 2,3), 3≻1 (rows 1,3).
- {N,R,B,Q} 3-cycle: blocks {1,2}, {2,3}, {3,1} of the circulant all equal [[0,x],[y,0]].
- Regret rule: scores (−10, −10, −1) on the 3×3 example; column 3 dominated by columns 1 and 2.
- Mixed counterexample [[2,3],[0,1]]: pᵀMp = 1 + x.
- N_t orbits; M_t ratio t; M_r boundary r.

## C. Things that stay informal in the sources (flag in the paper, do not overclaim)

- W19 (predicting realised private samples): only described; the paper states it as a remark.
- Literature priority: no claim of novelty for X5 (ingredients: Fink–Ruiz embedding, Brandt's
  vertex-transitivity remark) or for the consistency maps; state as "not found in the literature
  searched".
- Basu Mallik & Bhattacharya (2026): cite only for what the abstract states.

## D. Rounds 4–5 (Part III of the paper)

Every result in Part III was re-derived. None was false; the points below needed attention.

1. **G5, exact selection.**
   - V_e(b) = Pr(N ≥ t) = Σ_{n≥t} 2^{−n−1} = 2^{−t}.
   - f(e) = T(d(E_e)) is total because e ↦ d(E_e) is computable and T halts on the class.
   - The index of x ↦ 1 − f(x) gives f(e) = 1 − f(e).
   - Expected running time is finite because E[N] < ∞. ✔
2. **G10, halting reduction.**
   - The prompt's lead ("equal iff halts") cannot be uniform, because equality with a fixed total
     T is co-c.e.; the paper uses "equal iff does not halt".
   - Two-case definition of g_e: equal to 1 − T(x) when x ∉ P and e halts within |x| steps,
     otherwise equal to T(x).
   - Strings outside P must be arbitrarily long, so a halting e yields a witness of inequality.
   - Payoff table 2(1−b) + a. If e does not halt, b = a and the values are 2 vs 1, so T(d_e) = 0.
     If e halts, b is frozen and action 1 is better by 1, so T(d_e) = 1. ✔
3. **G9, local matching.**
   - With A ≡ 1−a, g_a is replaced and both outputs equal 1−a, so the payoff is 1.
   - With t itself, the outputs are a and 1−a, so the payoff is 0. ✔
4. **G11, five-and-ten.**
   - S ⊢ q → ψ uses determinism: under q, T(d) = 10 is refutable, so the second conjunct is vacuous.
   - □ψ → q by formalised search: the search looks only for proofs of ψ, so its first hit returns 5.
   - Löb gives S ⊢ q; an actual proof of ψ exists, so the search halts. ✔
5. **G7, non-implication.** The four alternative patterns are pairwise distinct. The payoff 1/0/2
   at z/v/w gives each direction, and agents taking 0 reproduce the baseline. ✔
6. **H2, context environments realise causal matrices (added link, not in R5).**
   - States b ∈ A, μ_a = δ_a, U(b,a) = u(a, c(b)), so M[b,a] = W_{E,b}(a) and M[a,a] = V_E(a).
   - The identity context with u(a,x) = M[x,a] realises any 2×2 rational matrix.
   - Only "independent ⇒ equal rows" holds for environments. The converse holds for the matrix,
     not the environment, and the paper says so.
7. **H6, complete map.**
   - Witness properties re-checked one by one:
     - slot: all but CF5;
     - port: CF2, 3, 5, 6;
     - base: CF4, 5, 6;
     - flat: CF2, 5, 10;
     - all four: CF1, 7, 8.
   - Maximality: adding any axiom to each maximal set completes a core.
   - Exhaustiveness: case split on CF5 / CF3 / CF4 / CF10, as in the paper. ✔
8. **H8, conditional map.** Re-derived independently.
   - κ_base satisfies CF9′ and CF10′, so {CF4,CF5,CF10} and {CF5,CF6,CF10} disappear.
   - {CF2,CF5,CF6,CF10′} is a minimal core: deleting CF2 / CF5 / CF6 / CF10′ leaves sets
     witnessed by base / slot / flat / port.
   - Exhaustiveness: CF3 → port; CF4 or CF9′ → base; else CF10′ with ¬CF6 → flat, CF10′ with
     ¬CF2 → base, ¬CF10′ → port. ✔
9. **H9, global-total map.** The diagonal component c(d,a) = τ(d) is constant in a, so CF3, CF4,
   CF6 and CF9 each force W. Maximal sets checked as for H6; flat is ratified by any globally total
   τ. ✔
10. **Literature checks for Part III.** Records are in notes/literature/clusterD_notes.md and
    clusterE_notes.md.
    - Williamson's collapse argument is confirmed on pp. 30–31 of the 2015 Amsterdam Colloquium
      paper.
    - Logical induction: Theorem 4.6.1 is on p. 36, Definitions 4.7.1 and 4.8.2 on pp. 38 and 40.
    - Benson-Tilsen: Corollary 4.6 is "playing chicken is the only way to win".
    - Earliest written statement of the five-and-ten pattern: Drescher 2009. Löbian form: Slepnev
      2012. Chicken rule: Slepnev 2011. No one is credited with the name.
    - Nolan's "strangeness of impossibility" is not attributed in the paper, since sources disagree
      on whether he endorses it.

Informal points kept as remarks, not theorems:
- the König compactness remark;
- "no largest decidable solvable class";
- the impossible-world representation of kernels;
- the exploration-scope example for logical induction.
