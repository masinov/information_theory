# Cluster E: verification notes

Checked 2026-10-20. The main source is the Crossref API (`api.crossref.org/works/<doi>`), which returned authors, title, venue, volume, issue, pages and date for every DOI below. Two primary texts were read directly: Williamson's 2015 Amsterdam Colloquium paper (open access PDF) and a scan of Lewis 1976. The open-access full text of Berto et al. 2018 (Europe PMC, PMC6435010) was also read. Statuses:

- **VERIFIED**: every bibliographic field in the .bib entry was confirmed by at least one authoritative source.
- **PARTIAL**: some fields or claims could not be confirmed. Each case is explained.
- **UNVERIFIED**: no item in this cluster.

## Conditionals

**lewis1973counterfactuals**: VERIFIED (bibliographic). Oxford: Blackwell and Cambridge, MA: Harvard University Press, 1973, x+150 pp. The Harvard ISBN is 0-674-17541-7.
- Sources: library catalogue record (Harvard imprint); PhilArchive record (Blackwell); Lewis's own citations give "Blackwell and Harvard University Press".
- Content: the standard source of vacuism. If the antecedent is impossible, there are no antecedent-worlds, so the counterfactual is vacuously true. Berto et al. 2018 (§2) and the Brogaard & Salerno abstract both describe this as the orthodox Lewis view.
- Pages: not checked in the book. Berto et al. 2018 (fn. 18) cite Lewis 1973 p. 25 for the "largest prime" counterpossibles. The same paper cites pp. 19–20 for the Limit Assumption and pp. 21–24 for modal operators defined from counterfactuals. Cite these pages only as "cf.".

**lewis1976**: VERIFIED. Philosophical Review 85(3):297–315, July 1976, DOI 10.2307/2184045.
- Sources: Crossref gives the first page only. The end page is confirmed by a 19-page scan of the article, which also locates the results below by page.
- Content, first result (p. 300): "any language having a universal probability conditional is a trivial language". A trivial language cannot provide three possible but pairwise incompatible sentences.
- Content, second result (p. 302): if a class of probability functions is closed under conditionalizing, there is no probability conditional for that class unless it consists entirely of trivial (at most four-valued) functions.
- Imaging, and the Stalnaker conditional as a probability-revision conditional under imaging, are discussed from p. 310 onward.

**stalnaker1968**: PARTIAL. In N. Rescher (ed.), *Studies in Logical Theory*, Oxford: Blackwell, 1968, pp. 98–112.
- Sources: Stalnaker's MIT publication list (Oxford, 1968, 98–112); the reference list of Berto et al. 2018 (Blackwell, pp. 98–112); Wikipedia.
- Not confirmed: the series label "American Philosophical Quarterly Monograph Series, No. 2". No online source checked here states it. One source (Wikipedia) gives the publisher as OUP, while others give Blackwell; the .bib entry uses Blackwell. Drop the `series`/`number` fields if in doubt.
- Content: the selection-function (closest-world) semantics for conditionals. It is useful only as context for the Stalnaker–Lewis orthodoxy.

## Counterpossibles

**nolan1997**: VERIFIED (bibliographic); PARTIAL for the SIC page and Nolan's stance.
- Bibliographic: Notre Dame Journal of Formal Logic 38(4):535–572, Oct. 1997, DOI 10.1305/ndjfl/1039540769.
- Title correction: Crossref and Project Euclid give the title exactly as "Impossible Worlds: A Modest Approach", with no further subtitle.
- Content (from the abstract): Nolan defends impossible worlds as a modest commitment. He treats reasoning about the impossible as reasoning with counterpossible conditionals, gives a semantics for it, and uses non-vacuous counterpossibles (the Hobbes squaring-the-circle pair).
- SIC: the "Strangeness of Impossibility Condition" says any possible world is closer to (more similar to) a possible world than any impossible world is. Secondary sources (Melchior 2021, Phil. Studies, DOI 10.1007/s11098-020-01453-8) cite it at p. 550. The Nolan full text was not consulted.
- CAUTION on the stance: Nolan names the condition, but sources disagree on whether he endorses it. Berto et al. 2018 fn. 9 say SIC "is rejected in Nolan [1997], where it receives this name". Melchior says Nolan offers it as a conjecture without endorsing it and discusses possible counterexamples. Do not write that Nolan "adopts" SIC without checking pp. 550–551.

**williamson2015**: VERIFIED. "Counterpossibles", in T. Brochhagen, F. Roelofsen and N. Theiler (eds.), *Proceedings of the 20th Amsterdam Colloquium*, Amsterdam: ILLC, University of Amsterdam, 2015, pp. 30–39. DOI 10.53437/2shbpp13.
- Sources: openjournals.nl PAC record (title, pages, 2015-12-01, DOI); UvA DARE record (editors, ILLC, 487 pp.); the PDF itself.
- The argument (read directly, §1 "What is at Stake"), pp. 30–31:
  - (2) |A □→ C| = f(|A|, |C|), refined to (3) |A □→ C| = f(|A|, |A| ∩ |C|), so (4) if |A| = {} then |A □→ C| = f({}, {}). This is on p. 30.
  - With reflexivity (5) |A □→ A| = W, this gives f({}, {}) = W, hence (6) every counterpossible is a necessary truth. This step is on p. 31.
- Williamson also gives object-language versions on p. 31: from (7)–(8), and from "strict implication implies counterfactual implication", (10)–(12).
- The Hobbes/sick-children examples (13)–(14), from Nolan, are on p. 31. Principles (17)–(18) are on p. 32. Principle (19), that opposite counterfactuals imply an impossible antecedent, is on p. 33.

**williamson2018**: VERIFIED (Crossref). Topoi 37(3):357–368, DOI 10.1007/s11245-016-9424-x; online 2016-08-29, issue Sept. 2018.
- Content: the journal version of the vacuist defence. It argues that apparent false counterpossibles reflect a fallible heuristic.
- It appears in a 2018 Topoi issue whose introduction (Aloni, Topoi 37:355–356) discusses Williamson's contribution. Its relation to the 2015 proceedings paper (expanded version or not) was not checked in detail. Cite the 2015 paper for the pp. 30–31 argument.

**bertoetal2018**: VERIFIED (Crossref). J. Philosophical Logic 47(4):693–713, DOI 10.1007/s10992-017-9446-x; online 2017-08-16, issue Aug. 2018. Open access.
- Content: defends nonvacuism against Williamson with an impossible-worlds semantics (§2, drawing on Priest).
- §§3–4 rebut Williamson's theoretical arguments and his "fallible heuristic" debunking of nonvacuist intuitions. §5 argues his modal epistemology is compatible with nonvacuism.

**brogaardsalerno2013**: VERIFIED (Crossref). Synthese 190(4):639–660, DOI 10.1007/s11229-012-0196-6; online 2012-12-21, issue March 2013.
- Content (abstract): rejects the Lewisian vacuous-truth view. Keeps a Lewis-style comparative-similarity semantics and classical logic, but adds impossible worlds with a similarity ordering, so counterpossibles can be non-vacuously true or false.
- Williamson 2015 (p. 33) criticises their characterisation of orthodoxy as "trivial" (vacuously true and semantically uninformative).

*Kment (2014, Modality and Explanatory Reasoning, OUP)*: skipped as instructed. It is cited by Williamson 2015 and Berto et al. 2018 as a further nonvacuist.

## Causal models

**pearl2009**: VERIFIED. *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge: Cambridge University Press, 2009. ISBN 978-0-521-89560-6 (hb). DOI 10.1017/CBO9780511803161.
- Sources: Crossref and the CUP Core page.
- Chapters, from the CUP table of contents:
  - ch. 3 "Causal Diagrams and the Identification of Causal Effects", pp. 65–106. This is where interventions and the do(·) operator enter.
  - ch. 7 "The Logic of Structure-Based Counterfactuals", pp. 201–258.
- 1st edition 2000: not re-checked.

**spirtesetal2000**: PARTIAL. *Causation, Prediction, and Search*, 2nd ed., MIT Press. DOI 10.7551/mitpress/1754.001.0001.
- Crossref confirms the authors, title, MIT Press and edition 2, but its date is 2001-01-29 (the MIT Press Direct record).
- The print year 2000 and Cambridge, MA are standard but not confirmed online here.
- Content: causal discovery from conditional independences (PC/FCI algorithms); the manipulation theorem for interventions.

## Superrationality

**hofstadter1983**: VERIFIED (venue); PARTIAL (title string).
- Crossref: Scientific American 248(6):14–28, June 1983, DOI 10.1038/scientificamerican0683-14. Crossref's title is only "Metamagical Themas", the column name.
- The column title "Dilemmas for Superrational Thinkers, Leading Up to a Luring Lottery" comes from Wikipedia and secondary sources. The May 1983 column (248(5):16–26, DOI 10.1038/scientificamerican0583-16) is the earlier Prisoner's Dilemma column; do not confuse the two.
- Reprinted as ch. 30 of *Metamagical Themas* (Basic Books, 1985). Reprint pages are reported inconsistently (737–755 vs. 737–780), so they are not in the entry.
- Content: introduces "superrationality". Symmetric reasoners in a one-shot Prisoner's Dilemma should recognise that they will reach the same choice, and so cooperate.

## Sources

- Crossref API: works/10.2307/2184045, 10.1305/ndjfl/1039540769, 10.1007/s11245-016-9424-x, 10.1007/s10992-017-9446-x, 10.1007/s11229-012-0196-6, 10.1017/CBO9780511803161, 10.7551/mitpress/1754.001.0001, 10.1038/scientificamerican0683-14.
- https://platform.openjournals.nl/PAC/article/view/22236 (Williamson 2015, record and PDF).
- https://dare.uva.nl/id/61a67723-fbdf-44b5-9595-71f6869bf81a (20th Amsterdam Colloquium proceedings, editors).
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6435010 (Berto et al. 2018, full text).
- https://www.andrewmbailey.com/dkl/Probabilities_of_Conditionals.pdf (scan of Lewis 1976).
- https://www.cambridge.org/core/books/causality/B0046844FAE10CBF274D4ACBDAEB5F5B (Pearl 2009).
- https://link.springer.com/article/10.1007/s11098-020-01453-8 (Melchior, SIC at Nolan p. 550; seen via search snippets only).
- https://philosophy.mit.edu/stalnaker/pub (Stalnaker 1968 pages).
- https://en.wikipedia.org/wiki/Metamagical_Themas (Hofstadter column title).
