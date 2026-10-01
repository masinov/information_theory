# Registered Information over Contrast Domains

## Appendix A: Measurable extensions and their limits

The monograph establishes finite-domain results unless an individual theorem states otherwise. This appendix proves one extension to standard Borel observations and identifies the hypotheses needed for broader generalizations. Appendix D supplies the supplementary finite results.

### A.1 What the categorical language supplies

Channels, deterministic maps, composition, conditional independence, and sufficiency can be expressed in the category of standard Borel spaces and Markov kernels. This is a useful language for extending individual results; it is not a proof that finite partition lattices, optimization problems, or uniform reconstruction theorems extend unchanged. [Fritz's treatment of sufficient statistics](https://arxiv.org/abs/1908.07021) states hypotheses that must be checked for the chosen category and theorem.

### A.2 A finite-state extension that does hold

> **Proposition A.1 (a sufficient likelihood statistic for Borel observations).** Let the state set be finite, `D={1,…,m}`, and let each observation law `P_z` be a probability measure on a standard Borel space `Y`. Put `ν=(1/m)Σ_z P_z`, choose measurable Radon–Nikodym densities `f_z=dP_z/dν`, and define `T(y)=(f_1(y),…,f_m(y))`. Modify the vector on a ν-null set to take values in the compact simplex `{u≥0:Σu_z=m}`. Then the experiment reporting `T(Y)` is Blackwell equivalent to the original experiment.
>
> *Proof.* Reporting `T` is deterministic processing. Since `Y` and the target simplex are standard Borel, take a regular conditional distribution `K(dy|t)` of `ν` given `T`. For a measurable set `B`, disintegration gives
>
> `P_z(B)=∫_B f_z(y)ν(dy)=∫ t_z K(B|t)ν_T(dt)`.
>
> The distribution of `T` under `P_z` has density `t_z` with respect to `ν_T`. Thus the same kernel `K`, independent of `z`, reconstructs every `P_z` from that distribution. Null-set choices are harmless because all `P_z` are absolutely continuous with respect to `ν`. ∎

This proposition extends existence of a lossless likelihood statistic for finite states. It does not assert a standard Borel quotient for an arbitrary equivalence relation on an infinite state space, nor an everywhere-canonical statistic independent of null-set choices.

### A.3 Where the finite proofs require new work

1. **Quotients and lattice operations.** A measurable equivalence relation on a standard Borel space need not have a standard Borel quotient. A measurable quotient and a measurable transitive closure cannot simply be assumed. The finite partition lattice is therefore not automatically an internal lattice of standard Borel quotient objects. One must restrict to suitable smooth quotients or work with a different object and prove the required operations exist.
2. **Zero-error information.** Finite support overlap uses positive atom probabilities. In nonatomic models, topological support, measure-theoretic singularity, and existence of an almost-sure decoder are different notions. An almost-sure criterion must specify which null sets are allowed and whether one decoder works for every state. The finite confusability graph is not extended merely by replacing finite supports with topological supports.
3. **Asymptotic identification.** The finite proof takes a positive minimum separation over finitely many distinct laws. That argument does not give uniform consistency over an arbitrary infinite state family. Pointwise and uniform answerability must be separated, with measurable estimators and identifiability/regularity hypotheses supplied.
4. **Coupling minima.** Fixed marginals give compact coupling sets under suitable Polish weak-topology formulations, but this does not automatically yield compactness of an arbitrary state-indexed kernel family with additional constraints. Continuity or lower semicontinuity of the chosen objective must be established in the chosen topology. Write an infimum unless attainment has been proved. Avoid undefined differences of infinite mutual informations.
5. **Measurable choices.** An argmin description alone does not produce a measurable selector. Nonempty closed-valued measurable correspondences in appropriate Polish spaces are one setting for selection theorems; arbitrary policy classes do not satisfy those hypotheses automatically. Near-optimal measurable selection may require a different theorem and a different conclusion.
6. **Deficiency duality and attainment.** General randomization theorems have specified classes of experiments, losses, and kernels. Finite LP attainment and a finite attaining decision problem cannot be transported verbatim to arbitrary spaces. A supremum of risks or an approximate simulator is not automatically an attained certificate pair.
7. **Infinite horizons.** Finite-prefix laws require a compatible extension and causal consistency. Detection exponents need assumptions on dependence and distinguishability. Neither follows from finite-horizon notation alone.

### A.4 Safe use of the finite results

Every finite counterexample remains a counterexample to an unrestricted universal claim. Deterministic factorization and explicit channel simulations can often be extended when their maps are measurable. Proposition A.1 is one completed extension. The other items above are a research program, not completed consequences of a change in vocabulary.
