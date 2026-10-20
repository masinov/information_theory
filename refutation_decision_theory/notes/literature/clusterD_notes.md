# Cluster D: verification notes

Checked 2026-10-20. Sources used:

- the Crossref API (`api.crossref.org/works/<doi>`) for every DOI;
- the arXiv API (`export.arxiv.org/api/query`) for arXiv versions and dates;
- the LessWrong / Alignment Forum GraphQL API (`lesswrong.com/graphql`) for post titles, authors, `postedAt` dates and original IAFF item ids (`agentFoundationsId`);
- Wayback Machine snapshots of `agentfoundations.org/item?id=N`, to cross-check IAFF dates;
- MIRI's publications page (`intelligence.org/all-publications/`) and the MIRI PDFs themselves.

Theorem, section and page numbers were read from the PDFs named in each entry.

Statuses:

- **VERIFIED**: every bibliographic field in the .bib entry was confirmed by at least one authoritative source.
- **PARTIAL**: some fields or claims could not be confirmed. Each case is explained.
- **UNVERIFIED**: not confirmed. No entry in this cluster ended up UNVERIFIED.

The entries are in `latex/refs_D.bib`. Its `verification` fields are non-printing; biber ignores them with a datamodel warning, as it does in refs.bib.

## Computability

**rice1953**: VERIFIED (Crossref). Trans. AMS 74(2):358–366, 1953, DOI 10.1090/S0002-9947-1953-0053041-6.
- Crossref lists the author by surname only. The given name "Henry Gordon" in the entry is from memory; the printed form "H. G. Rice" is confirmed by Péter's JSL review (DOI 10.2307/2268870).
- Content: Rice's theorem. Every nontrivial index set (class of r.e. sets) is undecidable. The theorem number inside the paper was not checked.

**kleene1938**: VERIFIED (Crossref). J. Symbolic Logic 3(4):150–155, Dec. 1938, DOI 10.2307/2267778.
- Content: the paper in which the (second) recursion theorem first appears, according to Moschovakis 2010.
- The location of the theorem within the paper (page, numbering) was **not checked**.

**moschovakis2010**: VERIFIED (Crossref). Bull. Symbolic Logic 16(2):189–239, June 2010, DOI 10.2178/bsl/1286889124.
- Do not confuse it with the shorter CSL 2009 paper of the same title (LNCS 5771, pp. 24–39, DOI 10.1007/978-3-642-04027-6_5).
- Content: a survey of the second recursion theorem's applications (self-reference, fixed points).

**konig1927**: VERIFIED (no DOI, so confirmed from secondary records). Vol. 3, no. 2–3, pp. 121–130, June 1927.
- The journal's official title is *Acta Litterarum ac Scientiarum Regiae Universitatis Hungaricae Francisco-Josephinae, Sectio Scientiarum Mathematicarum* (Szeged), now *Acta Sci. Math. (Szeged)*.
- Sources: N. Markey's bibliography record "actaszeged3(2-3)-Kon"; Wikipedia, "Kőnig's lemma"; Dean & Walsh, "The Prehistory of the Subsystems of Second-Order Arithmetic" (arXiv:1612.06219), which places the lemma (Unendlichkeitslemma) on p. 122.
- The title is sometimes printed with "Schlußweise". The author is Dénes Kőnig (not Julius König).

**cook1971**: VERIFIED (Crossref). Proc. 3rd Annual ACM STOC ('71), pp. 151–158, DOI 10.1145/800157.805047.
- The venue (Shaker Heights, Ohio, May 1971) is from memory and not recorded in the entry.
- Content: the NP-completeness of SAT (Cook's theorem).

## Provability logic

**lob1955**: VERIFIED (Crossref). J. Symbolic Logic 20(2):115–118, March 1955, DOI 10.2307/2266895.
- Content: Löb's theorem. If ⊢ □P → P then ⊢ P.

**boolos1993**: VERIFIED.
- Bibliographic details: CUP, Cambridge, 1993, xxxvi+276 pp.
  - Source: Artemov's review, JSL 60(4):1316–1317, 1995, DOI 10.2307/2275893; NYPL catalogue.
  - Hardback ISBN 0-521-43342-8; paperback 978-0-521-48325-4.
  - Crossref DOI 10.1017/CBO9780511625183 gives the online date 1994-02-25. Use 1993.
- Content: the standard reference for GL (Gödel–Löb), Solovay's completeness theorems, and the de Jongh–Sambin fixed-point theorem.
- Chapter numbers were **not confirmed**. Cite by topic, or check a copy before giving chapter or page numbers.

## Program equilibrium

**tennenholtz2004**: VERIFIED (Crossref). Games Econ. Behav. 49(2):363–373, Nov. 2004, DOI 10.1016/j.geb.2004.02.002.
- Content: introduces program equilibrium. Players submit programs that can read each other's code, and mutual cooperation in the one-shot PD becomes an equilibrium (via a syntactic-equality program).

**barasz2014**: VERIFIED (arXiv API). arXiv:1401.5577 [cs.GT], v1 22 Jan 2014, v2 5 Apr 2021.
- Authors are as given. arXiv spells the first author "Mihaly Barasz"; the entry uses Bárász.
- Note: MIRI's publications page lists the title as "Robust Cooperation **on** the Prisoner's Dilemma"; arXiv has "**in**". Use the arXiv title.
- The v2 comment says the paper was "Updated 2021 to indicate that bounded analogues of these results have yet to be proved".
- Content, checked in the v2 PDF:
  - Theorem 3.1: PA ⊢ [FairBot(FairBot) = C].
  - Theorem 3.2: PrudentBot is unexploitable, cooperates with itself and with FairBot, and defects against CooperateBot.
  - Section 4: the modal-agents framework, using Theorem 4.1 (arithmetic soundness of GL), Theorem 4.2 (modal fixed-point theorem) and Theorem 4.3 (uniqueness of modal fixed points).
- A related workshop version: LaVictoire et al., "Program Equilibrium in the Prisoner's Dilemma via Löb's Theorem", AAAI 2014 MIPC workshop (per MIRI's page). It has no entry here.

**critch2019**: VERIFIED (Crossref). J. Symbolic Logic 84(4):1368–1381, Dec. 2019 (online 2 Apr 2019), DOI 10.1017/jsl.2017.42.
- arXiv:1602.04184, per MIRI's page. The earlier title was "Parametric Bounded Löb's Theorem and Robust Cooperation of Bounded Agents".
- Content: a resource-bounded ("parametric bounded") Löb theorem, giving robust cooperation between bounded open-source agents (bounded FairBot-style agents).
- Theorem numbers were **not checked**.

## MIRI reports and proof-based UDT

**lavictoire2015**: VERIFIED.
- Number and URL: MIRI technical report 2015-6, according to MIRI's publications page and the Demski–Garrabrant 2019 bibliography. URL intelligence.org/files/lob-notes-IAFF.pdf.
- Dates:
  - The PDF title page is dated February 23, 2015.
  - MIRI's release announcement is dated 18 Mar 2015.
  - An earlier version was announced on IAFF as item 94 by "orthonormal" (LaVictoire), AF date 2015-01-22.
- Content, from the PDF's table of contents:
  - §3.2 "Löbian cooperation", p. 6.
  - §3.3 "Spurious counterfactuals", p. 8.
  - §6.2 "Fixed points of modal statements", p. 17.
  - §7.1 "Modal Combat in the Prisoner's Dilemma", p. 20.
  - §7.2 "Modal Decision Theory", p. 23. It presents the "Slepnev–Fallenstein model of UDT" (Algorithm 3).

**bensontilsen2014**: VERIFIED.
- MIRI technical report 2014-4 (MIRI publications page; the PDF carries no number). Dated August 22, 2014 (PDF). URL intelligence.org/files/UDTSearchOrder.pdf.
- Content:
  - §2 describes spurious counterfactuals in Slepnev's proof-based UDT, and Nesov's diagonalisation clause, "playing chicken against the universe" (credited via [Slepnev 2011]).
  - **Corollary 4.6, "Playing chicken with the universe is the only way to win"** (begins on p. 6): given only the action and outcome sets, setting every fᵢ = ∞ (or sup of the outcomes) is the only search strategy that guarantees maximal utility.
  - The abstract states the same corollary.

**soaresfallenstein2015agi**: VERIFIED.
- Crossref: chapter DOI 10.1007/978-3-319-21365-1_17, pp. 156–165, Springer, Cham, 2015. Editors Bieger, Goertzel, Potapov. Book subtitle "8th International Conference, AGI 2015, Berlin, Germany, July 22–25, 2015, Proceedings".
- LNCS vol. 9205 is from the Springer book page and library catalogues. Some catalogues label it LNAI 9205.
- ISBNs: print 978-3-319-21364-4, eBook 978-3-319-21365-1.
- It is the abridged version of "Toward Idealized Decision Theory" (arXiv:1507.01986), as MIRI's page states. Content was not re-read here.

**fallenstein2013fiveandten** (extra entry): VERIFIED.
- "The 5-and-10 Problem and the Tiling Agents Formalism", MIRI Brief Technical Note 2013-9 (MIRI page; Demski–Garrabrant 2019 bibliography). URL intelligence.org/files/TilingAgents510.pdf.
- It is a write-up from the Dec. 2013 MIRI workshop.
- Content:
  - Explains that Slepnev's proof-based UDT is vulnerable to the 5-and-10 problem while Yudkowsky–Herreshoff tiling agents are not.
  - Cites Slepnev's "What a reduction of 'could' could look like" and "An example of self-fulfilling spurious proofs in UDT".
  - Mentions "Vladimir Slepnev's solutions: Playing chicken and 'A model of UDT without proof limits'".
- Demski–Garrabrant (2019, §2.1) cite this note, with Garrabrant 2017, for the five-and-ten problem.

## Fallenstein's IAFF posts (modal UDT)

Original venue: Intelligent Agent Foundations Forum (agentfoundations.org), now hosted on the AI Alignment Forum and mirrored on LessWrong.

- The "AF date" is the `postedAt` field from the LessWrong/AF API.
- The "Wayback" figure comes from the relative "N days ago" label in a 7 May 2015 snapshot. That label is floored, so the estimate may run up to about one day early.

**fallenstein2015evil**: VERIFIED, with a date caveat. "'Evil' decision problems in provability logic". IAFF item 47.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic
- **Date caveat**: the AF date is 2015-01-10, but that is not the original date. The Wayback label "176 days ago" gives about 12 Nov 2014, and "An optimality result for modal UDT" (item 50) refers to this post as "yesterday". The .bib uses `date = {2014-11}`.
- The requested key says "2015" while the content is from 2014. The key was kept as requested, but authoryear will print 2014.
- Main result:
  - Defines modal decision theories and "provably extensional" (fair) modal decision problems in GL.
  - Formalises drnickbone's argument: for every modal decision theory T there is a provably extensional "evil" problem that gives T the second-best outcome, while any agent acting differently gets the best outcome. So no modal decision theory, including modal UDT, is optimal on all fair problems.

**fallenstein2014optimality**: VERIFIED. "An optimality result for modal UDT". IAFF item 50.
- Dates: AF date 2014-11-15; Wayback ≈ 13 Nov 2014. The entry uses `date = {2014-11}`.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8f/an-optimality-result-for-modal-udt
- Main theorem: for every provably extensional modal decision problem P there is a sound (true) closed GL formula φ such that modal UDT searching for proofs in PA + φ achieves the best outcome any decision theory can achieve on P.
- It is a modal version of an unpublished bounded-proof-length result by Easwaran, Soares and Fallenstein.

**fallenstein2014improving**: VERIFIED. "Improving the modal UDT optimality result". IAFF item 76.
- Dates: AF date 2014-11-23; Wayback ≈ 24 Nov 2014. Consistent.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ea9/improving-the-modal-udt-optimality-result
- Main theorem (Christiano's suggested strengthening, proved in detail): for every modal decision theory T and provably extensional problem P, take any true φ such that GL + φ proves which action T takes on P and which outcome it gets. Then UDT^(φ) does at least as well on P as T does.
- Search-engine summaries also mention a "strong enough consistency axiom" simplification (Benja and Marcello). That phrase was **not** found in the post body retrieved via the API. It may be in a comment or a later edit, so do not cite it to this post without checking.

**fallenstein2015third**: VERIFIED. "Third-person counterfactuals". IAFF item 98.
- Dates: AF date 2015-02-03; Wayback ≈ 1 Feb 2015. The entry uses `date = {2015-02}`.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebf/third-person-counterfactuals
- Main content:
  - Distinguishes first-person counterfactuals (used in modal UDT's definition) from third-person ones (needed to state optimality).
  - Defines a UDT-based notion of logical third-person counterfactuals, which "fails visibly" (returns an error) in the cases raised by Soares's "global UDT" post.
  - This is a definition and discussion, not a single theorem.

**fallenstein2015chicken**: VERIFIED. "The odd counterfactuals of playing chicken". IAFF item 99, a follow-up to item 98.
- Dates: AF date 2015-02-02; Wayback ≈ 2 Feb 2015. The AF dates put this post a day before item 98, but the item numbers and the text show it was written after it. The entry uses `date = {2015-02}`.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ec0/the-odd-counterfactuals-of-playing-chicken
- Main result:
  - With a provability oracle, chicken-style UDT treats models of PA as impossible worlds, and the only models where A() = a are those where "A() ≠ a" is provable.
  - A 5-and-10 variant: action 1 gives the best outcome unless it is provable the agent does not take action 1, in which case it gives the worst. Action 2 always gives the middle outcome.
  - On this problem modal UDT takes action 2. The problem is "fully informative", so the third-person optimality notion certifies this arguably wrong behaviour as optimal.

## Logical induction and later

**garrabrant2016li**: VERIFIED (arXiv API and v5 PDF). arXiv:1609.03543 [cs.AI], v1 12 Sep 2016, v5 7 Dec 2020. Authors as given.
- **Theorem 4.6.1 (Closure under Finite Perturbations)**, §4.6 "Non-Dogmatism", p. 36 of v5, proof in App. G.7. Statement: if two markets agree for all but finitely many n, one is a logical inductor iff the other is.
- **Definition 4.7.1 (Conditional Probability)**, §4.7 "Conditionals", p. 38. V(φ | ψ) := V(φ∧ψ)/V(ψ) if V(φ∧ψ) < V(ψ), and 1 otherwise.
- **Definition 4.8.2 (Expectation)**, §4.8 "Expectations", p. 40. The approximate expectation operator with precision k is E_k^V(X) := Σ_{i=0}^{k−1} (1/k)·V("X > i/k").
- Page numbers are for v5. Earlier versions may paginate differently.

**garrabrant2017obstacles**: VERIFIED. "Two Major Obstacles for Logical Inductor Decision Theory". IAFF item 1399.
- Dates: AF date 2017-04-17; Wayback (20 Jul 2018, "458 days ago") ≈ 18 Apr 2017. Consistent.
- URL: https://www.alignmentforum.org/posts/5bd75cc58225bf06703753d4/two-major-obstacles-for-logical-inductor-decision-theory
- Content:
  - Obstacle 1, "untaken actions are not observable". There is a logical inductor for which the conditional-expectation agent on the 5-and-10 problem converges to 5: one wealthy trader sets E(U | A=5) ≈ .5 and E(U | A=10) ≈ 0, and is never penalised because the A=10 condition is never true. ε-exploration, described as "analogous [to] the chicken rule", fixes convergence but has its own problems.
  - Obstacle 2, "no updatelessness for computations".

**demskigarrabrant2019**: VERIFIED (arXiv API and v3 PDF). arXiv:1902.09469 [cs.AI], v1 25 Feb 2019, v3 6 Oct 2020.
- **The five-and-ten problem is §2.1 "Action counterfactuals", pp. 7–10 (v3)**, within §2 "Decision theory".
- It cites Fallenstein 2013 and Garrabrant 2017b for the problem, and gives the Löbian proof of the spurious counterfactual ("We call this a 'spurious proof'", p. 9).

**leikehutter2015**: VERIFIED (PMLR page). "Bad Universal Priors and Notions of Optimality", Proc. 28th Conference on Learning Theory, PMLR vol. 40, pp. 1244–1259.
- COLT 2015, Paris, 3–6 July 2015. Editors Grünwald, Hazan, Kale.
- Content, from the PMLR abstract:
  - Unlucky or adversarial choices of the UTM make AIXI "misbehave drastically".
  - Legg–Hutter intelligence, and hence balanced Pareto optimality, is "entirely subjective".
  - "Every policy is Pareto optimal in the class of all computable environments."
- PMLR's publication date is 2015-06-26. Theorem numbers were not checked.

**taylor2020**: VERIFIED. Jessica Taylor, "Two Alternatives to Logical Counterfactuals".
- Blog: unstableontology.com, 2020-04-01. Note the URL slug is `/2020/04/01/alternatives-to-logical-counterfactuals/`, not "two-alternatives-…".
- LessWrong/AF copy (user jessicata, `af: true`), 2020-04-01: https://www.lesswrong.com/posts/yBdDXXmLYejrcPPv2/two-alternatives-to-logical-counterfactuals
- Content: argues that logical counterfactuals are unsatisfactory, and offers two replacements: counterfactual nonrealism, and policy-dependent source code.

## Origin of the "5-and-10 problem" and the "chicken rule" (fiveandten)

Findings, from the earliest source found to the latest. All dates come from the LessWrong API.

1. **drescher2009**: VERIFIED. Gary Drescher, comment on Yudkowsky's "Ingredients of Timeless Decision Theory", LessWrong, **2009-08-20**.
   - URL: https://www.lesswrong.com/posts/szfxvS8nsxTgJLBHs/ingredients-of-timeless-decision-theory?commentId=pcafc8AS82DuJxZu5
   - Old comment id 1217 (base 36) = 49291.
   - States the pattern without the $5/$10 illustration: actions A1…An, value of Ai = i. "Suppose I choose A6. I know I'm a utility-maximizing agent … Therefore … A6 has a value of at least 7."
   - lukeprog's "So You Want to Save the World" (LessWrong, dated 2012-01-01; comments from 27 Dec 2011) links to this comment as the description of "the '5-and-10 problem' … by Gary Drescher, who doesn't use the 5-and-10 example illustration".
   - **This is the earliest verifiable written source found for the problem itself.**
2. **slepnev2010**: VERIFIED. Vladimir Slepnev (cousin_it), "What a reduction of 'could' could look like", LessWrong, **2010-08-12**.
   - It is a repost of an email to the decision-theory-workshop list.
   - It introduces the proof-searching agent ("agent()==A implies world()==U"), the setting in which spurious proofs arise.
   - It does not discuss 5-and-10 itself.
3. **slepnev2011**: VERIFIED. Slepnev, "A model of UDT with a halting oracle", LessWrong, **2011-12-18** (old URL /lw/8wc/).
   - **Earliest verifiable written statement of the chicken rule**, phrased as step 1: "Play chicken with the universe: if S proves that A()≠a for some action a, then return a."
   - The post says "The basic idea is due to Vladimir Nesov and me". Benson-Tilsen 2014 credits the chicken clause to Nesov, "as reported in [Slepnev 2011]".
   - The LessWrong wiki 5-and-10 page cites this post's comments for the "heavy ghost" variant.
4. **The name "5-and-10"**:
   - It appears in writing by **Dec 2011** in lukeprog's post: Kaj_Sotala's comment of 2011-12-27; lukeprog's reply quotes "Stuart Armstrong's explanation of the 5-and-10 problem (sometimes known as the heavy ghost problem)"; Vladimir_Nesov's correction of 2011-12-28.
   - Armstrong's text appears to be a LessWrong wiki entry whose original date I could not determine.
   - **The person who coined the name was not identified.** No earlier dated written use was found; it probably arose in the 2010–2011 decision-theory-workshop mailing list discussions, but that is unverified.
5. **slepnev2012**: VERIFIED. Slepnev, "An example of self-fulfilling spurious proofs in UDT", LessWrong, **2012-03-25**.
   - The first explicit Löbian construction of a spurious proof, with payoffs 5 vs 10.
   - It credits **Benja Fallenstein** as "the first to point out that spurious proofs pose a problem for UDT".
6. **fallenstein2013fiveandten**: VERIFIED (MIRI note 2013-9, Dec. 2013). The first MIRI report-style document with "5-and-10" in its title.

Recommendation:
- For the problem: cite drescher2009 (first written statement) and slepnev2012 (first explicit Löbian spurious-proof construction), with fallenstein2013fiveandten or demskigarrabrant2019 §2.1 as the standard later references.
- For the chicken rule: cite slepnev2011, attributing the idea to Nesov and Slepnev.
- Do not attribute the coinage of "5-and-10" to anyone without further evidence.

## Corrections to the brief

- **fallenstein2015evil** was originally posted in **mid-November 2014** (IAFF item 47), not 2015. The 2015-01-10 Alignment Forum date is not the original.
- **taylor2020**: the blog slug omits "two-"; the URL is given above.
- **barasz2014**: MIRI's page writes "on the Prisoner's Dilemma"; arXiv has "in". The latest arXiv version is v2 (2021), which carries a caveat about bounded analogues.
- **soaresfallenstein2015agi**: LNCS 9205, pp. 156–165, DOI 10.1007/978-3-319-21365-1_17. Some catalogues call it LNAI 9205.
- **lavictoire2015** exists and is verified as MIRI TR 2015-6.
- Extra entries added for the origin question: drescher2009, slepnev2010, slepnev2011, slepnev2012, fallenstein2013fiveandten.
