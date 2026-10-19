# Assessment

**The incompatibility claim is correct once “optimal” means satisfying specified conflicting criteria. The unqualified thesis is false under your definition of a decision theory.**

Because every deterministic finite problem has finitely many policies, there is a lookup-table theory that maximizes ex-ante value on every well-defined problem. What fails is joint satisfaction of ex-ante maximization and causal dominance—or other particular combinations of requirements.

The main results are:

- **C1 and C2 are incompatible**, already on a noisy, two-action Newcomb problem with one always-reached information set.
- A stronger characterization is available: **any difference between the state distributions induced by two prescriptions permits a payoff assignment separating C1 from C2**, even with payoffs bounded in \([0,1]\).
- **Deterministic C3 is individually unsatisfiable** on a class containing Death in Damascus. It therefore cannot belong to a minimally inconsistent family whose members are each individually satisfiable.
- Under the explicit completion below, the maximal consistent subsets of C1–C5 are
  \[
  \boxed{\{C1,C4,C5\},\qquad \{C2,C5\}.}
  \]
  A specified evidential completion gives a corresponding C1–C6 classification.
- **Bomb needs correction** once the agent observes whether a bomb is present.
- There is already a closely related **Arrow-style impossibility theorem in Briggs (2010)**. The broad novelty claim should therefore be withdrawn or substantially narrowed. [Download on Academia](https://www.academia.edu/2307714/Decision_Theoretic_Paradoxes_as_Voting_Paradoxes?utm_source=chatgpt.com)

Below I distinguish results that follow from your framework directly from those requiring additional stipulations.

---

# 1. A precise model — T1

## 1.1 Problems and policies

For the general consistency results, use finite extensive-form problems in which **no information set occurs twice on one path**. Perfect recall is a sufficient, stronger restriction. This subclass contains the witnesses needed here.

The deterministic policy space is
\[
\Pi_D=\prod_{h\in H_D}A_h,
\]
with all action sets finite and nonempty.

Your policy-dependent transition kernels determine the distribution of actual play, but they do not by themselves settle every causal counterfactual. To make those counterfactuals explicit, supplement the tree with:

- a finite nonempty set \(S_D\) of **structural environment plans**;
- a distribution \(\mu_\pi\in\Delta(S_D)\) for every \(\pi\in\Pi_D\);
- the payoff \(U_D(s,\pi)\) obtained by traversing the tree with environment plan \(s\) and policy \(\pi\).

An environment plan specifies the nonagent responses needed to determine play under every possible agent policy. It can prescribe different responses after different earlier physical actions.

Thus:
\[
V_D(\pi)=\sum_{s\in S_D}\mu_\pi(s)U_D(s,\pi).
\]

The distinction is:

- **Ordinary causal dependence on earlier actions** is represented by the responses within \(s\).
- **Predictive dependence on the policy** is represented by \(\pi\mapsto\mu_\pi\).

A finite tree with policy-dependent kernels can be represented this way by supplying potential outcomes for its nature and prediction nodes. The coupling of outcomes on alternative branches is an additional modeling choice.

Conversely, such a model can be implemented by a policy-dependent root node selecting \(s\), followed by deterministic traversal.

Call this fully specified class \(\mathcal F^*\), including the commitment extensions defined below. The basic Newcomb impossibility applies more broadly; the exhaustive consistency table is specifically for this completion.

## 1.2 Fairness and well-definedness

Require \(S_D\), \(U_D\), and the entire map \(\pi\mapsto\mu_\pi\) to be fixed features of \(D\). Evaluation may depend on an agent’s prescriptions, but not separately on its theory identity.

Also require:

> **For every admissible policy, the problem supplies a well-defined probability distribution.**

This is distinct from fairness. A verbally described “perfect predictor” can satisfy an action-based fairness condition while its promised behavior is logically inconsistent.

A fixed algorithm \(g_0\) may appear in the environment, as you allow. But its presence does not automatically make self-referential specifications well-defined.

## 1.3 Local causal interventions

Write
\[
R_h(\pi)=\{s:h\text{ is reached under }(s,\pi)\}.
\]

The actual probability of reaching \(h\) is
\[
r_\pi(h)=\mu_\pi(R_h(\pi)).
\]

Let \(\pi[h\leftarrow a]\) change only the prescription at \(h\). Since \(h\) cannot occur earlier on the same path, this change does not alter whether \(h\) is reached **when the environment plan is fixed**.

Define
\[
Q_\pi(h,a)=
\frac{\displaystyle
\sum_{s\in R_h(\pi)}
\mu_\pi(s)U_D(s,\pi[h\leftarrow a])
}{r_\pi(h)}
\]
whenever \(r_\pi(h)>0\).

This specifies the counterfactual completely: retain the original distribution over environmental responses, change the local action, and retain the policy’s other prescriptions.

The crucial difference is
\[
\begin{aligned}
Q_\pi(h,a)&\text{ uses }\mu_\pi,\\
V_D(\pi[h\leftarrow a])&\text{ uses }\mu_{\pi[h\leftarrow a]}.
\end{aligned}
\]

## 1.4 Completed C1–C3

**C1:** \(T_D\in\arg\max_\pi V_D(\pi)\).

**C2:** At a positively reached \(h\), do not choose \(b\) if some \(a\) satisfies
\[
U_D(s,\pi[h\leftarrow a])
>
U_D(s,\pi[h\leftarrow b])
\qquad\text{for every }s\in R_h(\pi).
\]

Here compatibility is **structural**, including states assigned probability zero by \(\mu_\pi\).

**C3:** At every positively reached \(h\),
\[
\pi(h)\in\arg\max_a Q_\pi(h,a).
\]

These definitions imply
\[
\boxed{C3\Longrightarrow C2.}
\]

**Proof.** Strict improvement in every structural state reaching \(h\) implies strict improvement in conditional expectation under \(\mu_\pi\). ∎

### Why the structural-state stipulation matters

If “compatible with \(h\)” means only the positive-probability states under the selected policy, exact Death in Damascus makes **C2 itself unsatisfiable**: the sole supported state puts Death in the selected city, so switching strictly improves every supported outcome.

Likewise, on unrestricted trees, “hold only past states fixed” leaves unanswered how to evaluate future prediction nodes. Freezing their policy dependence while averaging over their outcomes can make C2 collapse into an unsatisfiable best-response requirement.

The completed C2 above is a deliberate resolution of these ambiguities.

## 1.5 Commitment and C4

Define a canonical, tagged commitment extension \(K(D)\):

1. The agent chooses \(q\in\Pi_D\).
2. This choice irrevocably installs \(q\).
3. The environment then implements the distribution and behavior appropriate to \(q\).

Formally, take
\[
S_{K(D)}=\prod_{q\in\Pi_D}\operatorname{supp}(\mu_q),
\qquad
\mu^{K(D)}=\bigotimes_{q\in\Pi_D}\mu_q.
\]
For a tuple \((s_q)_q\), committing to \(q\) yields \(U_D(s_q,q)\). Therefore
\[
\boxed{V_{K(D)}(q)=V_D(q).}
\]

This models a **causal choice of policy before prediction**. Changing the commitment changes the subsequent environment response.

**C4:** If \(T\) chooses commitment \(q\) in \(K(D)\), then
\[
q(h)=T_D(h)
\]
at every information set positively reached under \(T_D\).

The commitment constructor is tagged and well-founded, so \(K(D)\), \(K(K(D))\), and so forth have unambiguous decompositions.

## 1.6 C5

A decision theory is already defined to be total. Consequently, **C5 is redundant as a property of decision theories**.

An empty recommendation set means a proposed criterion fails to define such a theory. That is exactly what happens to deterministic C3.

If partial theories were allowed, totality could become an independent axiom. That would change §2.

---

# 2. Ex-ante optimal theories exist; C1 and C2 conflict — T2

## Theorem 1: Universal ex-ante selection

There exists a total deterministic theory satisfying C1 on every well-defined finite problem.

**Proof.** Fix a finite tie-breaking order for each policy space and set
\[
T^{\mathrm{ex}}_D
=
\operatorname{first}\arg\max_{\pi\in\Pi_D}V_D(\pi).
\]
Every \(\Pi_D\) is finite and nonempty, so every maximum exists. ∎

This is why the literal statement “no decision theory is optimal on all fair problems” needs qualification.

## Theorem 2: Newcomb incompatibility

Let \(O\) denote one-boxing and \(B\) two-boxing. Use the payoff table

| Action | Opaque box full | Opaque box empty |
|---|---:|---:|
| \(O\) | 2 | 0 |
| \(B\) | 3 | 1 |

Specify symmetric predictor error:
\[
\Pr(\mathrm{full}\mid O)=1-\varepsilon,\qquad
\Pr(\mathrm{full}\mid B)=\varepsilon.
\]

Then
\[
V(O)=2(1-\varepsilon),\qquad
V(B)=1+2\varepsilon.
\]

Thus
\[
V(O)-V(B)=1-4\varepsilon.
\]

For
\[
\boxed{0\le\varepsilon<\tfrac14,}
\]
C1 uniquely requires \(O\).

But two-boxing adds exactly one in every fixed state:
\[
U(s,B)-U(s,O)=1.
\]
Therefore C2 and C3 uniquely require \(B\). ∎

Hence no theory satisfies C1 and C2 on any class containing this problem.

### Why this is close to trivial

For each local criterion \(C_i\), let
\[
A_i(D)=\{\pi:\pi\text{ satisfies }C_i\text{ in }D\}.
\]

For arbitrary lookup-table theories and purely local criteria,
\[
\exists T\ \forall D\ \bigwedge_i C_i(T,D)
\quad\Longleftrightarrow\quad
\forall D\ \bigcap_i A_i(D)\ne\varnothing.
\]

The reverse implication follows by selecting the first policy in each intersection.

Newcomb simply exhibits
\[
A_1(D)\cap A_2(D)=\varnothing.
\]

No difficulty about general rules or computation is involved. This basic disagreement is already central to Nozick’s original presentation. [danielhoek.com](https://danielhoek.com/wp-content/uploads/2020/02/Nozick-Newcombs-Problem-and-Two-Principles-of-Choice.pdf?utm_source=chatgpt.com)

---

# 3. A stronger characterization of the obstruction — T3

The following is more informative than another named counterexample.

## Theorem 3: Policy-dependent state laws exactly characterize possible dominance conflict

Fix a finite action set \(A\), a finite hidden state space \(S\), and distributions \(\mu_a\) over states preceding one always-reached choice.

The following are equivalent:

1. For **every** payoff function \(u:A\times S\to[0,1]\), some ex-ante maximizing action is causally undominated.
2. All the distributions \(\mu_a\) are identical.

### Proof: \(2\Rightarrow1\)

Under a common distribution \(\mu\), strict statewise dominance implies strict expected-utility superiority. Therefore a dominated action cannot maximize expected utility.

### Proof: \(1\Rightarrow2\)

Suppose \(\mu_a\ne\mu_b\). After exchanging their names if necessary, choose an event \(E\subseteq S\) such that
\[
\delta=\mu_b(E)-\mu_a(E)>0.
\]

Choose
\[
0<c<\frac{\delta}{1+\delta}.
\]

Define
\[
u(b,s)=(1-c)\mathbf1_E(s),
\qquad
u(a,s)=(1-c)\mathbf1_E(s)+c.
\]
Give all other actions payoff zero.

All payoffs lie in \([0,1]\). Action \(a\) strictly dominates \(b\), by \(c\), in every state. Nevertheless,
\[
V(b)-V(a)=(1-c)\delta-c>0.
\]

Moreover, \(V(a)\ge c>0\), so \(b\) is the unique ex-ante maximizer over all actions. That maximizer is strictly dominated. ∎

**Interpretation:** Very accurate prediction and enormous stakes are unnecessary for an existence result. Any nonconstant dependence of the preceding state law on the prescription can produce the conflict. For fixed payoffs, the size of that dependence determines whether the conflict occurs.

---

# 4. Correcting and interpreting the other witnesses

## 4.1 Twin prisoner’s dilemma

Represent the twin’s action as a prediction node copying the agent’s prescription at the single choice:
\[
\text{Twin action}=\pi(h).
\]

Do not model the twin as another independently assignable coordinate in \(\Pi_D\); that would remove the stipulated identity of their decisions.

With your payoffs,
\[
V(C)=2,\qquad V(D)=1.
\]
So C1 chooses cooperation.

Holding the twin’s action fixed, defection improves payoff by one whether the twin cooperates or defects. Thus C2 and C3 choose defection.

This requires a stipulated dependence between the two outputs. “Same computation” is not something the tree establishes on its own. The Newcomb/PD connection is classical, including Lewis’s 1979 treatment. [andrewmbailey.com](https://andrewmbailey.com/dkl/Prisoners_Dilemma.pdf?utm_source=chatgpt.com)

## 4.2 Death in Damascus

Let actions and states both be \(\{A,B\}\), with
\[
U(s,a)=\mathbf1\{a\ne s\},
\qquad
\mu_a=\delta_a.
\]

For either deterministic policy, its chosen action gives zero under the induced state, while switching gives one. Thus no deterministic policy satisfies C3.

This persists with symmetric error \(\varepsilon<1/2\): staying with the predicted action has causal value \(\varepsilon\), while switching has value \(1-\varepsilon\).

Structural C2 does **not** fail: neither city dominates the other across both possible Death locations.

The absence of ratifiable pure acts is a longstanding result, rather than a new objection specific to your framework. [joelvelasco.net](https://joelvelasco.net/teaching/5330%28fall2015%29/skyrms90-ratifiability_LOD.pdf?utm_source=chatgpt.com)

## 4.3 Bomb: the policy space has four elements

Once bomb status is observed, there are two information sets:
\[
h_{\mathrm{bomb}},\qquad h_{\mathrm{clear}}.
\]
Hence four policies:
\[
(a_{\mathrm{bomb}},a_{\mathrm{clear}})\in\{L,R\}^2.
\]

### An inconsistent interpretation

Suppose the predictor promises to predict the eventual action, while its prediction determines the observation:

- predicts \(R\): bomb;
- predicts \(L\): no bomb.

The policy
\[
a_{\mathrm{bomb}}=L,\qquad a_{\mathrm{clear}}=R
\]
makes the prediction wrong in every case.

Therefore no such predictor can have a uniform error bound below one over all four admissible policies.

### A coherent repair

Specify that the predictor targets the fixed coordinate
\[
\pi(h_{\mathrm{bomb}}),
\]
whether or not that information set is eventually reached.

Let death cost \(M>1\), and set
\[
\Pr(\mathrm{bomb}\mid a_{\mathrm{bomb}}=L)=\varepsilon,
\quad
\Pr(\mathrm{bomb}\mid a_{\mathrm{bomb}}=R)=1-\varepsilon.
\]

The values are:

| Policy \((a_{\mathrm{bomb}},a_{\mathrm{clear}})\) | Ex-ante value |
|---|---:|
| \((L,L)\) | \(-M\varepsilon\) |
| \((L,R)\) | \(-M\varepsilon-(1-\varepsilon)\) |
| \((R,L)\) | \(-(1-\varepsilon)\) |
| \((R,R)\) | \(-1\) |

For
\[
\boxed{0<\varepsilon<\frac1{M+1},}
\]
C1 uniquely selects \((L,L)\), while C2 and C3 select \((R,L)\).

Your numbers satisfy this inequality.

But two qualifications matter:

1. At \(\varepsilon=0\), the bomb information set is unreached under \((L,L)\). The reached-only versions of C2 and C3 therefore do not oppose that policy.
2. If \(D\) is instead the already-conditioned problem “a bomb is visibly present,” its available values are \(-M\) and \(-1\). C1 then chooses Right.

MacAskill’s original essay supplies the visible-bomb challenge, but your utility scale and complete contingent-policy kernel are additional assumptions. [lesswrong.com](https://www.lesswrong.com/posts/ySLYSsNeFL5CoAQzN/a-critique-of-functional-decision-theory?utm_source=chatgpt.com)

---

# 5. Minimal inconsistent and maximal consistent sets — T3–T4

## 5.1 Explicit total theories

We need existence witnesses for consistent subsets, not merely examples on a few problems.

### A theory satisfying C1 and C4

On problems that are not commitment wrappers, choose an ex-ante maximizer.

Recursively, in \(K(D)\), commit to the policy already selected for \(D\).

Since
\[
V_{K(D)}(q)=V_D(q),
\]
this preserves C1 and satisfies C4 with exact policy agreement.

**C1 alone does not imply C4.** On a problem where both actions yield zero, an ex-ante maximizing lookup table could choose different tied actions in the original problem and its commitment extension.

### A theory satisfying C2

For every problem choose a fixed full-support measure \(\nu_D\) on \(S_D\), such as the uniform measure. Define
\[
T^\nu_D
=
\operatorname{first}\arg\max_{\pi}
\sum_s\nu_D(s)U_D(s,\pi).
\]

**Proof of C2.** Suppose its selected policy chooses a dominated action at a positively reached \(h\). Changing that action improves payoff in every structural state reaching \(h\) and leaves payoff unchanged elsewhere.

That set is nonempty, and \(\nu_D\) gives it positive probability. The change therefore strictly improves the defining objective, a contradiction. ∎

This selector is an existence witness; it need not be an attractive normative theory.

## 5.2 C2 and C4 are incompatible

Use exact Newcomb.

- In \(D\), C2 requires two-boxing.
- In \(K(D)\), committing to one-boxing yields 2; committing to two-boxing yields 1.

The commitment choice is an ordinary causal choice before the environment responds. One-box commitment therefore strictly dominates two-box commitment.

C2 requires committing to one-boxing, while C4 requires agreement with the original two-box prescription. Contradiction. ∎

## 5.3 Complete classification without C6

The inclusion-minimal inconsistent subsets are exactly
\[
\boxed{
\{C3\},\qquad
\{C1,C2\},\qquad
\{C2,C4\}.
}
\]

The maximal consistent subsets are exactly:

| Maximal consistent subset | Explicit theory |
|---|---|
| \(\{C1,C4,C5\}\) | Ex-ante maximization with coherent commitment choices |
| \(\{C2,C5\}\) | Maximization under a fixed full-support structural measure |

**Exhaustiveness proof.** A consistent set cannot contain C3. If it contains C2, it cannot contain C1 or C4. If it does not contain C2, its substantive members are contained in \(\{C1,C4\}\), which is satisfiable. C5 adds no restriction. ∎

Therefore, among C1–C5, **there is no minimally inconsistent family of three or more individually satisfiable criteria**.

Your requested minimality property is satisfied by \(\{C1,C2\}\) and \(\{C2,C4\}\): the singleton subsets have explicit total witnesses. But the first remains a direct pointwise disagreement.

---

# 6. Optional C6: a complete conditional classification

There is no unique C1–C6 table until the evidential joint law is fixed.

Under a deterministic selected policy, conditioning on an alternative action ordinarily means conditioning on a probability-zero event. The expression in C6 therefore cannot simply be read from the actual trajectory law.

Here is one explicit completion.

## 6.1 Reference-policy evidential law

Fix a full-support prior \(\kappa_D\) on \(\Pi_D\), for example uniform, and define
\[
J_D(\Pi=\pi,S=s)=\kappa_D(\pi)\mu_\pi(s).
\]

Under this reference law, let \(Y=U_D(S,\Pi)\), and define
\[
e_h(a)=\mathbb E_{J_D}[Y\mid h\text{ reached},\,\Pi(h)=a].
\]

Assign value \(-\infty\) to impossible action-conditioning events; entirely impossible information sets impose no restriction.

Define **C6\({}^\kappa\)** by maximizing these values at each positively reached information set.

This is a specified evidential criterion, **not an identification with every version of EDT**. In sequential problems, it evaluates continuation behavior using the reference distribution over policies.

A total satisfying theory exists: independently choose an \(e_h\)-maximizer at every \(h\). Full support ensures that any information set reachable under some actual policy has at least one finite evidential action value.

## 6.2 Additional incompatibilities

### C2 versus C6\({}^\kappa\)

In one-choice Newcomb, conditioning on the action identifies the complete policy:
\[
e(O)=V(O),\qquad e(B)=V(B).
\]
Thus C6\({}^\kappa\) one-boxes when \(\varepsilon<1/4\), conflicting with C2.

### C1 versus C6\({}^\kappa\)

Use counterfactual mugging:

- A fair coin is tossed.
- On heads, receive \(r\) iff a perfect predictor predicts that the tails prescription is Pay.
- On tails, choose Pay at cost \(c\), or Refuse at cost zero.
- Assume \(r>c>0\).

Then
\[
V(\mathrm{Pay})=\frac{r-c}{2}>0=V(\mathrm{Refuse}),
\]
so C1 requires Pay.

At the tails information set,
\[
e(\mathrm{Pay})=-c<0=e(\mathrm{Refuse}),
\]
so C6\({}^\kappa\) requires Refuse.

### C4 versus C6\({}^\kappa\)

In the mugging commitment extension,
\[
e_{\mathrm{commit}}(q)=V_D(q).
\]
C6\({}^\kappa\) therefore commits to Pay but chooses Refuse in the original problem. This violates C4.

## 6.3 Complete classification with this C6

The minimal inconsistent subsets are
\[
\boxed{
\begin{gathered}
\{C3\},\\
\{C1,C2\},\quad \{C2,C4\},\\
\{C1,C6^\kappa\},\quad
\{C2,C6^\kappa\},\quad
\{C4,C6^\kappa\}.
\end{gathered}}
\]

The maximal consistent subsets are:

| Maximal consistent subset | Explicit theory |
|---|---|
| \(\{C1,C4,C5\}\) | Coherent ex-ante selector |
| \(\{C2,C5\}\) | Fixed full-support structural-measure selector |
| \(\{C6^\kappa,C5\}\) | Local maximization of the reference evidential values |

**Exhaustiveness proof.** Among C1, C2, C4, and C6\({}^\kappa\), every pair except \(\{C1,C4\}\) is inconsistent. Each listed maximal set has a total witness. ∎

Different evidential semantics can change this table. The table is a theorem about the displayed definitions.

---

# 7. Robustness — T5

## 7.1 Perfect versus imperfect prediction

The scaled Newcomb conflict holds for every
\[
0\le\varepsilon<\tfrac14.
\]

With opaque-box prize \(M\) and two-box bonus \(c\), it holds when
\[
M(1-2\varepsilon)>c.
\]

Thus any symmetric predictor better than chance permits the conflict for suitable stakes. More generally, Theorem 3 applies whenever the two induced state distributions differ.

At \(\varepsilon=1/2\), this symmetric predictor carries no policy dependence, so this particular mechanism disappears.

## 7.2 Randomization does not reconcile C1 and C2

Let \(p\) be the probability of one-boxing.

For a distribution-observing predictor with
\[
\Pr(\mathrm{full}\mid p)=\varepsilon+(1-2\varepsilon)p,
\]
and an independently realized action,
\[
V(p)=1+2\varepsilon+(1-4\varepsilon)p.
\]

The same value formula holds if the predictor observes the sampled action and predicts it with symmetric error.

For \(\varepsilon<1/4\), C1 requires \(p=1\), while C2 requires \(p=0\).

### An exact approximate-impossibility result

Put \(g=1-4\varepsilon>0\). Define
\[
R_1(p)=\max_qV(q)-V(p),
\]
and let \(R_{\mathrm{causal}}\) be expected regret relative to the best action in the fixed realized state.

Then
\[
R_1(p)=g(1-p),\qquad
R_{\mathrm{causal}}(p)=p,
\]
so
\[
\boxed{\frac{R_1(p)}g+R_{\mathrm{causal}}(p)=1.}
\]

Consequently, simultaneous tolerances
\[
R_1\le\delta_1,\qquad R_{\mathrm{causal}}\le\delta_2
\]
are achievable exactly when
\[
\frac{\delta_1}{g}+\delta_2\ge1.
\]

This follows by solving
\[
1-\delta_1/g\le p\le\delta_2.
\]

At perfect prediction, every policy has regret at least \(1/2\) according to one of these two measures.

## 7.3 Mixed existence requires regularity

Merely allowing mixtures does not ensure either C1 or C3 is satisfiable.

### C1 counterexample

For \(p\in[0,1]\), let a binary environmental reward have success probability
\[
q(p)=
\begin{cases}
p,&p<1,\\
0,&p=1.
\end{cases}
\]
Payoff is the reward, independent of the realized action.

Then \(V(p)=q(p)\) has supremum 1 but no maximizer.

This is allowed by unrestricted distribution-dependent kernels.

### C3 counterexample

Let Death choose city 1 iff \(p\ge1/2\), where \(p\) is the agent’s probability of city 1.

- If \(p<1/2\), the unique causal best response is city 1.
- If \(p\ge1/2\), it is city 0.

No mixture ratifies itself, despite Death observing only the distribution.

### Positive theorem under continuity

For finite actions and states, suppose \(p\mapsto\mu_p\) is continuous and the action is independently sampled conditional on \(p\).

Then:

- C1 has a solution by compactness and continuity.
- C3 has a solution by Kakutani’s theorem.

For the second claim define
\[
Q(a;p)=\sum_s\mu_p(s)u(s,a),
\qquad
B(p)=\Delta\!\left(\arg\max_a Q(a;p)\right).
\]
The correspondence has nonempty compact convex values. Continuity of the finitely many \(Q(a;p)\) gives a closed graph. Kakutani supplies \(p\in B(p)\). ∎

Related existence theorems and their required assumptions are established by Halpern and, in a policy-dependent sequential model, Bell and colleagues. [cs.cornell.edu](https://www.cs.cornell.edu/info/people/halpern/papers/newcomb.pdf?utm_source=chatgpt.com)

### Predicting random samples needs additional semantics

For Death independently sampling the agent’s distribution, the usual symmetric model admits \(p=1/2\).

If Death predicts the realized private sample, the answer depends on whether the agent knows that sample and whether a deviation preserves or replaces its randomness. Conditioning on a revealed, perfectly predicted sample restores the deterministic instability.

A marginal support-optimality test can still accept \(p=1/2\) while ignoring correlations between the predictor and the actual sample. It should not be confused with a criterion preserving those correlations when evaluating the unchanged policy. Skyrms explicitly cautioned against an unconditional randomization rescue. [joelvelasco.net](https://joelvelasco.net/teaching/5330%28fall2015%29/skyrms90-ratifiability_LOD.pdf?utm_source=chatgpt.com)

## 7.4 Restrictions on unreached information sets

Newcomb has one information set reached with probability one under every policy. Therefore its impossibility survives all of these restrictions:

| Restriction on a prediction target | Newcomb survives? |
|---|---|
| Positive probability under the evaluated policy | Yes |
| Reached under every admissible policy | Yes |
| On the actual realized path | Yes |
| Already reached before the prediction occurs | No |

The final restriction removes anticipatory dependence.

In an ordinary causal tree, changing a later prescription cannot change the probability of reaching it. A positive conditional improvement at \(h\) therefore improves ex-ante value by reach probability times conditional gain. Hence an ex-ante optimum satisfies C3, and therefore C2.

Removing off-path predictions can remove particular witnesses such as counterfactual mugging and change the optional consistency table. It does not remove the central Newcomb incompatibility.

---

# 8. Taxonomy — T6

“Finitely many types” needs a specified equivalence relation.

## 8.1 Boolean classifications are automatically finite

Six yes/no verdicts produce at most \(2^6\) verdict vectors.

More generally, for \(k\) local criteria, the profile
\[
\mathcal S(D)=
\{I\subseteq\{1,\dots,k\}:
\text{some policy satisfies every criterion in }I\}
\]
has at most
\[
2^{2^k}
\]
possible values.

Thus a finite classification by joint-satisfiability profiles exists automatically. It need not help solve a problem. C4 must also be treated as a relation between problems, rather than silently counted as a local predicate.

## 8.2 Exact recommendation structures have infinitely many types

Define equivalence to require a bijection of policy spaces preserving each criterion’s acceptable policies.

In the continuous mixed model, infinitely many inequivalent problems exist even with two actions and one always-reached information set.

Choose distinct \(r_1,\ldots,r_n\in(0,1)\), and let
\[
\Pr(Y=1\mid p)
=
1-\prod_{i=1}^n(p-r_i)^2.
\]
Payoff is \(Y\), independent of the realized action.

This is a valid continuous probability because every squared factor lies in \([0,1]\).

Its value is maximized precisely at
\[
p\in\{r_1,\ldots,r_n\}.
\]
Thus exactly \(n\) policies satisfy C1.

Every policy satisfies C2 and C3 because, with \(Y\) fixed, the action has no payoff effect.

Problems with different \(n\) cannot be equivalent: a policy bijection preserving C1 would have to identify finite sets of different cardinalities. ∎

For deterministic policies, arbitrary finite matrices are already representable. Predict the chosen action \(i\) exactly and set
\[
U(s=i,a=j)=M_{ij}.
\]
Then C1 selects maximal diagonal entries, while C3 accepts exactly those \(i\) whose diagonal entry is maximal in row \(i\). The framework therefore contains arbitrary finite recommendation structures.

## 8.3 No finite benchmark suite certifies arbitrary lookup tables

There is an even more direct consequence of your permissive theory definition.

**Theorem.** No fixed finite suite of problems can establish that an arbitrary lookup-table theory satisfies C1 everywhere.

**Proof.** Start with the universal ex-ante maximizing theory. Choose an ordinary two-action problem outside the finite suite, with one strictly better action. Change the theory only on that problem to select the worse action.

The original and modified theories agree on every benchmark, but only the original satisfies C1 everywhere. ∎

This remains true even if every benchmark and the omitted problem belong to the same intuitive “type.” Representative testing requires an additional invariance requirement on theories.

Finally, infinitely many equivalence classes do **not** imply the absence of a finite-dimensional parameterization. A single real parameter already indexes infinitely many cases.

---

# 9. Literature, Arrow-style results, and novelty — T7

## 9.1 Briggs already proves a related Arrow-style impossibility

R. A. Briggs’s **“Decision-Theoretic Paradoxes as Voting Paradoxes” (2010), §6** proves incompatibility between Pareto and self-sovereignty requirements on decision-theoretic rankings. [Download on Academia](https://www.academia.edu/2307714/Decision_Theoretic_Paradoxes_as_Voting_Paradoxes?utm_source=chatgpt.com)

In notation adapted here, let \(M_{ba}\) be candidate \(a\)’s causal value conditional on choosing \(b\).

- **Pareto:** unanimous weak preference across rows, with one strict preference, requires strict overall preference.
- **Self-sovereignty:** the comparison of \(a,b\) depends only on their two complete rows.

Consider
\[
M^+=
\begin{pmatrix}
0&0&-1\\
0&0&-1\\
1&0&-1
\end{pmatrix},
\qquad
M^-=
\begin{pmatrix}
0&0&-1\\
0&0&-1\\
0&1&-1
\end{pmatrix}.
\]

Pareto requires \(a>b\) in the first and \(b>a\) in the second. The two relevant rows are unchanged, so self-sovereignty forbids the reversal.

Positive weighted column averages satisfy Pareto; diagonal scores satisfy self-sovereignty. Thus the pair is minimally inconsistent.

This concerns rankings and cross-problem independence. Importing it into your policy-only framework requires that additional structure; it is not a theorem against unrestricted ex-ante selection.

## 9.2 Skalse’s general counterexample and the diagonal issue

Skalse’s **“A General Counterexample to Any Decision Theory and Some Responses” (2021)** explicitly targets arbitrary decision theories. Its environment references a fixed target theory and rewards the evaluated agent according to its action. It should therefore **not** be dismissed merely as direct identity discrimination. [arxiv.org](https://arxiv.org/pdf/2101.00280?utm_source=chatgpt.com)

Under your fully specified finite model, however, a self-referential environment must first exist.

Consider
\[
D_b:\qquad u(a)=\mathbf1\{a\ne b\}.
\]
The intended diagonal needs
\[
b=T(D_b).
\]
But an ex-ante optimizer has
\[
T(D_0)=1,\qquad T(D_1)=0.
\]
No required fixed point exists.

This is a model-specific well-definedness objection, not a proof that fixed reference algorithms are unfair.

Lewis’s **“Why Ain’cha Rich?” (1981)** already analyzes a related failure: an announced reward for supposedly irrational choice can make the proposed scenario self-contradictory. [andrewmbailey.com](https://andrewmbailey.com/dkl/Why_Aincha_Rich.pdf?utm_source=chatgpt.com)

## 9.3 Sources requested in your checklist

| Source | Relevance and limit |
|---|---|
| **Nozick (1969), “Newcomb’s Problem and Two Principles of Choice,” pp. 114–146** | The classical expected-utility/dominance conflict. The central C1/C2 observation is not new. [danielhoek.com](https://danielhoek.com/wp-content/uploads/2020/02/Nozick-Newcombs-Problem-and-Two-Principles-of-Choice.pdf?utm_source=chatgpt.com) |
| **Gibbard & Harper (1978), “Counterfactuals and Two Kinds of Expected Utility,” pp. 125–162** | Foundational distinction between causal counterfactual evaluation and evidential conditioning; a central source for the stability debate. [Springer Nature Link](https://link.springer.com/content/pdf/10.1007/978-94-009-9789-9_5?utm_source=chatgpt.com) |
| **Jeffrey (1983), *The Logic of Decision*, 2nd ed.; Skyrms (1990), “Ratifiability and the Logic of Decision,” pp. 44–56** | Ratifiability as an equilibrium requirement, with substantive self-knowledge and existence assumptions. I verified Jeffrey’s formulation through the retrieved primary discussions rather than a complete inspection of his book. [joelvelasco.net](https://joelvelasco.net/teaching/5330%28fall2015%29/skyrms90-ratifiability_LOD.pdf?utm_source=chatgpt.com) |
| **Lewis (1979), “Prisoners’ Dilemma Is a Newcomb Problem”; Lewis (1981), “Causal Decision Theory”** | Connects Newcomb and correlated PD choices; formalizes causal evaluation using dependency hypotheses. [andrewmbailey.com](https://andrewmbailey.com/dkl/Prisoners_Dilemma.pdf?utm_source=chatgpt.com) |
| **Ahmed (2014), *Evidence, Decision and Causality*; “Dicing with Death”** | Defense of EDT and criticism of CDT, including the value of access to unpredictable randomization. These are not universal no-lookup-table theorems. [cambridge.org](https://www.cambridge.org/core/books/evidence-decision-and-causality/7077949D2CD42E99C08D4FBFE5321148?utm_source=chatgpt.com) |
| **Hare & Hedden (2016; online 2015), “Self-Reinforcing and Self-Frustrating Decisions,” *Noûs* 50: 604–628** | Investigates decision dependence and self-frustrating deliberation. Relevant to C3 and endogenous beliefs. [web.mit.edu](https://web.mit.edu/~casparh/www/Papers/HareHeddenSelfReinforcing.pdf?utm_source=chatgpt.com) |
| **Oesterheld & Conitzer (2021), “Extracting Money from Causal Decision Theorists,” *Philosophical Quarterly* 71: 701–716** | Predictive offers and a sequential money-loss argument against CDT. Its target is narrower than every possible decision theory. [academic.oup.com](https://academic.oup.com/pq/article/71/4/pqaa086/6118001?utm_source=chatgpt.com) |
| **Yudkowsky & Soares (2017; revised 2018), “Functional Decision Theory”** | Proposes function-output counterfactuals and discusses fairness. It explicitly leaves formal fairness and general optimality unresolved. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com) |
| **MacAskill (2019), “A Critique of Functional Decision Theory”** | Source of Bomb and criticism of guaranteed-payoff violations. It does not uniquely specify your complete policy-dependent model. [lesswrong.com](https://www.lesswrong.com/posts/ySLYSsNeFL5CoAQzN/a-critique-of-functional-decision-theory?utm_source=chatgpt.com) |

Three further mathematical connections deserve attention:

- **Halpern, “A Note on the Existence of Ratifiable Acts”** supplies sufficient conditions for mixed ratifiability and explains why randomization alone is insufficient. [cs.cornell.edu](https://www.cs.cornell.edu/info/people/halpern/papers/newcomb.pdf?utm_source=chatgpt.com)
- **Bell, Linsefors, Oesterheld & Skalse (2021), “Reinforcement Learning in Newcomblike Environments”** is particularly close to your policy-dependent framework. It distinguishes optimality from ratifiability and proves a continuity-based existence theorem. [proceedings.neurips.cc](https://proceedings.neurips.cc/paper/2021/file/b9ed18a301c9f3d183938c451fa183df-Paper.pdf?utm_source=chatgpt.com)
- **MacDermott, Everitt & Belardinelli (2023)** characterize decision theories using mechanised causal graphs. **Cooper, Oesterheld & Conitzer (2024)** study conditions under which modified self-locating beliefs align causal recommendations with ex-ante policy optimization. These reinforce the need to fix intervention and belief semantics before comparing labels. [arxiv.org](https://arxiv.org/abs/2307.10987?utm_source=chatgpt.com)

I did not find a published theorem giving exactly the consistency tables above for exactly these completed definitions. That is a bounded search result, not an originality claim.

## 9.4 Corrections to the proposed “known positions”

**CDT \(\approx\) C2 + C3 is too strong.** Maximizing causal expected utility relative to a given belief state differs from requiring the resulting choice and its induced beliefs to form a fixed point. Failure of deterministic ratifiability does not show that every version of CDT is undefined. This distinction is explicit in the ratifiability literature. [joelvelasco.net](https://joelvelasco.net/teaching/5330%28fall2015%29/skyrms90-ratifiability_LOD.pdf?utm_source=chatgpt.com)

**EDT \(\approx\) C6 requires an epistemic model.** Specify the joint law, self-knowledge, zero-probability conditionals, and treatment of future choices.

**FDT \(\approx\) C1 is not an established equivalence.** The FDT paper needs a theory of computational counterfactual dependence and does not prove universal ex-ante maximization on your class. Its discussion even treats punishment for matching a fixed agent as intuitively unfair, whereas your fairness clause permits fixed environmental algorithms. [arxiv.org](https://arxiv.org/pdf/1710.05060?utm_source=chatgpt.com)

The neutral label for the constructed optimizer is **ex-ante policy maximization**.

---

# 10. Stipulations and a defensible thesis

The results above make the following choices explicit:

1. Policies are deterministic unless a mixed variant is stated.
2. Every admissible policy has a well-defined induced probability law.
3. Information sets do not repeat on a path.
4. Structural environmental responses, including alternative-branch responses, are part of the model.
5. Causal deviations freeze the baseline distribution over those responses.
6. Other policy prescriptions remain fixed during a local deviation.
7. C2 quantifies over structural states, including baseline probability-zero states.
8. Positive reach is measured under the evaluated policy.
9. Predictor error is specified by a kernel; the Newcomb calculations use symmetric error.
10. A predictor targets specified policy coordinates; “same computation” is represented by stipulated dependence.
11. Commitment is irrevocable, occurs before environmental response, and offers the full policy set.
12. Commitment extensions are canonically identified for cross-problem consistency.
13. C5 is totality already built into the definition of a theory.
14. The optional C6 uses the displayed reference-policy law and null-event convention.
15. Mixed variants additionally specify sampling, predictor access, information, counterfactual coupling, and continuity.
16. Taxonomy claims specify what an equivalence must preserve.

A defensible replacement for the opening thesis is:

> **On any class of well-defined, action-extensional decision problems containing a sufficiently predictive Newcomb problem, no policy assignment can satisfy both ex-ante optimality and statewise causal dominance. The conflict occurs within a single always-reached choice and survives imperfect prediction and randomization. Nevertheless, a universally ex-ante-optimal assignment exists. Stronger consistency classifications depend on explicit definitions of causal state, commitment, evidential conditioning, and randomized interventions.**

That statement preserves the valid impossibility, makes its scope precise, and leaves room for the positive existence result that your unrestricted lookup-table definition entails.