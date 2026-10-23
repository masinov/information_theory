# organon

The apparatus for the philosophical investigations in this repository: what they share, as opposed to
their content. It holds the bibliography, a graph of entries (claims, concepts, arguments, branches,
objections, decisions, questions, tests), the method itself, and a journal of the work.

Investigations keep their own folders (for example `minimal_epistemic_core/`); their registers are
views generated from the entries here.

## Principles

1. **Text is the source of truth.** Every entry is a Markdown file under git. Indexes and views are
   rebuilt from the files.
2. **Every claim has a provenance and a verification level.** Ours or attributed; checked against the
   text, against a record, or only from memory.
3. **Nothing is deleted.** Refuted ideas and closed branches keep their files, status and reasons.
4. **A graph, not a tree.** Typed links allow both foundational and mutually supporting structures;
   which one a theory has is a question for the investigation (`meta/Q-shape`).
5. **The schema belongs to the method** and is revisable like any other assumption.

## Layout

```
organon/
  README.md        this file
  CLAUDE.md        working protocols for sessions with Claude
  method/          schema.md; rules M1–M5; methodological presuppositions (Mp-*); test protocols (T-*)
  graph/           entries, one folder per namespace (an investigation or a frame), each opened
                   by _investigation.md or _frame.md: mec/ (minimal epistemic core), meta/
  library/
    refs.bib       central bibliography, with verification levels
    merge-notes.md how it was merged from the folders' own .bib files
    sources/       notes on individual works (src/ entries)
    texts/         full texts: local only, not in git
  views/           templates for generated registers
  journal/         one file per working session: handoff notes
  notebook/        untyped, dated thinking that fits no entry type yet
  formal/          formalizations and model-finder runs
  tools/           check.py, q.py, register.py
```

## Use

```
python tools/check.py                      check links, statuses, citations, bibliography
python tools/q.py type=position status=open
python tools/q.py --links mec/C            what links to an entry
python tools/q.py --method mec             method in force in a namespace
python tools/register.py                   regenerate views
grep -ri "in virtue of" graph library      most searches need nothing more
```

## Status

Set up on 2026-10-23. The register of the minimal epistemic core was migrated in as the first test of
the format. Folders still cite their own `.bib` files; papers can switch to `library/refs.bib` with
`\addbibresource{<relative path>/organon/library/refs.bib}`.
