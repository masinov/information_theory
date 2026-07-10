# Registered Information over Contrast Domains

## Part VII: The Stratified Decomposition

---

## 52. Purpose, and the resolution announced

Remark 42.3 left the manuscript's one standing quantitative conjecture: *a decomposition of multivariate information exists that is indexed by descent address, with the three mechanism classes as its pure generators, and the known impossibility results for scalar partial information decomposition reflect the attempt to sum across addresses.* Section 23.2 had prepared the ground by separating three mechanisms that the PID literature aggregates under "synergy" — prior-marginalization, admissibility restriction, support geometry — with coupling as the statistical stratum's own mechanism (Proposition 22.4(2)) and accumulation as the reverse phenomenon outside any fixed-datum decomposition. Part V assigned descent addresses: witness and reflection are cosheaf-side and exact; coupling is sheaf-side and graded; prior-marginalization "is not a descent failure at all but a change of ledger." Part VI closed the mechanism inventory with the interaction matrix (§50.2), certifying that no further mechanism is waiting in the composite theory. The conjecture is therefore ripe, and this part resolves it.

The resolution has an unexpected shape, and it is stated up front. The conjecture is **proved** in its ledger-relative reading and **refuted** in a natural strengthening, and the split is itself a theorem. Precisely:

- There is an evaluation functional $\nu_{\mu,q}$ turning the exact obstruction calculus of §37 — and with it every interval identity of Parts II, V, and VI — into a **nonnegative, additive decomposition in bits**, faithful over full-support priors (§53). Under it, the reflection–witness decomposition (Theorem 37.7), the cross-layer factorization (Proposition 46.2), and the cover calculus all become additive information identities, with the three pure generators realized and computed: one bit of pure witness, $\log_2 3 - \tfrac23$ bits of pure reflection, $\tfrac32 - \tfrac34\log_2 3$ bits of pure coupling (§§54–55).
- The coupling address is quantified by the **fiber excess** — the family's information above the minimum over Part V's coupling fiber — and this functional is proved to *coincide definitionally* with the synergy measure of [Bertschinger, Rauh, Olbrich, Jost & Ay 2014] once the ledgers are matched: BROJA's optimization domain **is** the coupling fiber of the prior-marginalized family (Proposition 55.4).
- The **ledger functor** — prior-marginalization, §23.2's mechanism (1) — is proved to transport quanta *between addresses*: for per-view question-blind deterministic families, the entire synergy sits at the witness address of the fine ledger and at the coupling address of the coarse ledger, the same bit changing address under marginalization (Theorem 56.2). Hence no ledger-invariant address assignment exists, the strengthened conjecture is false, and the scalar-PID impossibility is **located**: axiom systems that key different axioms to different ledgers constrain a quantity the transport theorem shows is not well defined across the crossing (§56).
- The stratified decomposition theorem (Theorem 57.1) assembles the components, exhibits the vanishing loci as the tame loci already named — separability, singleton fibers, sterility — records the two principled exclusions (the ledger functor is a *map between* decompositions, not a component; accumulation varies the datum), and states exactly which question is answered and which is deliberately not: the decomposition allocates information to *mechanisms*, and its universal nonnegativity at every arity is purchased by evaluating chains per cover rather than inverting over the redundancy lattice (§57).

**The ledger discipline.** Every quantitative decomposition is relative to a *ledger*: the data held fixed while alternatives are ranged over. The framework supplies two, and keeping them separated is the part's method. The **fine ledger** fixes the candidatewise per-view channels $\{P_v(\cdot \mid Z)\}$ — its space of alternatives is exactly the coupling fiber of Definition 39.1. The **coarse ledger** fixes the question-conditional channels $\{P(Y_v \mid q(Z))\}$ — the object PID works with — and §56 identifies it as the fine ledger *of the prior-marginalized family*. Neither ledger is wrong; the crossing between them is where the addresses move.

**Assumptions.** (A1), (A5), (A6) throughout; priors have full support unless stated. Sections 53–54 are exact ((A2)), with monotone admissibility as in Part II. Sections 55–57 relax (A2) as in Part III. Anchoring appears only through Part VI's policy lever, under the exact anchored regime of §44. Part VII presupposes Parts I–VI and uses their numbering; nothing in Parts I–VI is modified, except that the open-problem sentences of §23.2 and Remark 42.3 receive discharge pointers.

---

## 53. The evaluation functional

The exact obstruction calculus outputs intervals in $\mathrm{Part}(D)$; a decomposition of *information* needs numbers. The bridge is the observation that a pair $(\mu, q)$ evaluates partitions monotonically, so intervals evaluate to nonnegative reals and concatenations evaluate additively.

> **Definition 53.1 (evaluation).** For a full-support prior $\mu$ on $D$, a question $q$, and a partition $\pi \in \mathrm{Part}(D)$, write $[Z]_\pi$ for the block random variable of $\pi$ under $Z \sim \mu$. The **evaluation** of an interval $[a, b]$ (with $a \le b$) is
> $$
> \nu_{\mu,q}\big([a,b]\big) \;=\; I_\mu\big(q(Z);\, [Z]_b\big) \;-\; I_\mu\big(q(Z);\, [Z]_a\big).
> $$
> (For the endpoint pairs of non-monotone structures, where the left quantity can exceed the right — Definition 37.1's parenthetical — $\nu$ is signed; the calculus below is developed for the monotone case, mirroring §37.)

> **Proposition 53.2 (properties of $\nu$).**
> 1. **(Nonnegativity.)** $\nu_{\mu,q}([a,b]) \ge 0$: since $a \le b$, the block variable $[Z]_a$ is a function of $[Z]_b$, and the data-processing inequality applies.
> 2. **(Chain additivity.)** $\nu_{\mu,q}([a,b]) = \nu_{\mu,q}([a,m]) + \nu_{\mu,q}([m,b])$ for any $a \le m \le b$: evaluation telescopes along exactly the concatenation typed in Definition 15.3.
> 3. **(Zero law.)** $\nu_{\mu,q}([a,b]) = 0$ iff $H(q(Z) \mid [Z]_a) = H(q(Z) \mid [Z]_b)$, i.e. iff the refinement from $a$ to $b$ is **$q$-null**: $q(Z) \perp [Z]_b \mid [Z]_a$. An interval can be nondegenerate and $q$-null; $\nu$ measures what the refinement does *for this question under this prior*.
> 4. **(Joint faithfulness.)** For full-support $\mu$: $\sup_q \nu_{\mu,q}([a,b]) > 0$ iff $a < b$ strictly. Indeed the question $q_b$ with $\ker(q_b) = b$ gives $\nu_{\mu,q_b}([a,b]) = H_\mu([Z]_b) - H_\mu([Z]_a)$, which is strictly positive because a strictly finer partition splits some block of positive mass.
>
> *Proof.* 1 and 2 are as stated. 3: monotonicity makes the difference of conditional entropies the evaluation, and its vanishing is the stated conditional independence. 4: with $\ker(q_b) = b$, $q_b(Z)$ and $[Z]_b$ determine each other, so $I(q_b; [Z]_b) = H([Z]_b)$ and $I(q_b; [Z]_a) = H([Z]_a)$ (the coarser block variable being a function of the finer); full support gives every block positive mass, and strict refinement strictly increases entropy. $\square$

Item 4 deserves a sentence against Part V's linearized track. Homology was a *sound but incomplete* certificate for the witness component and provably blind to reflection (Proposition 38.5), because it evaluated a shadow of the anomaly. The evaluation family $\{\nu_{\mu,q}\}$ is **complete** — it detects every nondegenerate interval — because it evaluates the intervals themselves. What $\nu$ does *not* do is identify mechanism: a number carries no address. Addresses come from *which chain the interval sits on*, which is the content of §§54–55; $\nu$ is the measure, the calculus is the geometry.

> **Proposition 53.3 (the calculus, pushed forward).** Let $K$ be monotone and $(\mu, q)$ fixed. Every interval identity of the exact theory becomes an additive identity in bits:
> 1. for any cover $\mathcal{U}$ of finite $T$: $\nu(\Delta_K(T)) = \nu\big([\sigma^{\mathrm{sep}}_K(T),\, \ell(\mathcal{U})]\big) + \nu\big(\delta_K(\mathcal{U}; T)\big)$, both terms nonnegative (Proposition 37.2);
> 2. for invariance structures: $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}(T)) + \nu(\Delta^{\mathrm{wit}}(T))$ (Theorem 37.7);
> 3. for mixed sets: $\nu(\Delta_K(T)) = \nu(J_K(T)) + \nu(X_K(T))$ (Proposition 46.2).
>
> In particular the vanishing theorem evaluates: if $K$ is separable at $T$, every term of every such identity is zero for every $(\mu, q)$ (Theorem 37.3); and absorption evaluates: a composite defect can be $\nu$-null while a stage defect carries positive bits one level down, with no inconsistency, since stages of distinct view sets are never summed — additivity is along chains within one $T$. $\square$

---

## 54. The exact addresses, in bits

> **Theorem 54.1 (the cosheaf addresses quantified).** Let $K_G$ be an invariance structure, $\mu$ full-support, $q$ a question.
> 1. **(Additive reflection–witness split.)** $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}(T)) + \nu(\Delta^{\mathrm{wit}}(T))$, with both terms computed from the orbit-graph data of Theorem 37.5 and the evaluation of Definition 53.1.
> 2. **(Pure witness: one bit.)** On the parity configuration (§16.1; uniform $\mu$; $q = q_G$): $\nu(\Delta^{\mathrm{refl}}) = 0$ and $\nu(\Delta^{\mathrm{wit}}) = I(q_G; [Z]_{P_G}) - I(q_G; [Z]_\bot) = 1 - 0 = 1$ bit — the XOR bit of §23.2, now carrying an address: witness, cosheaf, exact. More generally, on the cyclic hierarchy $C_{k+1}$ (Theorem 38.4; uniform $\mu$): the pure witness quantum is $1$ bit **at every arity**, all-or-nothing — $\nu(\Delta^{\mathrm{wit}}(T)) = H(q_G) = 1$ for the full family and the admissible information of every proper subfamily is $0$.
> 3. **(Pure reflection: $\log_2 3 - \tfrac23$ bits.)** On Worked example E (uniform $\mu$ on six elements; $q = q_G$ the three-valued orbit question): $\nu(\Delta^{\mathrm{wit}}) = 0$ and
> $$
> \nu(\Delta^{\mathrm{refl}}) \;=\; I\big(q_G;\, [Z]_{\mathrm{lift}(\{O_1O_2 \mid O_3\})}\big) \;=\; \log_2 3 - \tfrac23 \;\approx\; 0.918 \text{ bits},
> $$
> since the ceiling partition has blocks of mass $\tfrac23$ (within which the orbit is uniform on $\{O_1, O_2\}$, one residual bit) and $\tfrac13$ (pure $O_3$).
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
> 1. **(Fine ledger.)** The fine fiber is a singleton (Theorem 42.1(3)), so $C_{\mu,q}(T) = 0$: the entire quantum $I_\mu(q; Y_T)$ is cosheaf-side, and under an invariance ceiling it is placed by §54's split.
> 2. **(Coarse ledger.)** Per-view $q$-blindness makes each marginalized channel $P(Y_v \mid q)$ constant in $q$; the product coupling $Q^\otimes(y_T \mid q) = \prod_v P(y_v)$ lies in the coarse fiber and renders $Y_T \perp q$, so $\min I = 0$ and
> $$
> C^{\mathrm{coarse}}_{\mu,q}(T) \;=\; I_\mu\big(q(Z); Y_T\big).
> $$
> **The entire quantum sits at the coupling address of the coarse ledger.**
> 3. **(Instance.)** For the parity configuration, the one bit of Theorem 54.1(2) — witness address, fine ledger — is exactly the one bit of coarse-ledger coupling excess: $C^{\mathrm{coarse}} = 1$ bit, realized between the XOR coupling and the product coupling. The known fact that XOR is BROJA-synergistic is, in this typing, the image of a witness class under the ledger functor.
>
> *Proof.* 1 is Proposition 55.2. 2: $Y_v \perp q$ gives $P(y_v \mid q) = P(y_v)$; the product coupling has the required $(q, Y_v)$-marginals and makes the joint output independent of $q$; nonnegativity of mutual information makes it a minimizer. 3 instantiates 2 with §23.2's computation and Theorem 54.1(2). $\square$

> **Corollary 56.3 (refutation of the ledger-invariant strengthening).** There is no assignment of descent addresses to information quanta that is invariant under prior-marginalization: the parity bit is witness-addressed at the fine ledger and coupling-addressed at the coarse ledger, and both addresses are *correct on their own ledgers* — the fine fiber genuinely is a singleton; the coarse fiber genuinely is not. A stratified decomposition exists per ledger (Theorem 57.1); a ledger-free one does not. $\square$

> **Remark 56.4 (locating the scalar impossibility).** The diagnosis of §23.2 — a single scalar decomposition summarizing mechanistically inhomogeneous quantities — can now be stated with the mechanism computed. Scalar PID axiom systems draw constraints from both sides of the crossing: the identity axiom and target-relative decomposition structure are coarse-ledger commitments (they constrain distributions of $(q, Y_v, Y_w)$, i.e. marginalized families — Proposition 55.4 makes BROJA's own measure coarse-native), while Blackwell-order monotonicity intuitions and channel-level reasoning are fine-ledger commitments (they live on the candidatewise channels the coarse ledger has already averaged). Theorem 56.2 shows the crossing carries actual bits whose address is not preserved, so a scalar functional answering to both ledgers at once is being asked to take a value the transport theorem shows is not well defined. This is consistent with, and gives a structural reading of, the formal impossibility of nonnegative multivariate extension under the identity axiom [Rauh, Bertschinger, Olbrich & Jost 2014] and the lattice-freeness of the Blackwell order [Bertschinger & Rauh 2014]. The claim made here is the located diagnosis, not a rederivation of those theorems: what the framework adds is that the obstruction to scalar PID sits at a nameable place — the ledger crossing — and that on either side of it, decomposition succeeds (Theorem 57.1).

---

## 57. The stratified decomposition theorem

> **Theorem 57.1 (the stratified decomposition).** Fix a coherent family, a full-support prior $\mu$, and a question $q$, and work on a fixed ledger (fine, or coarse via Definition 56.1).
> 1. **(Graded clause; the sheaf address.)** For every finite $T$:
> $$
> I\big(q(Z); Y_T\big) \;=\; C_{\mu,q}(T) \;+\; I^{\min}_{\mu,q}(T),
> $$
> with $C \ge 0$ the coupling component and $I^{\min} \ge \max_v I(q; Y_v) \ge 0$ the marginal-forced residual; $C$ vanishes whenever the fiber is a singleton, in particular on deterministic families.
> 2. **(Exact clause; the cosheaf addresses.)** For deterministic families under a monotone admissibility structure, the admissible information decomposes additively along the canonical chains: for every cover, $\nu(\Delta_K(T)) = \nu([\sigma^{\mathrm{sep}}_K(T), \ell(\mathcal{U})]) + \nu(\delta_K(\mathcal{U}; T))$; for invariance structures, $\nu(\Delta_{K_G}(T)) = \nu(\Delta^{\mathrm{refl}}) + \nu(\Delta^{\mathrm{wit}})$; for mixed feature–record sets, $\nu(\Delta_K(T)) = \nu(J_K(T)) + \nu(X_K(T))$ — all terms nonnegative, at every arity (Propositions 53.2–53.3, Theorem 54.1).
> 3. **(Pure generators.)** Each address is realized purely, with the other components zero: **witness** — parity, $1$ bit (and $1$ bit at every arity on the hierarchy $C_{k+1}$); **reflection** — Worked example E, $\log_2 3 - \tfrac23$ bits (with the support-geometric zero-error instances filed at this address, Remark 54.2); **coupling** — Proposition 22.4(2)'s pair, $\tfrac32 - \tfrac34\log_2 3$ bits.
> 4. **(Vanishing loci $=$ tame loci.)** Up to $q$-nullity (Proposition 53.2(3)), the components vanish exactly where the qualitative theory said the phenomena vanish: the exact components on separable structures (Theorem 37.3), the cross-layer component on the sterile locus (Proposition 46.4), the coupling component on singleton fibers — in particular on the deterministic fiber, which is where the two clauses glue (Theorems 24.2, 42.1).
> 5. **(Exclusions, principled.)** Prior-marginalization is not a component but the **functor between the decompositions** (Definition 56.1, Theorem 56.2). Accumulation is not a component because it varies the datum: $C$ and $\nu$ are functionals of a fixed family, while accumulation compounds *readings* of it — §23.2's coda, with the exclusion now typed rather than observed.
>
> Consequently Remark 42.3's conjecture holds in its ledger-relative reading — a decomposition of multivariate information indexed by descent address exists, with the mechanism classes as its pure generators — and fails in the ledger-invariant strengthening (Corollary 56.3), with the scalar-PID impossibility located at the crossing (Remark 56.4).
>
> *Proof.* 1 is Definition 55.1 and Proposition 55.2 (existence of the minimum by compactness). 2 collects §§53–54. 3 collects Theorem 54.1(2,3) and Proposition 55.3, with the cross-vanishing checks recorded there: the pure-witness and pure-reflection families are deterministic ($C = 0$ by Proposition 55.2), and the pure-coupling family has candidate-blind marginals with no ceiling in play. 4: each cited theorem gives degeneracy of the relevant intervals or triviality of the fiber; degenerate intervals are $\nu$-null for every $(\mu, q)$, and singleton fibers force $C = 0$; the $q$-nullity proviso is Proposition 53.2(3)'s one-way gap between measure and geometry. 5 is as stated. $\square$

> **Remark 57.2 (what is answered, and what is deliberately not).** The stratified decomposition allocates information to *mechanisms per cover*: its indices are descent addresses, its identities are chain evaluations, and its universal nonnegativity — at every arity, with no analogue of the three-source breakdown — is purchased precisely by refusing the operation that scalar PID is built on: comparing allocations *across* covers by Möbius inversion on the redundancy lattice [Williams & Beer 2010]. Chains telescope; antichains must be inverted, and inversion is where local positivity dies [Rauh, Bertschinger, Olbrich & Jost 2014]. The decomposition therefore does not answer PID's allocation question (how much information each subset of sources contributes uniquely, redundantly, synergistically); it answers the question the manuscript has been building since §16 — *by which mechanism, at which address, switchable by which dial* — and Theorem 56.2 is the formal reason the two questions cannot have a common answer. Whether each single address admits an internal lattice-refinement (a PID *within* the witness class, say, stratified by the nerve's missing-face dimension of §38.3) is the sharpest question the resolution leaves open.

---

## 58. Worked example I: a three-address ledger

Assemble the three pure generators on one contrast domain: $D = D_1 \times D_2 \times D_3$ with independent uniform prior, where $D_1 = \{00,01,10,11\}$ carries the parity configuration (views $v, w$ reading the $D_1$ coordinates), $D_2 = \{Z, Z'\}$ carries Proposition 22.4(2)'s coupled pair (graded views $s, t$ reading the $D_2$ factor), and $D_3$ carries Worked example E (views $v_3, w_3$ reading the $D_3$ factor). The group $G_1 \times 1 \times G_3$ acts factorwise; its orbit partition is the product $P_{G_1} \times \top \times P_{G_3}$, and since kernels of factor-local views are cylinder partitions and both lattice operations of Fact 3.3 factorize on products of factor-local data, the invariance ceiling computes factorwise. The question is the joint $q = (q_{G_1}, \mathrm{id}_{D_2}, q_{G_3})$; readings are admissible exact readings on the deterministic factors tensored with arbitrary channels on the graded factor. Independence across factors makes every information quantity additive, and the ledger reads:

| address | carrier | quantum (bits) | invariant | dial |
|---|---|---|---|---|
| witness (cosheaf, exact) | $D_1$: parity | $1$ | nerve non-fullness ($\partial\Delta^1$; §38) | the cover; or Part VI's policy (Theorem 54.1(4)) |
| reflection (cosheaf, exact) | $D_3$: Example E | $\log_2 3 - \tfrac23 \approx 0.918$ | components/meet non-commutation (Theorem 37.7) | the ceiling |
| coupling (sheaf, graded) | $D_2$: the pair | $\tfrac32 - \tfrac34\log_2 3 \approx 0.311$ | fiber non-constancy; excess and width (§55) | the coupling — a point of the fiber |

Total admissible synergy: $\approx 2.230$ bits, each summand switchable by its own dial and none by the others'. Marginalizing the prior onto $q$ transports the first row's bit to the third row's address (Theorem 56.2) — the table is a table *per ledger*, which is the resolution in one picture.

---

## 59. Status of Part VII and added references

Part VII has (i) constructed the evaluation functional $\nu_{\mu,q}$ and proved it nonnegative, additive along exactly the concatenations the interval calculus types, null exactly on $q$-null refinements, and jointly faithful over full-support priors — complete where Part V's homological certificate was incomplete, because it evaluates the intervals rather than a shadow — thereby pushing every interval identity of §§37, 46 forward to additive identities in bits (Definition 53.1, Propositions 53.2–53.3); (ii) quantified the cosheaf addresses: the reflection–witness split is additive, the parity/XOR bit is a pure witness quantum ($1$ bit at every arity on the cyclic hierarchy, all-or-nothing), Worked example E carries a pure reflection quantum of $\log_2 3 - \tfrac23$ bits, the support-geometric zero-error instances are filed at the reflection address, and Part VI's policy lever moves exactly one bit (Theorem 54.1, Remark 54.2); (iii) quantified the sheaf address as the fiber excess, with the marginal-forced residual as its complement, vanishing on singleton fibers, realized purely at $\tfrac32 - \tfrac34\log_2 3$ bits on Proposition 22.4(2)'s pair, and — a definitional identification — coinciding with the BROJA synergy measure once ledgers are matched: the BROJA optimization domain *is* the coupling fiber of the prior-marginalized family, so the coupling address's exact, Shannon, and enriched invariants line up as $\sigma^{=}$-fiber-non-constancy, fiber excess, and Le Cam diameter (Definition 55.1, Propositions 55.2–55.4, Remark 55.5); (iv) constructed the ledger functor — §23.2's mechanism (1), typed — and proved the transport theorem: for per-view question-blind deterministic families the entire quantum is witness-addressed at the fine ledger and coupling-addressed at the coarse ledger, refuting any ledger-invariant address assignment and locating the scalar-PID impossibility at the crossing, with the honest delimitation that the located diagnosis is offered as a structural reading of, not a rederivation of, the formal impossibility results (Definition 56.1, Theorem 56.2, Corollary 56.3, Remark 56.4); (v) assembled the stratified decomposition theorem — graded clause, exact clause, pure generators, vanishing loci equal to the named tame loci, principled exclusions of the ledger functor and accumulation — resolving Remark 42.3's conjecture: **proved** in the ledger-relative reading, **refuted** in the ledger-invariant strengthening (Theorem 57.1); (vi) recorded what the decomposition deliberately does not answer — PID's cross-cover allocation question, whose inversion over the redundancy lattice is exactly where nonnegativity dies, whereas chain evaluation keeps it at every arity (Remark 57.2); and (vii) exhibited the three-address ledger on one product configuration, with each quantum switchable by its own dial and the ledger functor visibly moving the witness bit to the coupling address (§58, Worked example I).

What Part VII has *not* done: internal refinement of single addresses — in particular whether the witness class supports a decomposition graded by the missing-face dimension of the nerve hierarchy (§38.3), the natural candidate for a PID *inside* one mechanism; the enriched (deficiency-valued) evaluation functional, for which Proposition 53.2's chain additivity is the target identity and §37's composition law the intended cocycle law — the interval-cohomology program of Part V §43, one coefficient level up; the unified graded-ceiling chain (the exact and graded clauses of Theorem 57.1 glue along the deterministic fiber but are not yet one identity); the untame triple half carried from §51; a treatment of *used* content, where the evaluation functional's dependence on $(\mu, q)$ suggests the long-deferred entry point; and H5, the measure-theoretic pass, and the dynamical scene theory, unchanged from prior ledgers.

**References added in Part VII:**

- Rauh, J., Bertschinger, N., Olbrich, E., and Jost, J. (2014). "Reconsidering Unique Information: Towards a Multivariate Information Decomposition." *Proceedings of the IEEE International Symposium on Information Theory (ISIT 2014)*, 2232–2236.

All other sources — Williams & Beer, Bertschinger–Rauh, Bertschinger–Rauh–Olbrich–Jost–Ay, Le Cam, Torgersen — were already cited; the one addition is the formal impossibility theorem that Remark 56.4 reads structurally.
