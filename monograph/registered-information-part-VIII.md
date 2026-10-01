# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part VIII: Corruption, Closure, and Control

---

## 60. Corruption and policy design

This part studies explicit failures of budget transfer, finite annihilation thresholds, and the cost of verdict policies. Independent coordinate replacement and whole-record contamination are distinct models. A least adequate transfer is an order-theoretic supremum question; an incomparable pair does not refute its existence. Appendix D.5 resolves the full unconstrained coupling-fiber case, while D.11 certifies specified budgets for polyhedral attack classes.

---

## 61. Failure examples and transfer certificates

### 61.1 Two ways to defeat accumulation closure

> **Theorem 61.1 ((K3̂) need not transfer under joint blindness).** There exist coherent families with admissibility structures satisfying (K0̂)–(K3̂), and family patterns, such that a separable admissible reading of the perceived family strictly Blackwell-dominates the joint ceiling. This occurs already for:
>
> 1. **(Scheduling: jointly blind, nothing injected.)** A jointly candidate-blind pattern — hence within the descent-neutral class of Theorem 41.2, with the perceived family a garbling of the honest one (Proposition 29.8(1)) — consisting of anti-correlated *erasures*: no false content enters, every marginal footprint is as budgeted, and the violation is pure accounting.
> 2. **(Creation: marginally blind, ceilings null.)** A marginally candidate-blind pattern of coupled intrusions against the *maximally restrictive* structure (all ceilings null): each perceived view is Blackwell-null and every per-view reading admissible, yet the perceived joint carries a coupling-address class. At rate $\varepsilon = \tfrac12$ the injected class is exactly the pure coupling generator of Proposition 55.3, of quantum $\tfrac32 - \tfrac34 \log_2 3$ bits.
>
> Consequently the hypothesis doing the work in Proposition 48.1 is the **independence** of the per-view corruptions, not their blindness; joint blindness — sufficient for descent-neutrality of content (Theorem 41.2) — is insufficient for transfer of ceiling brackets.
>
> *Proof.* 1: Let $D = \{Z, Z'\}$ with uniform prior, let $Y = D \cup \{\star\}$, and let $v = w$ be the identity view (deterministic, never emitting $\star$); the honest family is deterministic, hence coherent with the diagonal coupling. Fix $\delta \in (0, \tfrac12)$ and let $E_\delta$ denote the erasure experiment $E_\delta(\cdot \mid Z) = (1-\delta)\delta_Z + \delta\,\delta_\star$. Set $\Gamma(\{v\}) = \Gamma(\{w\}) = E_\delta$ and $\Gamma(\{v,w\}) = E_\delta^{(2)}$, the *independent double look* $Z \mapsto E_\delta(\cdot \mid Z) \otimes E_\delta(\cdot \mid Z)$; (K0̂)–(K1̂) hold and the structure is monotone. (K3̂) holds on the honest family: a per-view admissible processing has $G_x \circ v \preceq_B E_\delta$, i.e. $G_x(\cdot \mid Z) = (H_x \circ E_\delta)(\cdot \mid Z)$ for a single channel $H_x$ and all $Z$; a separable reading applies the two processings independently to the diagonal joint, giving $G_v(\cdot \mid Z) \otimes G_w(\cdot \mid Z) = (H_v \otimes H_w)\big(E_\delta(\cdot|Z) \otimes E_\delta(\cdot|Z)\big) \preceq_B E_\delta^{(2)}$. Now corrupt with the jointly blind family pattern $\lambda(\varnothing) = 1 - 2\delta$, $\lambda(\{v\}) = \lambda(\{w\}) = \delta$, $\lambda(\{v,w\}) = 0$, all replacements $\delta_\star$: **anti-correlated erasures** with the same marginal footprint, $\tilde v = \tilde w = E_\delta$. The identity processing is perceived-admissible ($\mathrm{id} \circ \tilde v = E_\delta \preceq \Gamma(\{v\})$), and the resulting separable perceived reading is $\widetilde{P}_S$ itself: $(Z, Z)$ with probability $1 - 2\delta$, $(\star, Z)$ or $(Z, \star)$ with probability $\delta$ each — **the candidate is recovered with certainty**, since both coordinates are never erased. If $\widetilde{P}_S \preceq_B \Gamma(\{v,w\}) = E_\delta^{(2)}$, then by Blackwell–Sherman–Stein its Bayes error at the uniform prior would be at least that of $E_\delta^{(2)}$, which is $\delta^2/2 > 0$; but its Bayes error is $0$. Contradiction.
> 2: Let $D = \{Z, Z'\}$, uniform prior, and let $v, w$ be the constant views $\equiv 0$ with $Y = \{0,1\}$ (Blackwell-null, jointly and severally). Set every ceiling to the null experiment: (K0̂)–(K2̂) hold, monotonicity is trivial, and (K3̂) holds because every honest reading of constant data is null. Corrupt with Proposition 29.8(2)'s pattern at rate $\varepsilon$: under $Z$, both views are intruded together with probability $\varepsilon$ (replacement $\delta_{(1,1)}$), neither otherwise; under $Z'$, each independently at rate $\varepsilon$ (replacement $\delta_1$). The pattern is marginally blind — each perceived marginal is $(1-\varepsilon)\delta_0 + \varepsilon\delta_1$ under both candidates — so every perceived view is null and every per-view processing is perceived-admissible. The separable reading with identity processings is the perceived joint: $(1-\varepsilon)\delta_{00} + \varepsilon\delta_{11}$ under $Z$, the product under $Z'$; these differ (mass $\varepsilon(1-\varepsilon) > 0$ at $01$ under $Z'$ only), so the reading is non-null and strictly exceeds the null joint ceiling. At $\varepsilon = \tfrac12$ the perceived family is precisely the family of Propositions 22.4(2) and 55.3, and the injected class is the pure coupling generator, quantum $\tfrac32 - \tfrac34\log_2 3$ bits, with fiber width one bit. $\square$

Three comments fix the theorem's place. First, item 1 is a *scheduling* phenomenon with a plain operational reading: a per-view accounting that budgets "each channel delivers an independent $(1-\delta)$-reliable look" is beaten by an adversary — or an environment — that anti-correlates the failures, because "at least one honest look, always" strictly dominates "two independent looks"; the data-processing inequality is untouched ($\widetilde{P}_S \preceq_B P_S$ throughout), and what fails is the ceiling's implicit independence assumption, exposed by the transfer. Second, item 2 upgrades Proposition 29.8(2) from a content statement to an *admissibility* statement: intrusion coupling is not merely a source of superadditivity but a device for smuggling a class past any per-view gate — and Part VII prices the payload, closing a loop the manuscript could not have closed before §55: **the attack injects the pure coupling generator**. Third, the alignment of boundaries is now exact and threefold: marginal-only blindness is where descent classes are created (Proposition 41.3), where superadditivity is injected (Proposition 29.8(2)), and where null ceilings are defeated (item 2); joint blindness rescues content comparison (Theorem 41.2) but not ceiling accounting (item 1); product preprocessing is one sufficient way to preserve the budget bracket (Proposition 48.1), with a broader branchwise criterion in Appendix D.6.

### 61.2 Adequate transfers and least-element questions

> **Proposition 61.2 (adequate transfers and the actual order obstruction).** An adequate transfer is an upper bound of the class of perceived readings. A least transfer exists exactly when that class has a supremum in the Blackwell order. Incomparability alone does not rule it out. In particular the two mirrored binary-state experiments discussed in the original proof have a join: binary-state finite experiments form a lattice [Bertschinger–Rauh 2014, Proposition 16]. That example therefore does **not** prove nonexistence.
>
> The general order is not a lattice, so no unrestricted existence theorem follows without additional hypotheses; a particular nonexistence claim must exhibit a class without a supremum and show it is realized by the allowed corruption model. That realization remains open here. The lower-set completion always contains the union of the readings' principal lower sets. This is a least lower set containing the class, not automatically an achievable experiment or an accumulation-closed class. See Appendix D.5–Appendix D.6. $\square$

---

## 62. The lever under fire: annihilation, decay, counterfeit

The policy-created class of Theorem 46.3(1) — carrier $\{v, \tau_a\}$ on the parity domain, quantum one bit (Theorem 54.1(4)) — is now subjected to corruption. The general instrument comes first.

> **Lemma 62.1 (whole-record annihilation threshold).** Let a coherent family over finite $T$ have honest joint $P_T$, let $q$ be binary with both classes of positive prior mass, and let $\bar p_1, \bar p_2$ be the $q$-conditional average honest joint laws, $d = \lVert \bar p_1 - \bar p_2 \rVert_1 > 0$. Consider record-level patterns of common rate $\varepsilon$: perceived law $(1-\varepsilon) P_T(\cdot \mid Z) + \varepsilon\, Q_Z$.
>
> 1. **(Blind: never.)** If $Q_Z \equiv Q$, then for every $\varepsilon < 1$ the perceived $q$-conditional averages differ by $(1-\varepsilon)(\bar p_1 - \bar p_2) \ne 0$, so $I_\mu(q; \widetilde{Y}_T) > 0$: no blind pattern annihilates the class.
> 2. **(Targeted: exactly at $d/(2+d)$.)** A targeted pattern with $I_\mu(q; \widetilde{Y}_T) = 0$ exists iff
> $$
> \varepsilon \;\ge\; \varepsilon^* \;=\; \frac{d}{2 + d}.
> $$
>
> *Proof.* Annihilation for binary $q$ means equality of the perceived $q$-conditional averages, $(1-\varepsilon)\bar p_i + \varepsilon \bar Q_i$ with $\bar Q_i$ the class-average clutter; equivalently $(1-\varepsilon)(\bar p_1 - \bar p_2) = \varepsilon(\bar Q_2 - \bar Q_1)$. A difference of two probability measures is exactly a signed measure of total mass zero and $L_1$ norm at most $2$; the left side has total mass zero and norm $(1-\varepsilon)d$, so solvability requires $(1-\varepsilon)d \le 2\varepsilon$, i.e. $\varepsilon \ge d/(2+d)$. Conversely, for such $\varepsilon$ write $s = \tfrac{1-\varepsilon}{\varepsilon}(\bar p_1 - \bar p_2) = s^+ - s^-$ (equal masses $\le 1$) and set $\bar Q_2 = s^+ + (1 - \lVert s\rVert_1/2)\rho$, $\bar Q_1 = s^- + (1 - \lVert s\rVert_1/2)\rho$ for any probability $\rho$; realize candidatewise by $Q_Z := \bar Q_i$ on class $i$. 1 is the displayed identity with $\bar Q_1 = \bar Q_2$. $\square$
>
> When the honest class-conditional averages have disjoint supports, $d = 2$ and $\varepsilon^* = \tfrac12$: annihilating a cleanly separated class requires counterfeiting half the record. Post-processing cannot resurrect annihilated information. Under blind whole-record contamination, a fixed decoder retains positive question information if its clean output was informative, by the affine row identity of Proposition 47.1; an already uninformative decoder does not acquire it.

> **Theorem 62.2 (fate of the policy bit: a trichotomy with constants).** On Theorem 46.3's configuration under the erring policy (honest record pair $(Y_v, Y_{\tau_a})$; $q = q_G$; uniform prior):
>
> 1. **(Zero-error stratum: dies at any rate.)** For every pattern with $\varepsilon > 0$ and positive joint full-support clutter (or independent full-support replacement of every coordinate) of the joint record, the perceived supports of all candidates coincide, so $q_G$ is not zero-error answerable from any reading: at the $\sigma^0$ stratum (Definition 21.6, Theorem 22.1) the class exists only at $\varepsilon = 0$.
> 2. **(Statistical stratum, blind: survives every rate, with closed-form decay.)** Under independent candidate-blind uniform clutter at rate $\varepsilon$ on each channel, each behaves as a binary symmetric channel of crossover $\varepsilon/2$; the parity statistic $\widetilde{Y}_v \oplus \widetilde{Y}_\tau$ (identifying $t^* \equiv 0$, $d \equiv 1$) is sufficient for $q_G$, is orbit-equalizing (its law is constant on $G$-orbits), and carries
> $$
> I\big(q_G;\, \widetilde{Y}_v, \widetilde{Y}_\tau\big) \;=\; 1 - h\big(\varepsilon(1 - \varepsilon/2)\big) \;>\; 0
> \qquad (\varepsilon < 1),
> $$
> vanishing only at $\varepsilon = 1$ — the injectivity of blind contamination (Theorem 29.4(2)), with its decay curve.
>
> 3. **(Statistical stratum, targeted: annihilated exactly at $\tfrac12$.)** The honest $q_G$-conditional average laws of the pair are supported on $\{(0,t^*),(1,d)\}$ and $\{(0,d),(1,t^*)\}$ respectively — disjoint, $d = 2$ — so by Lemma 62.1 the class is annihilable by common-rate whole-record targeted contamination iff $\varepsilon \ge \tfrac12$; the cross-clutter $Q_Z := \bar p_{\text{other orbit}}$ realizes annihilation at exactly $\tfrac12$.
>
> *Proof.* 1: positive joint full-support clutter (or independent full-support replacement of every coordinate) puts every output profile in every candidate's perceived support; zero-error content is then trivial and Theorem 22.1 applies. 2: uniform clutter at rate $\varepsilon$ replaces a bit by a fair coin, i.e. flips it with probability $\varepsilon/2$; the two perceived channels are independent BSC$(\varepsilon/2)$ readings of $b_1$ and $b_2$; conditional on the parity, the pair's law depends only on the XOR by symmetry, so the XOR is sufficient, and it mis-reports the parity iff exactly one channel flipped: crossover $2\cdot\tfrac{\varepsilon}{2}(1 - \tfrac{\varepsilon}{2}) = \varepsilon(1-\varepsilon/2)$. Orbit-equalization: the global flip inverts both bits, and the XOR's law is invariant under simultaneous inversion. 3: read the four honest outputs off Theorem 46.3's proof and apply the lemma. $\square$

> **Theorem 62.3 (counterfeit: targeted corruption forges the lever).** On the same configuration under the **loyal** policy:
>
> 1. **(Creation at every rate.)** The targeted pattern on the verdict channel with $\varepsilon(Z) = \varepsilon \cdot \mathbb{1}[b_2(Z) = 1]$ and clutter $\delta_d$ creates the class at every $\varepsilon > 0$, with exact quantum
> $$
> I\big(q_G;\, Y_v, \widetilde{Y}_{\tau_\ell}\big) \;=\; 1 - \big(1 - \tfrac{\varepsilon}{2}\big)\, h\!\left(\frac{1-\varepsilon}{2 - \varepsilon}\right),
> $$
> increasing from $0$ to $1$ bit as $\varepsilon: 0 \to 1$.
>
> 2. **(Perfect counterfeit.)** At $\varepsilon = 1$ the perceived loyal record equals, *as an experiment*, the honest erring record: $\widetilde{\tau_\ell} = \tau_a$ exactly. Hence no reading — admissible or not, at any stratum — distinguishes "erring policy, honest record" from "loyal policy, forged record": **provenance of a class is not a record-level fact.** Attribution requires fidelity metadata; the axis of §32.2 is forensically necessary.
>
> *Proof.* 1: with $b_1$ delivered exactly by $v$, the parity's residual uncertainty is $b_2$'s; the forged verdict is a one-sided channel on $b_2$ ($t^*$ certainly when $b_2 = 0$; $d$ with probability $\varepsilon$ when $b_2 = 1$), so the verdict $d$ (probability $\varepsilon/2$) resolves $b_2$ and the verdict $t^*$ (probability $1 - \varepsilon/2$) leaves posterior $\Pr(b_2 = 1 \mid t^*) = \tfrac{1-\varepsilon}{2-\varepsilon}$; take expectations of the binary entropy. 2: at $\varepsilon = 1$ the forged verdict is $d$ iff $b_2 = 1$, which is $\tau_a$'s defining table; the two records are equal as channels, hence as experiments. $\square$

> **Remark 62.4 (the limit of robustness-as-invariance; one number, three roles).** Theorem 47.3 protects admissible content when the admissible readings equalize the clutter's variation. Against Lemma 62.1's annihilating cross-clutter this protection is void by construction: the clutter's variation across candidates *is* the question's — a reading equalizing $g \circ Q_{O_1} = g \circ Q_{O_2}$ with $Q_{O_i} = \bar p_{\text{other}}$ thereby equalizes $g \circ \bar p_1 = g \circ \bar p_2$ and carries no $q_G$-information at all, the annihilation absorbed into the ceiling rather than repelled by it. Robustness-as-invariance is exactly robustness against clutter *transverse* to the question; along the question's own direction the trade-off of Proposition 47.4 is unimprovable. The section's constant $\tfrac12$ meanwhile appears in three roles worth distinguishing: the annihilation threshold (rate $\tfrac12$ on every record), the perfect counterfeit's average corrupt mass (rate $1$ on the half of the candidates with $b_2 = 1$), and Theorem 61.1(2)'s creation exhibit at its Part VII calibration point — in each case, *half the ledger* is the price of erasing, forging, or smuggling a cleanly separated one-bit class.

---

## 63. The policy calculus

The exact anchored regime of §44, with determination-monotone $K$ (Theorem 45.4), a full-support prior $\mu$, a question $q$, and a fixed **baseline** $B \subseteq \widehat{V}$ (the record-free evidence: feature views, and presentation/context views as the scenario provides). A compatible policy $a$ adjoins its verdict view; define its **value** and **cost**
$$
V(a) \;=\; \nu_{\mu,q}\big(\big[\gamma_K(B),\ \gamma_K(B \cup \{\tau_a\})\big]\big),
\qquad
E(a) \;=\; \mu\{Z : a(e(Z)) \ne o(Z)\}.
$$

> **Proposition 63.1 (separation of coordinates).** $V(a)$ depends on $a$ only through $\ker(\tau_a)$: by Theorem 45.4(3), $\gamma_K = g \circ \sigma$ for monotone $g$, and $\sigma(B \cup \{\tau_a\}) = \sigma(B) \vee \ker(\tau_a)$. The cost $E(a)$ is not a function of $\ker(\tau_a)$: on Theorem 46.3's configuration with prior mass $\tfrac13$ on $\{b_2 = 1\}$, the policies $(t^*\!,\, d)$ and $(d,\, t^*)$ have the same verdict kernel $\ker(w)$ but costs $\tfrac13$ and $\tfrac23$. A policy is thus two choices — a **partition** (which purchases classes) and a **truth-assignment within it** (which spends error) — and only the first reaches the value. $\square$

> **Theorem 63.2 (no free classes; Fano's exchange rate).** Let the scenario be tracked-target ($o \equiv t^*$), let $m=|\tau_a(D)\cup\{t^*\}|$. For $m\ge2$ use the bound below; for $m=1$ the verdict is constantly loyal and $V=E=0$. Failure symbols are counted only when emitted.
>
> 1. **(No free classes.)** $E(a) = 0$ forces $\tau_a \equiv t^*$, hence $\ker(\tau_a) = \bot$ and $V(a) = 0$: zero-error policies purchase nothing beyond the baseline.
> 2. **(The exchange rate.)** For every compatible policy,
> $$
> V(a) \;\le\; S_0 \;+\; h\big(E(a)\big) \;+\; E(a)\,\log_2(m - 1),
> $$
> where $S_0 = I\big(q; [Z]_{\sigma(B)}\big) - I\big(q; [Z]_{\gamma_K(B)}\big) \ge 0$ is a policy-independent constant of the scene (the baseline content the ceiling suppresses). Classes are bought with errors, at at most Fano's rate.
>
> 3. **(Tightness.)** On Theorem 46.3's configuration ($S_0 = 0$, $m = 2$): the erring policy has $V = 1$ bit and $E = \tfrac12$, meeting the bound $V \le h(E)$ with equality. For this $S_0=0$ scenario, one bit requires $E=1/2$. No such universal lower bound follows when $S_0>0$; the baseline can contain suppressed information unlocked by a verdict.
>
> *Proof.* 1 is Proposition 63.1 with the observation that in a tracked-target scenario the error event is exactly $\{\tau_a \ne t^*\}$. 2: by (K1), $\gamma_K(B \cup \{\tau_a\}) \le \sigma(B \cup \{\tau_a\}) = \sigma(B) \vee \ker(\tau_a)$, so $[Z]_{\gamma_K(B \cup \tau_a)}$ is a function of the pair $\big([Z]_{\sigma(B)}, \tau_a(Z)\big)$; hence
> $$
> V(a) \le I\big(q; [Z]_{\sigma(B)}, \tau_a(Z)\big) - I\big(q; [Z]_{\gamma_K(B)}\big) = S_0 + I\big(q; \tau_a(Z) \mid [Z]_{\sigma(B)}\big) \le S_0 + H\big(\tau_a(Z)\big),
> $$
> and $\tau_a$ is determined by the pair (error indicator, which wrong verdict), so $H(\tau_a) \le h(E) + E \log_2(m-1)$ — the grouping form of Fano's bound [Cover & Thomas 2006]. 3: $\sigma(B) = \ker(v)$ and $I(q_G; [Z]_{\ker v}) = 0 = I(q_G; [Z]_{\gamma_G(B)})$, so $S_0 = 0$; $V = 1$ by Theorem 54.1(4), $E = \tfrac12$, $h(\tfrac12) = 1$. $\square$

> **Proposition 63.3 (the lever's design space; the frontier).** On Theorem 46.3's configuration the compatible policies are the four maps $\{c_0, c_1\} \to \{t^*, d\}$, with (uniform prior):
>
> | policy | verdict kernel | $E$ | $V$ |
> |---|---|---|---|
> | $\ell = (t^*, t^*)$ | $\bot$ | $0$ | $0$ |
> | $a = (t^*, d)$ | $\ker(w)$ | $\tfrac12$ | $1$ bit |
> | $\bar a = (d, t^*)$ | $\ker(w)$ | $\tfrac12$ | $1$ bit |
> | $\bar d = (d, d)$ | $\bot$ | $1$ | $0$ |
>
> The Pareto frontier is $\{\ell, a\}$ (with $\bar a$ value-equivalent to $a$), and $\bar d$ is the instructive failure: maximal error, zero value. Value is not monotone in error, because value is a function of the error's **pattern** — the kernel — and $\bar d$'s kernel is $\bot$ again. The loyalty anomaly of Proposition 30.2, the compounding of Theorem 46.3, the bit of Theorem 54.1(4), and the exchange rate of Theorem 63.2 are one fact viewed at four resolutions: *patterned error is the currency of cross-layer information, and Fano sets the exchange rate.* $\square$

> **Corollary 63.4 (certified design in the stated attack model).** For the policy-bit construction with the full-support contamination and retained-record assumptions of Theorems 62.2–62.3, a designed class has the stated statistical-stratum survival behavior, annihilable at rate $d/(2+d)$ by an adversary who knows the question (Lemma 62.1), and perfectly counterfeitable on a loyal substrate (Theorem 62.3(2)). Purchasing a class by policy design is therefore only half a control system; the other half is fidelity certification (§32.2) — provenance metadata that no record-level reading can reconstruct. The policy lever and the fidelity axis are complements, not alternatives. $\square$

---

## 64. Worked example J: design, attack, forgery, audit

The calibration laboratory of §49, one quarter on. The lab has read §46: it *designs* the context-reading linkage, accepting anchoring error on half the batches to make the calibration-invariant agreement question answerable from assay A plus the linkage verdicts — one bit, bought at the Fano-tight price $E = \tfrac12$ (Theorem 63.2(3)); the swap policy $\bar a$ would buy the same bit for the same price (Proposition 63.1), and the policy that attributes every record to the distractor buys nothing at the maximal price (Proposition 63.3). Ordinary transcription noise on the record does not threaten the purchase: the bit decays as $1 - h(\varepsilon(1 - \varepsilon/2))$ and survives every blind rate below one (Theorem 62.2(2)), though single-shot certainty about agreement is gone at any positive rate (62.2(1)). A competitor who can *target* the record — substitute plausible entries that depend on the batch — erases the bit exactly when half the ledger is theirs (Theorem 62.2(3)), and a subtler adversary does the reverse: forges the erring pattern onto an honestly loyal log, producing a record byte-equivalent, as an experiment, to the designed one (Theorem 62.3(2)). The auditor of §49, who once erred by discarding verdicts, now faces the deeper problem: even reading everything, the record cannot say whether its one bit was designed or planted. What settles it is nothing in the record — it is the lab's fidelity certification: signed policy declarations, custody of the anchoring step, the metadata of §32.2. The audit trail is not bureaucracy; it is the only carrier of a class's provenance (Corollary 63.4). Meanwhile the lab's per-instrument accounting of noise budgets is itself vulnerable to Theorem 61.1(1): two instruments whose failures are anti-correlated (shared power rail, alternating duty cycle) jointly outperform the certified per-instrument ceilings without a single false symbol — the accounting, not the physics, is what breaks.

---

## 65. Recovery, and the matrix completed

> **Theorem 65.1 (recovery).** At $\varepsilon \equiv 0$, Theorem 61.1's patterns are empty, Lemma 62.1 and Theorems 62.2–62.3 are vacuous, and the transferred structure is the structure: §§61–62 collapse to Part VI's tame half stated at rate zero. Under (A4′), the correspondence is single-valued, the policy space is a singleton, the design space of §63 degenerates ($V$ and $E$ are constants), and the frontier is the single point $(0, V)$ of the forced policy — there is nothing to control because nothing was ever chosen. Under $K^{\mathrm{can}}$, $S_0 = 0$ and Theorem 63.2's bound reads $V \le h(E) + E\log_2(m-1)$ pure, while (K3̂)-transfer questions trivialize (no ceilings to defeat). Parts IV, VI, and VII are recovered as the rate-zero, forced-policy, and full-admissibility fibers respectively. $\square$

The triple cell of the interaction matrix (§50.2) is now closed in both halves, and the completed row reads: **independent blind** — transfers everything (Propositions 47.1, 48.1, 48.2; Theorem 41.2); **jointly blind, coupled** — content-neutral but accounting-defeating: descent data preserved (Theorem 41.2), ceiling brackets violated by scheduling (Theorem 61.1(1)); **marginally blind** — creates: descent classes (Proposition 41.3), superadditivity (Proposition 29.8(2)), and ceiling violations by injection of the pure coupling generator (Theorem 61.1(2)); **targeted** — annihilates at threshold $d/(2+d)$, counterfeits perfectly, severs comparison (Lemma 62.1, Theorems 62.2–62.3, 29.6). Whether a least adequate transfer exists is open in general (Proposition 61.2); the lower-set representation of the perceived readings always exists but need not be achievable by any experiment (Remark 24.6).

---

## 66. Established results and scope

The finite examples establish closure failures, blind decay, targeted cancellation, and counterfeit under the declared retained-record model. The policy entropy bound includes the baseline gap S0 and uses the realized verdict alphabet. The one-bit/half-error conclusion requires its stated zero-baseline binary case. Restricted transfer classes may need separate existence proofs; no binary antichain is used as a no-join certificate.

**References added in Part VIII:** none. The part is built from Cover & Thomas (Fano's inequality, already cited in §22.4), Bertschinger–Rauh (lattice-freeness, already cited at Definition 23.1), and the manuscript's own results — the fourth part of the last five to add nothing, which is the intended sense in which the theory is by now consuming its own capital.
