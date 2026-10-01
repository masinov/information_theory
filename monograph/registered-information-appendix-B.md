# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Appendix B: Computational Certificates

This appendix states the finite optimization programs, records explicit certificates, and identifies independent validation runs. An exact optimum requires matching upper and lower bounds; an LP output by itself is numerical evidence. The repeated-BSC value has its complete certificate in B.6. The general measurable case is subject to Appendix A.

### B.1 The two finite programs

**Deficiency (Parts IX, XI).** For finite experiments $E : D \to \Pr(Y_E)$, $F : D \to \Pr(Y_F)$, the deficiency $\delta(E, F) = \min_M \max_Z \mathrm{TV}(M \circ E(\cdot \mid Z), F(\cdot \mid Z))$ is the linear program: variables a column-stochastic matrix $M \in \mathbb{R}^{Y_F \times Y_E}_{\ge 0}$, slack variables $u_{Z,y} \ge |(M E_Z - F_Z)_y|$, and $t$; minimize $t$ subject to $\tfrac12 \sum_y u_{Z,y} \le t$ for every $Z$ and column sums of $M$ equal to one. Its dual is, by Le Cam's randomization criterion, a prior-and-loss pair — a decision problem — certifying the optimum from below; the in-text lower bounds are hand-chosen feasible duals, which is why each equality claim closes.

**Single-record annihilation feasibility (Parts VIII, X).** For a binary question with class-conditional average laws $\bar p_1, \bar p_2$ and rate $\varepsilon$, existence of an annihilating pattern is the linear feasibility problem in the clutter variables $Q_\bullet$ (one distribution per knowledge cell — per candidate for clairvoyant patterns, per prefix for causal ones): $(1-\varepsilon)(\bar p_1 - \bar p_2) + \varepsilon(\bar Q_1 - \bar Q_2) = 0$ with $\bar Q_i$ the induced class averages, all variables in simplices. Thresholds are located by bisection on $\varepsilon$; the closed forms in-text ($d/(2+d)$; the causal $\tfrac12$) are proved by the $L_1$ mass-balance arguments of Lemma 62.1 and Theorem 77.1, the programs serving as verification.

### B.2 Certificate index

Selected finite values, with their in-text certificate pairs (channel; decision problem). Entries marked ▸ are supplied here because the text proved them by structural argument or program only.

| value | stated at | upper certificate | lower certificate |
|---|---|---|---|
| $\delta(\bot_3, \{1\!\mid\!23\}) = \tfrac12$; $\delta(\{1\!\mid\!23\}, \top_3) = \tfrac12$; $\delta(\bot_3, \top_3) = \tfrac23$ | Thm 69.3 | in-proof (uniform split channels) | in-proof (uniform priors on $\{1,2\}$, $\{2,3\}$, $\{1,2,3\}$) |
| partition formula $1 - 1/k_B$ | Prop 69.1 | in-proof (uniform over sub-blocks) | in-proof (representatives prior) |
| erasure geodesic $(\lambda' - \lambda)/2$ | Thm 69.4(2) | in-proof (mass-matching channel) | in-proof (uniform guessing) |
| $\delta(\text{null}, \mathrm{BSC}(c)) = \tfrac12 - c$; lever decay $\tfrac12(1-\varepsilon)^2$ | Thm 70.2, Prop 71.1 | in-proof (constant midpoint) | in-proof (uniform guessing) |
| scheduling gap $\delta^2/2$; coupling width $\tfrac12$ | Prop 71.2 | in-proof | in-proof |
| annihilation threshold $d/(2+d)$; targeted lever $\tfrac12$; causal $\tfrac12$ vs clairvoyant $\tfrac13$ | Lem 62.1, Thm 62.2(3), Thm 77.1 | attack clutters in-proof ($s^\pm$ construction; cross-clutter) | $L_1$ mass balance in-proof (a valid dual: no signed measure of mass $0$ and norm $> 2$ is a difference of distributions) |
| blind decay $1 - h(\varepsilon(1 - \varepsilon/2))$; creation quantum | Thm 62.2(2), 62.3(1) | exact sufficiency computations in-proof | — (equalities, not optima) |
| detection bound $\tfrac12 \mathrm{BC}^n$, $\mathrm{BC} = 2^{-1/2}$ | Thm 78.3(3) | elementary in-proof ($\min \le \sqrt{\cdot}$; multiplicativity) | — |
| ▸ memoryless frontier of the adaptivity exhibit | Thm 76.2(1) | table B.3 below | exhaustiveness: the four maps $\{A, B\} \to \{t^*, d\}$ are all memoryless policies |
| ▸ $\varphi \otimes \varphi \succ_B \varphi$, numerically $\delta(N, N \otimes N) = 0.084$ at crossover $0.3$ | Thm 84.1(2) | strictness certificate: Proposition 23.3's posterior argument (two concordant outputs of $N\otimes N$ realize a posterior outside the one-copy posterior interval $[0.3,0.7]$, so $N \otimes N \preceq N$ is impossible; with attainment under (A6), $\delta > 0$) | the numeric value is B.1's program; only strictness, certified structurally, is used by any theorem |

### B.3 The enumeration table for Theorem 76.2

The scene of Theorem 76.2 ($D = \{1,2\} \times \{0,1\}^2$ uniform; $q = b_1 \oplus b_2$; ceiling $K_G$; baseline $\{f_1, v_2\}$; context $e_2$ per the branch-swapped table; costs and values per §63's definitions). The memoryless policies are exactly the four maps $\tau : \{A, B\} \to \{t^*, d\}$:

| policy | $E$ | $V$ (bits) | computation of $V$ |
|---|---|---|---|
| $(t^*, t^*)$ | $0$ | $0$ | $\ker \tau = \bot$; $\gamma(B) = \ker(k)$, $I(q; \cdot) = 0$ |
| $(d, t^*)$ (err on $A$) | $\tfrac12$ | $\tfrac12$ | branch $1$: $\sigma$ full, meet with $P_G$ = the two orbits ($+\tfrac12$); branch $2$: $A$-cell $\subseteq \ker v_2$, no new distinction ($+0$) |
| $(t^*, d)$ (err on $B$) | $\tfrac12$ | $\tfrac12$ | symmetric (complement cells) |
| $(d, d)$ | $1$ | $0$ | $\ker \tau = \bot$ again — Proposition 63.3's $\bar d$ pathology |

The adaptive policy "err on $A$ iff $k = 1$" has $E = \tfrac14$, $V = \tfrac12$ (Theorem 76.2's proof), strictly dominating. All five $(E, V)$ policy pairs were additionally re-derived by machine over the eight-candidate partition lattice (join = common refinement; meet = transitive closure of the union, computed by union–find).

### B.4 Reproducibility note

Every randomized structural check reported in the text (transport commutations of Lemma 83.2: $200$ instances per law; the collapse-axis commutations) is a finite identity test over partitions of sets of size at most $24$, fully specified by the lemma statements plus the two lattice-operation algorithms named in B.3. No theorem's proof depends on a computation: in every case the computation verifies a proof given in-text, or (the two ▸ rows) the certificate is stated here.


### B.5 Review-run checks (2026-10-01)

The historical random-test counts above are reports from the original manuscript, not runs certified by this review. The new independent [check script](../review/check_finite_claims.py) uses NumPy/SciPy and a separately implemented row-stochastic deficiency LP; it does not call the companion papers' shared solver. Run from the repository root:

```sh
/usr/bin/python3 docs/information_theory/review/check_finite_claims.py
```

The adjacent [JSON results](../review/finite-check-results.json) record 57,600 saturation checks, 76 comparable-partition deficiency checks, the strict triangle example, repeated BSC deficiency `.084`, the selective-replacement and absorbed-edge counterexamples, the four-policy frontier and adaptive point, AND deficiency `.1`, and the ε-family values. Assertions use numerical tolerances; these checks supplement the proofs rather than replace exact certificates. The earlier claim that every numerical value already has an explicit displayed optimal certificate pair is too strong: the repeated-BSC value is an independently reproduced LP optimum and now has the explicit exact certificate in B.6. The detection row gives the Bhattacharyya bound for the uniform forged marginal; arbitrary fixed marginals have no larger coefficient, and Appendix D.7 gives a sharper exact minimax risk.

### B.6 Exact certificate for repeated BSC(0.3)

Write channels as state-by-output matrices in this paragraph. A one-copy output `0` is sent by the simulator to `(00,01,10,11)` with probabilities `(.58,.21,.21,0)`; output `1` is sent with probabilities `(0,.21,.21,.58)`. Applied to BSC(.3), this produces rows

```
(.406,.21,.21,.174),
(.174,.21,.21,.406).
```

The target independent two-copy rows are `(.49,.21,.21,.09)` and `(.09,.21,.21,.49)`. Each row differs in TV by `.084`, giving the upper bound.

For the lower bound, use binary guessing with prior probabilities `(.3,.7)` and zero–one loss. One copy has Bayes error `.3`. Two copies have Bayes error `.063+.063+.063+.027=.216`. The risk gap is `.084`, so Proposition 68.3 closes the bound exactly. All displayed decimals are terminating rational values, not rounded LP outputs. Marginalization proves the reverse deficiency is zero.


### B.7 Structural integration checks

Run `/usr/bin/python3 docs/information_theory/review/check_integrated_claims.py` from the repository root. The [checker](../review/check_integrated_claims.py) exhausts 19 partition sublattices for D.8, all 729 nested graph pairs on four vertices for D.9, and 4,096 binary three-bag constraint systems for D.10, including separate empty-separator cases. It also reconstructs D.12's globally coherent parity example. The [JSON output](../review/integrated-check-results.json) records the results. These checks validate finite instances independently of the general proofs.

The same structural checker verifies D.13 on all 225 pairs of four-point partitions, comparing both operator compositions, saturation at their meet, and the rectangular incidence criterion on every subset.

The integration checker also verifies all 60 contexts of the witness-hierarchy examples with two through five views, including the distinct empty-context witness formula in Theorem 38.4.
