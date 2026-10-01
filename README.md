# Registered Information — project workspace

**Integrated edition (2026-10-01).** The monograph now contains the corrected statements, proofs, hypotheses, and conclusions directly. Start with [Part I](monograph/registered-information-kernel.md); [Appendix D](monograph/registered-information-appendix-D.md) contains the supplementary proofs, including the site criterion, witness cut criterion, exact join-tree propagation, and finite transfer certificates. The [proof audit](review/proof-audit.md) records the revision history of all 136 original numbered results and indexes the 16 numbered appendix additions. The companion papers' empirical runs were not rerun.

Recommended order: Parts I–III (foundations), IV–VI (records, descent, admissibility), VII and IX (quantification), VIII and X (corruption and interaction), XI (qualified synthesis), then Appendices A–D. [Review checks](review/check_finite_claims.py) and their [results](review/finite-check-results.json) provide a separate, reproducible validation path. [Integration checks](review/check_integrated_claims.py) and their [results](review/integrated-check-results.json) validate the added structural examples.


Foundational monograph plus its derived papers, each self-contained with its own
scripts, results, and reproduction notes.

```
monograph/                     [RI]  the manuscript (Parts I–XI, Appendices A–D)
review/                         proof audit, corrections, new results, independent checks
continuation-scaffold.md             historical project log (both papers)
papers/
  shared/
    ri_pilot.py                shared kernel: deficiency, q_info, fiber_min_I, … (used by BOTH papers)
  1-empirical-ri/              [ERI]  derived paper #1 — "Empirical Registered Information"
    paper.md  INSTRUCTIONS.md  pilot-design.md  RESULTS.md
    ri_text.py                 paper-#1 reference impl (covering/selection/certificates)
    src/                       drivers: synth8_validation, data_mnist, mnist_experiment,
                               prepare_corpus, corpus_experiment
    data/  results/            inputs (SemCor/MNIST) and JSON outputs
  2-lecam-synergy/             derived paper #2 — "Le Cam Synergy" (cites [RI] and [ERI])
    paper-lecam-synergy.md
    ri_pid.py                  reference lib (gates, S_delta, S_I, BROJA-CI); imports shared kernel
    src/  results/             (experiment driver TBD — paper's tables came from the author's runs)
venv/                          Python env (numpy, scipy, nltk)
```

**Shared kernel.** `papers/shared/ri_pilot.py` is the single source of truth for the
deficiency/mutual-information primitives. Paper #1's drivers add `../../shared` to the
path; paper #2's `ri_pid.py` adds `../shared`. Paper #2 reusing this kernel means its
`BROJA-CI(AND)=0.5000` doubles as a cross-check of paper #1's solver.

**Reproduce.** See `papers/1-empirical-ri/RESULTS.md` (run its scripts from that folder;
the venv lives at repo root). Paper #2 currently ships the library only; a driver would
be needed to regenerate its §6 tables locally.
