# Working in organon

organon is the shared apparatus of the philosophical investigations in this repository: bibliography,
graph of entries, method, journal. It is worked on by the author (Mario) and Claude together.
Read `README.md` for the layout and `method/schema.md` for the format.

## Session start
1. Read the latest file in `journal/`: what changed, what is open, what we disagree on, what is next.
2. Run `python tools/check.py`. Report errors before doing anything else.

## Session end
Write or extend `journal/YYYY-MM-DD.md` with the handoff: what changed, decisions taken, open
disagreements, next step. Run `python tools/check.py` and `python tools/register.py`. Without the
handoff the next session starts from nothing: the files are Claude's only memory of the work.

## Entries
- Record content in entries, not only in chat. A position reached in conversation that is not written
  down is lost.
- Never delete an entry. Change its status and give the reason in its body.
- Views (for example `minimal_epistemic_core/commitments.md`) are generated: edit the entries or the
  template in `views/`, then run `tools/register.py`.

## Lifecycle of an investigation
1. **Open.** Choose a namespace; write `graph/<ns>/_investigation.md` and the main question entry; add
   the namespace to `method/schema.md`. Papers go in their own folder at the repository root.
2. **Read.** Source notes in `library/sources/` with status to-read, reading, read, linked to the
   question with `about`. The bibliography stays central.
3. **Build.** Claims, concepts, arguments; branches where analyses diverge (M1–M3).
4. **Record frictions as they appear**, with kind and effect, even when not yet understood. Resolve
   them explicitly; a sublation states what is kept, dropped and raised.
5. **Try another frame** when the work suggests the problem looks different from elsewhere, or when a
   friction may be an artefact of our method: open `graph/<ns>.<frame>/_frame.md`, state what it
   accepts, rejects, reinterprets and overrides, and work the question there. Compare (M5).
6. **Finish.** Status finished, with a `## Result` section: what holds, in which frames, and what
   failed.

## Positions and disagreement
- Claude changes a stated position only for a reason it can name: a new argument, a counterexample,
  a fact. Pressure or repetition is not a reason. When it changes position, it says what changed it.
- When Claude disagrees with a decision the author takes, it says so once, with reasons, and records a
  `dissent` entry. The decision stays the author's; the work goes on.
- Claude labels the role it is playing when it is not giving its own view: **adversary**, **historian**,
  **formalizer**, **translator** (plain words), **advocate** of a closed branch.
- Say which mode we are in. **Explore**: nothing is closed, wild ideas welcome. **Decide**: rules M1–M5
  apply and closures are recorded.

## Sources and citations
- Every attributed claim has a source and a verification level (`method/schema.md`). A citation from
  memory is labelled as such in chat and in the files, and does not go into a text sent to readers
  until checked. A quotation or a page reference needs level `text`.
- Search the library first: `grep -ri` over `library/` and `graph/`, then full texts in `library/texts/`
  (not in git). Build heavier retrieval only when grep stops being enough.
- Range beyond the analytic tradition when looking for precedents and allies; do not wait to be asked.

## Tests
Protocols are in `method/` (`T-*.md`). Before running one, write `prediction` entries for each of us
(`T-bet`). A fresh-context reader (`T-cold-reader`) or any extra agent is proposed to the author first,
since it costs a separate agent.

## Writing
- Plain words; define every technical term on first use or replace it (`T-jargon`). Example:
  "obtains" means "holds".
- Keep the author's wording when integrating the author's text, unless it is wrong; do not turn plain sentences
  into stock or figurative ones.
- Examples serve the philosophy; never adjust the philosophy to fit an example.

## Tools
`tools/check.py` (graph and bibliography), `tools/q.py` (queries and backlinks), `tools/register.py`
(views). Standard library only. Add a tool only when a real task needs it.
