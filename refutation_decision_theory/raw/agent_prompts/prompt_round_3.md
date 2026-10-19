PROBLEM (ROUND 3): Menu semantics, causal invariance, and a dichotomy theorem
for decision theories

0. CONTEXT AND GOAL
Rounds 1-2 established that, within a single problem, the conflicts between
optimality criteria are shallow (singletons and pairs, the central pair being
Briggs 2010). Two cross-problem results look substantive:
 (T2) No neutral, non-trivial choice rule is both invariant under row
      translations and contraction-consistent.
 (T3) Under neutrality, affine invariance, binary independence and ordering, the
      only rules are: increasing diagonal, decreasing diagonal, or universal
      indifference.
Candidate thesis (the DICHOTOMY):
  "Menu-coherent evaluation forces ex-ante evaluation; causal evaluation
   cannot be menu-coherent without becoming trivial."
Goal of round 3: decide whether the dichotomy survives its weakest point, the
semantics of shrinking a menu; strengthen T3 into an exact characterization;
make the domain requirements explicit; and settle novelty.

1. MODEL (fixed)
1.1 A problem D: finite extensive form, no information set repeated on a path;
    deterministic policies Pi_D; structural plans S_D; a law mu_pi on S_D for
    every policy pi (well-defined, fair: fixed features of D, independent of
    the identity of the theory evaluated); payoffs U_D(s, pi).
1.2 Causal matrix: M_D[pi, sigma] = sum over s of mu_pi(s) * U_D(s, sigma).
    Row pi = causal evaluation of every policy under the beliefs induced by
    pi. Diagonal = ex-ante value V_D.
1.3 Realizability (round 1): every finite real square matrix is M_D for some
    fair, well-defined D.
1.4 Rules: a reflexive relation >=_M on the index set I, with recommendation
    G(M) = {i : no j with j >_M i}, required to be nonempty for every M. Index
    labels persist under restriction. Single-valued selectors and mixed
    lotteries are out of scope unless a task says otherwise.

2. AXIOMS (from round 2; same names)
N  Neutrality: simultaneous permutation of rows and columns permutes the output.
F  Common affine invariance: M -> a*M + b*11^T with a > 0.
R  Row translations: M -> M + b*1^T for any vector b (adding b_i to every entry
   of row i).
P  Column Pareto: column sigma weakly above column tau in every row, strictly in
   one, implies sigma >_M tau.
D  Diagonal optimality: G(M) is contained in argmax_i M_ii.
B  Binary independence across sizes: each comparison agrees with the comparison
   in its principal 2x2 restriction.
S  Briggs's self-sovereignty: preserving both candidates' full rows (same index
   set) preserves their comparison.
C  Contraction: G(M) intersected with K is contained in G(M|_K). THE
   RESTRICTION OPERATOR IS NOW A PARAMETER (see §4).
O  Ordering: >=_M is complete and transitive.
Q  Non-triviality: for some fixed I, two matrices yield different choice sets.

3. ESTABLISHED RESULTS (accept unless an error is found)
E1 Under N, F (no R), the minimal inconsistent subsets of
   {N,F,P,L,D,J,B,S,C,O,Q} are {L}, {J}, {P,D}, {P,B}, {P,S}, {P,C}, where L
   is restricted Pareto and J is global ratifiability. Witnesses: column sums
   for {N,F,P,O,Q}; diagonal ranking for {N,F,D,B,S,C,O,Q}.
E2 With R added: the new minimal inconsistent subsets are {R,D}, {N,R,B,Q} and
   {N,R,C,Q}, where C uses PRINCIPAL restriction (deleting rows and columns
   together). Proof of {N,R,C,Q}: normalize each row so its diagonal entry is
   zero, embed the matrix as a principal submatrix of a circulant using index
   labels 2^i mod m with m > 2(2^(k-1) - 1), and apply shift-symmetry plus
   contraction. Each one-axiom deletion is satisfiable (by a responsive
   fixed-label rule, diagonal maximization, row-range maximization, and
   all-tied, respectively). The theorem needs menus of unbounded size; with a
   fixed maximum size it fails.
E3 T3: under A0 (reduction to M), N, F, B, O, the only rules are increasing
   diagonal, decreasing diagonal, and universal indifference. This needs menus
   of at least three options.
E4 Commitment: every row of the commitment matrix equals V_D, for every
   coupling. Hence, in Newcomb, the A3-vs-C4 reversal holds iff
   m(1-2eps) > c; the structural C2-vs-C4 reversal holds only at eps = 0,
   under every coupling.
E5 Taxonomy: without B, or with S in place of B, there are 2^(|R|) distinct
   rules; finite benchmark suites cannot certify P or D.

4. CENTRAL TASK: SEMANTICS OF A SMALLER MENU
Removing options from a problem can be modeled in at least three ways:
 C_pr  Principal restriction: delete the removed options' rows AND columns.
       (A smaller menu also removes the beliefs one would have if one chose
       the removed options.)
 C_col Column restriction: keep all rows, delete only the columns. The input
       becomes a rectangular matrix (belief states x available options);
       define rules, the axioms and G on this rectangular domain.
 C_ref Fixed-reference restriction: rows are averaged by a reference
       distribution over belief states, as in fixed-prior CDT; state exactly
       how the reference distribution transforms under restriction.
Tasks:
 M1 Realizability. For each semantics, decide whether a menu restriction
    corresponds to a fair, well-defined problem D' obtained from D (removing
    policies from the agent while keeping the predictor's response law). State
    which semantics, if any, is forced by the model of §1, and which require
    extra stipulations.
 M2 Re-prove or refute E2's theorem {N,R,C,Q} under C_col and under C_ref.
    In particular, decide whether column-sum ranking (fixed-prior CDT)
    satisfies N, R, C and Q under each semantics. If the theorem fails under
    some semantics, find the strongest replacement impossibility there, or
    prove that none exists among the §2 axioms.
 M3 Give the complete minimal-inconsistent / maximal-consistent map of §2
    under C_col (for N, F, R, P, D, B, S, C, O, Q), with witnesses and proofs.
 M4 Determine whether the DICHOTOMY holds under each semantics, and state it
    precisely as a theorem in each case where it does.

5. STRENGTHENING T3
 S1 Monotonicity. Define diagonal monotonicity (Mon): raising M_ii, all else
    fixed, never removes i from G(M) and never makes i worse in >=_M. Prove
    that N, F, B, O, Q and Mon single out increasing diagonal ranking, i.e.
    ex-ante evaluation.
 S2 Weaker independence. Replace B by C (each semantics of §4) plus O. Do
    N, F, C, O, Q and Mon still force diagonal ranking? If not, characterize
    every rule satisfying them, or give the family's size and a natural
    sub-characterization.
 S3 State T3 and S1/S2 with their exact minimal domain requirements (minimum
    menu size; which matrices must be in the domain).

6. DOMAIN REQUIREMENTS FOR T2
 Q1 Identify a domain-richness condition, stated in terms of which matrices
    the domain must contain (e.g. circulants of all sizes, or symmetric
    embeddings), that is necessary and sufficient for {N,R,C,Q} to be
    inconsistent.
 Q2 Decide whether natural physical restrictions on problems preserve that
    richness: bounded payoffs (e.g. in [0,1]); predictors whose accuracy is
    bounded away from 1; at most k agent actions per information set; at most
    one information set.

7. INTERPRETATION OF R
 I1 Prove or refute: a rule satisfies R iff it depends on M only through the
    row-normalized matrix Z_ij = M_ij - M_ii (equivalently, within-row
    differences).
 I2 Classify the following theories in matrix form as satisfying R or not,
    specifying the matrix semantics used for each: fixed-prior CDT (column
    weights); ratifiability (Jeffrey, Skyrms); deliberational CDT (Arntzenius;
    Joyce); EDT with the reference-policy law; ex-ante/FDT-style evaluation.
    State whether "R = causal evaluation" is a theorem, a good approximation,
    or false.

8. LITERATURE AND NOVELTY
 L1 Verify these citations, reporting exact theorem statements and page or
    section numbers: Briggs, "Decision-Theoretic Paradoxes as Voting
    Paradoxes," Philosophical Review 119(1), 2010, §6; Fink & Ruiz, "Every
    graph is an induced isopart of a circulant," Czechoslovak Math. J. 36(2),
    1986; Basu Mallik & Bhattacharya, "Consistency and social choice:
    Possibilities and impossibilities," Mathematical Social Sciences, 2026;
    Halpern, "A Note on the Existence of Ratifiable Acts," Review of Symbolic
    Logic 13(3), 2020; Bell, Linsefors, Oesterheld & Skalse, NeurIPS 2021.
    Flag any that cannot be confirmed.
 L2 Search for prior statements of E2/T2, E3/T3 and the dichotomy, in:
    social choice (Sen's alpha and neutrality impossibilities; symmetric or
    circulant profiles; tournament solutions and contraction consistency);
    decision theory (choice-dependent credences and menu dependence in CDT;
    Joyce; Egan, "Some Counterexamples to Causal Decision Theory," 2007;
    Wedgwood; Spencer & Wells; Ahmed). Report the closest result, the exact
    differences, and whether the dichotomy as stated appears anywhere.

9. CLOSURE CRITERION
Round 3 closes the problem when it delivers:
 (a) a justified choice of menu semantics (M1), or results under all three;
 (b) the status of T2 and the complete consistency map under that semantics
     (M2-M3);
 (c) the DICHOTOMY as a precise theorem with its exact assumptions, or a proof
     that it fails, with the strongest true replacement (M4);
 (d) the exact characterization in S1 and the answer to S2;
 (e) domain-richness conditions (Q1-Q2);
 (f) the verdict on I1-I2;
 (g) verified citations and a novelty assessment (L1-L2).

10. OUTPUT FROM EACH AGENT
For each task attempted: definitions, theorem statements, complete proofs or
explicit counterexamples, every stipulation beyond §1-4, any errors found in
§3, and full citations (author, title, venue, year, section/page) for every
source used.