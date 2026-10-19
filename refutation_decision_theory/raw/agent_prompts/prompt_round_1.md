PROBLEM: Impossibility of an optimal decision theory from conflicting optimality criteria

0. THESIS
No decision theory is optimal on all fair decision problems. The obstruction comes
from mutually incompatible optimality criteria for a single choice, not from
demanding a general rule: any assignment of actions to problems, including an ad hoc
case-by-case one, counts as a decision theory, so the impossibility must hold for
every such assignment.

1. DECISION PROBLEMS
A decision problem D is a finite extensive-form tree with:
 - nature nodes with fixed probability distributions;
 - prediction nodes: nature nodes whose distribution may depend on the agent's
   policy, but only through the actions that policy prescribes at specified
   information sets (with predictor error eps >= 0);
 - agent information sets H_D, each h with a finite action set A_h;
 - real-valued payoffs at the leaves.

2. DECISION THEORIES
A policy for D is a map pi: H_D -> A_h (deterministic).
 Variant M: pi(h) in Delta(A_h); state whether predictors observe the distribution
 or a sampled action.
A decision theory T assigns to every D in the class a policy T_D. No uniformity,
computability or generality is required; every lookup table is a decision theory.
Ex-ante value: V_D(pi) = expected payoff of pi in D, with predictions computed
from pi.

3. FAIRNESS
D is fair if the agent's payoff distribution depends on the agent only through the
actions its policy prescribes, never through the identity, name or source code of
the theory being evaluated. Fixed algorithms may appear as constants of the
environment (e.g. "Omega predicts what algorithm g0 does") as long as g0 does not
vary with the agent being evaluated.
Reason: without fairness, the diagonal problem D_T ("pay 1 to agents whose action
differs from T's") defeats every T trivially. Results must hold on the class F of
fair problems, or on a natural subclass that still contains the witnesses in §5.

4. CANDIDATE CRITERIA (to be made precise; refine as needed)
For a theory T and a fair D:
C1 Ex-ante optimality: V_D(T_D) = max over pi of V_D(pi).
C2 Causal dominance: at any information set h reached with positive probability,
   holding fixed the outcomes of all nature and prediction nodes preceding h (the
   "state"), if action a yields strictly more than b in every state compatible
   with h, then T_D(h) != b.
C3 Causal ex-post optimality (ratifiability): at every positively-reached h, T_D(h)
   maximizes expected payoff given h, with predictions held fixed at the values
   T_D itself induces.
C4 Reflective stability: if, before any prediction node, the agent may choose which
   policy it will run in D (and predictors observe that choice), T chooses a policy
   agreeing with T_D on all positively-reached information sets.
C5 Existence: T's own criterion is satisfiable, i.e. T_D is defined, for every
   fair D.
C6 (optional) Evidential optimality: T_D(h) maximizes E[payoff | h, agent takes a].
   Requires a joint distribution, e.g. via common-cause nodes; formalize if used.

5. WITNESS PROBLEMS (scaled payoffs)
W1 Newcomb: a predictor (error eps) predicts pi(h); box B holds 2 iff it predicts
   one-box; two-boxing adds 1. C1 -> one-box. C2, C3 -> two-box.
W2 Twin prisoner's dilemma: two copies of the same policy play a PD with payoffs
   T=3, R=2, P=1, S=0. C1 -> cooperate. C2 -> defect.
W3 Bomb (MacAskill): a predictor with error eps = 1e-24 puts a bomb in Left iff it
   predicts Right, and leaves a note saying so. The agent observes the note and the
   bomb. Left is free, death = -1e9; Right costs 1.
   Ex ante: V(Left) = -eps*1e9 ~ -1e-15 > V(Right) ~ -1, so C1 -> Left.
   At the reached information set (bomb visible): C2, C3 -> Right.
W4 Death in Damascus: Death predicts the agent's city exactly and waits there;
   payoff 0 if met, 1 otherwise. No deterministic policy satisfies C3.
   Variant M restores existence if Death predicts only the distribution.
W5 (optional) Counterfactual mugging: ex-ante vs ex-post conflict on paying.
W6 (optional) Smoking lesion: for C6.

6. KNOWN POSITIONS (sanity checks)
CDT ~ C2 + C3; violates C1 and C4 (W1), and C5 for deterministic policies (W4).
EDT ~ C6; violates C2 (W1); counterintuitive on lesion-type problems (W6).
FDT ~ C1 on fair problems with policy-level predictors; violates C2 and C3
     (W1, W3).

7. TASKS
T1 Make §1-4 precise. Flag every place where an informal notion (counterfactual,
   "same computation", "holding the state fixed") has to be fixed by stipulation.
T2 Prove that no theory satisfies C1 and C2 on F (expected witness: W1). State why
   this alone is close to trivial.
T3 Find the strongest non-trivial version, Arrow-style: a set of criteria, each
   satisfiable on F by some theory, every proper subset jointly satisfiable
   (demonstrate with an explicit theory for each), and the full set unsatisfiable.
T4 Characterize the maximal consistent subsets of {C1, ..., C6}.
T5 Robustness: does the impossibility survive (a) eps = 0 vs eps > 0,
   (b) mixed policies, (c) predictors that observe only actions at reached
   information sets, (d) excluding predictions about unreached information sets?
T6 Taxonomy: test the claim that "the relevant problem types are few." Either give
   a finite parameterization of F up to the criteria (finitely many types whose
   verdicts settle C1-C6 everywhere), or prove none exists (e.g. construct
   infinitely many fair problems that are pairwise non-equivalent with respect to
   the criteria).
T7 Literature check before claiming novelty: Nozick (1969); Gibbard & Harper
   (1978); Jeffrey and Skyrms on ratifiability; Lewis; Arif Ahmed; Caspar Hare &
   Brian Hedden; Caspar Oesterheld (with Conitzer); Yudkowsky & Soares (FDT,
   fairness); MacAskill (Bomb). Report any existing impossibility results of
   this form.

8. EXPECTED OUTPUT FROM EACH AGENT
The definitions used, theorem statements, complete proofs, a list of every
stipulation made, and which tasks were addressed.