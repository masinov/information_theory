PROBLEM (ROUND 2): Cross-problem impossibility theorems for decision theories

0. STATUS AND WORKING THESIS
Round 1 established, within a single problem, that:
 - a total deterministic theory satisfying ex-ante optimality on every
   well-defined finite problem exists (pick an ex-ante maximizer per problem);
   hence "no decision theory is optimal" is false as stated;
 - all incompatibilities among the within-problem criteria C1-C5 are singletons
   or pairs ({C3}, {C1,C2}, {C2,C4}); there is no Arrow-style family of three
   or more criteria;
 - the core conflict (C1 vs C2 in Newcomb) is Nozick's (1969).
Working thesis for round 2: a non-trivial, Arrow-style impossibility for
decision theories, if one exists, must come from CROSS-PROBLEM consistency
axioms (invariance, independence, contraction), not from within-problem
optimality criteria.
Goal: close the question. Either prove a sharp cross-problem impossibility
theorem with independent axioms, or prove that every inconsistency among the
natural axioms below reduces to a singleton or pairwise conflict. In both cases,
determine what prior work (especially Briggs 2010) already covers.

1. MODEL (fixed from round 1)
1.1 A problem D is a finite extensive-form problem in which no information set
    occurs twice on one path. Its deterministic policies are Pi_D = prod over
    h in H_D of A_h, with each A_h finite and nonempty.
1.2 Structural environment plans: a finite set S_D; for every policy pi a
    distribution mu_pi on S_D; and a payoff U_D(s, pi) obtained by traversing
    the tree with plan s and policy pi. A plan specifies every non-agent
    response, including responses on branches that are not taken.
    V_D(pi) = sum over s of mu_pi(s) * U_D(s, pi).
1.3 Well-definedness: mu_pi is defined for EVERY pi in Pi_D.
    Fairness: S_D, U_D and the map pi -> mu_pi are fixed features of D; nothing
    depends on the identity or source code of the theory being evaluated.
    Fixed algorithms may appear as constants of the environment.
1.4 A decision theory T assigns to every D a policy T_D (or, in §3, a choice set
    or ranking). There is no uniformity requirement, so lookup tables are allowed.

2. WITHIN-PROBLEM CRITERIA AND ROUND-1 RESULTS (accept unless an error is found)
Let R_h(pi) = {s : h is reached under (s, pi)} and r_pi(h) = mu_pi(R_h(pi)).
Let pi[h<-a] be pi with only its prescription at h changed. For r_pi(h) > 0,
  Q_pi(h,a) = [ sum over s in R_h(pi) of mu_pi(s) * U_D(s, pi[h<-a]) ] / r_pi(h).
C1 Ex-ante optimality: T_D maximizes V_D.
C2 Structural causal dominance: at a positively reached h, never choose b if
   some a satisfies U_D(s, pi[h<-a]) > U_D(s, pi[h<-b]) for every s in
   R_h(pi), including states to which mu_pi assigns probability zero.
C3 Ratifiability: at every positively reached h, pi(h) maximizes Q_pi(h, .).
   (C3 implies C2.)
C4 Commitment stability: in the commitment extension K(D), T commits to a
   policy that agrees with T_D at every information set positively reached
   under T_D.
Round-1 results:
 R1 A universal C1 theory exists.
 R2 Newcomb with symmetric error eps < 1/4: C1 requires one-box; C2 and C3
    require two-box.
 R3 For a single always-reached choice, dominance and ex-ante optimality can
    conflict for some payoffs in [0,1] iff the induced state laws mu_a are not
    all equal.
 R4 No deterministic policy satisfies C3 in Death in Damascus.
 R5 Bomb, with the bomb observed: there are four policies; for
    0 < eps < 1/(M+1), C1 selects (L,L) and C2/C3 select (R,L).
 R6 With product coupling in K(D) and exact prediction, C2 and C4 are
    inconsistent.
 R7 Maximal consistent subsets of C1-C5: {C1,C4,C5} and {C2,C5}.
 R8 No finite benchmark suite certifies C1 for arbitrary lookup tables.
 R9 Mixed policies: C1 and C3 solutions exist when p -> mu_p is continuous
    (by compactness and Kakutani's theorem); without continuity, there are
    counterexamples.

3. REDUCED FORM: THE CAUSAL MATRIX
For a problem D, define the square matrix indexed by policies
  M_D[pi, sigma] = sum over s of mu_pi(s) * U_D(s, sigma),
the value of running sigma while the environment responds as it would to pi.
The diagonal is V_D. Row pi is the causal evaluation of all policies under the
beliefs induced by pi.
Realizability (round 1): every finite real square matrix is M_D for some fair,
well-defined D (exact prediction of the chosen index, with U(s=i, a=j) = M_ij).
So rules on matrices have an unrestricted domain, as in Arrow's theorem.
Deleting a set of policies (their rows and columns) is also realizable; this
defines restriction for contraction axioms.

4. CROSS-PROBLEM AXIOMS (candidates; refine definitions where needed)
A theory is a choice rule G(M), a nonempty subset of the indices, or a ranking
>=_M on the indices, defined for all finite real square matrices.
A0 Reduction (consequentialism): T depends on D only through M_D, up to
   relabeling of policies.
A1 Neutrality: permuting indices (rows and columns together) permutes the
   output.
A2 Affine invariance: replacing M by alpha*M + beta with alpha > 0 leaves the
   output unchanged. (Optionally, also study row-wise translations.)
A3 Row-Pareto: if M[pi,sigma] >= M[pi,tau] in every row pi, with at least one
   strict inequality, then tau is not chosen (or sigma > tau).
   Variant A3r (restricted Pareto): the same condition, required only in rows
   sigma and tau.
A4 Diagonal optimality (C1 in reduced form).
A5 Global ratifiability: a chosen pi maximizes row pi. (Individually
   unsatisfiable for deterministic choice by R4; include it in the mixed
   variant.)
A6 Binary independence (IIA): the comparison of sigma and tau depends only on
   the 2x2 submatrix on {sigma, tau}.
   Variant A6b (Briggs's self-sovereignty): it depends only on rows sigma and
   tau in full.
A7 Contraction consistency (Sen's alpha): if pi is chosen in M and survives
   into a restriction M', then pi is chosen in M'.
A8 Ordering: >=_M is complete and transitive. For choice rules: G is
   rationalizable by a weak order.
A9 Non-triviality: excludes constant rules and rules that ignore M entirely
   (state precisely).
Reference witnesses to check against the axioms: diagonal maximization (A4),
fixed-weight row averages (A3), maximin over rows, the uniform structural
measure selector from round 1, and global-ratifiability selection where it
exists.

5. TASKS
P1 Literature verification (do first). Obtain and verify Briggs, "Decision-
   Theoretic Paradoxes as Voting Paradoxes" (Philosophical Review, 2010), §6,
   and Skalse, "A General Counterexample to Any Decision Theory and Some
   Responses" (arXiv 2101.00280, 2021). State their theorems exactly, translate
   them into the axioms of §4, and say which tasks below they already settle.
   Also check Bell, Linsefors, Oesterheld & Skalse (NeurIPS 2021) and Halpern's
   note on the existence of ratifiable acts. Report any other Arrow-style
   result in decision theory.
P2 Consistency map. For the axioms of §4 (exclude any judged unnatural, with
   reasons), determine all inclusion-minimal inconsistent subsets and all
   maximal consistent subsets, with an explicit witness rule for every
   consistent set and a proof for every inconsistent one.
   Lead to verify: A3r together with A8 may already fail on a 3x3 cyclic matrix
   of the Death-in-Damascus type (for example, a > b, b > c and c > a each
   forced by restricted Pareto).
P3 Main theorem. Decide whether there is a minimal inconsistent family of
   THREE OR MORE axioms, each individually satisfiable and natural, with every
   proper subset consistent. If so, prove it, show each axiom is independent by
   exhibiting rules for the subsets, and compare it with Briggs. If not, prove
   a reduction theorem: every inconsistency among the listed axioms contains a
   singleton or pairwise inconsistent core.
P4 Coupling gap from round 1. R6 used product coupling and exact prediction.
   Make the commitment extension K(D) depend on a coupling lambda (a joint law
   over prod over q of supp(mu_q) with marginals mu_q). Characterize the
   couplings and error levels eps >= 0 for which C2 (or A3) conflicts with C4.
   In particular, decide whether a shared-noise (comonotone) coupling preserves
   the conflict at eps > 0 while the product coupling destroys it.
P5 Taxonomy, i.e. "the relevant problem types are few." Under A0 + A1 + A2,
   and with or without A6, decide whether a theory is determined by finitely
   many parameters (for example, by its behavior on 2x2 matrices modulo affine
   transformations). If so, give the parameterization, and decide whether a
   finite benchmark suite then certifies A3 or A4 compliance, contrasting with
   R8. If not, prove that no finite parameterization exists.
P6 Mixed policies (secondary). Extend the P2/P3 results to mixed policies under
   the continuity conditions of R9, including A5.
P7 Evidential criterion (optional). If C6 is used, give two or more evidential
   semantics (reference-policy law, self-knowledge conditioning) and state
   which results depend on the choice.

6. CLOSURE CRITERION
The problem counts as closed when we have:
 (a) a verified account of Briggs (2010) and Skalse (2021) in §4 terms;
 (b) the complete consistency map from P2;
 (c) either a sharp theorem (P3, positive) or a reduction theorem (P3, negative);
 (d) answers to P4 and P5;
 (e) a final statement of the thesis, with its scope, saying which parts are
     new and which are already known.

7. EXPECTED OUTPUT FROM EACH AGENT
For every task attempted: exact definitions used, theorem statements, complete
proofs or counterexamples, every stipulation made beyond §1-4, any errors found
in round-1 results, and full citations for any literature relied on (author,
title, venue, year, section).