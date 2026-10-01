# Proof-by-proof audit of the monograph

Reviewed 2026-10-01, restricted to `docs/information_theory`. This inventory covers every numbered Fact, Lemma, Proposition, Theorem, and Corollary in Parts I–XI. Definitions, examples, prose claims, and Appendices A–D were also checked for their role in the arguments; the appendix dispositions appear below. This is a finite mathematical audit, not formal verification. No claim that all original statements were sound is intended.

**Integration completed.** The monograph's current statements and proofs incorporate the corrections directly; readers no longer need to override theorem text with review qualifications. The V/Q/X/C codes below record the disposition of the **original** 136 results, not unresolved TODOs. [Appendix D](../monograph/registered-information-appendix-D.md) is authoritative for D.1–D.13 (15 numbered statements including subordinate lemmas); Appendix A contains Proposition A.1. The older R1–R7 labels in the review map to D.1–D.7. Classical imported results remain explicitly cited dependencies.

Status key:

- **V — verified:** the finite argument follows under the stated and inherited assumptions; the row identifies its proof mechanism.
- **Q — qualified/repaired:** the result requires the recorded correction, scope condition, or proof repair.
- **X — replaced:** a former stronger conclusion is false or unproved; the text supplies the narrower valid result.
- **C — cited:** an external theorem is explicitly imported; the manuscript proves only the indicated direction.

The principal structural assumptions are finite nonempty state/output spaces, coherent joint channels, full-support priors when an almost-sure statement is converted to an everywhere statement, and finite view sets (or the explicit full-subset extension) for adjunction claims. Covers in the witness analysis are nonempty covering families; this does not prevent them from covering the empty object. “Pure witness” at the graph level must not be substituted for a nondegenerate interval after taking components.

## Part I: exact kernel

| Result | Status | Proof check / required correction |
|---|---|---|
| [Fact 3.1](../monograph/registered-information-kernel.md) | V | Quotient by equal fibers gives a well-defined injection and unique image factorization. |
| [Fact 3.2](../monograph/registered-information-kernel.md) | V | Define the decoder on each realized fiber; constancy is necessary and sufficient. |
| [Fact 3.3](../monograph/registered-information-kernel.md) | V | Intersection of equivalences gives the information join; transitive closure of their union gives the meet, including empty-family conventions. |
| [Fact 3.4](../monograph/registered-information-kernel.md) | V | Adjunction inequalities yield the closure/interior identities and fixed-point isomorphism; completeness follows when both ambient posets are complete. |
| [Lemma 4.4](../monograph/registered-information-kernel.md) | V | Composition proves preorder laws; the fiber factorization criterion proves equivalence with refinement. |
| [Lemma 4.7](../monograph/registered-information-kernel.md) | V | Soundness forces the canonical fiber to lie in each registered piece. This is pointwise constraint informativeness, not uniqueness of every lossless registration. |
| [Lemma 5.3](../monograph/registered-information-kernel.md) | V | Equality of canonical fibers is exactly equality of all observed view values. |
| [Proposition 5.6](../monograph/registered-information-kernel.md) | V | Apply fiber constancy to the joint representation; the induced decoder is unique only on realized profiles. |
| [Theorem 6.2](../monograph/registered-information-kernel.md) | V | A join is below a partition iff each generating kernel is below it; achievable partitions are fixed points, with internal meets rather than necessarily ambient meets. |
| [Proposition 6.3](../monograph/registered-information-kernel.md) | V | The paired fiber is the intersection of the two fibers at the same candidate. |
| [Theorem 6.4](../monograph/registered-information-kernel.md) | Q | Principal ideal proof is valid; arbitrary ambient meets must exclude the empty meet unless the ideal top is ambient top. |
| [Theorem 6.5](../monograph/registered-information-kernel.md) | V | A new view helps precisely by separating unresolved pairs; necessary and sufficient conditions are the fiber criterion again. |
| [Theorem 6.7](../monograph/registered-information-kernel.md) | V | The canonical quotient and the joint profile determine each other; every factor consolidation maps uniquely from the quotient in the stated direction. |
| [Corollary 6.8](../monograph/registered-information-kernel.md) | V | Apply the answerability inequality to every question, then use the join universal property. |
| [Corollary 6.9](../monograph/registered-information-kernel.md) | V | Nonanswerability is witnessed by a same-profile pair with different question values. |
| [Corollary 6.10](../monograph/registered-information-kernel.md) | V | A total correct decoder cannot distinguish such a pair; R1 adds the maximal safe partial decoder. |
| [Proposition 6.11](../monograph/registered-information-kernel.md) | Q | Generalized set information algebra supported by the saturation identity now supplied; arbitrary focusing need not commute. R2 separates join closure from least supports. |

## Part II: admissibility

| Result | Status | Proof check / required correction |
|---|---|---|
| [Proposition 12.1](../monograph/registered-information-part-II.md) | Q | Reflexivity, augmentation, and transitivity follow from join inequalities. This proves soundness, not completeness for an arbitrary fixed dependency basis. |
| [Lemma 14.2](../monograph/registered-information-part-II.md) | V | A registration is a function of a presentation, so equality of presentations implies equality of registered pieces. |
| [Lemma 14.4](../monograph/registered-information-part-II.md) | V | Assign each realized profile its containing rho-block; rho below raw content makes this well-defined and sound. |
| [Proposition 14.4′](../monograph/registered-information-part-II.md) | V | These canonical block registrations realize every allowed partition; upward transport preserves the registered distinctions under monotone ceilings. |
| [Proposition 14.6](../monograph/registered-information-part-II.md) | V | Every singleton ceiling lies below the joint ceiling by monotonicity, and the joint ceiling lies below the raw partition by definition. |
| [Theorem 15.1](../monograph/registered-information-part-II.md) | Q | Singleton-generated content is a left adjoint on all subsets. Its terminal quotient is for registered ceiling outputs, not necessarily raw views. |
| [Proposition 15.2](../monograph/registered-information-part-II.md) | V | Canonical ceiling-realizing combinations attain the join of singleton ceilings; monotonicity bounds every separable reading. |
| [Corollary 15.4](../monograph/registered-information-part-II.md) | Q | Join preservation implies a right adjoint on the complete subset lattice. Require finite V or the stated extension from finite subsets, and grounding for the empty join. |

## Part III: experiments

| Result | Status | Proof check / required correction |
|---|---|---|
| [Fact 20.1](../monograph/registered-information-part-III.md) | V | Finite factorization follows by conditioning on each realized statistic value; zero-probability fibers can be defined arbitrarily. |
| [Lemma 21.7](../monograph/registered-information-part-III.md) | V | Identical rows overlap in support; a zero-error decoder must be constant on overlap components; graded order refines these shadows. |
| [Theorem 22.1](../monograph/registered-information-part-III.md) | V | Connected overlap paths force equal answers. Conversely every output's possible states lie in one component, giving a decoder. |
| [Theorem 22.2](../monograph/registered-information-part-III.md) | V | Finitely many unequal rows have positive minimum separation; empirical frequencies identify the row class uniformly. Equal rows cannot be separated at any sample size. |
| [Proposition 22.3](../monograph/registered-information-part-III.md) | V | Marginalization sends joint overlap edges into each marginal graph; under conditional independence the edge relation is the intersection, whose components can refine the joined component partitions. |
| [Proposition 22.3′](../monograph/registered-information-part-III.md) | Q | The graph retains the overlap relation. Under reversed edge inclusion, component formation is a right adjoint, although the closure mechanism is informally called reflection. |
| [Proposition 22.4](../monograph/registered-information-part-III.md) | V | Equal joint laws imply equal marginals; a conditionally independent joint is determined by them. The equal-versus-independent bit example gives strictness without CI. |
| [Proposition 22.5](../monograph/registered-information-part-III.md) | Q | Monotonicity and upper-bound claims hold. Binary-state experiments are a lattice; failure of joins is a general larger-state phenomenon, not universal. |
| [Theorem 22.6](../monograph/registered-information-part-III.md) | V | Proportional likelihood columns are exactly the finite minimal sufficient statistic classes; normalization gives a common reconstruction kernel on each class. |
| [Theorem 22.7](../monograph/registered-information-part-III.md) | V | Full-support prior turns vanishing conditional entropy into an everywhere finite decoder; vanishing MI is equality of all relevant conditional laws. The bounds are data processing. |
| [Proposition 23.3](../monograph/registered-information-part-III.md) | Q | Independent replication of the noisy ceiling gives strict accumulation. Corrected posterior witness is a concordant posterior outside the one-copy range, not posterior one half. Distinct view indices represent independent looks. |
| [Proposition 23.5](../monograph/registered-information-part-III.md) | V | The accumulation axiom places every separable reading below the joint ceiling; data processing gives the information bracket. |
| [Lemma 24.1](../monograph/registered-information-part-III.md) | V | A garbling of a deterministic map can yield another deterministic map only if it is constant on the original fibers. |
| [Theorem 24.2](../monograph/registered-information-part-III.md) | V | Deterministic marginals force the unique paired point mass; all three content strata then agree. No arbitrary infinite-noise limit is being asserted. |
| [Proposition 24.4](../monograph/registered-information-part-III.md) | Q | Singleton-generated join formula gives the adjunction on the full subset lattice; finite-subset-only formulations require the stated finite/extension convention and grounding. |

## Part IV: anchoring

| Result | Status | Proof check / required correction |
|---|---|---|
| [Lemma 27.4](../monograph/registered-information-part-IV.md) | V | When the true origin is absent from the compatible correspondence, every admissible verdict is wrong; integrate that event. |
| [Proposition 27.5](../monograph/registered-information-part-IV.md) | V | Loyal tracked-target policies attain the irreparable floor for every emission law; the converse uses an emission concentrated on a disloyal input. The identity example has error profiles (1-a,a), an antichain with no simultaneous floor attainment. |
| [Lemma 27.7](../monograph/registered-information-part-IV.md) | V | Compose statistical simulators; garbling preserves row equality and cannot disconnect states linked by support overlap. |
| [Proposition 27.8](../monograph/registered-information-part-IV.md) | V | Record projections give the garbling hierarchy; attribution can be simulated from the full evidence using the fixed policy kernel. |
| [Corollary 28.1](../monograph/registered-information-part-IV.md) | V | Apply the already proved zero-error and repeated-sampling criteria to each record channel separately. |
| [Proposition 28.2](../monograph/registered-information-part-IV.md) | V | The constant-presentation/candidate-revealing-verdict construction satisfies the declared correspondence and realizes the separation. |
| [Corollary 28.3](../monograph/registered-information-part-IV.md) | X | Replaced the identification of selective acceptance with forgetting verdicts. Deletion/gap pipelines require their own channel and sampling protocol. |
| [Theorem 29.3](../monograph/registered-information-part-IV.md) | V | Candidate-blind whole-record mixing is an output garbling; a higher rate is a further blind mixture when rates are below one. |
| [Theorem 29.4](../monograph/registered-information-part-IV.md) | V | A common full-support component connects all states; affine mixing with positive honest weight preserves row inequalities; data processing and MI continuity give the remaining finite claims. |
| [Theorem 29.6](../monograph/registered-information-part-IV.md) | V | Candidate-conditioned clutter can implement the exhibited loss, creation, and incomparable channels. No blind-garbling conclusion applies. |
| [Proposition 29.8](../monograph/registered-information-part-IV.md) | Q | Joint blindness gives a joint garbling and positive survival preserves equal-law partitions. Selective replacement need not annihilate zero-error content; the counterexample retains a reveal. |
| [Proposition 30.2](../monograph/registered-information-part-IV.md) | V | The erring acceptance/gap pattern encodes context distinctions absent from the loyal presentation; the explicit decoder proves strict domination. |
| [Theorem 30.4](../monograph/registered-information-part-IV.md) | Q | Sterility provides a candidate-independent simulator of every acceptance rule from the loyal record. This is sufficient, not a necessary condition in each fixed model. |
| [Proposition 30.6](../monograph/registered-information-part-IV.md) | V | Condition on each available policy input and minimize posterior error over its allowed verdicts; randomized choices cannot improve a finite linear objective. |
| [Theorem 32.1](../monograph/registered-information-part-IV.md) | X | Replaced unconditional all-record collapse by the exact projection relations and a sterile-context recovery condition; small targeted corruption also converges in deficiency. |

## Part V: descent

| Result | Status | Proof check / required correction |
|---|---|---|
| [Lemma 35.2](../monograph/registered-information-part-V.md) | Q | Positive union covers pull back by intersections; determination covers need not. Empty covers are excluded for consistency with the witness sheaf. |
| [Proposition 35.4](../monograph/registered-information-part-V.md) | Q | Stability extends from nested equal-content pairs through their union; use finite achievable content or finite V, and quotient a preorder for literal uniqueness. |
| [Theorem 35.5](../monograph/registered-information-part-V.md) | V | Factor a determination cover into a union cover of its union followed by a redundant inclusion; both implications follow. |
| [Corollary 35.6](../monograph/registered-information-part-V.md) | Q | The gluing equation descends to achievable content. A Grothendieck topology does not follow on a nondistributive lattice without pullback stability. |
| [Proposition 36.3](../monograph/registered-information-part-V.md) | V | Intersecting sound pieces is sound and cannot add distinctions beyond the tuple; canonical ceiling blocks attain the bound. The obstruction is cofinality, not existence of combinations. |
| [Proposition 37.2](../monograph/registered-information-part-V.md) | Q | Refining a cover lowers the joined left endpoint. For empty T use the positive cover containing the empty set; empty members otherwise do not affect grounded endpoints. |
| [Theorem 37.3](../monograph/registered-information-part-V.md) | Q | The singleton cover supplies the maximal defect and the squeeze proves vanishing; its global adjunction conclusion inherits 15.4's domain convention. |
| [Lemma 37.4](../monograph/registered-information-part-V.md) | V | Associativity of joins gives the composite endpoint identity. Vanishing is a joint endpoint condition, so nonzero stage defects can be absorbed. |
| [Theorem 37.5](../monograph/registered-information-part-V.md) | V | Orbit moves and joint-indistinguishability edges generate exactly the lifted graph components, in both directions. |
| [Corollary 37.6](../monograph/registered-information-part-V.md) | V | Every ceiling is the meet of raw content with the orbit partition; equal orbit partitions therefore give equal ceilings, defects, and graph decompositions, independently of the acting group. |
| [Theorem 37.7](../monograph/registered-information-part-V.md) | V | Nested edge relations give the three ordered component partitions; parity and the explicit three-orbit example realize the two strict intervals separately. |
| [Lemma 38.1](../monograph/registered-information-part-V.md) | Q | Inclusion restrictions force a matching family to be one candidate pair, which lies in the total intersection. This needs positive covers and is not the contextuality event presheaf. |
| [Proposition 38.3](../monograph/registered-information-part-V.md) | V | Witness-set intersections define a downward-closed nerve. Full vertices with a missing top face detect an edge defect; component formation can absorb it. |
| [Theorem 38.4](../monograph/registered-information-part-V.md) | Q | The designated-pair formula holds for nonempty view subsets; at the empty context all cross pairs are witnesses. Every proper subset has a witness and the full set does not. The k=1 agreement with parity is at the orbit-graph level, not an isomorphism of raw view partitions; the nerve is a simplex boundary, with the stated reduced homology and two-orbit answerability. |
| [Proposition 38.5](../monograph/registered-information-part-V.md) | X | Replaced the purported equivalence between nerve/homology defects and nondegenerate witness intervals. Missing redundant edges and full nerve families separate these claims. |
| [Theorem 39.2](../monograph/registered-information-part-V.md) | C | Running-intersection conditional products prove sufficiency. Necessity is the cited universal Vorob'ev result; arbitrary fixed degenerate alphabets are excluded from the converse. |
| [Proposition 39.3](../monograph/registered-information-part-V.md) | Q | Empty fibers express nonextendability; varying couplings may change statistical content. Nonconstancy establishes existence of superadditivity somewhere, not at every observed point. |
| [Proposition 39.4](../monograph/registered-information-part-V.md) | V | The exhibited correlated intrusion schedules preserve each marginal channel while varying the joint by candidate; the perceived channel itself need not be candidate-blind. |
| [Proposition 40.1](../monograph/registered-information-part-V.md) | V | Couple honest/perceived draws on no intrusion, use identity simulators, then apply both deficiency triangles and the minimum Lipschitz bound. |
| [Proposition 40.2](../monograph/registered-information-part-V.md) | V | Synchronous versus independent rare intrusions give identical marginals and unequal joint rows at every interior rate, despite distance tending to zero. |
| [Lemma 41.1](../monograph/registered-information-part-V.md) | V | Induction on marginal size cancels all lower-order differences; the remaining coefficient is at least positive no-intrusion mass. |
| [Theorem 41.2](../monograph/registered-information-part-V.md) | V | Marginalizing the replacement mixture produces the induced pattern; injectivity on every marginal preserves equal-law partitions. Existing amalgamations remain amalgamations. |
| [Proposition 41.3](../monograph/registered-information-part-V.md) | V | The rare-intrusion construction already supplies the example for every interior rate; maximal discrete defect is compatible with arbitrarily small metric change. |
| [Theorem 42.1](../monograph/registered-information-part-V.md) | Q | Full admissibility makes combinations cofinal; deterministic marginals have a unique joint and pairwise witness nerves are simplexes. This does not identify full context with presentations without 32.1's extra hypothesis. |

## Part VI: interactions

| Result | Status | Proof check / required correction |
|---|---|---|
| [Proposition 45.2](../monograph/registered-information-part-VI.md) | V | Exact record partitions are joins of their atom kernels; leak and sterility statements follow from factorization through the presentation. |
| [Theorem 45.4](../monograph/registered-information-part-VI.md) | V | All-determination closure, determination monotonicity, and factorization through raw content are equivalent using canonical realizing registrations and union comparison. |
| [Corollary 45.5](../monograph/registered-information-part-VI.md) | Q | The iff concerns every determination. Monotone forgetful ceilings already pass nested record-ladder closure; repackaging invariance is the failing property. |
| [Proposition 46.2](../monograph/registered-information-part-VI.md) | V | The policy-independent feature restriction recovers the prior theory; the cross-layer identity is associativity of the joined partitions. |
| [Theorem 46.3](../monograph/registered-information-part-VI.md) | V | Directly compute the four-candidate kernels: each local admissible partition is null while the feature/verdict pair recovers the orbit question; adjoining its answer absorbs the defect. |
| [Proposition 46.4](../monograph/registered-information-part-VI.md) | Q | Deleting sterile atomic views preserves raw content for N-complete sets. Comparing cover defects requires each cover member, not merely its union, to be N-complete. |
| [Proposition 47.1](../monograph/registered-information-part-VI.md) | Q | For a fixed decoder the blind affine mixture preserves row equality. Output-ceiling-defined admissible decoder classes may change, and ceiling realizability must be rechecked. |
| [Theorem 47.3](../monograph/registered-information-part-VI.md) | Q | A fixed decoder equalizing all clutter reduces it to common blind contamination. This is a sufficient robustness mechanism, not an iff characterization. |
| [Proposition 47.4](../monograph/registered-information-part-VI.md) | V | Choose rate one at each candidate; equality with every allowed clutter forces the decoded honest row to be the same at every state. |
| [Proposition 48.1](../monograph/registered-information-part-VI.md) | Q | Product preprocessing composes with each local decoder and invokes honest accumulation closure. This bounds readings; it need not make the old ceiling realizable. R6 extends the sufficient criterion. |
| [Proposition 48.2](../monograph/registered-information-part-VI.md) | V | Compose each admissible accepted-record reading with the sterile simulator from the loyal record; the output experiment and its ceiling bound are unchanged. |
| [Theorem 50.1](../monograph/registered-information-part-VI.md) | Q | Recovery uses the corrected record-collapse hypotheses of 32.1. Context cannot be discarded solely because attribution is uniquely correct. |

## Part VII: Shannon evaluation

| Result | Status | Proof check / required correction |
|---|---|---|
| [Proposition 53.2](../monograph/registered-information-part-VII.md) | V | Partition refinement gives conditional-information increments; full support makes a strict interval detectable by some question. Supremum over questions is not positivity for every fixed question. |
| [Proposition 53.3](../monograph/registered-information-part-VII.md) | V | Mutual-information potential differences telescope; the identities follow along the specified ordered exact-partition chain. |
| [Theorem 54.1](../monograph/registered-information-part-VII.md) | V | The examples reduce to an orbit bit or a binary component partition. Uniform three-orbit reflection gives the indicated binary entropy; hierarchy arity does not change the two-orbit bit. |
| [Proposition 55.2](../monograph/registered-information-part-VII.md) | V | The observed coupling is feasible, and marginalization gives the lower bound by each source MI; a singleton fiber forces zero excess. |
| [Proposition 55.3](../monograph/registered-information-part-VII.md) | V | The null independent coupling attains zero minimum; the actual two-row entropy calculation gives 3/2 minus (3/4)log2(3). |
| [Proposition 55.4](../monograph/registered-information-part-VII.md) | V | For two sources the fixed target/source marginals are exactly the coarse fiber constraints in the stated BROJA complementary-information definition. |
| [Theorem 56.2](../monograph/registered-information-part-VII.md) | Q | Fine determinism gives singleton fiber; coarse source blindness permits a target-independent product with zero MI. A witness address additionally needs a specified invariance ceiling and graph calculation. |
| [Corollary 56.3](../monograph/registered-information-part-VII.md) | Q | Parity disproves preservation of its assigned fine/coarse addresses. This is not a general impossibility theorem for ordinary PID axioms without additional premises. |
| [Theorem 57.1](../monograph/registered-information-part-VII.md) | Q | Exact interval evaluation telescopes and fiber excess has its own identity. They do not automatically form one additive invariant; zero excess need not mean singleton fiber. |

## Part VIII: corruption and design

| Result | Status | Proof check / required correction |
|---|---|---|
| [Theorem 61.1](../monograph/registered-information-part-VIII.md) | V | Explicit joint/marginally blind coupling attacks defeat the ceiling bracket. They prove failure examples, not necessity of independence in all robust models. |
| [Proposition 61.2](../monograph/registered-information-part-VIII.md) | X | Binary incomparability did not prove missing suprema. Adequate transfer is an upper-bound problem; nonexistence for a realized restricted class remains open. R5 solves the unconstrained fiber equivalence. |
| [Lemma 62.1](../monograph/registered-information-part-VIII.md) | Q | L1 mass balance gives epsilon at least d/(2+d); positive/negative parts construct attaining clutter. Survival transfers only to fixed decoders informative before corruption. |
| [Theorem 62.2](../monograph/registered-information-part-VIII.md) | Q | Keep whole-record targeted and independent-coordinate blind contamination models separate. Full joint support, not marginal positivity alone, ensures zero-error extinction. |
| [Theorem 62.3](../monograph/registered-information-part-VIII.md) | V | The candidate-dependent verdict pattern reproduces the erring record on a loyal substrate with no retained co-registered variable; provenance is extra information in this model. |
| [Proposition 63.1](../monograph/registered-information-part-VIII.md) | V | Determination-stable value depends on the verdict partition; swapping truth assignments can change error while preserving that partition. |
| [Theorem 63.2](../monograph/registered-information-part-VIII.md) | Q | Fano bounds extra value after the baseline gap S0. The one-bit/half-error corollary requires S0=0 and the effective realized binary alphabet. |
| [Proposition 63.3](../monograph/registered-information-part-VIII.md) | V | All four context-to-verdict maps are enumerated; both intermediate maps have the same kernel/value and complementary cost. |
| [Corollary 63.4](../monograph/registered-information-part-VIII.md) | Q | The design/counterfeit conclusion is for the stated attack and retained-record model, not an impossibility of external or co-registered certification. |
| [Theorem 65.1](../monograph/registered-information-part-VIII.md) | Q | Zero-rate recovery and full admissibility hold; unique anchoring fixes policies on realized inputs only and retains the sterile-context caveat for record equivalence. |

## Part IX: deficiency

| Result | Status | Proof check / required correction |
|---|---|---|
| [Proposition 68.2](../monograph/registered-information-part-IX.md) | Q | LP compactness, identity, and triangle arguments hold; corrected simulator orientation proves containment monotonicity. |
| [Proposition 68.3](../monograph/registered-information-part-IX.md) | V | Transport an optimal decision rule through any simulator; bounded-loss TV control gives the lower certificate. Equality uses finite randomization duality, not the inequality alone. |
| [Proposition 69.1](../monograph/registered-information-part-IX.md) | V | Uniform splitting supplies the upper simulator; uniform representatives in a maximally split block give the matching guessing lower bound. Independently LP-checked on small partitions. |
| [Proposition 69.2](../monograph/registered-information-part-IX.md) | V | Every nontrivial deterministic split has at least two blocks. Only a strictly positive value below one half certifies a nondeterministic-equivalent interval; zero does not. |
| [Theorem 69.3](../monograph/registered-information-part-IX.md) | V | The three-state chain has leg values one half and span two thirds; the resulting positive triangle defect is not an additive potential difference. |
| [Theorem 69.4](../monograph/registered-information-part-IX.md) | Q | An attaining decision problem for the span proves necessity of a common tight certificate; common tightness proves sufficiency. Binary erasure geodesic calculation generalizes with factor 1-1/k. |
| [Proposition 70.1](../monograph/registered-information-part-IX.md) | V | Simulation can only increase Bayes risk; ordered experiments obey MI data processing. A particular question need not detect every strict experiment inequality. |
| [Theorem 70.2](../monograph/registered-information-part-IX.md) | V | The midpoint simulator and binary guessing loss give null-to-BSC deficiency; binary entropy and Taylor expansion give the stated square law on this class. |
| [Proposition 71.1](../monograph/registered-information-part-IX.md) | V | Independent blind bit corruption multiplies the parity bias; targeted cancellation and counterfeit creation give the three exhibited curve shapes. |
| [Proposition 71.2](../monograph/registered-information-part-IX.md) | V | Independent erasures fail only on double erasure, producing delta squared over two; the binary null/full couplings attain the fiber width one half. |

## Part X: dynamics

| Result | Status | Proof check / required correction |
|---|---|---|
| [Proposition 75.4](../monograph/registered-information-part-X.md) | Q | Finite trajectories form a contrast domain. Stochastic causal families need joint causal factorization; marginal prefix-measurability alone can hide future-dependent couplings. |
| [Theorem 76.1](../monograph/registered-information-part-X.md) | V | Chain rule bounds verdict-stream information by sum of conditional entropies; Fano at each round and concavity give the horizon-averaged bound. |
| [Theorem 76.2](../monograph/registered-information-part-X.md) | V | The exhaustive four memoryless policies give (0,0), (1/2,1/2), (1/2,1/2), (1,0); the specified adaptive policy gives (1/4,1/2), independently reconstructed. |
| [Corollary 76.3](../monograph/registered-information-part-X.md) | Q | The exhibit demonstrates a frontier improvement subject to the universal rate bound. It is not a universal formula for the value of history in every model. |
| [Theorem 77.1](../monograph/registered-information-part-X.md) | Q | Feasible-set inclusion gives the causal inequality; the two-bit single-record example attains thresholds one half versus d/(2+d). Arbitrary per-slot models require their own program. |
| [Corollary 77.2](../monograph/registered-information-part-X.md) | X | Replaced a universal front-loading interpretation with the stated single-record exhibit and its interior beta hypotheses. |
| [Theorem 78.1](../monograph/registered-information-part-X.md) | Q | A causal forger can reproduce the policy only when its allowed inputs/randomness can simulate the relevant conditional laws and no retained co-registration constraint prevents it. |
| [Theorem 78.3](../monograph/registered-information-part-X.md) | Q | A positive honest-versus-forged coupling gap is essential. The Bhattacharyya coefficient is at most 1/sqrt(2), equal only for uniform forged bits; product bounds require iid rounds. R7 handles adaptive precommitment directly. |
| [Theorem 80.1](../monograph/registered-information-part-X.md) | Q | Horizon one removes history/future distinctions but can retain a one-round commitment/shared-noise gap. The resource itself must be removed to recover perfect static counterfeit. |

## Part XI: domain transport and synthesis

| Result | Status | Proof check / required correction |
|---|---|---|
| [Lemma 83.2](../monograph/registered-information-part-XI.md) | Q | Pullback preserves joins and nonempty ambient meets; the empty meet belongs internally to the ideal. Trace is meet-lax; product relations factor by coordinate paths. Prior averaging is a different operation. |
| [Proposition 83.3](../monograph/registered-information-part-XI.md) | Q | Apply the transport laws to joins of kernels. Saturation is left adjoint in subset order and right adjoint in reversed information order. |
| [Theorem 83.5](../monograph/registered-information-part-XI.md) | Q | The generalized labeled set algebra is supported; vacuous-extension and trace identities follow blockwise. Least support requires ambient meet closure, not merely join closure. The common scene must have specified surjections to its member domains; a pair of quotient maps need not surject onto their Cartesian product. |
| [Theorem 84.1](../monograph/registered-information-part-XI.md) | Q | Independent tensor is a well-defined nonidempotent operation; arbitrary chosen couplings do not define a binary operation on Blackwell classes. No full graded valuation-algebra axiomatization is proved. R3 gives the precise tensor-idempotent locus. |
| [Proposition 84.2](../monograph/registered-information-part-XI.md) | X | Replaced closure equivalence with cofinality: monotone admissible exact readings already combine; separability asserts that combinations dominate all joint readings. |
| [Theorem 85.1](../monograph/registered-information-part-XI.md) | X | Replaced the global collapse/commuting-axes assertion with separate finite recovery statements. Averaging, context, and noisy classical information preclude the former universal conclusion. |
| [Theorem 88.1](../monograph/registered-information-part-XI.md) | Q | The one-domain recovery uses a join-closed generated family. Taking an ambient meet-closed sublattice can enlarge Ach and destroy the claimed verbatim identification. |

## Appendices and additions

| Item | Disposition |
|---|---|
| Appendix A, former measure-theoretic pass | Withdrawn as a blanket extension. Replaced with Proposition A.1, whose dominating measure, likelihood statistic, and common disintegration kernel prove finite-state Borel sufficiency, plus explicit unresolved hypotheses. |
| Appendix B, finite programs and certificates | LP formulation checked. Repeated-BSC posterior explanation corrected. Historical machine-verification claims distinguished from the new review run. The repeated-BSC value now additionally has an explicit optimal simulator and decision-problem certificate in B.6. |
| Appendix C, vocabulary | Read under the corrected distinctions: positive covers; graph defect versus component interval; down-set versus directed ideal; generalized set algebra versus a graded valuation algebra; exact/graded half-gap excludes zero. |
| R1, certified partial answer | Fiberwise necessity and sufficiency, maximality by inclusion, and full-support probability uniqueness. |
| R2, saturation and support | Blockwise saturation identity and nested focusing; equivalence-path proof for meet supports; explicit counterexample to join-only least support. |
| R3, replication idempotency | Equality in mutual-information data processing forces overlapping rows to coincide; common-row simulation proves all converses. |
| R4, averaging and lifting | Image inclusion of compact finite coupling polytopes, objective preservation, attainment, and convexity of TV. |
| R5, least coupling and join | Simulate all marginals conditionally on an arbitrary upper bound, then use the least-element universal property in both directions. |
| R6, budget transfer | Branchwise admissible composite decoders give branch simulators; their candidate-independent mixture gives the final simulator. |
| R7, committed-bit minimax test | Conditional match probabilities give an upper risk for adaptive forgers; the independent fair forger gives the matching simple-testing lower bound. |

## Added appendix proof inventory

| Result | Proof check |
|---|---|
| [Proposition A.1](../monograph/registered-information-appendix-A.md) | A common dominating measure and regular conditional law reconstruct every finite-state observation measure from its likelihood statistic. |
| [Theorem D.1](../monograph/registered-information-appendix-D.md#d1-maximal-certified-partial-answer) | Fiber constancy proves the maximal safe partial decoder; full support gives probability-maximizing uniqueness. |
| [Lemma D.2](../monograph/registered-information-appendix-D.md#d2-saturation-algebra-and-its-support-boundary) | Blockwise saturation identities and nested-partition composition. |
| [Proposition D.2a](../monograph/registered-information-appendix-D.md#d2-saturation-algebra-and-its-support-boundary) | Meet-generated equivalence paths preserve membership in a supported piece; four points refute join-only least support. |
| [Theorem D.3](../monograph/registered-information-appendix-D.md#d3-exactly-when-independent-replication-is-idempotent) | Equality in conditional mutual information forces overlapping rows to coincide; class-label simulation proves the converses. |
| [Theorem D.4](../monograph/registered-information-appendix-D.md#d4-quotient-averaging-enlarges-the-feasible-coupling-choices) | Averaging maps the fine fiber into the coarse fiber and preserves the objective; compactness supplies minima and the lifting equality criterion. |
| [Lemma D.4a](../monograph/registered-information-appendix-D.md#d4-quotient-averaging-enlarges-the-feasible-coupling-choices) | The same simulator and convexity of total variation give deficiency contraction. |
| [Theorem D.5](../monograph/registered-information-appendix-D.md#d5-least-coupling-and-the-blackwell-join) | Conditional simulation of marginals from any upper bound proves both universal-property implications. |
| [Proposition D.6](../monograph/registered-information-appendix-D.md#d6-a-sufficient-transfer-rule-for-graded-budgets) | Mix the branch simulators using candidate-independent weights; branchwise admissibility is essential. |
| [Theorem D.7](../monograph/registered-information-appendix-D.md#d7-sharp-committed-bit-detection-including-adaptive-forgers) | Iterated conditional matching gives the adaptive upper risk; an independent fair forger attains the minimax lower bound. |
| [Theorem D.8](../monograph/registered-information-appendix-D.md#d8-exactly-when-join-covers-form-a-site) | Pull back the binary join cover to obtain distributivity; distributivity, join associativity, and the representable criterion prove the converse and subcanonicity. |
| [Theorem D.9](../monograph/registered-information-appendix-D.md#d9-when-a-witness-defect-changes-the-information-partition) | A split component supplies a deleted cut; such a cut forbids a retained path. A single deletion reduces to the bridge criterion. |
| [Theorem D.10](../monograph/registered-information-appendix-D.md#d10-exact-propagation-on-coordinate-join-trees) | The message induction invariant is extendability of separator assignments; running intersection makes the subtree extensions compatible. |
| [Proposition D.11](../monograph/registered-information-appendix-D.md#d11-finite-certificates-for-polyhedral-transfer-classes) | Mixtures of vertex simulators give exact domination and the worst-deficiency equality by TV convexity. |
| [Proposition D.12](../monograph/registered-information-appendix-D.md#d12-witness-anomalies-do-not-imply-marginal-contextuality) | The coherent global row, or its prior mixture, is an amalgamation; parity gives a simultaneous nonzero witness anomaly. |
| [Theorem D.13](../monograph/registered-information-appendix-D.md#d13-exactly-when-partition-extractions-commute) | Commuting equivalence-relation composites equal their generated equivalence; singleton saturation then gives the rectangular block-intersection criterion in both directions. |

## Validation and limitations

The [independent check script](check_finite_claims.py) and [JSON output](finite-check-results.json) reproduce small finite examples and search-check the reported counterexamples. The run passed 57,600 saturation tests and 76 comparable-partition LP checks, plus the named corruption, coupling, BSC, AND, and policy examples. Floating-point checks use tolerances. The general statements rest on their proofs, not enumeration.

The empirical papers' original corpus/MNIST/bootstrap runs were not rerun. Their dependency warnings and the companion-paper impact section identify consequences of this review; they do not claim a full independent statistical replication. The source checks are linked in the corrections document. Remaining work is explicitly labeled as open: contextuality comparison, partition-site topology, constrained coupling minima, measurable generalization, and a full graded algebra.

The integration run additionally passed all join-cover tests on 19 sublattices of the three-point partition lattice, 729 nested graph pairs, and 4,096 three-bag binary constraint systems. It also checks an explicit globally coherent model with a witness anomaly. See [the integration checker](check_integrated_claims.py) and [its results](integrated-check-results.json). All 152 numbered statements have an inventory entry; this is not proof-assistant verification.

The extraction-commutation criterion was additionally checked on all 225 pairs of partitions of a four-point domain, over every subset.

Theorem 38.4’s empty-context correction is checked in all 60 contexts of its two- through five-view examples. Its audit status now records the integration-stage proof repair.
