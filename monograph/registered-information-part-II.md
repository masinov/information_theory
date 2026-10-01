# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part II: Worked Examples and the Admissibility Layer

---

## 10. Overview of Part II

Part II has two halves. Sections 11–13 test the kernel against three settings where the right answer is already known: a small diagnostic problem, functional dependencies in relational databases, and observability of a finite machine. In each case the induced quotient, answerability, and the marginal-value theorem reproduce the established notions.

Sections 14–16 relax standing assumption (A3). Canonical registration — the most informative sound registration, by Lemma 4.7 — is replaced by an **admissibility structure**: for each finite set of views, a ceiling on the distinctions an admissible decoder may draw. This models interpreters that cannot realize the canonical registration, such as decoders constrained by an invariance or by an output budget. Assumptions (A1), (A2), (A4), and (A5) remain in force.

The main results are:

- every ceiling is realized by some sound registration (Lemma 14.4), and monotonicity of the ceilings is exactly the condition that admissible readings stay admissible when more data are supplied (Proposition 14.4′);
- for monotone structures, admissible content is bracketed between nothing and canonical content (Proposition 14.6);
- content obtained by reading each view separately keeps the kernel's adjunction and its corollaries (Theorem 15.1), while content obtained by reading the views jointly keeps it exactly when the structure is *separable* (Corollary 15.4);
- the gap between joint and separate content, the **registration anomaly**, is realized at full strength by an invariance structure on two bits (§16.1), and can be inverted by non-monotone structures (§16.2).

---

## 11. Worked example A: clinical diagnosis and missing information

This example exhibits, on the smallest scale that shows all phenomena, the full cycle: compute the induced quotient, detect an unanswerable question via unresolved pairs, and verify the marginal value of a new view.

**Setup.** Let the contrast domain be six patient states,
$$
D=\{s_1,s_2,s_3,s_4,s_5,s_6\}.
$$
Three views are available: a lab reading $L:D\to\{\mathrm{lo},\mathrm{hi}\}$, a symptom flag $F:D\to\{0,1\}$, and an age bracket $A:D\to\{\mathrm{y},\mathrm{o}\}$. The question is a diagnosis $q:D\to\{\text{well},\text{mild},\text{severe}\}$. The data are given by the table:

| state | $L$ | $F$ | $A$ | $q$ |
|---|---|---|---|---|
| $s_1$ | lo | 0 | y | well |
| $s_2$ | lo | 0 | o | mild |
| $s_3$ | lo | 1 | y | mild |
| $s_4$ | hi | 0 | y | mild |
| $s_5$ | hi | 1 | y | severe |
| $s_6$ | hi | 1 | o | severe |

**Content of $\{L,F\}$.** The view partitions are
$$
\ker(L)=\{\,s_1s_2s_3\mid s_4s_5s_6\,\},\qquad
\ker(F)=\{\,s_1s_2s_4\mid s_3s_5s_6\,\}.
$$
Their join (common refinement, Fact 3.3), which by Definition 5.2 is $\sigma(\{L,F\})$, groups states by the pair $(L,F)$:
$$
\sigma(\{L,F\})=\{\,s_1s_2\mid s_3\mid s_4\mid s_5s_6\,\}.
$$

**Answerability of $q$.** By Proposition 5.6, $q$ is answerable from $\{L,F\}$ iff it is constant on every block. It is constant on $\{s_3\}$, $\{s_4\}$, and $\{s_5s_6\}$ (both severe), but on the block $\{s_1s_2\}$ we have $q(s_1)=\text{well}\ne\text{mild}=q(s_2)$. Hence $q$ is **not** answerable from $\{L,F\}$, and the unresolved-pair set (Definition 5.5) is
$$
U(\{L,F\},q)=\{(s_1,s_2),(s_2,s_1)\}.
$$
The states $s_1,s_2$ agree on both available views yet differ in diagnosis: this is the exact locus of missing information.

**Marginal value of $A$.** The remedy must separate the unresolved pair. Since $A(s_1)=\mathrm{y}\ne\mathrm{o}=A(s_2)$, the view $A$ separates $(s_1,s_2)$, so by Theorem 6.5(3) adding $A$ makes $q$ answerable. Indeed the profiles $(L,F,A)$ are pairwise distinct across all six states, so
$$
\sigma(\{L,F,A\})=\top\quad(\text{the discrete partition}),
$$
and $q$ factors trivially. Note the audit did not require examining $q$ against every subset of views: by Corollary 6.8 it reduced to comparing one partition, $\sigma(S)$, against $\ker(q)$, and the fix was dictated by one pair.

The example also illustrates why content is domain-relative (Definition 4.1): had $D$ excluded $s_2$, the pair would not exist and $\{L,F\}$ would already answer $q$. Sufficiency is a property of data *against a contrast domain and a question*, never of data alone.

---

## 12. Worked example B: relational dependency theory recovered

This example validates the kernel against an established theory: functional dependencies in the relational model. The claim is that answerability, the induced quotient, and the universal property specialize exactly to functional determination, the agreement partition, and projection — and that Armstrong's inference rules become lattice identities.

**Setup.** Fix a relation instance: a finite set $D$ of tuples over an attribute set $\mathcal U$. For $X\subseteq\mathcal U$, the **projection view** is $\pi_X:D\to\prod_{a\in X}\mathrm{dom}(a)$, $t\mapsto t{\restriction}X$. Its kernel $\ker(\pi_X)$ is the classical *agreement partition*: two tuples share a block iff they agree on every attribute in $X$.

**Determination is answerability.** A functional dependency $X\to Y$ holds in the instance iff any two tuples agreeing on $X$ agree on $Y$, i.e. iff $\pi_Y$ is constant on the blocks of $\ker(\pi_X)$. By Fact 3.2 and Definition 5.4 this is exactly
$$
X\to Y \quad\Longleftrightarrow\quad \pi_Y \text{ answerable from } \{\pi_X\}
\quad\Longleftrightarrow\quad \ker(\pi_Y)\le\ker(\pi_X),
$$
that is, the $X$-partition refines the $Y$-partition. Determination *is* answerability; the "closer to determined" ordering is refinement.

**Content of a projection set.** For a set of attributes viewed as $S=\{\pi_{X_1},\dots,\pi_{X_k}\}$, Definition 5.2 and (3.1) give
$$
\sigma(S)=\bigvee_i \ker(\pi_{X_i})=\ker(\pi_{X_1\cup\cdots\cup X_k}),
$$
the agreement partition of the union of attributes. By Theorem 6.7(3), the induced quotient is (isomorphic to) the image of the joint projection $\pi_{\bigcup_i X_i}$: the set of distinct $(\bigcup_i X_i)$-value profiles realized in the instance. The kernel's "free lossless summary of the data" is, here, the projected relation.

**Armstrong's axioms as lattice facts.** Writing $\ker_X:=\ker(\pi_X)$ and using $\ker_{X\cup Z}=\ker_X\vee\ker_Z$:

> **Proposition 12.1 (soundness of the Armstrong rules).** The three Armstrong rules hold as identities in $\mathrm{Part}(D)$:
>
> - *Reflexivity:* if $Y\subseteq X$ then $\ker_Y\le\ker_X$, so $X\to Y$.
> - *Augmentation:* if $\ker_Y\le\ker_X$ then $\ker_{Y\cup Z}=\ker_Y\vee\ker_Z\le\ker_X\vee\ker_Z=\ker_{X\cup Z}$, so $XZ\to YZ$.
> - *Transitivity:* if $\ker_Z\le\ker_Y$ and $\ker_Y\le\ker_X$ then $\ker_Z\le\ker_X$, so $X\to Z$.
>
> *Proof.* Reflexivity: $\pi_X$ pairs $\pi_Y$ with $\pi_{X\setminus Y}$, so $\ker_X=\ker_Y\vee\ker_{X\setminus Y}\ge\ker_Y$. Augmentation and transitivity are monotonicity of $\vee$ and transitivity of $\le$, as displayed. $\square$

The rules are sound for the fixed view family. Completeness of Armstrong inference over all relational models is a separate classical theorem [Armstrong 1974], which this lattice proof does not reprove: it does not show that every dependency true in a given instance follows by the rules from an arbitrarily chosen basis. What the lattice view does show is that, in a fixed instance, the agreement partitions $\{\ker_X\}_{X\subseteq\mathcal U}$ form a join-subsemilattice of $\mathrm{Part}(D)$ (since $\ker_{X\cup Z}=\ker_X\vee\ker_Z$) and that the dependencies holding in the instance are exactly its order. The partition view of dependencies is the basis of dependency-discovery algorithms [Huhtala et al. 1999], and its appearance here as a special case is evidence that the kernel's primitives are the right ones: a theory built for heterogeneous views specializes, with no adjustment, to the attribute-incidence case that classical dependency theory and Formal Concept Analysis already treat [Armstrong 1974; Ganter & Wille 1999].

---

## 13. Worked example C: observability of a finite machine

This example validates the kernel against control- and automata-theoretic observability (cf. Kalman 1963; Nerode 1958): the induced quotient of the output-history views is the observable-state partition, and answerability of "which state?" is observability.

**Setup.** Let a deterministic Moore machine have state set $D=\{p,q,r\}$, a single input letter with transition $\delta:D\to D$ given by $p\mapsto q$, $q\mapsto r$, $r\mapsto r$, and output $\lambda:D\to\{0,1\}$ with $\lambda(p)=\lambda(q)=0$, $\lambda(r)=1$. The **depth-$k$ view** is the output observed after $k$ steps,
$$
v_k:=\lambda\circ\delta^{\,k}:D\to\{0,1\},\qquad k=0,1,2,\dots
$$
Each $v_k$ is a legitimate view on $D$; the available family after observing horizon $H$ is $S_H=\{v_0,\dots,v_H\}$.

**Computing the observable quotient.**
$$
v_0:\ p\mapsto0,\ q\mapsto0,\ r\mapsto1
\ \Rightarrow\ \ker(v_0)=\{\,pq\mid r\,\};
$$
$$
v_1=\lambda\circ\delta:\ p\mapsto\lambda(q)=0,\ q\mapsto\lambda(r)=1,\ r\mapsto\lambda(r)=1
\ \Rightarrow\ \ker(v_1)=\{\,p\mid qr\,\}.
$$
Then
$$
\sigma(S_1)=\ker(v_0)\vee\ker(v_1)=\{\,pq\mid r\,\}\vee\{\,p\mid qr\,\}=\{\,p\mid q\mid r\,\}=\top .
$$
The three states become pairwise distinguishable at horizon $1$: the machine is observable, and the question "which state?" (the identity question $\mathrm{id}:D\to D$, with $\ker(\mathrm{id})=\top$) is answerable from $S_1$ by Proposition 5.6.

**Reading the kernel notions in automata terms.** The induced quotient $\sigma(S_H)$ is exactly the partition that identifies states not separable within horizon $H$; its stabilization $\sigma(S_\infty)$ is the Nerode/observability partition, and the machine is minimal/observable iff $\sigma(S_\infty)=\top$. Unresolved pairs (Definition 5.5) for the identity question are precisely the *indistinguishable state pairs*; Theorem 6.5 says a longer horizon helps exactly when a newly observed output separates some still-merged pair — the partition-refinement step of state-minimization algorithms [Hopcroft & Ullman 1979]. The observability special case of the kernel thus coincides with the classical construction, and control-theoretic observability [Kalman 1963] is its dynamical-state instance.

Taken together, Examples A–C show the kernel is neither vacuous nor ad hoc: two of the three instances recover established theories on the nose, and the third yields the operationally correct diagnosis-and-remedy. With the kernel thus anchored, the remainder of Part II relaxes canonical registration.

---

## 14. The admissibility layer: registered partitions and admissible ceilings

Standing assumption (A3) fixed registration to the canonical $\kappa^{\mathrm{can}}_v(y)=v^{-1}(y)$, which by Lemma 4.7 is the most informative sound registration. Real interpreters — bounded decoders, invariant readouts, resource-limited extractors — cannot always realize it. This section relaxes (A3): registration is henceforth chosen from an admissibility class, and the content it induces is studied as that class varies. The development stays exact and deterministic; assumptions (A1), (A2), (A4), (A5) remain in force.

> **Convention (finiteness of view sets).** From this point through the end of Part III, all view sets $S, T \subseteq V$ are finite unless explicitly stated otherwise: Definition 14.3 assigns ceilings to finite sets only, and the joint notions below are defined through them. The one systematic exception is recorded where it occurs — the separable adjunction (Theorem 15.1) involves only singleton ceilings and holds for arbitrary $S \subseteq V$.

### 14.1 The partition induced by a registration

> **Definition 14.1.** For a view $v$ and a registration $\kappa_v:Y_v\to\Phi_D$, the **registered partition** is
> $$
> \rho(\kappa_v):=\ker(\kappa_v\circ v)\in\mathrm{Part}(D),
> $$
> the partition of $D$ by equality of registered pieces: $Z\sim Z'$ iff $\kappa_v(v(Z))=\kappa_v(v(Z'))$.

> **Lemma 14.2 (registration is distinction–non-increasing).** For every registration $\kappa_v$,
> $$
> \rho(\kappa_v)\le\ker(v),
> $$
> with equality for the canonical registration: $\rho(\kappa^{\mathrm{can}}_v)=\ker(v)$.
>
> *Proof.* The map $\kappa_v\circ v$ factors through $v$ by construction, so $v(Z)=v(Z')\Rightarrow\kappa_v(v(Z))=\kappa_v(v(Z'))$; hence $\ker(v)$ refines nothing beyond $\rho(\kappa_v)$, i.e. $\rho(\kappa_v)\le\ker(v)$. For canonical, $\kappa^{\mathrm{can}}_v(v(Z))=v^{-1}(v(Z))=[Z]_{\ker(v)}$, so the induced partition is $\ker(v)$ itself. $\square$

Lemma 14.2 is the exact counterpart, at the level of distinctions, of Lemma 4.7's statement at the level of pieces: registration can only *discard* the distinctions a view already draws, never manufacture new ones, and canonical registration discards none. Everything downstream lives in the interval $[\bot,\ker(v)]$.

### 14.2 Admissibility structures

The kernel used one registration per view; admissibility allows a *class* and, crucially, must also say what is admissible on *compound* views, because that is where the theory's new content lies. We formulate admissibility directly at the level of registered partitions, since by Lemma 14.2 the partition is what determines content.

> **Definition 14.3.** For a view family $V$ on $D$, an **admissibility structure** $K$ assigns to each finite $T\subseteq V$ an **admissible ceiling**
> $$
> \gamma_K(T)\in\mathrm{Part}(D),
> $$
> subject to:
>
> - **(K0) Grounding.** $\gamma_K(\varnothing)=\bot$.
> - **(K1) Boundedness.** $\gamma_K(T)\le\sigma(T)$ for all $T$ (no registration invents distinctions its raw material does not draw; Lemma 14.2).
> - **(K2) Realizability closure.** For each $T$, every $\rho\le\gamma_K(T)$ is itself admissible on $T$; i.e. an admissible reading may always be coarsened. Equivalently, the admissible partitions on $T$ form the principal ideal ${\downarrow}\gamma_K(T)$.
>
> $K$ is **monotone** if $T\subseteq T'\Rightarrow\gamma_K(T)\le\gamma_K(T')$: enlarging the raw material never lowers the admissible ceiling.

(K2) records that admissibility caps *resolving power*, not the freedom to ignore: given an admissible reading one may always throw information away, so the admissible partitions on a fixed $T$ are exactly those below a top element $\gamma_K(T)$. The content of an admissibility structure therefore lies not in the per-$T$ ideals but in *how the ceilings on different $T$ relate* — the assignment $T\mapsto\gamma_K(T)$ as a whole. Monotonicity is optional and marks a fault line examined in §16.

That the axioms describe realizable structure, rather than stipulating it, is guaranteed by the following lemma.

> **Lemma 14.4 (realization of admissible partitions).** Let $T \subseteq V$ be finite, let $c_T = \langle v \rangle_{v \in T} : D \to \prod_{v \in T} Y_v$ be the compound view, and let $\rho \le \sigma(T)$. Then the registration defined on realized profiles by
> $$
> \kappa\big(c_T(Z)\big) = [Z]_\rho
> $$
> (extended by the null value $D$ off the image) is well defined, sound, and has registered partition $\rho(\kappa) = \rho$. Together with Lemma 14.2 applied to the compound view, the partitions realizable by sound registrations of $c_T$ are therefore exactly the principal ideal ${\downarrow}\,\sigma(T)$: axioms (K1)–(K2) delimit precisely the realizable range, and nothing in Definition 14.3 is stipulative beyond the choice of ceiling.
>
> *Proof.* Well-definedness: $c_T(Z) = c_T(Z')$ means $Z \sim_T Z'$, i.e. $[Z]_{\sigma(T)} = [Z']_{\sigma(T)}$; since $\rho \le \sigma(T)$, every $\sigma(T)$-block lies inside a $\rho$-block, so $[Z]_\rho = [Z']_\rho$. Soundness: $Z \in [Z]_\rho$. Registered partition: $\kappa(c_T(Z)) = \kappa(c_T(Z'))$ iff $[Z]_\rho = [Z']_\rho$, so $\rho(\kappa) = \ker(Z \mapsto [Z]_\rho) = \rho$. The converse bound $\rho(\kappa) \le \ker(c_T) = \sigma(T)$ for every registration is Lemma 14.2. $\square$

Lemma 14.4 grounds each ceiling *individually*. Whether a family of ceilings is *simultaneously* realizable by one coherent class of decoders is a further question, and it is exactly where monotonicity acquires operational content.

> **Proposition 14.4′ (simultaneous realization: the operational content of monotonicity).** An admissibility structure $K$ induces, for each finite $T \subseteq V$, the registration class
> $$
> \mathcal{K}(T) \;=\; \{\, \kappa \ \text{sound on the compound view } c_T \;:\; \rho(\kappa) \le \gamma_K(T) \,\},
> $$
> nonempty and realizing its ceiling by Lemma 14.4, and a down-set in resolving power by construction. Say the family $\{\mathcal{K}(T)\}_T$ is **closed under restriction** if for all finite $T' \subseteq T$ and every $\kappa' \in \mathcal{K}(T')$, the composite $\kappa' \circ \mathrm{pr}_{T'} \in \mathcal{K}(T)$, where $\mathrm{pr}_{T'} : \prod_{v \in T} Y_v \to \prod_{v \in T'} Y_v$ is the coordinate projection — i.e., a reading admissible on part of the data remains admissible on all of it. Then
> $$
> \{\mathcal{K}(T)\}_T \ \text{is closed under restriction} \quad\iff\quad K \ \text{is monotone}.
> $$
>
> *Proof.* First note $\kappa' \circ \mathrm{pr}_{T'}$ is sound on $c_T$ (since $\mathrm{pr}_{T'} \circ c_T = c_{T'}$ and $\kappa'$ is sound) with $\rho(\kappa' \circ \mathrm{pr}_{T'}) = \ker(\kappa' \circ c_{T'}) = \rho(\kappa')$. ($\Leftarrow$) $\rho(\kappa' \circ \mathrm{pr}_{T'}) = \rho(\kappa') \le \gamma_K(T') \le \gamma_K(T)$, the last inequality by monotonicity. ($\Rightarrow$) By Lemma 14.4 choose $\kappa' \in \mathcal{K}(T')$ with $\rho(\kappa') = \gamma_K(T')$; closure under restriction gives $\gamma_K(T') = \rho(\kappa' \circ \mathrm{pr}_{T'}) \le \gamma_K(T)$. $\square$

Monotonicity is thereby not a bare order axiom but a coherence law *across* view sets: it characterizes exactly the ceiling families that a single class of decoders, closed under ignoring part of its input, realizes simultaneously. This — not any inequality on ceilings of unions — is the correct cross-$T$ constraint at this layer. A subadditivity axiom $\gamma_K(T \cup T') \le \gamma_K(T) \vee \gamma_K(T')$ would, by contrast, combine with monotonicity to force separability (Definition 15.3) and legislate the registration anomaly of §16 out of existence; the theory deliberately refrains.

Two canonical instances:

- **Full admissibility** $K^{\mathrm{can}}$: $\gamma_{K^{\mathrm{can}}}(T)=\sigma(T)$. This is the kernel; canonical registration is admissible everywhere. It is monotone.
- **Ceiling from a resolving structure.** Fix, for each view $v$, a partition $C_v\in\mathrm{Part}(D)$ (the finest distinctions the decoder can draw from $v$'s presentations) and, for compound views, a ceiling $C_{\langle T\rangle}$; set $\gamma_K(T)=C_{\langle T\rangle}\wedge\sigma(T)$. Invariance ceilings (§16) are of this form.

### 14.3 Separable and joint admissible content

An admissible interpreter facing a view set $S$ has two regimes: register each view separately (subject to per-view ceilings) and then combine the pieces, or register the compound view jointly (subject to the compound ceiling). The kernel conflated these; admissibility splits them.

> **Definition 14.5.** For $S\subseteq V$ under an admissibility structure $K$:
>
> - the **separable content** is
> $$
> \sigma^{\mathrm{sep}}_K(S)=\bigvee_{v\in S}\gamma_K(\{v\});
> $$
>
> - the **joint content** is
> $$
> \sigma^{\mathrm{jnt}}_K(S)=\gamma_K(S).
> $$
> A question $q$ is **separably (resp. jointly) answerable from $S$ under $K$** iff $\ker(q)\le\sigma^{\mathrm{sep}}_K(S)$ (resp. $\le\sigma^{\mathrm{jnt}}_K(S)$).

> **Proposition 14.6 (bracketing and ordering).** For every $S\subseteq V$:
> $$
> \bot\ \le\ \sigma^{\mathrm{sep}}_K(S)\ \le\ \sigma^{\mathrm{jnt}}_K(S)\ \le\ \sigma(S),
> $$
> where the second inequality requires $K$ monotone, and the outer two hold for every $K$. Under full admissibility both middle terms collapse to $\sigma(S)$.
>
> *Proof.* Left and right: (K0)/(K1) give $\bot\le\gamma_K(\{v\})$ and $\gamma_K(S)\le\sigma(S)$; joins of terms $\le\sigma(S)$ stay $\le\sigma(S)$. Middle: if $K$ is monotone then $\gamma_K(\{v\})\le\gamma_K(S)$ for each $v\in S$, so the join $\sigma^{\mathrm{sep}}_K(S)\le\gamma_K(S)=\sigma^{\mathrm{jnt}}_K(S)$. Collapse under $K^{\mathrm{can}}$: $\gamma(\{v\})=\ker(v)$, whose join is $\sigma(S)=\gamma(S)$. $\square$

Proposition 14.6 is the promised bracket: admissible content sits between "nothing" and the kernel's canonical content, and the separable/joint pair sits inside that bracket whenever the structure is monotone. The next two sections determine what the kernel theorems become in this bracket, and where they break.

---

## 15. Fate of the kernel theorems under admissibility

We take $\sigma^{\mathrm{sep}}_K$ and $\sigma^{\mathrm{jnt}}_K$ in turn and ask which of Theorems 6.2, 6.4, 6.5, 6.7 survive.

### 15.1 The adjunction survives for separable content

> **Theorem 15.1 (T1 relativized).** Fix an admissibility structure $K$ (neither monotonicity nor the finiteness convention of §14 is required: separable content depends only on the singleton ceilings, so the statement holds for arbitrary $S \subseteq V$). Define $\tau_K:\mathrm{Part}(D)\to\mathcal P(V)$ by $\tau_K(\pi)=\{v\in V:\gamma_K(\{v\})\le\pi\}$. Then $(\sigma^{\mathrm{sep}}_K,\tau_K)$ is a Galois connection:
> $$
> \sigma^{\mathrm{sep}}_K(S)\le\pi\iff S\subseteq\tau_K(\pi).
> $$
> Consequently the full content of Theorem 6.2 holds with $\gamma_K(\{v\})$ in place of $\ker(v)$: $\sigma^{\mathrm{sep}}_K$ preserves unions as joins, $\tau_K\sigma^{\mathrm{sep}}_K$ is a closure operator on $\mathcal P(V)$, and the admissibly-achievable quotients $\mathrm{Im}\,\sigma^{\mathrm{sep}}_K$ form a complete lattice.
>
> *Proof.* $\sigma^{\mathrm{sep}}_K(S)=\bigvee_{v\in S}\gamma_K(\{v\})\le\pi$ iff $\gamma_K(\{v\})\le\pi$ for all $v\in S$ iff $S\subseteq\tau_K(\pi)$. The consequences are Fact 3.4, exactly as in Theorem 6.2, since $\sigma^{\mathrm{sep}}_K$ is again a join over per-view quantities. $\square$

The reason the adjunction is robust is structural: $\sigma^{\mathrm{sep}}_K$ is built as a join over singleton contributions $\gamma_K(\{v\})$, and any such map is automatically a left adjoint. Restricting registration merely replaces each generator $\ker(v)$ by a coarser generator $\gamma_K(\{v\})$; the order-theoretic scaffolding is untouched.

Likewise Theorems 6.4 and 6.5 survive verbatim for $\sigma^{\mathrm{sep}}_K$: the separably answerable questions form the principal ideal ${\downarrow}\sigma^{\mathrm{sep}}_K(S)$, and a view $w$ separably helps $q$ iff $\gamma_K(\{w\})$ separates some pair unresolved by $\sigma^{\mathrm{sep}}_K(S)$. The proofs are those of Part I with the generators renamed. The universal property (Theorem 6.7) becomes: $\sigma^{\mathrm{sep}}_K(S)$ is terminal among consolidations realizable by admissible *per-view* registration.

### 15.2 What genuinely changes: joint content is not a join over views

The joint content $\sigma^{\mathrm{jnt}}_K(S)=\gamma_K(S)$ is, in general, **not** expressible as a join of singleton contributions, and this is where the kernel's coherence law fails.

> **Proposition 15.2 (fate of Proposition 6.3).** For a monotone $K$ and $S\subseteq V$,
> $$
> \sigma^{\mathrm{sep}}_K(S)\ \le\ \sigma^{\mathrm{jnt}}_K(S),
> $$
> and the inequality can be strict. Under full admissibility it is an equality (Proposition 6.3). Consequently $\sigma^{\mathrm{jnt}}_K$ need not preserve unions and need not admit an upper adjoint.
>
> *Proof.* The inequality is Proposition 14.6. Strictness is exhibited in §16. If $\sigma^{\mathrm{jnt}}_K$ preserved unions it would satisfy $\gamma_K(S)=\bigvee_{v\in S}\gamma_K(\{v\})=\sigma^{\mathrm{sep}}_K(S)$ for all $S$; a strict instance refutes this and, by Fact 3.4(ii), refutes the existence of an upper adjoint. $\square$

So the kernel identity "register-then-combine $=$ combine-then-register" (Proposition 6.3), which underwrote both the adjunction for joint content and the coincidence of the separable and joint notions, is exactly the statement that $K$ is **separable**:

> **Definition 15.3.** $K$ is **separable at $S$** if $\sigma^{\mathrm{sep}}_K(S)=\sigma^{\mathrm{jnt}}_K(S)$, and **separable** if this holds for all $S$. The **registration anomaly** at $S$ is, for monotone $K$, the interval
> $$
> \Delta_K(S)=\big[\,\sigma^{\mathrm{sep}}_K(S),\ \sigma^{\mathrm{jnt}}_K(S)\,\big]\subseteq\mathrm{Part}(D),
> $$
> nontrivial (non-degenerate) exactly when the endpoints disagree. The interval typing is deliberate: intervals in a complete lattice restrict, intersect, and compose, which is the raw material an obstruction theory needs (§16.4), whereas a bare pair has no algebra. For non-monotone $K$ the two contents may be incomparable, and the anomaly is then recorded as the unordered pair of endpoints.

> **Corollary 15.4 (finite-view adjunction criterion).** Let $V$ be finite and $K$ monotone. The following are equivalent: (i) $K$ is separable; (ii) $\sigma_K^{\mathrm{jnt}}:\mathcal P(V)\to\mathrm{Part}(D)$ preserves all unions, including the empty union; (iii) it has a right adjoint; (iv) it equals $\sigma_K^{\mathrm{sep}}$.
>
> *Proof.* Separability is (iv). The singleton-generated formula in (iv) preserves unions and has the right adjoint of Theorem 15.1. Union preservation gives that formula by expressing any subset as the union of its singletons. A left adjoint preserves unions. Grounding follows from the raw-content bound at the empty set. For infinite $V$, the finite-subset version characterizes finite-union preservation; the right-adjoint statement applies to the arbitrary-join extension on $\mathcal P(V)$, not in general to a map with domain $\mathcal F(V)$. $\square$

The fate of T1 is thus sharp. **For separable content the adjunction always holds; for joint content it holds iff the admissibility structure is separable, and the obstruction is exactly the registration anomaly $\Delta_K$.** Full admissibility (the kernel) is separable, which is why Part I never saw the anomaly. Any strictly sub-canonical $K$ that reads the joint more finely than the combination of its parts breaks separability — and that, far from being pathological, is the generic and interesting case, as the next section shows.

---

## 16. The registration anomaly, and where it points

### 16.1 A worked non-separable structure: invariance and parity

We give an explicit $S$ and $K$ with $\sigma^{\mathrm{sep}}_K(S)=\bot$ but $\sigma^{\mathrm{jnt}}_K(S)$ nontrivial — a maximal anomaly, in which separate admissible registration recovers *nothing* while joint admissible registration answers a real question.

**Setup.** Let $D=\{00,01,10,11\}$, thought of as pairs of bits, and let the group $G=\{\mathrm{id},\phi\}$ act on $D$ by the global bit-flip $\phi:00\leftrightarrow11,\ 01\leftrightarrow10$. Two views expose the coordinates,
$$
v(b_1b_2)=b_1,\qquad w(b_1b_2)=b_2,
$$
with $\ker(v)=\{00\,01\mid10\,11\}$ and $\ker(w)=\{00\,10\mid01\,11\}$, so $\sigma(\{v,w\})=\top$. The target question is parity, $q(b_1b_2)=b_1\oplus b_2$, whose content is $\ker(q)=\{00\,11\mid01\,10\}$.

**Admissibility by invariance.** Let the decoder be required to produce readings invariant under $G$: an admissible registered partition must have $G$-stable blocks. The finest $G$-invariant partition of $D$ is the orbit partition
$$
P_G=\{\,00\,11\mid01\,10\,\},
$$
and we take the invariance ceiling $\gamma_K(T)=P_G\wedge\sigma(T)$ (an instance of the resolving-structure ceiling of §14.2; one checks (K0)–(K2) and monotonicity hold, since $\wedge\sigma(T)$ is monotone in $T$ and $P_G$ is fixed).

**Separate content vanishes.** For the single view $v$,
$$
\gamma_K(\{v\})=P_G\wedge\ker(v)=\{00\,11\mid01\,10\}\wedge\{00\,01\mid10\,11\}.
$$
The meet is the coarsest common coarsening: $00\sim11$ (from $P_G$) and $00\sim01$, $10\sim11$ (from $\ker v$) chain all four elements together, so $\gamma_K(\{v\})=\bot$. By symmetry $\gamma_K(\{w\})=\bot$, hence
$$
\sigma^{\mathrm{sep}}_K(\{v,w\})=\bot\vee\bot=\bot.
$$
Neither coordinate, read invariantly, distinguishes anything: a flip-invariant reading of $b_1$ alone cannot tell $b_1=0$ from $b_1=1$, since $\phi$ swaps them.

**Joint content answers parity.** For the compound view $\langle v,w\rangle$, $\sigma(\{v,w\})=\top$, so
$$
\sigma^{\mathrm{jnt}}_K(\{v,w\})=\gamma_K(\{v,w\})=P_G\wedge\top=P_G=\{00\,11\mid01\,10\}=\ker(q).
$$
Parity is jointly answerable under $K$, though nothing is separably answerable. The anomaly is maximal:
$$
\Delta_K(\{v,w\})=[\,\bot,\ \ker(q)\,],\qquad \sigma^{\mathrm{sep}}_K(\{v,w\}) < \sigma^{\mathrm{jnt}}_K(\{v,w\}).
$$

The phenomenon is the informational core of parity secret-sharing [Shamir 1979]: each share (coordinate) individually carries nothing about the secret (parity), while the shares jointly determine it. The kernel could not express this, because canonical registration is separable; admissibility is precisely the added structure that makes "jointly informative, separately null" a representable — and quantifiable — state of affairs. In measurement-theoretic terms the invariance ceiling is the *meaningfulness* criterion [Krantz, Luce, Suppes & Tversky 1971; Narens 2002]: admissible content is invariant content, and the anomaly states that meaningful joint content can strictly exceed the join of meaningful marginal contents.

### 16.2 The opposite regime, and why monotonicity is the divide

Strictness in Proposition 15.2 assumed monotonicity, which delivered $\sigma^{\mathrm{sep}}_K\le\sigma^{\mathrm{jnt}}_K$. Non-monotone admissibility can invert it. Consider a decoder with an **output budget**: it emits at most one bit regardless of input, so every admissible reading has at most two blocks. Note that the budget constraint by itself carves out a down-set of $\mathrm{Part}(D)$ that is *not* a principal ideal — there is no finest two-block partition below $\top$ — so a budget-limited decoder is modelled, within Definition 14.3, by an admissibility structure that makes a definite choice of ceiling inside the budget. (Down-sets of $\mathrm{Part}(D)$ form a complete lattice under inclusion, so a budget class can always be represented as a lower set, with ceilings — principal down-sets — as the representable case. The graded theory meets the same issue twice more; Remark 24.6 records what the lower-set representation does and does not provide.) In the parity setup, take $\gamma_K(\{v\})=\ker(v)$ and $\gamma_K(\{w\})=\ker(w)$ (each already two-block), and for the compound view let the decoder spend its bit on the first coordinate: $\gamma_K(\{v,w\})=\ker(v)$. Axioms (K0)–(K2) hold, but monotonicity fails: $\gamma_K(\{w\})=\ker(w)\not\le\ker(v)=\gamma_K(\{v,w\})$. Then
$$
\sigma^{\mathrm{sep}}_K(\{v,w\})=\ker(v)\vee\ker(w)=\top,
\qquad
\sigma^{\mathrm{jnt}}_K(\{v,w\})=\ker(v)<\top:
$$
separate content strictly exceeds joint content.

The two regimes sit on opposite sides of the kernel's equality:
$$
\underbrace{\sigma^{\mathrm{sep}}_K\ \le\ \sigma^{\mathrm{jnt}}_K}_{\text{monotone: guaranteed (Prop. 14.6)}}
\qquad\text{vs.}\qquad
\underbrace{\sigma^{\mathrm{jnt}}_K\ \le\ \sigma^{\mathrm{sep}}_K}_{\text{non-monotone: possible, not forced}},
$$
with equality — Proposition 6.3 — exactly at separable structures, of which full admissibility is one. The precise statement is asymmetric: **monotonicity rules out the resource-limited inversion** $\sigma^{\mathrm{jnt}}_K < \sigma^{\mathrm{sep}}_K$ (Proposition 14.6); when monotonicity fails, budget-type inversions become possible, though not forced — a non-monotone structure may order the two contents either way, leave them equal, or leave them incomparable, and may do so differently at different view sets. Both regimes are real; the kernel occupies the seam between them.

### 16.3 Un-collapsing encoded / extractable / used

The anomaly lets us separate notions the kernel fused. Reading Part I's canonical content as *what is present in principle* and admissible content as *what a legitimate decoder recovers*, Proposition 14.6 stratifies content over $S$:
$$
\underbrace{\sigma(S)}_{\text{encoded}}\ \ge\ \underbrace{\sigma^{\mathrm{jnt}}_K(S)}_{\text{extractable}}\ \ge\ \underbrace{\sigma^{\mathrm{sep}}_K(S)}_{\text{separably extractable}}\ \ge\ \underbrace{\vphantom{\sigma^{\mathrm{jnt}}}\ \cdots\ }_{\text{used}}
$$
(the monotone case). *Encoded* is what the views draw at all; *extractable* is what admissible joint registration recovers; *separably extractable* is what admissible per-view registration recovers; *used* — content that additionally drives a downstream process — is a further coarsening requiring a model of that process and is deferred (it modifies neither P1–P6 nor the admissibility layer but adds dynamics; §8, beyond H2). The distinctions *encoded $\ne$ extractable $\ne$ separably extractable* are now theorems, witnessed by strict instances such as §16.1, rather than informal slogans. This is the stratification the admissibility layer was introduced to provide: in particular it separates "the representation contains the distinction" ($\le\sigma$) from "an admissible decoder can draw it" ($\le\sigma^{\mathrm{jnt}}_K$), which is the exact ambiguity that undermines interpretability claims resting on unconstrained probes.

### 16.4 The anomaly as the entry point to gluing

For monotone $K$, $T\mapsto\gamma_K(T)$ is covariant in the view set. Separability says that its singleton contributions jointly attain its value on $T$. Locally admissible readings always combine under monotonicity; the possible failure is that those combinations do not dominate all joint readings (Proposition 36.3). Thus the interval $\Delta_K$ is a cofinality defect, not by itself a failure of the sheaf axiom for a Set-valued presheaf.

Part V develops positive union covers, orbit graphs, and witness sets. Appendix D.8 states the additional distributivity condition needed for join covers on achievable partitions to form a site. Appendix D.12 shows why the parity admissibility anomaly does not imply contextuality of the ordinary marginal empirical model. These distinctions preserve the local-to-global motivation without identifying different gluing problems.

---

## 17. Summary of Part II

The worked examples show that the kernel carries out a diagnostic audit and reproduces functional dependency theory and observability without adjustment. The admissibility layer proves that ceilings are realizable (Lemma 14.4), that monotonicity is coherence across view sets (Proposition 14.4′), that admissible content is bracketed by canonical content (Proposition 14.6), and that the kernel's adjunction survives for separable content and, for joint content, exactly at separable structures (Theorem 15.1, Corollary 15.4). The registration anomaly $\Delta_K$ is the obstruction, and §16 realizes it in both directions.

Two points are deliberately left for later. The anomaly is a failure of combined local readings to reach the resolving power of joint readings; it is not a failure to combine local readings at all, which always succeeds (Proposition 36.3). Its local-to-global analysis is the subject of Part V, which also shows when join covers form a site (Appendix D.8).

**References added in Part II** (see Part I, §References, for those already cited):

- Armstrong, W. W. (1974). "Dependency Structures of Data Base Relationships." *Information Processing 74* (Proc. IFIP Congress), 580–583. North-Holland.
- Hopcroft, J. E., and Ullman, J. D. (1979). *Introduction to Automata Theory, Languages, and Computation.* Addison-Wesley.
- Huhtala, Y., Kärkkäinen, J., Porkka, P., and Toivonen, H. (1999). "TANE: An Efficient Algorithm for Discovering Functional and Approximate Dependencies." *The Computer Journal* 42(2), 100–111.
- Nerode, A. (1958). "Linear Automaton Transformations." *Proceedings of the American Mathematical Society* 9(4), 541–544.
- Shamir, A. (1979). "How to Share a Secret." *Communications of the ACM* 22(11), 612–613.
