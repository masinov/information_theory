# Registered Information over Contrast Domains

## Appendix A: The Measure-Theoretic Pass

This appendix makes honest the claim, standing since §20.5, that the finiteness assumption (A6) is an artifact of the concrete presentation. It does two things: states the reinterpretation, and inventories exactly which arguments need more than reinterpretation. It adds one reference (measurable selection); everything else is covered by sources cited in Parts I and III.

### A.1 The reinterpretation

Every definition of the manuscript is written in the vocabulary of channels, composition, determinism, marginals, couplings, conditional independence, and sufficiency — the native operations of a **Markov category** — plus the lattice of partitions of the contrast domain. Interpreting the same definitions in $\mathsf{BorelStoch}$, the Markov category of standard Borel spaces and Markov kernels [Cho & Jacobs 2019; Fritz 2020], yields the general theory with no change of statement: contrast domains become standard Borel spaces; partitions become measurable equivalence relations with their quotient $\sigma$-algebras, the lattice operations being generated $\sigma$-algebra (join) and intersection-with-completion of the induced relations (meet, via measurable transitive closure on standard Borel quotients); views, ceilings, patterns, policies, and streams are kernels with the stated measurability (causal = adapted); the Fisher–Neyman factorization and hence Theorem 22.6 hold synthetically in this setting [Fritz 2020], as §20.5 already recorded. The Shannon quantities of Part VII and the deficiencies of Part IX are classical in this generality [Cover & Thomas 2006; Le Cam 1964; Torgersen 1991].

### A.2 The inventory: what needs an argument, not a reinterpretation

Four points in the manuscript used finiteness as more than convenience; each has a standard general replacement, listed with its location.

1. **Attainment on coupling fibers** (Definition 55.1; Propositions 55.2–55.4; §39). The fiber of couplings with prescribed kernels is, in the Borel setting, a set of probability measures that is convex and compact in the weak topology (tightness is inherited from the fixed marginals), and $I_Q(q; Y_T)$ is weakly lower semicontinuous; the minimum $I^{\min}$ is therefore attained and the fiber-excess calculus of Part VII survives, with "min" never silently becoming "inf."

2. **Certificates for deficiency values** (Part IX, §68.3). The finite linear programs are the finite shadow of Le Cam's general randomization criterion: deficiency equals the supremum of Bayes-risk gaps over decision problems with bounded loss in full generality [Le Cam 1964; Torgersen 1991]. The certificate discipline — channel above, decision problem below — is exactly the general proof method; only the *computability* by LP is finite-specific, and no theorem of Part IX relied on it (the LPs were verification, as stated there).

3. **Measurable selection** (rules and policies chosen pointwise: the minimum-distance rule of Theorem 22.2, the annihilating clutters of Lemma 62.1, the policy constructions of §§63, 76). Each such choice is an argmin/argmax over a parameter measurably indexed by the data; in the Borel setting these selections exist by the Kuratowski–Ryll-Nardzewski theorem [Kuratowski & Ryll-Nardzewski 1965], the appendix's one added reference. No optimality claim changes; only the word "choose" acquires its measurable justification.

4. **Finite enumerations and exhibits.** Two distinct roles must be separated. Where finiteness powered an *enumeration in a proof of optimality over a class* (the memoryless frontier of Theorem 76.2, the four-policy table of Proposition 63.3), the general statements replace maxima by suprema over the measurable class, attained or not, with the exhibited policies still witnessing the strict dominations — the theorems' content is unchanged. Where finiteness is intrinsic to a *counterexample* (parity, Worked example E, the cyclic hierarchy, every corruption exhibit), nothing needs generalizing: a finite counterexample refutes a general law, and the exhibits' finiteness is a feature of the manuscript's method, not a limitation of its scope.

### A.3 What is not claimed

The pass extends the *static and finite-horizon* theory to standard Borel generality. It does not deliver infinite-horizon or continuous-time dynamics — problem P6 of §86, where the causal gap and the detection exponent await their stationary-process forms — and it does not revisit the finite combinatorial content of the descent theory (nerves, orbit graphs), whose objects are finite by nature at any base generality.

**Reference added in Appendix A:**

- Kuratowski, K., and Ryll-Nardzewski, C. (1965). "A General Theorem on Selectors." *Bulletin de l'Académie Polonaise des Sciences* 13, 397–403.
