# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part V: Descent and Obstruction

---

## 34. Three local-to-global problems

Work with finite view families, or with their finitely achievable content and explicitly stated extensions. The base for witness sheaves is the positive subset site: covering families are nonempty unions. Content gluing is a covariant join equation. Witness sets instead use inclusion restrictions retaining a candidate pair, while distributional data restrict by marginalization. These objects have distinct gluing questions. Orbit graphs compute exact admissibility intervals; their witness edges and component partitions must be distinguished.

---

## 35. The base: covering systems and the comparison theorem

Descent needs a base. Two candidates were promised: Part I (§8, H4) designated the view-refinement preorder $(V, \preceq)$ as "the future base site," with coverings by families that jointly determine a view; Definition 24.5 equipped $\mathcal{F}(V)$, the finite subsets of $V$, with the union coverage. This section shows the two are compatible in a precise and instructive way, and fixes the primary base.

> **Definition 35.1 (covering systems on $\mathcal{F}(V)$).** A **covering system** on $\mathcal{F}(V)$ assigns to each finite $T$ a collection of **covers**: families of subsets of $T$. Two systems are used below:
>
> - the **union system**: a nonempty family $\{T_i\}_i$ covers $T$ iff $\bigcup_i T_i = T$ (Definition 24.5);
> - the **determination system**: a nonempty family $\{T_i\}_i$ with $T_i \subseteq T$ covers $T$ iff $\bigvee_i \sigma(T_i) = \sigma(T)$ — the parts jointly determine the compound view (the $\mathcal{F}(V)$-form of the coverage promised at P3).
>
> A content system $\mathcal{C}$ (Definition 24.3) **glues** for a covering system if $\bigvee_i \mathcal{C}(T_i) = \mathcal{C}(T)$ on every cover, whenever the join exists.

Every union cover is a determination cover, since $\bigvee_i \sigma(T_i) = \sigma(\bigcup_i T_i)$ by Theorem 6.2(1); the determination system also contains covers that do not union to $T$, e.g. $\{T'\}$ for any $T' \subseteq T$ with $\sigma(T') = \sigma(T)$ (a redundant view removed). Determination-gluing is therefore the stronger condition. The two systems also differ in kind:

> **Lemma 35.2 (only the union system is a coverage).** The union system is stable under pullback: if $\{T_i\}$ covers $T$ and $T' \subseteq T$, then $\{T_i \cap T'\}$ covers $T'$ (because $\mathcal{F}(V)$ is a distributive lattice: $(\bigcup T_i) \cap T' = \bigcup (T_i \cap T')$), so it is a Grothendieck coverage in the strict sense. The determination system is not: with $T = \{v, w\}$, $\ker(w) \le \ker(v)$, the family $\{\{v\}\}$ covers $T$, but its pullback along $\{w\} \subseteq T$ is $\{\varnothing\}$, and $\sigma(\varnothing) = \bot \ne \sigma(\{w\})$ in general. $\square$

Gluing conditions are well posed for any covering system, so nothing below depends on the Grothendieck axioms; but Lemma 35.2 is the technical reason $\mathcal{F}(V)$ with unions is the primary base, and the comparison theorem is what makes the choice harmless.

> **Definition 35.3 (determination stability).** A content system $\mathcal{C}$ is **determination-stable** if for all finite $T' \subseteq T$ with $\sigma(T') = \sigma(T)$: $\mathcal{C}(T') = \mathcal{C}(T)$ — removing redundant views does not change content.

> **Proposition 35.4 (stability is factorization through $\sigma$).** For finite $V$, with preorder values taken modulo equivalence, a content system $\mathcal{C}$ is determination-stable iff it factors through the content map: $\mathcal{C} = \widetilde{\mathcal{C}} \circ \sigma$ for a (unique, monotone) $\widetilde{\mathcal{C}} : \mathrm{Ach}(V) \to \mathsf{C}$.
>
> *Proof.* ($\Leftarrow$) immediate. ($\Rightarrow$) First, stability extends from nested to arbitrary pairs: if $\sigma(T) = \sigma(T'')$, then $\sigma(T \cup T'') = \sigma(T) \vee \sigma(T'') = \sigma(T)$, and stability applied to $T \subseteq T \cup T''$ and $T'' \subseteq T \cup T''$ gives $\mathcal{C}(T) = \mathcal{C}(T \cup T'') = \mathcal{C}(T'')$. So $\widetilde{\mathcal{C}}(\sigma(T)) := \mathcal{C}(T)$ is well defined on $\mathrm{Im}\,\sigma = \mathrm{Ach}(V)$. Monotonicity: if $\sigma(T) \le \sigma(T'')$ then $\sigma(T \cup T'') = \sigma(T'')$, so $\mathcal{C}(T) \le \mathcal{C}(T \cup T'') = \mathcal{C}(T'')$ by monotonicity of $\mathcal{C}$ and stability. $\square$

> **Theorem 35.5 (comparison).** For a content system $\mathcal{C}$ valued in a complete lattice, the following are equivalent:
>
> 1. $\mathcal{C}$ glues for the determination system;
> 2. $\mathcal{C}$ glues for the union system **and** is determination-stable.
>
> *Proof.* (1)$\Rightarrow$(2): union covers are determination covers; and for $T' \subseteq T$ with $\sigma(T') = \sigma(T)$, the singleton family $\{T'\}$ is a determination cover of $T$, whose gluing reads $\mathcal{C}(T') = \mathcal{C}(T)$. (2)$\Rightarrow$(1): let $\{T_i\}$ be a determination cover of $T$ and put $T^* = \bigcup_i T_i \subseteq T$. Then $\sigma(T^*) = \bigvee_i \sigma(T_i) = \sigma(T)$, so union-gluing on the cover $\{T_i\}$ of $T^*$ gives $\bigvee_i \mathcal{C}(T_i) = \mathcal{C}(T^*)$, and stability gives $\mathcal{C}(T^*) = \mathcal{C}(T)$. $\square$

> **Corollary 35.6 (descent of the gluing equation).** For a determination-stable content system on finite $V$, gluing for determination covers is equivalent to the equations $\widetilde{\mathcal C}(\pi)=\bigvee_i\widetilde{\mathcal C}(\pi_i)$ for nonempty families with $\pi_i\le\pi$ and $\bigvee_i\pi_i=\pi$ in $\mathrm{Ach}(V)$. These families form a pullback-stable coverage exactly when this finite lattice is distributive (Appendix D.8).
>
> *Proof.* Choose finite view sets realizing each $\pi_i$ and $\pi$. Their union with the latter realizes $\pi$ and is determination-covered by the former. Factorization through $\sigma$ identifies the gluing equation. Conversely every determination cover yields just such an equation. The site criterion is proved independently in D.8; gluing equations themselves require no site. $\square$

Stability is a genuine dividing line among admissibility structures, not a formality. Invariance ceilings $\gamma_G(T) = P_G \wedge \sigma(T)$ (§16.1) visibly factor through $\sigma$ and are stable, so the anomalies of §§37–38 live on both bases; the budget structure of §16.2, whose compound ceiling was a *choice*, is not stable in general. Operationally, stability says the decoder's constraint is a constraint on *distinctions*, not on the packaging of the raw material — an invariance is stable, an interface-format restriction typically is not.

Throughout the rest of Part V, "cover" without qualification means a union cover.

---

## 36. Three levels of descent data

The base carries three assignments that the manuscript has been working with, at different moments, without separating them. Fix a monotone admissibility structure $K$ (for the graded level, a coherent family).

**The reading level.** $T \mapsto \mathcal{K}(T)$, the admissible registrations of the compound view (Proposition 14.4′). This is the manuscript's native object: Proposition 6.3 is its trivial gluing law, §16.1 its first violation, and Proposition 14.4′ its cross-$T$ coherence.

**The content level.** $T \mapsto \mathcal{C}(T)$, a content system (Definition 24.3): $\sigma^{\mathrm{jnt}}_K$, the strata, the schema. This is the *shadow* of the reading level: by Lemma 14.4, $\gamma_K(T)$ is exactly the top of the resolving powers realized in $\mathcal{K}(T)$.

**The distribution level.** $T \mapsto \mathcal{P}(T)$, the joint channels over $T$, with **restriction given by marginalization**. Unlike the first two levels this is a genuinely contravariant assignment with non-injective restrictions — a presheaf in the strict sense — and it is where Part III's coupling phenomena live (§39).

Two structural remarks organize everything that follows.

> **Remark 36.1 (chirality).** Reading and content data are covariant with information — more views, more readings, more content — and their descent conditions are *join-shaped*: do the local contributions exhaust the global object? This is cosheaf chirality, and it is the chirality of every anomaly in Parts I–II. Distribution data is contravariant — more views, a bigger joint that *restricts* to the parts — and its descent condition is *limit-shaped*: do compatible local sections extend? This is sheaf chirality, the chirality of the marginal problem and of the contextuality literature [Abramsky & Brandenburger 2011]. The manuscript's obstruction theory therefore has two ends, and §38 exhibits the exact point where they meet: the witness presheaf, a sheaf-chirality object whose global-section emptiness is a cosheaf-chirality anomaly.

> **Remark 36.2 (what "gluing" means per level).** At the content level, gluing is Definition 24.5. At the distribution level, gluing is amalgamation of matching families (§39). At the reading level, the right notion is fixed by the next proposition — and it is *not* existence of a glued reading, which always holds.

> **Proposition 36.3 (the reading-level formulation of the anomaly).** Let $K$ be monotone and $T$ finite. Then:
>
> 1. **(Gluing always succeeds.)** For any per-view admissible readings $\kappa_v \in \mathcal{K}(\{v\})$, $v \in T$, the combination $\kappa(y) = \prod_{v \in T} \kappa_v(y_v)$ is sound on $c_T$ with $\rho(\kappa) \le \bigvee_{v} \rho(\kappa_v) \le \sigma^{\mathrm{sep}}_K(T) \le \gamma_K(T)$; hence $\kappa \in \mathcal{K}(T)$: locally admissible readings always combine admissibly.
> 2. **(Combinations are cofinal below $\sigma^{\mathrm{sep}}_K$.)** The registered partitions of readings dominated by combinations are exactly ${\downarrow}\,\sigma^{\mathrm{sep}}_K(T)$: the bound in 1 is attained by combining the ceiling-realizing readings of Lemma 14.4, whose combination has $\kappa(c_T(Z)) = \bigcap_v [Z]_{\gamma_K(\{v\})} = [Z]_{\sigma^{\mathrm{sep}}_K(T)}$.
> 3. **(The anomaly is a cofinality defect.)** $\mathcal{K}(T)$ realizes ${\downarrow}\,\gamma_K(T)$ (Lemma 14.4), so $\Delta_K(T) = [\sigma^{\mathrm{sep}}_K(T), \gamma_K(T)]$ is exactly the gap between the combined class and the joint class: it is degenerate iff every joint admissible reading is dominated in resolving power by a combination of per-view admissible readings.
>
> *Proof.* 1: Soundness: each factor contains $Z$, so the intersection does. The registered partition: equality of all factors implies equality of the intersection, so $\rho(\kappa) \le \bigvee_v \rho(\kappa_v)$; the remaining inequalities are Definition 14.5 and Proposition 14.6. 2: Blocks of a join are intersections of blocks (Fact 3.3), giving the displayed identity, hence $\rho(\kappa) = \sigma^{\mathrm{sep}}_K(T)$ for that combination; domination then sweeps out the down-set. 3: Immediate from 2 and Lemma 14.4. $\square$

Proposition 36.3 fixes the shape of the exact obstruction theory. The failure mode is not the non-existence of a glued object — the cosheaf-chirality glue always exists — but the failure of glued objects to be *cofinal*: joint readings exist that no assembly of local readings dominates. The defect is an interval, and intervals are what §37 computes with. It also settles the division of labor announced in the plan of §34: the reading level is primary, the content level is its faithful shadow (the interval endpoints are exactly the class tops), and the distribution level is the graded fiber over both.

---

## 37. The exact obstruction calculus

Throughout this section $K$ is a monotone admissibility structure and all view sets are finite.

### 37.1 Cover defects and the vanishing theorem

> **Definition 37.1 (cover defect).** For a cover $\mathcal{U} = \{T_i\}$ of $T$, the **defect** of $\mathcal{U}$ is the interval
> $$
> \delta_K(\mathcal{U}; T) \;=\; \Big[\, \bigvee_i \gamma_K(T_i),\; \gamma_K(T) \,\Big] \;\subseteq\; \mathrm{Part}(D),
> $$
> well defined because monotonicity gives $\gamma_K(T_i) \le \gamma_K(T)$ for each $i$. The cover **glues** iff its defect is degenerate. (For non-monotone $K$ the left quantity can exceed the right — the inversion of §16.2 — and the defect is recorded as an endpoint pair, per the convention of Definition 15.3; the calculus below is developed for the monotone case.)

> **Proposition 37.2 (refinement monotonicity; universality of $\Delta_K$).**
>
> 1. If $\mathcal{V}$ refines $\mathcal{U}$ (both cover $T$, and every member of $\mathcal{V}$ is contained in some member of $\mathcal{U}$), then $\delta_K(\mathcal{V}; T) \supseteq \delta_K(\mathcal{U}; T)$: defects grow under refinement.
> 2. The singleton cover $\mathcal{U}_0(T) = \{\{v\}\}_{v \in T}$ for nonempty $T$ (and $\mathcal{U}_0(\varnothing)=\{\varnothing\}$) is the finest cover up to empty members, and its defect is the registration anomaly: $\delta_K(\mathcal{U}_0; T) = \Delta_K(T)$. Consequently every cover defect is a sub-interval of $\Delta_K(T)$ sharing its right endpoint: **the registration anomaly is the universal defect.**
>
> *Proof.* 1: For $V \in \mathcal{V}$ choose $U_V \in \mathcal{U}$ with $V \subseteq U_V$; monotonicity gives $\gamma_K(V) \le \gamma_K(U_V)$, so $\bigvee_V \gamma_K(V) \le \bigvee_U \gamma_K(U)$, i.e. the left endpoint drops; the right endpoint is fixed. 2: Every cover is refined by $\mathcal{U}_0$ (each $v \in T$ lies in some $T_i$), whose left endpoint is $\bigvee_{v \in T} \gamma_K(\{v\}) = \sigma^{\mathrm{sep}}_K(T)$. $\square$

> **Theorem 37.3 (vanishing).** For monotone $K$ and finite $T$, the following are equivalent:
>
> 1. every cover of $T$ glues;
> 2. the singleton cover of $T$ glues;
> 3. $\Delta_K(T)$ is degenerate, i.e. $K$ is separable at $T$ (Definition 15.3).
>
> Globally: all defect intervals of all covers of all finite $T$ vanish iff $K$ is separable iff (Corollary 15.4) $\sigma^{\mathrm{jnt}}_K$ glues as a content system iff it admits an upper adjoint.
>
> *Proof.* (1)$\Rightarrow$(2) trivially; (2)$\Leftrightarrow$(3) is Proposition 37.2(2) and Definition 15.3. (3)$\Rightarrow$(1): for any cover $\mathcal{U}$, Proposition 37.2 squeezes $\sigma^{\mathrm{sep}}_K(T) \le \bigvee_i \gamma_K(T_i) \le \gamma_K(T)$; degeneracy of the outer interval forces degeneracy of the inner. The global statement collects Corollary 15.4. $\square$

The vanishing theorem is the promised statement "the invariant vanishes iff descent holds," in its exact form: the invariant is the universal defect interval, descent is gluing over the union coverage, and the equivalence is complete — no cover can fail if the singleton cover succeeds, and no cover can carry an obstruction the anomaly does not already contain.

### 37.2 Composition and absorption

Intervals were given composable typing in Definition 15.3; here is the composition they were typed for.

> **Lemma 37.4 (composition of defects).** Let $\mathcal{U} = \{T_i\}$ cover $T$ and, for each $i$, let $\mathcal{V}_i = \{T_{ij}\}_j$ cover $T_i$; the composite $\mathcal{V} = \{T_{ij}\}_{i,j}$ covers $T$. Writing $\ell(\cdot)$ for the left endpoint of a defect:
> $$
> \ell\big(\delta_K(\mathcal{V}; T)\big) \;=\; \bigvee_i \ell\big(\delta_K(\mathcal{V}_i; T_i)\big),
> $$
> with all right endpoints $\gamma_K(T)$, resp. $\gamma_K(T_i)$. Consequently:
>
> 1. if $\delta_K(\mathcal{U}; T)$ and every $\delta_K(\mathcal{V}_i; T_i)$ are degenerate, so is $\delta_K(\mathcal{V}; T)$: triviality composes;
> 2. exactly, $\delta_K(\mathcal{V}; T)$ is degenerate iff $\bigvee_i \ell(\delta_K(\mathcal{V}_i; T_i)) = \gamma_K(T)$ — a *joint* condition on the stage defects, which can hold with individual stage defects nondegenerate. Local anomalies can be **absorbed**.
>
> *Proof.* $\ell(\delta_K(\mathcal{V};T)) = \bigvee_{ij}\gamma_K(T_{ij}) = \bigvee_i \big(\bigvee_j \gamma_K(T_{ij})\big)$, regrouping the join. Item 1: degeneracy of each stage gives $\bigvee_j \gamma_K(T_{ij}) = \gamma_K(T_i)$, and degeneracy of $\mathcal{U}$ gives $\bigvee_i \gamma_K(T_i) = \gamma_K(T)$. Item 2 restates the displayed identity. $\square$

Absorption is not hypothetical; the manuscript's own running example exhibits it.

**Absorption on the parity configuration.** Take §16.1's setup ($D$ the two-bit strings, $G$ the global flip, coordinate views $v, w$, invariance ceiling $\gamma_G$) and adjoin the parity view $u(Z) = b_1 \oplus b_2$, whose kernel is $P_G$ itself, so $\gamma_G(\{u\}) = P_G \wedge \ker(u) = P_G$. Let $T = \{u, v, w\}$; then $\gamma_G(T) = P_G \wedge \top = P_G$. The cover $\mathcal{U} = \{\{u\}, \{v,w\}\}$ has $\ell = P_G \vee P_G = P_G = \gamma_G(T)$: degenerate. Refining $\{v,w\}$ by singletons has stage defect $\Delta_{K}(\{v,w\}) = [\bot, P_G]$: maximally nondegenerate. Yet the composite (the singleton cover of $T$) has $\ell = P_G \vee \bot \vee \bot = P_G$: degenerate. The parity anomaly is real at its own level and absorbed one level up — the interval calculus is genuinely local, and "the data glues" is a statement about a cover, not about the world.

### 37.3 Invariance structures: the orbit-graph formula

The calculus is now applied to the structure class the manuscript has used as its canonical anomaly source since §16.1: **invariance ceilings** $\gamma_G(T) = P_G \wedge \sigma(T)$ for a group $G$ acting on $D$, with $P_G$ the orbit partition. Everything reduces to finite graphs on the orbit set.

Recall (Fact 3.3) that the meet $P_G \wedge \pi$ is the partition whose equivalence relation is the transitive closure of $R_G \cup E_\pi$, where $R_G$ is orbit equivalence and $E_\pi$ the equivalence of $\pi$; and that the interval ${\downarrow} P_G \subseteq \mathrm{Part}(D)$ of orbit-saturated partitions is isomorphic, as a complete lattice, to $\mathrm{Part}(D/G)$, by taking blocks to their orbit contents (joins on both sides are common refinements of saturated partitions, which are saturated). We write $\mathrm{lift}$ for the inverse isomorphism.

> **Theorem 37.5 (orbit-graph formula).** For finite $T$, define the graph $\Gamma_T$ on vertex set $D/G$: orbits $O \ne O'$ are adjacent iff some $Z \in O$, $Z' \in O'$ have $Z \sim_T Z'$. Then
> $$
> \gamma_G(T) \;=\; \mathrm{lift}\big(\mathrm{comp}(\Gamma_T)\big),
> $$
> the lift of the connected-component partition of $\Gamma_T$. In particular $\gamma_G(\{v\}) = \mathrm{lift}(\mathrm{comp}(\Gamma_{\{v\}}))$ and
> $$
> \sigma^{\mathrm{sep}}_{K_G}(T) \;=\; \mathrm{lift}\Big(\bigvee_{v \in T} \mathrm{comp}(\Gamma_{\{v\}})\Big),
> \qquad
> \Delta_{K_G}(T) \;=\; \mathrm{lift}\Big(\Big[\bigvee_{v} \mathrm{comp}(\Gamma_{\{v\}}),\; \mathrm{comp}(\Gamma_T)\Big]\Big).
> $$
>
> *Proof.* $\gamma_G(T) = P_G \wedge \sigma(T)$ has equivalence $\mathrm{tc}(R_G \cup {\sim_T})$. Define $Z \equiv Z'$ iff $q_G(Z), q_G(Z')$ lie in the same $\Gamma_T$-component. $\equiv$ is an equivalence containing $R_G$ (same orbit, same vertex) and $\sim_T$ (a $\sim_T$-pair witnesses an edge or lies in one orbit); conversely any equivalence containing both contains, for each $\Gamma_T$-edge, all pairs across the two orbits (chain through the witnessing pair and orbit moves), hence relates any two candidates over vertices in one component, by induction along a path. So $\equiv \; = \; \mathrm{tc}(R_G \cup \sim_T)$, which is the claim. The displayed consequences are the instance $T = \{v\}$, Definition 14.5, and the fact that $\mathrm{lift}$ is a lattice isomorphism onto ${\downarrow}P_G$, within which all the quantities lie. $\square$

> **Corollary 37.6 (orbit invariance).** The invariance anomaly depends on the group action only through its orbit partition: two actions with the same orbits — abelian or not, faithful or not — induce identical ceilings, identical defects, and identical decompositions below. $\square$

Corollary 37.6 discharges, in one line, the requirement that the formula be verified beyond abelian actions: any non-abelian action is covered by exhibiting its orbits, and Worked example F below runs the machinery on a faithful $S_3$-action for concreteness.

### 37.4 The reflection–witness decomposition

The formula exposes structure inside the anomaly that the interval $\Delta_{K_G}(T)$ alone does not show. Three graphs are in play, with nested edge sets:
$$
\Gamma_T \;\subseteq\; \bigcap_{v \in T} \Gamma_{\{v\}} \;\subseteq\; \Gamma_{\{v\}} \quad (\text{each } v),
$$
where the first inclusion holds because a joint witness is a per-view witness for every view, and can be strict because per-view witnesses need not be *the same pair*.

> **Theorem 37.7 (decomposition).** For an invariance structure and finite $T$:
> $$
> \sigma^{\mathrm{sep}}_{K_G}(T)
> \;\le\;
> \mathrm{lift}\Big(\mathrm{comp}\Big(\bigcap_v \Gamma_{\{v\}}\Big)\Big)
> \;\le\;
> \gamma_G(T),
> $$
> and the anomaly concatenates accordingly, $\Delta_{K_G}(T) = \Delta^{\mathrm{refl}}(T) \cdot \Delta^{\mathrm{wit}}(T)$, into:
>
> - the **reflection component** $\Delta^{\mathrm{refl}}(T) = \big[\sigma^{\mathrm{sep}}_{K_G}(T),\ \mathrm{lift}(\mathrm{comp}(\bigcap_v \Gamma_{\{v\}}))\big]$: the failure of component formation to commute with edge intersection — the mechanism of Proposition 22.3′, now inside the exact theory;
> - the **witness component** $\Delta^{\mathrm{wit}}(T) = \big[\mathrm{lift}(\mathrm{comp}(\bigcap_v \Gamma_{\{v\}})),\ \gamma_G(T)\big]$: the failure of per-view witnesses to cohere into a joint witness — edges asserted view by view with no common witnessing pair.
>
> Both components are independently and strictly realizable: the parity structure of §16.1 has $\Delta^{\mathrm{refl}}$ degenerate and $\Delta^{\mathrm{wit}}$ maximal, and Worked example E below has $\Delta^{\mathrm{wit}}$ degenerate and $\Delta^{\mathrm{refl}}$ nontrivial.
>
> *Proof.* The middle term lies above the left: components of a graph with fewer edges refine components of any single $\Gamma_{\{v\}}$, hence refine their join. It lies below the right by $\Gamma_T \subseteq \bigcap_v \Gamma_{\{v\}}$ and monotonicity of components under edge inclusion (in the lifted order: fewer edges, finer components, greater partition). Concatenation of the intervals is the identity $[a, b] = [a, m] \cdot [m, b]$ of Definition 15.3's interval typing. Parity: $\Gamma_{\{v\}}$ and $\Gamma_{\{w\}}$ each consist of the single edge $O_1O_2$ (witnessed by $(00, 01)$ and $(00, 10)$ respectively), so the intersection graph retains the edge and $\mathrm{comp} = \bot$ on two vertices — equal to $\sigma^{\mathrm{sep}} = \bot$, so $\Delta^{\mathrm{refl}}$ degenerates — while $\Gamma_T$ is empty (no pair agrees on both coordinates across orbits), so $\gamma_G = P_G$ and $\Delta^{\mathrm{wit}} = [\bot, P_G]$ is the whole anomaly. Example E supplies the other extreme. $\square$

> **Worked example E (a pure reflection anomaly).** Let $D = \{a_1, a_2, b_1, b_2, c_1, c_2\}$ and let $G = \mathbb{Z}_2$ act by the involution swapping $a_1 \leftrightarrow a_2$, $b_1 \leftrightarrow b_2$, $c_1 \leftrightarrow c_2$, with orbits $O_1 = \{a_1 a_2\}$, $O_2 = \{b_1 b_2\}$, $O_3 = \{c_1 c_2\}$. Two views:
> $$
> v:\ a_1 \mapsto \alpha,\ a_2 \mapsto \beta,\ b_1 \mapsto \alpha,\ b_2 \mapsto \gamma,\ c_1 \mapsto \gamma,\ c_2 \mapsto \delta;
> $$
> $$
> w:\ a_1 \mapsto p,\ a_2 \mapsto q,\ b_1 \mapsto p,\ b_2 \mapsto r,\ c_1 \mapsto s,\ c_2 \mapsto q,
> $$
> with the listed values pairwise distinct within each view. Then $\Gamma_{\{v\}}$ has edges $\{O_1O_2, O_2O_3\}$ (witnesses $(a_1, b_1)$ and $(b_2, c_1)$) and $\Gamma_{\{w\}}$ has edges $\{O_1O_2, O_1O_3\}$ (witnesses $(a_1, b_1)$ and $(a_2, c_2)$); each is connected, so $\gamma_G(\{v\}) = \gamma_G(\{w\}) = \bot$ and $\sigma^{\mathrm{sep}} = \bot$. The intersection graph has the single edge $O_1O_2$, whose per-view witnesses are the *same pair* $(a_1, b_1)$ — which is therefore a joint witness — so $\Gamma_T = \bigcap_v \Gamma_{\{v\}}$ and the witness component is degenerate. Components of the single-edge graph give $\gamma_G(T) = \mathrm{lift}(\{O_1 O_2 \mid O_3\})$, so
> $$
> \Delta_{K_G}(T) \;=\; \Delta^{\mathrm{refl}}(T) \;=\; \big[\bot,\ \mathrm{lift}(\{O_1O_2 \mid O_3\})\big],
> $$
> nontrivial with no witness incoherence anywhere: the anomaly is produced entirely by the two connected per-view graphs intersecting to a disconnected one — transitive closure failing to commute with intersection, on three vertices. (One checks directly: $\sigma(T)$ merges exactly $a_1, b_1$; the meet with $P_G$ chains $a_2$–$a_1$–$b_1$–$b_2$ and isolates $\{c_1, c_2\}$, matching the formula.)

The decomposition also settles a question of mechanism left open by the mechanism ladder of §22.2. There, reflection was identified as the graded zero-error mechanism; here it reappears *inside the exact theory*, driven not by noise supports but by orbit projection. The two exact anomalies known to the manuscript — invariance-type registration anomalies and the tolerance-to-partition losses of Proposition 22.3′ — are, at the level of mechanism, one phenomenon in two lattices: a closure operator (transitive closure; component formation) failing to commute with a meet (edge intersection). The witness nerve records missing joint witnesses at the edge level. Its homology is studied next; Appendix D.9 supplies the separate component-level cut criterion.

---

## 38. The witness nerve and the linearized track

This section carries out the linearized program promised in §34 and determines exactly what it can and cannot see.

### 38.1 The witness presheaf is a sheaf

Fix an invariance structure, finite $T$, and an orbit pair $(O, O')$. For $T' \subseteq T$ define the **witness set**
$$
W_{T'}(O, O') \;=\; \{\, (Z, Z') \in O \times O' \;:\; Z \sim_{T'} Z' \,\},
$$
so that $(O,O')$ is an edge of $\Gamma_{T'}$ iff $W_{T'}(O,O') \ne \varnothing$. The assignment $T' \mapsto W_{T'}(O,O')$ is contravariant with restriction maps the inclusions $W_{T'} \subseteq W_{T''}$ for $T'' \subseteq T'$.

> **Lemma 38.1 (sheaf property for positive covers).** The witness presheaf is a sheaf for the positive union coverage (nonempty covering families, including over the empty object): for any cover $\{T_i\}$ of $T$,
> $$
> W_{T}(O, O') \;=\; \bigcap_i W_{T_i}(O, O'),
> $$
> and since restrictions are inclusions, every matching family is constant and amalgamates uniquely. Consequently the witness anomaly is **not** a failure of compatible local data to glue; it is the emptiness of the global-section set despite nonemptiness of every local one. This all-local-sections, no-global-section pattern has the same possibilistic form as the logical contextuality of [Abramsky & Brandenburger 2011], but the two presheaves differ (see the scope note below and Appendix D.12), and no identification is claimed.
>
> *Proof.* Agreement on $T = \bigcup T_i$ is agreement on every $T_i$; the intersection identity follows. A matching family assigns $w_i \in W_{T_i}$ agreeing under restriction; restrictions being inclusions into common supersets, agreement forces $w_i = w_j$ as pairs, and the common value lies in the intersection. $\square$

**Mathematical scope.** The lemma uses the positive union coverage of §35. If the empty family covers $\varnothing$, a Set-valued sheaf must have a singleton there, whereas $W_\varnothing=O\times O'$ generally does not. Further, this is an intersection-consistency problem with inclusion restrictions retaining the *entire candidate pair*. It is not, without a comparison construction, the Abramsky–Brandenburger event/support presheaf with coordinate restrictions. Nonempty local sets need not form a matching family; their empty total intersection violates no sheaf axiom.

### 38.2 The nerve and its characterizations

> **Definition 38.2 (witness nerve).** The **witness nerve** of $(T; O, O')$ is the simplicial complex
> $$
> N_T(O, O') \;=\; \{\, T' \subseteq T \;:\; W_{T'}(O, O') \ne \varnothing \,\},
> $$
> downward closed because the witness sets are antitone.

> **Proposition 38.3 (nerve dictionary).** For an orbit pair $(O, O')$:
>
> 1. $v$ is a vertex of $N_T(O,O')$ iff $(O,O')$ is an edge of $\Gamma_{\{v\}}$; the vertex set is full iff $(O,O')$ is an edge of $\bigcap_v \Gamma_{\{v\}}$.
> 2. $T \in N_T(O,O')$ (the top face is present) iff $(O,O')$ is an edge of $\Gamma_T$.
> 3. The pair carries an **edge-level witness defect** — a per-view-confusable, jointly-separated orbit pair — iff its nerve has a full vertex set and a missing top face.
> 4. $\Delta^{\mathrm{wit}}(T)$ nondegenerate implies some pair carries an edge-level defect; the converse can fail, since component formation can absorb redundant missing edges — the absorption phenomenon of Lemma 37.4 recurring one level down.
>
> *Proof.* 1–3 unfold the definitions. 4: if all full-vertexed nerves have their top faces, then $\Gamma_T = \bigcap_v \Gamma_{\{v\}}$ and the middle and right terms of Theorem 37.7 coincide; the converse direction only needs the component partitions to differ, which requires some edge difference but is not implied by one. $\square$

### 38.3 The hierarchy: threshold structures and sphere boundaries

The nerve is not merely a bookkeeping device; on a canonical family of structures it takes the values that make the linearized track genuinely cohomological.

> **Theorem 38.4 (the cyclic hierarchy $C_{k+1}$).** For every $k \ge 1$ there is an invariance structure with $k+1$ views whose anomaly is a pure witness anomaly and whose witness nerve is the boundary of the $k$-simplex:
> $$
> N_T(O, O') \;=\; \partial \Delta^k,
> \qquad
> \widetilde{H}_{k-1}\big(N_T(O,O')\big) \cong \mathbb{Z} \;\ne\; 0 .
> $$
> Moreover the structure is an exact **all-or-nothing threshold scheme**: the orbit question $q_G$ (kernel $P_G$) is jointly answerable under $\gamma_G$ from the full family and from no proper subfamily — every proper subfamily has admissible content $\bot$.
>
> *Construction and proof.* Let $X = \{1, \dots, k+1\}$, let $D = X \sqcup X'$ be two disjoint copies, and let any group with the two copies as its orbits act — e.g. $\mathbb{Z}_{k+1}$ cycling both copies, or the diagonal action of the full symmetric group; by Corollary 37.6 the choice is immaterial. Take views $v_1, \dots, v_{k+1}$, where $v_m$ assigns a common value to $i$ and $i'$ for every $i \ne m$, distinct values across these two-element classes, and fresh values to $m$ and $m'$ — distinct from each other and from every class value, so that $(m, m')$ does not agree on $v_m$. Then the pair $(i, i')$ agrees on $v_m$ iff $i \ne m$, and a cross pair $(i, j')$ with $i \ne j$ agrees on no view (its members always lie in distinct value classes). For nonempty $T'$, $W_{T'}(O,O')=\{(i,i'):v_i\notin T'\}$. At the empty context, $W_\varnothing=O\times O'$ is also nonempty. Thus $W_{T'}$ is nonempty iff $T'\ne T$: the nerve is exactly the set of proper subsets of $T$, i.e. $\partial\Delta^k$, whose reduced homology is that of the sphere $S^{k-1}$. Purity: on two vertices the middle term of Theorem 37.7 has a single edge (all vertices full), so $\mathrm{comp} = \bot = \sigma^{\mathrm{sep}}$ and $\Delta^{\mathrm{refl}}$ degenerates, while $\Gamma_T$ is empty, so $\gamma_G(T) = P_G$ and $\Delta^{\mathrm{wit}} = [\bot, P_G]$. Threshold: any proper $T' \subsetneq T$ omits some $v_i$, so $(i, i') \in W_{T'}$, the orbit graph over $T'$ is connected, and $\gamma_G(T') = \bot$; the full family has $\gamma_G(T) = P_G = \ker(q_G)$, so $q_G$ is jointly answerable exactly there. $\square$

> **Worked example F (the triangle on a non-abelian action).** Instantiate $k = 2$ with $G = S_3$ acting diagonally on $D = \{1,2,3\} \sqcup \{1',2',3'\}$ (a faithful, non-abelian action with orbits the two copies). Concretely, with values chosen per the construction, view $v_1$ merges $(2,2')$ and $(3,3')$; $v_2$ merges $(1,1')$ and $(3,3')$; $v_3$ merges $(1,1')$ and $(2,2')$. Each designated pair agrees on exactly two of the three views; no pair agrees on all three; the nerve is the hollow triangle $\partial\Delta^2$ with $\widetilde{H}_1 \cong \mathbb{Z}$. The orbit question ("which copy?") is answerable under invariance from all three views jointly and from no two — a $3$-share all-threshold scheme whose obstruction class is the fundamental class of a circle. The case $k=1$ has the same two-orbit witness interval and nerve $\partial\Delta^1=S^0$ as the parity structure of §16.1. Its raw view partitions need not be isomorphic to the two binary coordinate partitions; the agreement is at the witness-graph level.

### 38.4 The division of labor, proved

> **Worked example G (a homology-blind witness anomaly).** Let $D = \{a_1, a_2, b_1, b_2\}$ with $G = \mathbb{Z}_2$ swapping within $A = \{a_1 a_2\}$ and $B = \{b_1 b_2\}$, and three views $u, v, w$ arranged so that $(a_1, b_1)$ agrees on exactly $\{u, v\}$, $(a_2, b_2)$ agrees on exactly $\{v, w\}$, and no pair agrees on $\{u, w\}$ or on all three (assign shared values only as stipulated, fresh values elsewhere). Then $W_u = \{(a_1,b_1)\}$, $W_v = \{(a_1,b_1), (a_2,b_2)\}$, $W_w = \{(a_2,b_2)\}$, $W_{uv} = \{(a_1,b_1)\}$, $W_{vw} = \{(a_2,b_2)\}$, $W_{uw} = W_{uvw} = \varnothing$. The nerve is the *path* $u - v - w$: full vertex set, missing top face — an edge-level witness defect — but contractible, with vanishing reduced homology in all degrees.

> **Proposition 38.5 (limits of nerve certificates).** For a fixed orbit pair with a full vertex set, a missing top face is exactly an edge-level witness defect. Nonzero reduced homology implies that defect, but the path nerve in Example G shows the converse fails. Neither condition alone certifies a nonzero **partition-level** witness interval: redundant missing edges can be absorbed by component formation (Proposition 38.3(4)).
>
> Reflection compares component partitions of several graphs and is not certified by the presence of a missing top face for one orbit pair. Example E proves that a reflection anomaly can occur while each pair's nerve is a simplex on its own vertices. A degenerate witness *interval* does not imply equality of the joint graph and the intersection graph, and therefore does not force every nerve to be a simplex.
>
> *Proof.* The first statements are Proposition 38.3 and contractibility of Example G. Removing a redundant edge can leave components unchanged; this separates graph defects from interval defects. Example E verifies the last existence statement. Appendix D.9 characterizes precisely when the deleted edges split a component. The full family of nerves does encode all edge sets and hence can reconstruct reflection; what is insufficient is the asserted per-pair homological certificate. $\square$

Two closing connections. First, chirality (Remark 36.1): the witness presheaf is a sheaf-chirality object whose global-section emptiness detects an edge-level witness defect, which may still be absorbed at the content-partition level. In this sense §38 is where the two ends meet: the witness presheaf is analogous to the distribution-level problem of the next section, although no identification with its support presheaf has been constructed. Second, the linearized track answers the question of *degree*: witness anomalies are stratified by the minimal dimension of a missing face over a full skeleton, parity failing at dimension one, the triangle at dimension two, and the hierarchy showing every degree is realized. The hierarchy is formally reminiscent of the logical/strong contextuality hierarchy, but witness anomalies do not imply contextuality of the marginal empirical model (Appendix D.12).

---

## 39. Coupling descent: the marginal problem as a sheaf condition

The distribution level is where descent takes its classical sheaf form, and where a sixty-year-old theorem was waiting to be recognized as the descent criterion.

> **Definition 39.1 (coupling presheaf; fibers).** Under (A6), the **coupling presheaf** on $\mathcal{F}(V)$ assigns to finite $T'$ the set $\mathcal{P}(T')$ of channels $D \to \Pr(\prod_{v \in T'} Y_v)$, with restriction along $T'' \subseteq T'$ given by marginalization. A **matching family** over a cover $\{T_i\}$ of $T$ is a family $p_i \in \mathcal{P}(T_i)$ agreeing under marginalization on all intersections $T_i \cap T_j$; an **amalgamation** is $p \in \mathcal{P}(T)$ restricting to every $p_i$. The **fiber** over a matching family is its set of amalgamations. A coherent graded family (Definition 21.2) is exactly a compatible choice of amalgamations at every level; the coupling fiber of Remark 21.3 is the fiber over the singleton-cover matching family (the marginal system), for every $T$ at once.

> **Theorem 39.2 (Vorob'ev's theorem as the descent criterion).** Let $\mathcal{U} = \{T_1, \dots, T_n\}$ be a cover of $T$. For every choice of finite outcome alphabets, every matching family over $\mathcal U$ admits an amalgamation iff $\mathcal{U}$ is **acyclic**: its maximal members admit a running-intersection ordering ($T_{m} \cap (T_1 \cup \cdots \cup T_{m-1}) \subseteq T_{j(m)}$ for some $j(m) < m$, after reordering). [Vorob'ev 1962] The acyclicity condition is, in modern terminology, decomposability of the hypergraph — the junction-tree condition.
>
> *Proof sketch.* Sufficiency is the sequential conditional-product construction: given a running-intersection ordering, extend the partial amalgamation over $T_1 \cup \cdots \cup T_{m-1}$ by adjoining, independently given the separator $T_m \cap T_{j(m)}$, the conditional of $p_{T_m}$ given that separator; consistency on the separator is exactly the matching condition, and the marginal checks are direct. Necessity — for every non-acyclic complex there exists a consistent, non-amalgamable family — is Vorob'ev's theorem, applied candidatewise (channels are indexed families of finite distributions, and the obstructing family can be taken constant in $Z$ or not, as needed). $\square$

Three consequences knit the reformulation into the standing theory.

> **Proposition 39.3 (the two failure modes, in one object).** Over the coupling presheaf:
>
> 1. **(Contextual evidence $=$ empty fiber.)** A matching family with no amalgamation is a system of locally coherent, jointly incoherent experimental records — Part I §8's "joint inconsistency of individually coherent views," and exactly the no-signalling empirical models whose non-extendability constitutes contextuality in [Abramsky & Brandenburger 2011]. Theorem 39.2 says which covers are immune: the acyclic ones. The candidate-pair witness presheaf of §38 has different restrictions; it is not identified with this empirical-model support presheaf. Appendix D.12 gives an explicit separation.
> 2. **(Underdetermination $=$ non-singleton fiber.)** Even over acyclic covers the fiber is generally not a singleton, and statistical content is *not a function of the matching family*: Proposition 22.4(2)'s two couplings lie in one fiber over the singleton cover of $\{v, w\}$, with $\sigma^{=}$ equal to $\bot$ at one point of the fiber and $\top$ at another. For the singleton-cover fiber, non-constancy of $\sigma^{=}$ is equivalent to existence of some statistically superadditive coupling; it is not a condition satisfied by every coupling in that fiber, and the Le Cam diameter of a fiber is the natural quantitative measure of the underdetermination.
>
> *Proof.* 1 collects Theorem 39.2 and the cited identifications. 2: the singleton cover is acyclic (empty intersections); the two couplings of Proposition 22.4(2) share their marginal matching family by construction and differ in $\sigma^{=}$ as computed there. $\square$

> **Proposition 39.4 (anchored generators).** Intrusion coupling (Proposition 29.8) is a physical mechanism acting at the distribution level of descent: a marginally-blind family pattern fixes the perceived matching family over the singleton cover (each perceived marginal is determined and candidate-blind) while selecting the point of the fiber through the correlation of intrusions — under $Z$ one amalgamation, under $Z'$ another. Mis-anchoring thereby *generates* nontrivial motion along fibers with every feature channel honest, which is the descent-level restatement of Part IV's finding that anchoring supplies a source of the coupling mechanism rather than a fourth mechanism. $\square$

---

## 40. Approximate descent

Remark 24.7 typed the comparison cells metrically; this section proves the two results that fix what quantitative descent can and cannot mean. Recall Le Cam's deficiency $\delta(E, F)$ and distance $\Delta(E, F) = \max(\delta(E,F), \delta(F,E))$ [Le Cam 1964; Torgersen 1991], Represent the local experiments of a cover $\mathcal{U} = \{T_i\}$ by the union of their lower sets, ${\bigcup_i}{\downarrow}P_{T_i}$ (Remark 24.6), and measure the comparison cell at $T$ by
$$
d(\mathcal{U}; T) \;=\; \min_i \, \delta\big(P_{T_i},\, P_T\big),
$$
the deficiency of the best single local experiment at reproducing the global one; it is zero exactly when $P_T$ lies in that union. This is a deliberately weak measure. It does not assemble the local experiments into a joint one — an assembled join would require a chosen amalgamation, i.e. a point of §39's fiber, and the fiber is the object under study, not an input — so a cover whose members are informative only jointly has a positive cell even when the joint experiment is determined by the members (for example, under conditional independence). The two results below concern this measure.

> **Proposition 40.1 (stability under blind corruption).** Let a coherent family over $T$ be corrupted by a jointly candidate-blind family pattern (Definition 29.7) with survival probability $\lambda(\varnothing) = 1 - \varepsilon > 0$. Then $\Delta(\widetilde{P}_{T'}, P_{T'}) \le \varepsilon$ for every $T' \subseteq T$, and consequently every enriched cell defect is $2\varepsilon$-stable:
> $$
> \big|\, d(\mathcal{U}; T)\big(\widetilde{P}\big) \;-\; d(\mathcal{U}; T)\big(P\big) \,\big| \;\le\; 2\varepsilon
> \qquad \text{for every cover } \mathcal{U} \text{ of } T.
> $$
>
> *Proof.* Couple the perceived and intended draws on the event of no intrusion, which has probability $\ge 1 - \varepsilon$ under every candidate; then $\|\widetilde{P}_{T'}(\cdot \mid Z) - P_{T'}(\cdot \mid Z)\|_{TV} \le \varepsilon$ for all $Z$ (the induced pattern on $T'$ has survival $\ge \lambda(\varnothing)$), and the identity transition witnesses both one-sided deficiencies, as in Remark 29.5. For the cells, the deficiency triangle inequality gives, for each $i$, $\delta(\widetilde{P}_{T_i}, \widetilde{P}_T) \le \delta(\widetilde{P}_{T_i}, P_{T_i}) + \delta(P_{T_i}, P_T) + \delta(P_T, \widetilde{P}_T) \le \delta(P_{T_i}, P_T) + 2\varepsilon$, and symmetrically; minima over $i$ of functions moving by at most $2\varepsilon$ move by at most $2\varepsilon$. $\square$

> **Proposition 40.2 (discontinuity of the exact strata).** Approximate descent is a full-stratum notion: the partition-valued cells are not deficiency-continuous. For every $\varepsilon \in (0, 1)$ there is a marginally candidate-blind pattern at rate $\varepsilon$ under which the perceived family lies within Le Cam distance $2\varepsilon$ of an intended family whose every content is $\bot$ and every cell degenerate, while the perceived statistical cell at $\{v, w\}$ is maximal:
> $$
> \sigma^{=}(\widetilde{v}) = \sigma^{=}(\widetilde{w}) = \bot,
> \qquad
> \sigma^{=}\big(\widetilde{P}_{\{v,w\}}\big) = \top .
> $$
>
> *Proof.* Take $D = \{Z, Z'\}$, honest emissions deterministic at $0$ on both views for both candidates, clutter $\delta_1$ per view; under $Z$ both views intrude together with probability $\varepsilon$, under $Z'$ independently with probability $\varepsilon$ each. Each marginal pattern is blind at rate $\varepsilon$, so both perceived marginals equal $(1-\varepsilon)\delta_0 + \varepsilon\delta_1$ under both candidates: $\sigma^= = \bot$ per view. The perceived joints are $(1-\varepsilon)\delta_{00} + \varepsilon\delta_{11}$ under $Z$ and $\big((1-\varepsilon)\delta_0 + \varepsilon\delta_1\big)^{\otimes 2}$ under $Z'$, distinct for all $\varepsilon \in (0,1)$: $\sigma^= = \top$ jointly. Total variation to the intended (constant $\delta_{00}$) is at most $1 - (1-\varepsilon)^2 \le 2\varepsilon$ under either candidate. $\square$

> **Remark 40.3 (reading).** Along the blind fidelity axis, the enriched content system is Lipschitz (constant $2$) and quantitative descent is well posed, exactly as Remark 24.7 anticipated; the exact strata jump. This is the descent-theoretic face of the stratum trichotomy of Theorem 29.4 — the same fragility that annihilates $\sigma^0$ under arbitrarily small blind corruption makes exact cells discontinuous under arbitrarily small *coupled* corruption — and it delimits H4's approximate-gluing program precisely: obstruction classes can be measured stably only in the enriched (deficiency) coefficients; their exact shadows are discrete invariants that switch, not drift.

---

## 41. Fidelity and descent

Part IV established the trichotomy of the fidelity axis (§32.2); this section states what each regime does to descent data, upgrading Theorem 29.4(2) to the family level on the way.

> **Lemma 41.1 (blind replacement is injective).** Let $(\lambda, \{R_\kappa\})$ be a jointly candidate-blind family pattern on finite $S$ with $\lambda(\varnothing) > 0$. The induced affine map on joint laws,
> $$
> p \;\longmapsto\; \widetilde{p} \;=\; \sum_{\kappa \subseteq S} \lambda(\kappa)\, \big( p_{S \setminus \kappa} \otimes R_\kappa \big),
> $$
> is injective on $\Pr\big(\prod_{v \in S} Y_v\big)$.
>
> *Proof.* Let $d = p - p'$ with $\widetilde{p} = \widetilde{p}'$; we show every marginal $d_{S'}$ vanishes, by induction on $|S'|$. Marginalizing the identity $\sum_\kappa \lambda(\kappa)(d_{S\setminus\kappa} \otimes R_\kappa) = 0$ onto $S'$: a term with $\kappa \cap S' \ne \varnothing$ depends on $d$ only through $d_{S' \setminus \kappa}$, and $S' \setminus \kappa \subsetneq S'$, so it vanishes by the inductive hypothesis; a term with $\kappa \cap S' = \varnothing$ contributes $\lambda(\kappa)\, d_{S'}$. Hence $\big(\sum_{\kappa \cap S' = \varnothing} \lambda(\kappa)\big) d_{S'} = 0$ with coefficient $\ge \lambda(\varnothing) > 0$, so $d_{S'} = 0$; at $S' = S$ this is $p = p'$. $\square$

> **Theorem 41.2 (blind corruption is descent-neutral at the statistical stratum).** Let a coherent family over $T$ be corrupted by a jointly candidate-blind pattern with $\lambda(\varnothing) > 0$. Then:
>
> 1. **(Presheaf endomorphism.)** The replacement operation commutes with marginalization — the marginal of the perceived joint onto $T'$ is the perceived joint of the induced (again jointly blind, survival $\ge \lambda(\varnothing)$) pattern on $T'$ — so blind corruption is an endomorphism of the coupling presheaf: it carries matching families to matching families and amalgamations to amalgamations, and creates no distribution-level obstruction.
> 2. **(Exact invariance of $\sigma^{=}$.)** For every $T' \subseteq T$, $\sigma^{=}(\widetilde{P}_{T'}) = \sigma^{=}(P_{T'})$; hence every statistical-stratum content, every comparison cell, and every defect interval is *exactly* preserved. Blind corruption can neither create nor destroy statistical-stratum obstructions.
>
> *Proof.* 1: Marginalizing the replacement output onto $T'$ retains $y$'s coordinates on $T' \setminus \kappa$ and $r$'s on $\kappa \cap T'$; grouping configurations by $\kappa' = \kappa \cap T'$ yields a pattern on $T'$ with $\lambda_{T'}(\kappa') = \sum_{\kappa \cap T' = \kappa'} \lambda(\kappa)$ and clutter the corresponding $\lambda$-weighted mixture of marginals of the $R_\kappa$ — all $Z$-free, and $\lambda_{T'}(\varnothing) \ge \lambda(\varnothing)$. Commutation with marginalization is this computation; the consequences for matching families are formal. 2: By item 1 the map on $T'$-joints has the form of Lemma 41.1 with positive survival, hence is injective; injectivity gives $\widetilde{P}_{T'}(\cdot \mid Z) = \widetilde{P}_{T'}(\cdot \mid Z') \iff P_{T'}(\cdot \mid Z) = P_{T'}(\cdot \mid Z')$, i.e. $\ker \widehat{R}$ is preserved at every level, hence so are all joins, cells, and intervals built from these partitions. $\square$

> **Proposition 41.3 (marginal blindness creates classes at every rate).** Marginal candidate-blindness without joint blindness can create a maximal statistical comparison cell at arbitrarily small rate: the construction of Proposition 40.2 does so for every $\varepsilon \in (0, 1)$, of which Proposition 29.8(2) is the rate-$\tfrac12$ case. The gap between marginal and joint blindness is thus exactly the coupling channel, now measured: it is the entire distance between descent-neutrality (Theorem 41.2) and unbounded obstruction creation. $\square$

> **Remark 41.4 (the trichotomy, in descent form).** The fidelity axis of §32.2 sorts as follows. Under (A4′) the perceived and intended descent data are equal. Under jointly blind corruption the perceived datum is the image of the intended one under a presheaf endomorphism: obstructions are preserved exactly at $\sigma^{=}$ (Theorem 41.2), possibly altered at $\sigma^{0}$ (annihilated under whole-record common clutter, Theorem 29.4(1), but not under arbitrary partial replacement), and moved by at most $2\varepsilon$ in the enriched coefficients (Proposition 40.1). Under targeted corruption no comparison morphism need exist at all — Theorem 29.6 realizes creation, destruction, and incomparability — so the perceived datum is not a degraded copy of the intended one but a different descent problem, whose difference is partly made of information. Blind mis-anchoring garbles descent data; targeted mis-anchoring re-authors it.

---

## 42. Recovery, and descent as a coordinate

### 42.1 The descent-trivial fiber

> **Theorem 42.1 (recovery).** Under full admissibility, determinism, and sound unique anchoring — the kernel regime of Parts I–II, per Theorems 24.2 and 32.1 — all three levels of descent are trivial:
>
> 1. **(Readings.)** $\mathcal{K}(T)$ is the class of all sound registrations of $c_T$, and combinations of per-view canonical registrations are cofinal in it: every sound joint reading is dominated by a combination (Proposition 36.3 with $\gamma_K = \sigma$; Lemma 4.7 and Proposition 6.3 are its two classical faces).
> 2. **(Content.)** Every defect interval of every cover degenerates (Theorem 37.3, $K^{\mathrm{can}}$ being separable); with trivial $G$, orbits are singletons, every realized witness nerve is a full simplex on its vertex set (a $\sim_T$-pair is its own joint witness), and both components of Theorem 37.7 vanish identically.
> 3. **(Distributions.)** The deterministic coupling presheaf is a sheaf with *unique* amalgamation: deterministic marginals admit exactly one joint (the pairing), so every matching family glues, uniquely (Theorem 24.2(1) restated). Neither failure mode of Proposition 39.3 — contextual evidence, underdetermination — can occur.
>
> *Proof.* Each item collects the citations given; item 3's uniqueness: a joint law whose marginals are point masses is the product point mass. $\square$

### 42.2 The coordinate

Section 24 tracked codomain and compositionality; Remark 24.6 added representability; §32.2 added fidelity. Part V's results are collected as a fifth coordinate — **descent**, per level — extending the collapse table:

| layer | reading level | content level | distribution level |
|---|---|---|---|
| kernel (full admissibility, deterministic) | combinations cofinal (Thm 42.1) | all defects vanish (Thm 37.3) | sheaf, unique gluing (Thm 42.1) |
| monotone admissibility | glue exists; cofinality fails at nonseparable $K$ (Prop. 36.3) | interval calculus: universal defect $\Delta_K$, composition with absorption (§37.1–2) | — (exact) |
| invariance ceilings | as above, computed on orbit graphs | anomaly $=$ reflection $\cdot$ witness (Thm 37.7); edge-level witness defects encoded by nerves, with incomplete homology certificates; component absorption remains possible; threshold hierarchy $\partial\Delta^k$ (§38) | — (exact) |
| graded (coherent families) | Part VI: exact all-determination coherence (Thm. 45.4); fixed-decoder invariance and sufficient budget transfer (Props. 47.1, 48.1) | strata as in §24 | Vorob'ev: unconditional gluing iff acyclic cover; fibers carry underdetermination; $\sigma^{=}$ non-constant on fibers (§39) |
| enriched | — | cell defects $2\varepsilon$-stable under blind corruption; exact cells discontinuous (§40) | fiber diameter in Le Cam metric |
| fidelity | — | blind: presheaf endomorphism, $\sigma^{=}$-obstructions exactly preserved; marginal-only blindness creates; targeted severs comparison (§41) | intrusion coupling moves along fibers (Prop. 39.4) |

The asymmetry worth naming: at the exact levels the glue always *exists* and the obstruction is cofinality (how much the glue reaches); at the distribution level existence itself can fail. The manuscript's two oldest slogans — "no coherent combination" and "multiple coherent combinations" (Part I §8, H4) — turn out to live at different levels of the same base, and both now have addresses, criteria, and generators.

### 42.3 Two closing remarks

> **Remark 42.2 (the epistemological payoff).** Part V delivers a classical theory of **jointly irreducible evidence**: configurations of individually meaningful, individually invariant readings that admit no joint witness — small finite domains and finite groups, with no quantum-mechanical input — with the invariance structures of §16.1 as generators, the witness nerve as an edge-level criterion, and sphere boundaries as the canonical examples. (Contextuality in the sense of the marginal problem is the distribution-level phenomenon of §39; Appendix D.12 shows the two are distinct.) Read against Part I's roots (§2): contrastivism supplies the domain-relativity, measurement-theoretic meaningfulness supplies the ceilings, and the witness anomaly is the exact statement that *meaning can be irreducibly joint* — invariant content that exists at the family and at no member, with the threshold hierarchy showing the phenomenon at every arity. Underdetermination, its sheaf-chirality twin, is the non-singleton fiber, quantified by Le Cam diameter. Both are now theorems with computable invariants rather than named phenomena.

> **Remark 42.3 (the decomposition problem).** Witness loss, component reflection, and coupling variation identify distinct local-to-global mechanisms. Part VII evaluates exact partition chains and, separately, coupling-fiber excess; it does not prove one universal additive decomposition for arbitrary graded ceilings. Prior averaging changes the fiber and the assigned addresses, with the inequality of Appendix D.4. An axiomatic unification must specify its input data, admissibility, and coefficient object before a proof or a PID comparison can be attempted.

---

## 43. Established results and scope

The interval calculus, orbit formula, reflection/witness split, and threshold examples are finite results. Nerves detect missing witness edges; Appendix D.9 gives the additional cut criterion for a nonzero partition interval. Appendix D.8 settles the join-cover site criterion. Marginal nonextendability concerns merely local channel data; a coherent global family already supplies an amalgamation (D.12). The witness presheaf is not automatically the event/support presheaf of contextuality. The universal acyclicity converse in Theorem 39.2 is an explicitly imported result.

**References added in Part V:** none. The part is built entirely from sources already cited in Parts I–IV — Abramsky & Brandenburger, Vorob'ev, Le Cam, Torgersen, Shamir, and the manuscript's own results — a fact worth recording, since it certifies that the obstruction theory was latent in the assembled material rather than imported.
