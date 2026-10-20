# Note on rounds 4 and 5: the Anti-Newcomb test case

The prompts and outputs in this folder are kept exactly as they were sent and received. This note
records one defect in them, so that a reader does not take that material as part of the problem.

## What happened

The round 4 prompt (task K6) and the round 5 prompt (task P6) include an "Anti-Newcomb" example,
together with a person's two readings of it: an "identity" reading and a "solve-then-apply" reading.
This material did not come from the task of proving or refuting the thesis. It came from an earlier,
unrelated conversation, held before the proving work began. That conversation had discussed the
example, and the prompt writer carried it into prompts that were meant to be self-contained. The
person's name came along with it.

The provers treated the example as part of the problem and reported on it:

- **Round 4, output §9.** The prover analysed an exclusive transparent/opaque-box version, with
  causal matrix (1 2; 1 0). This is close to Skalse's construction, not the example as later
  specified.
- **Round 5, output §8.** The prover analysed the version stated in the round 5 prompt:
  U(one-box) = 2x and U(two-box) = 2x + 1, where x = 1 iff f(d) = one-box. Its payoff table is
  Newcomb's.

## Why the example is not used in the paper

The example tests only one thing: whether an embedded program f counts as linked to the agent or as
a fixed component. The paper already settles that distinction with problems it needs anyway:

- Newcomb's problem and the twin prisoner's dilemma show the linked case.
- The fixed-copy diagonal shows the fixed case.

Round 5's test-case table shows the point directly. Anti-Newcomb receives exactly the Newcomb vector
when f is linked, and the frozen-predictor vector when f is fixed, so it adds no verdict that the
other rows lack. Round 5 also notes that it is not a diagonal defeating every theory, so it bears on
neither the possibility results nor the impossibility results.

The paper therefore omits the example, the two named readings, and the attribution. All other
results of rounds 4 and 5 are independent of it.
