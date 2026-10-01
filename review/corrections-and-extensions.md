# Registered information: corrections and extensions

> **Integration record.** The monograph now incorporates the corrected statements and proofs directly. R1–R7 below are retained as review history; their authoritative manuscript versions are [Appendix D.1–D.7](../monograph/registered-information-appendix-D.md). D.8–D.13 additionally settle finite site stability, witness cuts, coordinate propagation, polyhedral transfer certification, and the nonimplication from witness anomalies to contextuality, and the extraction-commutation criterion.


Review date: 2026-10-01. Scope: the monograph in `../monograph`, its mathematical dependencies, and consequences for the two companion papers. This is a mathematical review, not a formal proof-assistant verification. The [proof audit](proof-audit.md) records the disposition of every numbered result. [Executable checks](check_finite_claims.py) independently test finite examples; [results](finite-check-results.json) record the run. No empirical dataset experiments were rerun.

## 1. What the theory is expressing

The starting object is a contrast domain of candidate scenes, with views that identify some candidates and distinguish others. Registration associates presentations with sound constraints on candidates. A question is answerable when its partition is coarser than the distinction supplied by the registered data. The foundational adjunction relates collections of views to their joint partition. Saturated subsets then form a downstream information algebra: intersection combines constraints and saturation forgets distinctions.

The later parts deliberately separate things that coincide in the deterministic kernel: support-based certainty, equality of likelihood laws, and full statistical experiment; presentations, attribution verdicts, and context; fixed local resources and their actual joint coupling; unrestricted decoding and institutionally admissible readings. The most useful organizing principle is the failure of a proposed consolidation or local-to-global identity, together with an explicit object witnessing that failure.

The sound core survives. The original claim that all of these directions form one completed, commuting extension does not. Exact partition defects, statistical decision losses, and presheaf extension problems need distinct hypotheses and distinct certificates.

## 2. Editorial and mathematical priorities

Read Parts I–III first for the partition and experiment orders. Parts IV–VI introduce records, coupling, and admissibility. Part V's witness constructions should be read as a separate local-to-global analysis, with the sheaf caveats below. Parts VII and IX give two different quantitative instruments. Parts VIII and X apply them to corruption and interaction. Part XI is a synthesis subject to the qualifications in this review. Appendix A now states the actual measurable-space boundary; Appendix B identifies reproducible finite checks.

Corrections have been placed beside the affected claims, including replacement statements where necessary. Older introductions, conclusions, and completion narratives are historical and have no independent theorem status. The project continuation scaffold is not a proof source. A publication rewrite should consolidate repeated recovery discussions into a table of hypotheses and conclusions and place the graph/partition distinction before any contextuality language.

### Major corrections

| Issue | Correct conclusion | Locations |
|---|---|---|
| Binary-state Blackwell antichain used to deny a join | Binary finite experiments form a lattice. Incomparability is insufficient. General nonlattice behavior begins with larger state spaces. | III §22.5; VIII §61.2; R5 below |
| Generalized information algebra conflated with commuting variable-domain algebras | Saturation supplies the generalized set algebra. Arbitrary partition extractions do not commute; join closure does not imply ambient meet closure or least supports. | I §6.11; XI §§83–84; R2 |
| Witness-edge defect treated as a partition defect | A missing edge can be redundant for connectivity. Nerve homology addresses an edge-level question before component formation. | V §38.5; §3 below |
| Witness presheaf identified with contextuality | The candidate-pair presheaf has inclusion restrictions and is a sheaf for positive union covers. It is not automatically the event/support presheaf. | V §§35–39 |
| All record layers collapse under unique correct attribution | Context may still contain information. Presentation/full-record equivalence requires sterility or another explicit sufficiency hypothesis. | IV §32; VI §50 |
| Blind partial replacement always kills zero-error information | An unreplaced coordinate can retain the state. Whole-record common full-support clutter is a sufficient condition. | IV §29.8; VIII §62 |
| Monotone forgetful ceiling fails nested record closure | Monotonicity already gives closure on a nested ladder. Failure concerns all determination maps or repackaging. | VI §45.5 |
| Fixed-decoder equality implies invariance of admissible decoders | The admissible class can change when it is defined by the corrupted output experiment. | VI §47.1 |
| A single ledger or deterministic fiber controls all extensions | Exact intervals and graded deficiencies answer different questions; quotient averaging changes coupling fibers. | VII §57; XI §85; R4 |
| Pointwise Borel reinterpretation completes the theory | Quotients, selections, uniform limits, and optimization need additional hypotheses. | Appendix A |
| Commitment alone implies a positive detection exponent | A positive gap between honest coupling and the allowed forgeries is needed. The bit example admits a sharper exact test. | X §78; R7 |

### Source checks and their proper roles

[Kohlas, *Algebras of Information* (2017), §§2.5–3.1](https://arxiv.org/abs/1701.02658) supplies generalized set algebras and partition-based conditional independence. It supports the saturation construction, without making arbitrary extractions commute. The older valuation-algebra terminology should not conceal that distinction.

[Bertschinger and Rauh, *The Blackwell relation defines no lattice* (2014), Proposition 16](https://arxiv.org/abs/1401.3146) explicitly establishes the binary-input lattice exception. The monograph's cited reference therefore contradicts its former binary no-join argument.

[Abramsky and Brandenburger (2011)](https://arxiv.org/abs/1102.0264) use coordinate restrictions of assignments on measurement contexts. [Abramsky, Mansfield and Barbosa (2011)](https://arxiv.org/abs/1111.3620) give cohomological obstructions with a one-way sufficiency limitation. Neither reference identifies the present candidate-pair nerve with that obstruction. A comparison map is a research problem.

[Vorob'ev (1962)](https://epubs.siam.org/doi/abs/10.1137/1107014) underlies the universal marginal-extension/acyclicity assertion. The manuscript proves running-intersection sufficiency; the converse is imported, with quantification over sufficiently rich alphabets. Singleton alphabets cannot witness necessity.

[Fritz, *A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics*](https://arxiv.org/abs/1908.07021) provides an appropriate categorical language. It does not make every quotient standard Borel or every measurable optimization problem attain its optimum. Appendix A distinguishes a proved finite-state extension from the unproved global pass.

## 3. Counterexamples that should remain visible

**Noncommuting extraction.** On `D={1,2,3}`, let `a=12|3`, `b=1|23`, and `E={1}`. Then `s_a(s_b(E))={1,2}` whereas `s_b(s_a(E))=D`. This does not invalidate generalized set information algebras. It invalidates an unqualified commutativity axiom.

**No least achievable support.** On `D={1,2,3,4}`, take `a=12|3|4`, `b=1|23|4`, with achievable domains `{bottom,a,b,top}`. This family is join closed. The piece `{4}` is saturated for `a`, `b`, and `top`, but not for `bottom`. Since `a` and `b` are incomparable, it has no least achievable support. Their ambient meet `123|4` is missing.

**Absorbed witness edge.** Use orbit classes `A={1,2}`, `B={3,4}`, `C={5,6}` and deterministic views

```
v = (0,0,0,0,0,1)
w = (0,0,0,1,1,0).
```

The intersection of the singleton orbit graphs is the triangle `AB,AC,BC`. The joint-view graph is the path `AB,BC`. For `AC`, both singleton witnesses exist but no joint witness does: the two-vertex nerve has two isolated points, hence nonzero reduced H0. Both graphs nevertheless have one connected component. Thus this homological edge certificate does not imply a nonzero component-partition witness interval. The executable checks reconstruct all these graphs.

**Blind partial replacement preserves certainty.** Let two clean views both reveal a fair binary state. Erase the first alone with probability `r`, the second alone with probability `r`, and neither with probability `1-2r`, for `0<r≤1/2`, independently of the state. The joint always reveals the state. Independently scheduling those same marginal erasures would instead erase both with probability `r²`. The deficiency from the independent schedule to the anti-correlated one is `r²/2`; this is coupling information invisible in marginal corruption rates.

**Correct attribution does not remove context.** A constant presentation, a context equal to the state, and a forced constant tracked-target verdict satisfy unique correct anchoring. The presentation record is null while the full record reveals the state. Context sterility is not optional in the former recovery assertion.

## 4. New finite results

These are additions to this manuscript, without a claim of priority over the literature. All domains and output alphabets in R1–R7 are finite and nonempty. Write `π≤ρ` for “ρ is more informative,” and `E≼B F` when `E` is a garbling of `F`. Deficiency `δ(E,F)` measures simulation of `F` from `E`. Mutual information uses a specified prior; full support is stated where needed.

### R1. Maximal certified partial answer

**Theorem.** Let a deterministic registered representation be `r:D→X` and a question be `q:D→A`. A sound partial decoder `d:X→A∪{abstain}` may answer `a` only when every candidate in the realized fiber `r⁻¹(x)` has question value `a`. The maximal answerable domain is exactly the union of the fibers on which `q` is constant. On that domain the answer is unique. Under a full-support prior this decoder uniquely maximizes the probability of answering, up to unrealized outputs.

**Proof.** If a fiber contains two question values, any non-abstaining answer is wrong for at least one candidate. If the fiber is constant, its common value is safe. Thus decisions can be made independently on each realized fiber, and including every constant fiber gives the maximal domain. Full support makes omission of any such fiber strictly reduce retained probability. ∎

This adds a useful intermediate notion between total zero-error answerability and probabilistic loss: how much of the domain permits a certified answer. With non-full-support priors the maximal domain is unchanged, but probability-maximizing decoders need not be unique on zero-mass fibers.

**Semantic caution.** Equality of registered pieces can encode distinctions beyond what an individual piece entails. For `D={0,1}`, registrations `κ(0)={0}`, `κ(1)=D` are sound and distinct. Observing which piece was emitted identifies the candidate, although the constraint `D` alone entails no answer. The manuscript's equality-kernel answerability concerns observation of the registered representation. Constraint entailment is a different semantics and should be named when intended.

### R2. Saturation algebra and its support boundary

**Lemma.** For a partition `π`, saturation satisfies

```
sπ(∅)=∅,   E⊆sπ(E),   sπ(sπ(E)∩F)=sπ(E)∩sπ(F).
```

If `ρ≤π`, then `sρ sπ=sρ=sπ sρ`. If `E` is `π`-saturated and `F` is `ρ`-saturated, then `E∩F` is `(π∨ρ)`-saturated.

**Proof.** A π-block meets `sπ(E)∩F` exactly when it meets both `E` and `F`: once it meets `E`, the whole block lies in `sπ(E)`. This proves the displayed identity block by block. Nested partitions give nested block unions, proving both compositions. A `(π∨ρ)`-block lies within one block of each partition, so membership in `E∩F` is constant on it. ∎

These identities support combination by intersection, units `D`, nulls `∅`, and downward focusing by saturation on any join-closed domain family, in the generalized set-algebra sense. They do not require commuting extraction for incomparable domains.

**Proposition.** If the domain family is finite, contains a support of `E`, and is closed under ambient nonempty meets, then `E` has a least support in that family. Join closure alone does not suffice.

**Proof.** Saturation of `E` under a partition says its equivalence relation never crosses from `E` to its complement. The relation of the ambient meet is generated by unions of the supporting equivalence relations; every path still stays on one side. Thus `E` is saturated for the meet of all its supports. Meet closure places that least support in the family. The four-point example in §3 refutes the join-only claim. ∎

### R3. Exactly when independent replication is idempotent

**Theorem.** For a finite experiment `P`, the following are equivalent:

1. `P⊗P` is Blackwell equivalent to `P`, where the two outputs are independent given the state.
2. Every pair of rows of `P` is either identical or has disjoint support.
3. The zero-error partition `σ⁰(P)` equals the equal-law partition `σ⁼(P)`.
4. `P` is Blackwell equivalent to the deterministic experiment reporting its row-equivalence class.

**Proof.** Give the state a full-support prior, and let `Y,Y′` be the independent replicates. Under (1), data processing in both directions gives `I(Z;Y,Y′)=I(Z;Y)`, so `I(Z;Y′|Y)=0`. For any realized `y` and any state `z` with `P(y|z)>0`, conditional independence of replicates gives `Law(Y′|Z=z,Y=y)=P(·|z)`. Vanishing conditional mutual information forces this law to depend only on `y`. Therefore states sharing any positive-probability output have identical rows, proving (2).

Under (2), each realized output identifies the row class, and sampling the common row from that class simulates `P`. This proves (4). The support-overlap graph then has exactly the row classes as components, giving (3). Conversely (3) forbids an overlap edge between unequal rows, proving (2). Finally (4) makes replication equivalent to repetition of a deterministic class label, proving (1). ∎

Thus strict accumulation under independent replication is exactly the failure of the experiment to be equivalent to deterministic information. This supplies a structural replacement for the erroneous “posterior 1/2 is impossible” argument: a BSC can always be garbled to posterior 1/2 by discarding its output. For crossover `c∈(0,1/2)`, two concordant outputs instead yield a posterior outside `[c,1-c]`, which one BSC cannot produce. At `c=.3`, the independently checked deficiency is `.084`.

### R4. Quotient averaging enlarges the feasible coupling choices

Let `μ` have full support on `D`, and let `q:D→A` be surjective. For a fine-state channel `P`, define `(M_qP)(·|a)=Σ_{z:q(z)=a} μ(z|a)P(·|z)`. Let `F_D` be the fiber of joint channels with specified fine-state marginals, and `F_A` the fiber with their averaged marginals. Write

```
m_D = min_{Q∈F_D} Iμ(q(Z);Y),
m_A = min_{R∈F_A} Iμq(A;Y).
```

**Theorem.** `m_A≤m_D`. For an actual fine coupling `P`, its coarse fiber excess is at least its fine fiber excess, and their difference is exactly `m_D−m_A`. Equality holds precisely when some coarse minimizer has a lift in `F_D`.

**Proof.** Averaging maps `F_D` into `F_A` and leaves the joint law of `(q(Z),Y)` unchanged. Hence minimizing on its image cannot improve on minimizing over all `F_A`. Both fibers are compact finite-dimensional polytopes, and mutual information is continuous, so minima exist. Equality holds exactly when a fine minimizer maps to a coarse minimizer, equivalently when some coarse minimizer has a feasible lift. Subtract the two minima from the same actual mutual information to obtain the excess formula. ∎

**Lemma.** `δ(M_qE,M_qF)≤δ(E,F)`.

**Proof.** Any fixed output simulator for the fine experiments also simulates their averages. Convexity of total variation bounds each averaged error by the maximum fine-state error. Infimize over simulators. ∎

Averaging therefore contracts simulation error, but need not preserve determinism or conditional independence. In the XOR example deterministic fine-state marginals force a unique fine coupling, while their question-averages admit different couplings. The excess difference is a concrete measure of a lost lifting constraint, not evidence that ordinary question-level information decompositions are undefined.

### R5. Least coupling and the Blackwell join

**Theorem.** Fix finitely many finite marginal experiments `P_i` on the same state space. Their full, unconstrained coupling fiber has a Blackwell-least member if and only if the `P_i` have a least upper bound in the finite-experiment Blackwell order. When they exist, these two experiments are equivalent.

**Proof.** Suppose a join `H` exists. Choose simulators `G_i` with `P_i=G_i H`, and, conditional on an output of `H`, sample the outputs of the `G_i` independently. The resulting joint `Q` lies in the coupling fiber and is a garbling of `H`. Its marginals show that it is an upper bound of all `P_i`, so `H≼B Q` as well. Every fiber member is an upper bound, hence dominates `H` and therefore `Q`.

Conversely, suppose the fiber has a least member `L`. Any upper bound `H` of the marginals yields a joint `Q` by the same conditional simulation construction, with `Q≼B H`. Since `L≼B Q`, we have `L≼B H`. As `L` itself has the required marginals, it is their least upper bound. ∎

Consequently binary-state finite coupling fibers always have a least Blackwell class, by the binary lattice theorem cited above. The state-conditionally-independent coupling need not represent it. For two equal noisy marginals, the diagonal coupling is equivalent to one copy, whereas independent replication can be strictly stronger by R3. Two incomparable fiber points do not exclude a least point elsewhere in the fiber. This theorem concerns the entire unconstrained fiber; budget, causal, or restricted-corruption subsets need a separate existence argument.

### R6. A sufficient transfer rule for graded budgets

**Proposition.** Let the honest family satisfy graded separable bracketing under a joint ceiling `Γ_S`. Suppose a perceived family is obtained by a candidate-independent random choice `r` followed by a product of local output channels `M_i^r`. Fix perceived local decoders `G_i`. If, for every branch of positive probability, each composite `G_i M_i^r` is admissible under its honest singleton ceiling, then the joint perceived reading is a garbling of `Γ_S`.

**Proof.** In each branch, honest separable bracketing supplies a simulator `L_r` from `Γ_S` to the joint decoded experiment. Mixing these simulators with the candidate-independent branch probabilities gives a simulator for the perceived joint reading. ∎

For a single product branch, admissibility of the perceived readings is exactly the needed composite admissibility. For a mixture, admissibility after averaging branches does not imply branchwise admissibility; it cannot be silently substituted. This is a useful sufficient criterion, not a characterization of all robust corruptions.

**Order caution.** The down-set completion embeds any poset by `x↦↓x` and supplies unions as joins. It does not generally preserve joins already present: for incomparable `a,b` with a join, `↓a∪↓b` omits `a∨b`. In particular it encodes available alternatives, not an assembled joint experiment. The manuscript's `min_i δ(E_i,F)` similarly chooses one local resource; it is not deficiency from a bundle of all resources.

### R7. Sharp committed-bit detection, including adaptive forgers

**Theorem.** In each of `n` rounds the honest audit reveals a fresh independent fair bit `Y_i` and an honest verdict `A_i=Y_i`. Under forgery, `A_i` must be chosen before `Y_i` is revealed and may depend on the entire past and private randomness, but that information is independent of the fresh bit. For equal prior odds between honesty and forgery, the minimax error probability over all such adaptive forgers is exactly `2^(−n−1)`.

**Proof.** Accept honesty if and only if every verdict matches. Honesty is never rejected. Conditional on any past and precommitted verdict, the fresh bit matches with probability `1/2`; iterated conditioning gives probability `2^(−n)` of all matches under every allowed forgery. The equal-prior risk is therefore `2^(−n−1)`.

For a lower bound, allow the forger to choose independent fair verdict bits. Its joint law is uniform on all `4^n` bit/verdict sequences. The honest law is uniform on the `2^n` matching sequences and zero elsewhere. The optimal simple-hypothesis equal-prior Bayes error is one half the sum of the smaller probability at each outcome, namely `(1/2)2^n 4^(−n)=2^(−n−1)`. No test can beat that against this allowed forger. ∎

At `n=20`, the exact risk is `2^(−21)≈4.77×10^(−7)`, sharper than the original Bhattacharyya bound. This does not cover partial-round attacks, leaked fresh bits, biased/dependent future bits, or noisy honest verdicts. Those are separate models with potentially different rates.

## 5. Consequences for the companion papers

The empirical paper's choice to implement finite channels is consistent with the reviewed scope. The present review does not certify corpus alignment, sample-size claims, or the reported MNIST/SemCor runs. Its results files remain records of the original runs. Point estimates of exact support or equality partitions are particularly fragile under sampling; the distinction between model-level certainty and finite-sample evidence should remain explicit.

The Le Cam synergy paper's central finite quantity—deficiency from a specified independent-marginal baseline to the observed joint experiment—remains meaningful. The independent implementation reproduces the AND value `.1`, and `Sδ=ε/4` in its ε-family. The binary-antichain baseline argument has been replaced directly by R5; its independent-marginal baseline is a modeling choice, not a uniquely forced minimum. The information-theoretic quadratic coefficient is asymptotic, not an exact finite-ε constant. An information-preserving deterministic relabeling gives zero deficiency, so a strict upper bound such as `<1/2` alone does not establish a positive graded loss. The empirical paper’s half-gap corollary now requires its entire confidence interval to lie strictly inside `(0,1/2)`; an upper bound alone cannot exclude zero. Existing empirical “graded” labels based only on the upper test remain qualified, not recertified. A claim of strict replication gain needs an actual failure of Blackwell sufficiency, as characterized in R3. The Le Cam paper’s universal smoothing-bias claim is also withdrawn: its Lipschitz bound controls error on a TV-radius event, not the sign of estimator bias.

Neither the fine/coarse coupling-fiber difference nor a witness/partition distinction by itself proves an impossibility theorem for standard PID axioms. It proves that a question-level functional cannot recover additional fine-state or admissibility data that were discarded. A stronger incompatibility claim must specify the desired axioms and provide two models with the same input to the proposed functional but different required outputs.

## 6. Proposed lines of work

These are open directions, not completed theorems.

1. **Graph-sensitive descent before reflection.** Develop edge-level witness obstruction and component-level information loss as separate invariants. Seek necessary and sufficient conditions for a missing witness edge to change connectivity, using bridges/cuts. The absorbed-edge example must be a regression case for any proposed cohomological invariant.
2. **A genuine comparison with contextuality.** Specify a measurement scenario, an event presheaf with coordinate restrictions, and a map from registered candidate data. Prove which global-section obstructions are preserved or reflected. Do not identify an arbitrary nerve's homology with the contextuality obstruction by analogy.
3. **Sites for achievable partitions.** Join-cover equations on a nondistributive lattice do not automatically define a pullback-stable topology. Investigate distributive subfamilies, the original finite-view subset site, or a completion with an explicit universal property. Track what the completion changes about achievable domains and supports.
4. **Quantitative stability of R3.** If `δ(P,P⊗P)` is small, under what lower bounds on positive row masses is `P` close to a deterministic-equivalent experiment? Compactness may give nonconstructive finite-alphabet moduli; dimension-free bounds are a separate question. Discontinuity of support partitions rules out naive unconditional bounds on exact zero-error content.
5. **Constrained coupling minima.** R5 solves the unconstrained existence question. Characterize least elements under causal, local-budget, or corruption constraints, and construct a realizable three-state restricted class lacking a least transfer. The rejected binary antichain is not such a construction.
6. **Lifting obstruction under quotient averaging.** Study the nonnegative gap `m_D−m_A` from R4. Characterize when coarse minimizers lift, formulate finite feasibility certificates for a fixed coarse minimizer, and compare its value with witness/coupling defects under stated admissibility assumptions.
7. **Sequential audit with imperfect commitment.** Extend R7 to predictable biased bits, a bounded number of corrupted rounds, and side information about fresh randomness. Specify both hypotheses and error criterion before claiming an exponent. Conditional match-probability bounds offer a direct martingale route.
8. **A statistical version of certified partial answerability.** Replace R1's exact fibers by confidence sets with coverage guarantees, then optimize retained mass under a declared error budget. Separate estimation uncertainty from the structural content of the underlying experiment.
9. **Measured extensions one theorem at a time.** Begin with finite states and standard Borel observations as in Appendix A. Add regularity for one desired optimization or quotient construction at a time; record whether the conclusion is exact, almost sure, pointwise, or uniform.

A fruitful next paper would isolate one of these mechanisms with its counterexample, theorem, and experiment. The full theory should remain a framework connecting several mechanisms rather than claiming they are already equivalent manifestations of one invariant.
