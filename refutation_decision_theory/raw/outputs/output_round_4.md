# Round 4: results and scope

**The thesis is true for several precise classes, but the strongest clean impossibility is about exact computation, not specifically about inferring counterfactual dependence.**

There are four distinct results:

1. **Finite, deterministic oracle problems with exactly comparable payoffs admit a uniform computable optimizer on their valid-input domain.** The optimizer evaluates the environment under each finite policy. It does not need a lookup table or a predictor-identification algorithm.

2. **Requiring that optimizer to halt on every input string changes the answer.** If arbitrary fixed computable algorithms may occur in environments, a self-referential fixed-copy construction defeats every globally total computable rule. This is the Skalse-type baseline.

3. **Almost-surely terminating stochastic environments admit a stronger computational impossibility.** No computable rule can select an exact expected-payoff maximizer everywhere, even with two actions, payoffs in \(\{0,1\}\), no predictors, no embedded agent copies, and uniformly computable expected values.

4. **“Replace extensionally equivalent programs” does not supply a unique logical-counterfactual semantics.** Equality on the inputs actually used can be decidable but yield an unsatisfiable optimality condition. Equality on all inputs is undecidable, and admits a valid halting reduction, but it also leaves simple fixed-algorithm diagonals intact.

The literature already distinguishes replacing an agent from counterfactually changing that same agent’s decision. Fallenstein makes this distinction explicitly in “Third-person counterfactuals”; it is not a new distinction introduced by this round. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebf/third-person-counterfactuals?utm_source=chatgpt.com)

I give precise models and proofs below. “Promise-total” and “globally total” must remain separate throughout.

---

## 1. Definitions that make the question well-posed

### 1.1 Two meanings of a computable agent

Fix an effective language of descriptions with computably readable, finite, nonempty action sets.

A **globally total agent** is a computable function that halts and returns a legal action on every well-formed description, including descriptions that do not describe admissible environments.

A **promise-total agent on \(\mathcal C\)** is a partial computable procedure that halts and returns a legal action on every description belonging to \(\mathcal C\). It may diverge outside \(\mathcal C\).

These are different requirements. The wording “total computable function” normally means the first; “must halt on every description in the class considered” also permits the second interpretation. Both receive answers below.

For the negative results, a fixed binary action language suffices. Thus issues about choosing defaults in varying action sets do not affect them.

### 1.2 Owned inputs and policies

For the finite-policy results, an environment \(E\) has a finite set of owned queries

\[
Q_E=\{q(E,h):h\in H_E\},
\qquad
\Pi_E=\prod_{h\in H_E}A_{E,h}.
\]

The root description \(d(E)\) is one of these queries.

I stipulate that:

- a query identifies its parent environment and its information set;
- distinct environments have disjoint owned-query namespaces;
- repeated queries receive the same answer;
- the environment can access the evaluated agent only through these queries when \(F_{\mathrm{self}}\) is imposed.

The ownership condition matters. If two different environments can call the same query “their own,” the \(F_{\mathrm{any}}\) contradiction can reappear inside an ostensibly self-only class.

For a table policy \(\pi\), let \(E^\pi\) mean execution with every owned agent query answered by the corresponding table entry.

### 1.3 Payoff representation

A finite program does not literally return an arbitrary real number in finitely many bits. Three representations must be distinguished:

| Representation | What execution supplies |
|---|---|
| Exact rational | A rational payoff, or an explicit finite distribution with rational probabilities and rational payoffs |
| Computable real | A program providing arbitrarily accurate rational approximations |
| Sampled payoff | A random execution returning a realized payoff, whose expectation defines value |

The positive exact-optimization theorem uses the first representation. The stochastic impossibility uses only realized payoffs \(0\) and \(1\), so it does not exploit exotic real-valued outputs.

### 1.4 Agent substitution versus an anchored intervention

Some proposed notions define a genuine common payoff function

\[
U(E,A).
\]

Others first inspect or execute a reference agent \(T\), then freeze part of the resulting situation while considering alternatives. Those require

\[
U_K(E,T;A),
\]

where \(K\) is the intervention convention.

Require at least the baseline identity

\[
U_K(E,T;T)=U(E,T).
\]

Then the corresponding anchored optimality condition is

\[
U(E,T)\ge U_K(E,T;A)
\quad\text{for every admissible }A.
\tag{1}
\]

In general, there is no function \(W(E,A)\) such that

\[
U_K(E,T;A)=W(E,A)
\]

for every reference \(T\). Consequently, some versions of your question concern **a common environment’s best agent**, while others concern **whether an agent is a fixed point of its own counterfactual evaluations**.

That distinction is mathematically substantive.

### 1.5 The four executable replacement conventions

I use the following precise interpretations.

| Notion | Replacement convention |
|---|---|
| \(O_{\mathrm{const}}\) | Change the designated actual-action port; freeze other responses at their baseline values, or leave fixed embedded algorithms unchanged |
| \(O_{\mathrm{oracle}}\) | Replace every designated oracle call by a call to \(A\) |
| \(O_{\mathrm{syn}}\) | Replace specified, typed program occurrences whose syntax equals the reference program |
| \(O_{\mathrm{ext}}\) | Replace specified program components satisfying a stated extensional-equivalence test relative to the reference agent |

For \(O_{\mathrm{syn}}\) and \(O_{\mathrm{ext}}\), I freeze the original input description \(d(E)\) during replacement. Supplying the rewritten source \(d(E[A])\) instead changes the agent’s observation as well as the program occupying the agent role. That is another legitimate model, but a different one.

Raw substring replacement is not an adequate default for \(O_{\mathrm{syn}}\): it can alter quoted data, comments, unrelated identifiers, or program encodings. Typed occurrences or explicit component interfaces are needed.

\(O_{\mathrm{log}}\) is a family of logical semantics and procedures, not yet a fifth replacement operation. Section 7 fixes precise versions.

### 1.6 Fairness

The fairness conditions are overlapping restrictions, not four mutually exclusive classes.

- **\(F_{\mathrm{self}}\):** dependence on the evaluated agent is confined to \(Q_E\).
- **\(F_{\mathrm{any}}\):** arbitrary agent-query inputs are permitted.
- **\(F_{\mathrm{ext}}\):** replacing agents by extensionally equal agents preserves the relevant payoff kernel.
- **\(F_{\mathrm{const}}\):** fixed algorithms are permitted as environmental constants.

For anchored kernels, a strong extensionality requirement is

\[
T\equiv T',\quad A\equiv A'
\ \Longrightarrow\
U_K(E,T;A)=U_K(E,T';A').
\tag{2}
\]

There are also two locality requirements worth separating:

- **Executed-query locality:** actual executions call agents only on owned inputs.
- **Kernel locality:** the entire counterfactual kernel, including the rule that decides what to replace, depends on the reference agent only through its owned-input policy.

Global program-equivalence matching can satisfy the first while violating the second.

---

## 2. K1: the oracle case has a constructive positive theorem

Define the promise class

\[
\mathcal P_{\mathbb Q}
=
\left\{
E:
E^\pi\text{ halts and returns an exact rational value for every }
\pi\in\Pi_E
\right\}.
\]

This definition uses finite table oracles, so environment validity is not defined circularly in terms of whichever optimizer we eventually construct.

### Theorem 1 — Uniform optimization on the promise class

There is a promise-total computable agent that is \(O_{\mathrm{oracle}}\)-optimal on every \(E\in\mathcal P_{\mathbb Q}\).

#### Construction

On input \(q(E,h)\):

1. Recover \(E\) and its finite policy space.
2. Run \(E^\pi\) for every \(\pi\in\Pi_E\).
3. Obtain every exact rational value \(V_E(\pi)\).
4. Select the first maximizer \(\pi_E^*\) in a fixed effective ordering.
5. Return \(\pi_E^*(h)\).

#### Proof

There are finitely many policies, and every simulation terminates by the promise. Exact rational comparison terminates.

All owned queries recover the same parent environment and use the same tie-breaking rule. Therefore their answers form one coherent policy \(\pi_E^*\).

Every admissible competing agent \(A\) induces a policy

\[
\pi_E^A(h)=A(q(E,h)).
\]

Under oracle replacement,

\[
U(E,A)=V_E(\pi_E^A)
\le
\max_{\pi\in\Pi_E}V_E(\pi)
=
U(E,T^*).
\]

Thus \(T^*\) is optimal. \(\square\)

**The lead in K1 is therefore correct under these assumptions.** The optimizer never asks its live self what it would do during a counterfactual simulation. It supplies table answers instead.

### Is an explicit finite policy header necessary?

It is sufficient, but not always necessary.

For a finitely branching oracle machine that halts for **every abstract total oracle**, exhaustive exploration of its consistent oracle-answer tree terminates. Otherwise König’s lemma would give an infinite path whose answers extend to a total oracle, contradicting universal termination.

This supplies another route to a finite optimization problem.

However, termination merely against every **computable** oracle does not justify that compactness argument: an infinite computable tree can lack a computable infinite path. The finite-header model avoids this complication.

### What if termination depends on the oracle?

Dependence itself is harmless if every allowed policy still terminates.

The positive theorem fails when some alternatives are undefined. For example:

- action \(0\): return \(0\);
- action \(1\): simulate machine \(e\), then return \(1\) if it halts.

This environment is excluded from \(\mathcal P_{\mathbb Q}\) when \(e\) does not halt.

If one adds the convention “divergence has payoff \(-1\),” exact optimization would choose action \(1\) exactly when \(e\) halts. That would decide halting. The obstruction comes from the added divergence semantics, not from a failure of the finite-policy proof.

---

## 3. The two baseline impossibilities

### 3.1 \(F_{\mathrm{any}}\): incompatible requirements at a shared input

### Theorem 2 — No universal oracle optimum with unrestricted foreign queries

There are two terminating environments such that no agent, computable or otherwise, is optimal in both under \(O_{\mathrm{oracle}}\).

#### Proof

Choose one binary query \(q\), distinct from the environments’ own descriptions. Define

\[
E_0:\quad U(E_0,A)=\mathbf 1[A(q)=0],
\]

\[
E_1:\quad U(E_1,A)=\mathbf 1[A(q)=1].
\]

Each environment has optimal value \(1\), attained by a constant agent. No agent attains \(1\) in both. \(\square\)

This is a cross-problem consistency contradiction. It requires neither self-reference nor undecidability.

Under an \(O_{\mathrm{const}}\) intervention that changes only the current problem’s own action and freezes the foreign response, this particular argument disappears: the foreign response is then outside the permitted intervention.

### 3.2 Global totality plus fixed constants

### Theorem 3 — The fixed-copy diagonal

If admissible agents are globally total computable functions and arbitrary fixed computable algorithms may occur in environments, no agent is universally optimal—even for deterministic, binary, rational-valued environments whose evaluated-agent queries are confined to their own description.

#### Proof

Fix a candidate \(T\). Construct \(E_T\) containing a fixed algorithm \(g_0=T\). Let \(d=d(E_T)\). It computes

\[
c=g_0(d),
\]

obtains the evaluated agent’s actual action \(a\), and pays

\[
u(a)=\mathbf 1[a\ne c].
\]

The fixed algorithm \(g_0\) does not change when the evaluated agent changes.

Because \(T\) is globally total, \(g_0(d)\) terminates. Thus the environment terminates under either actual action.

The agent \(T\) takes action \(c\) and receives \(0\). A globally total agent that takes \(1-c\) at \(d\) receives \(1\). \(\square\)

This works under \(O_{\mathrm{const}}\). It also works under \(O_{\mathrm{oracle}}\) when \(g_0\) is an ordinary fixed program rather than a designated oracle call.

Your transparent/opaque-box construction is the same mechanism with different payoffs. It is the construction at the start of Skalse’s paper, with global totality and self-description supplying the missing implementation conditions. [arxiv.org](https://arxiv.org/pdf/2101.00280v1?utm_source=chatgpt.com)

### Why this does not contradict Theorem 1

The optimizer \(T^*\) in Theorem 1 is only promise-total.

Its attempted diagonal environment contains an embedded call to \(T^*(d(E_{T^*}))\). In this particular construction, evaluating the environment invokes the same optimization again, causing an infinite regress. The environment therefore fails the universal table-termination promise.

The positive theorem does not supply a globally total extension of \(T^*\).

### What the recursion theorem supplies

In a programming formalism with no built-in “own description” parameter, Kleene’s recursion theorem supplies the required self-description construction. It produces a program with specified behavior involving its own index; it does not prove that this behavior terminates. A modern complete statement and proof appear in Moschovakis, p. 190. [math.ucla.edu](https://www.math.ucla.edu/~ynm/papers/1602-002-1.pdf?utm_source=chatgpt.com)

There is no inconsistent equation such as \(a=1-a\) here. The actual agent and its fixed copy agree; the payoff simply rewards disagreement.

Nor is this a contradiction with the earlier matrix model. A source description can encode a computation involving \(T\) without supplying the result of that computation. Once the fixed copy’s answer is known, the corresponding fixed-environment matrix has an ordinary maximizer. The source-reading agent need not be able to select it uniformly while remaining globally total.

### A further \(O_{\mathrm{const}}\) baseline

If an oracle environment calls the same agent twice on \(d\), treating one call as prediction \(p\) and the other as action \(a\), and pays

\[
\mathbf 1[a\ne p],
\]

then:

- under coherent oracle substitution, every agent receives \(0\), so every agent is optimal;
- under an intervention changing only \(a\), every agent has an improving deviation.

Thus anchored \(O_{\mathrm{const}}\) can already be unsatisfiable in one environment. This is the familiar ratifiability obstruction, not a new computability result.

---

## 4. The strongest clean computational impossibility

This result avoids both baseline constructions.

### Theorem 4 — No computable exact optimizer for bounded stochastic programs

There is no computable exact expected-payoff optimizer for all almost-surely terminating binary-choice program environments, even if:

- the optimizer need halt only on valid inputs;
- realized payoffs lie in \(\{0,1\}\);
- there are no predictors or embedded agent copies;
- the agent is queried only on its own description;
- all expected values are uniformly computable;
- the environments have finite expected simulation time.

#### Proof

Let \((\varphi_e)\) be an effective enumeration of partial computable functions, and define

\[
K_b=\{e:\varphi_e(e)\text{ halts with output }b\},
\qquad b\in\{0,1\}.
\]

For each \(e\), construct \(E_e\):

1. Obtain the action \(a\in\{0,1\}\).
2. Draw \(N\in\mathbb N\) with
   \[
   \Pr(N=n)=2^{-n-1}.
   \]
3. Simulate \(\varphi_e(e)\) for \(N\) steps.
4. Pay \(1\) if that simulation observes output \(a\); otherwise pay \(0\).

Every environment terminates almost surely. Every simulation is bounded.

If \(e\in K_b\), with halting time \(t\), then

\[
V_e(b)=\Pr(N\ge t)=2^{-t}>0,
\qquad
V_e(1-b)=0.
\]

If no binary output occurs, both values are \(0\).

Suppose a promised-total exact optimizer existed. Then

\[
f(e)=T(d(E_e))
\]

would be a total computable binary function satisfying

\[
e\in K_b\implies f(e)=b.
\tag{3}
\]

Take an index \(e\) for the total program

\[
x\longmapsto 1-f(x).
\]

Then

\[
\varphi_e(e)=1-f(e).
\]

Condition (3) requires \(f(e)=1-f(e)\), a contradiction. \(\square\)

### What this proves

The failure is **exact selection**, not inability to approximate expected values.

After \(n\) simulation steps, unresolved expected payoff is at most \(2^{-n}\). Hence these expectations are uniformly computable reals with an explicit error bound.

What cannot be computed uniformly is which action belongs to the exact argmax when arbitrarily small advantages and genuine ties are both allowed.

### Positive replacements

For a finite policy set with uniformly computable values:

- **\(\varepsilon\)-optimality:** approximate each value within \(\varepsilon/3\), then maximize the approximations.
- **A promised unique maximizer:** refine enclosing intervals until one policy’s lower bound exceeds every other policy’s upper bound.
- **Exactly comparable values:** use ordinary finite maximization.

For bounded, almost-surely terminating programs with effective finite branching, expectation approximation can also be obtained by exploring executions until the remaining probability mass is small enough.

This theorem establishes a true, nontrivial version of your thesis on an especially fair class. It is a standard recursion-theoretic exact-selection obstruction, rather than a new conflict among decision theories.

---

## 5. K2: syntactic substitution

### 5.1 When syntax recognition suffices

Suppose the world is represented by a template with designated agent slots, and:

1. syntactic replacement changes exactly those slots;
2. every slot uses the same fixed owned-input namespace;
3. all other programs are constants;
4. every finite-policy replacement terminates with an exactly comparable payoff.

Then compilation from oracle calls to those slots preserves every counterfactual execution:

\[
U_{\mathrm{syn}}(E,T;A)
=
U_{\mathrm{oracle}}(E,A).
\]

Theorem 1 applies.

This is a substantive positive answer: the rule can evaluate arbitrary code implementing the environment without recognizing every consequence of its action analytically. It can execute the stipulated replacements.

It is also a restricted answer: the representation identifies the agent slots.

### 5.2 A differently encoded equivalent copy defeats literal substitution

Fix a globally total \(T\). Construct a closed program \(g\) such that

\[
g(x)=T(x)
\quad\text{for all }x,
\]

but whose representation contains no eligible occurrence of the exact target program.

For example, use an independently encoded machine implementation in a typed, atomic component. Merely adding a wrapper is insufficient if the original program remains an eligible nested occurrence.

Let the environment pay

\[
\mathbf 1[a\ne g(d(E))].
\]

Literal substitution changes the live agent but leaves \(g\) unchanged. Thus \(T\) receives \(0\), while an opposite-action agent receives \(1\).

Every computation terminates.

This proves the requested syntactic-copy failure. It is still the fixed-constant diagonal. Extending the matching rule to recognize this copy addresses this example, but raises the issues in the next section.

### 5.3 Syntactic substitution and extensional fairness

Literal matching can violate strong \(F_{\mathrm{ext}}\): two extensionally equal reference agents with different source code can produce different replacement masks.

A slot-based representation avoids that problem by preserving the agent role independently of the code currently occupying it. Literal code equality and role identity should not be conflated.

---

## 6. K3: extensional counterfactuals

### 6.1 A precise semantics

Let \(E\) contain a finite list of typed, atomic program components \(g_j\). Fix comparison domains \(X_j\) and reference function \(t\). Define

\[
S_t(E)=\{j:g_j|_{X_j}=t|_{X_j}\}.
\]

To evaluate \(A\), replace exactly these components by \(A\), and then execute the resulting environment:

\[
U_{\mathrm{ext}}(E,t;A).
\]

Matching occurs once, before replacement. Component boundaries and the description supplied to the agent remain fixed.

We also require every permitted counterfactual execution to terminate. Termination of the original environment alone does not imply this closure property.

The principal choices are:

- **Local equality:** \(X_j\) is a specified finite input set, or a frozen baseline trace.
- **Global equality:** \(X_j\) is the entire input domain.

For baseline-trace matching, treatment of uncalled components must also be stipulated. All witnesses below call every relevant component, so empty comparison sets do not affect them.

### 6.2 Matching against the counterfactual trace can be undefined

Suppose

\[
t(0)=t(1)=0,\qquad g(0)=0,\quad g(1)=1,
\]

and \(A(0)=1\).

The environment calls \(g(0)\), then calls \(g(1)\) exactly when the first result is \(1\).

Now require replacement iff the original \(g\) agrees with \(t\) on the inputs used in the resulting counterfactual execution.

- Without replacement, only input \(0\) is used. Agreement holds, so replacement is required.
- With replacement, inputs \(0\) and \(1\) are used. Agreement fails at \(1\), so replacement is forbidden.

There is no consistent replacement set, although every candidate execution terminates.

Thus “on the inputs it is run on” must specify **which execution determines those inputs**.

### 6.3 Local equality is computable—but can make optimality impossible

Equality of total programs on a specified finite set is decidable by running the relevant computations. Rice’s theorem is not needed.

Nevertheless:

### Theorem 5 — Local equality can leave no optimal agent

Under frozen matching on the single actual input \(d(E)\), there is a terminating \(F_{\mathrm{self}}\), \(F_{\mathrm{ext}}\) environment for which no deterministic agent satisfies anchored optimality.

#### Proof

The environment contains

\[
g_0\equiv0,\qquad g_1\equiv1.
\]

It calls both at \(d(E)\), queries the live agent there, and pays \(1\) iff the two component outputs agree.

Let \(a=t(d(E))\). Exactly \(g_a\) matches \(t\) on \(\{d(E)\}\).

The actual outputs are \(0,1\), so

\[
U_{\mathrm{ext}}(E,t;t)=0.
\]

Take \(A\equiv1-a\). Replacement changes \(g_a\) to \(A\), leaving \(g_{1-a}\) fixed. Both now return \(1-a\), so

\[
U_{\mathrm{ext}}(E,t;A)=1.
\]

Every reference agent therefore has an improving deviation. \(\square\)

This is not an undecidability theorem. It is a pathology of identifying computations through accidental agreement on one input. It should not be advertised as a theorem about FDT without that identification stipulation.

### 6.4 Rematching does not compose

Even global matching has a separate problem.

Start with components \(g_0\equiv0,g_1\equiv1\) and reference \(t\equiv0\).

- Replace \(t\) by \(a\equiv1\): both components become \(1\).
- Recompute matches relative to \(a\), then replace \(a\) by \(b\equiv0\): both become \(0\).

Direct replacement of \(t\) by \(b=t\) leaves the original pair \((0,1)\).

Hence

\[
R_{a\to b}(R_{t\to a}(E))
\ne R_{t\to b}(E).
\]

Keeping an original dependency label attached to the first component repairs composition. But that label supplies additional structure; equality of the current functions does not recover it.

### 6.5 Global equality leaves the fixed-constant diagonal intact

### Theorem 6 — Atomic global equality does not remove the baseline

For globally total computable agents, global-equivalence replacement of atomic components admits no universal optimizer when fixed algorithms are allowed.

#### Proof

Fix \(T\), and compile an atomic program

\[
h_T(x)=1-T(x).
\]

Construct an environment paying

\[
\mathbf 1[a=h_T(d(E))].
\]

Since \(h_T\) disagrees with \(T\) everywhere, it is not replaced. Actual \(T\) receives \(0\); an opposite-action competitor receives \(1\). All calls terminate. \(\square\)

The diagnostic point is:

\[
\text{“depends functionally on }T\text{”}
\quad\ne\quad
\text{“is extensionally equal to }T\text{.”}
\]

If the intended counterfactual transforms \(1-T\) into \(1-A\), it transports dependence through a program context. That is a stronger operation than equality-based replacement.

### 6.6 A valid halting-to-optimality reduction

The anticipated undecidability route can also be made rigorous, with explicit qualifications.

First, the equality direction in the proposed lead needs correction. For a uniformly total family \(g_e\) and fixed total \(T\), non-equivalence has a finite witness input. Thus

\[
\{e:g_e=T\}
\]

is co-c.e. One cannot uniformly make equality hold exactly when an arbitrary machine halts. The useful construction makes equality hold exactly when it **does not** halt.

### Theorem 7 — Global matching can make optimality decide halting

Assume atomic global matching, frozen descriptions, and globally total binary agents.

Choose a decidable description-prefix class \(P\) containing all environments constructed below, with arbitrarily long inputs outside \(P\).

Fix a hypothetical universal optimizer \(T\). Define

\[
g_e(x)=
\begin{cases}
T(x),&x\in P,\\
1-T(x),&x\notin P\text{ and machine }e
                   \text{ halts within }|x|\text{ steps},\\
T(x),&\text{otherwise}.
\end{cases}
\]

Each \(g_e\) is total, and

\[
g_e=T
\iff e\text{ does not halt}.
\tag{4}
\]

Construct \(E_e\), with \(d_e=d(E_e)\in P\), to obtain action \(a\), compute \(b=g_e(d_e)\), and pay

\[
u(a,b)=2(1-b)+a.
\]

Its payoff table is

| \(b\) | Action \(0\) | Action \(1\) |
|---|---:|---:|
| \(0\) | 2 | 3 |
| \(1\) | 0 | 1 |

Because \(d_e\in P\),

\[
g_e(d_e)=T(d_e)
\]

in both halting cases.

#### Proof

If \(e\) does not halt, global matching replaces \(g_e\) by the candidate \(A\). Thus \(b=a\), and the two values are \(2\) and \(1\). Optimality requires \(T(d_e)=0\).

If \(e\) halts, \(g_e\) remains fixed. Holding either value of \(b\) fixed, action \(1\) pays one more than action \(0\). Optimality requires \(T(d_e)=1\).

Therefore the computable function \(e\mapsto T(d_e)\) decides halting, contradiction. \(\square\)

Every actual and counterfactual execution terminates, and every payoff is rational.

However:

- it uses global equality, rather than equality only at actual inputs;
- it uses atomic components compiled using \(T\);
- it satisfies executed-query locality, but global matching violates strong kernel locality;
- it remains in a class already admitting fixed-constant diagonals.

It is a valid reduction. It is not a semantics-independent impossibility arising from the mere presence of embedded programs.

Under local matching, \(g_e\) always matches at \(d_e\), so action \(0\) always wins and the reduction disappears.

### 6.7 Positive subclasses and “largest natural subclass”

A broad positive theorem is available whenever the description supplies a **reference-independent, effective counterfactual evaluator**

\[
V(e,\pi)
\]

on a finite policy space, all evaluations terminate, and values are exactly comparable. Finite maximization applies regardless of whether the evaluator internally uses source analysis, simulation, or proofs.

For globally total implementations, useful representations include:

- finite circuits;
- explicitly clocked programs with stipulated timeout behavior;
- descriptions carrying checkable certificates sufficient to justify the required evaluations.

But two qualifications are essential:

1. **Clocks do not decide global equivalence.** Even a program that simulates machine \(e\) for only \(|x|\) steps can equal zero on every input exactly when \(e\) never halts.
2. **“Replace iff \(S\) proves equality” changes the semantics.** It agrees with true global matching only on a class with complete certified matching information. Positive equality certificates alone do not show that uncertified components are unequal.

There is no specified mathematical ordering of “natural subclasses.” For reference-independent problems with disjoint owned inputs, every proper decidable solvable description class can be enlarged by one further solvable instance, hard-coding an optimal policy there. Thus no largest proper class exists under that particular effective-subclass ordering.

Conversely, the entire class of terminating rational-valued finite-policy templates is a legitimate maximal **promise domain for that representation**. An unqualified “there is no largest subclass” would also be wrong.

---

## 7. K4: logical counterfactuals

Three different questions should be separated:

1. Can proofs establish the values of independently specified counterfactual programs?
2. Can material implications about the actual agent serve as counterfactual values?
3. Can logical uncertainty supply useful finite-time estimates?

### 7.1 A positive computable proof-based rule

Fix a sound, effectively axiomatized arithmetic theory \(S\) strong enough to verify finite program traces.

For an environment in Theorem 1’s class, enumerate proofs until, for every policy \(\pi\), a statement

\[
\operatorname{Eval}(e,\pi)=r_\pi
\]

has been proved for some rational \(r_\pi\). Then maximize the \(r_\pi\).

This is promise-total and optimal:

- every actual terminating computation has a finite trace;
- that trace has a proof in \(S\);
- soundness makes the proved value correct;
- only finitely many such proofs are needed.

**A fixed proof system’s incompleteness does not prevent it from eventually verifying every particular terminating finite computation.** What it may fail to prove is a uniform termination statement or a global equivalence.

This proof-based optimizer uses the same counterfactual evaluator as the simulation optimizer. It does not infer a new intervention semantics from proof search alone.

### 7.2 Why material implication is problematic

Let

\[
H_a=[T(d(E))=a],\qquad Y_u=[U(E,T)=u].
\]

If \(S\vdash\neg H_a\), then

\[
S\vdash H_a\to Y_u
\]

for every \(u\). These implications cannot all be distinct correct payoff values.

Moreover, for an actually terminating computable agent, a sufficiently strong arithmetic theory can verify its finite execution. Logical omniscience about that execution therefore makes the other action antecedents false. Conditioning a coherent probability distribution over models of that theory on those antecedents is then undefined.

### 7.3 A fully computable 5-and-10 failure

Here is a complete reconstruction of the spurious-proof mechanism.

Let \(E_0\) pay the numerical action selected from \(\{5,10\}\). Fix an effectively axiomatized theory \(S\) satisfying the standard derivability conditions for Löb’s theorem.

Use self-reference to define \(T\):

- on descriptions other than \(d(E_0)\), return \(10\);
- on \(d(E_0)\), enumerate \(S\)-proofs until finding a proof of
  \[
  \psi=
  \bigl(T(d(E_0))=5\to U(E_0,T)=5\bigr)
  \wedge
  \bigl(T(d(E_0))=10\to U(E_0,T)=0\bigr);
  \]
- then return \(5\).

Termination of the exceptional search is initially unproved.

Write

\[
q=[T(d(E_0))=5].
\]

The program and environment establish

\[
S\vdash q\to\psi.
\]

Provability distribution gives

\[
S\vdash \Box_S q\to\Box_S\psi.
\]

Formalizing the proof enumeration gives

\[
S\vdash\Box_S\psi\to q.
\]

Hence

\[
S\vdash\Box_S q\to q.
\]

Löb’s theorem yields \(S\vdash q\). Combining this finite proof with \(S\vdash q\to\psi\) supplies an actual proof of \(\psi\). The search therefore terminates and returns \(5\).

Thus \(T\) is globally total but receives \(5\), while constant \(10\) receives \(10\). \(\square\)

This refutes the displayed material-implication selection scheme. It does not refute every logical-counterfactual procedure.

Benson-Tilsen’s *UDT with Known Search Order*, §2, analyzes this mechanism. His full classification, Theorem 4.5 and Corollary 4.6, concerns a specified transparent-universe model, proof-search order, and provability oracle; it should not be quoted as a theorem about every computable proof-based agent. [intelligence.org](https://intelligence.org/files/UDTSearchOrder.pdf?utm_source=chatgpt.com)

### 7.4 A precise partial logical-counterfactual semantics

One verified proposal is Fallenstein’s modal “third-person counterfactual” semantics.

Let \((A_i)\) and \((U_j)\) be provably mutually exclusive and exhaustive modal action and outcome vectors. Define

\[
L(i)=u_j
\quad\text{iff}\quad
GL\vdash A_i\to U_j
\quad\text{and}\quad
GL\nvdash\neg A_i.
\tag{5}
\]

The outcome is unique when defined. It is undefined if the action is provably impossible or no outcome is determined.

A pair is **fully informative** when (5) is defined for every action. On that domain, modal UDT’s descending-outcome proof search selects an \(L\)-maximizing action: it reaches a proof for an optimal outcome and cannot stop at a worse outcome first. This is optimality relative to the specified logical counterfactuals, not automatically relative to physical agent replacement. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebf/third-person-counterfactuals?utm_source=chatgpt.com)

This semantics avoids silently assigning arbitrary outcomes to a refuted action. It does so by becoming partial. In the computable 5-and-10 construction above, the refuted alternative is rejected rather than correctly assigned its ordinary intervention payoff.

### 7.5 The verified modal impossibility

Fallenstein considers fixed, fully modalized decision schemata \(T(\mathbf u)\), and problems satisfying

\[
GL\vdash
(\mathbf a\leftrightarrow\mathbf b)
\to
(P(\mathbf a)\leftrightarrow P(\mathbf b)).
\]

Every such fixed theory with at least two actions and outcomes fails on some provably extensional problem.

A compact reconstruction is: let \(B=T(\chi^{(2)})\), where \(\chi^{(2)}\) is the constant second-best outcome. Define \(P_T(a)\) to reward \(a\ne B\) and otherwise give the second-best outcome. Then \(P_T(B)=\chi^{(2)}\); modal fixed-point uniqueness makes \(B\) the theory’s action. A different constant action wins. The action variables occur outside boxes, establishing extensionality. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic?utm_source=chatgpt.com)

This is a fixed-environment-constant diagonal in a modal model. Its agent class is not the class of all total computable programs on arbitrary source descriptions.

### 7.6 The verified modal optimality theorem

For every finite provably extensional modal problem \(P\), let \(f(i)\) be the true outcome under constant action \(i\). Set

\[
\varphi=\bigwedge_i P_{f(i)}(\chi^{(i)}).
\]

Fallenstein proves that modal UDT using \(PA+\varphi\) selects the first optimal action. Extensionality and \(\varphi\) prove that action’s correct implication; any earlier successful query would, by soundness, establish an equally good or better actual outcome.

The quantifiers are

\[
\boxed{\forall P\ \exists\varphi,}
\]

not a single fixed proof system for all \(P\). The displayed general proof-query algorithm uses a halting oracle. [lesswrong.com](https://www.lesswrong.com/posts/5bd75cc58225bf0670374e8f/an-optimality-result-for-modal-udt?utm_source=chatgpt.com)

A stronger comparison result says that it suffices for the proof system to establish a competitor’s action and achieved outcome; modal UDT then does at least as well on a provably extensional problem. Again, proof strength is an explicit hypothesis. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ea9/improving-the-modal-udt-optimality-result?utm_source=chatgpt.com)

GL itself is decidable. These observations should not be compressed into the false claim that every restricted modal computation is noncomputable.

### 7.7 Logical induction

Logical induction supplies computable, improving assessments of logical sentences. It does not by itself specify which counterfactual program or intervention to evaluate.

Its Theorem 4.6.1 states that changing finitely many market days preserves logical induction. Consequently, the logical-induction criterion alone cannot force exact correctness of a particular finite-time belief or resulting decision. This does not prove that every decision procedure using logical induction fails a given simple problem. [arxiv.org](https://arxiv.org/pdf/1609.03543?utm_source=chatgpt.com)

One can use logical induction to estimate the outcomes of policy-substituted programs. Exact universal optimality on the stochastic class of Theorem 4 remains impossible for any computable resulting rule.

---

## 8. Implications between the optimality notions

There is no general implication chain

\[
O_{\mathrm{const}}
\Rightarrow O_{\mathrm{oracle}}
\Rightarrow O_{\mathrm{syn}}
\Rightarrow O_{\mathrm{ext}}.
\]

Replacing more components does not make optimality logically stronger or weaker.

### A general nonimplication lemma

Suppose two conventions produce baseline pattern \(z\), but replacing binary baseline agent \(0\) by agent \(1\) produces different patterns \(v,w\). Set

\[
u(z)=1,\qquad u(v)=0,\qquad u(w)=2.
\]

The baseline agent is optimal under the first convention and suboptimal under the second. Interchanging the payoffs of \(v,w\) proves the reverse nonimplication.

For example, a common typed representation can produce:

| Evaluation | Actual action | Additional oracle call | Extra literal copy | Equivalent encoded copy |
|---|---:|---:|---:|---:|
| Baseline | 0 | 0 | 0 | 0 |
| Const alternative | 1 | 0 | 0 | 0 |
| Oracle alternative | 1 | 1 | 0 | 0 |
| Syntactic alternative | 1 | 1 | 1 | 0 |
| Extensional alternative | 1 | 1 | 1 | 1 |

Assigning payoffs to these patterns gives both nonimplications for every distinct pair among the first four notions.

The complete comparison is therefore:

| Pair | General relationship |
|---|---|
| Const / oracle | Neither implies the other |
| Const / syntactic | Neither implies the other |
| Const / extensional | Neither implies the other |
| Oracle / syntactic | Equal under a slot-preserving compilation; otherwise neither |
| Oracle / extensional | Equal when the extensional operation selects exactly the designated dependencies; otherwise neither |
| Syntactic / extensional | Equal when replacement masks coincide; otherwise neither |
| Logical / const | No unqualified implication; specify the logical kernel and its translation |
| Logical / oracle | Ground policy-proof semantics can coincide with oracle evaluation; material-implication semantics need not |
| Logical / syntactic | Coincide only when the proof semantics verifies that same substitution operation |
| Logical / extensional | Coincide only when the proof semantics establishes that same matching and transport rule |

For the last four pairs, the label \(O_{\mathrm{log}}\) alone does not denote one predicate. Equation (5) is partial; ground policy proofs evaluate an independently supplied substitution; logical-induction scores are finite-time estimates. Treating these as one fifth total payoff function would conceal the main issue.

These are pointwise comparisons. At the level of universal theories, a criterion that no theory satisfies entails other properties only vacuously.

---

## 9. K6: Fernando’s two readings of Anti-Newcomb

Use the exclusive-box version in the prompt. Scale the transparent amount to \(1\) and the opaque amount to \(2\).

Let \(C\) mean transparent and \(O\) opaque. With coherent self-prediction, the causal matrix is

\[
M_{\mathrm{Anti}}
=
\begin{pmatrix}
1&2\\
1&0
\end{pmatrix},
\]

with rows and columns ordered \((C,O)\).

### Solve-then-apply: fixed-copy evaluation

The predictor computes the fixed original \(T(d)\).

- If \(T(d)=C\), the opaque box is full: \(T\) gets \(1\), while an alternative opaque-taking agent gets \(2\).
- If \(T(d)=O\), the opaque box is empty: \(T\) gets \(0\), while a transparent-taking agent gets \(1\).

This is \(O_{\mathrm{const}}\), or genuine agent replacement in an environment containing an unchanged algorithm constant.

### Identity: the linked computation changes too

If both the actual and predicted calls change coherently, the relevant values are

\[
V(C)=1,\qquad V(O)=0.
\]

Transparent is uniquely optimal.

This is obtained under:

- oracle substitution when both calls use the same oracle;
- syntactic substitution when both are designated matching occurrences;
- extensional substitution when the chosen matching semantics links them;
- a functional template explicitly transporting the dependence.

### Is Anti-Newcomb isomorphic to Newcomb?

For ordinary Newcomb with prize \(2\) and two-box bonus \(1\),

\[
M_{\mathrm{Newcomb}}
=
\begin{pmatrix}
2&3\\
0&1
\end{pmatrix},
\]

ordered as one-box, two-box.

These full problems are **not** isomorphic under action relabeling and positive affine utility transformation. Ordinary Newcomb has one column strictly dominating the other in every row. Exclusive Anti-Newcomb does not. That property is preserved by such isomorphisms.

If one retains only the diagonal rankings, both are strictly ordered binary choices, and a relabeling can identify their preferred actions. That is a much weaker equivalence.

Thus:

| Claim | Verdict |
|---|---|
| Both can be evaluated by coherent functional substitution | True under a specified dependency interpretation |
| Their full causal matrices are isomorphic | False for these versions |
| Raw source alone forces FDT to treat the fixed program as a changing copy | Not established by any of the definitions given |
| An unspecified “identity” counterfactual settles the issue | Undefined until the transport rule is fixed |

FDT’s paper itself flags fixed-copy “act differently from Fiona” examples as a difficulty for formalizing fairness. Your \(F_{\mathrm{const}}\) permission admits cases that its intended informal fairness standard seeks to exclude. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com)

---

## 10. K5: resource bounds

Finite clocks or circuit descriptions can support globally total optimizers: every required evaluation has a finite bound.

They do not imply that optimization fits the same resource bound as one environment execution. With many binary policy coordinates and a circuit payoff, finding an exact maximizing policy can encode SAT: reward \(1\) exactly for satisfying assignments. A polynomial-time exact policy optimizer for all such circuits would decide SAT in polynomial time.

Nor do per-input runtime bounds decide global program equality. The bounded-simulation construction in Section 6.6 already shows why.

Critch’s bounded Löb results provide positive cooperation theorems for specified proof-responsive program families under proof-length and growth assumptions. They do not establish universal optimality in the present environment class. [arxiv.org](https://arxiv.org/pdf/1602.04184?utm_source=chatgpt.com)

---

## 11. K7: verdict table

A literal \(2\times5\times4\) Cartesian table would include undefined combinations: oracle substitution presupposes oracle ports; extensional substitution presupposes component and matching conventions; the fairness conditions overlap.

Here is the table of coherent cases.

| Access and criterion | Fairness/domain | Computable universal optimum? | Status |
|---|---|---|---|
| OR, oracle replacement | Self-only, finite policies, terminating exact-rational evaluations; promise-total agents | **Yes** | Theorem 1; constructive finite optimization |
| OR, oracle replacement | Same representation, globally total agents, arbitrary fixed constants | **No** | Fixed-copy diagonal; baseline |
| OR, oracle replacement | Arbitrary foreign queries | **No**, even without computability | Two conflicting shared-query requirements |
| OR, actual-action-only intervention | Self-prediction held fixed | **No** in one environment | Ratifiability baseline |
| EM, fixed constants | Self-only evaluated-agent dependence; globally total agents | **No** | Skalse-type diagonal |
| EM, syntactic substitution | Complete designated slots, finite exact evaluations; promise-total agents | **Yes** | Compilation of Theorem 1 |
| EM, literal syntactic matching | Unmarked equivalent copies allowed; globally total agents | **No** | Encoded-copy diagonal |
| EM, frozen local-equivalence matching | Atomic components; self-only and extensional kernel | **No**, even abstractly | Two-constant no-solution theorem |
| EM, global-equivalence matching | Atomic components, fixed constants, globally total agents | **No** | Complement diagonal; also a valid halting reduction |
| Either, supplied dependency evaluator | Finite exact evaluations, checkable sufficient certificates or clocks | **Yes**, globally total on the certified language | Effective representation restores optimization |
| Either, ordinary stochastic evaluation | Self-only, no predictors, bounded finite-support rewards, almost-sure termination | **No**, even promise-total | Exact-selection impossibility |
| Proof-based ground policy evaluation | Terminating finite-policy rational templates | **Yes**, promise-total | Search for proofs of finite execution results |
| Fixed modal decision schema | Provably extensional modal problems with constants | **No** | Fallenstein’s established modal diagonal |
| Modal UDT with problem-specific true axioms | A given provably extensional modal problem | **Yes for that problem** | \(\forall P\exists\varphi\), not one universal proof system |
| Logical-induction-based estimates | A fixed finite decision time | **No guarantee from logical induction alone** | Finite perturbations preserve the criterion |
| Unspecified logical identity of arbitrary computations | Unannotated source | **Not a defined question yet** | Missing counterfactual transport semantics |

The stochastic row is the strongest negative result here that survives removing predictors, fixed-agent diagonals, and disputed dependence semantics.

---

## 12. Verified literature and novelty

The following identifies the sources actually relevant to the conclusions.

| Citation | Verified location and relevance |
|---|---|
| **H. G. Rice, “Classes of Recursively Enumerable Sets and Their Decision Problems,” Transactions of the AMS 74 (1953), 358–366. DOI: 10.1090/S0002-9947-1953-0053041-6.** | Bibliographic record verified. Rice concerns nontrivial semantic properties of partial computable functions/r.e. sets. The total-program and finite-input variants require the separate arguments above. Original theorem numbering was not verified. [ams.org](https://www.ams.org/journals/tran/1953-074-02/S0002-9947-1953-0053041-6/home.html?utm_source=chatgpt.com) |
| **S. C. Kleene, “On notation for ordinal numbers,” Journal of Symbolic Logic 3 (1938), 150–155.** | Original attribution checked through **Yiannis N. Moschovakis, “Kleene’s Amazing Second Recursion Theorem,” Bulletin of Symbolic Logic 16(2) (2010), 189–239**, especially p. 190. Moschovakis locates the original result in the final two lines of Kleene’s §2. [math.ucla.edu](https://www.math.ucla.edu/~ynm/papers/1602-002-1.pdf?utm_source=chatgpt.com) |
| **Moshe Tennenholtz, “Program equilibrium,” Games and Economic Behavior 49(2) (2004), 363–373. DOI: 10.1016/j.geb.2004.02.002.** | The author’s institutional abstract verifies the feasible-and-individually-rational payoff characterization. This concerns equilibrium in a program-submission game, not one rule optimal against every environment. The original article body was unavailable. [Israel Institute of Technology](https://cris.technion.ac.il/en/publications/program-equilibrium/?utm_source=chatgpt.com) |
| **Mihály Bárász, Paul Christiano, Benja Fallenstein, Marcello Herreshoff, Patrick LaVictoire, and Eliezer Yudkowsky, “Robust Cooperation in the Prisoner’s Dilemma: Program Equilibrium via Provability Logic,” arXiv:1401.5577 (2014; corrected version 2021).** | Theorem 3.1 proves FairBot self-cooperation; Theorem 4.8 preserves behavioral equivalence defined through PA-provable equivalence against every opponent. §5 discusses obstacles to optimality. These are not arbitrary semantic-equivalence guarantees for total programs. [arxiv.org](https://arxiv.org/pdf/1401.5577?utm_source=chatgpt.com) |
| **Andrew Critch, “A Parametric, Resource-Bounded Generalization of Löb’s Theorem, and a Robust Cooperation Criterion for Open-Source Game Theory,” Journal of Symbolic Logic 84(4) (2019), 1368–1381. DOI: 10.1017/jsl.2017.42.** | Journal metadata verified. Exact theorem text checked in the 2016 preprint, **“Parametric Bounded Löb’s Theorem and Robust Cooperation of Bounded Agents,” arXiv:1602.04184**: Theorem 3, §5; Theorem 4, §6. Its “fairness” is proof responsiveness, not the fairness definition in this question. [Cambridge Core](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/parametric-resourcebounded-generalization-of-lobs-theorem-and-a-robust-cooperation-criterion-for-opensource-game-theory/16063EA7BFFEE89438631B141E556E79?utm_source=chatgpt.com) |
| **Nate Soares and Benja Fallenstein, “Toward Idealized Decision Theory,” arXiv:1507.01986 (2015), extended AGI-2015 paper; originally MIRI Report 2014–7.** | §5 discusses logical counterfactuals and proof-based UDT; the general proof-query procedure explicitly requires a halting oracle. It presents a research program, not a universal computable optimality theorem. [arxiv.org](https://arxiv.org/pdf/1507.01986?utm_source=chatgpt.com) |
| **Tsvi Benson-Tilsen, “UDT with Known Search Order,” MIRI Technical Report 2014–4, August 22, 2014.** | §2, pp. 2–3: spurious counterfactuals. Theorem 4.5, p. 6, and Corollary 4.6, pp. 6–7: classification within its specified search-order model. The author is Tsvi Benson-Tilsen. [intelligence.org](https://intelligence.org/files/UDTSearchOrder.pdf?utm_source=chatgpt.com) |
| **Benja/Benya Fallenstein, “‘Evil’ decision problems in provability logic”; “An optimality result for modal UDT”; “Improving the modal UDT optimality result.”** | Author posts with proofs, displayed dates January 10, 2015; November 15, 2014; November 23, 2014. The migrated dates do not consistently reflect the posts’ stated sequence. These provide the modal negative theorem, problem-specific-axiom theorem, and competitor-relative strengthening. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic?utm_source=chatgpt.com) |
| **Scott Garrabrant, Tsvi Benson-Tilsen, Andrew Critch, Nate Soares, and Jessica Taylor, “Logical Induction,” arXiv:1609.03543 (2016; checked v5, 2020).** | Theorem 3.6.1: computable existence. Theorem 4.6.1, p. 36: closure under finite perturbations. These are epistemic results, not exact one-shot decision optimality. [arxiv.org](https://arxiv.org/pdf/1609.03543?utm_source=chatgpt.com) |
| **Eliezer Yudkowsky and Nate Soares, “Functional Decision Theory: A New Theory of Instrumental Rationality,” arXiv:1710.05060 (2017; revised 2018).** | Its evaluation uses a supplied subjunctive-dependency graph; deriving that structure is not solved by the formalism. Page 29, footnote 15, discusses fixed-copy fairness problems. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com) |
| **Joar Skalse, “A General Counterexample to Any Decision Theory and Some Responses,” arXiv:2101.00280 (2021).** | Opening construction and subsequent discussion of fairness and problem equivalence directly precede the fixed-copy result here. [arxiv.org](https://arxiv.org/pdf/2101.00280v1?utm_source=chatgpt.com) |
| **Jan Leike and Marcus Hutter, “Bad Universal Priors and Notions of Optimality,” COLT, PMLR 40 (2015), 1244–1259.** | Theorem 7 concerns dogmatic priors; Theorem 18 shows that every policy is Pareto optimal on their broad environment class. This is a different history-interaction model, but reinforces the need to distinguish exact universal dominance from weaker optimality criteria. [proceedings.mlr.press](https://proceedings.mlr.press/v40/Leike15.html?utm_source=chatgpt.com) |

**Verification limits.** The original full texts of Rice, Kleene, and Tennenholtz were not successfully retrieved; I have not invented internal theorem numbers for them. Their bibliographic records were checked, and Kleene’s theorem was checked in Moschovakis’s complete modern treatment. Automatic approval review rejected a direct shell-download fallback under the session’s network restrictions; the research continued through the permitted web tools.

---

## 13. Final thesis

A defensible replacement for the original thesis is:

> **No computable rule can exactly maximize expected payoff on every source-described, almost-surely terminating binary decision problem with bounded finite-support rewards—even when all dependence on the agent is through its own action, there are no predictors or embedded agent copies, and expected values are uniformly computable.**

This is true by Theorem 4. It is nontrivial, but its mathematical obstruction is established computability theory.

A second true statement is:

> **No globally total computable rule is optimal on all terminating source-described environments that permit arbitrary fixed computable algorithm constants.**

This is the fixed-copy diagonal. Its mechanism is already present in Skalse and in Fallenstein’s modal work.

The specifically counterfactual claim needs a different conclusion:

> **Source code and extensional equality alone do not determine a unique, compositional rule for transporting dependence under an alternative action. Once a coherent, effective, finite-policy counterfactual evaluator is fixed, exact rational optimization is computable on its termination promise.**

Accordingly, this round does **not** establish a new, semantics-independent impossibility of an optimal FDT/LDT-like rule. It establishes a precise classification of the sources of failure: incompatible foreign-query requirements, fixed-algorithm diagonalization, exact-selection undecidability, and defective or incomplete counterfactual semantics.

No result verified here is simultaneously established as **true, specifically about unavoidable counterfactual inference, and novel**. The useful contribution is the separation of those claims and the identification of exactly which additional assumptions make each theorem hold.