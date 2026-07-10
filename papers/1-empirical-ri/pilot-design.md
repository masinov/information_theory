# Pilot Design: Registered Information on Image Classes (MNIST)
 
*Companion to the manuscript. Design + reference implementation (`ri_pilot.py`) + synthetic validation run. Status: dry-run validated on planted ground truth; MNIST swap is a documented 10-line change.*
 
---
 
## 0. The modeling move (read this first)
 
The contrast domain is **not** the image space. It is the space of alternatives:
 
- **D = the 10 classes** (|D| = 10; for the validation synthetic, 8 planted classes).
- **Views = measurement channels** $P(Y_v \mid \text{class})$: each view is a quantized image statistic (a patch code), and its channel is *estimated* from data.
- **Questions** = class distinctions: the identity question, binary questions on confusable pairs (3v5, 4v9, 7v1), and structured questions (parity-type) for the transport experiment.
This keeps every lattice, LP, and convex computation from the manuscript trivially tractable (all objects live over a 10-element domain) and concentrates all statistical difficulty where it belongs: in the estimation of per-view channels. That estimation layer is the pilot's genuinely new content — the manuscript's theory is stated for *given* channels.
 
**Views (model-free core).** Partition each 28×28 image into a 4×4 grid of 7×7 patches → 16 views. Quantizer per patch: mean-intensity quantile bins (k = 4) for the robust baseline; k-means patch codes (k = 8–16) as the richer variant. Quantizers are fit on the train split and frozen. Channels: Laplace-smoothed empirical $\widehat{P}(\text{code} \mid \text{class})$. (A stage-2 variant replaces patches with quantized probe activations of a trained network, turning E1 into a direct probe-power audit; the core pilot stays model-free.)
 
---
 
## 1. Experiment E1 — Admissibility audit (Part II, empirically)
 
**Object.** The encoded-vs-extractable gap under a decoder class: per-view readings restricted to $b$-ary compressions (the budget ceiling, §16.2's flavor, at the Shannon rung).
 
**Procedure.** For a question $q$ and view set $T$: (i) $\widehat{I}_{\text{joint}} = \widehat{I}(q; Y_T)$; (ii) $\widehat{I}_{\text{sep}}(b)$: each view compressed alone to $b$ symbols by the $q$-optimal quantizer (exhaustive over merges at these alphabet sizes, or agglomerative information-bottleneck), then the compressed outputs read jointly; (iii) the **admissibility anomaly in bits** $\widehat{\Delta}(b) = \widehat{I}_{\text{joint}} - \widehat{I}_{\text{sep}}(b) \ge 0$, per Part VII's evaluation of the Part II interval. Sweep $b \in \{1, 2, 3, 4\}$, per question.
 
**Accumulation demo (Theorem 84.1 in the wild).** Two conditionally independent looks at the same statistic (disjoint pixel subsamples of one patch, or two independent stochastic quantizations): report $\widehat{I}(q; Y, Y') - \widehat{I}(q; Y) > 0$ — idempotency failure, measured in bits.
 
**Interpretability reading.** $\widehat\Delta(b)$ is the probe-power problem made quantitative: what the representation encodes about $q$ versus what per-part bounded probes extract.
 
## 2. Experiment E2 — Address decomposition (Parts V + VII, empirically)
 
**Objects.** For view pairs and a question $q$, the two-ledger decomposition:
 
- **Fine-ledger coupling component** $\widehat{C} = \widehat{I}_P(q; Y_v, Y_w) - \min_{Q \in \widehat{\mathrm{Fib}}} I_Q(q; Y_v, Y_w)$, the fiber ranging over couplings of the *estimated per-class marginals* (Definition 55.1). Convex program: $I$ is convex in the joint channel; solved by SLSQP over the product of per-class transportation polytopes (alphabets ≤ 16 ⟹ ≤ a few hundred variables).
- **Coarse-ledger component** = BROJA's $CI$ (Proposition 55.4 operationalized): the same solver on the $q$-marginalized family.
- **Marginal-forced residual** $\widehat{I}^{\min}$ and the per-view baselines.
**The transport test (Theorem 56.2, empirically).** Near-deterministic view pairs with parity-structured $q$: predicted $\widehat{C}_{\text{fine}} \approx 0$ (fiber near-singleton) while $\widehat{CI}_{\text{coarse}} > 0$ — the same bits changing address across ledgers, on data.
 
**Stratum classification with the half-gap (Proposition 69.2 as an instrument).** Anomaly intervals with estimated enriched value $\widehat{\nu}_\delta < \tfrac12 - m$ (margin $m$ from the bootstrap) are certified **graded**; the deficiency LP runs on estimated channels, and its estimation theory is trivial because $\delta$ is 1-Lipschitz in $\sup_z \mathrm{TV}$ (one line; contrast MI's boundary behavior) — Part IX's practical payoff.
 
**Deliverable.** Per confusable pair: the ledger table $\big(\widehat{I}_{\text{joint}}, \widehat{I}^{\min}, \widehat{C}_{\text{fine}}, \widehat{CI}_{\text{coarse}}, \max_v \widehat{I}_v\big)$ with CIs, plus the address classification.
 
## 3. Experiment E3 — Corruption curves (Parts VIII + X, empirically)
 
**Blind law.** Corrupt evaluation data at rate $\varepsilon$ (each code replaced by a candidate-free draw $Q$). Two predictions from the *clean* estimate, tested against re-estimation on corrupted data: (i) the Shannon curve equals the mixture formula $I$ computed analytically from $(1-\varepsilon)\widehat{P} + \varepsilon Q$; (ii) the enriched separation is **exactly linear**, $\widehat{d}(\varepsilon) = (1-\varepsilon)\,\widehat{d}(0)$ — the two-rung comparison (square law near annihilation) on data.
 
**Targeted law.** For binary $q$ with estimated class-conditional averages $\bar p_1, \bar p_2$, $\widehat{d} = \lVert \bar p_1 - \bar p_2 \rVert_1$: implement Lemma 62.1's optimal attack (the $s^{\pm}$ clutter) on the data; predictions: hard zero at $\widehat{\varepsilon}^* = \widehat{d}/(2 + \widehat{d})$, TV law $\max(0, (1-\varepsilon)\tau - \varepsilon)$, and *no* blind zero below $\varepsilon = 1$.
 
**Causal gap (optional stage 2).** Split views into "time 1" (top-half patches) and "time 2" (bottom); a prior tilt on a time-2-measurable factor; compare clairvoyant vs prefix-restricted attacks against Theorem 77.1's $\tfrac13$-vs-$\tfrac12$-type gap.
 
## 4. Estimation layer (the pilot's honest new content)
 
- **Plug-in with hygiene.** Laplace smoothing $\alpha = 0.5$; Miller–Madow bias correction on all $\widehat{I}$; nonparametric bootstrap (B = 200) over the evaluation split for 95% CIs on every reported number.
- **Refusal rule.** A pairwise analysis with joint alphabet $k^2$ is reported only if $n_{\text{class}} \ge 20\,k^2$; otherwise the pipeline coarsens the quantizer or declines — it refuses rather than overclaims (the framework's own discipline, applied to itself).
- **Splits.** Train (quantizers) / estimation (channels; all optimization) / evaluation (all reported values; corruption applied here).
- **Tolerances.** Stratum tolerances ($\widehat{\sigma}^{=}$-clustering; $\varepsilon$-supports for $\widehat{\sigma}^0$) set from bootstrap TV-fluctuation quantiles, not by hand.

## 5. Falsifiable hypotheses
 
**H1** $\widehat{\Delta}(b) > 0$ (CI-separated from 0) for small $b$ on confusable pairs. **H2** Accumulation gain > 0 beyond CI. **H3** Blind curves match the mixture prediction within CIs; enriched separation linear in $(1-\varepsilon)$. **H4** Targeted information hits zero at $\widehat d/(2+\widehat d)$ within estimation error; blind never does. **H5** Transport: pairs with $\widehat{C}_{\text{fine}} \approx 0$ and $\widehat{CI}_{\text{coarse}} \gg 0$ exist (parity-structured questions). **H6** The half-gap classifier's "graded" verdicts agree with known injected noise. Any clean failure of H3/H4 falsifies the modeling frame, not just a tuning choice — that is the point of running laws with closed forms.
 
## 6. Validation protocol (this dry run)
 
Because the theory's predictions have exact closed forms, the pipeline is validated **before touching real data** on a synthetic domain with planted structure ("Synth-8": $D = \{0,1\}^3$, 8 classes): a deterministic parity pair (planted transport: $C_{\text{fine}} = 0$, $CI_{\text{coarse}} = 1$ bit), a planted pure-coupling pair (Proposition 22.4(2): quantum $\tfrac32 - \tfrac34\log_2 3 \approx 0.3113$ bits, fiber min $0$), two independent BSC(0.15) looks (accumulation; blind decay; targeted threshold $\tfrac12$). Every estimator must recover its planted closed form within bootstrap CI; the same code path then runs on quantized glyph images (8×8 renders + pixel noise) to exercise the full quantizer→channel→analysis pipeline. **MNIST swap:** replace the generator with the torchvision loader and the glyph quantizer with the 4×4 patch quantizer; nothing else changes.
 
## 7. Budget and deliverables
 
CPU-only; every computation at these alphabet sizes runs in seconds (fiber programs are the slowest at ~1s per pair). Deliverables: this document; `ri_pilot.py` (estimation, evaluations, fiber/BROJA solver, deficiency LP, corruption operators, bootstrap harness, refusal rule); the validation run's tables and curve checks; and, on real MNIST, the E1–E3 report with H1–H6 verdicts.
