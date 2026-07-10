# Experiment results & reproduction — Empirical Registered Information

This is **paper #1** of the project (`papers/1-empirical-ri/`). It fills the two
⟦TO FILL⟧ blocks of `paper.md` (§7.1 MNIST, §7.2 corpus) per `INSTRUCTIONS.md`. All
code is in `src/`, driven by the shared kernel `../../shared/ri_pilot.py` and the
paper-local reference implementation `ri_text.py`.

**Post-review state (current):** the reviewer accepted the runs and adopted the
filled `paper.md` as canonical. The corpus run falsified the first-version covering
bound of Theorem 4.2; the theorem is corrected to the per-type form, `ri_text.py`
and `src/corpus_experiment.py` are patched, and the §7.2 prediction columns are
regenerated. `paper.md`, `INSTRUCTIONS.md`, `ri_text.py` (this folder) and the shared
`../../shared/ri_pilot.py` hold the reviewer's canonical versions; the transient
`paper_experiments_review/` folder was removed after adoption.

## Reproduce

```bash
# run from this folder:  cd papers/1-empirical-ri   (venv lives at repo root)
# deps (numpy, scipy, nltk) already installed in ../../venv
../../venv/Scripts/python src/synth8_validation.py     # -> results/synth8_validation.json (planted dry run, H2-H6)
../../venv/Scripts/python src/data_mnist.py            # downloads MNIST idx (~11 MB) into data/
../../venv/Scripts/python src/mnist_experiment.py      # -> results/mnist_results.json  (paper §7.1)
../../venv/Scripts/python src/prepare_corpus.py data/tokens.jsonl   # SemCor -> tokens.jsonl
../../venv/Scripts/python src/corpus_experiment.py data/tokens.jsonl # -> results/corpus_results.json (paper §7.2)
```

Run `synth8_validation.py` FIRST: per pilot-design §6, every estimator is checked
against its exact closed form on planted ground truth before the MNIST numbers are
trusted. It is where H5 (transport) and H6 (half-gap vs injected noise) live — the
MNIST confusable pairs use binary `q`, whose trivial ledger functor cannot exhibit
an address *split*.

NLTK data (`semcor`, `wordnet`, `omw-1.4`) downloads to the user default
(`~/AppData/Roaming/nltk_data`); a project-local `nltk_data/` path is rejected by
NLTK's downloader security check on Windows.

## Files

| file | role |
|---|---|
| `src/synth8_validation.py` | planted-ground-truth dry run (design §6): H2–H6 vs closed forms |
| `src/data_mnist.py` | MNIST loader via direct idx.gz download (no torchvision) |
| `src/mnist_experiment.py` | E1/E2/E3 (§7.1); vectorized + Miller–Madow estimators; frozen quantile bins |
| `src/prepare_corpus.py` | SemCor → `tokens.jsonl` (bucketed features, train-frozen vocab) |
| `src/corpus_experiment.py` | covering / selection+audit / certificates / annotator note (§7.2) |
| `results/mnist_results.json`, `results/corpus_results.json` | full numeric outputs |
| `data/corpus_summary.json` | per-word sense counts, dropped-rare, refusals |

## Headline results

**Synth-8 planted dry run (design §6).** All planted checks pass against closed
forms: transport C_fine=0.0000 / CI_coarse=0.998 (plant 0 / 1); coupling quantum
0.3092 vs 0.3113; accumulation +0.211; blind |gap|≤0.002; targeted hard zero
Î=0.00000 at ε\*=0.411; half-gap deterministic 0.4999 with ν̂_δ tracking injected
BSC noise (0.054→0.452 as crossover 0.05→0.45).

**MNIST (§7.1).** H1–H6 (design §5 mapping) supported; every closed-form law held
inside its bootstrap CI.
- E1 (**corrected**: b-ary compressed views read *jointly*, Miller–Madow
  corrected): Δ̂(b) monotone ↓, strictly positive & CI-separated for small b (H1),
  ≈0 at b=4 (sep=joint by construction); accumulation gain +0.147 bits (identity, H2).
- E2: fine = coarse ledger exactly (binary q ⇒ trivial ledger functor);
  ν̂_δ = 0.003 < ½ ⇒ graded interval (H6 on MNIST).
- E3: blind law matches to |gap| ≤ 0.005 bits (within CI), no annihilation for
  ε<1 (H3); **targeted hard zero exactly at ε\* = d/(2+d)** — Î = 0.0000 at
  ε\* = 0.308 (3v5), 0.279 (4v9) (H4).
- H5 (transport split) is exhibited on Synth-8, not MNIST: binary confusable-pair
  questions have a trivial ledger functor (C_fine = CI_coarse), so no address
  split is possible there — noted in-paper, not a falsification.

**Corpus (§7.2).** Refusal rule is active and reported, not hidden:
- *take, time, first* fully refuse (rarest sense < 40 tokens) — the "thin channels"
  finding.
- Covering: **this run falsified the first-version bound of Theorem 4.2** — under
  the old total-mass/best-BC formula the medians exceeded the "upper bound"
  (think 369 vs 78.9). The theorem is corrected to the **per-type form** (ri_text.py
  patched; src/corpus_experiment.py patched per INSTRUCTIONS §5); regenerated,
  every median now sits strictly below its prediction (think 369<1878, give
  476<2541) and hardest-pair ordering is correct for *give, think, go* (3/4).
  *tell* has genuinely never-resolved (censored) residual pairs.
- Selection: objective is submodular on all four estimable words — no
  super-additive pair, stall-audit correctly does **not** fire (specificity check;
  the 0.322-bit coupling exhibit stays SynthSense's planted result).
- Certificates produced at budgets {25,50,100} with residual pairs + recommended
  frames. Annotator Fano audit: N/A on SemCor (single-annotated) — validated on
  SynthSense.

## Documented protocol deviations (forced by data/environment)

1. **`pilot-design.md`** was provided after the first pass and reconciled: the
   H1–H6 hypotheses now follow the design's §5 wording exactly (H5 = transport,
   H6 = half-gap vs injected noise — not the placeholder mapping used before);
   E1's `I_sep(b)` now reads the b-ary-compressed views **jointly** per design §1
   (guaranteeing Δ̂(b) ≥ 0), and Miller–Madow bias correction (design §4) is applied
   to E1's count-based Î. E2/E3 operate on estimated channels, where Laplace
   smoothing + bootstrap handle bias (per `ri_pilot.mi`'s own note). The planted
   dry run of design §6 is now executed explicitly (`synth8_validation.py`).
2. **MNIST via direct idx download**, not `torchvision` — identical bytes, avoids a
   ~200 MB torch install. Data are the same 70 000 images.
3. **MNIST splits.** The top-4 joint alphabet 4⁴=256 makes the refusal bound
   20·256=5120 (~81% of the rarest class) incompatible with a *third* disjoint
   estimation/evaluation split. We freeze the quantizer on a disjoint 10k split and
   estimate+evaluate on the remaining 60k with B=200 bootstrap for CIs. Pairwise
   (E2, alphabet 16) stays far inside the rule.
4. **`emb8` omitted** in the corpus features (optional per INSTRUCTIONS §2) — the
   five symbolic context types avoid a transformer dependency and already exercise
   covering/selection/certificates.
5. **Adaptive alphabet coarsening** in the corpus run: rather than a fixed alphabet
   that refuses everywhere, each word/type uses the largest alphabet a ≤ n_min/20,
   in the spirit of "the pipeline coarsens or declines rather than overclaims" (§3).
6. **Corpus covering model.** SemCor tokens carry all context types at once, unlike
   §4's one-view-per-usage i.i.d. model. We model each usage as exposing one type
   drawn from λ_t = empirical informativeness (non-OTHER/non-boundary mass),
   normalized — the "empirical type frequencies" INSTRUCTIONS §3.2 asks for.
7. **Half-gap margin** (E2) is set to a fixed conservative ε̄ = 0.02; design §4
   prefers it from bootstrap TV-fluctuation quantiles. This does not affect any
   verdict — the measured ν̂_δ ≈ 0.003 sits two orders of magnitude below the ½
   threshold, so "graded" is robust to the margin. Worth tightening if the
   published version wants the tolerance data-driven throughout.
