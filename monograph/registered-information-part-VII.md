# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part VII: The Stratified Decomposition

---

## 52. Overview of Part VII

The exact calculus of Parts V and VI produces intervals of partitions. Part VII asks how much information an interval represents. It introduces two measurements on two different objects and keeps them separate.

The first is an **evaluation of exact intervals** (§53). Fixing a prior $\mu$ and a question $q$, an interval $[a,b]$ of partitions is assigned the difference $I(q;[Z]_b) - I(q;[Z]_a)$. This is nonnegative, additive along chains, and detects every nondegenerate interval when the question is allowed to vary (Proposition 53.2), so every interval identity of the exact calculus becomes an additive identity in bits (Proposition 53.3). Section 54 evaluates the witness and reflection examples of Part V.

The second is the **coupling excess** of a stochastic family (§55): the mutual information of its actual joint channel minus the minimum over all joint channels with the same marginals. Section 55 computes a pure example and shows that the synergy measure of Bertschinger, Rauh, Olbrich, Jost, and Ay is the coupling excess of the family obtained by averaging over the question (Proposition 55.4). Section 56 shows that this averaging can move the same bit from a witness interval to the coupling excess (Theorem 56.2). Section 57 collects the two measurements in one statement, emphasizing that they are separate identities on separate objects (Theorem 57.1, Remark 57.2).

---

## 53. The evaluation functional

The exact obstruction calculus outputs intervals in $\mathrm{Part}(D)$; a decomposition of *information* needs numbers. The bridge is the observation that a pair $(\mu, q)$ evaluates partitions monotonically, so intervals evaluate to nonnegative reals and concatenations evaluate additively.

> **Definition 53.1 (evaluation).** For a full-support prior $\mu$ on $D$, a question $q$, and a partition $\pi \in \mathrm{Part}(D)$, write $[Z]_\pi$ for the block random variable of $\pi$ under $Z \sim \mu$. The **evaluation** of an interval $[a, b]$ (with $a \le b$) is
> $$
> \nu_{\mu,q}\big([a,b]\big) \;=\; I_\mu\big(q(Z);\, [Z]_b\big) \;-\; I_\mu\big(q(Z);\, [Z]_a\big).
> $$
> (For the endpoint pairs of non-monotone structures, where the left quantity can exceed the right — Definition 37.1's parenthetical — $\nu$ is signed; the calculus below is developed for the monotone case, mirroring §37.)

> **Proposition 53.2 (properties of $\nu$).**
>
> 1. **(Nonnegativity.)** $\nu_{\mu,q}([a,b]) \ge 0$: since $a \le b$, the block variable $[Z]_a$ is a function of $[Z]_b$, and the data-processing inequality applies.
> 2. **(Chain additivity.)** $\nu_{\mu,q}([a,b]) = \nu_{\mu,q}([a,m]) + \nu_{\mu,q}([m,b])$ for any $a \le m \le b$: evaluation telescopes along exactly the concatenation typed in Definition 15.3.
> 3. **(Zero law.)** $\nu_{\mu,q}([a,b]) = 0$ iff $H(q(Z) \mid [Z]_a) = H(q(Z) \mid [Z]_b)$, i.e. iff the refinement from $a$ to $b$ is **$q$-null**: $q(Z) \perp [Z]_b \mid [Z]_a$. An interval can be nondegenerate and $q$-null; $\nu$ measures what the refinement does *for this question under this prior*.
> 4. **(Joint faithfulness.)** For full-support $\mu$: $\sup_q \nu_{\mu,q}([a,b]) > 0$ iff $a < b$ strictly. Indeed the question $q_b$ with $\ker(q_b) = b$ gives $\nu_{\mu,q_b}([a,b]) = H_\mu([Z]_b) - H_\mu([Z]_a)$, which is strictly positive because a strictly finer partition splits some block of positive mass.
>
> *Proof.* 1 and 2 are as stated. 3: monotonicity makes the difference of conditional entropies the evaluation, and its vanishing is the stated conditional independence. 4: with $\ker(q_b) = b$, $q_b(Z)$ and $[Z]_b$ determine each other, so $I(q_b; [Z]_b) = H([Z]_b)$ and $I(q_b; [Z]_a) = H([Z]_a)$ (the coarser block variable being a function of the finer); full support gives every block positive mass, and strict refinement strictly increases entropy. $\square$

Item 4 deserves a sentence against Part V's linearized track. Per-pair nerve homology supplies an incomplete edge-level certificate and does not by itself certify a component-partition witness interval (Proposition 38.5). The full collection of nerves contains more information than those homology groups alone. The evaluation family $\{\nu_{\mu,q}\}$ is **complete** — it detects every nondegenerate interval — because it evaluates the intervals themselves. What $\nu$ does *not* do is identify mechanism: a number carries no address. Addresses come from *which chain the interval sits on*, which is the content of §§54–55; $\nu$ is the measure, the calculus is the geometry.

> **Proposition 53.3 (the calculus, pushed forward).** Let $K$ be monotone and $(\mu, q)$ fixed. Every interval identity of the exact theory becomes an additive identity in bits:
>
> 1. for any cover $\mathcal{U}$ of finite $T$: $\nu(\Delta_K(T)) = \nu\big([\sigma^{\mathrm{sep}}_K(T),\, \ell(\mathcal{U})]\big) + \nu\big(\delta_K(\mathcal{U}; T)\big)$, both terms nonnegative (Proposition 37.2);
> 2. for invariance structures: $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}(T)) + \nu(\Delta^{\mathrm{wit}}(T))$ (Theorem 37.7);
> 3. for mixed sets: $\nu(\Delta_K(T)) = \nu(J_K(T)) + \nu(X_K(T))$ (Proposition 46.2).
>
> In particular the vanishing theorem evaluates: if $K$ is separable at $T$, every term of every such identity is zero for every $(\mu, q)$ (Theorem 37.3); and absorption evaluates: a composite defect can be $\nu$-null while a stage defect carries positive bits one level down, with no inconsistency, since stages of distinct view sets are never summed — additivity is along chains within one $T$. $\square$

---

## 54. The exact addresses, in bits

> **Theorem 54.1 (the cosheaf addresses quantified).** Let $K_G$ be an invariance structure, $\mu$ full-support, $q$ a question.
>
> 1. **(Additive reflection–witness split.)** $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}(T)) + \nu(\Delta^{\mathrm{wit}}(T))$, with both terms computed from the orbit-graph data of Theorem 37.5 and the evaluation of Definition 53.1.
> 2. **(Pure witness: one bit.)** On the parity configuration (§16.1; uniform $\mu$; $q = q_G$): $\nu(\Delta^{\mathrm{refl}}) = 0$ and $\nu(\Delta^{\mathrm{wit}}) = I(q_G; [Z]_{P_G}) - I(q_G; [Z]_\bot) = 1 - 0 = 1$ bit — the XOR bit of §23.2, now carrying an address: witness, cosheaf, exact. More generally, on the cyclic hierarchy $C_{k+1}$ (Theorem 38.4; uniform $\mu$): the pure witness quantum is $1$ bit **at every arity**, all-or-nothing — $\nu(\Delta^{\mathrm{wit}}(T)) = H(q_G) = 1$ for the full family and the admissible information of every proper subfamily is $0$.
> 3. **(Pure reflection: $\log_2 3 - \tfrac23$ bits.)** On Worked example E (uniform $\mu$ on six elements; $q = q_G$ the three-valued orbit question): $\nu(\Delta^{\mathrm{wit}}) = 0$ and
> $$
> \nu(\Delta^{\mathrm{refl}}) \;=\; I\big(q_G;\, [Z]_{\mathrm{lift}(\{O_1O_2 \mid O_3\})}\big) \;=\; \log_2 3 - \tfrac23 \;\approx\; 0.918 \text{ bits},
> $$
> since the ceiling partition has blocks of mass $\tfrac23$ (within which the orbit is uniform on $\{O_1, O_2\}$, one residual bit) and $\tfrac13$ (pure $O_3$).
>
> 4. **(The policy lever, in bits.)** On Theorem 46.3's configuration (uniform $\mu$; $q = q_G$): $\nu(X_{K_G}(\{v, \tau_a\})) = 1$ bit under the context-reading policy and $0$ under the loyal policy. The interpreter's one lever moves exactly one bit of witness-address synergy.
>
> *Proof.* 1 is Proposition 53.3(2). 2: for parity, $\Delta^{\mathrm{refl}}$ is degenerate (Theorem 37.7's computation), $[Z]_\bot$ is constant, and $[Z]_{P_G} = q_G(Z)$, giving $H(q_G) = 1$ bit; §23.2's direct computation confirms $I(q_G; Y_v) = I(q_G; Y_w) = 0$, so nothing separable is being double-counted. For $C_{k+1}$: purity is Theorem 38.4; the two orbits have equal mass under the uniform prior, so $H(q_G) = 1$; every proper subfamily has $\gamma_G(T') = \bot$, hence admissible information $0$ — the threshold property, evaluated. 3: purity is Worked example E; the evaluation is the stated entropy computation, $H(q_G) - H(q_G \mid \text{blocks}) = \log_2 3 - \big(\tfrac23 \cdot 1 + \tfrac13 \cdot 0\big)$. 4: Theorem 46.3(1) gives the intervals $[\bot, P_G]$ and $[\bot, \bot]$; evaluate as in 2. $\square$

> **Remark 54.2 (the reflection address covers the support-geometric mechanism).** Section 23.2's mechanism (3) — zero-error superadditivity through noise-support geometry (Proposition 22.3) — produces interval data in $\mathrm{Part}(D)$ at the $\sigma^0$ stratum, which $\nu$ evaluates by the same definition; and its mechanism was identified with reflection in two steps (Proposition 22.3′; §37.4's closing: a closure operator failing to commute with a meet, in two lattices). The exact addresses of the stratified decomposition are therefore two, not three: **witness** and **reflection**, with the support-geometric instances filed under reflection. Section 23.2's count of three mechanisms is unchanged — its mechanism (1) is the ledger functor of §56, not an address.

---

## 55. The coupling address

> **Definition 55.1 (fiber excess; fiber width).** Let a coherent family over finite $T$ have joint channel $P_T$ and coupling fiber $\mathrm{Fib}(T)$ — the amalgamations over the singleton-cover matching family (Definition 39.1): joint channels $Q$ with $Q$'s $v$-marginal equal to $P_v(\cdot \mid Z)$ for every $v \in T$ and $Z \in D$. For a prior $\mu$ and question $q$, the **coupling component** and **fiber width** are
> $$
> C_{\mu,q}(T) \;=\; I_{P}\big(q(Z); Y_T\big) \;-\; \min_{Q \in \mathrm{Fib}(T)} I_{Q}\big(q(Z); Y_T\big),
> \qquad
> W_{\mu,q}(T) \;=\; \max_{\mathrm{Fib}(T)} I_Q \;-\; \min_{\mathrm{Fib}(T)} I_Q .
> $$
> Under (A6) the fiber is a nonempty compact convex polytope and $I_Q$ is continuous (and convex) in $Q$, so both extrema are attained. Write $I^{\min}_{\mu,q}(T)$ for the minimum — the **marginal-forced residual**.

> **Proposition 55.2 (basic laws).** $C_{\mu,q}(T) \ge 0$, and $I^{\min}_{\mu,q}(T) \ge \max_{v \in T} I(q(Z); Y_v)$, since every $Q \in \mathrm{Fib}(T)$ has the family's own marginals. If the fiber is a singleton — in particular for deterministic families (Theorem 42.1(3)) — then $C_{\mu,q} \equiv 0$: **at the fine ledger, exact synergy carries no coupling component**, and the entire exact quantum is cosheaf-side, where §54 decomposes it. $\square$

> **Proposition 55.3 (pure coupling: $\tfrac32 - \tfrac34 \log_2 3$ bits).** For the family of Proposition 22.4(2) — $D = \{Z, Z'\}$, both marginal likelihoods uniform on $\{0,1\}$, outputs equal with probability one under $Z$ and independent under $Z'$ — with uniform prior and $q = \mathrm{id}$:
> $$
> I(q; Y_v) = I(q; Y_w) = 0,
> \qquad
> I^{\min}_{\mu,q}(\{v,w\}) = 0,
> \qquad
> C_{\mu,q}(\{v,w\}) = I_P(q; Y_{vw}) = \tfrac32 - \tfrac34 \log_2 3 \;\approx\; 0.311 \text{ bits},
> $$
> and both exact addresses vanish (the family is graded; no ceiling is in play and the deterministic calculus does not apply). The fiber width is $1$ bit, attained between the doubly-independent coupling and the coupling that is diagonal under $Z$ and antidiagonal under $Z'$. Pure coupling is realized.
>
> *Proof.* Per-view: uniform likelihoods are candidate-independent, so $Y_v \perp Z$. The doubly-independent coupling $\widetilde{Q}$ (product of the uniform marginals under both candidates) lies in the fiber and has $Y_{vw} \perp Z$, so the minimum is $0$. The family's own information: the two joint likelihoods are $\tfrac12(\delta_{00} + \delta_{11})$ and the uniform distribution; against their mixture $m = (\tfrac38, \tfrac18, \tfrac18, \tfrac38)$,
> $$
> I_P = \tfrac12 D\big(\tfrac12(\delta_{00}{+}\delta_{11}) \,\|\, m\big) + \tfrac12 D(\mathrm{unif} \,\|\, m)
> = \tfrac12\big(2 - \log_2 3\big) + \tfrac12\big(1 - \tfrac12 \log_2 3\big) = \tfrac32 - \tfrac34 \log_2 3 .
> $$
> Width: diagonal-vs-antidiagonal couplings have disjoint joint supports, giving $I = 1$ bit, the maximum for a binary candidate. $\square$

> **Proposition 55.4 (identification: BROJA synergy is the coupling component of the coarse ledger).** For two sources, the complementary (synergistic) information of [Bertschinger, Rauh, Olbrich, Jost & Ay 2014],
> $$
> CI(q;\, Y_v, Y_w) \;=\; I_P\big(q; Y_{vw}\big) \;-\; \min_{Q \in \Delta_P} I_Q\big(q; Y_{vw}\big),
> $$
> with $\Delta_P$ the set of joint distributions of $(q(Z), Y_v, Y_w)$ preserving the $(q, Y_v)$- and $(q, Y_w)$-marginals, coincides with $C_{\mu_q, \mathrm{id}}$ computed for the **prior-marginalized family**: the family over the quotient domain $D_q = D / \ker(q)$ with prior $\mu_q$ and channels $P(Y_v \mid q(Z))$. Indeed conditioning on the value of $q$ puts $\Delta_P$ in bijection with the coupling fiber of that family: fixing the $(q, Y_v)$-marginals is exactly fixing the candidatewise per-view channels over $D_q$. **The BROJA optimization domain is Part V's coupling fiber, over the coarse ledger; its synergy measure is the fiber excess.** $\square$

> **Remark 55.5 (three rungs of one coordinate).** The coupling address now has its invariant at each coefficient level, in the discipline of Remark 40.3: the *exact* invariant is non-constancy of $\sigma^{=}$ on fibers (Proposition 39.3(2)); the *Shannon* invariant is the fiber excess and width of Definition 55.1; the *enriched* invariant is the Le Cam diameter of the fiber (§39, §40). Proposition 55.3's family instantiates all three: $\sigma^{=}$ takes both $\bot$ and $\top$ on its fiber, the width is one bit, and the diameter is positive.

---

## 56. The ledger functor and the transport theorem

Section 23.2's mechanism (1) — prior-marginalization — was never an address; Remark 42.3 called it a change of ledger. Here is the change, as a map, and the theorem that it moves quanta between addresses.

> **Definition 56.1 (the ledger functor).** For a coherent family over $D$ with prior $\mu$ and question $q$, the **$q$-marginalization** is the coherent family over the quotient contrast domain $D_q = D/\ker(q)$ with prior $\mu_q$ and channels $P(Y_v \mid q(Z))$ (well defined by averaging $\mu$ within $q$-classes). The **coarse ledger** of $(family, \mu, q)$ is the fine ledger of its $q$-marginalization: in particular, the coarse fiber is the coupling fiber of the marginalized family, and $C^{\mathrm{coarse}}_{\mu,q} := C_{\mu_q, \mathrm{id}}(\text{marginalized family})$, which by Proposition 55.4 is BROJA's $CI$.

> **Theorem 56.2 (transport: the same bit changes address).** Let the family be deterministic over $D$, let $\mu$ have full support, and suppose the family is **per-view $q$-blind**: $I_\mu(q(Z); Y_v) = 0$ for every $v \in T$. Then:
>
> 1. **(Fine ledger.)** The fine fiber is a singleton (Theorem 42.1(3)), so $C_{\mu,q}(T) = 0$: this establishes zero fine coupling excess. A fine witness/reflection address requires a specified admissibility structure and its interval calculation; it is not determined by source blindness alone.
> 2. **(Coarse ledger.)** Per-view $q$-blindness makes each marginalized channel $P(Y_v \mid q)$ constant in $q$; the product coupling $Q^\otimes(y_T \mid q) = \prod_v P(y_v)$ lies in the coarse fiber and renders $Y_T \perp q$, so $\min I = 0$ and
> $$
> C^{\mathrm{coarse}}_{\mu,q}(T) \;=\; I_\mu\big(q(Z); Y_T\big).
> $$
> **The entire quantum sits at the coupling address of the coarse ledger.**
>
> 3. **(Instance.)** For the parity configuration, the one bit of Theorem 54.1(2) — witness address, fine ledger — is exactly the one bit of coarse-ledger coupling excess: $C^{\mathrm{coarse}} = 1$ bit, realized between the XOR coupling and the product coupling. The known fact that XOR is BROJA-synergistic is, in this typing, the image of a witness class under the ledger functor.
>
> *Proof.* 1 is Proposition 55.2. 2: $Y_v \perp q$ gives $P(y_v \mid q) = P(y_v)$; the product coupling has the required $(q, Y_v)$-marginals and makes the joint output independent of $q$; nonnegativity of mutual information makes it a minimizer. 3 instantiates 2 with §23.2's computation and Theorem 54.1(2). $\square$

> **Corollary 56.3 (noninvariance of the specified addresses).** No address assignment that agrees with the computed fine-ledger witness address and coarse-ledger coupling address of the parity/invariance example can be invariant under its prior-marginalization map.
>
> *Proof.* Theorem 54.1 assigns that fine-ledger bit to the witness interval under the specified invariance ceiling. Theorem 56.2 assigns its coarse fiber excess to coupling. The two required labels differ for the same transported bit. The conclusion concerns this address-preserving requirement, not arbitrary scalar functionals of the coarse distribution or a universal PID impossibility theorem. $\square$

> **Remark 56.4 (what the ledger comparison establishes).** Theorem 56.2 distinguishes a fine-state mechanism description from the ordinary target-relative distribution. The latter need not determine an admissibility-dependent fine-state address. This explains why a proposed invariant of both descriptions needs additional input and compatibility axioms. It does not derive or locate the formal PID impossibility theorem of Rauh et al. (2014): that theorem has its own axioms and proof. Blackwell comparisons can be formulated over either state space and are not intrinsically fine-ledger commitments. A rigorous comparison with PID should specify the proposed functional, its input, and the exact incompatible requirements. Appendix D.4 establishes the finite coupling-fiber inequality without an impossibility claim.

---

## 57. The stratified decomposition theorem

> **Theorem 57.1 (the stratified decomposition).** Fix a coherent family, a full-support prior $\mu$, and a question $q$, and work on a fixed ledger (fine, or coarse via Definition 56.1).
>
> 1. **(Graded clause; the sheaf address.)** For every finite $T$:
> $$
> I\big(q(Z); Y_T\big) \;=\; C_{\mu,q}(T) \;+\; I^{\min}_{\mu,q}(T),
> $$
> with $C \ge 0$ the coupling component and $I^{\min} \ge \max_v I(q; Y_v) \ge 0$ the marginal-forced residual; $C$ vanishes whenever the fiber is a singleton, in particular on deterministic families.
>
> 2. **(Exact clause; the cosheaf addresses.)** For deterministic families under a monotone admissibility structure, the admissible information decomposes additively along the canonical chains: for every cover, $\nu(\Delta_K(T)) = \nu([\sigma^{\mathrm{sep}}_K(T), \ell(\mathcal{U})]) + \nu(\delta_K(\mathcal{U}; T))$; for invariance structures, $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}) + \nu(\Delta^{\mathrm{wit}})$; for mixed feature–record sets, $\nu(\Delta_K(T)) = \nu(J_K(T)) + \nu(X_K(T))$ — all terms nonnegative, at every arity (Propositions 53.2–53.3, Theorem 54.1).
> 3. **(Separate mechanism examples.)** In the exact clause, parity has pure witness evaluation $1$ bit, and Example E has pure reflection evaluation $\log_2 3-2/3$ bits; both have zero coupling excess because their fine fibers are singletons. In the graded clause, Proposition 55.3 gives coupling excess $3/2-(3/4)\log_2 3$ bits. No exact witness/reflection split is asserted for that graded example without an additional admissibility construction.
> 4. **(Sufficient vanishing conditions.)** Exact interval evaluations vanish on separable structures. Sterility identifies defects with their presentation shadows only for covers whose members are $N$-complete; they vanish if those shadows glue. Coupling excess vanishes on singleton fibers and, more generally, whenever the observed joint minimizes the fiber objective. These are not converse characterizations for a fixed question, and the two clauses are separate identities on their respective objects.
> 5. **(Exclusions, principled.)** Prior-marginalization is not a component but the **functor between the decompositions** (Definition 56.1, Theorem 56.2). Accumulation is not a component because it varies the datum: $C$ and $\nu$ are functionals of a fixed family, while accumulation compounds *readings* of it — §23.2's coda, with the exclusion now typed rather than observed.
>
> These identities do not supply a single additive sum of witness, reflection, and coupling terms for arbitrary graded ceilings. Corollary 56.3 concerns the noninvariance of the specified parity addresses; it is not a general PID impossibility theorem (Remark 56.4).
>
> *Proof.* 1 is Definition 55.1 and Proposition 55.2 (existence of the minimum by compactness). 2 collects §§53–54. 3 collects Theorem 54.1(2,3) and Proposition 55.3; deterministic fibers give the two asserted zero coupling excesses by Proposition 55.2. The graded example is evaluated only by its fiber excess. 4: separability gives degeneracy, while Proposition 46.4 identifies the stipulated cover defects with their shadows; a zero shadow defect is needed for vanishing. By definition an observed minimizer has zero coupling excess; degenerate intervals are $\nu$-null for every $(\mu, q)$, and singleton fibers force $C = 0$; the $q$-nullity proviso is Proposition 53.2(3)'s one-way gap between measure and geometry. 5 is as stated. $\square$

> **Remark 57.2 (the allocation question remains distinct).** The exact formulas evaluate ordered partition chains; the graded formula compares one joint experiment with the minimum over its declared coupling fiber. These operations do not allocate unique, redundant, and synergistic contributions to every subset in a PID redundancy lattice. Theorem 56.2 changes the model and its available data; it does not prohibit a common answer after specifying an enlarged input. A refinement within one witness interval, perhaps using its nerve and cut structure, remains an open allocation problem.

---

## 58. Worked example I: a three-address ledger

Assemble the three pure generators on one contrast domain: $D = D_1 \times D_2 \times D_3$ with independent uniform prior, where $D_1 = \{00,01,10,11\}$ carries the parity configuration (views $v, w$ reading the $D_1$ coordinates), $D_2 = \{Z, Z'\}$ carries Proposition 22.4(2)'s coupled pair (graded views $s, t$ reading the $D_2$ factor), and $D_3$ carries Worked example E (views $v_3, w_3$ reading the $D_3$ factor). The group $G_1 \times 1 \times G_3$ acts factorwise; its orbit partition is the product $P_{G_1} \times \top \times P_{G_3}$, and since kernels of factor-local views are cylinder partitions and both lattice operations of Fact 3.3 factorize on products of factor-local data, the invariance ceiling computes factorwise. The question is the joint $q = (q_{G_1}, \mathrm{id}_{D_2}, q_{G_3})$; readings are admissible exact readings on the deterministic factors tensored with arbitrary channels on the graded factor. Under the declared independent factor construction, the displayed Shannon contributions add, and the ledger reads:

| address | carrier | quantum (bits) | invariant | dial |
|---|---|---|---|---|
| witness (cosheaf, exact) | $D_1$: parity | $1$ | nerve non-fullness ($\partial\Delta^1$; §38) | the cover; or Part VI's policy (Theorem 54.1(4)) |
| reflection (cosheaf, exact) | $D_3$: Example E | $\log_2 3 - \tfrac23 \approx 0.918$ | components/meet non-commutation (Theorem 37.7) | the ceiling |
| coupling (sheaf, graded) | $D_2$: the pair | $\tfrac32 - \tfrac34\log_2 3 \approx 0.311$ | fiber non-constancy; excess and width (§55) | the coupling — a point of the fiber |

Because the factors are independent and the question is a product, each row can be switched by its own dial without affecting the others. The three quanta are values of different functionals — two interval evaluations and one fiber excess — so their sum ($\approx 2.230$ bits) is not itself a term of any decomposition proved here (Remark 57.2). Marginalizing the prior onto $q$ transports the first row's bit to the third row's address (Theorem 56.2) — the table is a table *per ledger*, which is the resolution in one picture.

---

## 59. Summary of Part VII

Exact interval evaluations telescope along chains and give bits to the witness and reflection examples (Proposition 53.3, Theorem 54.1). Coupling excess is nonnegative, vanishes on singleton fibers, and coincides with the BROJA synergy of the question-averaged family (Propositions 55.2, 55.4). Averaging over the question can transfer a bit from a witness interval under an invariance ceiling to coupling excess (Theorem 56.2), so labels attached to the same bit depend on which description is fixed (Corollary 56.3).

What is not established: a single additive decomposition combining interval evaluations and coupling excess for arbitrary graded ceilings, and any impossibility theorem for partial information decomposition beyond the specific statement of Corollary 56.3. Zero coupling excess means that the actual joint attains the fiber minimum, not that the fiber is a singleton.

**References added in Part VII:**

- Rauh, J., Bertschinger, N., Olbrich, E., and Jost, J. (2014). "Reconsidering Unique Information: Towards a Multivariate Information Decomposition." *Proceedings of the IEEE International Symposium on Information Theory (ISIT 2014)*, 2232–2236.

All other sources — Williams & Beer, Bertschinger–Rauh, Bertschinger–Rauh–Olbrich–Jost–Ay, Le Cam, Torgersen — were already cited; the one addition is the formal impossibility theorem that Remark 56.4 reads structurally.
