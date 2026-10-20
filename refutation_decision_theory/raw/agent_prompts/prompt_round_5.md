PROBLEM (ROUND 5): Is there a coherent semantics for logical counterfactuals?
An impossibility programme

0. BACKGROUND (summary of rounds 1-4; accept unless an error is found)
 - When a problem SUPPLIES the counterfactual dependence (for every policy pi,
   the law mu_pi of how the world responds), ex-ante optimal choice is
   unproblematic: the uniform rule "rank policies by their own expected
   value" is coherent across problems, and conflicts between criteria are
   pairwise (Nozick 1969; Briggs 2010; Podgorski 2022).
 - When the agent must infer dependence from source code (round 4):
   * Oracle or designated-slot substitution on terminating finite-policy
     problems admits a computable optimizer (promise-total).
   * Fixed copies of the agent as environmental constants defeat every
     globally total rule (Skalse 2021; Fallenstein's modal version).
   * Exact argmax over computable expected values is uncomputable (recursive
     inseparability), independently of any decision theory.
   * Extensional matching fails: matching on actually-run inputs can leave no
     optimal agent; matching on all inputs misses dependent programs such as
     1 - T; rematching does not compose.
   * Material implication yields spurious counterfactuals (a computable
     5-and-10 agent exists); Fallenstein's modal "third-person counterfactual"
     semantics is partial.
 - Conclusion so far: once a rule for propagating the dependence of the world
   on the agent's output is FIXED, optimal choice is a finite computation. The
   open question is whether such a rule can be defined coherently. This is the
   problem of LOGICAL COUNTERFACTUALS.

1. THESIS TO TEST
  "No operator assigning outcomes to the non-actual outputs of a computation
   satisfies all of: baseline correctness, totality, calibration on
   independent problems, transport through dependent computations,
   extensionality, conservativity, compositionality, realizability and
   computability."
Goal: make the desiderata precise; determine their minimal inconsistent and
maximal consistent subsets; and decide whether there is a non-trivial
impossibility theorem (three or more natural desiderata, each satisfiable,
every proper subset satisfiable, the whole set inconsistent).

2. FRAMEWORK
2.1 Agents: total computable functions T from descriptions to actions (state
    results for globally total agents and, separately, for agents total only
    on the class considered). A fixed binary action set {0,1} suffices for
    negative results.
2.2 Environments: programs E built from typed atomic components g_1..g_k
    (programs) plus an actual-action port receiving T(d), where d = d(E) is
    E's source. Payoffs are exact rationals. E is admissible if it terminates
    with a rational payoff for every assignment of table functions to the
    action port and to every component (the "promise class" of round 4).
    Variant: allow fixed algorithms as constants (class F_const) or exclude
    them (state how exclusion is defined without presupposing the answer).
2.3 A counterfactual operator K maps (E, T, a), for a legal action a at d, to
    a value K(E,T,a) in Q or to "undefined". A transformation version is also
    allowed: K produces a counterfactual environment E[T(d) := a] whose
    execution gives the value; state which version each result uses.
2.4 The agent induced by K: T is K-ratifiable on E if T(d(E)) maximizes
    K(E,T,.).

3. DESIDERATA (candidates; give precise versions, possibly several each)
D1 Baseline: K(E,T,T(d)) = U(E,T).
D2 Totality: K(E,T,a) is defined for every legal a.
D3 Calibration on independence: if E depends on the agent only through the
   action port (no component computes, simulates or is equal to anything
   derived from T), then K(E,T,a) = the payoff of E with action a.
D4 Transport: if a component is a designated copy of T (same oracle or slot),
   its value at d becomes a. Strong version: if a component is C[T] for a
   computable context C (e.g. 1 - T, or T composed with h), its value at d
   becomes C applied to a.
D5 Extensionality:
   (agent) T and T' that compute the same function give the same K;
   (environment) replacing a component by an extensionally equal program
   leaves K unchanged.
D6 Conservativity: components that do not depend on T are unchanged.
   "Depend" is the notion under definition; give non-circular versions
   (syntactic independence; independence in a supplied dependency graph;
   invariance under all agent substitutions) and say which version each
   result uses.
D7 Compositionality: the transformation version satisfies
   (E[T(d):=a])[a := b] = E[T(d):=b], for an explicitly defined way of
   iterating.
D8 Computability: K is computable on the admissible class (or on a stated
   promise class).
D9 Realizability (non-spuriousness): for each a, there is an admissible agent
   A with A(d) = a such that K(E,T,a) equals A's payoff in E under a fixed,
   stated substitution rule. Counterfactual values must be values some actual
   alternative agent could obtain.
D10 Optimizability: on the class, some computable agent is K-ratifiable on
   every environment.

4. LEADS TO VERIFY
L1 Ambiguity under extensionality plus strong transport. If T is not
   injective (e.g. the constant-0 agent), a component g with g(d) = c can be
   written as h o T for many h that disagree at a != T(d). Strong D4 then
   gives conflicting values, and D5 forbids using syntax to choose. Determine
   whether D4(strong) + D5 + D2 is inconsistent outright, or only for
   non-injective agents; if the latter, whether any natural agent class
   avoids it.
L2 Round-4 Theorem 5 (matching on actually-run inputs): check which subset of
   D1-D10 it violates, and whether it yields a minimal inconsistent set with
   D10.
L3 Round-4 Theorem 6 (matching on all inputs misses 1 - T): check that it
   separates D5-based matching from D4(strong).
L4 Rematching non-composition (round 4, §6.4): formalize it as a D7 failure
   and identify which other desiderata force rematching.
L5 Material implication: show that the vacuous reading violates D9, and that
   the 5-and-10 construction violates D3 or D10.
L6 Fixed constants: decide whether, in F_const, D5(environment) + D4 force a
   fixed copy of T to be transported. That would conflict with treating it as
   a constant, and links to Skalse's diagonal.

5. TASKS
P1 Formalize D1-D10 in the framework of §2, giving several versions where the
   informal statement is ambiguous. Flag every circularity (especially D6).
P2 Settle L1-L6 with proofs or counterexamples.
P3 Consistency map: determine all inclusion-minimal inconsistent subsets and
   all maximal consistent subsets of the precise desiderata, giving an
   explicit operator witnessing each consistent set. Candidate witnesses to
   check:
    (W1) CDT intervention (change the action port only);
    (W2) oracle / designated-slot substitution;
    (W3) syntactic substitution of literal copies;
    (W4) extensional matching (local and global versions);
    (W5) FDT with a supplied dependency graph (state what the graph is);
    (W6) Fallenstein's modal third-person counterfactuals (partial);
    (W7) logical-induction conditioning with epsilon-exploration (state the
         exact construction and whether its values depend on the exploration
         scheme).
P4 Main theorem: decide whether there is a minimal inconsistent family of
   THREE OR MORE desiderata, each individually satisfiable and natural, with
   every proper subset consistent. If so, prove it and show independence with
   explicit witnesses. If not, prove that every inconsistency contains a
   singleton or pairwise core.
P5 Robustness: does the answer change for (a) globally total vs promise-total
   agents; (b) inclusion or exclusion of fixed constants; (c) restriction to
   injective or otherwise informative agents; (d) probabilistic K (values are
   distributions or credences rather than exact rationals); (e) policy-level
   counterfactuals (changing T on all owned inputs at once) rather than
   single-input counterfactuals?
P6 Test cases: for each witness in P3, compute the verdicts on Newcomb (the
   predictor calls the agent), twin prisoner's dilemma, 5-and-10, the
   fixed-copy diagonal, and Fernando's Anti-Newcomb:
     U(one-box) = 2x, U(two-box) = 2x + 1, with x = 1 iff f(d) = one-box,
   where f is the agent's own algorithm written into the environment.
   State which desiderata decide whether Anti-Newcomb is treated as Newcomb.
P7 Philosophical counterpart: relate the results to the counterpossibles
   debate (vacuism vs non-vacuism; impossible-worlds semantics). Say whether
   any non-vacuist semantics from that literature yields an operator
   satisfying the consistent sets found in P3.

6. LITERATURE (verify every citation; flag any that cannot be confirmed)
 Demski & Garrabrant, "Embedded Agency" (2018/2019, arXiv:1902.09469);
 Fallenstein, "Third-person counterfactuals" and the modal UDT posts;
 Soares & Fallenstein, "Toward Idealized Decision Theory" (2015);
 Benson-Tilsen, "UDT with Known Search Order" (MIRI 2014-4);
 Garrabrant et al., "Logical Induction" (2016);
 Yudkowsky & Soares, "Functional Decision Theory" (2017);
 Skalse (2021); work on the "chicken rule" and exploration-based
 counterfactuals; Nolan, "Impossible Worlds: A Modest Approach to the Logic of
 Counterfactuals" (Notre Dame J. Formal Logic, 1997); Williamson,
 "Counterpossibles" (Topoi, 2018); Berto, French, Priest & Ripley,
 "Williamson on Counterpossibles" (J. Philosophical Logic, 2018).
 Report the closest existing impossibility result for logical counterfactuals,
 if any, and how it differs from P4's answer.

7. CLOSURE CRITERION
Round 5 is complete when it delivers: precise versions of D1-D10; answers to
L1-L6; the full consistency map with witnesses; the P4 verdict (sharp theorem
or reduction theorem); the P5 robustness answers; the P6 test-case table; and
verified citations with a novelty assessment. If a sharp theorem is found,
state it as the final form of the thesis:
  "the obstacle to an optimal decision rule is not choosing well, but
   defining coherently what the alternatives to one's own choice are."
If not, state the strongest true replacement.

8. OUTPUT FROM EACH AGENT
For each task attempted: definitions, theorem statements, complete proofs or
explicit counterexamples, every stipulation beyond this statement, any errors
found in §0, and full citations (author, title, venue, year, section/page).