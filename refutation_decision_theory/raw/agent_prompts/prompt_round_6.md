PROBLEM (ROUND 6): Optimal decision theories exist only as non-computable objects

0. BACKGROUND (from earlier rounds; accept unless an error is found)
 - If problems are specified independently of the decision theory (each
   problem fixes how the world responds to every policy), an optimal theory
   exists trivially: choose an optimal policy problem by problem. A uniform
   rule ("choose the policy with the best expected result given how the world
   responds to it") also works. In that class, no problem can refer to the
   theory being evaluated, so "unfair" problems are excluded by construction.
 - If the theory is a program and environments may contain fixed copies of
   computable programs, every globally total computable theory T is defeated:
   an environment computes c = T(d), its own description being d, and pays
   1 iff the agent's action differs from c. Switching theories only moves the
   target.
 - A promise-total computable optimizer exists on deterministic finite-policy
   environments that terminate under every table policy (simulate each policy,
   take the best). An environment trying to embed it does not halt, so it is
   not admissible.
 - On almost-surely terminating stochastic environments with payoffs in {0,1},
   no computable rule (even promise-total) selects an exact expected-payoff
   maximizer everywhere, by recursive inseparability.
Goal: state and prove ONE clean theorem separating "case-by-case optimal
choice" from "optimal decision program", with exact hypotheses, the degree of
non-computability required, and its relation to existing results.

1. TARGET THEOREM (to be made precise, proved, and sharpened)
 (a) Against all admissible computable environments, including those
     containing fixed copies of arbitrary computable programs, an optimal
     decision theory EXISTS.
 (b) No globally total computable theory is optimal on that class: every one
     has an environment built against it.
 (c) Hence every globally total optimal theory is non-computable. On the
     stochastic class, every optimal theory is non-computable, even
     promise-total ones.
 (d) "Unfair" problems, those built against the theory, exist exactly for
     theories that environments can compute.

2. MODEL (fix precisely; state any change)
2.1 Descriptions are finite strings. Each admissible environment E has a
    finite set of owned queries Q_E (disjoint across environments), including
    its root description d(E), with finite action sets and finite policy
    space Pi_E.
2.2 Environments are programs. They may:
     - call the evaluated agent ONLY on owned queries (designated oracle calls);
     - contain arbitrary fixed computable programs as constants, including
       programs that compute some candidate theory.
    Deterministic class C_det: E^pi halts with an exact rational payoff for
    every table policy pi in Pi_E, and every embedded constant halts on the
    inputs on which it is called.
    Stochastic class C_sto: E draws from computable finite-support
    distributions, terminates almost surely for every table policy, and has
    rational payoffs in [0,1] (state the precise conditions).
2.3 Agents: arbitrary functions T from descriptions to legal actions, not
    necessarily computable. Distinguish:
     - globally total computable (halts on every string);
     - promise-total computable (halts on admissible inputs);
     - non-computable (state the Turing degree when relevant).
2.4 Evaluation: U(E,A) = the payoff of E when every designated oracle call is
    answered by A, while embedded constants stay fixed. (Designated calls are
    linked to the agent; embedded programs are not.) T is optimal on a class
    C if U(E,T) >= U(E,A) for every E in C and every agent A. For C_sto, use
    expected payoff.
2.5 Unrestricted foreign queries (an environment calling the agent on
    descriptions it does not own) are excluded; §5 task F treats them as a
    boundary case.

3. TASKS
E1 Existence. Prove that optimal agents exist on C_det and on C_sto. Show
   that the per-environment argmax policies are mutually consistent (owned
   queries are disjoint) and assemble into one total function on all
   descriptions, with a fixed default off the admissible class.
E2 Diagonal. Prove that for every globally total computable T there is an
   E_T in C_det (deterministic, binary, payoffs in {0,1}, F_self) with
   U(E_T,T) < max over A of U(E_T,A). Use the recursion theorem or a
   self-description mechanism, and verify that E_T is admissible.
E3 Escape. Prove that the diagonal cannot be built against an optimal T:
    (i)  for non-computable T, no embedded constant computes T;
    (ii) a computable constant may still AGREE with T on finitely many
         inputs. Show that no admissible environment exploits this. In
         particular, hard-coding k = T(d(E)) into E changes d(E). Prove that
         no E in C_det has a constant forcing T to be non-optimal, or find a
         counterexample.
    (iii) explain exactly why the promise-total computable optimizer escapes
         (inadmissibility of the embedding environment), and whether that
         escape depends on the choice of admissibility condition.
E4 Degree of non-computability. Determine the Turing degree needed for an
   optimal agent:
    - On C_det with globally total output: is membership in C_det decidable
      relative to 0' (the halting problem)? Is some optimal agent computable
      from 0'? Is 0' necessary, i.e. does every globally total optimal agent
      compute 0', or some other non-zero degree?
    - On C_sto: give upper and lower bounds (exact argmax of computable reals
      with ties; checking almost-sure termination).
    - Relativization: for every oracle X, if environments may be
      X-computable and contain X-computable constants, is every optimal agent
      non-X-computable? State and prove the relativized diagonal.
E5 Sharpness. For each hypothesis (owned queries only; designated calls
   linked and constants fixed; termination under all table policies; exact
   rational payoffs; global vs promise totality), show by example what fails
   if it is dropped.
E6 Unfairness characterization. Give a precise definition of an "unfair"
   environment (one constructed against a particular theory) that is not
   circular, and prove or refute: a theory T faces an environment in which it
   is non-optimal iff some admissible environment can compute T on its own
   owned queries. If only one direction holds, state which.

4. BOUNDARY CASES
F  Unrestricted foreign queries: confirm that no agent at all, computable or
   not, is optimal (two environments rewarding opposite answers to the same
   query), so the theorem needs owned queries.
G  Linked embedded copies: if embedded programs equal to the agent are
   treated as linked rather than fixed, decide whether the diagonal of E2
   still works. Relate this to the fact (earlier rounds) that whether an
   embedded program is linked or fixed cannot be read off its actual
   behaviour.
H  Bounded resources: if agents and environments are time-bounded, decide
   whether an analogue of the theorem holds (an optimal agent exists only
   above the environments' resource bound).

5. LITERATURE (verify every citation; flag any that cannot be confirmed)
 Skalse, "A General Counterexample to Any Decision Theory and Some
 Responses" (arXiv:2101.00280, 2021); Yudkowsky & Soares, "Functional
 Decision Theory" (arXiv:1710.05060), on fairness; Fallenstein, "'Evil'
 decision problems in provability logic"; Leike & Hutter, "On the
 Computability of AIXI" (UAI 2015) and "Bad Universal Priors and Notions of
 Optimality" (COLT 2015); standard sources on the recursion theorem,
 relativization and Turing degrees. Report the closest existing statement of
 the target theorem and exactly how it differs.

6. CLOSURE CRITERION
Round 6 is complete when it delivers:
 - the theorem of §1 stated with exact hypotheses and fully proved (E1-E3);
 - the degree bounds of E4, including the relativized diagonal;
 - the sharpness examples of E5;
 - the unfairness characterization of E6;
 - the boundary cases F-H;
 - verified citations and a novelty assessment.
Final statement to confirm or correct:
  "Optimal choice is always possible problem by problem, but no decision
   program that environments can run is optimal: unfair problems exist
   exactly for computable theories."

7. OUTPUT FROM EACH AGENT
For each task: definitions, theorem statements, complete proofs or explicit
counterexamples, every stipulation beyond this statement, any errors found
in §0, and full citations (author, title, venue, year, section/page).