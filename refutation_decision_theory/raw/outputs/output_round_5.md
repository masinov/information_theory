# Round 5: a conditional impossibility theorem, with a complete consistency map

**There is a sharp three-axiom impossibility, but it does not establish that coherent logical-counterfactual semantics are impossible.** The decisive distinction is between:

- preserving the behavior of a component **after the actual agent has been inserted**; and
- preserving the behavior of its **open computational context under every permitted substitution**.

The first kind of extensionality can erase exactly the information that counterfactual transport needs. The second is compatible with a total, computable substitution semantics.

For an explicit finite domain, I obtain:

1. A minimal inconsistent triple
   \[
   \boxed{\{D2,\ D4_{\mathrm{strong}},\ D5_{\mathrm{ground}}\}}.
   \]
2. A second minimal inconsistent triple
   \[
   \boxed{\{D3,\ D5_{\mathrm{ground}},\ D10\}},
   \]
   whose proper subsets all have **total, computable, baseline-correct witnesses**. This result does not depend on permitting undefined counterfactuals.
3. A complete map with **six minimal inconsistent subsets and four maximal consistent subsets**.
4. A second complete map for a specified program domain with arbitrary fixed total algorithms. Requiring the optimizing agent to be globally total introduces additional pairwise diagonal obstructions.

There are also two preliminary problems with the literal framework: its termination promise is too weak for arbitrary internal program rewriting, and source-changing component replacement can change the inputs supplied to the world. Those produce simpler failures unless repaired.

The results below address P1–P7. The consistency maps are explicitly scoped; there is no interpretation-independent map of the unrefined D1–D10.

---

## 1. Necessary repairs and stipulations

### 1.1 A fixed counterfactual operator need not admit a ratifiable action

The last conclusion in §0 needs correction.

A fixed, computable operator \(K(E,T,a)\) makes each individual comparison computable, assuming its values terminate. It does **not** guarantee an agent whose actual action maximizes those values.

For example, let a component copy the actual action \(b\), and let payoff be

\[
u(a,x)=\mathbf 1[a\ne x].
\]

The action-port-only operator gives

\[
K(E,b,b)=0,\qquad K(E,b,1-b)=1.
\]

Each baseline produces a finite, unambiguous ranking, but neither baseline is ratifiable.

The straightforward optimization theorem applies to a supplied table \(V_E(a)\) that is independent of the reference baseline. A baseline-dependent kernel introduces a separate fixed-point question.

### 1.2 The stated termination promise does not ensure termination of transported contexts

Two termination conditions must be distinguished:

1. the host terminates when its component interfaces are replaced by tables;
2. the original components—and their permitted counterfactual transformations—terminate.

The first does not imply the second.

Here is a counterexample even after requiring the original components to be total. Let \(T(x)=0\), and define

\[
C[P](x)=
\begin{cases}
0,&P(x)=0,\\
\text{diverge},&P(x)=1.
\end{cases}
\]

Treat \(g=C[T]\) as one opaque atomic component. Its actual behavior is the total constant-zero function. Let the host simply return \(g(d)\).

The host terminates under every whole-component table replacement. Nevertheless,

\[
C[T^{d\leftarrow1}](d)
\]

diverges.

Thus, on this literal opaque-component domain:

\[
\boxed{D2+\text{execution-faithful strong }D4
\text{ is already inconsistent}.}
\]

Here execution-faithful transport means that a defined counterfactual value must be the result of the transported execution. If D4 only requires agreement *when that execution terminates*, arbitrary fallback values remain possible.

**Repair used below:** the domain is closed under the stipulated interventions: every supplied computational context terminates under every permitted agent-table substitution.

This can be enforced by finite tables, a terminating language, suitable certificates, or an explicit termination promise. Atomic boundaries matter: replacing an opaque outer component by a table can conceal divergence inside it.

### 1.3 Raw-source extensionality has an unrelated failure

Suppose \(d(E)\) is literally the source string and component replacement changes that string.

Let \(E\) ignore the agent’s action and return

\[
g(d(E)),\qquad g(x)=|x|\bmod 2.
\]

In a language permitting harmless whitespace, replace \(g\) by an extensionally identical implementation padded by one character. The environment’s source parity changes, so its actual payoff changes. A constant agent takes the same action in both versions.

Baseline correctness requires different values; an unqualified source-changing D5 requires equal values. Hence:

\[
\boxed{\{D1,D5_{\mathrm{raw\ source}}\}
\text{ can already be inconsistent}.}
\]

The component functions are equal, but they are being called on different inputs.

**Repair used below:** implementation comparisons preserve the distinguished inputs, or explicitly rebase them. Counterfactual transformations retain the original observation. Distinct primary problems still have distinct descriptions; they are not all assigned one shared agent input.

### 1.4 Single-input transport changes one input, not the whole function

For an intervention at \(d\), define

\[
T^{d\leftarrow a}(x)=
\begin{cases}
a,&x=d,\\
T(x),&x\ne d.
\end{cases}
\]

Strong transport means evaluating \(C[T^{d\leftarrow a}]\).

For example,

\[
C[T]=T\circ h
\]

does **not** generally become the constant \(a\). If \(h(d)\ne d\), then

\[
C[T^{d\leftarrow a}](d)=T(h(d)).
\]

Replacing the whole agent by a constant action is a different, policy-level intervention.

---

## 2. A precise domain and precise versions of D1–D10

The first complete theorem uses a finite fragment. It is sufficient for the semantic obstruction and excludes termination and program-equivalence difficulties.

### 2.1 Finite computational contexts

An environment is

\[
E=(u;c_1,\ldots,c_k),
\]

where:

- the action set is \(A=\{0,1\}\);
- each component has a finite output alphabet \(B_i\);
- \(c_i:A\to B_i\) is a supplied table;
- the host is a finite rational payoff table
  \[
  u:A\times\prod_i B_i\to\mathbb Q.
  \]

The live parameter represents the agent’s output at the distinguished input.

Write

\[
V_E(a)=u(a,c_1(a),\ldots,c_k(a))
\]

for coherent substitution through the contexts, and

\[
W_{E,b}(a)=u(a,c_1(b),\ldots,c_k(b))
\]

for changing the action port while freezing component outputs at baseline \(b\).

An environment is **independent** when every \(c_i\) is constant. This definition is noncircular: independence is invariance under every substitution of the declared live parameter.

We consider local kernels

\[
K(E,b,a)\in\mathbb Q\cup\{\bot\},
\qquad b=T(d(E)).
\]

Restricting the kernel’s dependence on \(T\) to this local baseline is an explicit stipulation. The program extension in §5 preserves this interface.

### 2.2 Two different extensionality principles

Define **grounded equivalence** by

\[
E\sim_b E'
\quad\Longleftrightarrow\quad
\text{same host and interfaces, and }c_i(b)=c_i'(b)\text{ for all }i.
\]

Grounded extensionality requires

\[
E\sim_b E'
\Longrightarrow
K(E,b,a)=K(E',b,a),
\]

including equality of definedness.

This has a direct program interpretation: after inserting the actual agent, a component can be a closed computation returning \(c_i(b)\). Two such closed computations can be extensionally equal while their original contexts respond differently to another action.

By contrast, **parametric extensionality** identifies contexts only when

\[
c_i(a)=c_i'(a)\qquad\text{for every }a.
\]

Parametric extensionality preserves the information that grounded extensionality discards.

Agent extensionality is automatic in the local model: agents computing the same function have the same \(b\).

### 2.3 The principal axiom package

These are the versions used in the first complete map.

| Axiom | Precise requirement |
|---|---|
| **D1 Baseline** | \(K(E,b,b)=V_E(b)\). |
| **D2 Totality** | \(K(E,b,a)\ne\bot\) for every \(E,b,a\). |
| **D3 Independent calibration** | If all \(c_i\) are constant, every value is defined and \(K(E,b,a)=V_E(a)\). |
| **D4 Strong transport** | Whenever \(K(E,b,a)\) is defined, it equals \(V_E(a)\). This transports the entire supplied context and preserves the host. |
| **D5 Grounded extensionality** | \(E\sim_bE'\) preserves values and definedness. |
| **D6 Conservative host evaluation** | Every defined value has the form \(u(a,z_1,\ldots,z_k)\), with \(z_i=c_i(b)\) for each constant context \(c_i\). Other component responses are unrestricted by D6 alone. |
| **D7 Composition** | Transformations retain the original environment and baseline; subsequent intervention overwrites the target action. |
| **D8 Computability** | The option-valued kernel is computable on admissible inputs. In the finite domain, undefinedness can be returned explicitly. |
| **D9 Full slot realizability** | For every action \(a\), the value is defined and is attained by an alternative agent under coherent substitution of the live slot. |
| **D10 Complete ratifiability** | Some computable \(\tau\) has every alternative defined at \(b=\tau(E)\), and \(\tau(E)\) maximizes that table, for every \(E\). |

Three qualifications are essential.

**First, D4 is conditional on definedness.** A stronger formulation that itself requires all transported values to exist incorporates D2.

**Second, D9 is not independent of D2 and D4 in this domain.** Every alternative agent taking action \(a\) under slot substitution obtains exactly \(V_E(a)\). Constant-action agents supply the alternatives. Therefore,

\[
\boxed{D9\iff D2+D4.}
\]

**Third, this D7 is deliberately weak.** Represent a transformed environment by

\[
(E,b;\text{target }a),
\]

whose evaluator returns \(K(E,b,a)\). A further intervention overwrites the target:

\[
(E,b;a)[a\leftarrow z]=(E,b;z).
\]

The transformation record exists even if its evaluator returns \(\bot\). Every value kernel has such a lift. A history-free or fresh-rematching requirement is a different axiom.

---

## 3. The sharp theorems and complete finite consistency map

### 3.1 Four explicit witness operators

Define:

\[
K_{\mathrm{slot}}(E,b,a)=V_E(a),
\]

\[
K_{\mathrm{port}}(E,b,a)=W_{E,b}(a),
\]

\[
K_{\mathrm{base}}(E,b,a)=
\begin{cases}
V_E(b),&a=b,\\
\bot,&a\ne b,
\end{cases}
\]

and

\[
K_{\mathrm{flat}}(E,b,a)=V_E(b).
\]

The last operator assigns the actual payoff to every alternative. Every agent is ratifiable under it, but it generally violates calibration, conservative evaluation, and realizability.

All four satisfy D1, the stated D7, and D8.

For \(K_{\mathrm{slot}}\), choose the first maximizer of \(V_E(0),V_E(1)\). Since the finite syntax is decidable, this optimizer extends to a globally total function by returning a default on invalid strings.

### 3.2 Projection lemma

For any \(E,b\), let \(E^b\) replace each context by its constant baseline value:

\[
c_i^b(a)=c_i(b).
\]

Then

\[
E\sim_b E^b,
\]

\(E^b\) is independent, and

\[
V_{E^b}(a)=W_{E,b}(a).
\]

Two consequences follow.

**Projection lemma, total version.**

\[
\boxed{D3+D5\Longrightarrow K=K_{\mathrm{port}}\text{ everywhere}.}
\]

**Proof.** D3 defines the values in \(E^b\) as \(W_{E,b}(a)\). D5 transfers those values and their definedness to \(E\). ∎

**Projection lemma, conditional version.**

\[
\boxed{D5+D6\Longrightarrow
K(E,b,a)=W_{E,b}(a)\text{ whenever defined}.}
\]

**Proof.** Transfer a defined value to \(E^b\). Every component there is independent, so D6 fixes every component output and hence fixes the payoff. ∎

This is the main structural result: **calibration plus erasure of dependency information forces action-port intervention.**

### 3.3 Theorem A: transport cannot factor through grounded equivalence

\[
\boxed{\{D2,D4,D5\}\text{ is minimally inconsistent}.}
\]

**Proof of inconsistency.** Take

\[
u(a,x)=x,\qquad c(z)=z.
\]

At baseline \(b=0\), compare this with

\[
c'(z)=0.
\]

The instantiated component outputs agree, so \(E\sim_0 E'\). But at action \(1\),

\[
V_E(1)=1,\qquad V_{E'}(1)=0.
\]

D2 defines both values, D4 requires these unequal values, and D5 requires equality. ∎

**Independence.**

| Omitted axiom | Witness for the other two |
|---|---|
| D2 | \(K_{\mathrm{base}}\) |
| D4 | \(K_{\mathrm{port}}\) |
| D5 | \(K_{\mathrm{slot}}\) |

No computability or undecidability argument is involved. The obstruction is loss of information under an equivalence relation.

### 3.4 Theorem B: calibration, grounded extensionality, and ratifiability

\[
\boxed{\{D3,D5,D10\}\text{ is minimally inconsistent}.}
\]

Moreover, every proper subset has a total, computable, baseline-correct witness.

**Proof of inconsistency.** Use copied-action Damascus:

\[
u(a,x)=\mathbf1[a\ne x],\qquad c(z)=z.
\]

For either baseline \(b\),

\[
W_{E,b}(b)=0,\qquad W_{E,b}(1-b)=1.
\]

By the projection lemma, D3 and D5 force this table. Consequently, every actual action recommends its opposite, contradicting D10. ∎

**Independence.**

| Omitted axiom | Witness |
|---|---|
| D3 | \(K_{\mathrm{flat}}\): every action ties |
| D5 | \(K_{\mathrm{slot}}\): maximize \(V_E\) |
| D10 | \(K_{\mathrm{port}}\) |

All three witnesses satisfy D1, D2, D7, and D8. Thus this is a minimal inconsistent triple even relative to that common background.

This answers P4 positively in a substantive formal sense. Its fixed-point obstruction is familiar; the contribution here is the precise derivation of the causal kernel from two distinct semantic requirements.

### 3.5 Complete consistency theorem

**Theorem C.** Under the principal definitions in §2, the inclusion-minimal inconsistent subsets are exactly

\[
\boxed{
\begin{aligned}
&\{D5,D9\},\\
&\{D2,D4,D5\},\\
&\{D3,D4,D5\},\\
&\{D3,D5,D10\},\\
&\{D4,D5,D10\},\\
&\{D5,D6,D10\}.
\end{aligned}}
\]

The maximal consistent subsets are exactly:

| Witness | Maximal consistent subset |
|---|---|
| \(K_{\mathrm{slot}}\) | All ten axioms except D5 |
| \(K_{\mathrm{port}}\) | \(\{D1,D2,D3,D5,D6,D7,D8\}\) |
| \(K_{\mathrm{base}}\) | \(\{D1,D4,D5,D6,D7,D8\}\) |
| \(K_{\mathrm{flat}}\) | \(\{D1,D2,D5,D7,D8,D10\}\) |

#### Proof of the remaining inconsistent cores

- **\(\{D5,D9\}\):** D9 implies D2 and D4, so Theorem A applies.
- **\(\{D3,D4,D5\}\):** in Theorem A’s example, D3 defines the constant-context value as \(0\); D5 transfers it to the identity-context environment; D4 requires \(1\).
- **\(\{D4,D5,D10\}\):** in the identity-context probe \(u(a,x)=x,c(z)=z\), let D10 select \(b\). It requires the alternative \(1-b\) to be defined. Grounded equivalence with the constant context \(c^b(z)=b\) transfers definedness. D4 then requires respectively \(1-b\) and \(b\), while D5 requires equality.
- **\(\{D5,D6,D10\}\):** the conditional projection lemma forces the port-intervention values wherever defined. D10 defines both values at the selected baseline in copied-action Damascus, producing the same contradiction as Theorem B.

#### Minimality

The four operators establish all proper-subset claims. In addition to the tables above:

| Core | Witnesses obtained by deleting its axioms in the displayed order |
|---|---|
| \(\{D3,D4,D5\}\) | Base, Port, Slot |
| \(\{D4,D5,D10\}\) | Flat, Slot, Base |
| \(\{D5,D6,D10\}\) | Slot, Flat, Port |

The individual members of \(\{D5,D9\}\) are witnessed by Port and Slot.

#### Exhaustiveness

Let \(S\) contain none of the six cores.

- If D5 is absent, Slot witnesses \(S\).
- If D5 is present, D9 is absent.
- If D3 is present, the cores exclude D4 and D10; Port witnesses \(S\).
- If D4 is present, the cores exclude D2, D3, and D10; Base witnesses \(S\).
- If neither D3 nor D4 is present and D10 is present, D6 is excluded; Flat witnesses \(S\).
- If D10 is also absent, Port witnesses \(S\).

Every core-free set is therefore contained in one of the four displayed maximal sets. This proves completeness. ∎

### 3.6 A coherent positive model

Replace grounded D5 by parametric D5:

\[
c_i=c_i'\text{ as functions on every permitted alternative}.
\]

Then \(K_{\mathrm{slot}}\) satisfies **all ten axioms** on the finite domain.

Thus:

\[
\boxed{\text{The impossibility concerns erasing dependency context,
not extensionality in every sense.}}
\]

A supplied dependency graph with total structural equations gives the same positive model: intervene on the designated computation, recompute its descendants, retain independent mechanisms, and maximize the resulting finite payoff table.

---

## 4. How the map changes with partiality and realizability conventions

These conventions are not cosmetic.

### 4.1 Conditional realizability and maximization over defined alternatives

Suppose D9 instead says:

> Whenever \(K(E,b,a)\) is defined, that value is attainable under slot substitution.

Then D9 is equivalent to conditional D4.

Suppose D10 only requires the actual value to be defined and maximal **among defined alternatives**.

The exact minimal cores become

\[
\boxed{
\begin{aligned}
&\{D2,D4,D5\},\quad \{D2,D5,D9\},\\
&\{D3,D4,D5\},\quad \{D3,D5,D9\},\\
&\{D3,D5,D10\},\\
&\{D2,D5,D6,D10\}.
\end{aligned}}
\]

The maximal sets are:

| Witness | Maximal set under these conventions |
|---|---|
| Slot | All except D5 |
| Port | \(\{D1,D2,D3,D5,D6,D7,D8\}\) |
| Base | \(\{D1,D4,D5,D6,D7,D8,D9,D10\}\) |
| Flat | \(\{D1,D2,D5,D7,D8,D10\}\) |

The four-member core is minimal: deleting D2, D5, D6, or D10 is witnessed respectively by Base, Slot, Flat, or Port.

This larger core partly reflects splitting “defined and calibrated” into separate requirements. Theorem B is less sensitive to this bookkeeping: its proper-subset witnesses can all remain total.

### 4.2 Fixed-constant realizability is a different benchmark

If realizability freezes all embedded components at their reference implementations, then every alternative with action \(a\) obtains

\[
W_{E,b}(a).
\]

Full \(D9_{\mathrm{const}}\) therefore forces

\[
K=K_{\mathrm{port}}.
\]

It conflicts directly with total strong transport on copied-action examples.

By contrast, \(D9_{\mathrm{slot}}\) forces \(K=K_{\mathrm{slot}}\). Neither realization standard follows from the word “realizable.” It must be supplied.

Also, original D9 includes the actual action. One should not count D1 as an additional independent premise when that realization benchmark already fixes the actual payoff.

---

## 5. A second complete map: arbitrary fixed programs

The finite theorem extends to a specified program promise domain.

Let component contexts be programs

\[
c_i(d,a)\in B_i
\]

promised to terminate for **every string \(d\)** and every legal \(a\). The host remains a finite rational table. The environment’s distinguished description is supplied as \(d\).

A fixed algorithm is allowed as

\[
c(d,a)=F(d).
\]

Independence means invariance in the declared live parameter \(a\). Under this definition, such a fixed program is independent even when \(F\) happens to be the agent being evaluated.

### 5.1 Promise-total optimizing agents

The Slot optimizer evaluates both alternatives and selects a maximizer. It halts on every promised valid description.

The four kernels remain promise-computable, and **the complete map in Theorem C remains valid** when D10 requires only promise-totality.

No algorithm deciding membership in the promise class is required.

### 5.2 Globally total optimizing agents

Now require the optimizing agent \(\tau\) to halt on every string.

For any such candidate, construct the fixed component

\[
c(d,a)=\tau(d)
\]

and host

\[
u(a,x)=\mathbf1[a\ne x].
\]

This is admissible because \(\tau\) is globally total. Put

\[
b=\tau(d(E_\tau)).
\]

The actual payoff is \(0\), while the alternative action obtains \(1\).

Any one of D3, D4, D6, or D9, together with complete D10, forces those values at this baseline. Therefore each of

\[
\{D3,D10\},\quad
\{D4,D10\},\quad
\{D6,D10\},\quad
\{D9,D10\}
\]

is inconsistent.

This is the fixed-program diagonal underlying the Skalse-style objection. Skalse’s original example uses exclusive transparent and opaque boxes; the binary mismatch payoff is a simpler reconstruction under our explicit substitution convention. [arxiv.org](https://arxiv.org/pdf/2101.00280v1?utm_source=chatgpt.com)

### 5.3 Complete global-total map

For this program domain, independence convention, and complete D10, the exact minimal cores are

\[
\boxed{
\begin{aligned}
&\{D5,D9\},\\
&\{D2,D4,D5\},\\
&\{D3,D4,D5\},\\
&\{D3,D10\},\\
&\{D4,D10\},\\
&\{D6,D10\},\\
&\{D9,D10\}.
\end{aligned}}
\]

The maximal consistent sets are:

| Witness | Maximal set |
|---|---|
| Slot kernel, without a globally total optimizer | \(\{D1,D2,D3,D4,D6,D7,D8,D9\}\) |
| Port | \(\{D1,D2,D3,D5,D6,D7,D8\}\) |
| Base | \(\{D1,D4,D5,D6,D7,D8\}\) |
| Flat | \(\{D1,D2,D5,D7,D8,D10\}\) |

The earlier witnesses prove minimality. For exhaustiveness, if D10 is included, the new pairs exclude D3, D4, D6, and D9, leaving a subset of the Flat set. Without D10, the previous case analysis applies.

There is no contradiction with promise-total optimization. Embedding the promise optimizer as \(F(d)\) need not produce a component total on every string, so the proposed diagonal need not belong to this domain.

If D3 uses a different independence class—for example, a syntactically restricted class excluding embedded agent algorithms—the pair \(\{D3,D10\}\) need not follow. The map above explicitly uses independence from the declared live parameter.

---

## 6. The six proposed leads

### L1. The narrow issue is surjectivity, not injectivity

For postcomposition alone,

\[
h_0\circ T=h_1\circ T
\]

means that \(h_0\) and \(h_1\) agree on \(\operatorname{im}(T)\). It determines their values at every legal action precisely when those actions lie in that image.

Thus the relevant property is **surjectivity**.

A highly non-injective binary agent that outputs both bits does not exhibit this particular ambiguity. An injective function from infinitely many descriptions to a finite action set does not exist.

However, arbitrary computational contexts restore the problem. Fix an owned input \(d\), let \(t=T(d)\), and consider

\[
C_0[P](x)=0,
\qquad
C_1[P](x)=\mathbf1[P(d)\ne t].
\]

At \(P=T\), both are globally constant-zero programs. Under a change of the distinguished output to \(1-t\), their values differ.

This is a pointed-context construction: \(d\) remains fixed during the intervention. It works for informative and surjective agents, provided the agent class contains a genuine alternative at that input.

The minimal core depends on how transport is phrased:

- Tagged contexts, conditional transport, grounded extensionality: \(\{D2,D4,D5\}\).
- Transport that already asserts existence: \(\{D4,D5\}\).
- An untagged rule demanding agreement with **every decomposition** \(g=C[T]\): ambiguity is already inside D4; adding D2 can create a pair.
- Parametric extensionality: these contexts are not identified, and Slot works.

### L2. Local matching fails, but its failure is not forced by its other properties

Define local matching by recording each component’s actual queried inputs and selecting components that agree with \(T\) on those inputs. Exclude unqueried components from matching vacuously.

Let an environment contain fixed components

\[
g_0\equiv0,\qquad g_1\equiv1,
\]

both queried at \(d\), with payoff \(1\) iff their outputs agree. The actual action port is otherwise ignored.

For any baseline \(t=T(d)\), exactly \(g_t\) matches.

At the actual action,

\[
K_{\mathrm{loc}}(E,T,t)=0.
\]

At the other action, the selected component changes to \(1-t\), matching the unselected component:

\[
K_{\mathrm{loc}}(E,T,1-t)=1.
\]

No agent is ratifiable.

On an appropriate termination promise, this local operator can satisfy baseline correctness, totality, agent extensionality, implementation extensionality at fixed inputs, and computability. It nevertheless violates:

- D3 and D6 under fixed-component independence;
- strong D4 for transformed copies;
- D9 under ordinary fixed-component actual performance;
- D10.

This does **not** prove that \(\{D1,D2,D5,D8,D10\}\) is inconsistent. \(K_{\mathrm{flat}}\) witnesses their consistency in the local model.

If D9 instead compares against an alternative world modified using the same matching set frozen relative to the original \(T\), realizability becomes immediate. That is an explicitly reference-dependent benchmark, not the unchanged environment’s ordinary alternative-agent payoff.

### L3. Global equality matching misses transformed dependence and can be uncomputable

For binary \(T\), a component

\[
g(x)=1-T(x)
\]

is never extensionally equal to \(T\). Global equality matching leaves it fixed, while strong transport requires

\[
g^{\,a}(d)=1-a.
\]

Equality matching therefore does not implement transport through computational contexts.

There is also a computability obstruction even when every component is total.

Choose a recognizable family \(P\) of source strings containing the constructed environments, with arbitrarily long strings outside \(P\). Let \(T\equiv0\), and define

\[
g_e(x)=
\begin{cases}
0,&x\in P,\\
1,&x\notin P\text{ and machine }e
       \text{ halts within }|x|\text{ steps},\\
0,&\text{otherwise}.
\end{cases}
\]

Then \(g_e\) is total and

\[
g_e\equiv T\iff e\text{ never halts}.
\]

Let \(E_e\), with source in \(P\), return \(g_e(d(E_e))\). Its actual payoff is always zero.

Under global matching, its alternative-1 value is \(1\) if \(e\) never halts and \(0\) if it halts. Computing this \(K\) would decide halting.

The protected source family and the atomic matching boundary are explicit parts of the construction. This is an obstruction to that matching semantics, not to every extensional operator.

### L4. Fresh rematching fails composition; no listed axiom forces it

Start with the local-matching environment \((g_0,g_1)=(0,1)\) and baseline \(0\).

- Intervention to \(1\) changes the matching first component, producing \((1,1)\).
- Fresh matching against the new baseline \(1\) selects both components.
- Intervention back to \(0\) produces \((0,0)\).

The final payoff is \(1\). Direct intervention from the original baseline to \(0\) leaves \((0,1)\), with payoff \(0\).

Thus fresh rematching violates D7.

But none of D1–D10 requires fresh rematching. Retaining the original matching set, or retaining a supplied dependency graph, avoids this failure.

Literal syntactic substitution also needs a one-pass convention: replacement code \(T^{d\leftarrow a}\) itself mentions \(T\) away from \(d\). Repeatedly rescanning inserted code can expand indefinitely.

### L5. Material implication underdetermines \(K\)

Consider the relation

\[
\mathcal V(E,T,a)=
\{q:(T(d)=a)\rightarrow(U(E,T)=q)\text{ is true}\}.
\]

At the actual action, it contains only the actual payoff. At a nonactual action,

\[
\mathcal V(E,T,a)=\mathbb Q.
\]

So material implication does not itself define a numerical counterfactual operator.

In independent five-and-ten, the attainable payoff for taking ten is exactly ten. Selecting zero for that action violates D3 and D9. But **not every selector from the material relation must violate D9**: an additional rule could select the correct intervention value. Vacuism supplies no selection principle.

Likewise, a kernel assigning \((5,0)\) to an agent that takes five can ratify that agent. The failure is calibration or realizability; it need not violate D10, which only asks for an agent ratifiable according to \(K\).

The proof-search literature gives more motivated mechanisms producing spurious implications, but it does not remove this distinction between the implication relation and the rule selecting values from it. [intelligence.org](https://intelligence.org/files/UDTSearchOrder.pdf?utm_source=chatgpt.com)

### L6. Fixed copies are transported only if the equivalence convention erases their role

Compare a designated agent copy with a fixed program that computes the same closed function at the reference agent.

If D5 identifies these despite their different dependency roles, D4’s transport requirement transfers to the fixed program. This conflicts with fixed-component conservativity at a nonactual action.

If D5 preserves the open interface or dependency role, the implication does not follow.

Under the fixed-constant realization benchmark, full D9 already forces the ordinary port-intervention table. The global fixed-copy diagonal therefore yields

\[
\boxed{\{D9_{\mathrm{const}},D10\}\text{ inconsistent}.}
\]

D1 is redundant here.

Weakening D9 to cover only nonactual actions creates the minimal triple

\[
\{D1,D9^-_{\mathrm{const}},D10\}.
\]

Its proper-subset witnesses are port intervention, a baseline-preserving self-confirming kernel, and a kernel that assigns the actual action a value above every attainable alternative. This is a factorization of the fixed-copy diagonal, not a new result under original full D9.

---

## 7. The named candidate semantics

### W1–W5

| Candidate | Precise interpretation and status |
|---|---|
| **W1 CDT intervention** | \(K_{\mathrm{port}}\). Preserves grounded actual behavior and fixed components. Can lack any ratifiable action. Realizable under the fixed-component benchmark. |
| **W2 Oracle/designated slots** | \(K_{\mathrm{slot}}\) for the declared interfaces. On intervention-total finite-policy domains it is computable and optimizable. Preserves parametric extensionality, but not grounded erasure of dependency information. |
| **W3 Literal syntactic substitution** | Replace designated interfaces and original parsed occurrences of the reference agent’s code, once. Can miss equivalent compiled copies; can violate both agent and environment extensionality. Totality requires a promise covering the rewritten programs. |
| **W4 Local matching** | Match on actual queried inputs, then freeze that matching set. Computable under suitable termination promises, but the two-constants example defeats D3, D6, D9 under fixed-component semantics, and D10. |
| **W4 Global matching** | Match whole computed functions. Misses \(1-T\), and its values can be uncomputable by the construction above. |
| **W5 Supplied dependency graph** | A finite acyclic graph of typed variables with total structural equations, a designated computation node, and fixed exogenous data. Intervene on that node and recompute descendants. This is a coherent positive model; the graph supplies the disputed dependence. |

The graphical formulation of FDT explicitly uses a graph encoding subjunctive dependence and intervenes on a variable representing the decision computation. It should not be treated as an algorithm that uniquely extracts that graph from arbitrary closed source code. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com)

### W6. Guarded modal third-person counterfactuals

Fallenstein’s proposal uses mutually exclusive and exhaustive closed modal action formulas \(A_i\) and outcome formulas \(U_j\). Action \(i\) leads to outcome \(j\) when

\[
\mathrm{GL}\vdash A_i\rightarrow U_j
\quad\text{and}\quad
\mathrm{GL}\nvdash\neg A_i.
\]

Refutable actions and ambiguous outcome implications receive no value. The post’s relative optimality result assumes that the relevant action-outcome pair is fully informative, or satisfies its stated weaker condition. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebf/third-person-counterfactuals?utm_source=chatgpt.com)

A useful consequence for this round requires a separate proof.

**Proposition.** Replace GL by an arithmetic theory \(S\) that verifies concrete terminating computations and proves determinism of the interpreter. For an ordinary agent that terminates on \(d\), the guarded semantics is undefined at every nonactual action.

**Proof.** Let the actual action be \(b\). Its finite execution trace gives

\[
S\vdash T(d)=b.
\]

Determinism gives

\[
S\vdash T(d)\ne a
\]

for every \(a\ne b\). Every nonactual action fails the guard. If the actual environment also terminates, its trace verifies the actual payoff. ∎

Thus this arithmetic specialization is \(K_{\mathrm{base}}\).

- Under complete D10, it does not ratify an agent on a binary problem.
- Under maximization over defined alternatives, it ratifies every agent trivially.

This proposition is a reconstruction here, not a theorem attributed to Fallenstein. It explains why positive results for modal or provability-oracle agents cannot be transferred directly to ordinary terminating programs.

### W7. Logical induction with a specified exploration rule

A precise finite-stage construction is available. Fix a logical inductor \(P_n\), an encoding, a stage \(n\), and a provably \([0,1]\)-valued utility variable \(\bar U\). Use the paper’s conditional valuation convention and approximate expectation:

\[
K_n(a)=
\frac1n\sum_{i=0}^{n-1}
P_n\!\left(\bar U>i/n\mid A_n=a\right).
\]

The conditional is the capped ratio, with value \(1\) when the conditioning probability is zero. These are Definitions 4.7.1 and 4.8.2. [arxiv.org](https://arxiv.org/pdf/1609.03543?utm_source=chatgpt.com)

One published exploration scheme is

\[
A_n=
\begin{cases}
0,&P_n(A_n=0)<\varepsilon,\\
1,&P_n(A_n=1)<\varepsilon,\\
0,&K_n(0)>K_n(1),\\
1,&\text{otherwise}.
\end{cases}
\]

This is self-diagonalization against logical prices, not an independent physical coin. Its exploration clauses can override maximization of the current \(K_n\). Garrabrant’s discussion explicitly identifies the difference between exploratory deviations and reliably adopting the same action. [lesswrong.com](https://www.lesswrong.com/posts/5bd75cc58225bf06703753d4/two-major-obstacles-for-logical-inductor-decision-theory?utm_source=chatgpt.com)

Logical induction alone does not imply exact finite-stage calibration. To see this directly, replace every price at one stage by zero; finite-perturbation closure preserves logical induction. The conditional convention then assigns \(1\) to every conditioned proposition. For a constant-zero payoff, this yields \(K_n(0)=K_n(1)=1\), violating D1, D3, and D9. [arxiv.org](https://arxiv.org/pdf/1609.03543?utm_source=chatgpt.com)

Exploration’s scope is another input. For

\[
u(a,b)=a+2b
\]

at baseline \(a=b=0\):

- exploration changing only the final port gives \((0,1)\);
- exploration changing the port and designated copied bit together gives \((0,3)\).

Conditioning computes the implications of the supplied exploration mechanism; it does not select that mechanism.

---

## 8. Numerical test cases, including the current Anti-Newcomb

Use \(0=\) one-box/cooperate and \(1=\) two-box/defect. For the stipulated Newcomb and twin PD payoffs,

\[
u(a,b)=2(1-b)+a.
\]

Let \(t=T(d)\), and define vectors in action order \(0,1\):

\[
P_t=(2(1-t),\,2(1-t)+1),\qquad S=(2,1),
\]

\[
D_t=(t,\,1-t),\qquad Z=(0,0),\qquad H=(5,10).
\]

Here \(P_t\) freezes the predictor, \(S\) transports a shared copy, and \(D_t,Z\) are the corresponding vectors for the mismatch diagonal.

In the following table, Newcomb and the twin have designated dependencies. The diagonal’s embedded target and Anti-Newcomb’s \(f\) are initially declared fixed components. Literal-copy rows assume the direct source occurrences are present.

| Operator | Newcomb | Twin PD | Five-and-ten | Fixed-copy diagonal | Anti-Newcomb |
|---|---|---|---|---|---|
| **W1 Port only** | \(P_t\): two-box | \(P_t\): defect | \(H\): ten | \(D_t\): opposite \(t\) | \(P_t\): two-box |
| **W2 Designated slots** | \(S\): one-box | \(S\): cooperate | \(H\): ten | \(D_t\): opposite \(t\) | \(P_t\): two-box |
| **W3 Slots plus literal-copy rewriting** | \(S\): one-box | \(S\): cooperate | \(H\): ten | \(Z\): tie | \(S\): one-box |
| **W4 Local matching** | \(S\): one-box | \(S\): cooperate | \(H\): ten | \(Z\): tie | \(S\): one-box |
| **W4 Global matching** | \(S\): one-box | \(S\): cooperate | \(H\): ten | \(Z\): tie | \(S\): one-box |
| **W5 Supplied graph** | \(S\) if linked; \(P_t\) if fixed | Same | \(H\) | \(Z\) if linked; \(D_t\) if fixed | \(S\) if linked; \(P_t\) if fixed |
| **W6 Arithmetic guarded version** | Actual value only | Actual value only | Actual value only | Actual value only | Actual value only |
| **W7 Unspecified inductor/stage** | No unique numerical verdict | No unique numerical verdict | No exact verdict follows from LI alone | No unique numerical verdict | No unique numerical verdict |

For W6, “actual value only” means the other action is undefined, so there is no complete-ratifiability recommendation.

For a concrete W7 instance, the all-zero-price stage described above assigns the normalized upper bound to both actions. With the natural payoff bounds, its vectors are respectively

\[
(3,3),\ (3,3),\ (10,10),\ (1,1),\ (3,3).
\]

This permitted example shows why “logical induction” does not determine a unique finite-instance verdict.

### Anti-Newcomb’s exact status

The current specification is

\[
U(\text{one})=2x,\qquad
U(\text{two})=2x+1,
\qquad
x=\mathbf1[f(d)=\text{one}].
\]

Its **payoff table**, indexed by predictor output and action, is the ordinary Newcomb payoff table:

\[
\begin{pmatrix}
2&3\\
0&1
\end{pmatrix}.
\]

That does not make the complete decision problems isomorphic: the response of \(f\) under an alternative must still be specified.

- If \(f\) is a designated shared computation, coherent substitution gives \((2,1)\).
- If \(f\) remains a fixed program, the vector is \(P_t\), and two-boxing wins by \(1\).
- Literal or equality matching links the exact copy, but inherits the failures established above.
- Parametric extensionality preserves the fixed/shared distinction.
- Grounded extensionality that erases this distinction participates in the impossibility theorem.

Also, this Anti-Newcomb is **not itself a diagonal defeating every theory**. Under fixed-component semantics, a two-boxing target is already making the optimal choice. The mismatch-payoff environment is the relevant diagonal.

---

## 9. Robustness and domain requirements

| Variation | Result |
|---|---|
| **Globally total versus promise-total agents** | The finite semantic obstruction survives both. Arbitrary fixed total algorithms create the additional global-total diagonal pairs in §5. |
| **Including fixed algorithms** | Fixed-target diagonals return when alternatives leave the target fixed. They are unnecessary for the elementary finite context/extension obstruction. |
| **Excluding fixed algorithms** | Use a concrete grammar: declared agent interfaces, no unrestricted evaluation or source reflection, and intervention-total contexts. “Nothing derived from \(T\)” is not a workable definition: every \(g\) is \(C[T]\) for a context ignoring its argument. |
| **Injective or informative agents** | Injection into a finite action set is unavailable on an infinite description domain. Surjectivity fixes only the narrow \(h\circ T\) ambiguity; arbitrary contexts still distinguish actual equivalence from counterfactual equivalence. |
| **Distribution-valued \(K\)** | Exact transport can demand distinct point masses \(\delta_0,\delta_1\) for the same grounded representation. Uncertainty alone does not remove that contradiction. |
| **Mixed agents as an additional change** | Some ratifiability failures can acquire mixed fixed points, depending on predictor and sampling semantics. That is a further model change; it does not repair the exact transport/extensionality contradiction. |
| **Policy-level interventions** | Every one-input witness embeds in the policy-level setting. Finite owned-policy tables support the positive Slot theorem. Infinite policy spaces require separate optimization and computability assumptions. |
| **Bounded or certified languages** | They can support a globally total optimizer with a fallback on invalid descriptions. The unrestricted fixed-copy diagonal need not have a valid certificate or belong to the bounded class. |

The full consistency maps therefore require a domain statement specifying:

1. the atomic interfaces;
2. which contexts are intervention-total;
3. whether inputs are preserved under implementation changes;
4. whether fixed programs are permitted;
5. whether agents must halt globally;
6. the substitution benchmark used in D9;
7. the treatment of undefined alternatives in D10.

These are mathematical assumptions, not implementation details that can be omitted after the theorem is stated.

---

## 10. Counterpossibles and impossible-world semantics

The philosophical literature contains a close precedent for the information-loss issue.

### 10.1 An established collapse argument

In Williamson’s accessible 2015 version, let \(|A|\) denote the possible-world intension of \(A\), and suppose

\[
|A\Box\!\to B|
=f(|A|,|A|\cap|B|).
\]

If \(A\) is impossible, every consequent gives \(f(\varnothing,\varnothing)\). Reflexivity,

\[
|A\Box\!\to A|=W,
\]

then makes every counterpossible true. The argument shows how semantic identification plus ordinary counterfactual constraints eliminates nonvacuity. It is not a theorem about all numerical program operators. [platform.openjournals.nl](https://platform.openjournals.nl/PAC/article/download/22236/23870/54746?utm_source=chatgpt.com)

Berto, French, Priest, and Ripley instead permit impossible worlds with more discriminating valuations. Their §3.1 explains the conflict between reflexivity, classical consequence closure, and nontrivial treatment of contradictions; §3.2 explicitly discusses substitution failures inside counterfactual contexts. [Springer Nature Link](https://link.springer.com/article/10.1007/s10992-017-9446-x?utm_source=chatgpt.com)

The analogy to our theorem is precise at one level: **identifications appropriate to actual or possible behavior need not preserve distinctions needed under counterpossible suppositions.**

### 10.2 Can impossible worlds implement the consistent kernels?

Yes, as a representation construction.

Given a finite baseline-correct kernel \(K\):

- retain an actual world with the actual action and payoff;
- for every defined alternative \(a\), introduce a world recording action \(a\) and payoff \(K(E,b,a)\);
- select that world when evaluating the corresponding antecedent;
- for an undefined alternative, select multiple worlds with incompatible payoff values, so no unique numerical outcome is determined.

For nonactual outputs of a fixed computation, the selected worlds may be impossible relative to the original computation’s complete description. Retaining the origin and overwriting the target realizes the stated composition law.

This construction represents Slot, Port, Base, or Flat. It does not make them all satisfy realizability: impossible worlds can record unattainable values, and D9 separately rules those out.

Nor does it derive a canonical \(K\). The selection relation encodes the counterfactual policy one has already chosen. Impossible-world semantics provides room to preserve distinctions; it does not infer missing dependence information from a closed program’s ordinary extension.

---

## 11. Verified literature and novelty assessment

The following are the relevant verified references and their limits.

| Reference | Verified contribution and location |
|---|---|
| **Abram Demski and Scott Garrabrant, “Embedded Agency,” arXiv:1902.09469, 2019, based on the 2018 sequence.** | §2.1, pp. 7–10, discusses five-and-ten and exploration; §2.2, pp. 10–11, explains how an externally supplied agent slot already contributes disputed structure. It does not prove a universal numerical-\(K\) impossibility. [arxiv.org](https://arxiv.org/pdf/1902.09469?utm_source=chatgpt.com) |
| **Nate Soares and Benja Fallenstein, “Toward Idealized Decision Theory,” 2015, arXiv:1507.01986; originally MIRI 2014–7.** | Introduction and later discussion distinguish maximizing utilities from identifying counterfactual alternatives. The abridged AGI 2015 publication is titled “Two Attempts to Formalize Counterpossible Reasoning in Deterministic Settings.” [arxiv.org](https://arxiv.org/pdf/1507.01986?utm_source=chatgpt.com) |
| **Tsvi Benson-Tilsen, “UDT with Known Search Order,” MIRI technical report 2014–4, 2014.** | Theorem 4.5, p. 6, characterizes the selected action as the unique “safe” action under the defined search-order relations. Corollary 4.6, pp. 6–7, shows that optimistic first searches are the only universally successful strategy within that model. The model explicitly uses a provability/halting oracle. [intelligence.org](https://intelligence.org/files/UDTSearchOrder.pdf?utm_source=chatgpt.com) |
| **Benya Fallenstein, “Third-person counterfactuals,” displayed 3 February 2015.** | Defines the guarded partial GL semantics and proves relative optimality under its informativeness conditions. This is a research post, not a theorem about arbitrary ordinary total programs. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebf/third-person-counterfactuals?utm_source=chatgpt.com) |
| **Fallenstein, “An optimality result for modal UDT,” displayed 15 November 2014.** | For each provably extensional finite modal problem, some finite sound extension of PA makes the specified modal UDT optimal. The quantifiers are \(\forall P\,\exists\varphi\), not one fixed proof system working for all problems. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8f/an-optimality-result-for-modal-udt?utm_source=chatgpt.com) |
| **Fallenstein, “‘Evil’ decision problems in provability logic,” displayed 10 January 2015.** | A fixed-theory diagonal in the modal setting. This is a direct precedent for the fixed-constant obstruction, with its own modal hypotheses. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic?utm_source=chatgpt.com) |
| **Fallenstein, “The odd counterfactuals of playing chicken,” displayed 2 February 2015.** | Gives a problem in which the specified proof-based counterfactuals are informative yet differ from the payoff of another actual agent. The proof assumes a provability oracle and the specified proof system. [lesswrong.com](https://www.lesswrong.com/posts/5bd75cc58225bf0670374ec0/the-odd-counterfactuals-of-playing-chicken?utm_source=chatgpt.com) |
| **Scott Garrabrant, Tsvi Benson-Tilsen, Andrew Critch, Nate Soares, Jessica Taylor, “Logical Induction,” 2016, arXiv:1609.03543.** | Definitions 4.7.1 and 4.8.2 specify conditioning and approximate expectation; Theorem 4.6.1 gives finite-perturbation closure. These do not impose exact finite-stage decision calibration. [arxiv.org](https://arxiv.org/pdf/1609.03543?utm_source=chatgpt.com) |
| **Scott Garrabrant, “Two Major Obstacles for Logical Inductor Decision Theory,” 17 April 2017.** | Gives the explicit exploration rule and discusses how exploratory deviations can have different predictive consequences from ordinary decisions. Its discussion is not a general exact-optimality theorem. [lesswrong.com](https://www.lesswrong.com/posts/5bd75cc58225bf06703753d4/two-major-obstacles-for-logical-inductor-decision-theory?utm_source=chatgpt.com) |
| **Eliezer Yudkowsky and Nate Soares, “Functional Decision Theory: A New Theory of Instrumental Rationality,” 2017, revised 2018, arXiv:1710.05060.** | §§5–6 give graphical formulations and benchmark analyses with dependence relations supplied in the model. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com) |
| **Joar Skalse, “A General Counterexample to Any Decision Theory and Some Responses,” 2021, arXiv:2101.00280.** | The opening exclusive-box construction targets a fixed theory; the force of its conclusion depends on the fairness and alternative-agent interpretation. [arxiv.org](https://arxiv.org/pdf/2101.00280v1?utm_source=chatgpt.com) |
| **Daniel Nolan, “Impossible Worlds: A Modest Approach,” *Notre Dame Journal of Formal Logic* 38(4), 535–572, 1997.** | The supplied title’s extra subtitle is incorrect. Publisher metadata and indexed portions were confirmed; full-text access was blocked, so I do not claim full theorem-by-theorem verification. [projecteuclid.org](https://projecteuclid.org/journals/notre-dame-journal-of-formal-logic/volume-38/issue-4/Impossible-Worlds-A-Modest-Approach/10.1305/ndjfl/1039540769.short?utm_source=chatgpt.com) |
| **Timothy Williamson, “Counterpossibles,” *Topoi* 37(3), 357–368, 2018; online 2016.** | Publisher abstract and metadata confirm its defense of vacuism. The full journal text was unavailable; the exact collapse argument above was checked in the accessible 2015 *Amsterdam Colloquium* version, pp. 30–31. [Springer Nature Link](https://link.springer.com/article/10.1007/s11245-016-9424-x?utm_source=chatgpt.com) |
| **Francesco Berto, Rohan French, Graham Priest, David Ripley, “Williamson on Counterpossibles,” *Journal of Philosophical Logic* 47(4), 693–713, 2018.** | Full open-access text verified. §2.3 supplies the semantics; §§3.1–3.2 address closure and substitution. [Springer Nature Link](https://link.springer.com/article/10.1007/s10992-017-9446-x?utm_source=chatgpt.com) |

Two further close precedents deserve mention.

**David Lewis, “Probabilities of Conditionals and Conditional Probabilities,” *The Philosophical Review* 85(3), 297–315, 1976**, gives a genuine triviality theorem about representing conditional probabilities as probabilities of fixed conditional propositions. Its first result is on p. 300. It does not prohibit numerical conditional expectations or every logical-counterfactual kernel. [joelvelasco.net](https://joelvelasco.net/teaching/4310/lewis76-prob_cond_cond_prob.pdf?utm_source=chatgpt.com)

**Jessica Taylor, “Two Alternatives to Logical Counterfactuals,” 2020**, discusses changing source code together with hypothetical policies and the underdetermination of that change. It is a closely related proposal, not an independent-axiom impossibility theorem. [Unstable Ontology](https://unstableontology.com/2020/04/01/alternatives-to-logical-counterfactuals/?utm_source=chatgpt.com)

### Novelty

I did not locate the exact finite-kernel consistency maps or the precise triple \(\{D3,D5_{\mathrm{ground}},D10\}\) in the checked sources. That is not sufficient to claim publication novelty.

The defensible attribution is:

- the fixed-copy diagonal, spurious implications, and pure-ratifiability failures are established phenomena;
- the counterpossible literature already analyzes conflicts involving semantic identification and nonvacuity;
- the finite quotient theorem and exhaustive maps above are explicit reconstructions for the stated axiom package;
- their possible novelty lies in that formal packaging and characterization, not in discovering that counterfactual dependence requires additional structure.

---

## 12. Final form of the thesis

The unrestricted claim that no coherent logical-counterfactual operator exists is **false**. A provenance-preserving, intervention-total context semantics supplies a coherent positive model.

The following conditional thesis is true:

> **A total counterfactual semantics cannot always transport a computation through alternative outputs while also identifying every presentation that has the same instantiated actual behavior. Actual behavior can omit the information needed to determine the counterfactual extension.**

There is also a distinct ratifiability theorem:

> **Independent calibration and extensionality that erases dependency information can force action-port intervention, which need not admit a ratifiable deterministic action—even though each proper pair has a total, computable, baseline-correct semantics.**

For the broad class with arbitrary fixed algorithms and globally total optimizing agents, additional diagonal impossibilities remain. For opaque components without intervention closure, simpler termination failures arise before the substantive semantic question.

The strongest justified conclusion is therefore:

**An optimality theorem requires a specified account of the alternatives, a domain closed under those alternatives, and a matching realization benchmark. Grounded program equivalence alone cannot supply that account.**