# Registered Information — project workspace

Foundational monograph plus its derived papers, each self-contained with its own
scripts, results, and reproduction notes.

```
monograph/                     [RI]  the manuscript (Parts I–XI, Appendices A–C)
continuation-scaffold.md             project-wide running log (both papers)
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
