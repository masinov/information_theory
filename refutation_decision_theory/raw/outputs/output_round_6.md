# Round 6: the theorem is true, but the proposed characterization of “unfairness” is false

Parts **(a)–(c)** can be proved under a precise version of your model. Part **(d)** needs correction: computability is sufficient for a uniform construction of a defeating environment, but noncomputable theories can also be defeated.

The degree question has a sharper answer than “an optimal theory needs the halting problem”:

> **With unrestricted answers on inadmissible descriptions, the oracles capable of computing a globally total optimal agent are exactly the PA degrees. This holds for both the deterministic and stochastic classes.**
>
> **If the agent must return a prescribed computable default on every inadmissible description, the required strength rises to \(0'\) in the deterministic case and \(0''\) in the stochastic case.**

Here, a **PA degree** means a Turing degree that computes a binary diagonally noncomputable function, defined below. Some PA degrees are strictly below \(0'\).

The complete classification is:

| Environment class | Complexity of admissibility | Oracle sufficient and necessary for a promise-total optimizer | Oracle sufficient and necessary for a globally total optimizer, arbitrary answers outside the promise | Globally total optimizer with a prescribed default outside the promise |
|---|---|---|---|---|
| Deterministic, finite policies, explicit rational rewards | \(\Sigma^0_1\)-complete | Ordinary computability suffices | PA degree | Computes \(0'\) |
| Almost-sure termination, finite policies, bounded rational rewards | \(\Pi^0_2\)-complete | PA degree | PA degree | Computes \(0''\) |

The entries classify **oracles capable of computing an optimizer**. They do not assert a least PA degree; there is no such least degree.

---

## 1. Precise model and additional stipulations

I use the following effective implementation of your model.

### 1.1 Descriptions, ownership, and policies

Every well-formed environment description \(e\) specifies a program and a finite list of action menus. Its owned queries are computably tagged:

\[
Q_e=\{q(e,0),\ldots,q(e,k_e-1)\},
\qquad d(e)=q(e,0).
\]

The tagging is injective, so different environments have disjoint query sets. From an owned query, one can computably recover its environment and its local query number.

Each action menu is a computably supplied finite nonempty set. We can label its actions \(0,\ldots,m-1\), making \(0\) a legal default. Thus

\[
\Pi_e=\prod_{q\in Q_e}A_q
\]

is a computably supplied finite nonempty policy space.

Different source descriptions remain different environments, even if they happen to compute the same payoff function. We impose no invariance under changes of source representation.

### 1.2 Execution and constants

For \(\pi\in\Pi_e\), \(E_e^\pi\) means the execution in which every designated agent call is answered by the table \(\pi\).

Embedded programs remain fixed. They execute as ordinary computations, and their running time counts as part of the environment’s execution. They are not granted an instantaneous oracle for their mathematical outputs.

Consequently, the agent enters the evaluation only through its owned-query table:

\[
U(E_e,A)=V_e(A\!\restriction Q_e).
\]

Conversely, every finite table \(\pi\in\Pi_e\) extends to a total agent. Therefore

\[
\max_A U(E_e,A)=\max_{\pi\in\Pi_e}V_e(\pi).
\tag{1}
\]

### 1.3 The two classes

The deterministic class is

\[
\mathcal C_{\det}
=
\{e:\forall\pi\in\Pi_e,\ E_e^\pi
\text{ halts with an explicitly encoded rational reward}\}.
\]

Rational rewards may be unbounded in this class.

For the stochastic class, I use a probabilistic program language with effective finite branching and **exact rational transition probabilities**. Fair coins already suffice for all lower bounds. Terminal rewards are explicitly encoded rationals in \([0,1]\):

\[
\mathcal C_{\sto}
=
\{e:\forall\pi\in\Pi_e,\ E_e^\pi
\text{ terminates with probability }1\}.
\]

The reward bound is enforced by the language or a runtime guard. This lets us reason about bounded terminal rewards even on programs that fail the termination promise.

Almost-sure termination includes embedded computations. We do not additionally require termination on every null-probability infinite execution, or global totality of every embedded program on inputs that the environment never supplies.

These are substantive representation stipulations. In particular, requiring every constant program to be globally total would change the admissibility predicate.

### 1.4 Totality conventions

A **globally total implementation** halts on every string.

A **promise-total implementation** must halt on every owned query of an admissible environment. It may halt or diverge elsewhere. It need not recognize the promise, and its domain need not equal the promise exactly.

Unless stated otherwise, any maximizing policy is permitted when there is a tie.

Finally, distinguish:

- a default on malformed syntax, which is computable bookkeeping;
- a default on every **semantically inadmissible environment**, which is a much stronger requirement.

The degree distinction in the opening table concerns the second.

---

## 2. The main existence-and-diagonal theorem

### Theorem 1 — Optimal functions exist; globally total computable optimizers do not

Under the model above:

1. Optimal total agents exist on \(\mathcal C_{\det}\) and on \(\mathcal C_{\sto}\), including agents with a fixed default outside the admissible class.
2. Every globally total computable agent is strictly suboptimal in some environment in \(\mathcal C_{\det}\) having one binary owned query and rewards in \(\{0,1\}\).
3. A computable promise-total optimizer exists on \(\mathcal C_{\det}\).
4. No computable promise-total exact optimizer exists on \(\mathcal C_{\sto}\).

The stochastic assertion will follow from the stronger degree theorem in §4.

### 2.1 Existence: E1

Fix a computable ordering of each finite policy space. For each admissible environment, define

\[
\pi_e^*
=
\min\operatorname*{arg\,max}_{\pi\in\Pi_e}V_e(\pi).
\]

The maximum exists because the policy set is finite and the values are defined. In the stochastic case, bounded rewards ensure finite expectations.

Now define

\[
T^*(q)=
\begin{cases}
\pi_e^*(q),&q\in Q_e,\ e\text{ admissible},\\
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]

Ownership makes this consistent: no query receives prescriptions from two different environments.

For every admissible \(e\),

\[
U(E_e,T^*)
=
V_e(\pi_e^*)
=
\max_{\pi\in\Pi_e}V_e(\pi)
=
\max_A U(E_e,A).
\]

Thus \(T^*\) is a total optimal agent. This is an explicit set-theoretic definition, using a fixed finite tie order; no unrestricted choice principle is needed. ∎

**A correction to the background:** fixing \(U(E,\cdot)\) independently of the evaluated agent does not exclude environments containing fixed copies of particular programs. Those copies can be fixed features of the payoff function. The existence proof includes such environments.

### 2.2 The fixed-copy diagonal: E2

Let \(T\) be globally total and computable.

Construct an environment with its own root description \(d\) that performs:

```text
c := run the fixed program for T on d
a := designated_agent_query(d)
return 1 if a ≠ c, otherwise 0
```

A self-description facility implements this directly. With ordinary program indices, Kleene’s recursion theorem supplies the required self-reference. Its applicable form is that a program can be constructed whose behavior depends on its own program index; see Moschovakis’s precise statement on p. 190 and the self-reproduction application in §1. [math.ucla.edu](https://www.math.ucla.edu/~ynm/papers/1602-002-1.pdf?utm_source=chatgpt.com)

Call the resulting environment \(E_T\). It is admissible:

- it has one binary owned query;
- the embedded computation \(T(d)\) halts;
- under either table action, the remaining computation halts;
- its reward is \(0\) or \(1\);
- it makes no designated foreign query.

Because the embedded copy remains fixed,

\[
U(E_T,A)=\mathbf 1[A(d)\ne T(d)].
\]

Hence

\[
U(E_T,T)=0,
\qquad
\max_A U(E_T,A)=1.
\]

Indeed, a computable competitor that chooses \(1-T(d)\) at this one query suffices. ∎

The construction is uniform from an index for \(T\); its admissibility is guaranteed when that index denotes a globally total legal agent.

### 2.3 The deterministic promise optimizer and its escape: E3(iii)

On an owned query of \(E_e\), run the following algorithm \(P\):

1. Enumerate all policies in \(\Pi_e\).
2. Simulate \(E_e^\pi\) for every policy.
3. Once all simulations terminate, compare their rational rewards.
4. Select the first maximizing **complete policy**, and return its component at the requested query.

For an admissible deterministic environment, this halts. Reconstructing the same complete policy at every owned query ensures coordination.

Now attempt to construct \(E_P\), the diagonal environment containing \(P(d(E_P))\) as a fixed computation.

Suppose that computation halted with output \(b\). Then \(E_P\) would halt under both table actions and would be admissible. Since \(P\) is optimal on every admissible deterministic input, it would have to choose \(1-b\). But its output is \(b\), a contradiction.

Therefore

\[
P(d(E_P))\uparrow,
\]

so \(E_P\) is inadmissible.

This proves the escape, rather than merely suggesting that nontermination might occur.

The escape depends on the evaluation convention. If nontermination is assigned a reward and admitted as an outcome, one has changed both the environment class and the optimization problem.

---

## 3. Why finite agreement does not defeat an optimal agent: E3(i)–(ii)

Let \(T^*\) be an optimal total agent.

No ordinary embedded program computes \(T^*\) globally, by Theorem 1. Nevertheless, a computable program can agree with \(T^*\) on finitely many inputs. Noncomputability does not prohibit finite agreement.

What optimality prohibits is agreement at the particular input of an admissible anti-prediction environment.

For any fixed program \(p\), let \(E_p\) have the template

\[
c=p(d(E_p)),\qquad
U(E_p,A)=\mathbf1[A(d(E_p))\ne c].
\]

Whenever \(p(d(E_p))\) halts with a bit, the environment is admissible and its maximum value is \(1\). Therefore

\[
T^*(d(E_p))=1-p(d(E_p)).
\tag{3}
\]

So a fixed program may agree with \(T^*\) elsewhere, but it cannot both be accurate at this anti-prediction input and define an admissible instance.

### Hard-coding does not evade this

Let \(E_0\) pay for choosing \(1\), and let \(E_1\) pay for choosing \(0\). Their descriptions are \(d_0,d_1\). Optimality requires

\[
T^*(d_0)=1,\qquad T^*(d_1)=0.
\]

Thus neither hard-coded bit satisfies

\[
k=T^*(d_k).
\]

The statement “inserting the bit changes the description” is not by itself a proof. Equation (3), and this two-instance example, give the missing argument: the required self-consistency can fail.

This immunity belongs to **optimal agents**, not to noncomputable agents generally. Section 7 gives a noncomputable agent defeated by a fixed constant predictor.

---

## 4. Exact degree classification: E4

### 4.1 Binary diagonal noncomputability

Fix an acceptable enumeration \((\varphi_e)\) of partial computable functions.

A binary diagonally noncomputable function is a total function

\[
g:\mathbb N\to\{0,1\}
\]

such that

\[
\varphi_e(e)\downarrow
\quad\Longrightarrow\quad
g(e)\ne\varphi_e(e).
\tag{4}
\]

If the right-hand output is not binary, disagreement is automatic.

No such \(g\) is computable: otherwise choose an index \(e\) for \(g\), obtaining \(g(e)\ne g(e)\).

An oracle has **PA degree** exactly when it computes such a binary DNC function. This standard characterization is stated in Hirschfeldt’s §3.1, immediately after Theorem 3.21, and in the research literature on PA-complete degrees. [math.uchicago.edu](https://math.uchicago.edu/~drh/Papers/Papers/rm.pdf?utm_source=chatgpt.com)

### 4.2 A finite-selection lemma

We need one elementary consequence of binary DNC.

**Lemma.** Suppose a finite nonempty candidate set is given computably, candidates are excluded by a computably enumerable process, and at least one candidate is never excluded. A binary DNC oracle can select a never-excluded candidate.

**Proof.** Partition the current set \(B\) into two nonempty subsets \(B_0,B_1\). Construct a program with index \(k\) that ignores its input, watches the exclusion process, and returns \(i\) if every member of \(B_i\) is eventually excluded.

Because \(B\) contains a survivor, at most one side can be completely excluded.

Choose side \(B_{g(k)}\). If this side had no survivor, the program would eventually output \(g(k)\), contradicting (4). Therefore the selected side contains a survivor.

Repeat until a singleton remains. Only finitely many oracle calls are needed. ∎

### 4.3 Deterministic global optimization is exactly PA strength

**Upper bound.** For each environment, start with all policies as candidates. Simulate every policy. If all terminate, exclude precisely the nonmaximizing policies. If they do not all terminate, exclude nothing.

This is a computably enumerable exclusion process, and it always leaves a candidate. On admissible inputs, its survivors are exactly the maximizing policies.

The lemma therefore gives a globally total optimizer from any PA oracle. Every owned query reconstructs the same selected policy.

**Lower bound.** Given \(e\), construct a binary environment \(D_e\) that first runs \(\varphi_e(e)\). If it returns a bit \(b\), the reward is

\[
V_{D_e}(a)=\mathbf1[a=1-b].
\]

If it returns a non-bit, both actions receive \(0\). If it diverges, \(D_e\) is inadmissible.

For any globally total optimal agent \(T\), define

\[
g(e)=T(d(D_e)).
\]

Global totality makes \(g\) total even when \(D_e\) is inadmissible. If \(\varphi_e(e)\) returns a bit, optimality forces the opposite bit. Thus \(g\) is binary DNC. ∎

Notice that this lower bound does not need a self-referential environment. It identifies the computational difficulty of completing a promise optimizer on all descriptions.

### 4.4 Bounded stochastic expectations are computable on the promise

For a program, policy \(\pi\), and finite machine-time cutoff \(s\), compute

\[
H_{\pi,s}
=
\Pr(E^\pi\text{ has halted by time }s)
\]

and

\[
L_{\pi,s}
=
\mathbb E[
r\,\mathbf1_{\{E^\pi\text{ has halted by time }s\}}
].
\]

These are rational and computable from the finite execution tree. Define

\[
B_{\pi,s}=L_{\pi,s}+1-H_{\pi,s}.
\]

Then

\[
I_{\pi,s}=[L_{\pi,s},B_{\pi,s}]
\]

is a nested interval. Its lower endpoint increases, and its upper endpoint decreases because newly terminated probability mass contributes reward between \(0\) and that mass.

On an admissible input,

\[
V_E(\pi)\in I_{\pi,s},
\qquad
|I_{\pi,s}|=1-H_{\pi,s}\longrightarrow0.
\tag{5}
\]

To approximate the expectation within any positive rational error, search until the interval is sufficiently narrow. The search halts on the AST promise.

Thus the problem is not that these promised expected values lack computable approximations. The difficulty is selecting an **exact** maximizer when equality is possible.

### 4.5 A PA oracle gives a globally total stochastic optimizer

Exclude policy \(\pi\) whenever, for some \(\rho\) and \(s\),

\[
L_{\rho,s}>B_{\pi,s}.
\tag{6}
\]

On admissible environments, this excludes exactly the strictly suboptimal policies, by (5).

To use the finite-selection lemma globally, we must prove that invalid descriptions also retain a survivor.

For this purpose alone, define the auxiliary quantity

\[
\ell_\pi=\lim_sL_{\pi,s},
\]

the expected reward accumulated on terminating executions, with nontermination contributing zero. This does **not** change which environments are admissible.

For every program,

\[
L_{\pi,s}\le\ell_\pi\le B_{\pi,s}.
\tag{7}
\]

Choose a policy \(\pi^*\) maximizing the finitely many \(\ell_\pi\). It cannot be excluded: exclusion would imply

\[
\ell_\rho
\ge L_{\rho,s}
>
B_{\pi^*,s}
\ge \ell_{\pi^*},
\]

a contradiction.

Hence every description retains a survivor. The finite-selection lemma gives a total policy selector on every description, and it is optimal on every admissible stochastic environment. ∎

This is why an optimizer need not solve the harder problem of recognizing almost-sure termination.

### 4.6 Even promise-total stochastic optimization requires PA strength

For each \(e\), construct an environment \(S_e\) with one binary choice:

1. Obtain the agent’s action \(a\).
2. Sample \(N\ge0\) with
   \[
   \Pr(N=n)=2^{-(n+1)}.
   \]
3. Simulate \(\varphi_e(e)\) for \(N\) steps.
4. If a binary output \(b\) is observed, return \(\mathbf1[a\ne b]\); otherwise return \(0\).

Every \(S_e\) is admissible under both actions. It uses only a finite simulation budget after an almost-surely terminating geometric draw.

If \(\varphi_e(e)\) halts with bit \(b\) at step \(t\), then

\[
V_{S_e}(1-b)=\Pr(N\ge t)=2^{-t}>0,
\qquad
V_{S_e}(b)=0.
\]

Thus every exact optimizer chooses \(1-b\).

For any promise-total optimizer \(T\),

\[
g(e)=T(d(S_e))
\]

is therefore a total binary DNC function. Totality follows because **all instances in this reduction are admissible**. ∎

This proves the strongest computability separation here without a theory-specific predictor. The family is generated independently of the evaluated agent. It also has an effective running-time tail bound, and every realized reward is binary.

### 4.7 The exact degree spectrum

We have proved:

> An oracle computes a globally total optimizer for either class, with unrestricted off-promise answers, **iff** it has PA degree.
>
> An oracle computes a promise-total stochastic exact optimizer **iff** it has PA degree.

Every PA degree can also occur as the **exact degree of an optimal total agent**. Given an oracle \(X\) of PA degree, construct an \(X\)-computable optimizer, then encode \(X(n)\) into its choices on a computable family of distinct binary environments where both actions tie. Ownership ensures these modifications do not affect any other problem.

The Low Basis Theorem supplies a low PA degree \(X\), with

\[
X'\equiv_T0'.
\]

Such an \(X\) cannot compute \(0'\), since otherwise \(0''\le_T X'\equiv_T0'\). Consequently some optimal agents satisfy

\[
0<_T T<_T0'.
\]

Moreover, cone avoidance for effectively closed classes shows that no single noncomputable set is computed by every optimizer. These are standard basis-theorem consequences, not additional assumptions about decision theory. [math.uchicago.edu](https://math.uchicago.edu/~drh/Papers/Papers/rm.pdf?utm_source=chatgpt.com)

---

## 5. Admissibility and prescribed defaults

### 5.1 Deterministic admissibility is \(\Sigma^0_1\)-complete

Because there are finitely many policies,

\[
e\in\mathcal C_{\det}
\iff
\exists s\;
[\text{every }E_e^\pi\text{ halts legally within }s\text{ steps}].
\]

The bracketed predicate is decidable. Thus the class is computably enumerable.

For hardness, given a halting instance, construct an environment that ignores its action, runs that computation, and returns \(0\) if it halts. The environment is admissible exactly when the computation halts.

Therefore membership is \(0'\)-complete and, in particular, decidable relative to \(0'\).

### 5.2 Stochastic admissibility is \(\Pi^0_2\)-complete

Using the finite-time termination probabilities,

\[
e\in\mathcal C_{\sto}
\iff
\forall k\ \exists s\ \forall\pi\in\Pi_e:
H_{\pi,s}>1-2^{-k}.
\tag{8}
\]

The last quantifier is finite, yielding a \(\Pi^0_2\) definition.

For hardness, reduce

\[
\mathrm{TOT}=\{e:\forall n,\ \varphi_e(n)\downarrow\}.
\]

Sample a geometric \(N\), then run \(\varphi_e(N)\) without a cutoff. Every integer has positive sampling probability, so the resulting environment is AST exactly when \(e\in\mathrm{TOT}\).

Thus admissibility is \(\Pi^0_2\)-complete, of degree \(0''\). The same geometric reduction appears in Kaminski and Katoen, *On the Hardness of Almost–Sure Termination*, §6, Theorems 6–7. [arxiv.org](https://arxiv.org/pdf/1506.01930?utm_source=chatgpt.com)

### 5.3 Why a mandatory default changes the answer

Suppose the required off-promise default is \(0\).

For the deterministic class, construct \(H_e\) that waits for \(\varphi_e(e)\) and, if it halts, returns reward equal to the chosen action \(a\).

Then

\[
T(d(H_e))=
\begin{cases}
1,&\varphi_e(e)\downarrow,\quad\text{by unique optimality},\\
0,&\varphi_e(e)\uparrow,\quad\text{by the default requirement}.
\end{cases}
\]

So \(T\) computes \(0'\). Conversely, \(0'\) decides admissibility, after which ordinary finite-policy optimization suffices.

For the stochastic class, modify the \(\mathrm{TOT}\) reduction to return reward \(a\) after \(\varphi_e(N)\) halts. Then

\[
T(d(H_e))=
\begin{cases}
1,&e\in\mathrm{TOT},\\
0,&e\notin\mathrm{TOT}.
\end{cases}
\]

Thus \(T\) computes \(0''\). Conversely, \(0''\) decides admissibility, and \(0'\) suffices to select a survivor by deciding the c.e. exclusion predicates.

For any other computable legal default, reward its opposite in these constructions. Self-description supplies the default’s argument when necessary.

Therefore E1’s requested default-completed agents can be chosen at degrees exactly \(0'\) and \(0''\), respectively. Those degrees are not necessary when off-promise answers remain free.

### 5.4 Tie-breaking is another independent specification

For stochastic environments, prescribing a fixed lexicographic tie rule already raises the promise-selection requirement to \(0'\).

To see this, make action \(0\) have value \(0\), and action \(1\) have value \(2^{-t}\) if a given computation halts at time \(t\), otherwise \(0\). These values have uniformly computable approximations and can be realized by the geometric construction.

If ties must favor \(0\), the chosen action is \(1\) exactly when the computation halts.

The PA classification therefore concerns **choosing any maximizer**, as your optimality definition permits.

---

## 6. Relativization

Fix an oracle \(X\). Let environments and their fixed constants be \(X\)-computable, while retaining the same finite ownership and termination conventions.

For every globally total \(X\)-computable agent \(T\), the relativized recursion theorem constructs

\[
U(E_T^X,A)=\mathbf1[A(d)\ne T(d)].
\]

The fixed \(X\)-computation of \(T(d)\) halts, so \(E_T^X\) is admissible and defeats \(T\).

Hence:

\[
\boxed{\text{No globally total }X\text{-computable agent optimizes all }X\text{-computable admissible environments.}}
\]

Existence still holds by finite maximization and ownership.

The degree results relativize as well:

- deterministic promise optimization is \(X\)-computable;
- unrestricted total optimization requires and suffices to compute a binary \(\mathrm{DNC}^X\) function;
- stochastic promise optimization has that same requirement;
- prescribed semantic defaults require \(X'\) and \(X''\), respectively.

The environment oracle stays fixed in these statements. Giving the environments access to the optimizer’s stronger oracle creates a new class, to which the diagonal applies again.

---

## 7. “Unfairness”: a precise definition and the failed equivalence

“Constructed against a theory” describes provenance or intent unless we specify a mathematical witness.

A useful noncircular definition is:

> An **anti-prediction environment** is an environment of the syntactic template \(E_p\): run a fixed program \(p\) on the environment’s own root description, then reward disagreement with its output.

This defines an environment family without referring to optimality.

Call \(E_p\) **accurate for \(T\)** when

\[
p(d(E_p))=T(d(E_p)).
\]

For an admissible \(E_p\),

\[
E_p\text{ is accurate for }T
\iff
T\text{ receives }0\text{ while the maximum is }1.
\tag{9}
\]

The diagonal proves that every globally total computable \(T\) has an accurate admissible member of this family.

### Noncomputability does not imply immunity

Let \(T^*\) be an optimal noncomputable agent. Let \(E_0\) be an anti-prediction environment whose fixed predictor always returns \(0\). Optimality gives

\[
T^*(d(E_0))=1.
\]

Define \(A\) by changing this one answer:

\[
A(q)=
\begin{cases}
0,&q=d(E_0),\\
T^*(q),&\text{otherwise}.
\end{cases}
\]

A finite modification of a noncomputable function remains noncomputable. Yet

\[
U(E_0,A)=0<1=\max_B U(E_0,B).
\]

So a noncomputable theory can face an accurate, admissible anti-prediction environment.

### The proposed “iff” has three different readings

1. **Global simulation.**  
   If an environment can run a program computing \(T\) globally, the diagonal produces a defeating environment. The converse is false: the noncomputable \(A\) above is defeated.

2. **Finite agreement on owned queries.**  
   Every restriction \(T\!\restriction Q_E\) is a finite table and hence computable. This existential observation cannot characterize suboptimality. It also does not provide a uniform way to insert that table into an environment while preserving the query being predicted.

3. **Accuracy in an anti-prediction environment.**  
   Equation (9) gives an exact equivalence between accuracy and defeat **within that specified family**. It does not characterize globally computable theories.

Accordingly, the defensible implication is

\[
\text{global computable simulatability}
\Longrightarrow
\text{uniformly constructible defeat}.
\]

Neither being defeated nor having a locally accurate predictor implies global computability.

---

## 8. Sharpness of the hypotheses: E5 and boundary cases F–G

### 8.1 Foreign queries can destroy existence altogether: F

Let two environments query the same foreign input \(q\) and pay

\[
U(E_0,A)=\mathbf1[A(q)=0],
\qquad
U(E_1,A)=\mathbf1[A(q)=1].
\]

Both are deterministic and total, and each has attainable maximum \(1\). No agent attains both maxima.

Thus unrestricted foreign queries can eliminate optimal agents of **every** Turing degree.

Disjoint ownership is sufficient, not logically necessary. The exact existence condition is compatibility:

\[
\bigcap_{E\in\mathcal C}
\{T:T\!\restriction Q_E\in\operatorname{argmax}V_E\}
\ne\varnothing.
\]

Ownership guarantees this intersection is nonempty.

### 8.2 Linking the embedded copy removes the fixed-copy diagonal: G

If the embedded copy is designated as another linked occurrence of the evaluated agent, replacing \(T\) by \(A\) changes both calls. The diagonal payoff becomes

\[
U(E,A)=\mathbf1[A(d)\ne A(d)]=0.
\]

Every policy is then optimal in that environment.

This removes **that diagonal mechanism**. It does not remove the global promise-completion obstruction or the stochastic DNC lower bound, neither of which requires a linked copy of the evaluated agent.

Actual behavior cannot determine linkage. A fixed constant-zero program and a linked call to an agent currently outputting zero agree on the actual execution; they differ under replacement by an agent outputting one. Which occurrence changes is part of the intervention semantics.

### 8.3 Dropping termination under all policies

Without a convention for nontermination, some compared values are undefined.

If nontermination is instead assigned reward \(0\), consider:

- action \(0\): immediately return \(1/2\);
- action \(1\): run a given computation, returning \(1\) if it halts.

The optimal action identifies whether the computation halts. Thus the computable deterministic promise optimizer no longer applies.

### 8.4 Dropping explicit rational reward representation

Suppose a deterministic environment returns a program giving successively better approximations to its payoff, rather than an explicit rational.

Uniformly define two values by

\[
v_e(1-b)=2^{-t},\qquad v_e(b)=0
\]

if \(\varphi_e(e)\) first halts with binary output \(b\) at time \(t\), and both values \(0\) otherwise.

These have uniformly computable fast Cauchy names: simulate long enough that any later halt could change the value by less than the requested error.

Exact maximization again computes binary DNC.

In fact, every individual value in this example is rational. The relevant assumption is access to its **explicit exact representation**.

### 8.5 Dropping the stochastic reward bound

The bound \([0,1]\) supplies the upper interval endpoint in (5).

Without it, even a finite-expectation, AST family can force computation of \(0'\). Sample \(N\ge1\) with probability \(2^{-N}\). Let:

- action \(0\) pay \(1/2\);
- action \(1\) pay \(2^N\) exactly when a given computation first halts at step \(N\), and \(0\) otherwise.

Then

\[
V(1)=
\begin{cases}
1,&\text{the computation halts},\\
0,&\text{otherwise}.
\end{cases}
\]

All expected rewards are finite, but exact optimization decides halting.

### 8.6 Exactness and ties

On the bounded AST promise:

- For every rational \(\varepsilon>0\), an \(\varepsilon\)-optimal policy is computable: wait until every interval has width less than \(\varepsilon\), then choose the largest lower endpoint.
- If a unique maximizer is promised, exact optimization is computable: wait until one lower endpoint exceeds every other upper endpoint.

These are promise-total algorithms. They do not automatically provide globally total implementations on arbitrary program descriptions.

### 8.7 Finiteness

If the policy set is infinite, a maximum need not exist. For example, actions \(n\in\mathbb N\) with payoff

\[
1-\frac1{n+1}
\]

have supremum \(1\) and no maximizer. The finite-policy hypothesis supports existence as well as the computational analysis.

---

## 9. Bounded resources: H

There is no unconditional theorem that an optimizer must run strictly longer than its environments.

Two precise statements are available.

### Known worst-case execution bounds restore computability

If descriptions belong to a decidable clocked language with a supplied finite execution bound, then:

- deterministic policy values can be evaluated exhaustively;
- stochastic policy values can be calculated by summing the finite rational execution tree.

A globally total computable optimizer exists on that clocked class. Invalid syntax can receive a computable default.

The required running time can be large because there may be many policies and many random branches.

### A resource-bounded diagonal requires simulation closure

A bounded version of E2 works against an agent \(T\) whenever the allowed environment budget accommodates:

1. self-description;
2. simulation of \(T\) on that description;
3. the final comparison and reward.

If the environment’s budget cannot accommodate that simulation, the diagonal does not establish a lower bound.

There is also a separate expected-value computation cost. A short stochastic execution can encode a difficult comparison: action \(1\) evaluates a Boolean formula on a uniformly random assignment; action \(0\) pays a Bernoulli reward of mean

\[
\frac12+2^{-(n+1)}.
\]

Action \(1\) is optimal exactly when strictly more than half of the \(2^n\) assignments satisfy the formula. Each play is short, while exact evaluation concerns all assignments.

Thus “the environments can run the agent” is the useful resource condition for the diagonal. A general ranking by a single runtime bound is insufficient.

---

## 10. Literature verification and novelty

### Fixed-target decision problems are established

**Joar Skalse (2021), “A General Counterexample to Any Decision Theory and Some Responses,” arXiv:2101.00280, pp. 1–3.**  
Skalse’s fixed-target box construction is a direct predecessor of E2: the opaque box’s contents depend on what a designated theory permits, while another theory is evaluated in that same problem. The paper discusses fairness. It does not supply this ordinary-program admissibility analysis or the degree classification. [arxiv.org](https://arxiv.org/pdf/2101.00280v1?utm_source=chatgpt.com)

**Eliezer Yudkowsky and Nate Soares (2017; revised 2018), “Functional Decision Theory: A New Theory of Instrumental Rationality,” arXiv:1710.05060, §9, printed p. 29, footnote 15.**  
The footnote explicitly discusses punishing an agent for matching a fixed copy of Fiona and acknowledges the problem of specifying corresponding comparison environments. The fixed-copy obstruction is therefore already recognized in the FDT paper itself. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com)

**Benya Fallenstein (2015), “‘Evil’ decision problems in provability logic,” author post, displayed date 10 January 2015, sections “Definitions,” “Fixed points,” and “Evil problems.”**  
For finite fully modalized decision theories, the post constructs a provably extensional problem rewarding disagreement with a fixed target. This is a formal modal precursor, with different admissibility semantics. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic?utm_source=chatgpt.com)

There is a small proof repair worth recording: the post’s displayed competitor flips \(T_1(\mathbf u)\), which re-evaluates \(T\) on the competitor’s universe. Instead, use the closed competitor \((\neg B_1,B_1,\bot,\ldots)\), where \(\mathbf B\) is the fixed target action. This provably disagrees with \(\mathbf B\) and preserves the theorem. [alignmentforum.org](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374e8c/evil-decision-problems-in-provability-logic?utm_source=chatgpt.com)

An earlier informal predecessor is **drnickbone, “Problematic Problems for TDT,” LessWrong, 29 May 2012**, especially its fixed-simulation problems and discussion of algorithm-specific counterexamples. [lesswrong.com](https://www.lesswrong.com/posts/3GyQXTy2WhYcaBgS2/problematic-problems-for-tdt?utm_source=chatgpt.com)

### Computability of optimal agents and policies

**Jan Leike and Marcus Hutter (2015), “On the Computability of AIXI,” UAI 2015, pp. 464–473.**  
In the original ten-page version, Theorem 8 gives a one-level arithmetical-hierarchy upper bound for exact policy selection from computable values; Theorem 11 avoids that increase for approximate selection. Corollary 13 gives limit-computable exact and computable approximate policies for computable measures. Theorem 14 states that AIXI is noncomputable for every universal machine. These results concern different inputs and environment models, but the exact-selection issue is closely related. [jan.leike.name](https://jan.leike.name/publications/On%20the%20Computability%20of%20AIXI%20-%20Leike%2C%20Hutter%202015.pdf?utm_source=chatgpt.com)

**Jan Leike and Marcus Hutter (2015), “Bad Universal Priors and Notions of Optimality,” COLT 2015, PMLR 40:1244–1259, §5, Theorem 18.**  
The theorem says every policy is Pareto optimal in any class containing all lower semicomputable chronological conditional semimeasures. Its policies act on shared interaction histories, rather than disjoint environment-specific descriptions. It therefore does not contradict the existence theorem here. Its proof also explicitly observes that finite hard-coded behavior can define a computable environment even when the defended policy is noncomputable—a relevant warning against the proposed unfairness equivalence. [proceedings.mlr.press](https://proceedings.mlr.press/v40/Leike15.pdf?utm_source=chatgpt.com)

### Classical foundations of the degree result

**Yiannis N. Moschovakis (2010), “Kleene’s Amazing Second Recursion Theorem,” Bulletin of Symbolic Logic 16(2):189–239**, p. 190 and §1, supplies the precise self-reference theorem used in E2. [math.ucla.edu](https://www.math.ucla.edu/~ynm/papers/1602-002-1.pdf?utm_source=chatgpt.com)

**Carl G. Jockusch Jr. and Robert I. Soare (1972), “\(\Pi^0_1\) classes and degrees of theories,” Transactions of the AMS 173:33–56**, is the classical basis-theorem source. I could verify its attribution through accessible sources but could not retrieve the original AMS full text. Their companion paper, **“Degrees of members of \(\Pi^0_1\) classes,” Pacific Journal of Mathematics 40(3):605–616**, is accessible; pp. 612–613 discuss the relevant PA-completion and effectively closed-class results. [msp.org](https://msp.org/pjm/1972/40-3/pjm-v40-n3-p09-s.pdf?utm_source=chatgpt.com)

For modern exact statements, see **Denis R. Hirschfeldt, *Slicing the Truth: On the Computable and Reverse Mathematics of Combinatorial Principles*, World Scientific, Lecture Notes Series 28**, §3.1, especially Theorems 3.14, 3.17, and 3.21 in the author version. The series catalog dates publication to 2014; the book is also commonly cited with its 2015 copyright year. [math.uchicago.edu](https://math.uchicago.edu/~drh/Papers/Papers/rm.pdf?utm_source=chatgpt.com)

**Vasco Brattka, Matthew de Brecht, and Arno Pauly (2012), “Closed Choice and a Uniform Low Basis Theorem,” Annals of Pure and Applied Logic 163(8):986–1008**, Examples 3.2 and 3.10, provides the closest selection-theoretic framework: finite closed choice and its countable parallelization. Our upper bound selects from finite sets whose excluded elements are enumerated; that is precisely the relevant closed-choice structure. [arxiv.org](https://arxiv.org/pdf/1002.2800?utm_source=chatgpt.com)

**Benjamin Lucien Kaminski and Joost-Pieter Katoen (2015), “On the Hardness of Almost–Sure Termination,” arXiv:1506.01930**, §6, Theorems 6–7, already establishes the \(\Pi^0_2\)-completeness used in the stochastic admissibility analysis. [arxiv.org](https://arxiv.org/pdf/1506.01930?utm_source=chatgpt.com)

### Novelty assessment

I found no source among these stating the exact combined classification with:

- disjoint owned queries;
- fixed embedded programs;
- deterministic versus AST stochastic environments;
- global versus promise totality;
- unrestricted versus prescribed off-promise answers.

That does not establish priority. The main ingredients are established: finite maximization, fixed-target diagonals, binary DNC/PA degrees, finite closed choice, and AST complexity.

The defensible contribution is a **precise synthesis and sharpened classification**, especially the distinction between optimization and recognizing admissibility.

---

## 11. Corrected final thesis

The statement supported by the proofs is:

> **For computable environments with disjoint finite owned-query sets and well-defined values under every table policy, simultaneously optimal total agents exist. Every globally total computable agent is defeated by an admissible fixed-copy diagonal. Deterministic exact optimization remains computable on its termination promise; bounded stochastic exact optimization does not. With arbitrary off-promise answers, the exact oracle requirement for total optimal selection is PA degree, rather than necessarily the halting degree.**
>
> **Global computable simulatability guarantees a uniform method of constructing a defeating environment. It does not characterize all defeatable theories: noncomputable theories can also make predictable mistakes.**

Thus “optimal decision programs that the environments can run are impossible” is correct with the global-totality and simulation-closure hypotheses. **“Unfair problems exist exactly for computable theories” is not.**