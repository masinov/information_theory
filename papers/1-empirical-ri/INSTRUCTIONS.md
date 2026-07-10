# INSTRUCTIONS — user-executed runs (network/data required)

Environment: Python 3.10+, `numpy`, `scipy`; for §1 also `torchvision`. Files needed in the working directory: `ri_pilot.py`, `ri_text.py`, `pilot-design.md`, `paper.md`.

## 1. MNIST run (fills paper §7.1 ⟦TO FILL⟧)

1. Load data (the only network-dependent step):
```python
from torchvision.datasets import MNIST
import numpy as np
tr = MNIST("data", train=True, download=True); te = MNIST("data", train=False, download=True)
X = np.concatenate([np.array(tr.data), np.array(te.data)]) / 255.0
Z = np.concatenate([np.array(tr.targets), np.array(te.targets)])
```
2. Views: split each image into the 4×4 grid of 7×7 patches; per patch, quantize mean intensity into k = 4 quantile bins **fit on a train split and frozen** (design §0). Then per patch: `P = estimate_channel(codes, Z, k=4, n_class=10)` (from `ri_pilot.py`), using the estimation split; hold out an evaluation split for every reported number; bootstrap CIs with `bootstrap_ci` (B = 200); enforce `refusal(...)` before any pairwise analysis (k² = 16 is safe at MNIST sizes).
3. **E1** (paper §7.1 table): for q ∈ {identity, 3v5, 4v9}: `I_joint` over informative patches (use the top-4 patches by single-view Î to keep the joint alphabet within the refusal rule, and say so); `I_sep(b)` with per-patch optimal b-ary merges (exhaustive over merges at k = 4); report (b, Î_sep, Î_joint, Δ̂) with CIs, b ∈ {1,2,3,4}. Accumulation: two disjoint pixel-subsample codes of one patch; report the gain.
4. **E2**: for pairs of adjacent informative patches and q ∈ {3v5, 4v9}: `ledger_table(...)`; report (Î_joint, Î_min, Ĉ_fine, ĈI_coarse, max Î_v) with CIs; classify by the half-gap using `deficiency` with the margin from Cor 3.4.
5. **E3**: blind: corrupt evaluation codes at ε ∈ {0, .15, .3, .45, .6, .75, .9} with the uniform clutter; plot/tabulate Î vs the closed-form prediction `q_info(blind_mix(P̂_clean, ε), prior, q)` and the enriched TV vs (1−ε)·d̂(0). Targeted: `targeted_attack(...)` at ε around d̂/(2+d̂); verify the hard zero and the TV law.
6. Paste results into paper §7.1 at the ⟦TO FILL⟧ block; give H1–H6 verdicts per `pilot-design.md` §5. If any refusal fires, report it as a finding.

## 2. Corpus data preparation (text)

Obtain sense-annotated tokens (SemCor via NLTK is simplest: `nltk.download('semcor'); nltk.download('wordnet')`). Choose 5–10 polysemous words with ≥ 3 senses and ≥ 300 tokens each, plus (optional) 3 synonym confusion sets. Export one JSONL file, one token per line:
```json
{"word": "bank", "sense": "bank%1:14:00::", "features": {"prev_pos": "IN", "next_lemma": "river", "frame": "of_the_X", "emb8": 3}}
```
Feature guidance: 3–6 context types per word; keep alphabets small (≤ 8; the refusal rule will police you). Recommended types: previous/next lemma bucketed to top-(k−1)+OTHER; syntactic frame; and optionally `emb8` = k-means cluster id (k = 8) of a contextual embedding of the token, **with k-means fit on the train split only**. For the annotator audit, include a second sense field `"sense2"` where double annotations exist.

## 3. Corpus run (fills paper §7.2 ⟦TO FILL⟧)

1. Sanity + channels: `python3 ri_text.py corpus tokens.jsonl bank all` — prints per-type Î and refusals.
2. **Covering**: order tokens randomly; feed prefixes to `empirical_covering`/`certificate` with the pairs of the target question; plot resolved-pairs vs n; compare the slowest pair to `covering_prediction` computed from the estimated channels (replace the planted `CH`/`LAM` by the estimated channels and empirical type frequencies — both functions take only those). Report the hardest pair and whether prediction ordered it correctly.
3. **Selection + audit**: run `greedy` over the word's context types (using estimated channels; set `CH`/`PRIOR` module-level or adapt the two lines marked in `I_of_set`); budget k = 3. If greedy stalls (best gain < 1e-3 of H(q)), the audit reports candidate coupled pairs — a firing audit on real data is the paper's headline text result; report ĈI_coarse for the flagged pair with a bootstrap CI.
4. **Certificates**: for each word, the §4.3 certificate at budgets {25, 50, 100} tokens; paste one full certificate (residual pairs + recommended frames) into §7.2.
5. **Annotator audit**: on double-annotated tokens: disagreement E, bracket [E/2, E], and Ĥ(s|τ) vs h(ε̂)+ε̂log₂(m−1) with ε̂ = E/2 (Prop 6.1). If gold sense exists for a subsample, report the true ε against the bracket.
6. Paste into paper §7.2 ⟦TO FILL⟧; log every refusal.

## 4. Reporting discipline

Every number with a bootstrap CI; every closed-form comparison as (measured, predicted, |gap| vs CI); refusals listed, not hidden. If a closed-form law fails outside CIs, that falsifies the modeling frame per design §5 — report it prominently, not apologetically.

## 5. Post-review regeneration (corrected Theorem 4.2)

The corpus run exposed a bug in the first-version covering bound (see the paper's
correction disclosure at Thm 4.2). `ri_text.covering_prediction` is patched; your
`src/corpus_experiment.py` ports the old formula at its `covering_prediction`
(lines ~77–85). Replace the body of the per-pair loop with the per-type minimum:

```python
def per_type(t):
    b = max(BC(channels[t][:, i], channels[t][:, j]), 1e-9)
    return (1/lam[t]) * max(1.0, np.log(2*E/delta)/np.log(1/b))
out[(i, j)] = min(per_type(t) for t in seps)
```

**Normalization requirement (canonical, adopted from the executed port):** the `lam`
passed to the prediction MUST be the *normalized per-type arrival distribution of the
empirical stream* — the same one the accumulator samples. Raw masses, counts, or
per-token availability fractions (which can sum to more than 1 when tokens carry
several features) invalidate the bound's `1/lam_t` scaling.

Then re-run `corpus_experiment.py` and paste the regenerated per-word prediction
columns and hardest-pair ordering verdicts into paper §7.2 at the ⟦REGENERATE⟧
mark. Medians, refusals, certificates, tell's censored pairs, and the audit
result do not change.
