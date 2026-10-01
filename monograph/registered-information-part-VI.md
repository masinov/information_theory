# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part VI: Composite Relaxations — Admissible Records and the Interaction Matrix

---

## 44. Records under admissibility

Exact presentation, context, and verdict records are ordinary views in an extended family. All-determination coherence is equivalent to monotonicity plus determination stability; nested atomic record closure alone is weaker. Mixed covers obey the existing interval calculus. Sterile record atoms are redundant only relative to retained presentations, so cover comparisons require memberwise N-completeness. In the graded setting we distinguish a fixed decoder, a fixed budget experiment, and an achievable ceiling.

---

## 45. Admissible records: the extended family and the coherence law

### 45.1 Records decompose into views

> **Definition 45.1 (record resolution; the extended family).** Let $v$ be an exact anchored view: a deterministic emission $e_v : D \to Y_v \times C_v$ with an $\eta_v$-compatible selection policy $a_v$ (Definitions 19.5–19.6 with (A2)). Its **atomic record views** are the deterministic views
> $$
> N_v = \mathrm{pr}_Y \circ e_v : D \to Y_v,
> \qquad
> \chi_v = \mathrm{pr}_C \circ e_v : D \to C_v,
> \qquad
> \tau_v = a_v \circ e_v : D \to \widehat{T}
> $$
> (presentation, context, verdict). The records of Definition 27.6 are their compounds: $S_v \cong \langle \{N_v, \tau_v\} \rangle$ and $F_v \cong \langle \{N_v, \chi_v, \tau_v\} \rangle$. The **extended family** is $\widehat{V} = V \cup \{N_v, \chi_v, \tau_v : v \text{ anchored}\}$, and all Part II and Part V structure — admissibility structures, reading classes, covers, defects — is taken over $\mathcal{F}(\widehat{V})$.

Nothing needs to be re-founded: the atomic record views satisfy (P2), the compounds are ordinary compound views, and the kernel operates on $\widehat{V}$ as it does on $V$. The first dividend is the exact record calculus.

> **Proposition 45.2 (exact record calculus; the leak anatomy).** For an exact anchored view $v$:
>
> 1. **(Exact attribution processing inequality.)** $\ker(\tau_v) \le \ker(N_v) \vee \ker(\chi_v)$, since $\tau_v$ factors through $e_v$ (Lemma 14.2); hence $\ker(F_v) = \ker(N_v) \vee \ker(\chi_v)$, and adjoining the verdict to any set containing $N_v$ and $\chi_v$ changes no $\sigma$. This is the exact shadow of Proposition 27.8: attribution is informationally free given the full raw presentation.
> 2. **(Leakage, exactly.)** $\ker(S_v) = \ker(N_v) \vee \ker(\tau_v)$, and $v$ **leaks** (under its policy) iff $\ker(\tau_v) \not\le \ker(N_v)$, iff $\ker(S_v) > \ker(N_v)$ — the exact form of Proposition 28.2's phenomenon.
> 3. **(Anatomy.)** Call a pair $Z, Z'$ **critical** if $N_v(Z) = N_v(Z')$ and $\chi_v(Z) \ne \chi_v(Z')$, and write $e_v(Z) = (y, c)$, $e_v(Z') = (y, c')$. Then exactly one of three cases holds:
>    - **(taut)** $\eta_v(y,c) = \eta_v(y,c')$ is a singleton: no compatible policy separates the pair through its verdict;
>    - **(forced)** $\eta_v(y,c) \cap \eta_v(y,c') = \varnothing$ (in particular, distinct singletons — e.g. one sound, one failed status): *every* compatible policy separates it;
>    - **(optional)** otherwise (a shared option exists, and at least one side has room): separation is policy-dependent.
>
>    Some policy leaks at $v$ iff some critical pair is forced or optional. The all-policies criterion, however, is **global over presentation fibers, not pairwise**: for a realized presentation $y$ let $C_y = \{c : (y, c) = e_v(Z) \text{ for some } Z \in D\}$; a compatible policy is leak-free iff its verdict is constant on every realized fiber, which is possible iff
>    $$
>    \bigcap_{c \in C_y} \eta_v(y, c) \;\ne\; \varnothing \qquad \text{for every realized } y.
>    $$
>    Hence **every compatible policy leaks iff some realized fiber has empty total intersection**. A forced pair — empty *pairwise* intersection — is sufficient but not necessary: on fibers with at most two realized contexts the pairwise and global criteria coincide, and on larger fibers they separate. With $C_y = \{c_1, c_2, c_3\}$ and $\eta(y, c_1) = \{t_1, t_2\}$, $\eta(y, c_2) = \{t_2, t_3\}$, $\eta(y, c_3) = \{t_1, t_3\}$, every critical pair is optional, yet the total intersection is empty, so every compatible policy separates some pair — a Helly-type failure of the pairwise reading. Forced leaks are correspondence-driven — Proposition 28.2's mechanism, where the anchoring *status* varies across the pair — optional leaks are policy-driven — Proposition 30.2's mechanism — and the fiberwise criterion exhibits a third possibility the pairwise anatomy cannot: a leak forced globally by a correspondence no two of whose values conflict. The erroneous/irreparable distinction of Definition 19.5 thereby refines to the leak.
> 4. **(Exact sterility.)** If $\ker(\chi_v) \le \ker(N_v)$ (context draws no distinctions beyond the presentation — the exact form of Definition 30.3), there are no critical pairs, hence no policy leaks: $\ker(\tau_a) \le \ker(N_v)$ for every compatible policy $a$. More exactly: every policy is leak-free at $v$ iff every critical pair is taut; sterility is the case of no critical pairs at all.
>
> *Proof.* 1 and 2 are Lemma 14.2 and Fact 3.3 applied to the stated factorizations. 3: on a critical pair, $\tau$ separates iff $a(y,c) \ne a(y,c')$; compatibility confines the two values to the two $\eta$-sets, so equality is impossible iff the sets are disjoint, forced-possible iff a common element can be chosen, and mandatory-equal iff both sets are the same singleton; a non-critical $N$-equal pair has $e_v(Z) = e_v(Z')$ and hence equal verdicts under any policy, so all leakage lives on critical pairs, and the pairwise statements follow. For the global criterion: leak-freedom is exactly verdict-constancy on every realized fiber, a constant admissible choice on the fiber of $y$ is exactly an element of $\bigcap_{c \in C_y} \eta_v(y,c)$, and any family of such elements assembles into a compatible leak-free policy (off-fiber values chosen arbitrarily within $\eta$); the displayed three-context configuration witnesses that the pairwise condition is strictly weaker. 4: with no critical pairs, $N$-equal implies $e_v$-equal implies $\tau$-equal for every policy, i.e. $\ker(\tau_a) \le \ker(N_v)$; the refinement restates 3. $\square$

### 45.2 Determination restriction and the coherence theorem

The ladder maps $F_v \twoheadrightarrow S_v \twoheadrightarrow N_v$ are not coordinate projections between view *sets*; they are surjections *within* single views. Does Proposition 14.4′'s closure notion extend to them? It does — and the correct generality is not the ladder but determination itself.

> **Definition 45.3 (determination restriction; determination-monotone structures).** Let $T', T \subseteq \widehat{V}$ be finite with $\sigma(T') \le \sigma(T)$. Then the compound $c_T$ determines $c_{T'}$: the map $m_{T',T}$ defined on realized profiles by $m_{T',T}(c_T(Z)) = c_{T'}(Z)$ is well defined (equal $T$-profiles lie in one $\sigma(T)$-block, hence in one $\sigma(T')$-block, hence have equal $T'$-profiles), extended arbitrarily off the image. The family of reading classes $\{\mathcal{K}(T)\}_{T \in \mathcal{F}(\widehat V)}$ (Proposition 14.4′) is **closed under determination restriction** if $\sigma(T') \le \sigma(T)$ and $\kappa' \in \mathcal{K}(T')$ imply $\kappa' \circ m_{T',T} \in \mathcal{K}(T)$. The structure $K$ is **determination-monotone** if $\sigma(T') \le \sigma(T) \Rightarrow \gamma_K(T') \le \gamma_K(T)$.

For $T' \subseteq T$ the map $m_{T',T}$ is the coordinate projection (up to profile identification), so determination restriction extends Proposition 14.4′'s notion; and the record ladder is the case $T' = \{N_v\}$ or $\{N_v, \tau_v\}$ against $T = \{N_v, \chi_v, \tau_v\}$ and its relatives, since $\ker(N) \le \ker(S) \le \ker(F)$ makes each ladder surjection a determination restriction between the corresponding singletons of $\widehat V$'s compounds.

> **Theorem 45.4 (the coherence law for records).** For an admissibility structure $K$ on $\mathcal{F}(\widehat{V})$, the following are equivalent:
>
> 1. $\{\mathcal{K}(T)\}$ is closed under determination restriction;
> 2. $K$ is determination-monotone;
> 3. $\gamma_K$ factors through the content map as a monotone assignment: $\gamma_K = g \circ \sigma$ for a unique monotone $g : \mathrm{Ach}(\widehat{V}) \to \mathrm{Part}(D)$;
> 4. $K$ is monotone (Definition 14.3) **and** determination-stable (Definition 35.3).
>
> *Proof.* (1)$\Leftrightarrow$(2): verbatim the proof of Proposition 14.4′ with $m_{T',T}$ in place of $\mathrm{pr}_{T'}$ — soundness of $\kappa' \circ m_{T',T}$ on $c_T$ holds because $(\kappa' \circ m_{T',T})(c_T(Z)) = \kappa'(c_{T'}(Z)) \ni Z$, its registered partition is $\ker(\kappa' \circ c_{T'}) = \rho(\kappa')$, and the two directions then read exactly as there, with Lemma 14.4 supplying the ceiling-realizing $\kappa'$ for necessity. (2)$\Rightarrow$(3): $g(\sigma(T)) := \gamma_K(T)$ is well defined on $\mathrm{Im}\,\sigma = \mathrm{Ach}(\widehat V)$ (equal $\sigma$'s give inequalities both ways) and monotone by definition of determination-monotonicity; uniqueness is surjectivity of $\sigma$ onto $\mathrm{Ach}$. (3)$\Rightarrow$(2) is immediate. (2)$\Rightarrow$(4): inclusions and $\sigma$-equalities are special determinations. (4)$\Rightarrow$(2): if $\sigma(T') \le \sigma(T)$ then $\sigma(T \cup T') = \sigma(T)$, so stability gives $\gamma_K(T \cup T') = \gamma_K(T)$ and monotonicity gives $\gamma_K(T') \le \gamma_K(T \cup T') = \gamma_K(T)$. $\square$

> **Corollary 45.5 (record coherence and repackaging).** Reading classes are closed along **all determinations** iff $K$ is determination-monotone, equivalently monotone and determination-stable. Invariance ceilings $P_G\wedge\sigma(T)$ satisfy this condition. Closure along nested sets of record atoms alone follows already from monotonicity.
>
> Let $\mathcal N$ be the set of presentation atoms $N_v$. The presentation-only structure $\gamma(T)=\sigma(T\cap\mathcal N)$ is monotone. It can fail all-determination closure when a non-presentation view $\tau$ determines a nonconstant presentation $N'$: $\ker N'\le\ker\tau$ but $\gamma(\{N'\})=\ker N'>\bot=\gamma(\{\tau\})$. Thus its possible incoherence concerns repackaging, not the nested atomic ladder. If these kernels are equal, it directly violates stability; if they are strictly ordered, monotonicity plus Theorem 45.4 implies failure of stability somewhere in the family.
>
> *Proof.* The equivalence and last inference are Theorem 45.4. Meets are monotone, giving the invariance example. Intersecting nested view sets with $\mathcal N$ preserves their inclusion, proving the presentation-only monotonicity and the stated counterexample. $\square$

Theorem 45.4 combines projection coherence with invariance under repackaging. Nested atomic record sets require only monotonicity; all determination maps require the additional stability condition. The extended family then lets the existing interval calculus address mixed feature/record covers.

---

## 46. Mixed covers: compounding and absorption

### 46.1 Conservativity and the interaction identity

> **Definition 46.1 (mixed sets; cross-layer defect).** For finite $T \subseteq \widehat{V}$ write $T_f = T \cap V$ (the feature part) and $T_r = T \setminus T_f$ (the record part), assumed both nonempty; the **layer cover** is $\mathcal{U}_{\mathrm{lay}}(T) = \{T_f, T_r\}$, and the **cross-layer defect** is
> $$
> X_K(T) \;=\; \delta_K(\mathcal{U}_{\mathrm{lay}}; T) \;=\; \big[\, \gamma_K(T_f) \vee \gamma_K(T_r),\ \gamma_K(T) \,\big].
> $$

> **Proposition 46.2 (conservativity; the interaction identity).** Let $K$ be monotone on $\mathcal{F}(\widehat V)$.
>
> 1. Mixed covers are covers in $\mathcal{F}(\widehat{V})$, so Definition 37.1, Proposition 37.2, Theorem 37.3, and Lemma 37.4 apply **verbatim**: the composite theory adds no new law, and every mixed anomaly is an ordinary anomaly of the extended family.
> 2. Refining the layer cover by singletons, Lemma 37.4 gives the factorization
> $$
> \Delta_K(T) \;=\; J_K(T) \cdot X_K(T),
> \qquad
> J_K(T) = \big[\, \sigma^{\mathrm{sep}}_K(T_f) \vee \sigma^{\mathrm{sep}}_K(T_r),\ \gamma_K(T_f) \vee \gamma_K(T_r) \,\big],
> $$
> with $J_K(T)$ the **join of the pure-layer anomalies** (degenerate whenever both $\Delta_K(T_f)$ and $\Delta_K(T_r)$ are; the converse fails, by absorption) and $X_K(T)$ the genuinely cross-layer part. The two factors are independent coordinates of the total defect: §46.2 realizes every combination.
>
> *Proof.* 1 is Definition 45.1 — nothing in §37 used anything about $V$ beyond its being a view family. 2: the singleton cover of $T$ is the composite of $\mathcal{U}_{\mathrm{lay}}$ with the singleton covers of $T_f$ and $T_r$; Lemma 37.4 computes the left endpoint as $\sigma^{\mathrm{sep}}_K(T_f) \vee \sigma^{\mathrm{sep}}_K(T_r) = \sigma^{\mathrm{sep}}_K(T)$, and the concatenation is the interval identity $[a,b] = [a,m]\cdot[m,b]$ at $m = \gamma_K(T_f) \vee \gamma_K(T_r)$, which lies between the endpoints by Proposition 14.6 applied layerwise and monotonicity. Degeneracy of $J$ from degeneracy of both pure anomalies is the join of two equalities. $\square$

### 46.2 Both interaction modes, on one configuration

> **Theorem 46.3 (compounding and absorption).** There is a four-element contrast domain, an invariance structure, one feature view, and one exact anchored view such that:
>
> 1. **(Compounding: the leak completes the share.)** Under the context-reading policy $a$, the mixed pair $T = \{v, \tau_a\}$ has both pure-layer anomalies degenerate and cross-layer defect **maximal**, $X_{K_G}(T) = [\bot, P_G]$; under the loyal policy $\ell$, the same pair has $X_{K_G}(\{v, \tau_\ell\})$ degenerate. The cross-layer anomaly is **policy-created**: the loyalty anomaly of Proposition 30.2 and the witness anomaly of §16.1 compound, the erring policy's verdict acting as the missing share of the parity scheme.
> 2. **(Absorption.)** On $T = \{v, w, \tau_a\}$, the layer cover $\{\{v,w\}, \{\tau_a\}\}$ has degenerate defect while its feature stage carries the maximal anomaly $\Delta_{K_G}(\{v,w\}) = [\bot, P_G]$: the feature anomaly is absorbed at the layer cover. Symmetrically, the mixed cover $\{\{v, \tau_a\}, \{w\}\}$ is degenerate while its mixed member internally carries $[\bot, P_G]$.
>
> Hence, asked whether the registration anomaly and the loyalty anomaly compound or absorb each other, the answer is: **both** — the registration anomaly and the loyalty anomaly can compound, and either can absorb the other, and which occurs is a property of the cover and the policy, not of the layers. Moreover the compound instance is itself a witness anomaly of the extended family ($v$ and $\tau_a$ are relabeled parity shares; the witness nerve of the relevant orbit pair is $\partial\Delta^1$), confirming Proposition 46.2's conservativity: composition creates new *instances* across layers, never a new *kind*.
>
> *Proof.* Take §16.1's configuration: $D = \{00, 01, 10, 11\}$, $G$ the global flip with orbit partition $P_G$ (the parity partition), invariance structure $K_G$, feature view $v =$ first bit, and (for item 2) $w =$ second bit; recall $\gamma_G(\{v\}) = P_G \wedge \ker(v) = \bot = \gamma_G(\{w\})$ and $\gamma_G(\{v,w\}) = P_G$. The anchored view $u$ is tracked-target ($o \equiv t^*$) with a distractor $d$: $Y_u = \{y_0\}$ (so $N_u$ is constant), $C_u = \{0,1\}$ with $e_u(Z) = (y_0, b_2(Z))$, and $\eta(y_0, 0) = \eta(y_0, 1) = \{t^*, d\}$ — every status ambiguous, every critical pair optional (Proposition 45.2(3)). The loyal policy has $\tau_\ell \equiv t^*$, $\ker(\tau_\ell) = \bot$, $\varepsilon_\ell \equiv 0$; the context-reading policy $a$ (select $t^*$ on $c = 0$, $d$ on $c = 1$) has $\ker(\tau_a) = \ker(w)$ and errs with certainty on every candidate with $b_2 = 1$ — the exact skeleton of Proposition 30.2.
> 1: For $T = \{v, \tau_a\}$ the pure-layer anomalies are anomalies of singletons, hence degenerate. The defect: $\gamma_G(\{\tau_a\}) = P_G \wedge \ker(w) = \bot$, and $\gamma_G(T) = P_G \wedge (\ker(v) \vee \ker(w)) = P_G \wedge \top = P_G$; so $X = [\bot \vee \bot, P_G] = [\bot, P_G]$, and the invariant question $q_G$ (kernel $P_G$) is answerable under the ceiling from the pair jointly and from neither member — a witness anomaly with shares $v, \tau_a$, nerve $\partial\Delta^1$ exactly as for $\{v, w\}$ in Theorem 37.7's parity computation. Under $\ell$: $\gamma_G(\{v, \tau_\ell\}) = P_G \wedge (\ker(v) \vee \bot) = \bot$, so $X = [\bot, \bot]$.
> 2: $\gamma_G(\{v,w,\tau_a\}) = P_G \wedge \top = P_G$; the layer cover's left endpoint is $\gamma_G(\{v,w\}) \vee \gamma_G(\{\tau_a\}) = P_G \vee \bot = P_G$: degenerate, with the feature stage anomaly $[\bot, P_G]$ intact one level down — Lemma 37.4's absorption, now across layers. The mixed cover $\{\{v,\tau_a\},\{w\}\}$ has left endpoint $P_G \vee \bot = P_G$: degenerate, with its mixed member's internal defect maximal by item 1. $\square$

The theorem's moral is worth separating from its arithmetic. In Part IV the loyalty anomaly was an *informativeness* statement: an erring policy's record can Blackwell-dominate a faultless one's. Under admissibility it becomes an *interaction* statement: the policy is a dial that creates and destroys cross-layer obstruction classes, because the verdict view's kernel is the one datum in $\widehat{V}$ that the interpreter's own choices set. Anchoring is thereby the layer at which the obstruction theory acquires a *control* parameter — Part V computed classes of given configurations; Part VI's configurations contain a choice, and Theorem 46.3(1) is the statement that the choice reaches the classes.

> **Proposition 46.4 (sterile records reduce to their presentation shadow).** Call $T$ **$N$-complete** when it contains the presentation of each anchored record atom it contains. Suppose every relevant anchored view is exactly sterile and $K$ is determination-monotone. Delete context and verdict atoms to obtain $\bar T$. Then $\sigma(T)=\sigma(\bar T)$ and $\gamma_K(T)=\gamma_K(\bar T)$. For a cover all of whose members are $N$-complete, its defect equals that of its presentation-shadow cover. A zero cross-layer interval additionally requires the shadow cover to glue.
>
> *Proof.* Sterility gives $\ker\chi_v\le\ker N_v$ and $\ker\tau_v\le\ker N_v$. Each deleted atom is therefore redundant in an $N$-complete set. Determination stability gives ceiling equality. Apply this to the union and to each cover member to preserve both interval endpoints. Their equality to each other is precisely shadow gluing, not a consequence of sterility alone. $\square$

Proposition 46.4 gives a presentation-shadow reduction for N-complete sets and memberwise N-complete covers. It does not assert that arbitrary layer-grouping defects vanish. Compounding and absorption remain possible wherever the corresponding shadow or nonsterile configuration has a defect.

---

## 47. The graded corner I: fixed-decoder robustness

The remaining sections compose all three relaxations, in the half where composition is tame. Throughout, admissibility constrains readings of the **perceived** data (a modelling choice: admissibility constrains what the interpreter can do with the data it actually receives), and patterns are as in Definition 29.1.

> **Proposition 47.1 (fixed-decoder statistical invariance).** For candidate-blind contamination with common rate $\varepsilon<1$ and a fixed decoder $g$,
> $$g\widetilde v=(1-\varepsilon)gv+\varepsilon gQ,$$
> and $\sigma^=(g\widetilde v)=\sigma^=(gv)$. This holds simultaneously for a fixed collection of decoders. It does not assert invariance of a decoder class defined by $g\widetilde v\preceq_B\Gamma$, since that condition can change with the channel.
>
> *Proof.* Linearity gives the identity, and the affine map has positive coefficient on $gv$, so two candidate rows are equal after processing iff they were equal before contamination. For the boundary, take a clean identity view, contaminate it to a nontrivial BSC, and use that BSC as budget. Identity decoding fits the corrupted budget but not the clean one. $\square$

> **Definition 47.2 (equalizing readings).** Let a pattern have common rate $\varepsilon(Z) \equiv \varepsilon \in (0,1)$ and candidate-dependent clutter $(Q_Z)$. A reading $g$ **equalizes** the clutter if $g \circ Q_Z = g \circ Q_{Z'}$ for all $Z, Z'$ — the clutter's candidate-dependence lies in distinctions $g$ does not draw.

> **Theorem 47.3 (equalization is sufficient for blind-contamination behavior).** Fix a family of decoders and candidate-dependent clutter $Q_Z$ at a common rate $0<\varepsilon<1$. If each decoder $g$ equalizes the clutter, put $r_g=gQ_Z$, independent of $Z$. Then
> $$g\widetilde v_Z=(1-\varepsilon)gv_Z+\varepsilon r_g.$$
> Each decoded experiment is therefore a blind garbling of its clean counterpart, preserves its equal-law partition, and has both deficiencies to that counterpart at most $\varepsilon$. For fixed $g,Q$ it is Blackwell-decreasing with the rate. These are sufficient robustness conclusions; they do not characterize all robust models or guarantee invariance of a moving output-budget class.
>
> *Proof.* The identity is linearity. Replace the decoded output by an independent draw from $r_g$ with probability $\varepsilon$ to obtain the garbling. Injectivity of the affine row map gives equality-partition preservation; coupling on the uncorrupted event gives TV and both deficiency bounds. Additional blind replacement produces every higher rate below one. $\square$

> **Proposition 47.4 (distributional immunity is null).** Fix a nonempty clutter class $\mathcal{Q}$ and suppose $g \circ \tilde v = g \circ v$ for **all** patterns with clutter drawn from $\mathcal{Q}$ and all rate profiles $\varepsilon : D \to [0,1]$. Then $g \circ Q = g \circ v(\cdot \mid Z)$ for every $Q \in \mathcal{Q}$ and every $Z$; hence $g \circ v$ is constant in $Z$ and $g$ carries no content at any stratum.
>
> *Proof.* Take the rate spike $\varepsilon = \mathbb{1}_{\{Z\}}$: then $g \circ \tilde v(\cdot \mid Z) = g \circ Q$, and immunity forces $g \circ Q = g \circ v(\cdot \mid Z)$; ranging over $Z$ with $Q$ fixed makes $g \circ v$ constant. $\square$

Theorem 47.3 supplies a sufficient fixed-decoder robustness mechanism by equalizing clutter. Proposition 47.4 addresses the stronger demand of distributional immunity against every rate profile and every clutter in the declared nonempty class; that demand forces a null decoded experiment. These are distinct quantified statements, not a general equivalence between robustness and invariance.

---

## 48. The graded corner II: accumulation and extremality under ceilings

> **Proposition 48.1 (product preprocessing preserves the budget bracket).** Let $\widehat{K}$ satisfy (K0̂)–(K3̂) on a coherent family, and corrupt each view $v \in S$ independently by a candidate-blind pattern $(\varepsilon_v, Q_v)$ — a jointly candidate-blind product pattern (Definition 29.7). Judge admissibility of readings of the perceived family by the **same** ceilings $\Gamma_{\widehat K}$. Then every separable admissible reading of the perceived family is a garbling of $\Gamma_{\widehat K}(S)$: the upper bracket holds for the unchanged budget experiments. To call these budgets achievable ceilings of the perceived family, one must additionally verify (K1̂), $\Gamma(T)\preceq_B\widetilde P_T$.
>
> *Proof.* Write $M_v$ for the contamination garbling of Theorem 29.3(1), so $\widetilde{P}_S = (\bigotimes_v M_v) \circ P_S$ by joint blindness of the product pattern. A separable admissible reading of the perceived family is $(\bigotimes_v G_v) \circ \widetilde{P}_S = (\bigotimes_v (G_v \circ M_v)) \circ P_S$ — a separable reading of the *honest* family with per-view processings $G_v \circ M_v$. Its per-view admissibility holds because $(G_v \circ M_v) \circ v = G_v \circ \tilde v$ is admissible by hypothesis; (K3̂) on the honest family then bounds the whole reading by $\Gamma_{\widehat K}(S)$. $\square$
>
> Product preprocessing is sufficient, not necessary. Appendix D.6 extends this argument to candidate-independent mixtures whose branchwise composite decoders are admissible. Joint blindness alone does not supply those branchwise bounds.

> **Proposition 48.2 (extremality survives principal ceilings).** In the setting of Theorem 30.4 (tracked target, sterile context, clean scene), let admissibility on record readings be of ceiling type: a reading $g$ of a record $R$ is admissible iff its output experiment satisfies $g \circ R \preceq_B \Gamma$ for a fixed ceiling experiment $\Gamma$ (the (K2̂) form). Then for every compatible policy $A$, the admissible achievable set of $A$'s accepted record is contained in that of the loyal record:
> $$
> \{\, g \circ \tilde v_A \;:\; g \text{ admissible} \,\} \;\subseteq\; \{\, h \circ \tilde v_\ell \;:\; h \text{ admissible} \,\},
> $$
> so loyalty remains extremal under **every** principal graded ceiling. Inversion of the comparison requires admissible classes that are not determined by their output experiments — for example classes that fix the format of the reading as well as its output experiment, the graded analogue of §16.2's inversion. Admissibility criteria given by a lower set of experiments (Remark 24.6) are output-determined, so the proposition covers them as well.
>
> *Proof.* Theorem 30.4 gives $\tilde v_A = G_A \circ \tilde v_\ell$; for admissible $g$ put $h = g \circ G_A$, whose output experiment $h \circ \tilde v_\ell = g \circ \tilde v_A$ is the same, hence admissible under any output-determined criterion. $\square$

The graded comparisons use different hypotheses: fixed-decoder invariance in Proposition 47.1, product or branchwise-admissible preprocessing in Proposition 48.1 and Appendix D.6, and sterile-context output-determined admissibility in Proposition 48.2. Theorem 41.2 concerns equal-law partitions under jointly blind replacement. None of these statements implies that arbitrary corruption preserves every ceiling or every record comparison.

---

## 49. Worked example H: calibration, linkage, and the completed share

The configuration of Theorem 46.3, with measurement semantics. Two binary assays are run on each sample; a calibration ambiguity — the global flip $G$ — makes only their *agreement* meaningful, so the meaningfulness ceiling is the invariance structure $K_G$, and the meaningful question is $q_G$ with kernel $P_G$ (§16.1's measurement reading, Part II).

Assay A is registered as the feature view $v$. Assay B's value is never registered as a feature: it survives only as the *context* of a linkage step — the record is attributed to the tracked batch $t^*$ or to a distractor batch $d$, with both attributions admissible in every context (all statuses ambiguous; every critical pair optional, Proposition 45.2(3)).

The loyal linkage attributes everything to $t^*$: zero anchoring error, constant verdict, and the meaningful question is unanswerable from anything in the file — $\gamma_G(\{v, \tau_\ell\}) = \bot$. The context-reading linkage errs on half the candidates with certainty, and its verdict is worth a share: $\gamma_G(\{v, \tau_a\}) = P_G$, with cross-layer defect $[\bot, P_G]$ — the agreement of the assays, the only meaningful content in the problem, is recoverable exactly from *assay A plus the pattern of linkage decisions*, and from nothing less (Theorem 46.3(1)). An auditor who reads only features and discards verdicts operates the presentation-only structure of Corollary 45.5: the leak is closed by fiat at the cost of the entire interval, and the auditor's reading discipline is provably incoherent across the record ladder (not determination-stable). Adding assay B as a feature view restores comfort and exhibits absorption: over $\{v, w, \tau_a\}$ the layer cover glues, the verdict is redundant, and the famous anomaly of $\{v,w\}$ survives untouched one level down (Theorem 46.3(2)). In the graded regime, blind transcription noise on the assays changes none of the admissible statistical content (Proposition 47.1); noise whose direction depends on the batch is neutralized exactly if the calibration-invariant readings cannot see its variation (Theorem 47.3); and a laboratory that demands readings *distributionally* immune to arbitrary contamination has, by Proposition 47.4, demanded readings that measure nothing.

---

## 50. Recovery, the interaction matrix, and the discharged cell

### 50.1 Recovery

> **Theorem 50.1 (recovery with explicit record scope).** Under sound unique anchoring the verdict is forced and anchoring error is zero on realized inputs. Always $F\simeq_B E$ and $N\preceq_B S\preceq_B F$. In the tracked-target reading $S\simeq_B N$; equality with the evidence record additionally follows from sterile context. Under deterministic full admissibility, every registration and mixed-cover interval is degenerate, whether or not the context is sterile.
>
> *Proof.* The record statements are Theorem 32.1. Full admissibility gives $\gamma(T)=\sigma(T)$ and joins of view kernels preserve unions, so every cover glues, including mixed covers. This interval collapse does not imply that the presentation determines all other records. $\square$

### 50.2 The interaction matrix

The three relaxations now have all their pairwise interactions on record; the matrix collects the verdicts, with the diagonal the pure theories.

| | registration (A3) | determinism (A2) | anchoring (A4′) |
|---|---|---|---|
| **registration (A3)** | Part II: $\Delta_K$; separability $=$ gluing; Part V §37: universal defect, vanishing theorem, orbit formula, reflection $\cdot$ witness | §23: accumulation refutes the bracket; (K3̂) restores it at the price of budget semantics; budget classes are representable only as non-principal lower sets (Rem. 24.6) | **Part VI**: conservative calculus (Prop. 46.2); coherence $\iff$ determination-monotone $=$ monotone $+$ stable (Thm. 45.4); compounding *and* absorption, policy-created classes (Thm. 46.3); memberwise N-complete sterile-shadow reduction (Prop. 46.4) |
| **determinism (A2)** | — | Part III: strata; coupling fiber; Part V §39: Vorob'ev descent, contextual evidence / underdetermination | Part IV: fidelity trichotomy; Part V §§40–41: blind $=$ neutral endomorphism, $2\varepsilon$-stable enriched cells; marginal blindness creates; targeted severs |
| **anchoring (A4′)** | — | — | Part IV: leak anatomy now exact (Prop. 45.2(3)): forced (correspondence) vs. optional (policy) |

Part VIII supplies explicit joint- and marginal-blind transfer failures and computes the policy-bit examples under their distinct corruption models. Least-transfer existence is treated as an order problem, not inferred from an antichain. Appendix D.11 gives finite certificates for adequacy of a fixed transfer against a polyhedral attack class.

Reading the matrix against the tracked coordinates: codomain and compositionality (§24), representability (Remark 24.6), fidelity (§32.2), and descent (Part V §42.2) all remain in force over $\widehat{V}$ without modification, and Part VI adds no sixth coordinate — its finding is that the composite theory needs none. The interactions are governed by the coordinates already installed, plus one new *lever*: the policy, the single datum of the architecture set by the interpreter, whose reach into the obstruction classes is Theorem 46.3(1).

### 50.3 Summary of the composite results

The exact record-reading result is all-determination closure iff determination monotonicity. The graded results are fixed-decoder statistical invariance and sufficient budget-bracketing constructions; they are not an extension of that exact equivalence to every graded record class. Mixed exact defects are computed by the same interval calculus, with sterility reducing memberwise N-complete covers to their shadows.

---

## 51. Established results and scope

The exact part proves record coherence and examples of compounding and absorption. Fixed-decoder statistical invariance and clutter equalization give sufficient corruption-robustness results. Product preprocessing preserves the budget bracket; branchwise admissible mixtures extend this in Appendix D.6. Neither result automatically makes the old budgets achievable from corrupted data. Loyalty extremality is preserved by output-determined admissibility under the sterile-context hypotheses.

**References added in Part VI:** none. Like Part V, the part is built entirely from sources already cited — Huber, the measurement-theoretic literature, Fellegi–Sunter, and the manuscript's own results — which certifies that the interaction theory, too, was latent in the assembled material.
