# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part XI: The Information Algebra and the Global Collapse

---

## 82. Purpose: the last hook is the last assumption

One hook and one assumption remain, and the audit preceding this part found them to be the same promise. Hook H5 — multiple domains and full information algebra — was typed in §8 as the extension that "relaxes A5," the kernel's standing restriction to a single fixed contrast domain; and §8 fixed its brief exactly: reintroduce the ambient class of targets and a family of related contrast domains, and establish "coherence of registration with extraction, and functoriality of $\sigma$ along maps between contrast domains (restriction, refinement, and coarsening of $D$), extending Theorem 6.2." Proposition 6.11 already supplies more than a germ: over one domain, the saturated-set pieces form a complete **labeled idempotent information algebra** over the achievable-quotient lattice, with combination as intersection, focusing as Pawlak's upper approximation, and the whole structure functorial in the view family. What remains — and it is all that remains — is the *multi*-domain step, the fate of the algebra's axioms under the manuscript's relaxations, and the theorem toward which every part has been aimed.

Part XI establishes a finite generated-domain construction, subject to the common-scene hypothesis in Definition 83.4. Appendix A does not extend it automatically to arbitrary measurable domains. General extraction systems and unrestricted domain diagrams remain additional problems.

Section 83 supplies the deterministic transport calculus. Surjective pullback is an isomorphism onto a principal ideal and preserves nonempty ambient meets; factor products preserve the stated lattice operations; restriction preserves joins and is meet-lax. Prior-averaging channels onto a question is a separate operation, studied by Appendix D.4, and does not inherit all these identities. The resulting labeled saturated sets form the generalized set information algebra of Theorem 83.5; least supports require an additional ambient-meet-closure hypothesis.

Section 84 distinguishes the generalized set information algebra from a possible future graded algebra. Independent tensor combination can fail idempotency; Appendix D.3 characterizes exactly when it does. Separability is a cofinality condition for admissible exact readings, not their closure under combination.

Section 85 collects finite recovery results under their separate hypotheses. They do not establish a product of commuting extension axes. Sections 86–89 distinguish the proved finite construction from additional research questions; Appendix D supplies the finite closure results.

**Assumptions and conventions.** Finite nonempty domains and observation spaces remain in force. The common-scene representation requires specified surjections to the member domains. Deterministic pullback, trace, and factor products must be distinguished from prior-averaging of channels. Historical random-computation counts are not review-run certificates; Appendix B identifies the independently reproduced checks.

---

## 83. The multi-domain frame

> **Definition 83.1 (ambient class; carving; domain family).** Fix an ambient class $\Omega$ of targets — the universe from which contrast domains are carved (§2's deferred clause, now cashed). A **domain family** is a finite diagram $\mathcal{D}$ of contrast domains, each carrying its own view family, connected by generating morphisms of the three kinds H5 names:
> - **coarsening** $c_\pi : D \twoheadrightarrow D/\pi$ for $\pi \in \mathrm{Part}(D)$ — a question, promoted to a domain (the identification that makes Part VII's ledger functor, Definition 56.1, a *domain morphism*: prior-marginalization is coarsening along $\ker q$, with channels pushed forward by prior-averaging);
> - **restriction** $D' \hookrightarrow D$ for $\varnothing\ne D'\subseteq D$ — fewer live alternatives (conditioning; sub-cohorts); its reverse reading is **refinement**, traveling backward along a coarsening;
> - **joint domains** $D_1 \times D_2$ for distinct targets carved from $\Omega$ — the multi-target case, with factor-local view families (the constructor of Worked example I).
>
> Views transport contravariantly along coarsenings and restrictions (precomposition; trace) and factor-locally into products; graded families transport with them (pushforward of channels along $c_\pi$ with prior-averaging; restriction of kernels; factor tensors), coherence being preserved by marginality in each case.

> **Lemma 83.2 (transport calculus; the part's core).**
> 1. **(Coarsening: a lattice isomorphism onto an ideal.)** The pullback $c_\pi^* : \mathrm{Part}(D/\pi) \to \mathrm{Part}(D)$, $\bar\rho \mapsto \{c_\pi^{-1}(B) : B \in \bar\rho\}$, is an isomorphism of complete lattices onto the principal ideal ${\downarrow}\pi$ — the partitions coarser than $\pi$, i.e. the $\pi$-saturated ones. It preserves arbitrary joins and nonempty meets in the ambient partition lattice (all meets internally in the principal ideal): a transitive-closure chain downstairs lifts, because within-fiber moves are available by reflexivity, so $c_\pi^*(\bar\rho \wedge \bar\rho') = c_\pi^*\bar\rho \wedge c_\pi^*\bar\rho'$. Consequently expressions built from transported kernels, joins, and nonempty meets commute with this pullback. Internal top is $\pi$, so the empty ambient meet is excluded. This is deterministic pullback, not prior averaging of channels.
> 2. **(Restriction: exact on joins, lax on meets.)** The trace $\rho \mapsto \rho|_{D'}$ commutes with joins (blockwise intersection with $D'$ commutes with common refinement) but only laxly with meets, with the definite direction
> $$
> (\rho \wedge \rho')\big|_{D'} \;\le\; \rho|_{D'} \wedge \rho'|_{D'},
> $$
> strictly in general: on $D = \{1,2,3\}$ with $\rho = \{12 \mid 3\}$, $\rho' = \{1 \mid 23\}$, and $D' = \{1,3\}$, the $D$-meet is the single block (the chain runs through the excluded candidate $2$) while the traced meet is discrete. The mechanism is the manuscript's familiar one — a closure operator (transitive closure) failing to commute with a second operation — now in its third guise after the tolerance reflection of Proposition 22.3′ and the orbit reflection of Theorem 37.7: **chains of identification may pass through candidates that a restriction removes.**
> 3. **(Products: both operations factorize.)** For factor-local data, $(\rho_1 \times \rho_2) \vee (\rho_1' \times \rho_2') = (\rho_1 \vee \rho_1') \times (\rho_2 \vee \rho_2')$ and likewise for $\wedge$: a transitive-closure chain in the product interleaves into per-factor chains, holding the other coordinate fixed by reflexivity, and conversely per-factor chains concatenate. Hence contents *and ceilings* over factor-local views factorize — the lemma used ad hoc in Worked example I, established once.
>
> *Proof.* All three as sketched, each direction elementary; 1 and 3 additionally machine-verified on 200 randomized instances each, and 2's counterexample computed. $\square$

**Mathematical scope.** The ideal has top $\pi$, not ambient top $\top_D$; thus the empty meet is not preserved by its inclusion into $\mathrm{Part}(D)$. These transport statements concern deterministic pullback. Prior-averaging a channel onto a quotient is a different operation and does not preserve products or determinism (uniform XOR is a counterexample).

> **Proposition 83.3 (functoriality of $\sigma$; Theorem 6.2 extended; H5's first obligation).** Along the three constructors:
> $$
> \sigma_D\big(c_\pi^* \bar S\big) = c_\pi^*\big(\sigma_{D/\pi}(\bar S)\big), \qquad
> \sigma_{D'}\big(S|_{D'}\big) = \sigma_D(S)\big|_{D'}, \qquad
> \sigma_{D_1 \times D_2}(S_1 \sqcup S_2) = \sigma_{D_1}(S_1) \times \sigma_{D_2}(S_2)
> $$
> (Lemma 83.2 applied to joins of kernels), so registered content is functorial along restriction, refinement, and coarsening, and the adjunction of Theorem 6.2 transports: along a coarsening the entire T1 package restricts to the ideal ${\downarrow}\pi$; along products it factorizes. Moreover the focusing operator of Proposition 6.11 acquires its structural identity: $s_\rho$, the least $\rho$-saturated superset, **is the reflector in subset inclusion order** — the left adjoint of the inclusion $\Phi_\rho \hookrightarrow \mathcal{P}(D)$ — In the reversed information order it is a right adjoint; its orientation must be specified before applying an adjoint preservation law. Admissible content inherits the calculus with one caveat inherited from Lemma 83.2(2): ceilings involving meets transport exactly along coarsenings and products and only laxly along restrictions — restricting a scene can *sever* admissible identifications that chained through excluded candidates. $\square$

> **Definition 83.4 (the global algebra).** Let $\mathcal D$ be a finite family of domains equipped with specified surjections from a common finite scene $D^*$. Products are included only when the joint map onto the declared product is surjective (the "one scene, many questions, many targets" case; restrictions are treated as morphisms below rather than as generators). The **label lattice** $L \subseteq \mathrm{Part}(D^*)$ is the join-closed family generated by the $c^*$-pullbacks of the achievable-quotient lattices $\mathrm{Ach}(V_D)$, $D \in \mathcal{D}$; the **global pieces** are the labeled pairs
> $$
> \Phi^{\mathcal{D}} = \bigsqcup_{\rho \in L} \Phi_\rho, \qquad \Phi_\rho = \{(E, \rho) : E \subseteq D^* \ \rho\text{-saturated}\},
> $$
> with $d, \otimes, \Rightarrow$ as in Proposition 6.11 over $L$ — labels composing as there: $d(E,\rho) = \rho$, combination intersects sets and joins labels, focusing saturates and relabels — and **vacuous extension** of a piece of a member domain given by $c^*$-pullback of its saturated sets.

**Common-scene condition.** The common-scene construction assumes specified surjections from $D^*$ to every domain whose labels are pulled back. Two quotient maps need not induce a surjection onto their full Cartesian product: two copies of the same binary quotient give only the diagonal. Use the realized image as the joint domain, or assume/enlarge a common scene admitting the required surjections and restate its views. The factor-product laws of Lemma 83.2 apply to genuine Cartesian products; they are not a claim that arbitrary related targets vary independently.


> **Theorem 83.5 (multi-domain set algebra, qualified).** Use the join-closed label family $L$ of Definition 83.4. The labeled saturated sets form the generalized set information algebra of Proposition 6.11, with nontrivial focusing. For a surjection $c$, inverse image commutes with combination and focusing: $s_{c^*\rho}(c^{-1}E)=c^{-1}s_\rho(E)$. Restriction is combination-exact and focusing-lax: $s_{\rho|_{D'}}(E\cap D')\subseteq s_\rho(E)\cap D'$.
>
> Every piece has a supporting label. A **least** supporting label is guaranteed if $L$ is finite and closed under ambient meets; it is not guaranteed merely by join-closure. Choosing ambient-meet closure may add labels even in the single-domain case. With join-closure only, the single-domain label family is exactly $\mathrm{Ach}(V)$ under the standing finite convention.
>
> *Proof.* Apply the saturation identities of Proposition 6.11 and Appendix D.2. For surjective pullback a pulled-back block meets $c^{-1}E$ iff its image block meets $E$. For trace, a witness in $E\cap D'$ is also a witness in $E$, but the converse can fail. If a finite family of supporting labels is ambient-meet-closed, alternating equivalence chains preserve membership in $E$, proving support at their meet. Appendix D.2 gives the counterexample without meet closure. $\square$

> **Remark 83.6 (representability needs explicit functors).** The down-set completion is available for a poset, but its interaction with pullback, trace, and combination requires specified maps and a proof. Direct image followed by downward closure and inverse image are different constructions. No general commutation theorem or graded valuation-algebra repair is established here. In particular, the principal-down-set embedding does not preserve every existing join (Appendix D.6).

---

## 84. The algebra coordinate

> **Theorem 84.1 (independent combination and the algebra boundary).** The exact saturated-set construction is a generalized idempotent information algebra under the hypotheses of Proposition 6.11 and Theorem 83.5. For finite stochastic experiments, independent tensor product is well defined on Blackwell classes, associative and commutative up to equivalence, but need not be idempotent. BSC(0.3) is an explicit strict example, with deficiency to its independent double equal to 0.084 (Appendix B.6). Arbitrary supplied couplings do not define an operation on marginal Blackwell classes.
>
> *Proof.* The exact claim is the saturation calculus. Independent local simulators tensor to simulate independent products, so replacement by Blackwell-equivalent factors preserves the product class. Reassociation and exchange of output coordinates are invertible relabelings. Marginalization makes the independent double dominate one copy, and the certificate in Appendix B.6 proves strictness in the example. Finally, the equal-versus-independent bit coupling example has fixed marginal classes and different joint classes, ruling out an operation determined by those marginals for arbitrary supplied couplings. Appendix D.3 characterizes all tensor-idempotent finite experiments. No full graded valuation-algebra construction follows from these facts. ∎

> **Proposition 84.2 (separability is cofinality, not closure).** For monotone $K$, locally admissible exact readings are already closed under combination into the joint class (Proposition 36.3). Separability is the stronger assertion that combinations are **cofinal in resolving power** among joint readings, equivalently that the ceiling map preserves finite joins. It is not equivalent to ordinary closure of admissible pieces under combination.
>
> *Proof.* Combining readings with partitions bounded by $\gamma_K(T)$ and $\gamma_K(T')$ yields resolving power at most their join, which is at most $\gamma_K(T\cup T')$ by monotonicity. This proves closure regardless of separability. Ceiling-realizing block readings attain the join; cofinality holds exactly when that join equals the joint ceiling. The parity structure is closed in this sense but nonseparable. $\square$

---

## 85. The consolidated collapse theorem

> **Theorem 85.1 (scope of the recovery results).** The deterministic, fully admissible, correctly anchored presentation-only, static, single-domain specialization recovers the exact quotient theory of Part I. Its partition, answerability, and canonical-combination identities are Theorems 6.2–6.7. Finite stochastic experiments additionally recover the classical Blackwell, sufficiency, and Shannon statements of Part III under their own hypotheses; classical noisy information theory is not confined to a deterministic fiber.
>
> The multi-domain deterministic pullback and product identities hold by Lemma 83.2. No unrestricted assertion that all relaxations commute is made: prior marginalization can turn deterministic conditionally independent views into coupled stochastic views (XOR), and informative context prevents the all-record recovery excluded by Theorem 32.1. Restriction remains lax. The six coordinates remain an organizing taxonomy, not a proved product decomposition of theories or a uniqueness-of-axis theorem for anomalies.
>
> *Proof.* Substitute the stated hypotheses in the individual recovery results, including their scope conditions. The XOR counterexample and the context example in Theorem 32.1 show why these additional hypotheses are needed. $\square$

The deterministic fully admissible specialization recovers the exact kernel. Noisy classical experiment theory remains a valid part of the framework under its own hypotheses. The transport and recovery results connect these models without proving that all proposed extension directions commute.

---

## 86. Named open problems

The finite results above and in Appendix D require none of the conjectures below. The following list records which broader questions remain after the finite site, cut, and propagation results have been established.

**P1 (PID inside one address).** Does the witness class admit an internal nonnegative decomposition graded by the missing-face dimension of the nerve hierarchy (§38.3), i.e. a partial information decomposition *within* a single descent address, where Theorem 56.2's transport obstruction cannot arise because the ledger is fixed? Provenance: Remark 57.2.

**P2 (beyond the direct join-cover site).** Appendix D.8 settles pullback stability of join covers: it holds exactly for distributive finite achievable lattices, and then the coverage is subcanonical. The positive subset site already supports the witness sheaf. What remains is a useful alternative topology or base change representing more of the nondistributive content calculus, with an explicit comparison functor.

**P3 (sheafification of Theorem 6.7).** Whether registration-plus-consolidation is a sheafification in a precise sense — the universal property of Theorem 6.7 as the unit of a sheafification adjunction over the H4 site. Provenance: §8's H4 clause; open since Part I.

**P4 (used content).** A model of the downstream process that *uses* registered content, coarsening "extractable" to "used"; the evaluation functional's $(\mu, q)$-dependence (§53) is the flagged entry point — *used* is plausibly *evaluated against the questions the process actually asks*. Provenance: Part II §17; §59.

**P5 (a unified graded-ceiling construction).** Theorem 57.1 states separate exact-chain and coupling-fiber identities. Constructing a canonical combined object would require a specified class of graded admissible readings, a rule for their joint coupling, and a proof against double counting. The half-gap theorem does not by itself prove such a construction impossible; no universal construction is claimed here.

**P6 (infinite horizon and measurable optimization).** The finite-horizon conclusions hold under their stated causal and forensic models. Infinite horizons, continuous time, measurable quotient formation, uniform estimation, and optimization over kernel families require the separate regularity and attainment hypotheses listed in Appendix A.

**P7 (propagation beyond coordinate constraints).** Appendix D.10 proves exact finite message passing on Cartesian coordinate domains with a running-intersection tree. Generalized partition saturation alone is insufficient for this conclusion. Extending propagation to arbitrary common-scene partitions, graded couplings, or messages carrying interval defects requires additional conditional-independence or extension axioms and a convergence/correctness theorem.

---

## 87. Worked example M: one corpus, many domains

The laboratory, final appearance. Its corpus of records now serves two clients over one ambient class: an insurer running **entity resolution** — contrast domain $D_1$, identity reading, candidates are possible identities of the file's subject — and a clinic running **state tracking** — $D_2$, a coarsening of the joint scene domain $D^*$ by the question "which disease stage," tracked-target reading. The global algebra of Theorem 83.5 is the corpus's account of both at once: each record contributes a piece labeled in $L \subseteq \mathrm{Part}(D^*)$; the insurer's answer is a focusing $\varphi^{\Rightarrow \rho_1}$, the clinic's a focusing through the pulled-back stage question; and "everything the corpus says about anything" — the phrase (A5) deferred on page one — is the combination of all pieces, an element with a supporting label; a least support requires the ambient-meet-closure hypothesis of Appendix D.2. Part VII's ledger discipline is now geography: the clinic's coarse ledger *is* the coarsening morphism $c_{\ker q}$, and the transport theorem (56.2) says the insurer and the clinic may correctly file the same information quantum at different addresses — not a paradox but a change of domain. Two of the part's caveats appear in operation. For an assay whose unequal rows overlap in support, the clinic re-runs an independent measurement; Appendix D.3 gives $\varphi\otimes\varphi\succ_B\varphi$ — non-idempotent combination, accumulation by its classical name, and the reason the lab's (K3̂)-closed ceilings were priced as they were (Remark 23.6). And the insurer restricts to a sub-cohort $D' \subseteq D_1$ for an audit: two files that the full corpus admissibly identified fall apart in the restriction, because their identifying chain ran through an excluded third file — Lemma 83.2(2)'s laxity, live: **restriction can sever what combination had joined, and the severance is not an error but a theorem.**

---

## 88. The last recovery, and the coda

> **Theorem 88.1 (the (A5) fiber).** For the singleton family $\mathcal{D} = \{D\}$, the global algebra of Theorem 83.5 is Proposition 6.11 verbatim: $L = \mathrm{Ach}(V)$, vacuous extension is trivial, restriction morphisms are absent, and the labeled idempotent information algebra over the achievable-quotient lattice is recovered exactly. The multi-domain theory collapses onto its page-one germ, as each relaxation before it collapsed onto its own. $\square$

**Coda.** The common starting point is information relative to a declared contrast domain. Deterministic views yield a quotient order and a saturated-set algebra. Noise separates certainty, identifiability, and decision value; coupling determines what marginal descriptions omit. Admissibility introduces a gap between local and joint resolving power. Anchoring distinguishes the information in a record from the provenance of its attribution. These distinctions support useful comparison theorems, but do not make all defects instances of one invariant or all extensions commute.

---

## 89. Reviewed status of the monograph

The finite kernel, the qualified graph and partition calculus, the coupling-fiber constructions, and the explicit statistical decision comparisons provide the established framework. The [proof audit](../review/proof-audit.md) records every numbered result and its assumptions. The [supplementary theorems](registered-information-appendix-D.md) establish partial certification, a support criterion, a replication theorem, a quotient-lifting inequality, the least-coupling/join equivalence, a budget-transfer rule, and a sharp committed-bit test.

Several original completion claims have been withdrawn. A general measurable extension, a full graded valuation algebra, a comparison with contextuality cohomology, and unconstrained commutation of the proposed extension directions have not been established. The revised research directions identify concrete proof obligations and counterexamples that future work must respect. The companion papers' empirical claims remain subject to separate replication; Appendix B identifies exactly what this review checked.
