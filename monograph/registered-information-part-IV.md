# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part IV: The Substantive Theory of Anchoring

---

## 26. Records, attribution, and corruption

The record includes a presentation, possibly context, and an attribution verdict. Their projections define an information hierarchy; attribution accuracy and information content are different criteria. Whole-record blind contamination gives the stated mixture laws. Partial replacement and candidate-dependent coupling require their own hypotheses. Unique correct attribution does not make context uninformative; presentation/full-evidence equivalence uses sterility.

---

## 27. Graded anchoring: attribution channels, error, and the record

### 27.1 Grading the interface

Definitions 19.4–19.5 gave the exact anchoring apparatus: a correspondence $\eta : Y \times C \to \mathcal{P}(\widehat{T}) \setminus \{\varnothing\}$ delimiting the admissible attributions of each raw presentation, and a selection policy $a(y,c) \in \eta(y,c)$ resolving each to one. Grading replaces the policy by a channel and retains the correspondence as its support constraint.

> **Definition 27.1 (graded attribution).** Fix an anchoring scenario $(\widehat{T}, o)$ for $D$ (Definition 19.3) and spaces $Y, C$. A **graded attribution** is a channel
> $$
> A : Y \times C \to \Pr(\widehat{T}).
> $$
> $A$ is **compatible** with a correspondence $\eta$ if $\mathrm{supp}\, A(\cdot \mid y, c) \subseteq \eta(y, c)$ for all $(y,c)$. Deterministic $\eta$-compatible attributions are exactly the selection policies of Definition 19.5; a general compatible $A$ is a randomized policy over the admissible attributions.

> **Definition 27.2 (anchored graded view; verdict channel).** An **anchored graded view** on $D$ relative to $(\widehat{T}, o)$ is a triple $v = (E_v, \eta_v, A_v)$ where $E_v : D \to \Pr(Y_v \times C_v)$ is a **graded emission** (the channel form of the emission component of Definition 19.6, now producing presentation and context jointly), $\eta_v$ is a correspondence on $Y_v \times C_v$, and $A_v$ is an $\eta_v$-compatible graded attribution. The **verdict channel** of $v$ is the composite
> $$
> \alpha_v \;=\; A_v \circ E_v \;:\; D \to \Pr(\widehat{T}),
> $$
> the graded form of the attribution composite of Remark 19.8.

> **Definition 27.3 (error and irreparable rates).** For an anchored graded view and $Z \in D$, with $(y,c) \sim E_v(\cdot \mid Z)$ and $t \sim A_v(\cdot \mid y, c)$:
> $$
> \varepsilon_v(Z) \;=\; \Pr\big( t \ne o(Z) \,\big|\, Z \big)
> \qquad\text{(the \textbf{mis-anchoring rate}),}
> $$
> $$
> \iota_v(Z) \;=\; \Pr\big( o(Z) \notin \eta_v(y, c) \,\big|\, Z \big)
> \qquad\text{(the \textbf{irreparable rate}).}
> $$
> These grade the erroneous/irreparable distinction of Definition 19.5: $\iota_v$ measures the events on which *every* compatible attribution errs, so the defect lies in the correspondence; $\varepsilon_v - \iota_v$ is the part attributable to selection.

### 27.2 The irreparable floor and the attainability dichotomy

> **Lemma 27.4 (irreparable floor).** For every $\eta$-compatible attribution $A$ and every $Z \in D$:
> $$
> \varepsilon(Z) \;\ge\; \iota(Z).
> $$
>
> *Proof.* On the event $\{o(Z) \notin \eta(y,c)\}$, compatibility forces $t \in \eta(y,c) \not\ni o(Z)$, so $t \ne o(Z)$ almost surely; hence $\Pr(t \ne o(Z) \mid Z) \ge \Pr(o(Z) \notin \eta(y,c) \mid Z)$. $\square$

Whether the floor is attainable is exactly where the two readings of the origin map (Definition 19.3) part ways. Call an attribution **loyal** in the tracked-target reading ($o \equiv t^*$) if $A(t^* \mid y,c) = 1$ whenever $t^* \in \eta(y,c)$.

> **Proposition 27.5 (attainability dichotomy).**
> 1. **(Tracked-target reading.)** Every loyal attribution attains the floor uniformly: $\varepsilon(Z) = \iota(Z)$ for all $Z$ and all emissions. Conversely, the loyal attributions are exactly the compatible attributions attaining the floor for every $Z$ under every emission: if $A$ is not loyal, some emission witnesses $\varepsilon(Z) > \iota(Z)$.
> 2. **(Identity reading.)** No such extremal attribution need exist. There is a scenario with injective $o$ and $\iota \equiv 0$ in which every compatible attribution has total error $\sum_{Z} \varepsilon(Z) = 1$ — so every deterministic policy has $\varepsilon(Z) = 1$ for some $Z$ — and the achievable error profiles $\big(\varepsilon(Z)\big)_{Z \in D}$ form an antichain under the pointwise order: no policy dominates another, and none attains the floor at every candidate.
>
> *Proof.* 1. Loyalty makes $\{t \ne t^*\} \subseteq \{t^* \notin \eta(y,c)\}$ up to null events, and on the latter event error is certain by Lemma 27.4's argument; so $\varepsilon(Z) = \iota(Z)$. Conversely, if $A$ is not loyal there is $(y_0, c_0)$ with $t^* \in \eta(y_0, c_0)$ and $A(t^* \mid y_0, c_0) = 1 - \delta < 1$; an emission concentrated at $(y_0, c_0)$ gives $\iota(Z) = 0$ but $\varepsilon(Z) = \delta > 0$.
> 2. Let $D = \{Z_1, Z_2\}$, $o$ injective with values $t_1, t_2$, and one raw presentation $(y_0, c_0)$ emitted with probability one under both candidates, with $\eta(y_0, c_0) = \{t_1, t_2\}$. Then $\iota \equiv 0$. Any compatible $A$ is determined by $a := A(t_1 \mid y_0, c_0)$, with error profile $(\varepsilon(Z_1), \varepsilon(Z_2)) = (1 - a,\, a)$, whose coordinates sum to $1$; the deterministic policies realize $(0,1)$ and $(1,0)$; two profiles $(1-a, a)$, $(1-a', a')$ are pointwise comparable only if equal; and no profile is $(0,0)$, the floor. $\square$

The dichotomy is the part's first structural verdict: in the tracked-target regime, anchoring error is a *fidelity* problem with a uniform optimum; in the identity regime it is an *inference* problem — selecting the origin is answering the identity question, so policy optimality is necessarily decision-theoretic and prior-indexed. Section 30 develops both halves.

### 27.3 The record hierarchy

What does the interpreter actually receive? The interface leaves this open, and the theory must, because the choice is consequential. Fix an anchored graded view and, for actual candidate $Z$, draw $(y, c) \sim E(\cdot \mid Z)$ and $t \sim A(\cdot \mid y, c)$.

> **Definition 27.6 (records).** The **full record** is $F = (y, c, t)$; the **standard record** is $S = (y, t)$; the **forgetful record** is $N = y$. Each is a channel from $D$ (into $\Pr(Y \times C \times \widehat{T})$, $\Pr(Y \times \widehat{T})$, $\Pr(Y)$ respectively), as is the verdict channel $\alpha$ (Definition 27.2).

Before ordering the records, we state once, for reuse throughout the part, the graded form of "processing cannot create distinctions." Part III established it at the level of mutual information (Theorem 22.7(4)) and Part II at the exact level (Lemma 14.2); the stratum-wise statement is what Part IV needs.

> **Lemma 27.7 (garbling is stratum-wise non-increasing).** If $P' = G \circ P$ for channels $P, P' : D \to \Pr(\cdot)$ and a channel $G$, then
> $$
> \sigma^{0}(P') \le \sigma^{0}(P), \qquad \sigma^{=}(P') \le \sigma^{=}(P), \qquad P' \preceq_B P .
> $$
>
> *Proof.* The Blackwell statement is the definition of garbling. For $\sigma^=$: if $P(\cdot \mid Z) = P(\cdot \mid Z')$ then post-composition with $G$ gives $P'(\cdot \mid Z) = P'(\cdot \mid Z')$; so every $\sigma^=(P)$-equivalence implies a $\sigma^=(P')$-equivalence, i.e. $\sigma^=(P)$ refines $\sigma^=(P')$, i.e. $\sigma^=(P') \le \sigma^=(P)$. For $\sigma^0$: if $y \in \mathrm{supp}\,P(\cdot \mid Z) \cap \mathrm{supp}\,P(\cdot \mid Z')$, pick any $y' \in \mathrm{supp}\,G(\cdot \mid y)$ (nonempty); then $P'(y' \mid Z) \ge G(y' \mid y) P(y \mid Z) > 0$ and likewise for $Z'$, so every $\approx_P$-edge is an $\approx_{P'}$-edge; a graph with more edges has coarser components, so $\sigma^0(P') \le \sigma^0(P)$. $\square$

> **Proposition 27.8 (record hierarchy; attribution processing inequality).** For every anchored graded view:
> $$
> \alpha \;\preceq_B\; S \;\preceq_B\; F \;\simeq_B\; E,
> \qquad
> N \;\preceq_B\; S,
> $$
> and correspondingly at every stratum (Lemma 27.7). In particular: **no record, at any stratum, answers a question that the emission does not.** Attribution cannot create distinctions the raw presentations do not draw; it is informationally free given the full raw presentation.
>
> *Proof.* $F$ is obtained from $E$'s output $(y,c)$ by appending $t \sim A(\cdot \mid y, c)$ — a channel on the output, since $A$ does not read $Z$ — so $F \preceq_B E$; projecting $F$ onto $(y,c)$ recovers $E$, so $E \preceq_B F$, whence $F \simeq_B E$. The remaining relations are coordinate projections, which are channels. $\square$

Proposition 27.8 is the anchoring counterpart of Lemma 14.2, and it fixes the shape of everything that follows. Since $F \simeq_B E$, anchoring is not a source of content; since $N \preceq_B S \preceq_B F$, *discarding* parts of the record is a genuine processing step and can lose content. The interesting question is therefore not whether attribution adds information — it cannot — but what it **carries**: which parts of the emission's content survive into which records. That question has a sharp and initially surprising answer, and it is the subject of the next section.

---

## 28. Anchoring as content: the identity channel and leakage

### 28.1 The identity question and the two readings as extremes

The origin map is a view: $o : D \to \widehat{T}$ is a map on the contrast domain (the identity view of Remark 19.8), and hence also a question,
$$
q_o := o, \qquad \ker(q_o) \in \mathrm{Part}(D),
$$
the **identity question**: which origin does the actual candidate realize? Its content interpolates between the two readings of Definition 19.3: in the tracked-target reading $o$ is constant and $\ker(q_o) = \bot$ — the identity question is trivial, and anchoring's entire value lies in *guarding* feature content (§§29–30); in the identity reading $o$ is injective and $\ker(q_o) = \top$ — the identity question is maximal, and anchoring *is* inference. Intermediate kernels are partial resolution: entity-resolution problems in which several candidates share an origin.

The interface's type discipline now pays the dividend it was designed for: the identity question needs no new answerability theory.

> **Corollary 28.1 (anchoring strata; the type-stability dividend).** Fix an anchored graded view and any of its records $R \in \{F, S, N, \alpha\}$. Then, verbatim by Theorems 22.1 and 22.2 applied to the channel $R$:
> - attribution is **zero-error achievable from $R$** (some rule names the origin with certainty in one look) iff $\ker(q_o) \le \sigma^{0}(R)$;
> - attribution is **asymptotically achievable from $R$** iff $\ker(q_o) \le \sigma^{=}(R)$;
>
> and by Proposition 27.8 both criteria are monotone along $\alpha \preceq_B S \preceq_B F \simeq_B E$: whatever attribution quality a record supports, the emission supports. Anchoring quality is thereby a stratified, Blackwell-comparable resource, exactly as Remark 19.8 anticipated — and the grading machinery of Part III receives it without any redesign. $\square$

### 28.2 Anchoring leakage

Proposition 27.8 says attribution creates nothing. It does not say attribution records carry nothing beyond the presentation: the verdict $t$ is computed from $(y, c)$, and if the context $c$ is subsequently discarded, the verdict may be the only surviving trace of it. The phenomenon deserves exhibition at full strength.

> **Proposition 28.2 (anchoring leakage).** There is an anchored graded view whose forgetful record is null — the presentation law is a point mass, identical for all candidates, so $\sigma^{0}(N) = \sigma^{=}(N) = \bot$ and $N$ is Blackwell-null — while its standard record is maximal: $\sigma^{0}(S) = \top$. A view can present nothing and yet, through its attribution record alone, distinguish every pair of candidates with single-look certainty.
>
> *Proof.* Let $D = \{Z_1, Z_2\}$, tracked-target scenario $o \equiv t^*$. Take $Y = \{y_0\}$ a singleton and $C = \{c_1, c_2\}$, with emission $E(\cdot \mid Z_i) = \delta_{(y_0, c_i)}$. Set $\eta(y_0, c_1) = \{t^*\}$ and $\eta(y_0, c_2) = \{\bot\}$ (anchoring **fails**, in the status taxonomy of Definition 19.4, exactly in the contexts that $Z_2$ produces). Compatibility forces the attribution: $t = t^*$ under $Z_1$, $t = \bot$ under $Z_2$. The forgetful record is $\delta_{y_0}$ under both candidates: null. The standard record is $\delta_{(y_0, t^*)}$ under $Z_1$ and $\delta_{(y_0, \bot)}$ under $Z_2$: disjoint supports, so $\sigma^0(S) = \top$. $\square$

> **Corollary 28.3 (forgetting verdicts can lose information).** The forgetful record $N=Y$ is a garbling of $S=(Y,T)$ and can be strictly less informative, as Proposition 28.2 shows. This statement concerns retaining every presentation while forgetting its verdict. An acceptance pipeline that outputs $Y$ on acceptance and a gap symbol on rejection is a different channel (Definition 30.1); one that deletes rejected records conditions on acceptance and also needs the acceptance count or sampling protocol specified. Neither is automatically the channel $N$. $\square$

The mechanism should be named precisely, because it recurs in §§29–30 in corrupted form. By Proposition 27.8 all content originates in the emission $(y, c)$; leakage is context-borne content **smuggled into the record by the verdict** after the context itself is dropped. Anchoring cannot create; it can carry. In Proposition 28.2 what it carries is legitimate (the failure pattern honestly reflects the candidate); in §30 the same carrying capacity is what defeats the naive comparison of policies.

---

## 29. Mis-anchoring as contamination: the corruption theorems

### 29.1 Patterns and perceived views

We now let anchoring fail in the direction Part I promised to make "a definite mathematical question" (§8, H1): presentations of *other* origins accepted as being of the target, and presentations of the target lost. Rather than modeling scenes microscopically (streams of target emissions interleaved with distractor emissions, an acceptance layer, association decisions), Part IV works with the reduced form that all such models induce on a single registered observation, and records the reduction as an assumption with the microscopic theory as its named relaxation.

> **(A7) Reduced-form corruption.** Mis-anchoring affects a feature view through a pattern in the sense of Definition 29.1: the intrusion randomness is independent of the honest emission given the candidate, and observations are single records. The dynamical scene model (multi-slot streams, data association across time) is deferred; see §33. (Executed in Part X, which drops this assumption: Definitions 75.1–75.3, with Parts I–IX recovered as the static fiber by Theorem 80.1.)

> **Definition 29.1 (mis-anchoring pattern; perceived view).** Let $v : D \to \Pr(Y)$ be a graded feature view (the honest, correctly anchored channel). A **mis-anchoring pattern** for $v$ is a pair $(\varepsilon, Q)$ with $\varepsilon : D \to [0,1]$ (the **foreign-acceptance rate**) and $Q = (Q_Z)_{Z \in D} \subseteq \Pr(Y)$ (the **clutter laws**). The **perceived view** is
> $$
> \tilde v(\cdot \mid Z) \;=\; \big(1 - \varepsilon(Z)\big)\, v(\cdot \mid Z) \;+\; \varepsilon(Z)\, Q_Z(\cdot):
> $$
> with probability $\varepsilon(Z)$ the presentation registered as being of the target is in fact foreign, drawn from the clutter. The pattern is **candidate-blind** if $\varepsilon$ and $Q_Z$ do not depend on $Z$: neither the rate nor the nature of the intrusions varies with which candidate is actual.

The candidate-blind case is formally the $\varepsilon$-contamination (gross-error) model of robust statistics [Huber 1964], arrived at here from the anchoring side: the "gross errors" are presentations of foreign origin, and the robustness question becomes a content question, answered stratum by stratum below.

> **Remark 29.2 (omission is contamination by a null symbol; scene reduction).** False negatives — genuine target presentations mis-attributed away and hence lost — are the case $Q_Z = \delta_{\varnothing}$ for a null symbol $\varnothing \notin Y$ adjoined to the presentation space: the interpreter registers "nothing" in place of the lost presentation. Both corruption directions are thus patterns, and the theorems below cover them uniformly. As for the reduction itself: in a scene where each observation slot carries the target's emission or a foreign one, and the anchoring layer accepts a subset of each, the law of an accepted presentation given $Z$ is precisely a mixture of the honest law and a clutter law, with the rate determined by the scene's composition and the policy's acceptance behavior — the reduced form is not an idealization of the scene but its marginal. What (A7) defers is the *joint* structure across slots, which belongs with the stream dynamics.

### 29.2 Candidate-blind corruption: noise, exactly

> **Theorem 29.3 (candidate-blind mis-anchoring is a garbling, monotonically in the rate).** Let $(\varepsilon, Q)$ be candidate-blind. Then:
> 1. $\tilde v = G \circ v$ for the channel $G(y' \mid y) = (1 - \varepsilon)\, \delta_y(y') + \varepsilon\, Q(y')$; hence $\tilde v \preceq_B v$, all strata are non-increasing (Lemma 27.7), Bayes risks are non-decreasing (Blackwell–Sherman–Stein, §20.1), and the DPI applies to any further registration.
> 2. Degradation is monotone in the rate: for $0 \le \varepsilon' \le \varepsilon \le 1$ with $\varepsilon' < 1$ and common clutter $Q$,
> $$
> \tilde v_{\varepsilon} \;=\; (1 - \lambda)\, \tilde v_{\varepsilon'} + \lambda\, Q
> \quad\text{with}\quad
> \lambda = \frac{\varepsilon - \varepsilon'}{1 - \varepsilon'} \in [0, 1],
> $$
> so $\tilde v_{\varepsilon} \preceq_B \tilde v_{\varepsilon'}$: fewer intrusions is Blackwell-better.
>
> *Proof.* 1: $(G \circ v)(y' \mid Z) = (1-\varepsilon) v(y' \mid Z) + \varepsilon Q(y') = \tilde v(y' \mid Z)$. 2: Expand the right-hand side: $(1-\lambda)(1-\varepsilon') v + \big((1-\lambda)\varepsilon' + \lambda\big) Q$; the stated $\lambda$ gives $(1-\lambda)(1-\varepsilon') = 1 - \varepsilon$ and hence coefficient $\varepsilon$ on $Q$; and mixing with a fixed $Q$ at rate $\lambda$ is itself candidate-blind contamination, a garbling by item 1. $\square$

> **Theorem 29.4 (the stratum trichotomy under blind corruption).** Let $(\varepsilon, Q)$ be candidate-blind with $0 < \varepsilon < 1$. Then:
> 1. **(Annihilation of $\sigma^0$.)** $\mathrm{supp}\,\tilde v(\cdot \mid Z) = \mathrm{supp}\, v(\cdot \mid Z) \cup \mathrm{supp}\, Q$ for every $Z$; since $\mathrm{supp}\,Q \ne \varnothing$, every pair of candidates is confusable, the confusability graph is complete, and
> $$
> \sigma^{0}(\tilde v) = \bot .
> $$
> An arbitrarily small blind mis-anchoring rate destroys all zero-error content: the zero-error stratum is infinitely fragile.
> 2. **(Invariance of $\sigma^=$.)** The map $p \mapsto (1-\varepsilon)p + \varepsilon Q$ on $\Pr(Y)$ is injective for $\varepsilon < 1$, so
> $$
> \sigma^{=}(\tilde v) = \sigma^{=}(v):
> $$
> statistical content — and with it asymptotic answerability (Theorem 22.2) — is *exactly* preserved. Blind mis-anchoring is invisible to the repetition ledger.
> 3. **(Bracketed degradation of $\widehat\sigma$.)** For every prior $\mu$ and question $q$,
> $$
> e_\mu(q \mid v) \;\le\; e_\mu(q \mid \tilde v) \;\le\; (1 - \varepsilon)\, e_\mu(q \mid v) + \varepsilon .
> $$
>
> *Proof.* 1: Immediate from the mixture form and Definition 21.6, connected components of a complete graph being a single block. 2: $(1-\varepsilon)p + \varepsilon Q = (1-\varepsilon)p' + \varepsilon Q$ gives $(1-\varepsilon)(p - p') = 0$, so $p = p'$; hence $\tilde v(\cdot \mid Z) = \tilde v(\cdot \mid Z') \iff v(\cdot \mid Z) = v(\cdot \mid Z')$. 3: The lower bound is Theorem 29.3(1) with Blackwell–Sherman–Stein. For the upper bound, play the $v$-optimal rule $\alpha^*$ on the perceived data: its error is $\sum_Z \mu(Z)\big[(1-\varepsilon)\Pr_v(\alpha^* \ne q \mid Z) + \varepsilon \Pr_{Y \sim Q}(\alpha^*(Y) \ne q(Z))\big] \le (1-\varepsilon)\, e_\mu(q \mid v) + \varepsilon$. $\square$

The trichotomy is a strong validation of Part III's refusal to let graded content be one thing: the *same* corruption, at the *same* rate, is fatal to one ledger ($\sigma^0$), invisible to another ($\sigma^=$), and merely costly, within an explicit bracket, to the third ($\widehat\sigma$). Any single-number theory of "the information degraded by mis-anchoring" would have to average these three verdicts and would thereby misreport all of them.

> **Remark 29.5 (Le Cam deficiency of blind corruption).** Since $\|\tilde v(\cdot \mid Z) - v(\cdot \mid Z)\|_{TV} = \varepsilon\, \|Q - v(\cdot \mid Z)\|_{TV} \le \varepsilon$ for every $Z$, the identity transition witnesses $\delta(\tilde v, v) \le \varepsilon$ in Le Cam's deficiency (total-variation normalization) [Le Cam 1964]; and $\delta(v, \tilde v) = 0$ by Theorem 29.3(1). Blind mis-anchoring at rate $\varepsilon$ therefore costs at most $\varepsilon$, uniformly over all decision problems, in the approximate comparison of experiments. This is the first anchored instance of the Le Cam thread flagged in §25 as the quantitative refinement of the Blackwell stratum and the natural meeting point with approximate gluing (H4). In the enriched reading of Part III (§24, Remark 24.7), the bound is the first computed coefficient of an approximate-gluing cell. (Part V develops it into the $2\varepsilon$-stability of enriched cell defects; Proposition 40.1.)

### 29.3 Candidate-dependent corruption: not noise

> **Theorem 29.6 (targeted mis-anchoring re-authors the experiment).** Candidate-dependent patterns can place the perceived view in **any** Blackwell relation to the intended one:
> 1. **(Creation: the leak at the feature level.)** There are $v$ and a pattern with $\sigma^{=}(\tilde v) > \sigma^{=}(v)$; consequently $\tilde v$ is not a garbling of $v$ (Lemma 27.7), and indeed $\tilde v \succ_B v$ is realizable with $v$ Blackwell-null.
> 2. **(Destruction beyond garbling.)** There are $v$ and a pattern with $\sigma^{=}(\tilde v) < \sigma^{=}(v)$ collapsing distinctions entirely.
> 3. **(Incomparability.)** There are $v$ and a pattern with $\sigma^{=}(\tilde v)$ and $\sigma^{=}(v)$ incomparable in $\mathrm{Part}(D)$; then neither experiment is a garbling of the other.
>
> *Proof.* 1: Let $D = \{Z_1, Z_2\}$, $Y = \{0,1\}$, $v(\cdot \mid Z_i) = p$ for both candidates ($\sigma^=(v) = \bot$; $v$ is null). Take $\varepsilon(Z_1) = 0$, $\varepsilon(Z_2) = \tfrac12$, $Q_{Z_2} = q \ne p$. Then $\tilde v(\cdot \mid Z_1) = p \ne \tfrac12 p + \tfrac12 q = \tilde v(\cdot \mid Z_2)$, so $\sigma^=(\tilde v) = \top$. A null experiment is a garbling of anything, so $\tilde v \succ_B v$.
> 2: Let $v(\cdot \mid Z_1) = (\tfrac12, \tfrac12)$, $v(\cdot \mid Z_2) = (1, 0)$, $\varepsilon(Z_1) = 0$, $\varepsilon(Z_2) = \tfrac12$, $Q_{Z_2} = (0,1)$. Then $\tilde v(\cdot \mid Z_2) = \tfrac12(1,0) + \tfrac12(0,1) = (\tfrac12, \tfrac12) = \tilde v(\cdot \mid Z_1)$: $\sigma^= $ collapses from $\top$ to $\bot$.
> 3: Combine the mechanisms on disjoint parts of $D = \{1,2,3,4\}$, $Y = \{0,1\}$. Honest laws: $v_1 = v_2 = (\tfrac14, \tfrac34)$, $v_3 = (1,0)$, $v_4 = (\tfrac12, \tfrac12)$; so $\sigma^=(v) = \{\,12 \mid 3 \mid 4\,\}$. Pattern: $\varepsilon(1) = \varepsilon(4) = 0$; $\varepsilon(2) = \tfrac12$, $Q_2 = (1,0)$; $\varepsilon(3) = \tfrac12$, $Q_3 = (0,1)$. Then $\tilde v_1 = (\tfrac14, \tfrac34)$, $\tilde v_2 = \tfrac12(\tfrac14,\tfrac34) + \tfrac12(1,0) = (\tfrac58, \tfrac38)$, $\tilde v_3 = \tfrac12(1,0) + \tfrac12(0,1) = (\tfrac12,\tfrac12) = \tilde v_4$; so $\sigma^=(\tilde v) = \{\,1 \mid 2 \mid 34\,\}$. Neither of $\{12 \mid 3 \mid 4\}$ and $\{1 \mid 2 \mid 34\}$ refines the other; by Lemma 27.7 (applied in both directions) neither experiment garbles the other. $\square$

The moral completes the sharpening promised in §26: **mis-anchoring is noise exactly when it is blind.** A candidate-dependent pattern is not a processing of the intended experiment — it is a different emission, and the difference can be informative (item 1 is the feature-level form of anchoring leakage: the *rate pattern* $\varepsilon(\cdot)$ is itself a view on $D$, manifesting statistically when its indicator is unobserved), destructive (item 2), or both at once (item 3). Auditability is the operational face of item 1: where intrusion indicators can be observed (provenance checks, adjudicated subsamples), they are a legitimate additional view and their content is governed by the ordinary theory; where they cannot, their content surfaces as an uninterpreted statistical distinction, indistinguishable from honest signal — the epistemically dangerous case, and the anchored ancestor of dataset-shift pathologies.

### 29.4 Family-level corruption: intrusion coupling

Mis-anchoring across a view family introduces one further degree of freedom, and it lands exactly on a mechanism Part III has already isolated.

> **Definition 29.7 (family pattern).** For a finite view set $S$ of a coherent family with joint channel $P_S$, a **family mis-anchoring pattern** consists of, for each $Z$: a law $\lambda_Z$ on subsets $\kappa \subseteq S$ (the **intrusion configuration**) and clutter laws $R_{Z, \kappa} \in \Pr\big(\prod_{i \in \kappa} Y_i\big)$; the perceived joint draws $y \sim P_S(\cdot \mid Z)$, independently $\kappa \sim \lambda_Z$ and $r \sim R_{Z,\kappa}$, and outputs $y$ with its $\kappa$-coordinates replaced by $r$. The pattern is **jointly candidate-blind** if $\lambda_Z$ and $R_{Z,\kappa}$ do not depend on $Z$; it is **marginally candidate-blind** if each single view's induced pattern is candidate-blind.

> **Proposition 29.8 (intrusion coupling).**
> 1. **(Joint blindness.)** A jointly candidate-blind pattern is a garbling of the honest joint: draw the intrusion subset and clutter independently of the candidate, retaining the other coordinates. It cannot increase Blackwell content. If $\lambda(\varnothing)>0$, it preserves the equal-law partition by Lemma 41.1. It need not annihilate zero-error content: anti-correlated erasures of two identity copies can always leave one reveal. A positive common full-support replacement of the whole record is sufficient for zero-error annihilation.
> 2. Marginal blindness does not imply joint blindness, and the gap is a coupling channel: there is a family with *constant* honest channels (each view Blackwell-null, jointly and severally) and a marginally blind pattern whose perceived family exhibits the strict statistical superadditivity of Proposition 22.4(2):
> $$
> \sigma^{=}(\tilde P_{\{v,w\}}) = \top \;>\; \bot = \sigma^{=}(\tilde v) \vee \sigma^{=}(\tilde w).
> $$
>
> *Proof.* 1: The replacement operation reads only the honest profile $y$ and the $Z$-independent draws $(\kappa, r)$, hence defines a channel on the output space; composing it with $P_S$ yields $\tilde P_S$ by (A7)'s independence clause. 2: Let $D = \{Z, Z'\}$, $Y_v = Y_w = \{0,1\}$, honest emissions deterministic at $0$ under both candidates, and clutter $\delta_1$ on each view. Intrusion configurations: under $Z$, both views intrude together or neither, each with probability $\tfrac12$; under $Z'$, the two views intrude independently with probability $\tfrac12$ each. Each view's marginal pattern is candidate-blind (rate $\tfrac12$, clutter $\delta_1$, under both candidates), so each perceived marginal is $\tfrac12\delta_0 + \tfrac12\delta_1$ under both candidates: $\sigma^=(\tilde v) = \sigma^=(\tilde w) = \bot$. The perceived joints differ: under $Z$, uniform on $\{00, 11\}$; under $Z'$, uniform on $\{00,01,10,11\}$. Hence $\sigma^=(\tilde P_{\{v,w\}}) = \top$. $\square$

Proposition 29.8(2) is Proposition 22.4's coupling mechanism realized **inside the anchoring layer**, with every feature channel honest and every marginal pattern blameless: correlated intrusions are a physical source of coupling. The count of synergy mechanisms in §23.2 is unchanged — this is a source of the coupling mechanism, not a fourth mechanism — but the finding matters for two reasons. Practically, it identifies cross-record identity swaps (the same foreign entity contaminating several fields or sensors coherently) as a generator of exactly the joint-only distinctions that PID registers as synergy and that no per-view audit can detect. Structurally, it shows that anchored families widen the coupling indeterminacy of Remark 21.3 — the couplings of the perceived family now include intrusion couplings the honest family knows nothing about — which is one more anchored input to the marginal-problem/no-global-section phenomenon at hook H4.

---

## 30. Comparison of anchoring policies

### 30.1 Two orders on policies

> **Definition 30.1 (fidelity and informativeness).** Fix a scenario, an emission, and a correspondence $\eta$. For $\eta$-compatible attributions $A, A'$:
> - $A$ **fidelity-dominates** $A'$ if $\varepsilon_A(Z) \le \varepsilon_{A'}(Z)$ for every $Z \in D$ (pointwise comparison of error profiles);
> - $A$ **informativeness-dominates** $A'$ (relative to a designated record) if the record channel induced by $A$ Blackwell-dominates that induced by $A'$.
>
> For the tracked-target theory below, the designated record is the **accepted record**: the presentation $y$ if the attribution selected $t^*$, and the null symbol $\varnothing$ otherwise — the record of an interpreter who keeps what is anchored to the target and registers a gap where anchoring went elsewhere.

The kernel's instinct — inherited from Lemma 4.7, where the most faithful registration (canonical) was also the most informative — is that the two orders agree. They do not.

### 30.2 The loyalty anomaly

> **Proposition 30.2 (the loyalty anomaly: fidelity-extremal is not informativeness-extremal).** There is a tracked-target scenario with an error-free loyal policy $\ell$ and a compatible policy $a$ with $\varepsilon_a(Z) = 1$ for some $Z$, such that the accepted record of $a$ **strictly Blackwell-dominates** that of $\ell$: the maximally erring policy is strictly more informative than the faultless one.
>
> *Proof.* Let $D = \{Z_1, Z_2\}$, $o \equiv t^*$, $Y = \{y_0\}$, $C = \{c_1, c_2\}$, emission $E(\cdot \mid Z_i) = \delta_{(y_0, c_i)}$, distractor $d \in \widehat{T}$, and correspondence $\eta(y_0, c_1) = \{t^*\}$, $\eta(y_0, c_2) = \{t^*, d\}$. The loyal policy $\ell$ selects $t^*$ always: $\varepsilon_\ell \equiv 0$, and its accepted record is $\delta_{y_0}$ under both candidates — Blackwell-null. The policy $a$ selecting $t^*$ on $c_1$ (forced) and $d$ on $c_2$ has $\varepsilon_a = (0, 1)$, and its accepted record is $\delta_{y_0}$ under $Z_1$ and $\delta_{\varnothing}$ under $Z_2$: disjoint supports, $\sigma^0 = \top$. A null experiment is a garbling of any experiment, and not conversely here; so $a$'s record strictly dominates $\ell$'s. $\square$

The mechanism is §28's leakage wearing a different coat: $a$'s errors are context-driven, the context is candidate-revealing, and the error pattern smuggles it into the record. Anchoring errors are a channel; when that channel is candidate-dependent, error-minimization and information-maximization are different objectives, and a policy can be worth more *because* it errs. The kernel-like coincidence of the two orders is not gone, however — it holds exactly where the leak is closed.

### 30.3 The extremal-policy theorem

> **Definition 30.3 (sterile context).** An emission $E : D \to \Pr(Y \times C)$ has **sterile context** if it factors as $E(y, c \mid Z) = v(y \mid Z)\, \gamma(c \mid y)$ with $\gamma$ independent of $Z$ — equivalently, $C \perp Z \mid Y$: given the presentation, the context carries no further information about the candidate.

> **Theorem 30.4 (sterile-context extremality; the anchoring analogue of Lemma 4.7).** In a tracked-target scenario with sterile context and no clutter, the accepted record of every loyal policy Blackwell-dominates the accepted record of every $\eta$-compatible attribution:
> $$
> \tilde v_{A} \;\preceq_B\; \tilde v_{\ell}
> \qquad \text{for all compatible } A \text{ and loyal } \ell .
> $$
> Loyalty is thus simultaneously fidelity-extremal (Proposition 27.5(1)) and informativeness-extremal. Moreover sterility is exactly what the theorem needs: without it, Proposition 30.2 exhibits an error-free loyal policy strictly dominated.
>
> *Proof.* For a compatible attribution $A$, define the acceptance rate $s_A(y) = \sum_c \gamma(c \mid y)\, A(t^* \mid y, c)$ — independent of $Z$ by sterility. The accepted record is $\tilde v_A(y \mid Z) = v(y \mid Z)\, s_A(y)$ and $\tilde v_A(\varnothing \mid Z) = 1 - \sum_y v(y \mid Z)\, s_A(y)$. Compatibility gives $A(t^* \mid y, c) \le \mathbb{1}\{t^* \in \eta(y,c)\}$ pointwise, with equality for loyal $\ell$; hence $s_A(y) \le s_\ell(y)$ for all $y$. Define a channel $G$ on $Y \cup \{\varnothing\}$: on $y$ with $s_\ell(y) > 0$, pass $y$ with probability $s_A(y)/s_\ell(y)$ and output $\varnothing$ otherwise; on $y$ with $s_\ell(y) = 0$ (then $s_A(y) = 0$ and $y$ is never emitted by $\tilde v_\ell$), act arbitrarily; on $\varnothing$, output $\varnothing$. Then $(G \circ \tilde v_\ell)(y \mid Z) = v(y \mid Z)\, s_\ell(y) \cdot s_A(y)/s_\ell(y) = \tilde v_A(y \mid Z)$, and the $\varnothing$-masses match by complementation; so $\tilde v_A = G \circ \tilde v_\ell$. $\square$

**Mathematical scope.** Sterility is a sufficient uniform hypothesis, not a necessary condition for extremality in each fixed scenario. Nonsterile context with a forced loyal correspondence is an immediate counterexample to necessity. Proposition 30.2 establishes failure in some nonsterile scenarios only.

The shape is exactly Lemma 4.7's: an extremal element (loyal $\ell$, as canonical $\kappa^{\mathrm{can}}$ there) dominating a class (compatible attributions, as sound registrations there) that is not itself totally ordered — different sub-loyal policies' records are in general Blackwell-incomparable, just as different sound registrations are. And the theorem's boundary is exactly the leak: sterility says the context has nothing to smuggle, whence errors can only *thin* the record; the moment context is informative, the loyalty anomaly is available. In the collapse idiom of §24: the fidelity and informativeness orders coincide on a kernel-like sublocus and come apart off it, with leakage as the responsible mechanism.

> **Remark 30.4′ (the missingness reading).** The accepted record is a missing-data structure: a presentation is observed with probability $s_A(y)$ and replaced by the gap symbol $\varnothing$ otherwise. Sterility makes the acceptance mechanism depend on the raw material only through the presentation itself — no residual dependence on the candidate — which is the anchored counterpart of the ignorability conditions of the missing-data literature [Rubin 1976]: under it, Theorem 30.4 says the mechanism can only *thin* the loyal record (gaps still shift likelihoods, but never carry more than a garbling of the full record carries). Off sterility the mechanism is informative missingness — the missing-not-at-random regime — and the loyalty anomaly is its constructive exhibit: the pattern of gaps is itself a channel on $D$, and a policy can be worth more because of what its gaps reveal. The bridge is useful in both directions: missing-data practice supplies diagnostics and sensitivity analyses for exactly the non-sterile regime the extremality theorem excludes, and the framework returns, via Corollary 28.1, a stratified account of what an informative gap pattern can answer.

> **Remark 30.5 (cluttered scenes: acceptance as testing).** With clutter present, loyalty over-accepts: a policy that attributes to $t^*$ whenever admissible also admits every plausible foreign presentation, minimizing omissions at the price of contamination. Acceptance then becomes a per-presentation hypothesis test (target vs. clutter), the omission/contamination pair is a type-II/type-I error pair, and no policy is extremal across clutter levels — the precision–recall trade-off in its anchored form. The Bayes-optimal acceptance is likelihood-ratio thresholding on $(y,c)$, with the threshold set by the prior scene composition and the loss attached to each error type; this is scenario-dependent by nature, and the theory correctly refuses a uniform optimum here. Data-association practice reaches the same structure from the engineering side [Bar-Shalom & Fortmann 1988].

### 30.4 The identity regime: selection is constrained Bayes decision

> **Proposition 30.6 (identity selection is constrained Bayes decision).** In the identity reading, fix a prior $\mu$ on $D$ and score policies by the attribution risk $\Pr_\mu(t \ne o(Z))$. Then among $\eta$-compatible attributions the risk is minimized by any **constrained Bayes selector**
> $$
> a_\mu(y, c) \;\in\; \operatorname*{arg\,max}_{t \,\in\, \eta(y,c)} \; \pi(t \mid y, c),
> \qquad
> \pi(t \mid y, c) \;\propto \sum_{Z \,:\, o(Z) = t} \mu(Z)\, E(y, c \mid Z),
> $$
> and the minimal risk is $1 - \mathbb{E}\big[\max_{t \in \eta(y,c)} \pi(t \mid y, c)\big]$.
>
> *Proof.* $\Pr_\mu(t = o(Z)) = \mathbb{E}_{(y,c)} \sum_t A(t \mid y, c)\, \pi(t \mid y, c)$; for each $(y,c)$ the inner sum is maximized, subject to $\mathrm{supp}\,A(\cdot \mid y,c) \subseteq \eta(y,c)$, by concentrating the mass on a maximizer of $\pi(\cdot \mid y, c)$ over $\eta(y,c)$. $\square$

Three consequences knit the regime into the standing theory. First, by Proposition 27.5(2) there is no prior-free optimum: the identity regime admits only $\mu$-indexed optimality, exactly the decision-theoretic structure Part III built and precisely why the interface deferred anchoring until the graded toolkit existed. Second, selection is literally answering $q_o$: policies are decision rules for the identity question, their verdict channels are compared as experiments, and Corollary 28.1 already stratifies what any of them can achieve. Third, the classical theory of record linkage is the two-hypothesis case: with $\widehat{T}$-values "match"/"non-match" and a reject option (the status "possible link," playing the role of $\bot$), the optimal linkage rule of [Fellegi & Sunter 1969] — threshold the likelihood ratio of the comparison vector, with an indeterminate band — is the constrained Bayes selector of Proposition 30.6 with the reject region determined by the error-rate constraints; the founding computational proposal [Newcombe et al. 1959] is its empirical ancestor. Entity resolution is thereby placed where the framework says it belongs: not upstream of inference but as an instance of it.

---

## 31. Worked example D: record linkage with leakage

The example exercises the identity regime, the Bayes selector, leakage, and the record hierarchy on the smallest scale that shows them all.

**Setup.** An incoming lab record must be attributed to one of two patients: $D = \{P_1, P_2\}$, identity reading, $\widehat{T} = \{P_1, P_2, \bot\}$, $o$ the inclusion. The presentation is $y = (\text{initials}, \text{value})$ with initials fixed at the colliding "J.S." and value in $\{\mathrm{lo}, \mathrm{hi}\}$; the context is the source clinic $c \in \{\mathrm{A}, \mathrm{B}\}$. Emission: $P_1$ attends clinic A only and reads lo with probability $\tfrac34$; $P_2$ attends clinic B only and reads hi with probability $\tfrac34$. The correspondence is name-based: $\eta(y, c) = \{P_1, P_2\}$ for every raw presentation (both patients match the initials; every anchoring event is **ambiguous** in the taxonomy of Definition 19.4 — the clinic is evidence, not a constraint).

**Selection as inference.** The clinic determines the patient, so the policy $a_{\mathrm{clinic}}$ (select $P_1$ on A, $P_2$ on B) has $\varepsilon \equiv 0$; it is the constrained Bayes selector of Proposition 30.6 for every full-support prior, here achieving zero risk. Its verdict channel is $\alpha(P_i) = \delta_{P_i}$: $\sigma^0(\alpha) = \top$ — attribution answers the identity question with single-look certainty, although no field of the presentation alone does.

**Leakage and the record hierarchy.** The forgetful record $N$ (the value alone, initials being constant) has $\sigma^=(N) = \top$ (the laws $(\tfrac34, \tfrac14)$ and $(\tfrac14, \tfrac34)$ differ — identity is asymptotically resolvable from values by Theorem 22.2) but $\sigma^0(N) = \bot$ (overlapping supports — no single value certifies). The standard record $S = (y, t)$ under $a_{\mathrm{clinic}}$ has $\sigma^0(S) = \top$: the verdict carries the clinic into the record after the context is dropped, upgrading resolution from asymptotic to single-look. This is Proposition 28.2's carrying capacity in benign form — and Corollary 28.3's warning in concrete form: a pipeline that linked records and then discarded the link verdicts would demote its own content by a full stratum.

**The loyalty anomaly in miniature.** The tie-break policy $a_1$ ("always $P_1$") has error profile $(0, 1)$ and a constant verdict: fidelity-poor and informativeness-null at once — until audited, when its error indicator (an intrusion-indicator view in the sense of §29.3) restores $\top$. Which record the institution keeps decides which theorem governs it.

**A corruption coda.** If clinic B occasionally forwards records of an unrelated J.S., the accepted stream under $a_{\mathrm{clinic}}$ acquires a foreign-acceptance pattern concentrated on one candidate's file — candidate-dependent contamination, §29.3's regime, with Theorem 29.6's bidirectional consequences; the blind theorems of §29.2 apply only if the intrusions are indifferent to which patient is actual. The example ends where the stream dynamics deferred by (A7) begin.

---

## 32. Recovery and the fidelity axis

### 32.1 Recovery

> **Theorem 32.1 (qualified recovery).** Under sound unique anchoring, the realized verdict is forced and anchoring error is zero. Always $F\simeq_B E$ and $N\preceq_B S\preceq_B F$. In the tracked-target reading $T$ is constant, so $S\simeq_B N$; equality with $E=(Y,C)$ additionally requires sterile context $C\perp Z\mid Y$. Without it, constant $Y$ and candidate-revealing $C$ refute the former all-record equivalence. In the identity reading the verdict answers $o$, but need not recover distinctions inside an origin class or all context.
>
> For blind whole-record contamination with fixed clutter and rate $\varepsilon<1$, Theorems 29.3–29.4 give monotone Blackwell recovery as $\varepsilon\downarrow0$, invariant $\sigma^=$, and possibly discontinuous $\sigma^0$. For targeted contamination of rate at most $\varepsilon$, both deficiencies to the honest channel are at most $\varepsilon$ by the identity simulator, although no Blackwell direction is forced. Thus small targeted corruption has metric recovery too.
>
> *Proof.* The record relations are projections and attribution processing. Sterility supplies a candidate-independent simulator $C\mid Y$. The contamination conclusions follow by mixture coupling and the cited theorems. $\square$

### 32.2 The fidelity axis

The structural-collapse table of §24 tracked two degradation axes — the codomain of content and the compositionality of the content map — across the relaxation of (A3) and (A2). Retiring (A4′) does not primarily degrade either; it degrades a third thing that Parts I–III never had to distinguish from the others because it was identically perfect there: the **relation of the perceived experiment to the intended one**. Part IV's results sort into a trichotomy along this axis.

| anchoring regime | perceived vs. intended | governing results |
|---|---|---|
| sound & unique (A4′) | equal | Theorem 32.1(1); Parts I–III verbatim; verdict $=$ identity view |
| candidate-blind mis-anchoring | garbling, monotone in the rate | Theorems 29.3–29.4: $\sigma^0$ annihilated for any $\varepsilon > 0$; $\sigma^=$ exactly invariant for $\varepsilon < 1$; $\widehat\sigma$ degraded within the bracket; deficiency $\le \varepsilon$ (Remark 29.5) |
| candidate-dependent mis-anchoring | arbitrary: $\succeq_B$, $\preceq_B$, or incomparable | Theorem 29.6: the experiment is re-authored; leakage, collapse, and incomparability all realizable; Proposition 29.8: intrusion coupling sources joint-only content |

Read against §24: the kernel was the maximal-structure fiber of the *algebra*; (A4′) is the maximal-structure fiber of *fidelity*. Off it, the blind regime keeps the two experiments comparable — corruption is honest noise, and every Part III instrument (DPI, Blackwell monotonicity, the strata) measures it — while the targeted regime severs comparability itself: the interpreter's experiment is no longer a degraded copy of the intended one but a different experiment whose difference is partly *made of information* (the leak). The anomalies of the part — leakage, the loyalty anomaly, intrusion coupling — are the price receipts of this axis, in exactly the sense of §24's closing paragraph. And the axis feeds H4 twice over: intrusion couplings widen the marginal problem of Remark 21.3, and the fidelity trichotomy gives the prospective obstruction theory a new base datum — local records that fail to glue not because the views disagree but because they are not records *of the same experiment*. In the schema of Part III (§24, Definitions 24.3–24.5), fidelity is thereby a further coordinate of a content system, alongside codomain, cell-invertibility, and representability: it indexes which experiment the system is *about*, and the blind/targeted split classifies whether the perceived system is a garbled instance of the intended one at all. Both feeds are cashed in Part V: intrusion coupling generates motion along coupling fibers (Proposition 39.4), and the trichotomy becomes a classification of what corruption does to descent data — jointly blind corruption is a presheaf endomorphism preserving every statistical-stratum obstruction, marginal-only blindness creates classes at every rate, and targeted corruption severs the comparison itself (Theorem 41.2, Proposition 41.3, Remark 41.4).

---

## 33. Established results and scope

The part establishes the irreparable attribution floor, record processing order, leakage examples, explicit corruption comparisons, and sterile-context loyalty extremality. Selective acceptance is a separate channel from forgetting verdicts. Jointly blind partial replacement is a garbling but need not destroy zero-error information. Recovery is exactly the record relation and metric convergence stated in Theorem 32.1.

**References added in Part IV** (see Parts I–III for those already cited):

- Bar-Shalom, Y., and Fortmann, T. E. (1988). *Tracking and Data Association.* Academic Press.
- Fellegi, I. P., and Sunter, A. B. (1969). "A Theory for Record Linkage." *Journal of the American Statistical Association* 64(328), 1183–1210.
- Huber, P. J. (1964). "Robust Estimation of a Location Parameter." *The Annals of Mathematical Statistics* 35(1), 73–101.
- Newcombe, H. B., Kennedy, J. M., Axford, S. J., and James, A. P. (1959). "Automatic Linkage of Vital Records." *Science* 130(3381), 954–959.
- Rubin, D. B. (1976). "Inference and Missing Data." *Biometrika* 63(3), 581–592.
