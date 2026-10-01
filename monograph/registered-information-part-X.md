# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part X: Dynamical Scenes

---

## 74. Finite-horizon information and commitment

Finite trajectories are contrast domains, but a stochastic stream must satisfy joint causal factorization, not merely causal one-coordinate marginals. Online policies obey a horizon-level entropy bound and can improve the achievable cost/value frontier. Causal attacks form a restricted feasible class whose annihilation threshold must be compared with the same unconstrained model. Provenance testing requires a specified retained-record law and information available to the forger; commitment helps only when it enforces a positive coupling gap.

---

## 75. Scenes, streams, and the filtration

> **Definition 75.1 (dynamical scene).** A **dynamical scene** of horizon $n$ consists of finite slot spaces $X_1, \dots, X_n$ and a **trajectory domain** $D \subseteq \prod_{t \le n} X_t$: candidates are trajectories $Z = (Z_1, \dots, Z_n)$, and $Z_{\le t}$ denotes the prefix. A **causal view at time $t$** is a view (exact: a function; graded: a channel) whose value depends on $Z$ only through $Z_{\le t}$; an **anchored causal view at time $t$** is an anchored view (Definition 19.6) whose emission and context components are prefix-measurable, its context written $e_t(Z)$. For graded streams require a **joint causal factorization** into kernels at time $t$ depending only on $Z_{\le t}$ and past outputs (fresh randomization is independent of future candidate coordinates). Prefix-measurability of individual marginal channels alone does not suffice: future-dependent couplings of two null marginals would otherwise leak future information. The **record stream** is the resulting view family, graded by time; per Remark 29.2, Part IV's reduced form is recovered as the single-slot marginal, and what the scene adds is exactly the joint structure across slots that (A7) deferred.

> **Definition 75.2 (online policy).** An **online policy** for an anchored stream is a family $\pi = (\pi_t)_{t \le n}$ where $\pi_t$ selects the time-$t$ verdict as a function of the **context history** $(e_1(Z), \dots, e_t(Z))$, subject to per-time compatibility as in Definition 19.5. The policy is **memoryless** if each $\pi_t$ depends on $e_t$ alone. The verdict views $\tau^\pi_t$ are causal views at time $t$; the **verdict process** is their family. Per-round cost: $E_t(\pi) = \mu\{Z : \pi_t \text{ errs at } Z\}$; value as in §63 with the verdict process adjoined.

> **Definition 75.3 (causal pattern).** A **causal targeted pattern** on the record stream corrupts the time-$t$ record at rate $\varepsilon_t$ with clutter $Q_{Z_{\le t},\, t}$ — measurable in the prefix (and, harmlessly, in past corruption randomness). A **clairvoyant** pattern is Part VIII's: unrestricted $Z$-dependence. Blind patterns are prefix-measurable trivially, so the causal/clairvoyant distinction is a targeted-regime distinction.

> **Proposition 75.4 (transport; the filtration).** A dynamical scene's trajectory domain with its causal views is a contrast domain with views in the sense of Part I, so the finite constructions of Parts I–IX apply to the trajectory-domain views whenever their individual hypotheses hold. Causal restrictions constrain which channels or policies are allowed and do not disappear under this change of domain. The new object is the **filtration of registered content**: for a view set $S$,
> $$
> \sigma_t(S) \;=\; \sigma\big(S \cap V_{\le t}\big), \qquad \sigma_1(S) \le \sigma_2(S) \le \cdots \le \sigma_n(S) = \sigma(S),
> $$
> an increasing sequence in $\mathrm{Part}(D)$ (monotonicity of $\sigma$), with the graded and admissible analogues defined the same way. A question is **answerable at time $t$** iff $\ker(q) \le \sigma_t(S)$ (respectively the stratum-wise and ceiling-wise forms); **prediction** is answerability at $t$ of a question measurable only in coordinates beyond $t$ — a special case, not a new notion. Each increment $[\sigma_t, \sigma_{t+1}]$ is an interval of the exact calculus, so the evaluations of Parts VII and IX apply to the *time* axis as they did to the cover axis: $\nu_{\mu,q}$ decomposes the stream's information additively over rounds (chain additivity), while $\nu_\delta$ is subadditive over rounds with the defect calculus of §69 — the quasi-cocycle theorem acquires a temporal reading for free. $\square$

> **Remark 75.5 (two Part VIII phenomena were dynamics in disguise).** Accumulation (§23.1) is native here: each time step is a fresh look, so (K3̂)'s trade-off is not an exotic corner but the stream's default condition, and Theorem 61.1(1)'s scheduling attack is literally temporal — anti-correlated duty cycles across slots — as Worked example J's instruments anticipated. Part X adds no new theorem to either; it observes that their natural habitat has now been built, and that both were provable in reduced form precisely because (A7)'s marginal already carried them (Remark 29.2's point, vindicated).

---

## 76. Online control

The exact anchored regime, tracked-target, determination-monotone $K$, baseline $B$ (record-free evidence of the stream), question $q$, full-support $\mu$. For an online policy $\pi$ write $\vec\tau = (\tau^\pi_1, \dots, \tau^\pi_n)$ and
$$
V(\pi) = \nu_{\mu,q}\big(\big[\gamma_K(B),\ \gamma_K(B \cup \{\vec\tau\})\big]\big), \qquad E_t(\pi) = \mu\{Z : \pi_t \text{ errs at } Z\}.
$$

> **Theorem 76.1 (horizon-robust Fano).** For every online policy — adaptivity and memory included — with $m\ge2$ bounding the number of possible verdicts including $t^*$ in every round (the constantly loyal one-symbol case is trivial):
> $$
> V(\pi) \;\le\; S_0 \;+\; \sum_{t=1}^{n} \Big[ h\big(E_t(\pi)\big) + E_t(\pi)\log_2(m-1) \Big]
> \;\le\; S_0 + n\Big[h(\bar E) + \bar E \log_2(m-1)\Big],
> $$
> with $S_0$ the scene constant of Theorem 63.2 and $\bar E$ the average per-round error. The exchange rate of Theorem 63.2 is horizon- and adaptivity-invariant: history changes what a policy can do, not the price of doing it.
>
> *Proof.* By (K1), $\gamma_K(B \cup \{\vec\tau\}) \le \sigma(B) \vee \bigvee_t \ker(\tau^\pi_t)$, so the ceiling block is a function of $([Z]_{\sigma(B)}, \vec\tau(Z))$ and
> $$
> V(\pi) \le S_0 + H\big(\vec\tau(Z) \mid [Z]_{\sigma(B)}\big) \le S_0 + \sum_t H(\tau^\pi_t) ,
> $$
> by the chain rule. In a tracked-target scenario the time-$t$ error event is exactly $\{\tau^\pi_t \ne t^*\}$, so the grouping bound gives $H(\tau^\pi_t) \le h(E_t) + E_t \log_2(m-1)$; concavity of $h$ gives the per-symbol form. $\square$

> **Theorem 76.2 (the adaptivity premium).** There is a two-round scene on which adaptive policies strictly Pareto-dominate all memoryless ones. Let $D = \{1,2\} \times \{0,1\}^2$ (candidates $(k, b_1, b_2)$, uniform), $G$ the global flip of $(b_1, b_2)$, $q = b_1 \oplus b_2$, ceiling $K_G$. Round 1: feature $f_1 = k$ and an anchored view with context $e_1 = k$ (verdict held loyal throughout). Round 2: feature $v_2 = b_1$, and an anchored view whose presentation is **branch-ambiguous**: its context is
> $$
> e_2(Z) = \begin{cases} A & \text{if } k = 1,\, b_2 = 1 \ \text{ or } \ k = 2,\, b_1 = 0,\\ B & \text{otherwise,}\end{cases}
> $$
> with $o \equiv t^*$. Then, with $B = \{f_1, v_2\}$:
>
> 1. **(Memoryless frontier.)** The four memoryless policies $\tau(e_2)$ realize exactly $(E, V) \in \{(0,0),\, (\tfrac12, \tfrac12),\, (\tfrac12, \tfrac12),\, (1, 0)\}$: the loyal policy buys nothing, either single-cell erring policy buys $\tfrac12$ bit at cost $\tfrac12$, and the always-err policy has kernel $\bot$ again — the $\bar d$ pathology of Proposition 63.3, in a stream.
> 2. **(Adaptive point.)** The policy "err on $A$ iff $k = 1$" — a function of $(e_1, e_2)$ — achieves $(E, V) = (\tfrac14, \tfrac12)$: **the same class at half the cost**, strictly dominating the memoryless frontier.
> 3. Both frontiers respect Theorem 76.1 ($\tfrac12 \le h(\tfrac14)$); the premium is an efficiency gain, not a rate violation.
>
> *Proof.* Baseline: $\sigma(B) = \ker f_1 \vee \ker v_2$ is the $(k, b_1)$-partition; within each branch its blocks and the $G$-orbits chain every candidate together, so $\gamma_{K_G}(B) = P_G \wedge \sigma(B) = \ker(k)$ and $I(q; [Z]_{\gamma(B)}) = 0$ (parity is branch-independent). Adaptive policy: its verdict kernel is the indicator partition of $\{k=1, b_2 = 1\}$; adjoining it makes $\sigma$ full on branch $1$ and leaves branch $2$'s $b_1$-pairs, so the meet with $P_G$ yields the two branch-$1$ orbits and one branch-$2$ block: $I = \tfrac12$ bit (branch-$1$ orbits are pure parity classes, mass $\tfrac12$ total), $E = \mu\{k=1, b_2=1\} = \tfrac14$. Memoryless err-on-$A$: the kernel separates $\{k=1, b_2=1\} \cup \{k=2, b_1=0\}$; on branch $1$ this is the $b_2$-partition (full $\sigma$, orbit blocks after the meet, contribution $\tfrac12$); on branch $2$ the $A$-cell is the $b_1 = 0$ pair, already inside $\ker v_2$ — the verdict adds *no distinction there*, the branch stays one block, contribution $0$; but the cost counts every erring candidate: $E = \tfrac14 + \tfrac14 = \tfrac12$. Err-on-$B$ is the $b_2$/$b_1$-complement, symmetric: $(\tfrac12, \tfrac12)$. Loyal and always-err have kernel $\bot$. All eight values confirmed by exhaustive computation. $\square$

> **Corollary 76.3 (what adaptivity buys; the anomaly's price minimized).** The premium's mechanism is stated by the exhibit: round-1 information ($k$) tells the policy *which distinctions round 2 can purchase*, and the round-2 context, being branch-ambiguous, cannot. A memoryless policy must spend error mass on presentations whose verdicts buy nothing; the adaptive policy spends only where the kernel gains. Hence: **adaptivity buys frontier, never rate** (Theorem 76.1) — its value is exactly the error mass that foresight avoids wasting, here a factor of two. The reading against Proposition 30.2 completes the control picture: the loyalty anomaly persists in streams (positive value still requires positive error — Theorem 63.2(1) transports verbatim), but the adaptive erring policy is *globally more loyal* than its memoryless rival at equal value. History is the interpreter's second lever, and unlike the first, it costs nothing. $\square$

---

## 77. Causal corruption

> **Theorem 77.1 (the causal gap).** Fix a finite stream and two nested closed feasible classes of attacks, causal and clairvoyant, with a compact rate parameter and an attainable annihilation constraint. In item 3 the model is whole-law contamination of one record at common rate $\varepsilon$.
>
> 1. **(Order.)** The causal annihilation threshold is $\ge$ the corresponding clairvoyant optimum: causal patterns are a subset of clairvoyant ones.
> 2. **(Equality criterion.)** They coincide iff some optimal clairvoyant attack admits the required joint causal factorization (for one record, its clutter depends only on the available prefix).
> 3. **(Strict gap, exhibited.)** Horizon $2$; the only record is $R_1 = b_1$ at time $1$; the environment coordinate $b_2$ realizes at time $2$ and is never recorded; prior $b_1 \sim \mathrm{unif} \otimes b_2 \sim \mathrm{Bern}(\beta)$, $0<\beta<1$, $\beta\ne\tfrac12$; $q=b_1\oplus b_2$. The honest $q$-conditional laws of $R_1$ are $(1-\beta, \beta)$ and $(\beta, 1-\beta)$, so $d = 2|1-2\beta|$ and the **clairvoyant** threshold is
> $$
> \varepsilon^*_{\mathrm{clair}} = \frac{|1-2\beta|}{1+|1-2\beta|} \qquad (= \tfrac13 \text{ at } \beta = \tfrac34),
> $$
> while the **causal** threshold is $\tfrac12$ exactly, for every $\beta \ne \tfrac12$. Ignorance of the future forces the adversary from mixture-merging to pointwise merging.
>
> *Proof.* 1 is set inclusion. 2: if such a clutter exists it is causal and attains the clairvoyant value; conversely attainment exhibits it. 3: clairvoyant is Lemma 62.1 with the stated $d$. Causal: the time-$1$ clutter is a function $Q_{b_1}$; the perceived $q$-conditional difference is
> $$
> (1-\varepsilon)\big[P(\cdot \mid q{=}0) - P(\cdot \mid q{=}1)\big] + \varepsilon \sum_{b_1}\big[P(b_1 \mid q{=}0) - P(b_1 \mid q{=}1)\big] Q_{b_1}
> \;=\; (1-2\beta)\Big[(1-\varepsilon)(\delta_0 - \delta_1) + \varepsilon (Q_0 - Q_1)\Big],
> $$
> and for $\beta \ne \tfrac12$ the tilt factors out entirely: annihilation requires $(1-\varepsilon)(\delta_0 - \delta_1) = \varepsilon(Q_1 - Q_0)$, whose $L_1$ norms force $\varepsilon \ge \tfrac12$, attained by the cross-clutter $Q_0 = \delta_1$, $Q_1 = \delta_0$. The clairvoyant attack that achieves $\tfrac13$ at $\beta = \tfrac34$ uses class-average clutter, which depends on $b_2$ — not prefix-measurable, as item 2 requires. Both thresholds verified by LP feasibility bisection. $\square$

> **Corollary 77.2 (front-loading in the exhibit).** In Theorem 77.1(3), the causal premium is $1/2-d/(2+d)>0$ for $0<\beta<1$, $\beta\ne1/2$. It is a demonstrated benefit of the stated information constraint, not a universal formula for every early record. General causal thresholds require the prefix-constrained feasibility program in Appendix B. $\square$

---

## 78. Provenance: commitment and shared noise

> **Theorem 78.1 (causal conditional simulation).** Let $H_t$ be the information available to the forger before writing the time-$t$ verdict. Suppose the honest policy's conditional verdict law is a known kernel $A_t(\cdot\mid H_t)$, simulable using permitted private randomness, and the retained time-$t$ observation is conditionally independent of that verdict given $H_t$. Suppose also that both constructions have the same conditional transition law to the next available history. If replacement of each verdict is allowed, a causal forger on the loyal substrate reproduces the honest policy's complete retained-record law.
>
> *Proof.* Given $H_t$, draw a verdict from $A_t$ independently of the retained observation. Conditional independence makes the joint round law identical. The equal transition kernel gives the same next-history law; induction proves equality of the full record law. A missing input, retained shared randomness, or a replacement-rate restriction can invalidate these hypotheses. Time alone is therefore insufficient to prevent counterfeit, but the claim is confined to this simulation model. $\square$

The next theorem studies a different model in which a retained feature shares fresh randomness with the honest verdict and the forger must commit before observing it.

> **Definition 78.2 (co-registration; commitment).** At time $t$ let the interpreter's perception be one draw $y_t \sim u_t(\cdot \mid Z_{\le t})$, and let the round-record contain a **co-registered pair**: a retained feature $g(y_t)$ and the verdict $a(y_t)$, both functions of the *same* draw. The stream is **committed** (write-ahead) if any forgery's verdict-replacement at time $t$ may depend on $(Z_{\le t}, \text{record}_{<t}, \text{own randomness})$ but not on $y_t$ or its functions — the verdict is written before the co-registered feature is revealed to anything that could rewrite it.

> **Theorem 78.3 (provenance from commitment $+$ shared noise).**
>
> 1. **(Commitment is necessary.)** Without it — the forger sees $g(y_t)$ before writing — conditional resampling, $\hat a \sim \Pr(a(y_t)\in\cdot\mid g(y_t),Z_{\le t},\mathrm{past})$, reproduces the round-record's joint law exactly: forgery is perfect again.
> 2. **(Positive-gap commitment separates.)** Assume the fresh draw is independent of the forger’s precommitment information conditional on the candidate history and past. With commitment, any forged verdict is conditionally independent of $y_t$ given $(Z_{\le t}, \text{past})$, so the forged round-law is a *product-form* coupling of the feature and verdict margins, and the honest and forged round-laws differ by at least $g_t=\inf_\nu\mathrm{TV}(P_t,P_t^{\mathrm{feature}}\otimes\nu)$. Separation requires $g_t>0$; shared-origin notation alone does not imply this. On the canonical exhibit — $y_t$ a uniform bit, $g = a = y_t$ — the honest pair is the diagonal law and every committed forgery yields $\mathrm{TV} = \tfrac12$, *regardless of the forged verdict's marginal*: for any $\nu$, $\mathrm{TV}(\mathrm{diag}, \mathrm{unif} \otimes \nu) = \tfrac12$.
> 3. **(Sequential detection, exponential.)** In the forensic setting — provenance tested for a known candidate history, rounds conditionally independent given it — for two fixed hypotheses with iid round laws $P\ne Q$, the $n$-round Bayes error of the optimal audit is at most $\tfrac12 \mathrm{BC}^n$, where $\mathrm{BC} = \sum_y \sqrt{P(y)Q(y)} < 1$ is the round Bhattacharyya coefficient: since $\min(a,b) \le \sqrt{ab}$ pointwise and $\mathrm{BC}$ is multiplicative over products, $1 - \mathrm{TV}(P^{\otimes n}, Q^{\otimes n}) \le \mathrm{BC}^n$. On the bit exhibit with forged marginal $\nu$, $\mathrm{BC}=(\sqrt{\nu(0)}+\sqrt{\nu(1)})/2\le2^{-1/2}$, with equality only at uniform $\nu$: one round is inconclusive (error $\le 0.354$), twenty rounds pin provenance to error $\le 2^{-11}$.
>
> *Proof.* 1: the resampled pair $(g(y_t), \hat a)$ has, by construction, the joint law of $(g(y_t), a(y_t))$ given $(Z_{\le t}, \text{past})$; induct over rounds. 2: conditional independence forces the product form; on the exhibit, the honest law puts mass $\tfrac12$ on each diagonal cell while any product $\mathrm{unif} \otimes \nu$ splits $\tfrac{\nu_y}{2}$ across the column of each $y$, and the four-cell $L_1$ sum telescopes to $1$ for every $\nu$. 3: the optimal test errs with probability $\tfrac12(1 - \mathrm{TV})$ at equal priors; apply the two displayed elementary facts. All values verified numerically. $\square$

> **Remark 78.4 (the role of a coupling gap).** The committed audit compares its honest joint law with the forger's allowed laws. On the fair-bit example commitment forces a product law and leaves a uniform positive gap; Appendix D.7 gives the exact minimax test even for adaptive precommitted forgers. A different co-registered pair may have zero gap, and restrictions on a forger's knowledge can matter independently of commitment. The verdict concerns these declared hypotheses, not provenance in every possible attack model.

---

## 79. Worked example L: the write-ahead audit log

The laboratory examples can be read as three separate model-based design calculations. The branch policy of Theorem 76.2 obtains half a bit at half the deterministic memoryless error cost. The single-record model of Theorem 77.1 at $\beta=3/4$ has causal threshold $1/2$ versus clairvoyant threshold $1/3$. For a fresh independent fair checksum bit, an honest matching verdict, and an all-round precommitted forger, Appendix D.7 gives equal-prior minimax audit error $2^{-21}$ after twenty rounds. A real archive would need to establish those fresh-noise and attack assumptions before using that number; the bound is not a posterior probability of forgery for an arbitrary log.

---

## 80. Recovery: the static fiber

> **Theorem 80.1 (horizon-one recovery).** At horizon one, with the complete candidate state available at that time, there is no earlier record history and no unrevealed future state. The adaptive and causal-prefix distinctions of §§76–77 disappear. A committed co-registered pair can nevertheless retain a one-round honest/forged gap: on the fair-bit example its equal-prior minimax error is $1/4$ (Appendix D.7). Recovering the perfect-counterfeit model of Theorem 62.3 additionally removes the fresh shared-noise/commitment resource or makes its conditional law simulable by the forger.
>
> *Proof.* The first claims follow from the available histories. Substitute $n=1$ in D.7 for the positive gap. The last condition restores the simulation hypotheses of Theorem 78.1. A constant trajectory over several rounds need not be equivalent to a one-round experiment: independent repeated observations may accumulate information. $\square$

---

## 81. Established results and scope

The finite results include the adaptive-policy exhibit, the single-record causal threshold gap, conditional counterfeit simulation, and committed-bit testing. Appendix D.7 sharpens the latter to an exact minimax risk against adaptive precommitted forgers. Horizon one removes history and future-state restrictions but need not remove a co-registration gap. Infinite horizons, partial-round attacks, and general measurable causal optimization require additional hypotheses.

**References added in Part X:** none. The Bhattacharyya bound is derived elementarily in-proof; everything else is Cover & Thomas, Le Cam, and the manuscript's own results — the sixth part of the last seven to add nothing.
