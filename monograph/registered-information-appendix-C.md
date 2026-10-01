# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Appendix C: Controlled Vocabulary

The monograph's named objects, one line each, with the defining location. Terms are grouped by the layer that introduces them; the six **tracked coordinates** are marked ◆.

| term | defined | one-line meaning |
|---|---|---|
| contrast domain $D$ | §2, Def 4.1 | the space of alternatives relative to which information is assessed |
| view; kernel $\ker(v)$ | Def 4.2 | a presentation-producing map on $D$; the partition of candidates it cannot separate |
| registration; canonical registration | Def 4.6 | the record actually kept of a view's output; canonical = lossless |
| registered content $\sigma(S)$ | Def 5.2 | $\bigvee_{v \in S} \ker(v)$: the distinctions the views jointly draw |
| answerability | Prop 5.6 | a question is answerable iff its kernel factors below the content |
| achievable quotients $\mathrm{Ach}(V)$ | Thm 6.2(3) | the contents realizable by view sets; the algebra's label lattice |
| piece; combination; focusing | §3.4, Prop 6.11 | labeled saturated set $(E, \pi)$; intersection-with-label-join; saturation-with-relabel |
| admissibility structure $K$; ceiling $\gamma_K$ | Def 14.3 | the decoder's constraint: admissible readings and their content cap |
| separable vs joint content | Def 15.3 | what per-view admissible reading recovers vs joint admissible reading |
| registration anomaly $\Delta_K(T)$ | Def 15.3 | the interval from separable to joint admissible content — the layer's obstruction |
| ◆ compositionality; ◆ codomain | §24 table | whether content over unions decomposes; whether content lives in a lattice |
| ◆ representability | Rem 24.6 | whether content is a principal down-set (an element) or a general lower set; not necessarily a directed ideal |
| stratum: $\sigma^G$ / $\sigma^0$ / $\sigma^{=}$ / $\widehat\sigma$ | Defs 21.4–21.6, Prop 22.3′ | graph-valued zero-error content; its partition shadow; likelihood-equality content; the Blackwell class |
| coupling; coupling fiber | Rem 21.3, Def 39.1 | the joint behavior marginals do not determine; the space of its possibilities |
| accumulation | Prop 23.3, Thm 84.1 | independent looks compound — the failure of idempotent combination |
| presentation / context / verdict; policy | §19, Def 27.6 | the anchored record's three atoms; the selection resolving ambiguous attribution |
| leak | Prop 28.2, Prop 45.2 | verdict distinctions exceeding the presentation's — content smuggled by attribution |
| blind / targeted pattern | Def 29.1 | corruption indifferent to the candidate / conditioned on it |
| loyalty anomaly; sterility | Prop 30.2, Def 30.3 | erring policies can outinform loyal ones; contexts that cannot leak |
| ◆ fidelity | §32.2 | the record-vs-world axis: provenance, certification, forgery |
| cover; defect; descent | §§35–37 | a decomposition of a view set; the interval its data fail to glue by; the gluing discipline |
| reflection; witness | Thm 37.7 | component-level intervals from graph reflection and witness loss; missing edges alone need not make either interval nonzero |
| ◆ descent (coordinate) | §42 | which layer's data glue: readings/content (cosheaf side) vs distributions (sheaf side) |
| address | Part VII | the mechanism-and-side location of an information quantum (witness / reflection / coupling) |
| ledger | §52 | the data held fixed while alternatives range — fine (candidatewise) vs coarse (question-relative) |
| evaluation; rung | Def 53.1, Def 68.1, Rem 40.3 | the anomaly measured — in bits ($\nu_{\mu,q}$) or deficiency ($\nu_\delta$); the coefficient level (exact / Shannon / enriched) |
| lever | Thm 46.3, §63 | the policy, as the one interpreter-set dial into the obstruction classes |
| half-gap | Prop 69.2 | nondegenerate exact intervals have value $\ge \tfrac12$; only a strictly positive smaller value certifies grading |
| adaptivity premium; causal gap; commitment | Thms 76.2, 77.1, Def 78.2 | history's value to the policy; futurity's cost to the adversary; write-ahead as internalized provenance |
| domain family; vacuous extension | Defs 83.1, 83.4 | related contrast domains under coarsening/restriction/products; pullback of pieces |
| ◆ algebra (coordinate) | Thm 84.1 | generalized set-algebra laws and independent-replication idempotency; a full graded valuation algebra remains unproved |

**Symbols with more than one meaning.** A few letters are reused across parts; the meaning is always fixed by the local context, as listed here.

| symbol | meanings, with the parts where they occur |
|---|---|
| $S$, $T$ | finite view sets (throughout); in Part IV, $S$ is also the standard record (presentation and verdict), and view sets there are written $W$ |
| $\tau$ | the upper adjoint of the content map (Definition 6.1, Theorem 15.1); the verdict view $\tau_v$ of an anchored view (Parts VI, VIII, X); the separation $\tau$ of a dichotomy in total variation (Proposition 71.1) |
| $N$ | the forgetful record (Part IV); the presentation view $N_v$ (Part VI); a binary symmetric channel (Proposition 23.3, Appendix B) |
| $\delta$ | Le Cam deficiency $\delta(E,F)$ (Parts V, IX; Appendix D); point masses $\delta_y$; a cover defect $\delta_K(\mathcal U;T)$ (§37); the erasure probability in Theorem 61.1 and Proposition 71.2; the minimum total-variation gap in the proof of Theorem 22.2 |
| $\Delta$ | the registration anomaly $\Delta_K(T)$ (Definition 15.3) and its components (Theorem 37.7); Le Cam distance $\Delta(E,F)$ (§40); the simplex $\Delta^k$ (Theorem 38.4); the BROJA feasible set $\Delta_P$ (Proposition 55.4) |
| $d$ | the label map $d(E,\pi)=\pi$ (Proposition 6.11); a distractor origin (Parts IV, VI, VIII); the $L_1$ separation of two class averages (Lemma 62.1) |
| $K$ | an admissibility structure (Parts II, V, VI); a regular conditional kernel (Appendix A) |
| $m$ | the minimal sufficient statistic (Theorem 22.6); the number of verdict symbols (Theorem 63.2); fiber minima $m_D$, $m_A$ (Appendix D.4) |
| $\varepsilon$ | a corruption rate (Parts IV, V, VIII–X); an error threshold in $\varepsilon$-answerability (Definition 22.0) |
| $\iota$ | the irreparable attribution rate (Definition 27.3) |

**One overloaded word, disambiguated.** "Kernel" is used in exactly two senses: (i) $\ker(v)$, the kernel *of a map* — always with its argument; (ii) **the kernel**, Part I's exact deterministic core — the maximal-structure fiber of the collapse theorem, called the *exact core* where prose risks ambiguity. “Markov kernel” also occurs for a stochastic channel and has a different, explicitly qualified meaning.
