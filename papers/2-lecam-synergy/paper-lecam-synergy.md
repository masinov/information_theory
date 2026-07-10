# Le Cam Synergy: A Stable, Operational Measure of Synergistic Information, with a Diagnosis of PID Non-Uniqueness

*Derived paper #2 of the Registered Information project; cites the monograph as [RI] and the bridge paper as [ERI]. Every number below is from executed runs; there are no fill slots. Two of this paper's originally planned claims were falsified by its own experiments before writing, and both episodes are disclosed in place (§5.3, following the project's reporting discipline).*

---

## 1. Introduction

Partial information decomposition has two standing problems. The first is conceptual: its measures of synergy and redundancy disagree, the axioms proposed to adjudicate them conflict, and the field's own surveys state that no consensus exists on what an appropriate decomposition is. The second is practical: the quantities are bits, computed from plug-in estimates whose behavior is worst exactly where the scientific questions live — weak synergy, finite samples, values near zero.

This paper offers one object and one theorem. The theorem (§3) is a **diagnosis**: PID's measures are keyed to different *ledgers* — different choices of what is held fixed while alternatives range — and across the ledger crossing a fixed information quantum provably changes its address [RI, Thm 56.2], so axiom systems drawing commitments from both sides constrain a quantity that is not well defined; the classical impossibility of Rauh et al. sits at the crossing [RI, Rem 56.4]. The object (§4) is **Le Cam synergy** $S_\delta$: the statistical deficiency of the conditional-independence surrogate for the actual joint experiment about the target. It is prior-free, its value is an operational guarantee (a worst-case decision-risk advantage, §4.2), its zero is an operational statement (§4.3), its canonical baseline is *forced* by the very lattice-freeness that obstructs scalar PID uniqueness (§3.4), and it is estimable with distribution-free, finite-sample error certificates valid uniformly down to the zero boundary (§5).

One sentence of pitch discipline, kept throughout: $S_\delta$ is **not** the field's number computed better. It is a companion invariant of the same coordinate, interconvertible with bits only on binary-symmetric classes through the transfer function $S_I = \tfrac{2}{\ln 2}S_\delta^2 + O(S_\delta^4)$ [RI, Thm 70.2] — an identity this paper's experiments confirm to four digits (§4.5) — and the square law is precisely why near-null synergy is legible on the deficiency scale and quadratically compressed on the bit scale.

## 2. Setup

Sources $Y_1, \dots, Y_n$ and target $T$, finite alphabets, joint pmf $p$. The **experiment of the joint** is the channel $E_P : t \mapsto p(y_1 \ldots y_n \mid t)$; the **coarse fiber** is the set of joints preserving the $(T, Y_i)$-marginals — BROJA's optimization domain, identified in [RI, Prop 55.4] as the coupling fiber of the target-marginalized family. Deficiency: $\delta(E, F) = \min_M \max_t \mathrm{TV}\big((M \circ E)(\cdot \mid t), F(\cdot \mid t)\big)$, a finite linear program under finiteness, $1$-Lipschitz in $\sup_t$TV in each argument [ERI, Thm 3.3(2)], with the certificate discipline (explicit channel above, decision problem below) of [RI, §68]. Note the definition contains no prior on $T$: the maximum over candidates is deficiency's sup over priors and losses in disguise (Le Cam's randomization criterion), so **$S_\delta$ will require no prior choice** — bit-valued measures require the full joint including $p(T)$.

## 3. The ledger diagnosis

**Definition 3.1 (ledgers, in PID vocabulary).** The **coarse ledger** holds fixed the target-conditional channels $p(y_i \mid t)$: it is standard PID's own frame. The **fine ledger** arises whenever the sources are generated from a richer mechanism state $Z$ with $T = q(Z)$: it holds fixed the candidatewise channels $p(y_i \mid z)$. The mechanism-versus-observational distinction discussed informally in the PID literature is exactly this crossing, and prior-marginalization ($Z \to T$) is the functor between the ledgers [RI, Def 56.1].

> **Theorem 3.2 (transport; [RI, Thm 56.2] restated).** Let the sources be deterministic in $Z$ and per-source blind to $T$ ($I(T; Y_i) = 0$). Then at the fine ledger the fiber is a singleton and the synergy is entirely *witness-addressed* (a cosheaf obstruction: per-source witnesses that do not cohere); at the coarse ledger the fiber contains the product coupling, the fiber minimum is $0$, and the *same bits* are entirely *coupling-addressed*. XOR is the instance: one bit, two correct addresses, one on each side of the crossing. $\square$

**Theorem 3.3 (classification, by definitional objects only).** Sorting the major measures by what their defining optimization or formula holds fixed: BROJA's $CI$ *is* the coarse-ledger fiber excess (a definitional identification, [RI, Prop 55.4]), and its unique-information companion, the identity axiom of Harder et al., and Williams–Beer-style target-conditional constructions are coarse-native; Blackwell/degradation-monotonicity intuitions and channel-level reasoning are per-channel commitments that survive the fine reading; Kolchinsky's framework makes the *order* an explicit choice-point, to which the ledger adds the orthogonal axis of *what is held fixed*. Consequence, with Theorem 3.2: an axiom system drawing constraints from both sides of the crossing constrains a quantity the transport theorem shows is not invariantly defined — the structural reading of the formal impossibility of nonnegative multivariate extension under the identity axiom (Rauh et al. 2014), *located* rather than rederived [RI, Rem 56.4]. $\square$

> **Proposition 3.4 (the antichain forces the baseline).** The coarse fiber has, in general, no Blackwell-least element: the two-coupling exhibit of [RI, §61] gives fiber points whose "outputs-equal" statistics are certain and uniform respectively, so neither simulates the other; and the Blackwell order has no least upper or lower bounds in general (Bertschinger–Rauh 2014). Hence "synergy $=$ excess over the fiber *minimum*" is a scalar-rung privilege — bits totally order, experiments do not — and **any metric-valued synergy must choose a baseline point**. The conditional-independence coupling $E_\otimes$ is the canonical choice: it exists always, is distinguished by the frame itself (it is what "no synergy" *means* mechanically), and is the unique fiber point defined without optimization. The known obstruction to PID uniqueness thereby becomes the design principle. $\square$

## 4. Le Cam synergy

**Definition 4.1.** $E_\otimes : t \mapsto \bigotimes_i p(y_i \mid t)$, the conditional-independence point of the coarse fiber. The **Le Cam synergy** and its underdetermination companion are
$$
S_\delta(T; Y_1, \ldots, Y_n) \;=\; \delta\big(E_\otimes,\ E_P\big),
\qquad
W_\delta \;=\; \sup_{Q, Q' \in \text{fiber}} \Delta\big(E_Q, E_{Q'}\big),
$$
the latter measuring what the marginals fail to determine ([RI, Rem 55.5]; computed exactly for the canonical two-coupling fiber in [RI, Prop 71.2], $W_\delta = \tfrac12$; exact zoo values of the supremum are left with the multivariate problem, §7).

> **Theorem 4.2 (operational meaning).** By the randomization criterion,
> $$
> S_\delta \;=\; \sup_{\text{decision problems, } [0,1]\text{ loss}} \Big[ r\big(E_\otimes\big) - r\big(E_P\big) \Big],
> $$
> the maximal Bayes-risk advantage, over *all* priors and bounded losses, of the true joint over the best processing of a conditionally independent surrogate. **The number is a guarantee**: $S_\delta = s$ means some decision problem exists where using the real correlations beats any CI-simulation by exactly $s$, and none exists where it beats it by more. $\square$

> **Proposition 4.3 (basic laws).** $S_\delta \ge 0$; $S_\delta = 0$ iff $E_P \preceq_B E_\otimes$ — *no decision problem, at any prior, benefits from the correlation structure beyond conditional independence* — an operational zero. $S_\delta$ is invariant under output relabelings, monotone under garbling of the joint output, prior-free, and defined for any number of sources verbatim. It is **not** monotone under source-set inclusion or source garbling, and should not be: synergy is not a resource that processing respects (garbling one source can *create* the conditions under which the joint beats CI relative to the degraded marginals; the $\varepsilon$-family below realizes both directions). $\square$

**Proposition 4.4 (gate zoo, closed forms with certificate pairs).**
1. **XOR:** $S_\delta = \tfrac12$. ($E_\otimes$ is null, $E_P$ has disjoint $t$-supports hence is full for the dichotomy; $\delta(\text{null}, \text{full}_2) = \tfrac12$ with the constant-midpoint channel above and uniform guessing below [RI, §69].)
2. **RDN** (both sources copy $T$) and **UNQ** (one source copies, one is noise): $S_\delta = 0$, since $E_\otimes = E_P$ exactly — redundancy and uniqueness are correctly excluded, and Kolchinsky's COPY criterion is satisfied.
3. **AND:** $S_\delta = \tfrac{1}{10}$ **exactly.** *Upper certificate:* the channel that keeps the $(1,1)$-column at itself with mass $a$ and spends everything else reshaping toward the targets achieves $\max\big(1-a,\ \tfrac{a}{9}\big)$ (the $T{=}1$ leg costs $1-a$; the $T{=}0$ leg's only obstruction is the $\tfrac{a}{9}$ of product-coupling mass at $(1,1)$, which the free columns cannot cancel but can price at $\mathrm{TV} = \tfrac{a}{9}$ by shaping the remaining mass proportionally); balancing gives $a = \tfrac{9}{10}$, value $\tfrac1{10}$. *Lower certificate:* $0$–$1$ loss at prior $w = \Pr(T{=}1) = \tfrac1{10}$: $E_P$ has Bayes error $0$ (its $t$-supports are disjoint), while $E_\otimes$'s only ambiguous cell is $(1,1)$ with likelihoods $1$ vs $\tfrac19$, giving error $\min(w, \tfrac{1-w}{9}) = \tfrac1{10}$ at the balancing prior. Note the certifying prior $\tfrac1{10}$ is *not* the gate's natural $\tfrac14$: the deficiency's sup-over-priors found the adversarial one — the prior-freeness of Definition 4.1, working.
4. **The $\varepsilon$-family** ($T$ a fair bit; sources marginally uniform and $T$-blind; outputs correlated at strength $\varepsilon$ when $T = 0$, independent when $T = 1$): $S_\delta = \tfrac{\varepsilon}{4}$ **exactly** (midpoint channel above; uniform-prior guessing below, the honest joint's conditional TV being $\tfrac\varepsilon2$). $\square$

**Proposition 4.5 (the Shannon shadow and the transfer function, confirmed to four digits).** Let $S_I = I_P(T; Y_{1..n}) - I_\otimes(T; Y_{1..n})$, the bit-valued shadow at the gate's own prior (for two sources, $I_\otimes = I_1 + I_2 - I_\otimes(Y_1; Y_2)$, placing $S_I$ in the interaction-information family; it is reported as a companion, not a contribution). On the $\varepsilon$-family, $S_I = \tfrac{\varepsilon^2}{8\ln 2} + O(\varepsilon^4)$, and the measured ratio is $0.1803$ — equal to $\tfrac{2}{\ln 2}\big(\tfrac14\big)^2$, i.e. **the transfer function $S_I = \tfrac{2}{\ln 2} S_\delta^2 + O(S_\delta^4)$ of [RI, Thm 70.2] holds on this family with its exact constant.** Near-null synergy is linear on the deficiency scale and quadratically compressed on the bit scale. $\square$

## 5. Estimation

### 5.1 Stability with certificates

> **Theorem 5.1.** Let $\widehat p$ be the smoothed empirical joint and $\bar\epsilon = \max_t \mathrm{TV}(\widehat E_{P,t}, E_{P,t}) + \max_t \mathrm{TV}(\widehat E_{\otimes,t}, E_{\otimes,t})$. Then $|\widehat S_\delta - S_\delta| \le \bar\epsilon$ **deterministically**, with $\max_t \mathrm{TV}(\widehat E_\otimes, E_\otimes) \le \sum_i \max_t \mathrm{TV}(\widehat p(y_i|t), p(y_i|t))$ (the CI point is a product, and products of channels are within the sum of the factors' TV errors, by the maximal-coupling lemma of [ERI, Prop 3.5]). Consequently: rate $\sqrt{k/n_{\min}}$ with no entropy modulus; **finite-sample confidence intervals** $[\widehat S_\delta \pm \widehat{\bar\epsilon}]$ whose validity is a deterministic implication of the TV-radius event — assumption-free, and uniformly valid *including at the boundary* $S_\delta = 0$, where the estimand's positivity constraint and the plug-in MI's regime-switching limiting laws make bit-valued interval construction delicate. Coverage observed: $1.00$ at nominal $0.95$ (conservative, as a certificate must be; §6.4). Bias direction: smoothing pulls toward the uniform (null) point, so $\widehat S_\delta$ is biased *toward zero* — conservative for testing. $\square$

### 5.2 Relative accuracy

At matched $n$, the two estimators' absolute errors are incomparable because the estimands live on different scales; the scale-free comparison is relative error, where the square law tells: on the $\varepsilon$-family at $\varepsilon = 0.2$, observed relative RMSE (§6.2) is $0.56$ vs $1.53$ at $n = 250$ and $0.23$ vs $0.36$ at $n = 4000$ — a constant-factor advantage of $\approx 1.6$–$2.7\times$ for the deficiency scale, exactly what "estimating $\varepsilon/4$ versus estimating $0.18\,\varepsilon^2$" predicts. **No rate separation is claimed** — see the disclosure below.

### 5.3 Detection, and two disclosed falsifications

The plan for this paper conjectured a detection-rate separation: $n^\ast \sim \varepsilon^{-2}$ for $\widehat S_\delta$ versus $\varepsilon^{-4}$ for the bit route, from signal scales $\varepsilon$ vs $\varepsilon^2$ against generic $n^{-1/2}$ noise. **The experiment falsified the second half.** With null-calibrated critical values, both statistics detect at $n^\ast \sim \varepsilon^{-2}$ (measured slopes $-2.19$ and $-1.99$; §6.3), and the post-mortem is instructive: under the null, the plug-in mutual-information difference *is* a $G$-statistic, whose null fluctuations concentrate at scale $1/n$, not $n^{-1/2}$ — the bit route is quadratically clever exactly at the boundary, canceling the quadratic compression of its signal. The correct statement, and all this paper claims: **the operational measure incurs no detection penalty** — it matches the $G$-test's optimal $\varepsilon^{-2}$ rate while carrying its guarantees — and the enriched rung's genuine statistical advantages are the certificate quality of §5.1, the relative-accuracy constants of §5.2, prior-freeness, and the operational semantics of the reported number. (A second, earlier falsification for the record: the coverage experiment was designed expecting visible naive-bootstrap failure for $\widehat S_I$ near the boundary; at the tested $(\varepsilon, n)$ its empirical coverage was $0.93$–$0.97$ — adequate, merely *uncertified*. The claimed asymmetry is of guarantees, not of observed breakdown.)

## 6. Experiments (all executed; certificates per [ERI] Appendix-B discipline)

### 6.1 Gate zoo
| gate | $S_\delta$ | $S_I$ | BROJA-$CI$ | whole$-$sum |
|---|---|---|---|---|
| XOR | $0.5000$ | $1.0000$ | $1.0000$ | $1.0000$ |
| AND | $0.1000$ | $0.2704$ | $0.5000$ | $0.1887$ |
| RDN | $0.0000$ | $0.0000$ | $0.0000$ | $-1.0000$ |
| UNQ | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ |

Three readings: the AND row's $\tfrac1{10}$ carries Proposition 4.4(3)'s certificate pair, and the BROJA column reproduces the literature's $\tfrac12$ exactly — a solver cross-validation; the RDN row's $-1.0$ in the last column is the classical co-information sign pathology that motivated PID, displayed for contrast; and the $\varepsilon$-family rows (values $\varepsilon/4$ and $\approx 0.180\,\varepsilon^2$ at $\varepsilon \in \{0.1, 0.2\}$, matching closed forms to $10^{-4}$) are the transfer function live.

### 6.2 Estimator head-to-head (40 trials)
AND ($S_\delta = 0.100$): bias/RMSE of $\widehat S_\delta$: $-0.002/0.010$ at $n{=}250$, $+0.000/0.003$ at $n{=}4000$. $\varepsilon$-family at $\varepsilon = 0.2$ ($S_\delta = 0.050$, $S_I = 0.0073$): $\widehat S_\delta$ RMSE $0.028 \to 0.011$; $\widehat S_I$ RMSE $0.011 \to 0.003$ — smaller absolutely, but against a quadratically smaller estimand: relative RMSE $1.53 \to 0.36$ vs $0.56 \to 0.23$ (§5.2's numbers). Smoothing bias of $\widehat S_\delta$ is toward zero throughout, as Theorem 5.1 predicts.

### 6.3 Detection ($n^\ast$ to reach power $0.8$ at level $0.05$, null-calibrated)
| $\varepsilon$ | $n^\ast(\widehat S_\delta)$ | $n^\ast(\widehat S_I)$ |
|---|---|---|
| $0.400$ | $256$ | $256$ |
| $0.283$ | $512$ | $512$ |
| $0.200$ | $2048$ | $1024$ |
| $0.141$ | $2048$ | $2048$ |

Slopes of $\log n^\ast$ on $\log\varepsilon$: $-2.19$ and $-1.99$. No penalty, no separation; §5.3's disclosure.

### 6.4 Coverage near the boundary ($n = 1000$, nominal $0.95$)
$\widehat S_\delta$ with Lipschitz-certified radius: coverage $1.00$ at $\varepsilon \in \{0.1, 0.2\}$ (guaranteed-conservative). $\widehat S_I$ with naive percentile bootstrap: $0.97$ and $0.93$ (uncertified; adequate here).

### 6.5 The transport demo
The latent-$Z$ XOR run at both ledgers with the [ERI] pipeline: fine-ledger coupling component $0.0000$ (fiber a singleton; the synergy witness-addressed), coarse-ledger $S_\delta = \tfrac12$ and BROJA-$CI = 1$ bit — Theorem 3.2's crossing, on estimated channels.

## 7. Related work, limitations, and named problems

Order-based PID is the nearest program: Kolchinsky's axiomatic framework generates intersection/union measures from a chosen preorder, and Gomes–Figueiredo instantiate degradation/Blackwell-flavored measures within it, proving Williams–Beer compatibility. All of these evaluate in bits — the order selects a channel, mutual information prices it — and their authors note the orders are not lattices, working around the fact by optimizing the scalar. This paper's deltas are exactly three: the value type (deficiency — the first synergy whose number is a decision-theoretic guarantee, Theorem 4.2), the treatment of lattice-freeness (embraced as the forcing of the canonical baseline, Proposition 3.4, rather than worked around), and the estimation theory with certificates (§5), which the definitional literature does not address. BROJA is engaged as a theorem, not an analogy (its identification as coarse-fiber excess); Rauh et al.'s coarse-graining study of the Blackwell order is adjacent to the ledger functor and read as such. Limitations, honestly: the canonical baseline answers the *synergy* question and deliberately not PID's full allocation question — the lattice-refined multivariate decomposition of $S_\delta$ is a named problem (tied to [RI, Rem 57.2]); $W_\delta$'s exact computation beyond the certified examples goes with it; alphabets are finite (continuous targets via [RI, App. A]'s reduction; *Gaussian closed forms for deficiency are a named problem and are not improvised here*); and the diagnosis of §3 classifies measures by their definitional objects only — where a measure's commitments are genuinely mixed, the table says so rather than forcing a side.

## References

- [RI] *Registered Information over Contrast Domains*, Parts I–XI with Appendices A–C. — [ERI] *Empirical Registered Information* (derived paper #1).
- Williams, P. L., and Beer, R. D. (2010). "Nonnegative Decomposition of Multivariate Information." arXiv:1004.2515.
- Bertschinger, N., Rauh, J., Olbrich, E., Jost, J., and Ay, N. (2014). "Quantifying Unique Information." *Entropy* 16(4), 2161–2183.
- Bertschinger, N., and Rauh, J. (2014). "The Blackwell Relation Defines No Lattice." *Proc. IEEE ISIT 2014*.
- Rauh, J., Bertschinger, N., Olbrich, E., and Jost, J. (2014). "Reconsidering Unique Information: Towards a Multivariate Information Decomposition." *Proc. IEEE ISIT 2014*, 2232–2236.
- Rauh, J., Banerjee, P., Olbrich, E., Jost, J., Bertschinger, N., and Wolpert, D. (2017). "Coarse-Graining and the Blackwell Order." *Entropy* 19(10), 527.
- Kolchinsky, A. (2022). "A Novel Approach to the Partial Information Decomposition." *Entropy* 24(3), 403.
- Gomes, A. F. C., and Figueiredo, M. A. T. (2023). "Orders between Channels and Implications for Partial Information Decomposition." *Entropy* 25(7), 975.
- Ince, R. A. A. (2017). "Measuring Multivariate Redundant Information with Pointwise Common Change in Surprisal." *Entropy* 19(7), 318.
- Finn, C., and Lizier, J. T. (2018). "Pointwise Partial Information Decomposition Using the Specificity and Ambiguity Lattices." *Entropy* 20(4), 297.
- Barrett, A. B. (2015). "Exploration of Synergistic and Redundant Information Sharing in Static and Dynamical Gaussian Systems." *Phys. Rev. E* 91, 052802.
