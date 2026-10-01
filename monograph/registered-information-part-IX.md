# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part IX: The Enriched Evaluation

---

## 67. Overview of Part IX

Part IX replaces the Shannon evaluation of Part VII by a decision-theoretic one. The evaluation of an interval $[E,F]$ of experiments is the **Le Cam deficiency** $\delta(E,F)$: the smallest worst-case total-variation error with which $F$ can be simulated from $E$ (§68). It requires no prior or question, detects every nondegenerate interval on its own (Proposition 68.2), and every value is certified by a pair — a simulating channel from above and a decision problem from below (Proposition 68.3).

On exact intervals the deficiency measures the worst-case number of blocks into which a block splits (Proposition 69.1); consequently no exact interval has value strictly between $0$ and $\tfrac12$, so such a value certifies noise (Proposition 69.2). Unlike the Shannon evaluation, deficiency is not additive along chains, already on three points (Theorem 69.3); triangle equality holds exactly when one decision problem is tight on both legs (Theorem 69.4). Section 70 compares the two evaluations and finds that, on binary symmetric classes, the Shannon value is asymptotically the square of the deficiency (Theorem 70.2). Section 71 evaluates the exhibits of Part VIII.

---

## 68. The evaluation, and the certificate discipline

> **Definition 68.1 (enriched evaluation).** For a Blackwell interval $[E, F]$ (experiments on $D$ with $E \preceq_B F$), the **enriched evaluation** is the deficiency of the lower endpoint for the upper:
> $$
> \nu_\delta\big([E, F]\big) \;=\; \delta(E, F) \;=\; \inf_M \ \sup_{Z \in D}\ \mathrm{TV}\big((M \circ E)(\cdot \mid Z),\, F(\cdot \mid Z)\big).
> $$
> Exact intervals $[a, b]$ in $\mathrm{Part}(D)$ are evaluated as $\nu_\delta([E_a, E_b])$. (For the endpoint pairs of non-monotone structures, where $a \le b$ fails, the symmetrized distance $\Delta$ is the descriptive substitute, mirroring Definition 53.1's parenthetical; the calculus below is developed for the monotone case.)

> **Proposition 68.2 (basic laws).**
>
> 1. **(Nonnegativity; intrinsic faithfulness.)** $\nu_\delta \ge 0$, and $\nu_\delta([E,F]) = 0$ iff $E \equiv_B F$: since $E \preceq_B F$ gives $\delta(F, E) = 0$, vanishing of $\delta(E,F)$ is Blackwell equivalence. There is no analogue of Proposition 53.2(3)'s $q$-nullity proviso: **the enriched evaluation detects every nondegenerate interval by itself**, where the Shannon evaluation needed a supremum over questions (Proposition 53.2(4)).
> 2. **(Triangle inequality.)** For $E \preceq M \preceq F$: $\nu_\delta([E,F]) \le \nu_\delta([E,M]) + \nu_\delta([M,F])$.
> 3. **(Monotonicity.)** If $[E, F] \subseteq [E', F']$ (i.e. $E' \preceq E \preceq F \preceq F'$), then $\nu_\delta([E,F]) \le \nu_\delta([E',F'])$.
> 4. **(Attainment.)** Under (A6) the infimum is attained and $\nu_\delta$ is computable as a finite linear program.
>
> *Proof.* 1 is the definition plus Blackwell–Sherman–Stein. 2: if $M_1$ achieves $\mathrm{TV} \le t_1$ for $[E, M]$ and $M_2$ achieves $t_2$ for $[M, F]$, then, channels being TV-contractions, $\mathrm{TV}(M_2 M_1 E, F) \le \mathrm{TV}(M_2 M_1 E, M_2 M) + \mathrm{TV}(M_2 M, F) \le t_1 + t_2$ candidatewise. 3: write $E'=N\circ E$ and $F=G\circ F'$. If $M'$ simulates $F'$ from $E'$ with error $t$, then $GM'N$ simulates $F$ from $E$ with error at most $t$ by TV contraction. Taking infima proves containment monotonicity. 4: the feasible set is a product of simplices and the objective piecewise linear. $\square$

> **Proposition 68.3 (certificate discipline).** For every prior $\pi$ on $D$ and loss $L$ with values in $[0,1]$, the Bayes risks satisfy
> $$
> r_{\pi, L}(E) \;-\; r_{\pi, L}(F) \;\le\; \nu_\delta\big([E,F]\big),
> $$
> so any decision problem exhibits a lower bound; any explicit channel exhibits an upper bound; and a matching pair proves an exact value. (For $[0,1]$-losses, $|\!\int L\, dP - \int L\, dQ| \le \mathrm{TV}(P,Q)$; take a near-optimal simulation $M$, transport $F$'s optimal rule back along it, and average over $\pi$. This is Le Cam's randomization criterion in the finite case [Le Cam 1964; Torgersen 1991].) Every value asserted in this part is proved by such a pair; Appendix B lists the certificates and indicates which values were also checked numerically. $\square$

---

## 69. The quasi-cocycle theorem

### 69.1 Exact intervals in the enriched metric

> **Proposition 69.1 (partition formula).** For $a \le b$ in $\mathrm{Part}(D)$,
> $$
> \nu_\delta\big([a, b]\big) \;=\; \max_{B \in a} \Big(1 - \tfrac{1}{k_B}\Big),
> \qquad k_B = \#\{\text{$b$-blocks contained in } B\}.
> $$
> The enriched value of an exact interval is a **worst-case splitting arity**, not an information measure.
>
> *Proof.* Upper: the channel sending the $a$-block $B$ to the uniform distribution on its $k_B$ sub-blocks has, at every $Z \in B$, $\mathrm{TV} = 1 - 1/k_B$; mass placed outside $B$'s own sub-blocks is wasted, and uniform is minimax within them. Lower: let $B$ attain the maximum, take the uniform prior on one representative per sub-block of $B$, and the $0$–$1$ loss of guessing the $b$-block: $E_b$ has Bayes risk $0$, while $E_a$'s output is constant across the representatives, forcing risk $(k_B - 1)/k_B$. $\square$
>
> Consequently the four canonical quanta of Theorem 54.1 all evaluate to $\tfrac12$: the parity witness interval $[\bot, P_G]$ ($k = 2$), the hierarchy $C_{k+1}$'s interval at **every arity** ($k = 2$: two orbits — the arity-independence of Theorem 54.1(2), starker here), Worked example E's reflection interval $[\bot, \mathrm{lift}(\{O_1O_2 \mid O_3\})]$ ($k = 2$), and the policy lever's class $[\bot, P_G]$. The enriched rung does not distinguish witness from reflection by value; per Part VII's dictum, the evaluation is the measure and the address is the geometry.

> **Proposition 69.2 (the half-gap).** Every nondegenerate exact interval has $\nu_\delta \ge \tfrac12$ (some block splits, so some $k_B \ge 2$), while graded intervals realize every value in $(0, \tfrac12)$ (erasure legs, Theorem 69.4). Hence an enriched evaluation in $(0, \tfrac12)$ **certifies grading**: the exact/graded boundary, qualitative since Part III, is metrically visible as a gap. This is the enriched face of the discontinuity results (Proposition 40.2, Theorem 62.2(1)): exact anomalies cannot decay continuously *because there is nowhere in $(0, \tfrac12)$ for them to go* — they switch, as Remark 40.3 said, rather than drift. $\square$

### 69.2 Additivity fails, strictly, already exactly

> **Theorem 69.3 (the quasi-cocycle theorem).** Chain additivity degrades to the triangle inequality, and the degradation is strict already for exact chains: on $D = \{1, 2, 3\}$ with the chain $\bot \le m \le \top$, $m = \{1 \mid 23\}$,
> $$
> \nu_\delta([\bot, m]) = \tfrac12, \qquad \nu_\delta([m, \top]) = \tfrac12, \qquad \nu_\delta([\bot, \top]) = \tfrac23,
> $$
> with subadditivity defect $\tfrac13$. Consequently **no potential exists**: there is no function $\varphi$ on experiments with $\nu_\delta([E,F]) = \varphi(F) - \varphi(E)$ on Blackwell-comparable pairs — additivity would follow, and it fails. The additivity of the Shannon evaluation is thereby explained rather than generalized: $\nu_{\mu,q}$ is the coboundary of the entropy potential $\varphi_{\mu,q}(\pi) = I_\mu(q; [Z]_\pi)$ (Proposition 53.2(2) restated), and **additivity is a potential phenomenon — a Shannon-rung privilege, lost one coefficient level up, before any noise enters.**
>
> *Proof.* The three values are instances of Proposition 69.1 ($k = 2$, $2$, $3$), each carrying its certificate pair: for $[\bot, m]$, the constant channel $(\tfrac12, \tfrac12)$ against the uniform prior on $\{1, 2\}$; for $[m, \top]$, pass the revealed block and split $\{2,3\}$ uniformly, against the uniform prior on $\{2, 3\}$; for $[\bot, \top]$, the constant uniform channel against the uniform prior on all three, giving $1 - \tfrac13 = \tfrac23$ both ways. Then $\tfrac12 + \tfrac12 > \tfrac23$. $\square$

> **Theorem 69.4 (alignment and erasure geodesics).** Let $E\preceq_B M\preceq_B F$ be finite experiments. Triangle equality $\delta(E,F)=\delta(E,M)+\delta(M,F)$ holds iff one finite decision problem with loss in $[0,1]$ attains both leg deficiencies.
>
> For $k\ge2$ states and erasure experiments $E_\lambda(z)=\lambda\delta_z+(1-\lambda)\delta_\star$,
> $$\delta(E_\lambda,E_{\lambda'})=(\lambda'-\lambda)(1-1/k),\qquad0\le\lambda\le\lambda'\le1.$$
>
> *Proof.* A common tight decision problem has telescoping risk gaps equal to the sum of the legs; the randomization bound and triangle inequality force equality. Conversely choose a decision problem attaining the span deficiency, which exists by finite randomization duality. Each of its leg risk gaps is bounded above by the corresponding deficiency. Since their sum attains the sum of these bounds, both are tight.
>
> For erasures, retain revealed states; on an erasure, keep an erasure with probability $(1-\lambda')/(1-\lambda)$ and otherwise draw a uniform state. Its row error is $(\lambda'-\lambda)(1-1/k)$. The uniform-prior state-guessing problem has risk $(1-\lambda)(1-1/k)$ and attains that gap. When $\lambda=1$ both channels coincide and the value is zero. The strict triangle of Theorem 69.3 therefore has no common tight problem; its two displayed prior supports overlap but do not coincide. $\square$

> **Remark 69.5 (the interval-cohomology program, resolved deflationarily).** Assign $\nu_\delta$ to the $1$-simplices $(E \preceq F)$ of the order complex of experiments. The composition law of Lemma 37.4 asked whether this $1$-cochain is a cocycle; the answer is now structured. At the Shannon rung it is better than a cocycle — it is a **coboundary** of the entropy potential, which is *why* Part VII's decomposition telescopes. At the enriched rung it is not even a cocycle: the defect
> $$
> \mathsf{D}(E, M, F) \;=\; \nu_\delta([E,M]) + \nu_\delta([M,F]) - \nu_\delta([E,F]) \;\ge\; 0
> $$
> is precisely the simplicial coboundary $\mathsf{D} = \partial^* \nu_\delta$, hence automatically a $2$-cocycle (indeed exact), and the cohomological content is **not a hidden nonzero class but a canonical positivity structure**: $\mathsf{D} \ge 0$ everywhere (triangle inequality), $\mathsf{D} = 0$ exactly on aligned triples (Theorem 69.4), $\mathsf{D} = \tfrac13$ on the canonical exact exhibit. The right coefficient category is ordered, and what replaces exactness of a sequence is positivity of a defect. The question raised by Lemma 37.4 is thereby answered not with a new invariant lattice but with the exact statement of *which* algebraic property survives each rung: composition-exactness (exact rung, by construction), coboundary-additivity (Shannon rung, by the potential), triangle-with-computable-defect (enriched rung, by this section).

---

## 70. The rungs compared

> **Proposition 70.1 (risk transfer).** For every prior $\mu$ and question $q$: $e_\mu(q \mid E) \le e_\mu(q \mid F) + \nu_\delta([E, F])$ — Bayes-error gaps at every decision problem are controlled by the enriched evaluation (Proposition 68.3 with $0$–$1$ loss), and Theorem 22.7(2) converts the control into entropic consequences. The enriched rung is thus an upper modulus for the Shannon rung; the converse fails quantitatively, as follows. $\square$

> **Theorem 70.2 (the rung transfer function; the square law).** On binary-symmetric classes — dichotomies whose experiment is Blackwell-equivalent to a $\mathrm{BSC}(c)$, $c \le \tfrac12$ — both evaluations are exact functions of $c$ and hence of each other:
> $$
> \nu_\delta = \tfrac12 - c,
> \qquad
> I = 1 - h(c) = 1 - h\big(\tfrac12 - \nu_\delta\big),
> $$
> ($I$ at the uniform prior, in bits). Near annihilation ($\nu_\delta \to 0$):
> $$
> I \;=\; \tfrac{2}{\ln 2}\,\nu_\delta^{\,2} \;+\; O(\nu_\delta^{\,4}):
> $$
> **the Shannon evaluation is the square of the enriched evaluation.** On the policy lever under blind corruption this is live: $\nu_\delta(\varepsilon) = \tfrac12(1-\varepsilon)^2$ and $I(\varepsilon) = 1 - h(\varepsilon(1 - \varepsilon/2))$, with $I / \big(\tfrac{2}{\ln 2}\nu_\delta^2\big) \to 1$ as $\varepsilon \to 1$ — numerically, the ratio is $1.0000$ already at $\varepsilon = 0.9$.
>
> *Proof.* $\delta(\text{null}, \mathrm{BSC}(c)) = \tfrac12 - c$: upper, the constant channel $(\tfrac12, \tfrac12)$, whose TV to each row is $\tfrac12 - c$; lower, uniform-prior guessing, with Bayes errors $\tfrac12$ and $c$. The mutual information of a uniform binary source through $\mathrm{BSC}(c)$ is $1 - h(c)$. Substitute $c = \tfrac12 - \nu_\delta$ and expand $h$ at $\tfrac12$: $1 - h(\tfrac12 - x) = \tfrac{2}{\ln 2}x^2 + O(x^4)$. The lever instance is Theorem 62.2(2): the XOR statistic is $\mathrm{BSC}(\varepsilon(1-\varepsilon/2))$, and $\tfrac12 - \varepsilon(1 - \varepsilon/2) = \tfrac12(1-\varepsilon)^2$. $\square$

> **Remark 70.3 (the one-sided exception; the continuity ladder completed).** The square law is a *symmetric-noise* phenomenon. The counterfeit creation channel of Theorem 62.3(1) is one-sided — the verdict $d$ is certain evidence — and there the rungs agree at first order: the created class's $q$-conditional laws separate by $\mathrm{TV} = \varepsilon$, so its enriched size is $\varepsilon/2$, while its Shannon quantum expands as $\tfrac{\varepsilon}{2} + \tfrac{\varepsilon^2}{8 \ln 2} + O(\varepsilon^3)$. The organizing reading: one-sided channels retain a zero-error-flavored component, and where zero-error content survives, the rungs march together; where noise is symmetric and the class approaches annihilation, the Shannon rung goes blind quadratically and only the enriched rung remains first-order. Remark 40.3's continuity ladder now has its moduli: the exact rung **jumps** (Proposition 40.2; the half-gap of Proposition 69.2 is the reason there is nowhere to drift); the enriched rung is the **Lipschitz scale itself** (Proposition 40.1); the Shannon rung is continuous with entropy modulus — infinitely steep where zero-error content is lost (the derivative of $1 - h(c)$ at $c = 0$), quadratically flat where classes die (the square law).

---

## 71. Part VIII's exhibits, evaluated

> **Proposition 71.1 (the lever's enriched fate: three curve shapes).** On Theorem 46.3's configuration, the enriched quantum of the policy class:
>
> 1. **(Honest.)** $\nu_\delta = \tfrac12$ (Proposition 69.1; the half-gap value).
> 2. **(Blind, square law with soft zero.)** Under independent uniform clutter at rate $\varepsilon$ on both channels: $\nu_\delta(\varepsilon) = \tfrac12(1 - \varepsilon)^2$, positive for all $\varepsilon < 1$ (Theorem 70.2's computation) — the enriched form of survival under blind corruption, decaying smoothly to zero only at total corruption.
> 3. **(Targeted, piecewise linear with hard zero.)** Against optimal targeted patterns at common rate $\varepsilon$, with honest $q$-conditional TV separation $\tau$ ($= d/2$; $\tau = 1$ for the lever): the achievable perceived separation is exactly $\max\big(0,\ (1-\varepsilon)\tau - \varepsilon\big)$ in TV, so the enriched quantum is
> $$
> \nu_\delta(\varepsilon) \;=\; \tfrac12 \max\big(0,\ (1-\varepsilon)\tau - \varepsilon\big),
> $$
> linear in $\varepsilon$ with a **hard zero exactly at Lemma 62.1's threshold** $\varepsilon^* = \tau/(1+\tau) = d/(2+d)$ — for the lever, $\tfrac12\max(0, 1 - 2\varepsilon)$, dead at $\tfrac12$.
>
> Theorem 62.2's trichotomy is thereby a statement about **curve shapes**: a jump (exact), a square law with soft zero at $1$ (blind), a line with hard zero at $d/(2+d)$ (targeted).
>
> *Proof.* 2 is Theorem 70.2. 3: the adversary minimizes $\tfrac12\lVert (1-\varepsilon)(\bar p_1 - \bar p_2) + \varepsilon(\bar Q_1 - \bar Q_2)\rVert_1$; as in Lemma 62.1, $\bar Q_1 - \bar Q_2$ ranges over exactly the signed measures of total mass $0$ and $L_1$ norm $\le 2$, so the minimum is $\tfrac12\max(0, (1-\varepsilon)\cdot 2\tau - 2\varepsilon)$; the perceived class is a dichotomy of TV separation $t$, whose enriched size is $\delta(\text{null}, \cdot) = t/2$ (constant-midpoint channel; uniform-prior certificate). $\square$

> **Proposition 71.2 (scheduling gap; coupling width).**
>
> 1. The magnitude of Theorem 61.1(1)'s violation — the deficiency of the budgeted ceiling for the achieved reading — is exactly $\nu_\delta\big([E_\delta^{(2)},\ \widetilde{P}_S]\big) = \delta^2/2$: second order in the erasure budget (upper: pass any reveal, guess uniformly on the double erasure, which has probability $\delta^2$; lower: uniform-prior guessing, Bayes errors $\delta^2/2$ against $0$). The scheduling attack's profit is precisely the independence assumption's quadratic term.
> 2. The enriched width of Proposition 22.4(2)'s coupling fiber is $\tfrac12$, attained between the product coupling (Blackwell-null) and the perfect coupling (diagonal under $Z$, antidiagonal under $Z'$ — equivalent to full information for the dichotomy): $\Delta = \delta(\text{null}, \text{full}_2) = \tfrac12$, and no fiber pair exceeds it since $\delta(A, B) \le \delta(\text{null}, B) \le \tfrac12$ for dichotomies (Proposition 68.2(3)). Remark 55.5's three-rung column is complete: exact — $\sigma^{=}$ takes both $\bot$ and $\top$ on the fiber; Shannon — width $1$ bit; enriched — width $\tfrac12$. $\square$

---

## 72. Worked example K: one class, three rungs, five regimes

The policy lever's class, evaluated at every rung across the corruption regimes of Part VIII (uniform prior; blind = independent uniform clutter; targeted = optimal patterns of Lemma 62.1; entries for the admissible optimum; the targeted entries use the attack that is optimal for the enriched rung, which need not minimize the Shannon value):

| rung | honest | blind $\varepsilon = \tfrac14$ | blind $\varepsilon = \tfrac12$ | targeted $\varepsilon = \tfrac14$ | targeted $\varepsilon = \tfrac12$ |
|---|---|---|---|---|---|
| exact ($\sigma^0$) | $\tfrac12$ | — | — | — | — |
| Shannon (bits) | $1$ | $1 - h(\tfrac{7}{32}) \approx 0.242$ | $1 - h(\tfrac38) \approx 0.046$ | $1 - h(\tfrac14) \approx 0.189$ | $0$ |
| enriched | $\tfrac12$ | $\tfrac{9}{32} \approx 0.281$ | $\tfrac18 = 0.125$ | $\tfrac14$ | $0$ |

Readings, one per structural theorem. The exact row is the half-gap: at any positive rate there is no value in $(0, \tfrac12)$ for the exact quantum to take, so it is gone, not diminished (Proposition 69.2). The blind columns follow the square law — the Shannon entry is $1 - h(\tfrac12 - \text{enriched entry})$ exactly, both columns (Theorem 70.2) — and decay with soft zeros at $\varepsilon = 1$. The targeted columns are the piecewise-linear regime: the enriched entries lie on the line $\tfrac12(1 - 2\varepsilon)$ with its hard zero at the threshold (Proposition 71.1(3); the targeted-$\tfrac14$ perceived class is a $\mathrm{BSC}(\tfrac14)$, consistent across rungs). Down a noisy column the zero-error rung and the other two rungs disagree about whether content survives at all. The two quantitative rungs agree about survival — it persists under blind corruption and dies at the targeted threshold — and disagree, which is the point of this part, about *the geometry of its decay*: jump, square law, line. And on the honest column the two nonzero rungs report the same class at $\tfrac12$ and $1$ bit with no functional relation between them across configurations — Example E's reflection quantum shares the $\tfrac12$ with a different Shannon value ($\log_2 3 - \tfrac23$): the rungs are genuinely independent coordinates, which is why the monograph needed all three.

Finally, the chain defect has a design reading. Theorem 69.3's chain $\bot \le \{1 \mid 23\} \le \top$ on three candidates is the situation of a designer who refines a ternary distinction in two stages, first separating one candidate and then the remaining two. Evaluated in bits, the two stages add up to the direct refinement (Proposition 53.2); evaluated by deficiency, the stages cost $\tfrac12 + \tfrac12$ while the direct refinement costs $\tfrac23$. **A designer budgeting classes in bits can decompose the purchase into stages; a designer budgeting worst-case simulability cannot** — stage costs overstate the direct route. The two evaluations give different, and differently correct, advice.

---

## 73. Summary of Part IX

Linear-programming duality and explicit certificate pairs establish the partition formula, the half-gap, the strict triangle example, the alignment criterion for triangle equality, and the erasure geodesics (Propositions 69.1–69.2, Theorems 69.3–69.4). Shannon evaluation is additive along a fixed chain; deficiency is only subadditive. The square law is a local expansion on binary symmetric classes, not an identity for arbitrary experiments, and one-sided channels behave differently (Remark 70.3). Appendix B distinguishes exact certificates from numerical checks.

**References added in Part IX:** none.
