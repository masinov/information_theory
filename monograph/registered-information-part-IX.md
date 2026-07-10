# Registered Information over Contrast Domains

## Part IX: The Enriched Evaluation

---

## 67. Purpose: the third rung

The coefficient discipline of Remark 40.3 has run through the manuscript as a promise with two installments paid. The **exact** rung evaluates anomalies as intervals of partitions — complete for the exact obstructions (§37), discrete, and discontinuous under corruption (Proposition 40.2). The **Shannon** rung evaluates them in bits — the functional $\nu_{\mu,q}$ of Part VII, nonnegative, *additive along chains*, and jointly faithful. The **enriched** rung — deficiency-valued, the one Remark 24.7 typed, Proposition 40.1 stabilized, and Remark 55.5 listed as the coupling coordinate's third invariant — has been named at every appearance and constructed at none. Parts VII and VIII closed by calling it in: Proposition 53.2's chain additivity as the target identity, Lemma 37.4's composition law as the intended cocycle law, and Part VIII's corruption exhibits — the decay curve, the threshold, the scheduling gap, the counterfeit quantum — as the waiting test evaluations.

Part IX pays the third installment, and the announced expectation is confirmed as a theorem with an unexpected sharpening. The enriched evaluation $\nu_\delta$ — the Le Cam deficiency of an interval's lower endpoint for its upper — is nonnegative, **intrinsically faithful** (zero exactly on degenerate intervals, with no $q$-nullity proviso: the first evaluation in the manuscript that detects the geometry unaided), and monotone; but chain additivity **degrades to the triangle inequality**, and the degradation is strict *already on exact three-element partition chains, before any noise enters the theory* (Theorem 69.3: legs $\tfrac12 + \tfrac12$ against a span of $\tfrac23$, every value certified on both sides). The structural reading is the part's organizing statement: **additivity is a potential phenomenon.** The Shannon evaluation is additive because it is a coboundary — $\nu_{\mu,q}([a,b]) = \varphi(b) - \varphi(a)$ for the entropy potential $\varphi = I_\mu(q; [Z]_{(\cdot)})$ — while the enriched evaluation provably admits no potential, and what replaces exactness is an *ordered* structure: the subadditivity defect is a canonical nonnegative 2-cocycle whose vanishing locus is characterized (aligned triples: those certified by a common decision problem, with erasure interpolation as the canonical geodesic family). This resolves the interval-cohomology program of §43 in a deflationary but exact direction (Remark 69.5).

Around the centerpiece, the part proves what the enriched rung is *for*. A **partition formula** (Proposition 69.1) computes the enriched value of every exact interval in closed form — $1 - 1/k$ in the worst splitting arity $k$ — so the four canonical quanta of Theorem 54.1 all evaluate to $\tfrac12$, and a **half-gap theorem** follows: nondegenerate exact intervals have enriched evaluation at least $\tfrac12$, so values in $(0, \tfrac12)$ *certify grading* — the exact/graded boundary is metrically visible (Proposition 69.2). A **rung transfer function** (Theorem 70.2) links the Shannon and enriched evaluations exactly on binary-symmetric classes, $I = 1 - h(\tfrac12 - \nu_\delta)$, whence the Shannon rung is *the square* of the enriched rung near annihilation — the quantitative content of Remark 40.3's claim that stable measurement lives at the enriched level — while the counterfeit channel exhibits the one-sided exception where the rungs agree at first order (Remark 70.3). Part VIII's exhibits then evaluate in closed form: the blind decay of the policy bit is the square law $\tfrac12(1-\varepsilon)^2$ with a soft zero at $1$; the targeted decay is piecewise linear, $\tfrac12\max(0,\, (1-\varepsilon)\tau - \varepsilon)$, with a hard zero exactly at Lemma 62.1's threshold; the scheduling gap is $\delta^2/2$; and the coupling fiber's enriched width is $\tfrac12$, completing Remark 55.5's three-rung column (§71). Worked example K tabulates all three rungs on one configuration.

**Assumptions and conventions.** (A1), (A5), (A6) throughout; (A2) relaxed as in Part III. Deficiency and Le Cam distance are as fixed in §40: $\delta(E, F) = \inf_M \sup_Z \mathrm{TV}\big((M \circ E)(\cdot \mid Z),\, F(\cdot \mid Z)\big)$ over channels $M$, with $\mathrm{TV} = \tfrac12 L_1$, and $\Delta(E,F) = \max(\delta(E,F), \delta(F,E))$ [Le Cam 1964; Torgersen 1991]. Under (A6) all output spaces are finite, so every deficiency in this part is a finite linear program: infima are attained, and every stated value is proved by a **certificate pair** — an explicit channel for the upper bound and an explicit decision problem for the lower (§68.3). A partition $\pi \in \mathrm{Part}(D)$ is evaluated through its canonical experiment $E_\pi(\cdot \mid Z) = \delta_{[Z]_\pi}$. Part IX presupposes Parts I–VIII and modifies nothing in them; its debt was recorded in status ledgers only, so for the first time no backward discharge pointers are required.

---

## 68. The evaluation, and the certificate discipline

> **Definition 68.1 (enriched evaluation).** For a Blackwell interval $[E, F]$ (experiments on $D$ with $E \preceq_B F$), the **enriched evaluation** is the deficiency of the lower endpoint for the upper:
> $$
> \nu_\delta\big([E, F]\big) \;=\; \delta(E, F) \;=\; \inf_M \ \sup_{Z \in D}\ \mathrm{TV}\big((M \circ E)(\cdot \mid Z),\, F(\cdot \mid Z)\big).
> $$
> Exact intervals $[a, b]$ in $\mathrm{Part}(D)$ are evaluated as $\nu_\delta([E_a, E_b])$. (For the endpoint pairs of non-monotone structures, where $a \le b$ fails, the symmetrized distance $\Delta$ is the descriptive substitute, mirroring Definition 53.1's parenthetical; the calculus below is developed for the monotone case.)

> **Proposition 68.2 (basic laws).**
> 1. **(Nonnegativity; intrinsic faithfulness.)** $\nu_\delta \ge 0$, and $\nu_\delta([E,F]) = 0$ iff $E \equiv_B F$: since $E \preceq_B F$ gives $\delta(F, E) = 0$, vanishing of $\delta(E,F)$ is Blackwell equivalence. There is no analogue of Proposition 53.2(3)'s $q$-nullity proviso: **the enriched evaluation detects every nondegenerate interval by itself**, where the Shannon evaluation needed a supremum over questions (Proposition 53.2(4)).
> 2. **(Triangle inequality.)** For $E \preceq M \preceq F$: $\nu_\delta([E,F]) \le \nu_\delta([E,M]) + \nu_\delta([M,F])$.
> 3. **(Monotonicity.)** If $[E, F] \subseteq [E', F']$ (i.e. $E' \preceq E \preceq F \preceq F'$), then $\nu_\delta([E,F]) \le \nu_\delta([E',F'])$.
> 4. **(Attainment.)** Under (A6) the infimum is attained and $\nu_\delta$ is computable as a finite linear program.
>
> *Proof.* 1 is the definition plus Blackwell–Sherman–Stein. 2: if $M_1$ achieves $\mathrm{TV} \le t_1$ for $[E, M]$ and $M_2$ achieves $t_2$ for $[M, F]$, then, channels being TV-contractions, $\mathrm{TV}(M_2 M_1 E, F) \le \mathrm{TV}(M_2 M_1 E, M_2 M) + \mathrm{TV}(M_2 M, F) \le t_1 + t_2$ candidatewise. 3: write $E = N \circ E'$ and $F' \supseteq$-side as $F = G \circ F'$; channels through $N$ are a subset of channels from $E'$, giving $\delta(E', F) \ge$-comparison in the stated direction on the lower side, and post-composition with $G$ handles the upper: from $M'$ near-optimal for $[E', F']$, $G M'$ serves $[E', F]$, and restriction serves $[E, F]$. 4: the feasible set is a product of simplices and the objective piecewise linear. $\square$

> **Proposition 68.3 (certificate discipline).** For every prior $\pi$ on $D$ and loss $L$ with values in $[0,1]$, the Bayes risks satisfy
> $$
> r_{\pi, L}(E) \;-\; r_{\pi, L}(F) \;\le\; \nu_\delta\big([E,F]\big),
> $$
> so any decision problem exhibits a lower bound; any explicit channel exhibits an upper bound; and a matching pair proves an exact value. (For $[0,1]$-losses, $|\!\int L\, dP - \int L\, dQ| \le \mathrm{TV}(P,Q)$; take a near-optimal simulation $M$, transport $F$'s optimal rule back along it, and average over $\pi$. This is Le Cam's randomization criterion in the finite case [Le Cam 1964; Torgersen 1991].) Every value asserted in this part is proved by such a pair, and has additionally been verified by direct solution of the linear program. $\square$

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

> **Proposition 69.2 (the half-gap).** Every nondegenerate exact interval has $\nu_\delta \ge \tfrac12$ (some block splits, so some $k_B \ge 2$), while graded intervals realize every value in $(0, \tfrac12)$ (erasure legs, Theorem 69.4(2)). Hence an enriched evaluation in $(0, \tfrac12)$ **certifies grading**: the exact/graded boundary, qualitative since Part III, is metrically visible as a gap. This is the enriched face of the discontinuity results (Proposition 40.2, Theorem 62.2(1)): exact anomalies cannot decay continuously *because there is nowhere in $(0, \tfrac12)$ for them to go* — they switch, as Remark 40.3 said, rather than drift. $\square$

### 69.2 Additivity fails, strictly, already exactly

> **Theorem 69.3 (the quasi-cocycle theorem).** Chain additivity degrades to the triangle inequality, and the degradation is strict already for exact chains: on $D = \{1, 2, 3\}$ with the chain $\bot \le m \le \top$, $m = \{1 \mid 23\}$,
> $$
> \nu_\delta([\bot, m]) = \tfrac12, \qquad \nu_\delta([m, \top]) = \tfrac12, \qquad \nu_\delta([\bot, \top]) = \tfrac23,
> $$
> with subadditivity defect $\tfrac13$. Consequently **no potential exists**: there is no function $\varphi$ on experiments with $\nu_\delta([E,F]) = \varphi(F) - \varphi(E)$ on Blackwell-comparable pairs — additivity would follow, and it fails. The additivity of the Shannon evaluation is thereby explained rather than generalized: $\nu_{\mu,q}$ is the coboundary of the entropy potential $\varphi_{\mu,q}(\pi) = I_\mu(q; [Z]_\pi)$ (Proposition 53.2(2) restated), and **additivity is a potential phenomenon — a Shannon-rung privilege, lost one coefficient level up, before any noise enters.**
>
> *Proof.* The three values are instances of Proposition 69.1 ($k = 2$, $2$, $3$), each carrying its certificate pair: for $[\bot, m]$, the constant channel $(\tfrac12, \tfrac12)$ against the uniform prior on $\{1, 2\}$; for $[m, \top]$, pass the revealed block and split $\{2,3\}$ uniformly, against the uniform prior on $\{2, 3\}$; for $[\bot, \top]$, the constant uniform channel against the uniform prior on all three, giving $1 - \tfrac13 = \tfrac23$ both ways. Then $\tfrac12 + \tfrac12 > \tfrac23$. $\square$

> **Theorem 69.4 (geodesics; the alignment criterion).**
> 1. **(Common certificate $\Rightarrow$ additive.)** If a single decision problem $(\pi, L)$ with $L \in [0,1]$ certifies both legs — $r(E) - r(M) = \nu_\delta([E,M])$ and $r(M) - r(F) = \nu_\delta([M,F])$ — then the triple is additive: risks telescope, so $\nu_\delta([E,F]) \ge r(E) - r(F) = \nu_\delta([E,M]) + \nu_\delta([M,F])$, and the triangle inequality closes the gap.
> 2. **(Erasure interpolation is a geodesic.)** On any $D$ with the identity view, the erasure family $E_\lambda(\cdot \mid Z) = \lambda \delta_Z + (1-\lambda)\delta_\star$ satisfies $\nu_\delta([E_\lambda, E_{\lambda'}]) = \tfrac{\lambda' - \lambda}{2}$ for $\lambda \le \lambda'$ on a two-candidate domain — certified at every scale by the single problem "guess $Z$, uniform prior, $0$–$1$ loss" — an additive chain of arbitrary length, realizing all values in $(0, \tfrac12)$ for Proposition 69.2. (Upper certificate: pass reveals; on $\star$, reveal a further independent $\tfrac{\lambda'-\lambda}{1-\lambda}$-fraction — impossible without the candidate, so instead match the $\star$-mass and place the residual $\lambda' - \lambda$ on the uniform guess, giving $\mathrm{TV} = \tfrac{\lambda'-\lambda}{2}$; lower: Bayes errors are $\tfrac{1-\lambda}{2}$, and the gaps telescope.)
> 3. **(Non-alignment, necessarily.)** In Theorem 69.3's chain no common certificate can exist — item 1 would force additivity — and indeed the legs' certificates live on disjoint priors ($\{1, 2\}$ and $\{2, 3\}$): the defect measures the transversality of the worst-case problems. $\square$

> **Remark 69.5 (the interval-cohomology program, resolved deflationarily).** Assign $\nu_\delta$ to the $1$-simplices $(E \preceq F)$ of the order complex of experiments. The composition law of Lemma 37.4 asked whether this $1$-cochain is a cocycle; the answer is now structured. At the Shannon rung it is better than a cocycle — it is a **coboundary** of the entropy potential, which is *why* Part VII's decomposition telescopes. At the enriched rung it is not even a cocycle: the defect
> $$
> \mathsf{D}(E, M, F) \;=\; \nu_\delta([E,M]) + \nu_\delta([M,F]) - \nu_\delta([E,F]) \;\ge\; 0
> $$
> is precisely the simplicial coboundary $\mathsf{D} = \partial^* \nu_\delta$, hence automatically a $2$-cocycle (indeed exact), and the cohomological content is **not a hidden nonzero class but a canonical positivity structure**: $\mathsf{D} \ge 0$ everywhere (triangle inequality), $\mathsf{D} = 0$ exactly on aligned triples (Theorem 69.4), $\mathsf{D} = \tfrac13$ on the canonical exact exhibit. The right coefficient category is ordered — in the spirit of the ideal-valued repairs of Remark 24.6 — and what replaces exactness of a sequence is positivity of a defect. The program of §43 closes not with a new invariant lattice but with the exact statement of *which* algebraic property survives each rung: composition-exactness (exact rung, by construction), coboundary-additivity (Shannon rung, by the potential), triangle-with-computable-defect (enriched rung, by this section).

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
> 1. **(Honest.)** $\nu_\delta = \tfrac12$ (Proposition 69.1; the half-gap value).
> 2. **(Blind, square law with soft zero.)** Under independent uniform clutter at rate $\varepsilon$ on both channels: $\nu_\delta(\varepsilon) = \tfrac12(1 - \varepsilon)^2$, positive for all $\varepsilon < 1$ (Theorem 70.2's computation) — the enriched form of blind immortality, decaying smoothly to zero only at total corruption.
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
> 1. The magnitude of Theorem 61.1(1)'s violation — the deficiency of the budgeted ceiling for the achieved reading — is exactly $\nu_\delta\big([E_\delta^{(2)},\ \widetilde{P}_S]\big) = \delta^2/2$: second order in the erasure budget (upper: pass any reveal, guess uniformly on the double erasure, which has probability $\delta^2$; lower: uniform-prior guessing, Bayes errors $\delta^2/2$ against $0$). The scheduling attack's profit is precisely the independence assumption's quadratic term.
> 2. The enriched width of Proposition 22.4(2)'s coupling fiber is $\tfrac12$, attained between the product coupling (Blackwell-null) and the perfect coupling (diagonal under $Z$, antidiagonal under $Z'$ — equivalent to full information for the dichotomy): $\Delta = \delta(\text{null}, \text{full}_2) = \tfrac12$, and no fiber pair exceeds it since $\delta(A, B) \le \delta(\text{null}, B) \le \tfrac12$ for dichotomies (Proposition 68.2(3)). Remark 55.5's three-rung column is complete: exact — $\sigma^{=}$ takes both $\bot$ and $\top$ on the fiber; Shannon — width $1$ bit; enriched — width $\tfrac12$. $\square$

---

## 72. Worked example K: one class, three rungs, five regimes

The policy lever's class, evaluated at every rung across the corruption regimes of Part VIII (uniform prior; blind = independent uniform clutter; targeted = optimal patterns of Lemma 62.1; entries for the admissible optimum):

| rung | honest | blind $\varepsilon = \tfrac14$ | blind $\varepsilon = \tfrac12$ | targeted $\varepsilon = \tfrac14$ | targeted $\varepsilon = \tfrac12$ |
|---|---|---|---|---|---|
| exact ($\sigma^0$) | $\tfrac12$ | — | — | — | — |
| Shannon (bits) | $1$ | $1 - h(\tfrac{7}{32}) \approx 0.242$ | $1 - h(\tfrac38) \approx 0.046$ | $1 - h(\tfrac14) \approx 0.189$ | $0$ |
| enriched | $\tfrac12$ | $\tfrac{9}{32} \approx 0.281$ | $\tfrac18 = 0.125$ | $\tfrac14$ | $0$ |

Readings, one per structural theorem. The exact row is the half-gap: at any positive rate there is no value in $(0, \tfrac12)$ for the exact quantum to take, so it is gone, not diminished (Proposition 69.2). The blind columns follow the square law — the Shannon entry is $1 - h(\tfrac12 - \text{enriched entry})$ exactly, both columns (Theorem 70.2) — and decay with soft zeros at $\varepsilon = 1$. The targeted columns are the piecewise-linear regime: the enriched entries lie on the line $\tfrac12(1 - 2\varepsilon)$ with its hard zero at the threshold (Proposition 71.1(3); the targeted-$\tfrac14$ perceived class is a $\mathrm{BSC}(\tfrac14)$, consistent across rungs). Down any column, the three rungs never disagree about *whether* the class survives; they disagree — this is the part's point — about *the geometry of its dying*: jump, square law, line. And on the honest column the two nonzero rungs report the same class at $\tfrac12$ and $1$ bit with no functional relation between them across configurations — Example E's reflection quantum shares the $\tfrac12$ with a different Shannon value ($\log_2 3 - \tfrac23$): the rungs are genuinely independent coordinates, which is why the manuscript needed all three.

Finally, the chain defect in the field: adjoin to the lever's domain a third context class to make the verdict ternary, and the exact chain $\bot \le \{c_0 \mid c_1 c_2\}\text{-lift} \le$ (full verdict kernel) reproduces Theorem 69.3's triple inside a policy design space — the Fano exchange rate of Theorem 63.2 prices the endpoints in bits additively, while the enriched pricing of the same chain is strictly subadditive with defect $\tfrac13$: **a designer budgeting classes in bits can decompose the purchase into stages; a designer budgeting worst-case simulability cannot** — stage costs overstate the direct route. The two rungs give different, and differently correct, procurement advice.

---

## 73. Status of Part IX, the endgame, and added references

Part IX has (i) constructed the enriched evaluation $\nu_\delta$ — deficiency of the interval's lower endpoint for its upper, in §40's conventions — and proved its basic laws: nonnegative, **intrinsically faithful** with no $q$-nullity proviso (the first evaluation to detect the geometry unaided), monotone under containment, triangle inequality on chains, LP-computable with the certificate discipline (channel above, decision problem below) as the section-wide proof method (Definition 68.1, Propositions 68.2–68.3); (ii) computed every exact interval in closed form — the partition formula $\nu_\delta = 1 - 1/k$ in the worst splitting arity — whence the four canonical quanta all evaluate to $\tfrac12$ and the **half-gap theorem** follows: nondegenerate exact intervals sit at $\ge \tfrac12$, values in $(0, \tfrac12)$ certify grading, and the exact strata's discontinuity is explained as *having nowhere to drift* (Propositions 69.1–69.2); (iii) proved the **quasi-cocycle theorem**, the part's centerpiece: chain additivity degrades to the triangle inequality, strictly, already on the exact three-element chain $\tfrac12 + \tfrac12 > \tfrac23$ with certificate pairs on every value — hence **no potential exists**, additivity is exposed as a coboundary privilege of the Shannon rung (the entropy potential), the aligned/geodesic chains are characterized by the common-certificate criterion with erasure interpolation as the canonical additive family, and the interval-cohomology program of §43 closes deflationarily: the defect $\mathsf{D} = \partial^*\nu_\delta \ge 0$ is a canonical exact $2$-cocycle whose *positivity structure*, not a hidden class, is the invariant (Theorems 69.3–69.4, Remark 69.5); (iv) compared the rungs: risk transfer upward, the **rung transfer function** $I = 1 - h(\tfrac12 - \nu_\delta)$ on binary-symmetric classes with its square law $I = \tfrac{2}{\ln 2}\nu_\delta^2 + O(\nu_\delta^4)$ near annihilation — Remark 40.3's stability claim, quantified — and the one-sided exception where zero-error-flavored channels keep the rungs first-order aligned, completing the continuity ladder with computed moduli (Proposition 70.1, Theorem 70.2, Remark 70.3); (v) evaluated Part VIII's exhibit stock in closed form: the lever's three curve shapes — jump, square law $\tfrac12(1-\varepsilon)^2$ with soft zero, piecewise-linear $\tfrac12\max(0, (1-\varepsilon)\tau - \varepsilon)$ with hard zero exactly at $d/(2+d)$ — the scheduling gap $\delta^2/2$, and the coupling fiber's enriched width $\tfrac12$, completing Remark 55.5's three-rung column (Propositions 71.1–71.2); and (vi) tabulated one class across three rungs and five regimes, with the procurement moral: bit-budgeting decomposes, simulability-budgeting does not (§72, Worked example K).

**The endgame.** With the third coefficient rung paid, the manuscript's completion criterion can be stated and its schedule fixed. The criterion is internal: the work closes when every promise the text has made is discharged or formally retired, and the outstanding promises are of exactly three kinds. The coefficient discipline demanded three rungs — discharged as of this part. The reduction discipline demands that each standing assumption be relaxed once — (A2) fell in Part III, (A4′) in Part IV, and **(A7) alone remains**: Part X will treat dynamical scenes, where §63's calculus becomes online control and Theorem 62.3 becomes an intrusion-detection problem, both entry points sharpened twice already. The hook discipline demands H1–H5 be built — H1–H4 are discharged, and **H5 alone remains**: Part XI will construct the multi-domain information algebra on Proposition 6.11's germ and close with a **consolidated collapse theorem** assembling every recovery result into one statement exhibiting classical information theory as the fiber of the framework over (exact, forced-policy, static, single-domain, fully-admissible). A short appendix will make §20.5's measure-theoretic reducibility argument honest. Everything else in the open ledger — the PID inside one address (Remark 57.2), topos-level coverings (Lemma 35.2), the sheafification reading of Theorem 6.7, *used* content — is deliberately **not** scheduled: those items open territory rather than complete promised arcs, and the manuscript will end by converting them into precisely named open problems. Three parts and an appendix; then the unit is rounded.

What Part IX has *not* done: the unified graded-ceiling chain — for which the half-gap is now a caution: the exact and graded clauses of Theorem 57.1 live on metrically separated scales, so a single identity must bridge the gap the enriched rung exposes; the dynamical and algebraic parts just scheduled; and the deliberately retired residue above.

**References added in Part IX:** none. The part is built from Le Cam 1964, Torgersen 1991, and Cover & Thomas 2006 — all cited since Parts III and V — and the manuscript's own results: the fifth part of the last six to add nothing.
