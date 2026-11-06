# Cluster F: verification notes (round 6, §10 and §§2–5 citations)

Checked 2026-10-21. Sources used:

- the Crossref API (`api.crossref.org/works/<doi>`) for every DOI;
- arXiv abstract pages and PDFs (arXiv versions noted per entry);
- the LessWrong GraphQL API (`lesswrong.com/graphql`) for post dates and authors;
- PMLR pages, Marcus Hutter's official bibliography (`hutter1.net/official/bib.htm`), mlanthology.org and the ANU repository for the UAI paper;
- the PDFs themselves: FDT v1 and v2 (arXiv), the Leike–Hutter author PDF and arXiv:1510.05572, PMLR v40 Leike15.pdf, PJM 40(3) (msp.org), Hirschfeldt's preprint `rm.pdf`, arXiv:1002.2800v2, arXiv:1506.01930v1, the Acta Informatica accepted manuscript (UCL Discovery 10089603), and Odifreddi's *Classical Recursion Theory* vol. I (author-hosted CRT1.pdf).

The AMS full text of Jockusch–Soare (Trans. AMS 173) could not be retrieved, because the AMS site blocks automated access. Its theorem numbers come from secondary sources and are marked as such.

Statuses:

- **CONFIRMED**: the claim as stated in output_round_6.md is correct.
- **CORRECTED**: the claim is substantially right, but a detail needs fixing.
- **UNVERIFIABLE**: could not be checked here.

The entries are in `latex/refs_F.bib`, which uses the same non-printing `verification` field as refs.bib.

---

## 1. Yudkowsky & Soares, FDT, arXiv:1710.05060 (existing key `yudkowskysoares2017`)

**CONFIRMED.** §9, "The Global Perspective", printed p. 29, footnote 15. The footnote and its page are the same in v1 (13 Oct 2017) and v2 (22 May 2018). It is attached to the sentence "...if a satisfactory notion of 'fairness' can be formalized."

> "There are some immediate technical obstacles to precisely articulating this notion of fairness. Imagine I have a copy of Fiona, and I punish anyone who takes the same action as the copy. Fiona will always lose at this game, whereas Carl and Eve might win. Intuitively, this problem is unfair to Fiona, and we should compare her performance to Carl's not on the 'act differently from Fiona' game, but on the analogous 'act differently from Carl' game. It remains unclear how to transform a problem that's unfair to one decision theory into an analogous one that is unfair to a different one (if an analog exists) in a reasonably principled and general way."

Nuance: the footnote speaks informally of "a copy of Fiona". It does not say "fixed program". The output's paraphrase ("matching a fixed copy") is fair. The output's further claim ("acknowledges the problem of specifying corresponding comparison environments") matches the last sentence.

## 2. Leike & Hutter, "On the Computability of AIXI", UAI 2015 (new key `leikehutter2015aixi`)

**CONFIRMED, with one bibliographic caveat and one sharpening.**

- **Bibliographic caveat:** pp. 464–473 is the original pagination in *Proc. 31st UAI*, AUAI Press, Amsterdam, edited by Meila and Heskes (from Hutter's official bib and mlanthology; the ANU repository confirms AUAI Press). PMLR reissued the paper on 4 Oct 2026 as **PMLR R13:239–248**. Readers may meet either pagination. The entry uses the AUAI one and records the PMLR one. arXiv:1510.05572 (19 Oct 2015, comment "UAI 2015") has the same theorem numbering.
- **Theorem 8** (Complexity of Optimal Policies): "if V*_ν is Δ⁰_n-computable, then there is an optimal policy π*_ν … that is Δ⁰_{n+1}." This is a one-level increase for *any* n. The output's phrase "from computable values" is narrower than the theorem; it is the case n = 1 only.
- **Theorem 11** (Complexity of ε-Optimal Policies): the same hypothesis gives an ε-optimal policy that stays in Δ⁰_n. Confirmed.
- **Corollary 13** (Complexity of AIMU): if μ is a *measure* and the discount γ is *computable*, then AIMU (LT and DC) is limit computable (Δ⁰_2), and ε-optimal AIMU is computable (Δ⁰_1). Confirmed. Both hypotheses should be stated.
- **Theorem 14** (No AIXI is computable): "AIXI^LT and AIXI^DC are not computable for any universal Turing machine U." Confirmed. Note for §10: the proof builds an adversarial deterministic environment that simulates the putative computable optimal policy. It gives reward 0 while the agent follows that policy and 1 once it deviates. This is a fixed-copy diagonal of exactly the E2 type. The output says only that the results are "closely related"; the proof of Theorem 14 is in fact a direct predecessor of the E2 diagonal and is worth citing as such.

## 3. Leike & Hutter, "Bad Universal Priors and Notions of Optimality", COLT 2015 (existing key `leikehutter2015`)

**CONFIRMED.** The existing refs.bib key `leikehutter2015` is *this* paper (PMLR 40:1244–1259). No new key is needed. Cite `leikehutter2015`.

- §5 "Pareto Optimality". **Theorem 18** (Pareto Optimality is Trivial): "Every policy is Pareto optimal in any M ⊇ M^CCS_LSC". M^CCS_LSC is the class of lower semicomputable chronological conditional semimeasures. The theorem is on internal p. 10 of the PDF, which is **PMLR p. 1253**.
- The paper itself loosely calls M^CCS_LSC "the class of all computable environments" (abstract, §6). The output's precise wording is the better one.
- The output's remark about the proof is confirmed (p. 10 / PMLR p. 1253): "The environment µ is computable, even if the policy π is not: for a fixed history h and action output π(h), there exists a program computing µ." The paper adds that µ "is actually just a finite-state POMDP".

## 4. drnickbone, "Problematic Problems for TDT", LessWrong (new key `drnickbone2012`)

**CONFIRMED.** LessWrong API: postedAt 2012-05-29T15:41:37Z, user `drnickbone`, URL `/posts/3GyQXTy2WhYcaBgS2/problematic-problems-for-tdt`.

- In Problem 1, Omega fills box B according to "a simulation of this problem as presented to an agent running TDT". This is a fixed-target simulation.
- The post explicitly argues that such problems are "fair" (the reward depends only on the agent's actual choices). It contrasts them with an openly unfair "Discrimination" problem.
- The author's legal name was not established, so the entry uses the pseudonym.

## 5. Jockusch & Soare 1972

### 5a. "Π⁰₁ classes and degrees of theories", Trans. AMS 173:33–56 (new key `jockuschsoare1972trans`)

**CONFIRMED (metadata); theorem numbers PARTIAL.**

- DOI 10.1090/S0002-9947-1972-0316227-0 (AMS); the JSTOR DOI 10.2307/1996261 is the same article. Vol. 173, 1972, with no issue number (Crossref gives Nov. 1972).
- Full text was not read.
- Theorem locations from secondary sources:
  - **Thm 2.1: low basis theorem.** Cited as "[4, Theorem 2.1]" in the companion PJM paper, p. 612 ("has a member of degree a such that a′ = 0′"), and as "[39, Theorem 2.1]" by Brattka–Hendtlass–Kreuzer, arXiv:1501.00433.
  - **Thm 2.4: hyperimmune-free basis theorem** (arXiv:1501.00433; Patey et al., arXiv:1903.04273).
  - **Thm 2.5: cone avoidance**, in the form "WKL admits avoidance of ω cones" (arXiv:1903.04273). One web summary also mentioned a Corollary 2.11 in this connection; that is not confirmed, so cite Thm 2.5.
  - **Prop. 6.1:** a consistent extension of PA computes a complete one. **Prop. 6.5:** every recursively bounded Π⁰₁ class is degree-isomorphic to the class of completions of an axiomatizable theory. Both are cited as such in the PJM paper.
  - **PA degree iff computes a separating set for an effectively inseparable pair**, and **iff computes {0,1}-valued total extensions of every partial computable {0,1}-valued function**: Hirschfeldt attributes both to this paper (his Thms 3.20, 3.21). Their internal theorem numbers were **not found**.

### 5b. "Degrees of members of Π⁰₁ classes", Pacific J. Math. 40(3):605–616 (new key `jockuschsoare1972pacific`)

**CONFIRMED.** DOI 10.2140/pjm.1972.40.605, issue dated 1 March 1972. It appeared *before* the Trans. AMS paper, which it cites as "to appear".

pp. 612–613 contain:

- **Theorem 4:** there is a nonempty recursively bounded Π⁰₁ class such that every r.e. degree above the degree of any member is 0′.
- **Lemma 4.1:** the Martin-style effectively-immune lemma.
- **Corollary 4.2.**
- **Corollary 4.3:** no consistent extension (or nonstandard model) of PA lies below an incomplete r.e. degree.
- **Corollary 4.4** (Scott–Tennenbaum): there is a complete extension of PA of degree 0′.

The paper cites Scott [12, p. 118] for the fact that completions of PA compute members of every nonempty recursively bounded Π⁰₁ class. The output's "pp. 612–613 discuss the relevant PA-completion and effectively closed-class results" is accurate.

## 6. Hirschfeldt, *Slicing the Truth* (new key `hirschfeldt2014`)

**CORRECTED (theorem roles and year).**

- **Publication details.** World Scientific, Lecture Notes Series, Institute for Mathematical Sciences, NUS, **vol. 28**. DOI 10.1142/9208, ISBN 978-981-4612-61-6.
- **Year.** Crossref gives print Sept. 2014; dblp and catalogues give 2014. Hirst's BSL review (21(3), 2015, DOI 10.1017/bsl.2015.18) cites "2015, xiv+214 pp." **Use 2014**, and optionally note the 2015 copyright/review year, as the output does.
- **Subtitle.** The published subtitle is "On the Computable and Reverse Mathematics of Combinatorial Principles". The preprint's subtitle is "On the Computability Theoretic and Reverse Mathematical Analysis of Combinatorial Principles". The output uses the published form, which is correct.

Theorem numbers in the author preprint, §3.1 "Π⁰₁ classes, basis theorems, and PA degrees" (from p. 29). The numbering of the printed book was **not** checked.

| Preprint no. | Statement | Attribution |
|---|---|---|
| Thm 3.10 | **low basis theorem** | Jockusch–Soare [Trans.] |
| Thm 3.13 | hyperimmune-free basis theorem | Jockusch–Soare |
| Thm 3.14 | **cone-avoidance basis theorem** (if X is noncomputable, every nonempty Π⁰₁ class has a member not computing X) | Jockusch–Soare |
| Def. 3.15 | PA degree := the computable-from-it sets form a basis for Π⁰₁ classes | |
| Thm 3.16 | PA iff degree of a complete extension of PA ("built on work of Scott") | Solovay, see Odifreddi |
| Thm 3.17 | there is a low PA degree | Jockusch–Soare |
| Thm 3.18 | a c.e. set of PA degree is complete | Jockusch–Soare [PJM] |
| Def. 3.19 | effectively inseparable; example A = {e : Φ_e(e)↓ = 0}, B = {e : Φ_e(e)↓ = 1} | |
| Thm 3.20 | PA iff computes a separating set for an effectively inseparable pair | Jockusch–Soare |
| Thm 3.21 | PA iff, for each partial computable {0,1}-valued ψ, computes a total {0,1}-valued extension | Jockusch–Soare |

- **Directly after Thm 3.21 (p. 33):** "Thus a degree is PA iff it computes a 0,1-valued DNC function." The output's §4.1 claim ("stated … immediately after Theorem 3.21") is **confirmed**.
- **Correction to §10:** the output lists "Theorems 3.14, 3.17, and 3.21". Thm 3.14 is cone avoidance, *not* the low basis theorem; the low basis theorem is **3.10**. If the text uses Hirschfeldt for the low basis theorem, cite 3.10. Also cite 3.20 for the separating-set form.
- The recursion theorem is Hirschfeldt's Thm 2.1 (Kleene).

## 7. Brattka, de Brecht, Pauly 2012 (new key `brattkaetal2012`)

**CONFIRMED.**

- Crossref: APAL 163(8):986–1008, Aug. 2012, DOI 10.1016/j.apal.2011.12.020. arXiv:1002.2800 (v1 14 Feb 2010, v2 28 Sep 2010).
- In arXiv v2:
  - **Example 3.2**: C_{0} ≡_W id, C_{0,1} ≡_W LLPO, C_{0,…,n} ≡_W MLPO_{n+1} (finite closed choice).
  - **Example 3.10**: among other things, the parallelization of C_{0,1} is ≡_W C_{2^ℕ} (countable parallelization).
  - **Theorem 8.3** is the Uniform Low Basis Theorem ("C_{2^ℕ} is low computable").
- The APAL numbering was not compared with arXiv v2.

## 8. Kaminski & Katoen, MFCS 2015 (new key `kaminskikatoen2015`), and the Acta Informatica version (new key `kaminskietal2019`)

**CONFIRMED, with the journal numbering added.**

- **MFCS 2015:** *MFCS 2015, Proceedings, Part I*, LNCS **9234**, pp. **307–318**, Springer, DOI 10.1007/978-3-662-48057-1_24.
  - ISBN 978-3-662-48057-1 is Part I; Part II is LNCS 9235, 978-3-662-48054-0.
  - Editors: Italiano, Pighizzini, Sannella.
  - arXiv:1506.01930 v1, 5 Jun 2015, comment "MFCS 2015".
- **In arXiv v1, §6** "The Hardness of Deciding Probabilistic Termination":
  - **Theorem 6**: AST is Π⁰₂-complete;
  - **Theorem 7**: UAST (universal AST) is Π⁰₂-complete;
  - also Thm 8: PAST is Σ⁰₂-complete; Thm 10: UPAST is Π⁰₃-complete.
  - The output's "§6, Theorems 6–7" is **confirmed** for arXiv. The LNCS print was not checked.
- **Journal version:** Kaminski, Katoen, Matheja, "On the hardness of analyzing probabilistic programs", *Acta Informatica* **56(3):255–285**, 2019, DOI 10.1007/s00236-018-0321-1.
  - Online 15 May 2018; issue April 2019; received 15 Sep 2016.
  - In the accepted manuscript, **§4**: **Theorem 8** (AST Π⁰₂-complete), **Theorem 9** (UAST Π⁰₂-complete), Thm 10 (PAST Σ⁰₂-complete), Thm 11 (UPAST Π⁰₃-complete).
  - The typeset numbering was not checked.

## 9. Original and textbook sources

### (a) PA degree ⇔ DNC₂ / separating set of K₀, K₁

- **Scott 1962** (new key `scott1962`): "Algebras of sets binumerable in complete extensions of arithmetic".
  - *Recursive Function Theory*, Proc. Sympos. Pure Math. **5**, AMS, Providence, 1962, **pp. 117–121**, DOI 10.1090/pspum/005/0141595 (Crossref).
  - The editor (J. C. E. Dekker) is from memory.
  - Content: the sets representable in a completion of PA form a Scott set. Equivalently (Odifreddi Thm V.5.35, "Scott Basis Theorem", p. 511), the sets recursive in any consistent extension of PA form a basis for Π⁰₁ classes. This is the "PA ⇒ basis" half.
- **Solovay**: unpublished. Standard textbook source: **Odifreddi 1989, Thm V.5.36, pp. 511–513** (degree of a consistent extension of PA ⇔ degree of a complete extension ⇔ D(≤a) is a basis for Π⁰₁ classes). Hirschfeldt Thm 3.16 cites it in the same way.
- **The DNC₂ / separating-set / {0,1}-extension forms**: Jockusch–Soare 1972 (Trans. AMS), as attributed by Hirschfeldt Thms 3.20–3.21. The internal theorem number in J–S was **not** found.
  - Recommended citation: "Scott 1962; Solovay (see Odifreddi 1989, Thm V.5.36); Jockusch and Soare 1972 (Trans. AMS); see Hirschfeldt 2014, Thms 3.16, 3.20, 3.21 and the remark after 3.21."
  - The extension from 2 to n values (DNC_n) is Jockusch 1989, "Degrees of functions with no fixed points", Thm 5 (per arXiv:1501.00433). That is only needed if non-binary DNC is discussed.

### (b) Recursive inseparability of K₀ = {x : φ_x(x) = 0} and K₁ = {x : φ_x(x) = 1}

- **Odifreddi 1989** (new key `odifreddi1989`), **Theorem II.2.5, pp. 148–149**: "There are two disjoint, recursively inseparable r.e. sets". The first proof uses exactly K₀ and K₁. The theorem is credited to Rosser 1936, Kleene 1950, Novikov and Trakhtenbrot 1953.
- Hirschfeldt Def. 3.19 gives the same pair as *effectively* inseparable.
- **Rogers 1967** (key `rogers1967`, McGraw-Hill, 482 pp.; MIT Press reprint 1987) states this too, but its theorem number was **not** checked. Use Odifreddi for a located statement.

### (c) The relativized recursion theorem

- No textbook statement explicitly numbered as the *relativized* recursion theorem was verified.
- Best located option: **Odifreddi 1989, Thm II.2.13** (Second Recursion Theorem, Kleene 1938), p. 156, together with the general remark on relativization on **p. 177**. That remark says results are used "in relativized form when needed" but warns that relativization "requires a proof, even if only a check that everything relativizes in the original proof".
- Recommended wording: "the recursion theorem relativizes, with the same proof (Odifreddi 1989, Thm II.2.13 and p. 177)".
- Soare 1987 was **not** checked (UNVERIFIABLE here), so no `soare1987` entry was added.

## 10. Fallenstein, "Evil" decision problems (existing key `fallenstein2014evil`)

**Nothing contradicts mid-November 2014.**

- The LessWrong/AF API gives postedAt 2015-01-10T01:04:28Z (user Benja_Fallenstein, display name Benya_Fallenstein). This is the AF import date, as already recorded.
- The section headings named in the output are confirmed: Background, Definitions, Fixed points, Extensional (= "fair") decision problems, Evil problems.
- **Correction to §10:** "Benya Fallenstein (2015) … displayed date 10 January 2015" should cite the post as **2014** (mid-Nov., IAFF item 47), via `fallenstein2014evil`.
