# Lines of Flight: Potential New Papers from Registered Information

> **Historical planning document.** The [2026-10-01 proof audit](review/proof-audit.md) and [revised research directions](review/corrections-and-extensions.md) supersede completion claims and mathematical assertions affected by the review. This file is retained as project history.


Several legitimate lines of flight emerge from the present work, but they are not equally mature or equally likely to land well. The best new papers should do more than excerpt another monograph section: each should isolate one object, solve a recognizable problem in an existing literature, and minimize dependence on the full Registered Information vocabulary.

The directions below are ranked by a combination of conceptual importance, readiness, distinctiveness, and publication potential.

## 1. Addressed information decomposition beyond scalar PID

This is the deepest theoretical continuation.

The monograph already establishes that an information quantum can occupy different addresses:

- witness;
- reflection;
- coupling;

and that prior marginalization can move the same quantum between addresses. The natural next step is to build an actual address-valued decomposition rather than another scalar PID.

The paper's central question would be:

> Can multivariate information be decomposed first by obstruction mechanism, and only then internally within each mechanism?

The decisive advance would be a decomposition object such as

$$
\mathcal I =
\mathcal I_{\mathrm{wit}}
\oplus
\mathcal I_{\mathrm{ref}}
\oplus
\mathcal I_{\mathrm{cpl}},
$$

where the entries need not initially be scalars. They might be:

- interval classes;
- filtered vector spaces;
- simplicial invariants;
- fiber-valued quantities;
- or measures indexed by cover shape.

The first concrete target should be the open "PID inside one address" problem. For the witness address, the missing-face dimension of the witness nerve gives a plausible hierarchy:

$$
W_1,\;W_2,\ldots,W_k,
$$

where $W_j$ measures irreducibly $(j+1)$-way witness failure. This could produce a multivariate decomposition that remains nonnegative because it does not force Möbius inversion across mechanistically different objects.

Why this is timely: recent PID work continues to seek scalable or structurally principled alternatives—Blackwell PID, redundancy bottlenecks, synergy-first backbones, and multivariate nonnegative constructions—but generally retains a scalar output or begins from redundancy/synergy as a single species. See [Kolchinsky's redundancy bottleneck](https://pmc.ncbi.nlm.nih.gov/articles/PMC11276267/), the [synergy-first backbone decomposition](https://arxiv.org/abs/2402.08135), and recent work on [multivariate Blackwell-specific decomposition](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120422/).

What would make the paper publishable:

- one explicit address-valued definition;
- existence and nonnegativity;
- recovery of XOR and canonical PID examples;
- an example where scalar PID conflates two mechanisms but the new decomposition separates them;
- a precise relationship—not necessarily equality—to BROJA, Blackwell PID, and synergy-first methods.

**Risk:** High. This requires genuinely new mathematics rather than packaging.

**Potential title:** *Beyond Scalar PID: Information Decomposition by Descent Address*

## 2. Contextual evidence in classical data systems

This may be the monograph's cleanest standalone conceptual paper.

The result to isolate is that classical evidence systems exhibit two different obstruction mechanisms:

- **reflection:** closure or invariant completion fails to commute with combination;
- **witness:** locally valid witnesses fail to admit a global joint witness.

The witness component is characterized by a simplicial nerve, while reflection is invisible to that homology. This gives a precise theorem about the limits of cohomological contextuality detection.

The headline could be:

> Contextuality in ordinary data integration has at least two mechanisms, only one of which is detected by the usual simplicial invariants.

This would speak to contextuality, sheaf theory, databases, distributed sensing, and constraint satisfaction without requiring the entire information-theoretic tower.

A minimal paper would include:

1. finite contrast systems and invariant readings;
2. cover defects;
3. the reflection–witness factorization;
4. the witness nerve;
5. the $\partial\Delta^k$ hierarchy;
6. an explicit example with a reflection obstruction but trivial homology;
7. a comparison with distributional marginal contextuality.

That last distinction is essential: exact reading/content descent is cosheaf-shaped, whereas probabilistic marginal descent is sheaf-shaped. Treating both in one paper could clarify a real ambiguity in the literature.

There is active adjacent work on stochastic-extension and preparation contextuality, including a 2026 preprint that emphasizes nonunique stochastic extension. Our empty/non-singleton coupling-fiber distinction is closely adjacent, so the paper would need to distinguish its exact obstruction factorization and classical data-integration focus clearly. See [Sheaf-Theoretic Preparation Contextuality](https://arxiv.org/abs/2605.00975). Valuation-algebra contextuality is also an important predecessor: [Non-locality, contextuality and valuation algebras](https://pmc.ncbi.nlm.nih.gov/articles/PMC6754714/).

**Potential title:** *Reflection and Witness: Two Obstructions to Global Evidence*

**Risk:** Moderate. Much of the theorem stock already exists, but priority positioning needs care.

## 3. A statistical theory of registered content estimation

This is probably the strongest near-term paper.

The empirical paper currently combines several ideas—characterization, definition selection, anchoring, estimation, images, and text. A sharper statistics paper could isolate the fundamental estimation problem:

> Given samples from a family of channels, when can we recover registered distinctions, obstruction addresses, and deficiency-valued evaluations with finite-sample guarantees?

The current repository already contains the beginning:

- resolution-margin recovery of $\sigma^=$;
- Shannon continuity versus deficiency Lipschitzness;
- coupling-fiber stability;
- refusal rules;
- half-gap certification;
- hardest-pair characterization bounds.

A dedicated paper could provide:

- minimax upper and lower bounds for recovering $\sigma^=$;
- adaptive clustering when the resolution margin is unknown;
- simultaneous confidence sets for the registered partition;
- uncertainty sets for coupling fibers;
- confidence intervals for $C$, $S_\delta$, and cover defects;
- local alternatives near stratum changes;
- sample-complexity lower bounds showing when refusal is unavoidable.

The strongest statistical object may be a confidence set in the partition lattice:

$$
\Pr\!\left(
\underline{\sigma}_n
\le \sigma^=
\le \overline{\sigma}_n
\right)\ge 1-\alpha.
$$

That is much more faithful than forcing a potentially unstable point estimate. It also naturally implements the framework's anti-overclaiming discipline.

**Potential title:** *Estimating Information Structures: Confidence Sets for Registered Content*

**Risk:** Moderate-low. The current paper and code supply a credible base, but proper minimax results would lift it substantially.

## 4. Scalable Le Cam synergy

This is the most natural sequel to the second paper.

The existing Le Cam synergy paper defines a strong object but leaves several computational and analytic questions open:

- efficient multivariate computation;
- Gaussian closed forms;
- continuous-variable estimation;
- decomposition across source subsets;
- computation of the fiber diameter $W_\delta$;
- conditional or local Le Cam synergy.

The best version would not introduce another definition. It would make $S_\delta$ usable.

### 4.1 Gaussian theory

Derive $S_\delta$ for Gaussian experiments, ideally in terms of covariance or canonical-correlation objects. Gaussian PID remains active, and existing methods can over- or underestimate synergy in some regimes. See the recent [information-geometric Gaussian PID](https://pubmed.ncbi.nlm.nih.gov/39056905/).

### 4.2 Dual optimization

Exploit the randomization-criterion dual to compute $S_\delta$ through adversarial decision problems. This could yield:

- interpretable certificates;
- cutting-plane algorithms;
- sparse witnesses;
- scalability beyond the direct channel LP.

### 4.3 Variational estimation

Learn the simulating channel and adversarial loss jointly:

$$
\min_M\max_{t,\ell}
\left[
R_\ell(ME_\otimes)-R_\ell(E_P)
\right].
$$

The result could resemble modern adversarial representation learning while retaining exact decision-theoretic semantics.

**Potential title:** *Scalable Operational Synergy via Statistical Deficiency*

**Risk:** Moderate. Strong potential if accompanied by code, benchmark comparisons, and either a Gaussian theorem or a scalable dual algorithm.

## 5. Registered feature selection under non-submodularity

The empirical paper contains a result that deserves its own machine-learning treatment:

> Conditional independence gives submodularity; coupling-addressed information measures and bounds its failure.

Recent work applies PID directly to feature selection and interpretability, but our contribution would be more structural: it explains exactly when greedy selection is licensed and supplies an audit when it is not. Compare recent [PID for feature selection and interpretability](https://arxiv.org/abs/2405.19212).

A focused paper could develop an algorithm:

1. perform ordinary greedy selection;
2. estimate conditional coupling components among stalled candidates;
3. construct candidate bundles when the audit fires;
4. continue with singleton-plus-bundle selection;
5. return a certificate bounding missed value.

The theoretical result could strengthen the existing $\beta$-bounded greedy theorem into an adaptive approximation guarantee based on the actually observed coupling audit rather than a global worst-case $\beta$.

A compelling application would be spurious-feature detection. Current work is already combining PID and Blackwell sufficiency with dataset spuriousness, so our distinctive angle should be:

- contrast-domain dependence;
- decoder-relative extractability;
- bundle detection;
- and certified greedy failure.

See [Formalizing Spuriousness of Biased Datasets using PID](https://openreview.net/forum?id=vmkpk0ed1F).

**Potential title:** *When Greedy Feature Selection Fails: Coupling Certificates and Synergistic Bundles*

**Risk:** Low-moderate. This is accessible, testable, and close to existing code.

## 6. Provenance from commitment and shared randomness

This is the strongest security/distributed-systems line.

The monograph's dynamical result says that timestamps or causal order alone do not establish provenance: a forger can run the policy. Provenance becomes identifiable only through commitment plus shared registration noise, which forces a detectable coupling gap.

That can become a paper about authenticated sensing or audit logs:

> Provenance is not an intrinsic property of a record; it is a property of a committed coupling between records.

The theory should be generalized from the canonical binary example to:

- arbitrary finite alphabets;
- multiple sensors;
- partial compromise;
- delayed or lossy commitment;
- optimal shared-noise design;
- adversaries with bounded causal knowledge;
- sequential error exponents.

A clean theorem would characterize when a commitment scheme produces a strictly positive separation

$$
\inf_{\text{causal forgeries}}
\Delta(P_{\mathrm{auth}},P_{\mathrm{forge}})>0.
$$

The practical application could be sensor networks, laboratory audit trails, federated data provenance, or model-evaluation logs.

**Potential title:** *Provenance Is a Coupling: Commitment, Shared Noise, and Sequential Forgery Detection*

**Risk:** Moderate-high because it requires engagement with cryptographic and authentication literatures not yet represented in the monograph. The core idea, however, is distinctive.

## 7. Ambiguous and set-valued experiments as ideal-valued content

The monograph repeatedly finds the same obstruction:

- budget constraints yield nonprincipal admissibility sets;
- approximate answerability is down-set-valued;
- Blackwell joins may not exist;
- coupled corruption yields antichains.

Ideal completion repairs all four, at the price of representability.

This could become an elegant decision-theory paper:

> When an experiment is uncertain, constrained, or only partially specified, its natural information content is not one experiment but a down-set of experiments.

Recent work generalizes Blackwell comparison to ambiguous experiments, showing that this is an active problem. See [Informativeness orders over ambiguous experiments](https://www.sciencedirect.com/science/article/pii/S0022053124001431).

Our distinct contribution would be order-theoretic:

- ideal-valued experiments;
- representability criteria;
- joins restored by ideal completion;
- admissibility and ambiguity handled in the same object;
- exact relation to robust decision problems.

A central theorem could identify when an ideal-valued content is principal—when ambiguity admits a single sufficient representative—and measure failure of principality otherwise.

**Potential title:** *Ideal-Valued Statistical Experiments: Information under Ambiguity and Constraints*

**Risk:** High but intellectually strong. It could connect the monograph to mathematical economics and robust statistics.

## 8. The algebraic boundary between reusable and accumulating information

The monograph identifies accumulation with failure of Kohlas idempotency:

$$
N\otimes N\not\simeq N.
$$

This suggests a focused algebra paper about the transition from information algebras to valuation algebras.

The interesting question is not merely that quantitative evidence is non-idempotent—that is known—but:

> Can the amount and type of idempotency failure be classified using the framework's exact, Shannon, and deficiency rungs?

One could define an accumulation defect

$$
a(\phi)=d(\phi,\phi\otimes\phi)
$$

and ask for:

- monotonicity;
- subadditivity;
- behavior under focusing;
- factorization across products;
- fixed points;
- recovery of exact information algebras as the zero locus;
- relations to independent replication and experiment comparison.

This would enrich the algebra literature by turning the qualitative information-algebra/valuation-algebra boundary into a graded geometric boundary.

**Potential title:** *The Geometry of Idempotency Failure in Information and Valuation Algebras*

**Risk:** Moderate-high. It needs careful comparison with existing valuation-algebra theory, where idempotency is already recognized as the qualitative/quantitative dividing line.

## 9. Causal robustness of information attacks

The causal-gap theorem could seed a paper at the intersection of information theory, robust statistics, and online control.

The central phenomenon is:

- a clairvoyant adversary can tailor corruption to future class-relevant information;
- a causal adversary must act before that information is available;
- front-loading class-straddling content increases the required corruption mass.

The paper could develop a general causal annihilation threshold:

$$
\varepsilon^*_{\mathrm{causal}}
=
\inf\{\varepsilon:
\text{an adapted corruption makes the target classes indistinguishable}\}.
$$

Then characterize the causal premium

$$
\varepsilon^*_{\mathrm{causal}}
-
\varepsilon^*_{\mathrm{clairvoyant}}
$$

through filtrations, predictable projections, or conditional total variation.

This would make "front-load informative distinctions" into a theorem for robust sequential experiment design.

**Potential title:** *Causal Information Annihilation and the Value of Front-Loaded Evidence*

**Risk:** High, but potentially important if a general characterization replaces the current exhibit.

## Recommended portfolio

The recommended pursuit order is:

1. **Statistical estimation of registered content** — most mature and easiest to establish independently.
2. **Reflection and witness obstructions** — strongest clean theoretical extraction.
3. **Scalable Le Cam synergy** — natural continuation with a visible contemporary audience.
4. **Coupling-certified feature selection** — strongest applied and machine-learning route.
5. **Address-valued PID** — deepest long-term theoretical project.
6. **Provenance as coupling** — high-upside interdisciplinary paper.

The most valuable strategic distinction is:

- Papers 1–4 convert existing monograph capital into independently useful results.
- Papers 5–9 require substantial new theorem development and genuinely extend the framework.

If choosing only one ambitious new direction, the recommendation is **address-valued PID**. If choosing the next paper most likely to become complete and publishable quickly, the recommendation is **confidence sets and finite-sample inference for registered content**.
