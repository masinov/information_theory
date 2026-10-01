# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part III: The Anchoring Interface and the Graded Theory

---

## 18. Overview of Part III

Part III does two things. Section 19 fixes the *interface* for anchoring: it introduces the types — raw presentations, contexts, attribution spaces, correspondences, selection policies — in which the attribution step will be modelled in Part IV, and adopts the standing assumption (A4′) that every view is soundly and uniquely anchored. It proves no theorems.

Sections 20–24 relax (A2). A view becomes a channel $D \to \Pr(Y)$, and a view family must specify the joint channels of its subsets, since marginal channels do not determine how their noises are coupled. The finiteness assumption (A6) is adopted for the whole stochastic theory. The kernel's single content object $\sigma(S)$ then splits into three:

- **zero-error content** $\sigma^0(S)$, which governs what can be answered with certainty from one observation (Theorem 22.1);
- **statistical content** $\sigma^{=}(S)$, which governs what can be answered with vanishing error under unlimited repetition (Theorem 22.2);
- **full content** $\widehat\sigma(S)$, the Blackwell class of the joint channel, which retains every trade-off between error and prior.

Section 22 determines the fate of the kernel theorems at each stratum: the adjunction fails for zero-error content even under conditional independence but survives on its confusability graph, holds for statistical content exactly on conditionally independent families, and has no join to refer to at the full stratum (Propositions 22.3–22.5); the terminal consolidation becomes the minimal sufficient statistic (Theorem 22.6); and the entropic criteria connect the strata to Shannon quantities (Theorem 22.7). Section 23 combines noise with admissibility and finds that independent noisy readings can accumulate past a joint ceiling (Proposition 23.3). Section 24 proves that the deterministic channels recover the kernel exactly (Theorem 24.2) and organizes the results in a common schema.

---

## 19. The anchoring interface (H1: signature only)

The kernel's Definition 4.2 gives a view as a function $v : D \to Y_v$. This presupposes — standing assumption (A4) — that every presentation arrives already attributed: it is *of* the unknown candidate, not of something else, and the attribution is correct. Real presentations do not arrive so labeled: an entity mention must be resolved, a sensor trace must be attributed to a source, a data record must be matched to the patient it describes. This section fixes the types in which that attribution step will be modeled. It states no theorems; its purpose is to commit the framework to a signature so that the graded theory of §§20–24, and all later layers, are built against it.

> **Definition 19.1 (raw presentation).** A **raw presentation** is a pair $(y, c)$ with $y \in Y$ a **presentation** in a presentation space and $c \in C$ a **context** in a context space. The context carries whatever accompanies the presentation without being part of it: provenance metadata, time, channel identity, surrounding discourse.

> **Definition 19.2 (attribution space).** An **attribution space** is a set $\widehat{T}$ of **candidate origins**, together with a distinguished element $\bot \in \widehat{T}$ representing *no admissible origin*. Origins are the things presentations can be *of*: emitting entities, sources, referents.

> **Definition 19.3 (anchoring scenario; origin map).** An **anchoring scenario** for the contrast domain $D$ is an attribution space $\widehat{T}$ together with an **origin map**
> $$
> o : D \to \widehat{T} \setminus \{\bot\}
> $$
> assigning to each candidate the origin that presentations emitted under that candidate actually have. Elements of $\widehat{T} \setminus (o(D) \cup \{\bot\})$ are **distractors**: admissible-looking origins that no candidate realizes. Two readings of $o$ delimit the intended range. In the **tracked-target reading**, $o$ is constant: $D$ is the state space of a single observed target, and every presentation genuinely of it shares one origin. In the **identity reading**, $o$ is injective: $D$ is a space of possible identities of the emitter — the entity-resolution regime — and the origin varies with the candidate. Mixed cases are permitted.

> **Definition 19.4 (anchoring correspondence).** An **anchoring correspondence** is a map
> $$
> \eta : Y \times C \longrightarrow \mathcal{P}(\widehat{T}) \setminus \{\varnothing\},
> $$
> assigning to each raw presentation its set of admissible attributions. The **anchoring status** of $(y,c)$ is:
>
> - **unambiguous** if $\eta(y,c)$ is a singleton other than $\{\bot\}$;
> - **ambiguous** if $|\eta(y,c)| \ge 2$;
> - **failed** if $\eta(y,c) = \{\bot\}$.

> **Definition 19.5 (selection policy; anchoring error).** A **selection policy** for $\eta$ is a map $a : Y \times C \to \widehat{T}$ with $a(y,c) \in \eta(y,c)$: it resolves each raw presentation to a single attribution among the admissible ones. Relative to a scenario $(\widehat{T}, o)$ and a policy $a$, an anchoring event for a presentation actually emitted under candidate $Z$ is **erroneous** (a **mis-anchoring**) if $a(y,c) \ne o(Z)$, and **irreparable** if $o(Z) \notin \eta(y,c)$ — in the latter case every policy errs, so the defect lies in the correspondence, not in the selection. The distinction matters because the remedies differ: selection error is reducible by a better policy over the same $\eta$; correspondence error requires changing $\eta$ itself.

> **Definition 19.6 (anchored view, generalized signature).** A **generalized view** relative to an anchoring scenario $(\widehat{T}, o)$ is a tuple
> $$
> v = \big( Y_v,\; C_v,\; e_v,\; \eta_v,\; a_v \big)
> $$
> where $Y_v$ is a presentation space, $C_v$ a context space, $e_v$ an **emission component** describing how candidates give rise to presentations (in the exact case a map $e_v : D \to Y_v$; in the graded case of §21 a channel), $\eta_v$ an anchoring correspondence on $Y_v \times C_v$ valued in $\widehat{T}$, and $a_v$ a selection policy for $\eta_v$.

> **Definition 19.7 (kernel recovery; standing assumption A4′).** A generalized view is **soundly and uniquely anchored** if for every $Z \in D$ and every context $c \in C_v$ arising with $e_v(Z)$, the correspondence satisfies
> $$
> \eta_v\big(e_v(Z), c\big) = \{\,o(Z)\,\}
> $$
> — unambiguous, unfailed, and correct — whence the selection $a_v$ is forced and no anchoring event is erroneous. This condition forces the verdict but does not make context uninformative. If context is discarded, collapse to the presentation alone additionally requires $C\perp Z\mid Y$ (in the deterministic case, context is determined by the presentation). Under that additional condition the generalized view collapses to the kernel view $(Y_v, e_v)$ of Definition 4.2; under the tracked-target reading this is exactly the (A4) regime of Part I. Part III adopts, as standing assumption **(A4′)**, that all views are soundly and uniquely anchored.

> **Remark 19.8 (anchoring is channel-shaped).** The interface deliberately types anchoring so that it is not merely a pre-processing stage. The composite $Z \mapsto o(Z)$ is itself a view on $D$ in the sense of Definition 4.2 — the **identity view** — and the graded versions of the components are channels: emission $e_v : D \to \Pr(Y_v)$, attribution $Y_v \times C_v \to \Pr(\widehat{T})$, and their composite a channel $D \to \Pr(\widehat{T})$ over the same domain as the feature views. Anchoring quality thereby becomes Blackwell-comparable to feature content, and the substantive H1 theory should be expected to *couple* to the graded order of §§20–24 rather than sit orthogonally upstream of it. For this reason the interface fixes types and nothing else: freezing a pipeline (anchor first, then register) would prejudge a coupling that the graded theory is equipped to analyze.

**What is deliberately not done here.** No dynamics of attribution (how $\eta$ and $a$ are computed, from what evidence, at what reliability); no interaction between anchoring and content (how ambiguity, selection error, or irreparable mis-anchoring coarsens, distorts, or corrupts each stratum of content); no graded attribution theory — although every slot of Definition 19.6 is typed so that grading is a substitution, not a redesign (Remark 19.8). These constitute the substantive H1 theory and are deferred to a later part; the graded machinery about to be built — channels, Blackwell comparison, confusability, sufficiency — is precisely the toolkit that theory will need, which is the reason for the present ordering. Under (A4′), nothing in §§20–24 depends on this section beyond type compatibility.

---

## 20. Preliminaries for the graded theory

All material here is standard; sources accompany each notion. The following assumption is in force for the remainder of Part III.

> **(A6) Finiteness.** The contrast domain $D$ and all presentation spaces are finite. Probability distributions are points of the simplex $\Pr(Y)$; supports are $\mathrm{supp}\,p = \{y : p(y) > 0\}$.

### 20.1 Channels and garbling

A **channel** from $D$ to $Y$ is a map $P : D \to \Pr(Y)$; we write $P(y \mid Z)$ for the probability of presentation $y$ given candidate $Z$. A channel is **deterministic** if every $P(\cdot \mid Z)$ is a point mass; deterministic channels are exactly the kernel's views. Channels compose: for $G : Y \to \Pr(Y')$, the composite $(G \circ P)(y' \mid Z) = \sum_y G(y' \mid y) P(y \mid Z)$.

A channel $P'$ is a **garbling** of $P$, written $P \succeq_B P'$, if $P' = G \circ P$ for some channel $G$. The relation $\succeq_B$ is a preorder (the **Blackwell order**); by the Blackwell–Sherman–Stein theorem it coincides, for finite experiments, with uniform superiority in decision problems: $P \succeq_B P'$ iff for every prior on $D$ and every finite decision problem the optimal Bayes risk under $P$ is no worse than under $P'$ [Blackwell 1951, 1953; Torgersen 1991]. An **experiment** is a channel from $D$ considered up to Blackwell equivalence $\simeq_B$.

### 20.2 Sufficiency

Given a channel $P : D \to \Pr(Y)$, a map $T : Y \to Q$ is a **sufficient statistic** for the family $\{P(\cdot \mid Z)\}_{Z \in D}$ if the conditional distribution of the presentation given $T$ is the same for all candidates: for all $t$ with $\Pr(T = t \mid Z) > 0$, the distribution $P(\,\cdot \mid T = t, Z)$ does not depend on $Z$.

> **Fact 20.1 (factorization; finite case).** $T$ is sufficient iff there exist functions $g, h \ge 0$ with $P(y \mid Z) = g(T(y), Z)\, h(y)$ for all $y, Z$ [Halmos & Savage 1949].
>
> *Proof sketch.* ($\Leftarrow$) Compute the conditional given $T = t$ and observe cancellation of $g(t, Z)$. ($\Rightarrow$) Take $g(t, Z) = \Pr(T = t \mid Z)$ and $h(y) = P(y \mid T = T(y), Z)$ for any $Z$ with $\Pr(T = T(y) \mid Z) > 0$ (independent of $Z$ by sufficiency; set $h(y) = 0$ if no such $Z$ exists). $\square$

A sufficient statistic $T$ is **minimal** if it is a function of every sufficient statistic on the realized outcomes. Minimal sufficient statistics exist in the finite case and are constructed in Theorem 22.6 below [Lehmann & Scheffé 1950; Bahadur 1954].

### 20.3 Information measures

For jointly distributed finite variables, $H(\cdot)$, $H(\cdot \mid \cdot)$, $I(\cdot\,;\cdot)$, and $I(\cdot\,;\cdot \mid \cdot)$ denote entropy, conditional entropy, mutual information, and conditional mutual information [Cover & Thomas 2006]. Four standard facts are used repeatedly: $H(U \mid W) = 0$ iff $U$ is almost surely a function of $W$; the **data processing inequality (DPI)**: if $Z \to Y \to Y'$ is a Markov chain then $I(Z; Y') \le I(Z; Y)$, with equality iff $Z$ and $Y$ are conditionally independent given $Y'$ under that joint law (full support of the state prior is needed to conclude sufficiency at every candidate); the **chain rule**: $I(Z; Y, Y') = I(Z; Y) + I(Z; Y' \mid Y)$; and **Fano's inequality**: for any estimator $\widehat{q}$ of a variable $q$ with $M \ge 2$ values, $\Pr(\widehat q \ne q) \ge \big(H(q \mid Y) - 1\big)/\log_2 M$ [Cover & Thomas 2006].

### 20.4 Zero-error notions

For a channel $P$, two candidates are **confusable** if their output distributions share a support point; the resulting **confusability graph** underlies Shannon's zero-error theory of channels [Shannon 1956]. Zero-error questions of the present framework are governed by this graph (Theorem 22.1), not by any averaged quantity — the first indication that graded content is not one thing.

### 20.5 The categorical ambient (remark)

Everything this part uses — channels and their composition, determinism as a distinguished subclass, marginals, couplings, conditional independence, sufficiency — is native to **Markov categories**, the synthetic axiomatization of categorical probability [Cho & Jacobs 2019; Fritz 2020]. The development below stays concrete, but three consequences of the categorical reading are worth recording. First, the deterministic/graded relationship is structural: kernel views are the deterministic morphisms of the ambient Markov category, and the recovery theorem (Theorem 24.2) is the statement that the exact theory of Parts I–II is the restriction of the graded theory to that subcategory. Second, categorical treatments of sufficient statistics require their stated structural hypotheses [Fritz 2020]. Theorem 22.6 is proved here for finite experiments; Proposition A.1 extends existence of a lossless likelihood statistic to finite states and standard Borel observations. Third, Markov categories provide a language for possible generalization. They do not discharge quotient regularity, uniform identifiability, compactness, or measurable-selection hypotheses; Appendix A states the actual boundary.

---

## 21. Graded views and the stratification of content

### 21.1 Graded view families

> **Definition 21.1 (graded view).** A **graded view** on $D$ is a channel $v : D \to \Pr(Y_v)$. Under (A4′) its anchoring component is suppressed. Deterministic channels are identified with kernel views.

In the kernel, a set of views determined its compound view outright: the pairing $\langle v, w \rangle$ was constructed pointwise. Graded views lose this property: the marginal channels of $v$ and $w$ do not determine their joint behavior, because the noises may be coupled in different ways. This is a genuinely new degree of freedom with no kernel counterpart, and it must be built into the definition of a family.

> **Definition 21.2 (coherent graded family).** A **coherent graded view family** on $D$ is a set $V$ of graded views together with, for each finite $T \subseteq V$, a **joint channel** $P_T : D \to \Pr\big(\prod_{v \in T} Y_v\big)$, such that the assignment is **projective**: for $T' \subseteq T$, marginalizing $P_T$ onto the coordinates of $T'$ yields $P_{T'}$; and $P_{\{v\}} = v$. The family is **conditionally independent (CI)** if each $P_T$ is the product of its marginals given $Z$.

> **Remark 21.3 (coupling indeterminacy).** Distinct coherent families can share all their single-view channels and differ in every compound $P_T$. Content over view sets therefore depends on data the kernel never needed: the coupling. Moreover, a projectively consistent family of *pairwise* joints need not extend to a global joint at all — the classical marginal problem [Vorob'ev 1962] — which is exactly the no-global-section phenomenon analyzed sheaf-theoretically in [Abramsky & Brandenburger 2011]. Coupling indeterminacy is thus the graded theory's native entry point to hook H4 and is flagged here for that purpose. It is convenient to name the object: the **coupling fiber** over a marginal system $\{v\}_{v \in V}$ is the class of coherent families extending it. Vorob'ev's theorem characterizes the overlap structures over which the fiber is never empty; content over view sets is a function on the fiber, constant across it exactly when the coupling mechanism of Proposition 22.4(2) is absent. (The flag is cashed in Part V, §39: Vorob'ev's theorem is the unconditional-descent criterion of the coupling presheaf, and the fiber named here carries both of H4's failure modes — contextual evidence as its emptiness, underdetermination as its multiplicity — with coupling superadditivity located as non-constancy of $\sigma^{=}$ on fibers; Theorem 39.2, Proposition 39.3.)

### 21.2 Graded content: three strata

The kernel had one content object, $\sigma(S) \in \mathrm{Part}(D)$. Grading splits it into three, ordered by how much of the channel structure they retain.

> **Definition 21.4 (graded content, full stratum).** For finite $S \subseteq V$ of a coherent family, the **graded content** is the experiment
> $$
> \widehat{\sigma}(S) \;=\; [\,P_S\,]_{\simeq_B},
> $$
> the Blackwell class of the joint channel.

> **Definition 21.5 (statistical stratum).** The **graded registered representation** is the likelihood map
> $$
> \widehat{R}_S : D \to \Pr\Big(\textstyle\prod_{v \in S} Y_v\Big), \qquad \widehat{R}_S(Z) = P_S(\cdot \mid Z),
> $$
> and the **statistical content** is its kernel partition
> $$
> \sigma^{=}(S) \;=\; \ker\big(\widehat{R}_S\big) \in \mathrm{Part}(D):
> $$
> candidates are identified iff their output distributions are identical.

> **Definition 21.6 (zero-error stratum).** The **confusability relation** on $D$ is
> $$
> Z \approx_S Z' \;:\iff\; \mathrm{supp}\, P_S(\cdot \mid Z) \,\cap\, \mathrm{supp}\, P_S(\cdot \mid Z') \;\ne\; \varnothing,
> $$
> a reflexive and symmetric relation that is **not** transitive in general. The **zero-error content** $\sigma^{0}(S) \in \mathrm{Part}(D)$ is the partition of $D$ into connected components of $\approx_S$.

Definition 21.5 is the graded Definition 5.1–5.2: the registered representation of a candidate is no longer the set of unexcluded alternatives but the likelihood it induces, and indistinguishability is equality of likelihoods. Definition 21.6 captures a strictly more demanding operational notion — single-observation certainty — and its non-transitivity is the first structural novelty of grading: exact indistinguishability was an equivalence; confusability is only a tolerance, and content extraction must pass to components.

> **Lemma 21.7 (the strata are ordered).** For every finite $S$:
> $$
> \sigma^{0}(S) \;\le\; \sigma^{=}(S) \qquad \text{in } \mathrm{Part}(D),
> $$
> and both are monotone in $S$: $T \subseteq S$ implies $\sigma^{0}(T) \le \sigma^{0}(S)$ and $\sigma^{=}(T) \le \sigma^{=}(S)$. In the deterministic case $\sigma^{0}(S) = \sigma^{=}(S) = \sigma(S)$.
>
> *Proof.* If $\widehat R_S(Z) = \widehat R_S(Z')$ the two supports are equal, hence intersect (they are nonempty), so $Z \approx_S Z'$ and the two candidates share a $\sigma^0$-component; thus every $\sigma^=$-block lies in a $\sigma^0$-block, i.e. $\sigma^0(S) \le \sigma^=(S)$. Monotonicity of $\sigma^=$: if the joint likelihoods over $S$ are equal, their marginals over $T$ are equal. Monotonicity of $\sigma^0$: if joint supports over $S$ intersect at a point, its coordinates witness intersection of the marginal supports over $T$; so $\approx_S\; \subseteq\; \approx_T$ as edge sets, hence components over $S$ refine components over $T$. Deterministic case: point-mass likelihoods are equal iff the presentations are equal, and supports intersect iff the presentations are equal, so both relations coincide with $\sim_S$ and both partitions with $\sigma(S)$, the confusability relation being already transitive. $\square$

The interpretive content of the strata is fixed by the answerability theorems of the next section: $\sigma^0$ governs what can be answered *with certainty from one look*, $\sigma^=$ governs what can be answered *with vanishing error given unlimited repetition*, and $\widehat\sigma$ retains everything, including all intermediate error/prior trade-offs.

---

## 22. Fate of the kernel theorems under grading

### 22.1 Answerability grades into a family of notions

> **Definition 22.0.** Fix a question $q : D \to A_q$ and finite $S$. A (deterministic) **decision rule** is a map $\alpha : \prod_{v\in S} Y_v \to A_q$. The question is:
>
> - **zero-error answerable from $S$** if some rule satisfies $\Pr\big(\alpha(Y_S) = q(Z) \,\big|\, Z\big) = 1$ for every $Z \in D$;
> - **$\varepsilon$-answerable from $S$ under prior $\mu$** if some rule has Bayes error $e_\mu(q \mid S) := \Pr_{\mu}\big(\alpha(Y_S) \ne q(Z)\big) \le \varepsilon$;
> - **asymptotically answerable from $S$** if, with $n$ conditionally i.i.d. copies of $Y_S$ given $Z$, there are rules $\alpha_n$ whose worst-case error $\max_{Z} \Pr(\alpha_n \ne q(Z) \mid Z)$ tends to $0$.

> **Theorem 22.1 (zero-error answerability; fate of Proposition 5.6 and Theorem 6.4).** $q$ is zero-error answerable from $S$ iff $\ker(q) \le \sigma^{0}(S)$. Consequently the zero-error answerable questions form the principal ideal ${\downarrow}\,\sigma^{0}(S)$, and $\sigma^0(S)$, as a question, is the maximally informative zero-error answerable one.
>
> *Proof.* ($\Rightarrow$) Let $\alpha$ be a perfect rule. For every $Z$ and every $y \in \mathrm{supp}\,P_S(\cdot \mid Z)$, correctness with probability one over a finite support forces $\alpha(y) = q(Z)$. If $Z \approx_S Z'$, a common support point $y$ gives $q(Z) = \alpha(y) = q(Z')$. So $q$ is constant on $\approx_S$-edges, hence on connected components, i.e. $\ker(q) \le \sigma^0(S)$. ($\Leftarrow$) Suppose $q$ is constant on components. For each realized $y$ (in some support) set $\alpha(y) = q(Z_y)$ for any $Z_y$ whose support contains $y$; the value is well defined because any two such candidates are $\approx_S$-related. For arbitrary $Z$ and any $y \in \mathrm{supp}\,P_S(\cdot\mid Z)$ we get $\alpha(y) = q(Z)$, so the rule is perfect. The ideal statement follows as in Theorem 6.4. $\square$

> **Theorem 22.2 (asymptotic answerability).** $q$ is asymptotically answerable from $S$ iff $\ker(q) \le \sigma^{=}(S)$.
>
> *Proof.* ($\Leftarrow$) There are finitely many distinct likelihoods $\{\widehat R_S(Z)\}$; let $\delta > 0$ be the minimum total-variation distance between distinct ones. Let $\widehat p_n$ be the empirical distribution of the $n$ copies; define $\alpha_n$ to output $q(Z^*)$ for any $Z^*$ minimizing $\|\widehat p_n - \widehat R_S(Z^*)\|_{TV}$. Given $Z$, the law of large numbers gives $\|\widehat p_n - \widehat R_S(Z)\| \to 0$ a.s., so eventually the minimizer's likelihood equals $\widehat R_S(Z)$, i.e. $Z^* \sim_{\sigma^=} Z$; since $q$ is constant on $\sigma^=$-blocks, $\alpha_n$ is eventually correct, and finiteness of $D$ upgrades this to uniform error $\to 0$ (standard concentration, e.g. via Hoeffding on each cell). ($\Rightarrow$) If $\widehat R_S(Z) = \widehat R_S(Z')$ with $q(Z) \ne q(Z')$, then for any rule $\alpha_n$ the two error probabilities are computed under the *same* output distribution, and since $\alpha_n$ cannot equal both values at once, $\Pr(\alpha_n \ne q(Z) \mid Z) + \Pr(\alpha_n \ne q(Z') \mid Z') \ge 1$; the worst-case error is $\ge 1/2$ for every $n$. $\square$

Theorems 22.1–22.2 give the strata their meaning and show the kernel's single answerability criterion (Proposition 5.6) splits into inequivalent graded criteria with the *same lattice form*: factorization below a content partition. By contrast, $\varepsilon$-answerability at fixed $\varepsilon \in (0, \tfrac12)$ is a down-set condition on $\ker(q)$ (coarsening a question cannot increase its Bayes error: post-compose the optimal rule) but **not** a principal ideal in general — the same non-principality already met in the budget-type admissibility of §16.2, now arising intrinsically. Both instances, and a third at Definition 23.1, are lower sets that are not principal; Remark 24.6 names this property (representability) and states the limits of representing such classes by lower sets.

### 22.2 Fate of T1: the adjunction breaks twice

> **Proposition 22.3 (zero-error content is superadditive).** For finite $S, S'$ in a coherent family,
> $$
> \sigma^{0}(S \cup S') \;\ge\; \sigma^{0}(S) \vee \sigma^{0}(S'),
> $$
> and the inequality can be strict even for CI families. Hence $\sigma^0$ does not preserve joins and admits no upper adjoint; the adjunction of Theorem 6.2 fails for zero-error content.
>
> *Proof.* Inequality: if joint supports over $S \cup S'$ intersect at a point, its coordinate projections witness intersection over $S$ and over $S'$; so $\approx_{S\cup S'} \subseteq \approx_S \cap \approx_{S'}$ as edge sets, and every component of the smaller edge set is contained in a component of each larger one, hence in a block of $\sigma^0(S) \vee \sigma^0(S')$. Strictness: let $D = \{1,2,3\}$ and take CI views $v, w$ with supports
> $$
> \mathrm{supp}\,v(\cdot|1)=\{a\},\quad \mathrm{supp}\,v(\cdot|2)=\{a,b\},\quad \mathrm{supp}\,v(\cdot|3)=\{b\};
> $$
> $$
> \mathrm{supp}\,w(\cdot|1)=\{c,d\},\quad \mathrm{supp}\,w(\cdot|2)=\{c\},\quad \mathrm{supp}\,w(\cdot|3)=\{d\}
> $$
> (any strictly positive probabilities on these supports). Then $\approx_{\{v\}}$ has edges $\{12, 23\}$ and $\approx_{\{w\}}$ has edges $\{12, 13\}$; each graph is connected, so $\sigma^0(\{v\}) = \sigma^0(\{w\}) = \bot$ and the join is $\bot$. Under CI the joint support is the product of supports, so $\approx_{\{v,w\}}$ has edge set $\{12,23\} \cap \{12,13\} = \{12\}$, whence $\sigma^0(\{v,w\}) = \{\,12 \mid 3\,\} > \bot$. $\square$

Two views, each singly incapable of certifying anything with certainty, jointly certify a real distinction. This is a *noise-induced* analogue of Part II's registration anomaly: superadditivity of content arising not from a restricted decoder but from the support geometry of the channels themselves. It is the second independent mechanism producing "the whole reads more than its parts."

The mechanism can, however, be located with complete precision, and doing so shows that the zero-error stratum has a lossless invariant on which compositionality survives.

> **Proposition 22.3′ (the confusability graph is the lossless zero-error object).** Let $\mathrm{Tol}(D)$ be the set of reflexive symmetric relations (**tolerances**) on $D$ — a complete lattice under inclusion of edge sets — and order it by *reverse* inclusion, written $\sqsubseteq$ (fewer confusions $=$ more information), under which it is again a complete lattice with joins given by intersection of edge sets. Define the **graph-valued zero-error content** of finite $S$ as
> $$
> \sigma^{G}(S) \;:=\; \approx_S \;\in\; \mathrm{Tol}(D).
> $$
> Then, on CI families,
> $$
> \sigma^{G}(S) \;=\; \bigsqcup_{v \in S} \sigma^{G}(\{v\}) \qquad\big(\text{equivalently } \approx_S \,=\, \textstyle\bigcap_{v \in S} \approx_{\{v\}} \text{ as edge sets}\big),
> $$
> so $\sigma^{G}$ preserves unions as joins, and, for finite $V$ (or the arbitrary-intersection extension to all subsets), the full adjunction of Theorem 6.2 holds for graph-valued zero-error content over CI families, with generators $\sigma^{G}(\{v\})$ and upper adjoint $\tau^{G}(\theta) = \{v \in V : \sigma^{G}(\{v\}) \sqsubseteq \theta\}$ (in edge sets: every confusion $\theta$ permits is one the view permits — the views individually no more informative than $\theta$).
>
> *Proof.* Under CI, $\mathrm{supp}\, P_S(\cdot \mid Z) = \prod_{v \in S} \mathrm{supp}\, v(\cdot \mid Z)$, and products of nonempty sets intersect iff every pair of corresponding factors intersects; so $Z \approx_S Z'$ iff $Z \approx_{\{v\}} Z'$ for every $v \in S$, which is the displayed join law. The adjunction then follows exactly as in Theorem 15.1: any content map given as a join of singleton generators into a complete lattice is a left adjoint. $\square$

Proposition 22.3′ diagnoses Proposition 22.3 exactly. ("Lossless" refers to retaining the confusability relation, not the full experiment.) The partition $\sigma^{0}(S)$ is obtained from $\sigma^{G}(S)$ by passing to connected components, that is, to the transitive closure of the tolerance. In the information order this passage is a right adjoint to the inclusion of equivalence relations into tolerances — $\pi\sqsubseteq R$ iff $\pi\le\operatorname{comp}(R)$ — and right adjoints preserve meets but not, in general, joins. The superadditivity of $\sigma^{0}$ on CI families is precisely this failure: an order-theoretic fact about component formation, not a fact about channels. At the graph level, zero-error content over CI families is strictly compositional. We call the mechanism **reflection** (of tolerances onto partitions); the name is descriptive and does not refer to the orientation of the adjunction. Support geometry is its carrier, and off the CI class the joint support is no longer a product, so the law fails through coupling — consistently with the mechanism ladder below. Taking the graph as the primary invariant also aligns the stratum with the zero-error literature, where the confusability graph, not its component partition, carries the theory [Shannon 1956; Lovász 1979].

The statistical stratum sits strictly between the zero-error stratum and the full one, and its union behavior completes the picture:

> **Proposition 22.4 (statistical content: superadditivity exactly through coupling).** For finite $S, S'$ in a coherent family:
>
> 1. $\sigma^{=}(S \cup S') \;\ge\; \sigma^{=}(S) \vee \sigma^{=}(S')$;
> 2. the inequality can be strict, and the mechanism is coupling: candidates can have identical marginal likelihoods over each of $S$ and $S'$ yet distinct joint likelihoods over $S \cup S'$;
> 3. on CI families, $\sigma^{=}(S) = \bigvee_{v \in S} \sigma^{=}(\{v\})$ for every finite $S$; hence $\sigma^{=}$ preserves unions as joins, and the full adjunction of Theorem 6.2 holds for statistical content, with generators $\sigma^{=}(\{v\})$.
>
> *Proof.* 1: Equal joint likelihoods have equal marginals (projectivity), so every $\sigma^{=}(S \cup S')$-block lies inside a block of $\sigma^{=}(S)$ and of $\sigma^{=}(S')$. 2: Let $D = \{Z, Z'\}$ and let $v, w$ be binary views whose four marginal likelihoods are all uniform on $\{0,1\}$, so $\sigma^{=}(\{v\}) = \sigma^{=}(\{w\}) = \bot$; couple the noises so that under $Z$ the two outputs are equal with probability one, while under $Z'$ they are independent. Both joints have uniform marginals, so the family is projective; the joint likelihoods differ (one is supported on the diagonal), so $\sigma^{=}(\{v,w\}) = \top > \bot = \sigma^{=}(\{v\}) \vee \sigma^{=}(\{w\})$. 3: Under CI, $P_S(\cdot \mid Z) = \bigotimes_{v \in S} v(\cdot \mid Z)$, and a product distribution determines and is determined by its factors; hence $\widehat{R}_S(Z) = \widehat{R}_S(Z')$ iff $v(\cdot \mid Z) = v(\cdot \mid Z')$ for every $v \in S$, i.e. $\ker \widehat{R}_S = \bigvee_{v \in S} \ker \widehat{R}_{\{v\}}$ as in (3.1). The adjunction follows as in Theorem 6.2, the content map being again a join over singleton generators. $\square$

At the full stratum the failure is even more basic:

> **Proposition 22.5 (joint experiments and Blackwell joins).** The graded content map is monotone: marginalizing $P_S$ to $T\subseteq S$ is a garbling. Thus $P_{S\cup S'}$ is an upper bound of $P_S,P_{S'}$. It need not be their least upper bound: marginal channels do not determine their coupling, and the chosen coupling can add information. Finite binary-state experiments do have Blackwell joins; for larger state spaces joins can fail [Bertschinger & Rauh 2014]. Deterministic experiments have unique joint coupling and their join is the common-refinement partition. Appendix D.5 characterizes least members of full coupling fibers.
>
> *Proof.* Projections prove the order assertions. The equal-versus-independent binary coupling example of Proposition 22.4 gives different joint information for fixed null marginals. Deterministic marginals force a paired point mass, and Lemma 24.1 identifies its least-upper-bound property. The general existence/nonexistence distinction is the cited Blackwell lattice theorem. $\square$

The fate of T1 is thus a trichotomy across the strata, ordered by how much structure fails and why. Zero-error content is superadditive even for CI families — Proposition 22.3's example is CI — with support geometry as the carrier and reflection as the mechanism: at the graph level the CI composition law is exact, and it is the passage to components that destroys it (Proposition 22.3′). Statistical content is superadditive exactly through coupling, and on CI families recovers the full adjunction: at this stratum the kernel's compositionality is not lost but *conditional*. Full graded content loses the very lattice in which a join law could be stated, and its unions acquire an input — the coupling — that the parts do not determine. Under admissibility (Part II) the adjunction failed *contingently*, at non-separable structures; under grading it degrades *structurally*, and the responsible mechanism migrates upward: from reflection (of the confusability graph onto partitions), to coupling, to the order itself. The kernel is the locus where all three pathologies are invisible.

### 22.3 Fate of T4: minimal sufficiency

The kernel's Theorem 6.7 characterized $D/\sigma(S)$ as the terminal lossless consolidation. Grading relocates the consolidation from the state side to the evidence side — one compresses the outcome space of the experiment rather than the domain — and the terminal object becomes the minimal sufficient statistic.

> **Theorem 22.6 (graded T4).** Let $P_S$ be the joint channel of a finite $S$ and let $Y^+ \subseteq \prod_{v\in S} Y_v$ be its realized outcomes ($y \in Y^+$ iff $P_S(y \mid Z) > 0$ for some $Z$). Define on $Y^+$:
> $$
> y \equiv y' \;:\iff\; \exists\, c > 0\ \ \forall Z \in D:\ \ P_S(y \mid Z) = c\, P_S(y' \mid Z)
> $$
> (proportional likelihood profiles), and let $m : Y^+ \to Y^+/{\equiv}$ be the quotient map. Then:
>
> 1. $m$ is a sufficient statistic for $\{P_S(\cdot \mid Z)\}_Z$;
> 2. $m$ is minimal: for every sufficient statistic $T$ there is a map $f$ with $m = f \circ T$ on $Y^+$;
> 3. sufficiency is exactly losslessness: a statistic $T$ is sufficient iff $I(Z; T(Y_S)) = I(Z; Y_S)$ for every prior on $D$ (equality in the DPI);
> 4. in the deterministic case, $Y^+ = \mathrm{Im}\,\langle v \rangle_{v \in S}$, the classes of $\equiv$ are singletons, and $m$ is (up to iso) the identity on $\mathrm{Im}\,\langle v\rangle_{v\in S} \cong D/\sigma(S)$: Theorem 6.7's terminal consolidation is recovered exactly.
>
> *Proof.* 1: Fix a representative $y_0$ in each class; for $y \equiv y_0$ write $P_S(y \mid Z) = c_y P_S(y_0 \mid Z)$. Then $P_S(y \mid Z) = g(m(y), Z)\, h(y)$ with $g([y_0], Z) = P_S(y_0 \mid Z)$ and $h(y) = c_y$; sufficiency by Fact 20.1. 2: Let $T$ be sufficient with factorization $P_S(y \mid Z) = g(T(y), Z) h(y)$; for realized $y$, $h(y) > 0$. If $T(y) = T(y') = t$ with $y, y' \in Y^+$, the factorization gives $P_S(y \mid Z) = g(t, Z)\, h(y)$ and $P_S(y' \mid Z) = g(t, Z)\, h(y')$ for every $Z$ simultaneously, whence $P_S(y \mid Z) = \tfrac{h(y)}{h(y')}\, P_S(y' \mid Z)$ with $\tfrac{h(y)}{h(y')} > 0$ — no ratio of possibly-zero likelihoods is ever formed — so $y \equiv y'$ and $m(y) = m(y')$; hence $m$ factors through $T$ on $Y^+$. 3: Equality in the DPI for all priors iff the Markov chain $Z \to T(Y_S) \to Y_S$ holds in the conditional sense defining sufficiency [Cover & Thomas 2006]. 4: With point-mass likelihoods, $P_S(y \mid Z) = \mathbb{1}\{\langle v\rangle(Z) = y\}$; two distinct realized outcomes have disjoint, nonempty preimages, so their profiles are never proportional; $\equiv$ is equality, and $\mathrm{Im}\,\langle v \rangle \cong D/\sigma(S)$ is Theorem 6.7(3). $\square$

Theorem 22.6 also grades Lemma 4.7. In the kernel, sound registrations were bracketed between constants and the canonical (most informative) one; in the graded theory, *lossless* registrations of an experiment are bracketed between the identity and the minimal sufficient statistic (the coarsest lossless one, by items 2–3), and any coarsening past $m$ begins to lose content, with the DPI quantifying the loss. Registration theory thus acquires a floor with a classical name.

### 22.4 The Shannon bridge

Fix a coherent family, finite $S$, a question $q$, and a **full-support prior** $\mu$ on $D$; let $Z \sim \mu$ and $Y_S \sim P_S(\cdot \mid Z)$.

> **Theorem 22.7 (entropic criteria).**
>
> 1. $H\big(q(Z) \mid Y_S\big) = 0$ for one (equivalently, every) full-support prior iff $\ker(q) \le \sigma^{0}(S)$ — the vanishing of conditional entropy is exactly zero-error answerability.
> 2. (Fano, quantitative unanswerability.) For any rule, with $M = |A_q| \ge 2$:
> $$
> \Pr\big(\alpha(Y_S) \ne q(Z)\big) \;\ge\; \frac{H(q(Z) \mid Y_S) - 1}{\log_2 M}.
> $$
>
> 3. (Chain rule; graded T3.) $I\big(Z; Y_{S \cup \{w\}}\big) = I(Z; Y_S) + I(Z; Y_w \mid Y_S) \ge I(Z;Y_S)$, and $e_\mu(q \mid S \cup \{w\}) \le e_\mu(q \mid S)$: a further view never hurts, and its marginal value is the conditional mutual information, null iff $Y_w \perp Z \mid Y_S$.
> 4. (DPI; graded Lemma 14.2.) For any registration channel $\kappa$ applied to $Y_S$: $I(Z; \kappa(Y_S)) \le I(Z; Y_S)$ — registration cannot create information, with equality exactly at sufficiency.
>
> *Proof.* 1: $H(q(Z) \mid Y_S) = 0$ iff for every realized $y$, $q$ is constant on $\{Z : \mu(Z) P_S(y \mid Z) > 0\}$; with $\mu$ full-support these are the sets $\{Z : y \in \mathrm{supp}\, P_S(\cdot\mid Z)\}$. Constancy on all of them is equivalent to constancy on every $\approx_S$-edge (an edge is witnessed by some shared $y$; conversely each such set is pairwise $\approx_S$-connected through $y$), hence to $\ker(q) \le \sigma^0(S)$ by connectivity, as in Theorem 22.1. 2 and 4 are Fano and the DPI [Cover & Thomas 2006], the equality case in 4 being Theorem 22.6(3). 3: chain rule plus nonnegativity of conditional mutual information; the Bayes-risk inequality holds because marginalizing away $Y_w$ is a garbling, and garbling cannot lower Bayes risk (Blackwell–Sherman–Stein, §20.1). $\square$

This is the promised enrichment of the Shannon base, and its shape deserves emphasis: each qualitative kernel principle acquires a quantitative counterpart —

| kernel (exact) | graded / entropic |
|---|---|
| Prop. 5.6: answerable iff $\ker(q) \le \sigma(S)$ | Thm 22.1 / 22.7(1): zero-error iff $\ker(q)\le\sigma^0(S)$ iff $H(q \mid Y_S) = 0$ |
| Def. 5.5: unresolved pairs witness failure | Thm 22.7(2): Fano converts residual entropy into forced error |
| Thm 6.5: marginal value via separated pairs | Thm 22.7(3): marginal value $= I(Z; Y_w \mid Y_S)$; Bayes risk monotone |
| Lemma 14.2: registration non-increasing | Thm 22.7(4): DPI |
| Lemma 4.7: canonical = most informative sound registration | Thm 22.6(2–3): minimal sufficiency = coarsest lossless registration |
| Thm 6.7: terminal consolidation $D/\sigma(S)$ | Thm 22.6: minimal sufficient statistic; deterministic case recovers 6.7 |

— so mutual information enters not as a replacement for the distinction-structure account but as its prior-weighted shadow, exactly as anticipated in Part I (§8, H3). The information bottleneck [Tishby, Pereira & Bialek 1999] now also finds its place: it is the *lossy* relaxation of Theorem 22.6 — minimize retained rate subject to retaining a stipulated amount of question-relevant information — i.e., the graded form of budget-type (non-monotone) admissibility from §16.2.

---

## 23. Graded admissibility and the anatomy of synergy

### 23.1 Graded ceilings

> **Definition 23.1.** A **graded admissibility structure** $\widehat K$ on a coherent family assigns to each finite $T$ a **ceiling experiment** $\Gamma_{\widehat K}(T)$ with $\Gamma_{\widehat K}(T) \preceq_B P_T$ (K1̂), with $\Gamma_{\widehat K}(\varnothing)$ the null experiment (K0̂), the admissible readings on $T$ being exactly the garblings of $\Gamma_{\widehat K}(T)$ (K2̂: a principal Blackwell down-set). $\widehat K$ is **monotone** if $T \subseteq T' \Rightarrow \Gamma_{\widehat K}(T) \preceq_B \Gamma_{\widehat K}(T')$.

As in §16.2, (K2̂) is a genuine restriction: natural resource constraints (rate limits, output budgets) carve out Blackwell down-sets that are not principal, and here the failure is aggravated by the absence of least upper bounds in the Blackwell order [Bertschinger & Rauh 2014] — there is in general no canonical completion of a non-principal admissible class to a ceiling. Part II's repair (a definite choice of ceiling within the class) remains available and remains a modeling act.

Part II's bracketing does **not** survive in graded form unamended, and establishing what does survive requires first fixing the object being compared.

> **Definition 23.2 (separable admissible reading).** For finite $S$, a **separable admissible reading** of $S$ under $\widehat K$ is an experiment of the form
> $$
> \Big(\bigotimes_{v \in S} G_v\Big) \circ P_S,
> $$
> where each $G_v$ is a channel on $Y_v$, applied to the $v$-coordinate of the joint data, such that $G_v \circ v$ is admissible on $\{v\}$, i.e. $G_v \circ v \preceq_B \Gamma_{\widehat K}(\{v\})$. Each view is processed by its own admissible per-view decoder; no cross-view processing occurs.

> **Proposition 23.3 (accumulation: monotonicity does not bound separable readings).** There is a coherent CI family and a *monotone* graded admissibility structure satisfying (K0̂)–(K2̂) with a separable admissible reading that strictly Blackwell-dominates the joint ceiling. Hence the bracketing of Proposition 14.6 fails in the graded theory without further axioms.
>
> *Proof.* Let $D = \{0,1\}$ and let $v, w$ be conditionally independent copies of the binary symmetric channel $N$ with crossover $\varepsilon \in (0, \tfrac12)$; the joint channel is $P_{\{v,w\}} = N \otimes N$. Set $\Gamma(\{v\}) = \Gamma(\{w\}) = \Gamma(\{v,w\}) = N$. This structure is monotone (all ceilings equal) and satisfies (K0̂)–(K2̂); in particular (K1̂) holds since $N \preceq_B N \otimes N$ by marginalization. The identity processings $G_v = G_w = \mathrm{id}$ are per-view admissible ($\mathrm{id} \circ v = N \preceq_B N$), and the resulting separable reading is $N \otimes N$ itself. But $N \otimes N \succ_B N$ strictly: dominance is marginalization; non-equivalence holds because the achievable posteriors differ — under a uniform prior, one look yields posteriors in $\{\varepsilon, 1-\varepsilon\}$, while two looks also realize the posterior $\tfrac12$ (discordant outcomes) and $\varepsilon^2/(\varepsilon^2 + (1-\varepsilon)^2)$ (concordant ones) — and the concordant posterior is strictly below $\varepsilon$. Every posterior from a garbling of one look is a convex combination of its posteriors and lies in $[\varepsilon,1-\varepsilon]$. Thus no garbling of $N$ reproduces $N\otimes N$. $\square$

The mechanism deserves a name: **accumulation**. Independent noisy looks at the same candidate compound their evidence, so even *re-reading the same view* is informative. In the exact theory this is invisible because combination is idempotent — $\ker(v) \vee \ker(v) = \ker(v)$, and a second reading of a deterministic view adds nothing. The failure of the Part II argument is therefore not a missing hypothesis but a category difference between exact combination (idempotent joins in a lattice) and graded combination (non-idempotent products of channels under couplings, in an experiment order where joins need not exist in general). Wherever ceilings are meant to cap *total* extractive power, accumulation can carry separable readings past a joint ceiling that monotonicity alone leaves unguarded.

The bracket can be restored — at a price that must be stated honestly.

> **Definition 23.4 (accumulation closure).** $\widehat K$ is **accumulation-closed** — axiom **(K3̂)** — if for every finite $S$, every separable admissible reading of $S$ is a garbling of $\Gamma_{\widehat K}(S)$.

> **Proposition 23.5 (graded bracketing under (K3̂)).** If $\widehat K$ satisfies (K0̂)–(K3̂), then for every finite $S$, prior $\mu$, and question $q$,
> $$
> e_\mu\big(q \mid \text{any separable admissible reading of } S\big)
> \;\ge\;
> e_\mu\big(q \mid \Gamma_{\widehat K}(S)\big)
> \;\ge\;
> e_\mu\big(q \mid P_S\big),
> $$
> the graded form of Proposition 14.6's bracket.
>
> *Proof.* Each separable reading is a garbling of $\Gamma_{\widehat K}(S)$ by (K3̂), and $\Gamma_{\widehat K}(S)$ is a garbling of $P_S$ by (K1̂); garbling cannot lower Bayes risk (Blackwell–Sherman–Stein, §20.1). $\square$

> **Remark 23.6 (the expressive trade-off).** The constant noisy ceiling of Proposition 23.3 models a total-output cap, but independently admissible one-copy readings together exceed it. Thus that particular cap and those local reading classes cannot simultaneously satisfy (K3̂). The honest joint ceiling $\Gamma(S)=P_S$ does satisfy (K3̂), as does any realizable joint ceiling dominating the actual separable readings. This is an explicit conflict between a resource model and an accumulation axiom, not a proof that every budget model lacks a least completion. Adequacy of a proposed transfer is studied in Proposition 61.2 and Appendix D.11; full coupling fibers are governed by D.5. Down-set completion by itself supplies neither a physical coupling nor a principal achievable completion.

### 23.2 Three mechanisms under one name

Consider again the parity configuration of §16.1: $D = \{00,01,10,11\}$, coordinate views $v, w$, question $q = b_1 \oplus b_2$, now with the uniform prior. Direct computation gives
$$
I\big(q(Z); Y_v\big) = 0, \qquad I\big(q(Z); Y_w\big) = 0, \qquad I\big(q(Z); Y_v, Y_w\big) = 1 \text{ bit}:
$$
each coordinate is *independent* of parity, yet the pair determines it. In the partial information decomposition (PID) literature this is the canonical example of **synergy** — information carried only jointly [Williams & Beer 2010]. The present framework shows that at least three distinct mechanisms produce this signature, and separates them:

1. **Prior-marginalization synergy** (full admissibility, exact views, a prior): the computation above. Note the contrast with the exact theory's verdict: by Theorem 6.5, $v$ alone *does* strictly help $q$ (it separates unresolved pairs such as $(00, 10)$), while its mutual information with $q$ is exactly zero. The discrepancy is not a paradox but a difference of accounting: the kernel counts *distinctions drawn*, MI counts *question-marginal uncertainty removed on prior-average*, and a view can do much of the first while doing none of the second. PID's "synergy" begins where these two ledgers diverge.

2. **Admissibility-induced synergy** (Part II, §16.1): with the invariance ceiling, even the *distinction ledger* becomes superadditive — $\sigma^{\mathrm{sep}}_K = \bot$ while $\sigma^{\mathrm{jnt}}_K = \ker(q)$ — with no prior and no noise involved. Deterministic channels being a special case of graded ones, this mechanism persists verbatim in the graded theory.

3. **Support-geometric synergy** (Proposition 22.3): zero-error content is superadditive purely through the intersection pattern of noise supports, with full admissibility and before any prior enters.

The examples distinguish changes in prior-relative information, admissible resolving power, and support geometry. A general axiomatic decomposition connecting these mechanisms is not established by those examples. Part VII gives exact-chain evaluations and coupling-fiber excess as separate constructions, and Appendix D.4 proves how the latter changes under quotient averaging. Neither construction alone proves a PID impossibility theorem.

A closing note on §23.1's accumulation phenomenon, which stands to these three mechanisms as their reverse. Where each of (1)–(3) makes the whole read *more* than the sum of its parts, accumulation makes separable readings exceed a joint *ceiling* — an anti-synergetic divergence tied not to the joint distribution but to the multiplicity of admissible readings and the choice of ceiling. PID cannot see it even in principle: PID decomposes a *fixed* joint distribution of sources and target, so mechanisms that vary with the ceiling assignment or with how many admissible looks a decoder takes lie outside its object of study altogether. Accumulation is related to, but distinct from, PID's redundancy: redundant information is carried by each source separately *within* one fixed joint; accumulated information is created by compounding looks *across* readings that no single fixed joint represents. It is recorded here as a fourth entry in the anatomy — the one that only the admissibility-plus-grading combination exposes.

---

## 24. The zero-noise limit: recovery of the kernel

### 24.1 Recovery

> **Lemma 24.1 (deterministic Blackwell order is view refinement).** For deterministic channels $v, v'$ on $D$: $v \succeq_B v'$ iff $v' \preceq v$ in the refinement preorder of Definition 4.3, iff $\ker(v') \le \ker(v)$.
>
> *Proof.* ($\Leftarrow$) Lemma 4.4 provides a deterministic mediating map, which is in particular a channel. ($\Rightarrow$) Let $v' = G \circ v$ with $G$ a channel. For each $Z$, $\delta_{v'(Z)} = G(\cdot \mid v(Z))$, so $G(\cdot \mid v(Z))$ is the point mass at $v'(Z)$; if $v(Z) = v(Z_1)$ the two point masses coincide, so $v'(Z) = v'(Z_1)$, i.e. $\ker(v') \le \ker(v)$, and Lemma 4.4 converts this into a deterministic factorization. $\square$

> **Theorem 24.2 (recovery).** Restrict a coherent family to deterministic channels (equivalently, let all noise vanish). Then:
>
> 1. couplings are unique, so the family is determined by its single views, and Remark 21.3's indeterminacy disappears;
> 2. the Blackwell preorder restricts to the refinement preorder, on which suprema exist and are computed in $\mathrm{Part}(D)$ (Lemma 24.1, Fact 3.3);
> 3. $\sigma^{0}(S) = \sigma^{=}(S) = \sigma(S)$ (Lemma 21.7), and Theorems 22.1 and 22.2 both reduce to Proposition 5.6;
> 4. the inequalities of Propositions 22.3 and 22.4 are equalities (Theorem 6.2(1)) — deterministic couplings are unique, so every family is trivially CI and both superadditivity mechanisms vanish; the adjunction T1 holds;
> 5. the minimal sufficient statistic is the terminal consolidation $D/\sigma(S)$ (Theorem 22.6(4) = Theorem 6.7);
> 6. the entropic criteria specialize: $H(q(Z) \mid R_S(Z)) = 0$ for full-support priors iff $\ker(q) \le \sigma(S)$, and the DPI holds with equality precisely for registrations preserving $\ker$-structure, recovering Lemma 14.2's equality case.
>
> *Proof.* Each item collects the deterministic specializations established in the lemma or theorem cited within it; no new argument is required. $\square$

The exact theory of Parts I–II is thus not an idealization discarded by the graded theory but its precise zero-noise fiber — the sublocus on which couplings are canonical, the content order is a complete lattice, the three strata coincide, and every graded theorem collapses onto its kernel ancestor.

### 24.2 The structural collapse

The recovery theorem invites a reading of Parts I–III as a single object: a record of how much algebraic structure the notion of content retains as the standing assumptions are relaxed one by one. Two things degrade, and they degrade independently, so the record must track both: the **codomain** in which content lives (is it still a lattice?), and the **compositionality of the content map** over unions of view sets (does content over $S \cup S'$ still decompose as a join of the contents over the parts?). The table collects the verdicts established across the three parts.

| layer | content object | codomain | content map over unions |
|---|---|---|---|
| kernel (Part I) | $\sigma(S)$ | complete lattice $\mathrm{Part}(D)$ | preserves joins; full adjunction (Thm 6.2) |
| separable admissibility (Part II) | $\sigma^{\mathrm{sep}}_K(S)$ | complete lattice $\mathrm{Part}(D)$ | preserves joins; full adjunction (Thm 15.1) |
| joint admissibility (Part II) | $\sigma^{\mathrm{jnt}}_K(S)$ | complete lattice $\mathrm{Part}(D)$ | superadditive at non-separable $K$ (Prop. 15.2); inverted at non-monotone $K$ (§16.2); adjunction iff separable (Cor. 15.4) |
| graded, zero-error stratum | $\sigma^{0}(S)$ (partition shadow of $\sigma^{G}$) | complete lattice $\mathrm{Part}(D)$ | superadditive even on CI families (Prop. 22.3); adjunction restored at the graph level, where CI content composes exactly (Prop. 22.3′) — the loss is the reflection to partitions |
| graded, statistical stratum | $\sigma^{=}(S)$ | complete lattice $\mathrm{Part}(D)$ | superadditive exactly through coupling; joins and adjunction restored on CI families (Prop. 22.4) |
| graded, full stratum | $\widehat{\sigma}(S)$ | Blackwell preorder; binary-state lattice, joins may fail in general [Bertschinger & Rauh 2014] | ill-posed: the union's content depends on the coupling, which the parts do not determine (Prop. 22.5, Rem. 21.3) |
| graded admissibility (§23) | readings under $\widehat K$ | Blackwell preorder | separable/joint bracket only under accumulation closure (K3̂), at the cost of budget semantics (Rem. 23.6) |

The partition-valued strata keep a lattice codomain even when their content maps fail to preserve joins. The full experiment order adds a different issue: in general some joins fail to exist, and even where they exist a supplied joint experiment can be strictly above the join. These distinctions motivate separate exact and decision-theoretic comparisons; they do not make every noisy experiment a nonlattice case.

### 24.3 The content-system schema

The collapse table invites, and the accumulated results now permit, a single definition of which every content notion in Parts I–III is an instance. Let $\mathcal{F}(V)$ denote the finite subsets of $V$, a join-semilattice under union.

> **Definition 24.3 (content system).** A **content system** over $(D, V)$ is a monotone map $\mathcal{C} : \mathcal{F}(V) \to \mathsf{C}$ into a preordered **content codomain** $\mathsf{C}$, together with the **comparison cells**
> $$
> \mathcal{C}(T) \vee \mathcal{C}(T') \;\le\; \mathcal{C}(T \cup T'),
> $$
> wherever the join on the left exists — i.e. a lax morphism of join-semilattices. $\mathcal{C}$ is **strict** if all cells exist and are equalities. The non-invertible cells are the system's **anomalies**.

The manuscript's content maps are then classified by two coordinates — the codomain and the status of the cells:

| content map | codomain $\mathsf{C}$ | comparison cells |
|---|---|---|
| $\sigma$ (Part I) | $\mathrm{Part}(D)$ | strict (Theorem 6.2) |
| $\sigma^{\mathrm{sep}}_K$ | $\mathrm{Part}(D)$ | strict (Theorem 15.1) |
| $\sigma^{\mathrm{jnt}}_K$, monotone $K$ | $\mathrm{Part}(D)$ | strict iff $K$ separable (Corollary 15.4); $\Delta_K$ is the non-invertible cell |
| $\sigma^{G}$ on CI families | tolerance lattice $\mathrm{Tol}(D)^{\sqsubseteq}$ | strict (Proposition 22.3′) |
| $\sigma^{0}$ | $\mathrm{Part}(D)$ | lax even under CI, through reflection (Proposition 22.3) |
| $\sigma^{=}$ | $\mathrm{Part}(D)$ | strict on CI families; lax through coupling (Proposition 22.4) |
| $\widehat{\sigma}$ | Blackwell preorder | no general join-based cell; supplied coupling remains additional data (Proposition 22.5) |

Three facts hold at the level of the schema itself.

> **Proposition 24.4 (adjunction schema).** Let $\mathsf C$ be a complete lattice and let $\mathcal C:\mathcal P(V)\to\mathsf C$ satisfy $\mathcal C(T)=\bigvee_{v\in T}\mathcal C(\{v\})$, including $\mathcal C(\varnothing)=\bot$. Then $\mathcal C$ is left adjoint to $\tau(\pi)=\{v:\mathcal C(\{v\})\le\pi\}$. In particular this applies to a grounded singleton-generated system on finite subsets when $V$ is finite, or to its arbitrary-join extension when $V$ is infinite.
>
> *Proof.* $\mathcal C(T)\le\pi$ iff each singleton generator is below $\pi$, iff $T\subseteq\tau(\pi)$. The closure and fixed-point consequences are Fact 3.4. $\square$

> **Definition 24.5 (gluing).** Equip $\mathcal{F}(V)$ with the **positive union coverage**: a nonempty family $\{T_i\}_i$ covers $T$ iff $\bigcup_i T_i = T$. Grounding at $\varnothing$ is imposed separately. This convention is needed for the witness presheaf of §38. A content system **glues** if its comparison cells are invertible on covers: $\bigvee_i \mathcal{C}(T_i) = \mathcal{C}(T)$ whenever $\{T_i\}$ covers $T$. Separability (Definition 15.3) is exactly gluing for $\sigma^{\mathrm{jnt}}_K$; Propositions 6.3, 22.3′, and 22.4(3) are gluing statements; and the sheaf-theoretic extension H4 is, in this vocabulary, the obstruction theory of non-invertible cells, with the interval-typed anomaly (Definition 15.3) supplying composable coefficients. This covariant join equation is the definition used here; it is distinct from the contravariant Set-valued sheaf axiom. That obstruction theory is executed in Part V (Theorems 37.3, 37.5, 38.4, 39.2, 41.2, 42.1), with **descent** installed as a tracked coordinate of the architecture alongside the collapse table's two, representability (Remark 24.6), and fidelity (Part IV, §32.2).

> **Remark 24.6 (representability; down-set completion and its limits).** Three classes met so far are lower sets of an information order that are not principal: output-budget admissibility (§16.2), $\varepsilon$-answerable questions (§22.1), and resource-limited graded admissibility (§23.1). Call a content notion **representable** when it is a principal down-set — the down-set of a single element, such as a ceiling — and only **lower-set valued** otherwise. Representability is the third tracked coordinate, alongside the codomain and compositionality of the collapse table.
>
> For an information preorder $P$, let $\operatorname{Down}(P)$ be all lower sets, ordered by inclusion. Intersections and unions give a complete lattice and $p\mapsto{\downarrow}p$ is an order embedding modulo equivalence, so every such class can be *represented* as an element of $\operatorname{Down}(P)$. This representation does not repair the classes. These lower sets need not be directed ideals. A lower set represents available alternative experiments, not their assembled joint experiment. In particular ${\downarrow}a\cup{\downarrow}b$ can be strictly smaller than ${\downarrow}(a\vee b)$ even when the latter join exists.
>
> For a **specified** closure rule on lower-set assignments that is preserved by intersections, intersections of closed majorants yield a least closed assignment. This formal fact does not prove that graded accumulation closure for arbitrary supplied couplings has such a rule, that the assignment is principal, or that its generator is achievable. Those are additional obligations. The Blackwell no-join obstruction is general, with the binary-state exception of Proposition 22.5. Appendix D.5 treats unconstrained coupling minima directly.

> **Remark 24.7 (quantitative cells).** Le Cam deficiency (§25) makes experiments a generalized metric space in the sense of enriched category theory [Lawvere 1973; Le Cam 1964]. The approximate-gluing programme flagged for H4 is then the study of comparison cells that hold up to a stated deficiency — a quantitative laxity — rather than a separate theory. Section 40 develops one such measure and its limitations.

---

## 25. Summary of Part III

Noise separates three operational questions — certainty from one look, identifiability under repetition, and decision value — and the three content strata answer them (Theorems 22.1, 22.2, Definition 21.4). The kernel's adjunction survives in different forms at different strata, and its failures are located precisely: in the passage from confusability graphs to partitions, in the coupling of noises, and in the absence of joins in the Blackwell order. Minimal sufficiency replaces the terminal consolidation, and the Shannon bridge of §22.4 makes the exact criteria quantitative.

Accumulation explains why monotone local ceilings need not bound joint readings (Proposition 23.3); Appendix D.3 characterizes exactly when independent replication adds nothing. Non-principal classes can be represented by lower sets, but that representation neither preserves existing joins nor selects a physical coupling (Remark 24.6). The recovery theorem (Theorem 24.2) identifies the kernel as the deterministic part of the graded theory. Appendix A gives one extension beyond finite observation spaces and lists the hypotheses needed for others.

**References added in Part III** (see Parts I–II for those already cited):

- Bahadur, R. R. (1954). "Sufficiency and Statistical Decision Functions." *The Annals of Mathematical Statistics* 25(3), 423–462.
- Bertschinger, N., and Rauh, J. (2014). "The Blackwell Relation Defines No Lattice." *Proceedings of the IEEE International Symposium on Information Theory (ISIT 2014)*, 2479–2483.
- Bertschinger, N., Rauh, J., Olbrich, E., Jost, J., and Ay, N. (2014). "Quantifying Unique Information." *Entropy* 16(4), 2161–2183.
- Cho, K., and Jacobs, B. (2019). "Disintegration and Bayesian Inversion via String Diagrams." *Mathematical Structures in Computer Science* 29(7), 938–971.
- Fritz, T. (2020). "A Synthetic Approach to Markov Kernels, Conditional Independence and Theorems on Sufficient Statistics." *Advances in Mathematics* 370, 107239.
- Lawvere, F. W. (1973). "Metric Spaces, Generalized Logic, and Closed Categories." *Rendiconti del Seminario Matematico e Fisico di Milano* 43, 135–166.
- Le Cam, L. (1964). "Sufficiency and Approximate Sufficiency." *The Annals of Mathematical Statistics* 35(4), 1419–1455.
- Lehmann, E. L., and Scheffé, H. (1950). "Completeness, Similar Regions, and Unbiased Estimation, Part I." *Sankhyā* 10(4), 305–340.
- Lovász, L. (1979). "On the Shannon Capacity of a Graph." *IEEE Transactions on Information Theory* 25(1), 1–7.
- Shannon, C. E. (1956). "The Zero Error Capacity of a Noisy Channel." *IRE Transactions on Information Theory* 2(3), 8–19.
- Torgersen, E. (1991). *Comparison of Statistical Experiments.* Cambridge University Press.
- Vorob'ev, N. N. (1962). "Consistent Families of Measures and Their Extensions." *Theory of Probability and Its Applications* 7(2), 147–163.
- Williams, P. L., and Beer, R. D. (2010). "Nonnegative Decomposition of Multivariate Information." arXiv:1004.2515.
