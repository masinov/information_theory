# Cluster B: verification notes (checked 2026-10-19)

Notation used in the annotations: M[i,j] is the expected value of option j under the beliefs induced by choosing i. The diagonal M[i,i] is the evidential expected utility of i, which Podgorski calls i's "self-esteem".

Sources used: Crossref API (DOI metadata), arXiv abstract pages, the LessWrong GraphQL API (post dates and text), the NeurIPS proceedings BibTeX, and full texts that I downloaded and read. The full texts were:
- Yudkowsky & Soares (arXiv v2)
- Skalse (arXiv)
- Bell et al. (NeurIPS PDF)
- Halpern (NSF PAR author version)
- Briggs (published PDF, archived copy)
- Podgorski (author's preprint)
- Oesterheld & Conitzer, de se paper (CMU PDF)
- Yudkowsky, TDT (MIRI PDF)

---

## FDT / TDT / UDT

### yudkowskysoares2017: VERIFIED
- **Citation:** Eliezer Yudkowsky and Nate Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality", arXiv:1710.05060 [cs.AI].
- **Versions:** v1 13 Oct 2017; v2 22 May 2018. The arXiv page shows no journal reference.
- **Fairness (§9 "The Global Perspective", read in the v2 text):**
  - The informal notion is "dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand. Informally, we call these sorts of problems 'fair problems.'"
  - On the open problem: "there may be a general-purpose decision theory that matches or outperforms all rivals in fair dilemmas, if a satisfactory notion of 'fairness' can be formalized."
  - Footnote 15 gives the "punish anyone who acts like Fiona's copy" example. It says "It remains unclear how to transform a problem that's unfair to one decision theory into an analogous one that is unfair to a different one ... in a reasonably principled and general way."
  - The Conclusion (§10) lists as future work "A simple formal criterion for distinguishing fair dilemmas from unfair ones".
  - §2 already says Newcomb's problem is "fair game" because the predictor rewards predicted actions, not decision procedures. It forward-references §9.
- **Relevance:** This is the canonical statement that FDT is claimed optimal on "fair" problems and that the formal fairness criterion is left open. Your cross-problem axioms can be presented as one way of filling that gap.

### levinsteinsoares2020: VERIFIED (Crossref)
- **Citation:** Benjamin A. Levinstein and Nate Soares, *J. Phil.* 117(5): 237–266, 2020, doi:10.5840/jphil2020117516.
- **Content (abstract):** The paper gives new counterexamples to EDT and CDT, "including one in which the optimal action is causally dominated". It presents FDT through subjunctive dependence.
- **Relevance:** This is the peer-reviewed venue for FDT. It is the one to cite when a refereed source is needed.

### soaresfallenstein2015: VERIFIED (arXiv)
- **Citation:** Nate Soares and Benja Fallenstein, arXiv:1507.01986 (7 Jul 2015, v1 only).
- **Comment field:** "extended version of a paper accepted to AGI-2015". I did not verify the AGI-2015 proceedings version (LNCS, Springer), so I cite the arXiv version.
- **Relevance:** Argues for policy selection and logical counterfactuals as the target for an idealised decision theory.

### yudkowsky2010: VERIFIED (PDF title page)
- **Citation:** The PDF cites itself as "Yudkowsky, Eliezer. 2010. Timeless Decision Theory. The Singularity Institute, San Francisco, CA."
- **Hosting and length:** It is hosted at intelligence.org/files/TDT.pdf with a MIRI cover page and runs 120 pages.
- **Citability:** It is citable as a technical report. It was not peer reviewed.
- **Relevance:** TDT is the precursor to FDT. It treats the decision as the output of an abstract computation.

### dai2009: VERIFIED (LessWrong API)
- **Citation:** Wei Dai, "Towards a New Decision Theory", LessWrong, posted 2009-08-13.
- **Citability:** This is the standard citation for the origin of UDT. Citable only as @online.
- **Relevance:** This is the policy-selection idea: choose the input–output map that is optimal under the prior. It is the "ex ante policy optimality" side of your dichotomy.

### macaskill2019: VERIFIED (LessWrong API, full text)
- **Citation:** Will MacAskill (username wdmacaskill), "A Critique of Functional Decision Theory", LessWrong, 2019-09-13, cross-posted to the AI Alignment Forum.
- **Bomb, verbatim:**
  - "You face two open boxes, Left and Right, and you must take one of them. In the Left box, there is a live bomb; taking this box will set off the bomb, setting you ablaze, and you certainly will burn slowly to death. The Right box is empty, but you have to pay $100 in order to be able to take it."
  - "A long-dead predictor predicted whether you would choose Left or Right, by running a simulation of you and seeing what that simulation did. If the predictor predicted that you would choose Right, then she put a bomb in Left. If the predictor predicted that you would choose Left, then she did not put a bomb in Left, and the box is empty."
  - "The predictor has a failure rate of only 1 in a trillion trillion. Helpfully, she left a note, explaining that she predicted that you would take Right, and therefore she put the bomb in Left."
  - The case also stipulates that you are the last person in the universe.
- **Verdicts:** FDT takes Left. CDT and EDT take Right.
- **Guaranteed Payoffs, verbatim:** "In conditions of certainty — that is, when the decision-maker has no uncertainty about what state of nature she is in, and no uncertainty about the utility payoff of each action is — the decision-maker should choose the action that maximises utility."
- **Relevance:** This is the sharpest case where ex ante policy optimality (Left: a 10^-24 chance of death against a $100 cost) and ex post or ratifiable choice come apart.

### skalse2021: VERIFIED (full text)
- **Citation:** Joar Skalse (Oxford), arXiv:2101.00280 [cs.AI], 1 Jan 2021, v1 only. The arXiv page shows no journal reference.
- **Construction:**
  - For any decision theory XDT, DP(XDT) has a transparent box with $1,000 and an opaque box. The agent takes exactly one box.
  - The opaque box is empty if XDT *permits* taking the opaque box; otherwise it contains $2,000. The agent knows this.
  - If XDT recommends exactly one box, a theory YDT that inverts the recommendation does better by $1,000.
  - If XDT permits both, the opaque box is empty, and YDT = "take transparent with prob. 1" weakly dominates. The case where 1 ∈ S (S being the set of probabilities with which XDT permits taking the opaque box) is handled separately.
  - The construction extends to prior-dependent theories as DP(ZDT, D).
  - Skalse argues DP(XDT) is not "unfair" in the FDT sense: the outcome depends only on the action, and the set-up only requires computing XDT's output.
- **Responses discussed:**
  1. Exclude the problem as unfair. Skalse finds no principled criterion for doing so.
  2. Argue the agents face different problems. He distinguishes *physical*, *experiential* and *epistemic* equivalence of decision situations. Under epistemic equivalence, XDT and YDT agents face different problems, since they assign different values to P(state | action), so the argument fails. The cost is that this also individuates Newcomb's problem by the agent's self-knowledge.
  3. XDT is still "right" (taking the transparent box) even though YDT earns more.
- **Footnote 1:** A satisfactory theory must permit at least one act. This rules out plain ratificationism, citing Egan 2007.
- **Relevance:** The "epistemic equivalence" individuation of problems is essentially your choice of the causal matrix as the problem's identity.

---

## AI / learning approaches, ratifiability, formal results

### oesterheldconitzer2021: VERIFIED (Crossref; author page)
- **Citation:** *Phil. Quarterly* 71(4): 701–716, 2021, doi:10.1093/pq/pqaa086.
- **Content:** In the "Adversarial Offer", two boxes cost $1 each. The seller puts $3 in each box she predicts the buyer will *not* buy, with accuracy 0.75. CDT buys a box and loses money in expectation. The paper extends this to a diachronic Dutch book against CDT.
- **Relevance:** This is a money-pump argument for ex ante policy evaluation over causal (ratifiable-style) choice.

### belletal2021: VERIFIED (official NeurIPS BibTeX and paper PDF)
- **Citation:** James Bell, Linda Linsefors, Caspar Oesterheld and Joar Skalse, *Advances in Neural Information Processing Systems* 34, eds. Ranzato, Beygelzimer, Dauphin, Liang and Wortman Vaughan. Curran Associates, pp. 22146–22157. NeurIPS 2021 spotlight.
- **Definitions:**
  - An NDP (Newcomblike decision process) is *continuous* if the transition function T and reward R are continuous in the policy.
  - Definition 1: π is *strongly ratifiable* on M if supp(π(·|s)) ⊆ argmax_a q_π(a|s) for all s ∈ M.
- **Theorem 2:** A model-free agent's limit policy is strongly ratifiable on the states it visits infinitely often.
- **Theorem 3, verbatim:** "Every continuous NDP has a strongly ratifiable policy." The proof is via Kakutani. The paper notes discontinuous NDPs may have none.
- **Further results:** Theorem 5 covers weak ratifiability. Theorem 6, the "Repellor Problem", shows non-convergence.
- **Relevance:** Value-based RL converges, if at all, to ratifiable policies, that is, causal/ratifiable fixed points rather than ex ante optima. Newcomb is the example: the only strongly ratifiable policy is two-boxing.

### halpern2020: VERIFIED (Crossref; author version read)
- **Citation:** Joseph Y. Halpern, *Rev. Symb. Logic* 13(3): 503–508, Sept 2020, doi:10.1017/S175502031800028X. Online 15 Oct 2018.
- **Set-up:**
  - Savage framework with finite S, O and A.
  - A probability Pr on S × A; only the conditionals Pr(·|a) are used.
  - Def. 2.1: a is ratifiable iff E_{Pr|a}(u_a) ≥ E_{Pr|a}(u_{a'}) for all a'. This is exactly M[a,a] ≥ M[a,a'] in your notation.
- **Assumptions:**
  - (3) No cost to randomising: (Σα_i a_i)(s) = Σα_i a_i(s), with u extended linearly by (2).
  - (4) Jeffrey-style mixing of conditionals: Pr(·| αa + (1−α)a') = α Pr(·|a) + (1−α) Pr(·|a').
- **Theorem 2.2:** "If (3) and (4) hold, then there is always a ratifiable act in [the convex hull of] A". The proof is via Kakutani on the best-response correspondence.
- **Counterexample showing (4) is necessary:** A red/blue-box predictor who puts the $1,000 in red whenever she predicts randomisation.
- **Relevance:** With mixed acts and linear belief-mixing, the causal matrix extends bilinearly. A ratifiable mixed act is then a Nash-type fixed point, so ratifiability is always satisfiable but generally not ex ante optimal.

### everittetal2015: VERIFIED (Crossref; Springer catalogue)
- **Citation:** Tom Everitt, Jan Leike and Marcus Hutter, in *Algorithmic Decision Theory (ADT 2015)*, ed. Toby Walsh. LNCS 9346 (LNAI subseries), Springer, pp. 205–221, doi:10.1007/978-3-319-23114-3_13.
- **Content (PARTIAL, not read in full):** The paper defines sequential (act-based vs policy-based) versions of EDT and CDT for agents in general environments, in the AIXI-style setting.
- **Relevance:** This is the action-level vs policy-level distinction in a sequential setting.

### macdermottetal2023: VERIFIED (arXiv)
- **Citation:** Matt MacDermott, Tom Everitt and Francesco Belardinelli, arXiv:2307.10987, 20 Jul 2023, v1 only. I found no journal reference or later venue.
- **Content (abstract):** Mechanised causal models characterise and distinguish EDT, CDT and FDT and give a taxonomy of them.

### cooperetal2024: VERIFIED (arXiv; Oesterheld's homepage lists it as a working paper)
- **This is the paper you meant.** Emery Cooper, Caspar Oesterheld and Vincent Conitzer, "Can CDT rationalise the ex ante optimal policy via modified anthropics?", arXiv:2411.04462. v1 7 Nov 2024; v2 20 Nov 2024. I found no venue.
- **Content (abstract):**
  - If the agent assigns credence to being in the predictor's simulation, CDT can one-box.
  - The paper generalises this to self-locating beliefs: simulation-based models and "Generalised Generalised Thirding" (GGT). It characterises the resulting CDT policies and proves that, under certain conditions, they include the ex ante optimal ones.
- **Not this paper:** The title you guessed, "Can de se choice be ex ante reasonable in games of imperfect recall? A complete analysis", is a *different* working paper by Oesterheld and Conitzer only, without Cooper. Its CMU version is dated 5 Jan 2024. It is included as `oesterheldconitzer2024dese`.
- **De se paper content:**
  - Piccione and Rubinstein (1997) show the ex ante optimal policy is "modified multiself consistent", that is, compatible with CDT plus generalised thirding.
  - The new result is that the ex ante optimal policy is compatible with EDT plus generalised double-halfing.
  - Generalised single-halfing escapes the Draper–Pust Dutch book, but other Dutch books apply to it.
  - The paper is unpublished as of Oct 2026, as far as I could find.

### oesterheld2019: VERIFIED (Crossref)
- **Citation:** Caspar Oesterheld, *Synthese* 198 (Suppl. 27): 6491–6504, Nov 2021. Online 25 Feb 2019. doi:10.1007/s11229-019-02148-2. Crossref gives the issue as "S27".
- **Dating:** Cite as 2021 (print) or 2019 (online first). The key `oesterheld2019` follows your naming but `date = {2021}`. Adjust if you prefer.
- **Content (abstract):** An approval-directed agent maximising an overseer's expected-utility score is governed by two decision theories: the agent's own, and the overseer's. The paper shows which one governs the agent's behaviour in which situations.

### wolpertbenford2013: VERIFIED (Crossref)
- **Citation:** David H. Wolpert and Gregory Benford, *Synthese* 190(9): 1637–1646, 2013. Online 17 Mar 2011. doi:10.1007/s11229-011-9899-3.
- **Earlier version:** arXiv:1003.1343, titled "What does Newcomb's paradox teach us?".
- **Content (abstract, PARTIAL):** The expected-utility and dominance arguments presuppose two different, mutually incompatible Bayes-net/game formalisations of how the choice and the prediction are related. The predictor's accuracy is irrelevant to the resolution.

### briggs2010: VERIFIED (published PDF read; Crossref)
- **Citation:** Rachael Briggs, *Phil. Review* 119(1): 1–30, 2010, doi:10.1215/00318108-2009-024.
- **Byline:** The byline as printed is "**Rachael Briggs**". Later publications appear as R. A. Briggs. Use "Briggs, Rachael" in the .bib and the year disambiguates.
- **Location of §6:** §6 "No Adequate Decision Theory" runs pp. 21–26 (§7 begins on p. 26). P and S are stated on **p. 22**, the impossibility proof is on **pp. 23–24**, and fn. 14 (p. 24) links it to Sen's Liberal Paradox.
- **Set-up:** V^B(A) is the value that the post-B self S_B assigns to A, so V^B(A) = M[B,A]. E is the overall evaluation.
- **P, strong Pareto:** "For any actions A1 and A2 in A, if for all B ∈ A, V^B(A1) ≥ V^B(A2) and there is some B ∈ A such that V^B(A1) > V^B(A2), then E(A1) > E(A2)."
- **S, self-sovereignty:** "For any decision situations D = ⟨A, K, C⟩ and D′ = ⟨A, K′, C′⟩ involving the same set of actions A, if A contains a pair of actions A1 and A2 such that V^{A1} = V′^{A1} and V^{A2} = V′^{A2}, then ... E(A1) > E(A2) iff E′(A1) > E′(A2)." This is a *cross-problem* axiom: the ranking of A1 vs A2 depends only on the rows M[A1,·] and M[A2,·].
- **Result:** "it is impossible for any completely general decision theory to satisfy both P and S." The proof uses ≥ 3 actions. Briggs notes this is "no accident":
  - In two-option problems, Wedgwood's benchmark theory (BT) satisfies both.
  - EDT and BT satisfy S but violate P.
  - CDT satisfies P but violates S, even with two options.
  - Both principles are ordinal.

### podgorski2022: VERIFIED (Crossref; author preprint read)
- **Citation:** Abelard Podgorski, *Noûs* 56(1): 176–203, March 2022. Online 31 Oct 2020. doi:10.1111/nous.12353.
- **Self-Esteem Theorem (section "The Self-Esteem Theorem"; proof in the Appendix; page numbers here are from the preprint, not the journal):**
  - Take 3-option decision-relative value matrices V_Y(Z), with V_Y(Z) = M[Y,Z]. An overall evaluation O(X) is a function of all the V_Y(Z).
  - P(X,Y) ∈ {1, 0, −1} is the sign of O(X) − O(Y).
  - "IIA: P(X, Y) is a function P′ of V_X(X), V_Y(Y), V_X(Y), and V_Y(X)."
  - "The Self-Esteem Theorem: Given IIA, P(X, Y) is a function of X and Y's self-esteem – that is, V_X(X) and V_Y(Y) alone."
  - Proof: a matrix with A and C sharing p's forces P(A,C) = 0, hence O(A) = O(C), hence P(A,B) = P(C,B). The proof implicitly needs a rich domain of matrices and a single P′ across problems.
- **Consequence Podgorski draws:** Since self-esteem equals evidential expected utility, the only overall-value view respecting IIA is EDT.
- **Correction to your description:** The theorem is about **overall-value (scalar O) rules plus IIA**, not about tournament rules. Podgorski's own tournament decision theory escapes it because pairwise "defeat" need not come from any single overall evaluation, so the IIA question does not arise in the same form.
- **Footnote 16:** Restates Briggs's P and S and calls S "a kind of self-sovereignty principle slightly weaker than the IIA we use above."

### gallow2026: VERIFIED (Crossref)
- **Citation:** J. Dmitri Gallow, "Comparativism About Instrumental Value", *Philosophy and Phenomenological Research* 113(2): 346–363, Sept 2026. Online 2 Jul 2026. doi:10.1111/phpr.70139.
- **Content (abstract):**
  - Gallow rejects both nihilism (associated with EDT) and absolutism (associated with CDT) about instrumental value.
  - Comparativism: there are facts about how much more or less helpful a choice was than an alternative, but no absolute amount.
  - This yields new theories of instrumental rationality that avoid problems facing CDT.
- **Relevance:** This is the philosophical motivation for rules defined by pairwise comparisons, M-differences, rather than scalar values.

---

## Dynamic choice / ex ante vs ex post

### kuhn1953: VERIFIED for the chapter (Crossref); editors PARTIAL
- **Citation:** Harold W. Kuhn, "Extensive Games and the Problem of Information", in *Contributions to the Theory of Games, Vol. II* (Annals of Mathematics Studies 28), Princeton UP, 1953, pp. 193–216, doi:10.1515/9781400881970-012.
- **Editors:** The editors (H. W. Kuhn and A. W. Tucker) come from standard knowledge. The Crossref record I checked does not list them.
- **Relevance:** Introduces perfect recall. Kuhn's theorem says mixed and behavioural strategies are equivalent under perfect recall. Imperfect recall is exactly where they come apart.

### hammond1988: VERIFIED (Crossref)
- **Citation:** Peter J. Hammond, *Theory and Decision* 25(1): 25–78, 1988, doi:10.1007/BF00129168.
- **Content (from knowledge, not re-read):** Consequentialist choice in decision trees, together with dynamic consistency, implies an ordering plus independence, and hence expected utility.

### mcclennen1990: VERIFIED (publisher records)
- **Citation:** Edward F. McClennen, *Rationality and Dynamic Choice: Foundational Explorations*, Cambridge UP, 1990. ISBN 978-0-521-36047-0 (hardback); the 2008 paperback is 978-0-521-06391-3.
- **Content (from knowledge):** Resolute choice: carrying out the ex ante plan even when it is not ex post optimal.

### piccionerubinstein1997: VERIFIED (Crossref)
- **Citation:** Michele Piccione and Ariel Rubinstein, *GEB* 20(1): 3–24, 1997, doi:10.1006/game.1997.0536.
- **Content (PARTIAL: confirmed via Oesterheld–Conitzer's summary and secondary sources, not re-read):**
  - Introduces the absent-minded driver: exit 1 pays 0, exit 2 pays 4, continuing past both pays 1. The planning-optimal p(continue) is 2/3.
  - Contrasts *planning-stage* with *action-stage* optimality. With updated beliefs at the intersection, the planning-optimal plan can look suboptimal.
  - Shows the planning-optimal strategy is "modified multiselves consistent" (CDT plus generalised thirding).
- **Relevance:** This is the direct analogue of ex ante optimal vs ratifiable.

### aumannetal1997: VERIFIED (Crossref)
- **Citation:** Robert J. Aumann, Sergiu Hart and Motty Perry, *GEB* 20(1): 102–116, 1997, doi:10.1006/game.1997.0577.
- **Content (PARTIAL, secondary sources):**
  - Argues there is no paradox. Defines *action-optimality*: at an intersection, optimise the current action, holding behaviour at other intersections fixed and using consistent beliefs.
  - Shows the planning-optimal strategy is action-optimal. The converse need not hold.
- **Attribution fix:** In this literature, "modified multiself consistency" is Piccione–Rubinstein's term. AHP's term is "action-optimal". The reconciliation points the same way: the ex ante optimum is a fixed point of the local, causal-style criterion, but not uniquely.

### gauthier1986: VERIFIED (library catalogues)
- **Citation:** David Gauthier, *Morals by Agreement*, Oxford: Clarendon Press, 1986.
- **ISBN:** Not included because catalogues list several ISBNs (019824746X; pbk 0198249926).
- **Content:** Constrained maximisation: dispositions that are rational to adopt ex ante bind later choice.

### gauthier1994: VERIFIED (Crossref)
- **Citation:** David Gauthier, "Assure and Threaten", *Ethics* 104(4): 690–721, July 1994, doi:10.1086/293651.
- **Content:** Rationality of following through on assurances and threats that were optimal to make ex ante.

### arntzeniusetal2004: VERIFIED (Crossref; PhilSci Archive)
- **Citation:** Frank Arntzenius, Adam Elga and John Hawthorne, *Mind* 113(450): 251–283, 2004, doi:10.1093/mind/113.450.251.
- **Authors:** Crossref lists only Arntzenius. The three authors are confirmed by the PhilSci-Archive preprint and the Princeton record.
- **Content:** Satan's apple and infinite-decision cases. Each choice is individually rational, yet the sequence is disastrous. Binding (ex ante commitment) rescues the agent, and Dutch books have no force in infinite cases.

---

## Items that could not be fully confirmed
- **Kuhn 1953 editors:** Standard knowledge, not shown in the Crossref record I checked.
- **Content summaries for Hammond, McClennen, Piccione–Rubinstein, AHP, Everitt et al.:** From abstracts, secondary sources and knowledge, not re-read in full. All bibliographic data for them is verified.
- **Podgorski page numbers:** I read the author's preprint, so I don't have journal page numbers for the Self-Esteem Theorem.
- **Soares & Fallenstein AGI-2015 proceedings version:** Not verified, so the arXiv version is cited.
- **No item needed `note = {UNVERIFIED: ...}`.** Every BibTeX field I included was confirmed against a primary record, except the Kuhn editors flagged above.
