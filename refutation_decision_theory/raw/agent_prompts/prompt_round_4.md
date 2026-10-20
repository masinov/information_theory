PROBLEM (ROUND 4): Optimality of a single computable decision rule that must
infer counterfactual dependence from descriptions of the world

0. BACKGROUND (summary of rounds 1-3; accept unless an error is found)
In a model where each problem SUPPLIES the counterfactual dependence (for every
policy pi, the law mu_pi of how the world responds), the picture is:
 - An everywhere ex-ante-optimal theory exists. It need not be an ad hoc lookup
   table: the uniform rule "rank policies by their own expected value" (the
   diagonal of the causal matrix M[pi,sigma] = E_{mu_pi}[U(s,sigma)])
   satisfies neutrality, affine invariance, binary independence, contraction,
   ordering and non-triviality at once.
 - Conflicts between criteria are pairwise (Nozick 1969; Briggs 2010).
   Independence + ordering force diagonal (ex-ante) ranking (Podgorski 2022,
   "Self-Esteem Theorem"). Principal contraction + neutrality + row invariance
   force choosing every option, but this disappears if shrinking a menu keeps
   the belief model fixed.
 - Lesson: every substantive result depends on how counterfactual dependence is
   STIPULATED. The model hands the rule exactly what CDT, EDT, FDT and LDT
   disagree about.
Round 4 removes that stipulation.

1. THESIS TO TEST
  "No single computable rule that receives only a description of its
   situation, and must itself infer what would happen under each of its
   possible outputs, is optimal on all fair problems."
Goal: make this precise in several natural ways; for each, prove it, refute
it, or reduce it to a known result; and state which version (if any) is true,
new and non-trivial.

2. MODEL
2.1 Agents. An agent is a total computable function T from descriptions
    (finite strings) to actions in a finite set specified by the description.
    T must halt on every description in the class considered. Variants with
    time bounds are optional (§6, task K5).
2.2 Environments. An environment E is a program that, given access to an
    agent, produces a real payoff (or a finite-support payoff distribution).
    The agent receives a description d(E), by default E's source code. Two
    access modes:
     (OR) Oracle access: E may call the agent as a black box on descriptions
          of its choosing, and the agent's actual action is the call on d(E).
     (EM) Embedded access: E is a closed program, and its source may contain
          programs (e.g. predictors or simulations) whose relation to the agent
          is not given by an oracle interface. The agent must work out from the
          source which parts of E depend on its output.
    Each environment must halt (or produce its payoff with probability 1) for
    every admissible agent; state precisely what "admissible" means in each
    model.
2.3 Self-reference. In (EM), environments may contain the agent's own code (by
    Kleene's recursion theorem such environments exist). State when
    self-referential descriptions are well-defined, contrasting this with the
    matrix model, where Skalse-type diagonal environments failed to be
    well-defined.

3. NOTIONS OF OPTIMALITY (the crux; define each precisely)
For an environment class C, T is optimal on C if, for every E in C,
U(E, T) >= U(E, A) for every admissible agent A, where "U(E, A)" must be given
a meaning for agents A other than the one E was written about:
 (O-const)  E is held fixed as a string; any code inside it is a constant.
            Replacing T by A changes only the agent's own action.
            (This is Fernando's "solve-then-apply" reading, and CDT-like.)
 (O-oracle) In (OR), replacing T by A replaces every oracle call.
 (O-syn)    In (EM), replacing T by A replaces every syntactic occurrence of
            T's code in E by A's code.
 (O-ext)    In (EM), replacing T by A also replaces every embedded program
            that is extensionally equivalent to T on the inputs it is run on.
            (This is Fernando's "identity" reading, and FDT/LDT-like.) State
            whether this is well-defined, and when.
 (O-log)    Counterfactuals given by a logical semantics: proof-based (as in
            modal UDT), or logical-uncertainty-based (as in logical induction).
            Fix one or more precise versions.
Report, for every pair of notions, which implications hold between them.

4. FAIRNESS CLASSES
 (F-self) E's payoff depends on the agent only through the agent's outputs on
          d(E) and on descriptions of E's own information sets; no queries
          about other problems.
 (F-any)  E may depend on the agent's outputs on arbitrary descriptions.
 (F-ext)  In (EM): E's payoff, under the chosen counterfactual notion, depends
          on the agent only through the function it computes, never through
          its syntax.
 (F-const) Fixed algorithms (including a copy of a particular theory) may
          appear as constants.
Lead to verify: (F-any) and (F-const) admit trivial impossibilities.
 - (F-any): E1 rewards answer a on some other description d', and E2 rewards
   answer b on d'.
 - (F-const) with (O-const): Skalse's construction. For any computable T,
   define via the recursion theorem an environment E_T with a transparent box
   (1000) and an opaque box worth 2000 iff T(d(E_T)) != opaque. Then T is
   beaten on E_T.
 Confirm or refute these; then treat them as the "trivial" baseline that any
 interesting result must avoid.

5. TASKS
K1 Oracle model with self-queries. In (OR) + (F-self) + (O-oracle), with
   environments that halt for every oracle, decide whether a computable
   optimal T exists. Lead: T can enumerate its possible policies on d(E), run
   E with the oracle fixed to each policy, and pick the best. Check whether
   this is correct, computable and optimal, and what happens when E's halting
   depends on the oracle.
K2 Embedded model, syntactic substitution. Same question in (EM) + (O-syn).
   Determine whether recognizing syntactic occurrences suffices, and construct
   environments where a functionally identical copy (different syntax) defeats
   (O-syn)-based agents.
K3 Embedded model, extensional counterfactuals. In (EM) + (O-ext) + (F-ext):
   (a) Is (O-ext) well-defined? Give conditions.
   (b) Prove or refute: no computable T is optimal on all such environments.
       Expected route: a reduction from undecidability of program equivalence
       (Rice's theorem) or from the halting problem, using predictors that are
       extensionally equal to T only if some program halts. Check that the
       environments are fair and well-defined; if they must be excluded,
       explain why.
   (c) If impossibility holds, find the largest natural subclass on which a
       computable optimal T exists (e.g. provably-extensional environments,
       where the equivalence is provable in a fixed theory).
K4 Logical counterfactuals. Under one or more precise versions of (O-log):
   (a) State the known pathologies (spurious counterfactuals; the "5-and-10"
       problem; Löbian obstacles) as theorems in this model.
   (b) Determine whether known optimality results for proof-based agents on
       "fair" or "provably extensional" problem classes hold, with exact
       hypotheses, and whether an optimality result beyond those classes is
       possible.
K5 Resource bounds (optional). With time-bounded agents and environments,
   decide whether the K1-K4 answers change (e.g. via parametric bounded Löb, or
   because exhaustive simulation becomes infeasible).
K6 Connection to Fernando's two readings. Show precisely how the "identity" and
   "solve-then-apply" readings of Anti-Newcomb correspond to (O-ext)/(O-syn)
   versus (O-const). State whether "Anti-Newcomb is isomorphic to Newcomb for
   FDT" is true, false or undefined under each notion.
K7 Verdict on the thesis. Fill in a table with a row for each combination of
   access mode, optimality notion and fairness class, and columns: does a
   computable optimal T exist? Is the answer known? Is it trivial? Then state
   the strongest true, non-trivial version of the thesis.

6. LITERATURE (verify every citation; flag any that cannot be confirmed)
 Rice (1953); Kleene's recursion theorem; Tennenholtz (2004), program
 equilibrium; Barasz, Christiano, Fallenstein, Herreshoff, LaVictoire &
 Yudkowsky (2014), robust cooperation via provability logic; Critch (2019),
 parametric bounded Löb; Soares & Fallenstein (2015), "Toward Idealized
 Decision Theory"; MIRI technical reports on modal UDT and its optimality on
 fair problems (verify authors, e.g. Benson-Tilsen); Garrabrant et al. (2016),
 "Logical Induction"; Yudkowsky & Soares (2017), "Functional Decision Theory";
 Skalse (2021), "A General Counterexample to Any Decision Theory and Some
 Responses"; Leike & Hutter (2015), "Bad Universal Priors and Notions of
 Optimality"; discussions of the "5-and-10" problem. Report the closest
 existing result to each answer in K7.

7. CLOSURE CRITERION
Round 4 is complete when it delivers: precise definitions for §2-4; the
implications between optimality notions; answers to K1-K4 and K6 with proofs
or explicit counterexamples; the K7 table; a final statement of the thesis
with its scope; and verified citations with a novelty assessment.

8. OUTPUT FROM EACH AGENT
For each task attempted: definitions, theorem statements, complete proofs or
explicit counterexamples, every stipulation made beyond this statement, any
errors found in §0, and full citations (author, title, venue, year,
section/page) for every source used.