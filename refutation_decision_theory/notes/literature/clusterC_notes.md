# Cluster C: verification notes

Checked 2026-10-19. The main source is the Crossref API (`api.crossref.org/works/<doi>`), which returned authors, title, venue, volume, issue, pages and date for every DOI listed below. Books were checked against library catalogues and publisher pages. Statuses:

- **VERIFIED**: every bibliographic field in the .bib entry was confirmed by at least one authoritative source.
- **PARTIAL**: some fields or claims could not be confirmed. Each case is explained.
- **UNVERIFIED**: the entry carries a `note = {UNVERIFIED: ...}`.

## Arrow

**arrow1951**: VERIFIED. Wiley, New York (with Chapman & Hall, London), 1951, Cowles Commission Monograph No. 12.
- Sources: Wikipedia record and library catalogues; Cowles Foundation page for CFM 12 (2nd ed.).
- Contribution: the general (im)possibility theorem. No social welfare function on an unrestricted domain satisfies weak Pareto, IIA and non-dictatorship (for at least 3 alternatives).

**arrow1963**: VERIFIED. 2nd ed., Wiley, 1963, Cowles Foundation Monograph 12. Adds "Notes on the Theory of Social Choice, 1963".

**arrow2012**: VERIFIED. 3rd ed., Yale University Press, New Haven, 2012, ISBN 9780300179316, foreword by Eric Maskin. Catalogue records describe it as a reprint of the 1963 Wiley edition.
- Note: no "Yale reprint of the 2nd ed." exists as a separate edition. The Yale printing is the 2012 third edition.

**arrow1959**: VERIFIED (Crossref). Economica (new series) 26(102):121–127, May 1959, DOI 10.2307/2550390.
- Contribution: suppose a choice function is defined on all finite (at least all two- and three-element) subsets. Then it is rationalised by a weak ordering if and only if it satisfies the Weak Axiom of Revealed Preference. Arrow's own condition, C5, is equivalent to WARP on that domain. This is the result Brandt & Harrenstein (2011, p. 2) cite as "rationalized by a complete and transitive relation iff WARP".

## Chernoff and May

**chernoff1954**: VERIFIED (Crossref). Econometrica 22(4):422–443, Oct. 1954, DOI 10.2307/1907435.
- Contribution: the origin of the contraction condition, often called "Chernoff's condition". If x is chosen from S and x ∈ T ⊆ S, then x is chosen from T. Sen (1969/1971) later named it property α.
- Both Brandt–Harrenstein 2011 and Basu Mallik–Bhattacharya cite Chernoff 1954 for this.

**may1952**: VERIFIED (Crossref). Econometrica 20(4):680–684, Oct. 1952, DOI 10.2307/1907651.
- Contribution: characterises simple majority rule for two alternatives as the only rule satisfying four conditions: decisiveness, anonymity, neutrality and positive responsiveness.
- It is the standard early source of a formal neutrality axiom (symmetry under relabelling alternatives).

## Sen

**sen1970**: VERIFIED. Holden-Day, San Francisco, 1970, Mathematical Economics Texts 5, xii+225 pp., ISBN 0816277656.
- Co-published by Oliver & Boyd, Edinburgh. This rests on CiNii catalogue records, not the title page.
- Later printings: North-Holland reprint 1979 (Advanced Textbooks in Economics 11); expanded edition Penguin 2016 and Harvard University Press 2017.
- Use year 1970, not 1969.
- Contribution: the systematic framework of collective choice rules. It covers the liberal paradox, quasi-transitive and acyclic social preference, and the possibility of social decision functions.

**sen1971**: VERIFIED (Crossref). Review of Economic Studies 38(3):307–317, July 1971, DOI 10.2307/2296384.
- Contribution: introduces and names properties α (contraction), β and γ (expansion).
- Proves that a choice function on all finite nonempty subsets is rationalisable by some (complete, reflexive) binary relation if and only if it satisfies α and γ. In BH 2011 Theorem 1 this appears as "rationalizable iff α and γ".
- α and β together are equivalent to rationalisability by an ordering, which is equivalent to WARP. That links back to Arrow 1959.
- Caution: the usual "α + β ⇔ WARP / ordering" statement and the "α + γ ⇔ rationalisable" statement are distinct results. Cite them separately.

**sen1977**: VERIFIED (Crossref). Econometrica 45(1):53–89, DOI 10.2307/1913287. Added because BH 2011 cite it for impossibility results that use only α (or weakened α) in Arrow's framework.

**sen1993**: VERIFIED (Crossref). Econometrica 61(3):495–521, May 1993, DOI 10.2307/2951715. One secondary record says 495–522; Crossref and RePEc give 495–521.
- Contribution: argues that "internal consistency" conditions such as α and WARP cannot be judged without reference to something external to choice, such as menu-dependence or objectives.
- Gives a version of Arrow's general possibility theorem that does not require internal consistency of social choice.
- Useful when motivating α as a substantive, not purely logical, requirement.

## Plott, Moulin and related

**plott1973**: VERIFIED (Crossref). Econometrica 41(6):1075–1091, Nov. 1973, DOI 10.2307/1914037.
- Contribution: introduces path independence, C(S ∪ T) = C(C(S) ∪ C(T)), and studies its relation to rationality and to Arrow-type social choice.
- Path independence is equivalent to α plus Aizerman's condition (Aizerman–Malishevski, as noted in BH 2011, Remark 2).

**moulin1985**: VERIFIED (Crossref and Springer). Social Choice and Welfare 2(2):147–160, Sept. 1985, DOI 10.1007/BF00437315.
- Contribution: a survey of rationalisability of choice functions on finite sets by one or several preference relations, via α, Aizerman and related conditions. The abstract says none of the main results is original.
- An earlier U. Minnesota working-paper version is dated 1984.

**moulin1986**: VERIFIED (Crossref). Social Choice and Welfare 3(4):271–291, Dec. 1986, DOI 10.1007/BF00292732.
- Contribution: axiomatises the uncovered set and compares it with the Copeland set and the sophisticated-agenda set.
- This is the standard reference for tournament solutions as neutral choice correspondences on tournaments.

**bordes1976**: VERIFIED (Crossref). Review of Economic Studies 43(3):451–457, DOI 10.2307/2297222. Added as optional.
- Contribution: early study of consistency (α-type and expansion-type) for majority-based choice.
- Shows the top cycle is the smallest majoritarian rule satisfying β+.

**blairetal1976**: VERIFIED (Crossref). Blair, Bordes, Kelly and Suzumura, JET 13(3):361–379, Dec. 1976, DOI 10.1016/0022-0531(76)90047-8. Added as optional.
- Contribution: Arrow-type impossibility theorems for social choice functions in which collective rationality is replaced by choice-consistency conditions (α and others).
- With α, IIA and Pareto they obtain veto or oligarchy-type conclusions. This is the classical "Arrow with α" line closest in form to the paper.

## Tournaments

**laslier1997**: VERIFIED (Crossref). Springer, Berlin/Heidelberg, 1997, series Studies in Economic Theory, DOI 10.1007/978-3-642-60805-6, ISBN 9783642645617 (print reprint) / 9783642608056 (e-book).
- The series volume number ("vol. 7") is from memory, was not confirmed by Crossref, and is omitted from the .bib.
- Contribution: the standard monograph on tournament solutions. Its definition requires Condorcet consistency, and it states the standard axioms: monotonicity, the superset property (SSP), independence of unchosen alternatives (IUA) and composition-consistency.

**brandt2009**: PARTIAL.
- Title: Brandt's CV lists "Tournament Solutions – Extensions of Maximality and their Applications to Decision-Making". The publication list in the same CV cites it as "Habilitation Thesis, Faculty for Mathematics, Computer Science, and Statistics, University of Munich, 2009". The CV's education section dates the habilitation to January 2010. The .bib uses 2009, as the author does, and records the discrepancy in a note.
- Not confirmed: the thesis text itself, so I could not locate its §2.4 or quote it.
- The requested §2.4 remark ("neutral nonempty tournament solutions select every vertex of a vertex-transitive tournament") is supported in substance by:
  - Brandt 2011 (JET, "Minimal stable sets", arXiv 0803.2138 v4, §2). It defines tournament functions as "stable with respect to tournament isomorphisms" and calls a tournament "homogeneous (or vertex-transitive)" if every pair a, b is related by an automorphism. That paper grew out of the habilitation.
  - Brandt, Brill & Harrenstein 2016, §3.2.3: "Non-emptiness and neutrality imply that every tournament solution has to select all alternatives in a 3-cycle." The 3-cycle is the smallest vertex-transitive case.
  - The general claim is immediate. Neutrality makes S(T) invariant under Aut(T), so S(T) is a union of Aut(T)-orbits; vertex-transitivity means a single orbit; non-emptiness then gives S(T) = A.
  - Recommendation: cite BBH 2016 (§3.2.3) and/or Brandt 2011 alongside, or instead of, the habilitation "§2.4", unless the section number can be checked against a copy.

**brandtbrillharrenstein2016**: VERIFIED (Crossref and Oxford ORA). Ch. 3, pp. 57–84, Handbook of Computational Social Choice, eds. F. Brandt, V. Conitzer, U. Endriss, J. Lang, A. D. Procaccia, Cambridge University Press, 2016 (published 25 Apr 2016), DOI 10.1017/CBO9781107446984.004.
- Contribution, from the text:
  - Tournament solutions are equivalent to neutral C1 functions (invariance under isomorphisms), and Condorcet consistency is not built in.
  - Neutrality plus non-emptiness forces selecting all of a 3-cycle.
  - The trivial solution TRIV satisfies monotonicity, stability and composition-consistency.

**brandtharrenstein2011**: VERIFIED (Crossref). JET 146(4):1721–1731, July 2011, DOI 10.1016/j.jet.2011.03.006 (arXiv 0910.3580).
- Contribution: defines set-rationalizability and set-analogues of Sen's α and γ (α̂, γ̂).
  - A choice function satisfies α̂ if and only if it is set-rationalizable (Theorem 2).
  - It satisfies α̂ and γ̂ if and only if it is self-stable (Theorem 3).
- The intro notes that α, "and even substantially weakened versions of α", yield Arrow-spirit impossibilities (citing Sen 1977), whereas γ is satisfied by, for example, the uncovered set.

**brandt2011**: VERIFIED (Crossref). JET 146(4):1481–1499, DOI 10.1016/j.jet.2011.05.004. Added as optional, as the citable published counterpart of the habilitation's main ideas.

## Recent consistency paper

**basumallikbhattacharya2026**: VERIFIED for metadata, PARTIAL for content.
- Metadata (Crossref): Arkarup Basu Mallik and Mihir Bhattacharya, "Consistency and social choice: Possibilities and impossibilities", Mathematical Social Sciences vol. 144, Dec. 2026, article 102582, DOI 10.1016/j.mathsocsci.2026.102582. The DOI resolves to Elsevier PII S0165489626000892.
- ScienceDirect returned 403, so the journal abstract was not read.
- Content: checked against the working paper, Ashoka Univ. Econ. Discussion Paper 142, "Consistency and social choice", March 2025. Basu Mallik is at ISI Kolkata and Bhattacharya at Ashoka University. The working paper states:
  - Setting: a single public good is chosen, with an unrestricted domain of strict preferences. The objects are social choice *functions* (single-valued) f(S, profile) defined on variable feasible sets S ⊆ X.
  - **Theorem 1**: if |X| ≥ 3 and |N| ≥ 2, no s.c.f. satisfies anonymity, Pareto efficiency and contraction consistency. Contraction consistency means: if f(S) ∈ T ⊆ S then f(T) = f(S). This is Chernoff/α for single-valued rules.
  - **Characterisation**: the Priority Rule (pick the highest alternative in a fixed ordering among the Pareto-efficient alternatives of S) is the unique s.c.f. satisfying Pareto efficiency and "Efficient Dominance" (ED), a WARP-type condition restricted to Pareto-efficient alternatives.
- The journal title adds "Possibilities and impossibilities". The published version may contain further results not in the WP.
- They mention Koray (2000) as an impossibility for unanimous, neutral, self-selective SCFs.

## Combinatorics

**finkruiz1986**: VERIFIED (Crossref and DML-CZ). John Frederick Fink and Sergio Ruiz, Czechoslovak Math. J. 36(2):172–176, 1986, DOI 10.21136/CMJ.1986.102080, MR 831304, Zbl 0614.05052.
- Contribution: every graph is an induced isopart of a circulant graph. This strengthens Fink's earlier "induced isopart of a regular graph".
- The powers-of-two / distinct-differences labelling (so that differences are distinct and no unintended circulant edges arise) is the user's description. I did not check it against the full text, but the DML-CZ PDF is freely available to confirm.

**erdosturan1941**: VERIFIED (Crossref). P. Erdős and P. Turán, J. London Math. Soc. s1-16(4):212–215, Oct. 1941, DOI 10.1112/jlms/s1-16.4.212.
- Contribution: the classical source on Sidon sets (B₂ sequences: all pairwise sums, equivalently all differences, are distinct), including the √n upper-bound estimate.
- A natural citation for "distinct-differences" sets. Optional.

## Analysis and probability tools

**kakutani1941**: VERIFIED. Duke Math. J. 8(3), 1941, DOI 10.1215/S0012-7094-41-00838-4 (Crossref; Crossref gives no page range). Pages 457–459 come from ProofWiki and the Lean/mathlib problem page.
- Contribution: fixed-point theorem for upper semicontinuous (closed-graph) correspondences with nonempty convex values from a compact convex set (simplex) into itself.

**strassen1965**: VERIFIED (Crossref). Annals of Mathematical Statistics 36(2):423–439, April 1965, DOI 10.1214/aoms/1177700153. Crossref gives the given name only as "V."; it is Volker Strassen.
- Contribution: existence of probability measures with given marginals.
- Its corollary for ordered spaces: P ≤_st Q if and only if there is a coupling (X, Y) with X ≤ Y almost surely. This is the standard source for the coupling characterisation of stochastic dominance.

**lindvall1992**: VERIFIED. Torgny Lindvall, Lectures on the Coupling Method, Wiley, New York, 1992 (Wiley Series in Probability and Mathematical Statistics), ISBN 0-471-54025-0.
- Corrected republication: Dover, Mineola NY, 2002, ISBN 0-486-42145-7.
- Contribution: textbook treatment of couplings, including the stochastic-domination and Strassen-type results.

## Closest prior results ("neutrality + α + invariance ⇒ choose everything"; valued tournaments)

1. **Neutral tournament solutions on symmetric tournaments** (BBH 2016 §3.2.3; Brandt 2011 §2; Laslier 1997).
   - What it shows: isomorphism invariance (neutrality) together with non-emptiness forces S(T) = A whenever T is vertex-transitive (3-cycles, regular "rotational" tournaments).
   - BBH 2016 state it explicitly for the 3-cycle. Brandt 2011 defines homogeneous (vertex-transitive) tournaments and the irregularity property: IRR means a solution can exclude alternatives in some regular tournament.
   - The literature asks whether solutions can exclude alternatives in regular, non-vertex-transitive tournaments (IRR), and which ones can (Banks set, ME). It treats the vertex-transitive case as trivial.
   - How it differs: it is a one-tournament symmetry argument. It does not use contraction consistency to propagate "choose everything" to *non-symmetric* inputs.

2. **α plus Condorcet consistency is incompatible on tournaments.** This is folklore, implied by the 3-cycle argument above.
   - Neutrality makes a 3-cycle {a, b, c} with a ≻ b ≻ c ≻ a select all three. Restricted to {a, b}, Condorcet consistency selects {a}. But α requires b to stay chosen, a contradiction.
   - So among neutral tournament solutions, only non-Condorcet-consistent ones such as TRIV satisfy α in full generality.
   - BH 2011 (intro) and Sen 1977 report that α "and even substantially weakened versions" lead to Arrow-type impossibilities, while γ-type expansion consistency is compatible with good majoritarian rules (uncovered set, minimal covering set, bipartisan set, top cycle).
   - I did not find an explicit published theorem of the form "every neutral tournament solution satisfying α is TRIV". Treat any such phrasing as folklore unless proved in the paper.

3. **Arrow-style impossibilities with α instead of collective rationality.**
   - Sen 1977 and Blair–Bordes–Kelly–Suzumura 1976 work in the profile-based setting with IIA, Pareto and α (and variants). They obtain dictatorship, veto or oligarchy-type conclusions.
   - **Basu Mallik & Bhattacharya 2026** (MSS 144, 102582) is the most recent: anonymity, Pareto and contraction consistency are incompatible for single-valued SCFs (|X| ≥ 3, n ≥ 2), and they characterise the Priority Rule under Pareto and Efficient Dominance.
   - How it differs: these are about *profiles of individual orderings* and single-valued or rationalisable rules. Their escape routes are veto power, priority orders or dropping anonymity, not "choose everything". The paper's setting (correspondences on real square matrices, with neutrality as invariance under simultaneous row/column permutation) is a cardinal, single-input analogue. It sits closer to tournament-solution theory than to profile-based Arrow theory.

4. **Valued / weighted / generalised tournaments.**
   - **Dutta & Laslier 1999** (SCW 16(4):513–532): "comparison functions" g with g(x, y) = −g(y, x), i.e. skew-symmetric real matrices. They extend the uncovered set, minimal covering set and bipartisan/essential set to this setting and study their axiomatic properties.
   - **De Donder, Le Breton & Truchon 2000** (MSS 40(1):85–109): C2 rules on weighted tournaments, which depend on majority margins. These are the weighted top cycle, uncovered set, minimal covering set and bipartisan set, compared set-theoretically with Kemeny, Kramer–Simpson and Borda.
   - **Laslier 2000** (SCW 17(2):269–282): metadata verified via Crossref. Its abstract, as read through a summary of the IDEAS page and not verbatim, concerns the Essential set (support of optimal mixed strategies in the symmetric electoral game) and a cloning-consistency axiom in a variable-agenda setting. BH 2011 cite it among the sources for the uncovered set satisfying expansion consistency (γ). Its content is only partly verified.
   - **Holliday, Norman, Pacuit & Zahedian** (arXiv 2208.06907; Contemporary Mathematics, AMS, "Mathematical Analyses of Decisions, Voting, and Games", 2023 per arXiv journal-ref): neutral weighted tournament solutions and margin graphs. They prove (SAT-assisted) incompatibility of binary γ (expansion consistency) with weakened resoluteness. AMS volume and page numbers are UNVERIFIED.
   - Also relevant: Fischer, Hudry & Niedermeier, "Weighted tournament solutions", ch. 4 of the same Handbook. It was not separately verified and is not in the .bib.
   - How they differ: all of these work with *skew-symmetric* matrices (margins), are concerned mainly with refining choice (excluding alternatives), and generally impose expansion-type (γ) rather than contraction-type (α) consistency. α is generally known to be too strong. The paper's results act on general square real matrices (not necessarily skew-symmetric) and derive "choose everything" or impossibility from neutrality + α + binary independence + invariance. I found no prior result with exactly this combination for cardinal or matrix-valued inputs.
