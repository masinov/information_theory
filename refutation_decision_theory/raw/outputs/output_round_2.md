## Result

There are two distinct answers, depending on whether the optional row-translation invariance is included.

1. **With A2 interpreted as a common positive affine transformation, the proposed family has no minimal inconsistent subset of three or more axioms.** After fixing the ranking–choice relationship precisely, every inconsistency contains one of two singleton obstructions or four pairwise obstructions. Briggs already proves one of the central pairs.

2. **Adding independent translations of individual rows produces a sharp impossibility with four independent axioms:**
   \[
   \boxed{\text{Neutrality}+\text{row translations}+\text{contraction}+\text{nontriviality}.}
   \]
   Every proper subset is satisfiable. The theorem holds for arbitrary nonempty choice correspondences, without ordering, Pareto, or diagonal optimality.

3. **The noisy commitment question has different answers for C2 and A3.** Positive predictor error destroys the Newcomb commitment reversal based on structural dominance under **every** coupling. The reversal based on expectation-matrix Pareto survives whenever one-boxing has higher ex-ante value, independently of the coupling.

4. **The taxonomy becomes finite only under strong additional assumptions.** Neutrality, global affine invariance, across-size binary independence, and a complete transitive ranking leave exactly three rules: maximize the diagonal, minimize it, or tie everything. Without ordering, or with Briggs’s weaker independence, there remain \(2^{|\mathbb R|}\) distinct rules.

The qualifications about choice correspondences, row translations, and independence are essential. I make them explicit below.

---

# 1. Literature verification

## 1.1 Briggs: the relevant theorem is a pairwise impossibility

**R. A. Briggs, “Decision-Theoretic Paradoxes as Voting Paradoxes,” *The Philosophical Review* 119(1), 2010, pp. 1–30, §6. DOI: 10.1215/00318108-2009-024.**

Writing \(M_{ij}=V^i(j)\), Briggs’s theorem says that no unrestricted expected-value ranking satisfies both:

- **P:** columnwise weak superiority, strict in at least one row, requires strict preference;
- **S:** preserving the two candidates’ entire rows preserves their strict comparison.

This is precisely the ranking version of
\[
\boxed{A3+A6b}.
\]

Her S concerns the **same action set** and equality of the full rows. It does not impose principal-submatrix contraction. The contradiction does not require neutrality or transitivity. I give an explicit matrix instance in §3. Ordinary CDT’s prior weights are additional data; uniform column sums provide a witness that depends only on the matrix. [Download on Academia](https://www.academia.edu/2307714/Decision_Theoretic_Paradoxes_as_Voting_Paradoxes?utm_source=chatgpt.com)

Thus Briggs already settles an important part of P2 and rules out presenting \(A3+A6b\), or its stronger \(A3+A6\) version, as a new Arrow-style result.

## 1.2 Skalse: the self-reference needs a well-definedness assumption

**Joar Skalse, “A General Counterexample to Any Decision Theory and Some Responses,” arXiv:2101.00280, 2021.**

Skalse proposes, for a fixed target theory \(XDT\), a choice between a transparent box containing \(1000\) and an opaque box. The opaque amount is \(0\) if \(XDT\) permits choosing it in that problem, and \(2000\) otherwise. He argues that another theory can outperform \(XDT\), while discussing objections about fairness and equivalence of decision situations. The target theory is an environmental constant; this is not simply punishment based on the evaluated agent’s identity. [arxiv.org](https://arxiv.org/pdf/2101.00280?utm_source=chatgpt.com)

**Translation into your extensional model:** the construction requires a fixed point specifying the opaque amount. For a diagonal-maximizing theory:

- If the amount is \(0\), the theory chooses transparent, which requires the amount to be \(2000\).
- If it is \(2000\), the theory chooses opaque, which requires the amount to be \(0\).

Neither amount gives a well-defined instance of the stipulated construction. This is our model-specific inference, not Skalse’s stated conclusion.

Consequently, the schema does **not** refute R1 on the class of fully specified, well-defined matrices. Its additional self-referential realizability assumption is where it leaves that class.

## 1.3 Bell et al. and Halpern: existence under specified mixing assumptions

**James Bell, Linda Linsefors, Caspar Oesterheld, and Joar Skalse, “Reinforcement Learning in Newcomblike Environments,” NeurIPS 34, 2021, Theorem 3.**

Their theorem states:

> Every continuous NDP has a strongly ratifiable policy.

Their Newcomblike decision processes have finite states and actions, bounded rewards, discount factor below one, and transitions and rewards that depend continuously on the policy distribution. Strong ratifiability requires every supported action to maximize its causal \(q_\pi\)-value. This establishes mixed existence; it does not identify ratifiable policies with ex-ante maximizers. [proceedings.neurips.cc](https://proceedings.neurips.cc/paper/2021/file/b9ed18a301c9f3d183938c451fa183df-Paper.pdf?utm_source=chatgpt.com)

**Joseph Y. Halpern, “A Note on the Existence of Ratifiable Acts,” *The Review of Symbolic Logic* 13(3), 2020, pp. 503–508; manuscript 2018, Definition 2.1 and Theorem 2.2. DOI: 10.1017/S175502031800028X.**

Halpern defines ratifiability by
\[
E_{P(\cdot\mid a)}[u(a)]
\ge E_{P(\cdot\mid a)}[u(b)]
\quad\text{for every }b.
\]
His existence theorem assumes statewise mixing of outcomes and an affine extension of conditional state probabilities:
\[
P^*(\cdot\mid \alpha a+(1-\alpha)b)
=
\alpha P(\cdot\mid a)+(1-\alpha)P(\cdot\mid b).
\]
He explicitly treats the latter as substantive. Randomization alone does not guarantee existence under arbitrary predictive semantics. [cs.cornell.edu](https://www.cs.cornell.edu/info/people/halpern/papers/newcomb.pdf?utm_source=chatgpt.com)

## 1.4 Other relevant precedents

**Felix Brandt and Paul Harrenstein, “Set-Rationalizable Choice and Self-Stability,” *Journal of Economic Theory* 146(4), 2011, pp. 1721–1731, §2.** They distinguish contraction \(\alpha\), expansion \(\gamma\), and rationalization by a complete transitive relation. Their cyclic binary-choice example exhibits the familiar obstruction to contraction-consistent nonempty choice. This is relevant to the proof of \(A3+A7\), although your restriction operation additionally deletes the corresponding rows. 

A related result in a different domain is **Arkarup Basu Mallik and Mihir Bhattacharya, “Consistency and social choice: Possibilities and impossibilities,” *Mathematical Social Sciences*, 2026, article 102582, DOI: 10.1016/j.mathsocsci.2026.102582**. The publisher reports an impossibility involving contraction consistency, Pareto efficiency, and anonymity or non-dictatorship. It uses a fixed electorate; your principal restriction removes voters and candidates together, so the translation is not direct. [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0165489626000892?utm_source=chatgpt.com)

The circulant construction used in §4 also has a close precedent, identified there. I found no earlier statement of the exact row-translation theorem below, but that is not sufficient to establish bibliographic novelty.

---

# 2. Precise conventions

A complete consistency map requires fixing ambiguities in A0, A6, A8, and A9.

## 2.1 Domain and outputs

Let \(I\) range over all finite nonempty subsets of a fixed infinite label universe. Matrices are \(M\in\mathbb R^{I\times I}\); restrictions preserve labels.

A rule supplies a reflexive relation \(\succeq_M\), with strict part \(\succ_M\), and its recommendation is exactly
\[
G(M)=\{i\in I:\nexists j\in I\text{ with }j\succ_M i\}.
\]
Require
\[
G(M)\ne\varnothing
\]
for every matrix.

When A8 is omitted, the relation may be incomplete or intransitive. When A8 holds, it is a complete transitive weak order.

This convention makes the ranking axioms constrain the same relation that determines choices. It also ensures that dropping A8 does not permit a “decision theory” that recommends nothing.

A **single-valued deterministic neutral selector** would already be impossible on the zero \(2\times2\) matrix: swapping the two indices preserves the input but moves either possible answer. Choice correspondences avoid that separate obstruction.

## 2.2 Axiom notation

I use the following abbreviations.

| Symbol | Your axiom | Exact interpretation |
|---|---|---|
| \(N\) | A1 | Simultaneous-permutation neutrality |
| \(F\) | A2 | Invariance under \(M\mapsto aM+b\mathbf1\mathbf1^\top\), \(a>0\) |
| \(P\) | A3 | Columnwise weak dominance, strict somewhere, requires strict preference |
| \(L\) | A3r | The same comparison test using only the two candidates’ rows |
| \(D\) | A4 | \(G(M)\subseteq\arg\max_i M_{ii}\) |
| \(J\) | A5 | Every \(i\in G(M)\) maximizes row \(i\) |
| \(B\) | A6 | Each comparison agrees with its principal \(2\times2\) restriction, across sizes |
| \(S\) | A6b | On a fixed universe, preserving the candidates’ two full rows preserves their comparison |
| \(C\) | A7 | \(G(M)\cap K\subseteq G(M|_K)\) |
| \(O\) | A8 | The output relation is complete and transitive |
| \(Q\) | A9 | For some fixed \(I\), two matrices have different choice sets |

A0 is taken as **labeled matrix reduction**. Neutrality is separately imposed by \(N\). If “up to relabeling” in A0 already includes neutrality, then \(N\) is a background assumption and must not also be counted as an independent axiom.

Two immediate implications are
\[
B\Longrightarrow S,\qquad B\Longrightarrow C.
\]
For the second, a surviving alternative cannot acquire a new strict defeater when all surviving pairwise comparisons are unchanged.

## 2.3 Three distinctions that affect the answer

**First, I use the ranking version of A3 offered in the question.** Merely excluding dominated alternatives from a choice set that is otherwise disconnected from the comparison relation is a different axiom system.

**Second, A8 must concern the actual output relation.** Saying only “each \(G(M)\) is rationalizable by some weak order” is vacuous: any nonempty set can be placed in a top indifference class. Requiring one order to rationalize choices from *all restrictions of an ambient matrix* is stronger and already entails contraction.

**Third, A3 is not C2.** A3 compares expected-payoff columns. C2 compares structural outcomes, including stipulated zero-probability states. The matrix can lose information relevant to C2. Likewise, global matrix ratifiability need not coincide with local information-set ratifiability in a multistage problem. The witnesses below are single-choice problems, where the required comparisons are unambiguous.

---

# 3. Complete consistency map with global affine invariance

## Theorem 1: all minimal inconsistent subsets

Under the preceding convention, the inclusion-minimal inconsistent subsets are exactly
\[
\boxed{
\{L\},\quad
\{J\},\quad
\{P,D\},\quad
\{P,B\},\quad
\{P,S\},\quad
\{P,C\}.
}
\]

In your notation:
\[
\boxed{
\{A3r\},\
\{A5\},\
\{A3,A4\},\
\{A3,A6\},\
\{A3,A6b\},\
\{A3,A7\}.
}
\]

The maximal consistent subsets are exactly:

| Maximal consistent subset, with A0 understood | Explicit rule |
|---|---|
| \(\{N,F,P,O,Q\}\) | Rank by column sums \(\sum_k M_{ki}\) |
| \(\{N,F,D,B,S,C,O,Q\}\) | Rank by diagonal entries \(M_{ii}\) |

Thus **every inconsistency in this family contains a singleton or pair**.

## Proofs of the obstructions

### Restricted Pareto fails by itself for a total choice rule

Consider
\[
K=
\begin{pmatrix}
0&-1&1\\
1&0&-1\\
-1&1&0
\end{pmatrix}.
\]
Using the relevant two rows for each comparison, \(L\) requires
\[
1\succ 2,\qquad 2\succ 3,\qquad 3\succ 1.
\]
Every alternative has a strict defeater, so \(G(K)=\varnothing\).

This sharpens the suggested \(A3r+A8\) witness. If one permits bare cyclic rankings with no nonempty recommendation when A8 is absent, then the obstruction is instead the pair \(\{A3r,A8\}\). That is a different output convention.

### Pure global ratifiability fails by itself

For
\[
H=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]
neither action maximizes its own row. Hence \(J\) permits no choice.

### Pareto and diagonal optimality conflict

For
\[
N_0=
\begin{pmatrix}
2&3\\
0&1
\end{pmatrix},
\]
column 2 strictly dominates column 1, while action 1 uniquely maximizes the diagonal. Thus \(P\) requires action 2 and \(D\) requires action 1.

### Pareto and self-sovereignty conflict

Use
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
Pareto requires \(1\succ 2\) in \(M^+\), and \(2\succ 1\) in \(M^-\). Rows 1 and 2 are unchanged, contradicting \(S\). Their principal binary blocks are also unchanged, contradicting \(B\).

This is an explicit instance of Briggs’s theorem.

### Pareto and contraction conflict

Return to \(K\). Pareto in its binary restrictions forces
\[
G(K|_{\{1,2\}})=\{1\},\qquad
G(K|_{\{2,3\}})=\{2\},\qquad
G(K|_{\{1,3\}})=\{3\}.
\]
Every possible full-menu choice loses in one restriction containing it. Contraction would preserve that choice there. Hence no nonempty full-menu choice is possible.

The mechanism is the classical binary cycle; the substantive modeling choice is that restriction removes **both columns and their associated rows**.

## Proof of completeness

Column sums satisfy \(N,F,P,O,Q\). Diagonal ranking satisfies \(N,F,D,B,S,C,O,Q\).

Now take any axiom set avoiding the displayed obstructions.

- If it contains \(P\), it excludes \(D,B,S,C\), so it is contained in the column-sum set.
- If it omits \(P\), it is contained in the diagonal set.
- It cannot contain either singleton obstruction \(L\) or \(J\).

Therefore every remaining set has an explicit witness. This proves both the minimal-obstruction list and the maximal-consistency list.

### Checks on the proposed reference rules

Positive fixed-weight column averages satisfy \(P\); uniform weights additionally satisfy neutrality. Arbitrary fixed unequal weights require persistent labels or extra input data.

Maximin over rows does **not** satisfy the stated strong Pareto axiom. In
\[
\begin{pmatrix}
0&0\\
2&1
\end{pmatrix},
\]
column 1 weakly dominates column 2, but both column minima are zero.

The uniform structural-measure selector from Round 1 is generally not an A0 rule: its construction uses structural-state information that need not be recoverable from \(M\).

---

# 4. A sharp positive theorem with row translations

Introduce the optional axiom
\[
R:\qquad
G(M+b\mathbf1^\top)=G(M)
\quad\text{for every }b\in\mathbb R^I,
\]
and impose the analogous invariance on the relation when one is supplied.

This preserves every within-row payoff difference. It can change diagonal comparisons arbitrarily, so it is a **substantive causal invariance assumption**, not an ordinary change of utility units.

## Theorem 2: neutrality, row translations, and contraction force trivial choice

On the domain of all finite real square matrices, every nonempty choice correspondence satisfying \(N,R,C\) obeys
\[
\boxed{G(M)=I\quad\text{for every }M.}
\]

Consequently,
\[
\boxed{\{N,R,C,Q\}}
\]
is inconsistent.

This theorem needs no ranking or Pareto axiom.

### Proof

Normalize an arbitrary \(k\times k\) matrix by subtracting its diagonal entry from each row:
\[
Z_{ij}=M_{ij}-M_{ii}.
\]
Then \(Z_{ii}=0\) and \(G(Z)=G(M)\).

Embed \(Z\) as a principal submatrix of a circulant matrix. Choose
\[
v_i=2^i,\qquad i=0,\ldots,k-1,
\]
in \(\mathbb Z/m\mathbb Z\), with
\[
m>2(2^{k-1}-1).
\]
All ordered nonzero differences \(v_j-v_i\) are distinct modulo \(m\): positive integer differences have unique powers of two dividing them, and the bound prevents modular collisions.

Set
\[
f(0)=0,\qquad f(v_j-v_i)=Z_{ij},
\]
and assign arbitrary values to unused arguments. Define
\[
A_{uv}=f(v-u).
\]
The principal submatrix on the \(v_i\) is \(Z\). Cyclic shifts preserve \(A\) and act transitively on its indices.

Neutrality and nonemptiness imply that \(G(A)\) contains every index. Contraction then implies that every index of the embedded \(Z\) is selected. Undoing normalization gives \(G(M)=I\). \(\square\)

The distinct-difference circulant construction adapts **John Frederick Fink and Sergio Ruiz, “Every graph is an induced isopart of a circulant,” *Czechoslovak Mathematical Journal* 36(2), 1986, pp. 172–176, §2**, which uses powers-of-two labels for graph embeddings. The symmetry observation is also standard in tournament-choice theory. Neither ingredient should be claimed as new. [dml.cz](https://dml.cz/bitstream/handle/10338.dmlcz/102080/CzechMathJ_36-1986-2_2.pdf?utm_source=chatgpt.com)

## Independence of all four axioms

Each one-axiom deletion has an explicit witness:

| Omitted axiom | Rule satisfying the other three |
|---|---|
| \(N\) | The responsive fixed-label rule defined below |
| \(R\) | Diagonal maximization |
| \(C\) | Row-range maximization |
| \(Q\) | Choose every alternative |

All these rules can also satisfy global affine invariance and complete transitive ordering.

**Row-range rule.** Rank \(i\) by
\[
r_i=\max_jM_{ij}-\min_jM_{ij}.
\]
It is neutral, invariant under separate row translations, and nonconstant.

**Responsive fixed-label rule.** Fix two labels \(u,v\) as an adjacent block above all other labels in a fixed priority order. When both occur, rank them according to
\[
\operatorname{sign}(M_{uu}-M_{uv});
\]
otherwise retain the fixed priority order. All other comparisons are fixed. This is nonconstant, row-translation invariant, and contraction consistent, but not neutral.

Because each one-deletion subset is satisfiable, every proper subset is satisfiable. Thus the four-axiom family is minimal.

If neutrality is incorporated into A0 as a background requirement, the same result is a minimal **three-axiom** family relative to that background:
\[
\boxed{\{R,C,Q\}\quad\text{given neutrality}.}
\]

## A second four-axiom obstruction

There is also
\[
\boxed{\{N,R,B,Q\}}.
\]

To prove it, suppose some strict binary comparison occurs. Row translations make both diagonal entries zero. Copy its oriented off-diagonal pattern around three alternatives. Neutrality and binary independence force a strict three-cycle, leaving no maximal alternative.

Therefore \(N+R+B\) permits no strict comparisons anywhere, so \(G(M)=I\). The same deletion witnesses prove minimality, with row range used when \(B\) is omitted.

Unlike the contraction theorem, this argument uses the stipulated link between comparisons and nonempty maximal choice.

## The complete augmented consistency map

Adding \(R\) introduces exactly three additional minimal inconsistent subsets:
\[
\boxed{
\{R,D\},\qquad
\{N,R,B,Q\},\qquad
\{N,R,C,Q\}.
}
\]

The first follows because row translations can make either of two different actions the unique diagonal maximizer while leaving the output unchanged.

The maximal consistent sets are:

| Witness rule | Maximal consistent set |
|---|---|
| Column sums | \(\{N,F,P,R,O,Q\}\) |
| Diagonal ranking | \(\{N,F,D,B,S,C,O,Q\}\) |
| Row ranges | \(\{N,F,R,S,O,Q\}\) |
| Responsive fixed-label rule | \(\{F,R,B,S,C,O,Q\}\) |
| All tied | \(\{N,F,R,B,S,C,O\}\) |

**Exhaustiveness.** A set containing \(P\) is confined to the column-sum row by its pairwise conflicts. Without \(P\), a set omitting \(R\) fits the diagonal row. If \(R\) is present, \(D\) is excluded. With both \(N,Q\), the two four-axiom obstructions exclude \(B,C\), leaving row range. Without \(N\), the label rule applies; without \(Q\), the all-tied rule applies.

This proves that there are no further minimal inconsistent subsets.

**Domain qualification.** The contraction theorem needs arbitrarily large finite matrices. With a fixed maximum size \(n\), “choose everyone below size \(n\), and use row-range maxima at size \(n\)” satisfies \(N,R,C,Q\).

---

# 5. Commitment couplings: complete Newcomb characterization

Let the opaque prize be \(m>c>0\), with transparent bonus \(c\), and symmetric error \(\varepsilon\in[0,1]\).

The original causal matrix is
\[
M_D=
\begin{pmatrix}
m(1-\varepsilon)&m(1-\varepsilon)+c\\
m\varepsilon&m\varepsilon+c
\end{pmatrix},
\]
with indices \(O,B\).

Both structural C2 and matrix A3 require \(B\). The ex-ante advantage of \(O\) is
\[
g=m(1-2\varepsilon)-c.
\]

## 5.1 Definition of the commitment extension

Let a commitment state be a vector
\[
\omega=(s_q)_{q\in\Pi_D},
\]
distributed according to a coupling \(\lambda\) with marginals \(\mu_q\). Committing to \(q\) yields
\[
U_K(\omega,q)=U_D(s_q,q).
\]

The distribution \(\lambda\) is fixed independently of the commitment action. Therefore
\[
M_K[p,q]
=
E_\lambda[U_D(s_q,q)]
=
V_D(q)
\]
for every row \(p\).

**Every row of the commitment matrix is identical, for every coupling.**

For Newcomb,
\[
M_K=
\begin{pmatrix}
m(1-\varepsilon)&m\varepsilon+c\\
m(1-\varepsilon)&m\varepsilon+c
\end{pmatrix}.
\]

It follows that
\[
\boxed{A3+C4\text{ conflicts on this pair exactly when }g>0.}
\]
The original problem requires \(B\); the commitment problem requires \(O\). At \(g=0\), commitment to \(B\) is permitted; at \(g<0\), it is required.

For the scaled \(m=2,c=1\) witness, the conflicting range is
\[
0\le\varepsilon<\frac14,
\]
independently of \(\lambda\).

## 5.2 All couplings and structural dominance

Let \(X\) indicate a full opaque box under commitment to \(O\), and \(Y\) a full opaque box under commitment to \(B\). Then
\[
P(X=1)=1-\varepsilon,\qquad P(Y=1)=\varepsilon.
\]
Every coupling is determined by
\[
t=P(X=1,Y=1),\qquad
0\le t\le\min(\varepsilon,1-\varepsilon).
\]

| \((X,Y)\) | Probability | \(O\) payoff | \(B\) payoff | \(O-B\) |
|---|---:|---:|---:|---:|
| \((1,1)\) | \(t\) | \(m\) | \(m+c\) | \(-c\) |
| \((1,0)\) | \(1-\varepsilon-t\) | \(m\) | \(c\) | \(m-c\) |
| \((0,1)\) | \(\varepsilon-t\) | \(0\) | \(m+c\) | \(-m-c\) |
| \((0,0)\) | \(t\) | \(0\) | \(c\) | \(-c\) |

Take first the convention
\[
S_K=\operatorname{supp}\lambda.
\]

Then:

- \(O\) strictly dominates \(B\) **iff \(\varepsilon=0\)**.
- \(B\) strictly dominates \(O\) **iff**
  \[
  \varepsilon\ge\frac12,\qquad t=1-\varepsilon.
  \]
- Otherwise neither dominates.

The first statement has a particularly simple proof. At any positive error, \(O\) pays zero with positive probability, whereas \(B\) always pays at least \(c>0\). No coupling can make \(O\) even weakly dominate \(B\).

Thus the Newcomb pair gives a C2–C4 contradiction at exact prediction, but **not at positive error**: choosing \(B\) in both problems remains C2-permissible.

This concerns the particular witness pair. It does not establish consistency of C2 and C4 on an entire class of other noisy problems.

## 5.3 Zero-probability structural states must be stipulated

If instead
\[
S_K=\prod_q\operatorname{supp}\mu_q
\]
and zero-\(\lambda\) points remain structural states, C2 quantifies over the entire product.

For \(0<\varepsilon<1\), all four pairs are then structural states, and neither commitment dominates, regardless of the coupling. At \(\varepsilon=0\), the product is the single favorable pair \((1,0)\); at \(\varepsilon=1\), it is \((0,1)\).

Changing a probability law cannot change C2 when its structural state set is held fixed.

## 5.4 Shared noise does not rescue this witness

The three common couplings are:

| Coupling | \(t\) |
|---|---:|
| Independent/product | \(\varepsilon(1-\varepsilon)\) |
| Shared predictor-correctness bit | \(0\) |
| Comonotone realized-payoff coupling | \(\min(\varepsilon,1-\varepsilon)\) |

Shared **correctness** noise and comonotone **payoffs** are different couplings. Neither restores \(O\)-dominance at positive error.

Couplings can matter in other problems. For example,
\[
U=1+100Z,\qquad W=100Z
\]
with a shared Bernoulli \(Z\) gives \(U>W\) everywhere on that coupling’s support. Product coupling admits the reversing pair \(U=1,W=100\). These are different payoff marginals from noisy Newcomb.

## 5.5 General coupling criterion

For finite commitment-payoff laws \(\nu_U,\nu_W\):

- A coupling with \(U\ge W\) almost surely exists iff
  \[
  F_U(x)\le F_W(x)\quad\forall x.
  \]
- A coupling with \(U>W\) almost surely exists iff
  \[
  F_U(x)\le F_W(x^-)
  \quad\forall x\in\operatorname{supp}\nu_U.
  \]

Necessity follows from the inclusions
\[
\{U\le x\}\subseteq\{W\le x\},
\qquad
\{U\le x\}\subseteq\{W<x\},
\]
respectively. For sufficiency, use the same uniform quantile for both variables; the displayed inequalities give the required quantile ordering.

Equivalently, solve a finite transport problem with mass allowed only on pairs satisfying the desired inequality. A payoff coupling lifts to an underlying-state coupling by distributing mass within payoff fibers according to their conditional state laws.

For a general \(D\), the remaining C4 requirement is agreement: some C2-permitted original policy must agree, on its positively reached information sets, with a C2-permitted commitment. The transport inequalities determine which commitment policies are structurally dominated.

---

# 6. Taxonomy and finite certification

“Finitely many parameters” needs a cardinal or regularity interpretation. A finite-dimensional input space does not make an arbitrary rule on that space a finite-dimensional family.

## 6.1 Without binary independence: no finite real parameterization

Consider
\[
N_t=
\begin{pmatrix}
0&-1\\
t+1&t
\end{pmatrix},
\qquad 0<t<1.
\]
These lie in pairwise distinct orbits under simultaneous permutations and common positive affine transformations.

Without a permutation, preserving the zero entry forces the translation to vanish, and preserving \(-1\) forces the scale to be one. A swap reverses the order of the diagonal values, which a positive affine map cannot repair.

For every \(E\subseteq(0,1)\), choose action 1 on the orbit of \(N_t\) when \(t\in E\), and action 2 otherwise; elsewhere use diagonal ranking. Transport the binary ranking equivariantly over each orbit.

This gives
\[
2^{\mathfrak c},\qquad \mathfrak c=|\mathbb R|,
\]
distinct rules satisfying A0, \(N,F,O\). Finite tuples of real numbers have cardinality only \(\mathfrak c\). Therefore no fixed finite-real-parameter decoder describes all such rules. Indeed, even countably many real parameters do not suffice.

This argument uses the permission to have arbitrary lookup rules; it should not be carried unchanged into a class with added continuity or measurability restrictions.

### Finite benchmarks cannot certify A3 or A4

Given a finite suite, choose an untested orbit \(N_t\).

- Column 1 strictly dominates column 2. Changing a column-sum rule to select 2 on that orbit creates an A3 violation.
- The second diagonal is larger. Changing a diagonal rule to select 1 creates an A4 violation.

The modified rules retain neutrality, affine invariance, and matrixwise weak ordering, and agree on every test. The same construction defeats finite adaptive testing.

## 6.2 Binary independence without ordering still leaves arbitrary functions

Let \(E\subseteq\mathbb R\). For \(M_{ii}>M_{jj}\), declare
\[
i\succ_M j
\quad\Longleftrightarrow\quad
\frac{M_{ij}-M_{jj}}{M_{ii}-M_{jj}}\in E.
\]
Never strictly prefer a lower diagonal to a higher one; tie all remaining pairs.

This satisfies \(N,F,B\). Strict comparisons always decrease diagonal values, so there are no strict cycles and a maximal alternative always exists.

On
\[
M_t=
\begin{pmatrix}
1&t\\
0&0
\end{pmatrix},
\]
the choice is \(\{1\}\) when \(t\in E\), and \(\{1,2\}\) otherwise. Again there are \(2^{\mathfrak c}\) distinct rules.

For finite certification of A4, start with \(E=\mathbb R\), which is diagonal ranking. A finite test suite exposes only finitely many displayed ratios. Remove one untested ratio \(r\) from \(E\). All tests remain unchanged, but \(M_r\) now admits the inferior-diagonal action.

So **A6 alone does not make finite benchmarks sufficient**.

## 6.3 Binary independence plus ordering: exactly three rules

### Theorem 3

Under A0, \(N,F,B,O\), the only ranking rules are:

1. increasing diagonal order;
2. decreasing diagonal order;
3. universal indifference.

### Proof

First, equal-diagonal alternatives must tie. Otherwise, the same oriented binary pattern can be copied around a three-cycle. Binary independence and neutrality reproduce the cycle, contradicting weak ordering.

Next, give alternatives \(i,i'\) the same diagonal value and give them arbitrary, independently specified off-diagonal interactions with a third alternative \(j\). Since
\[
i\sim i',
\]
transitivity of the weak order requires \(i\) and \(i'\) to compare identically with \(j\).

Their interactions with \(j\) were arbitrary. Therefore a pairwise comparison cannot depend on either off-diagonal entry. It depends only on the two diagonal values.

Finally, positive affine transformations map any ordered pair \(x<y\) to any other ordered pair. The rule must consistently prefer the larger value, consistently prefer the smaller value, or always tie. All three possibilities satisfy the axioms. \(\square\)

Adding \(Q\) removes universal indifference. Adding \(D\) selects increasing diagonal order.

**Conditional certification:** one binary matrix with unequal diagonals distinguishes the three rules, so one test certifies A4 **provided the structural axioms are already established globally**. Finite observations do not themselves verify A6 or A8.

A3 has no compliant rule in this class. For example,
\[
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]
has equal diagonals but a strictly dominant first column; all three rules tie its actions.

## 6.4 Briggs’s independence does not produce this rigidity

Define
\[
r_i=
\frac{M_{ii}-\min_jM_{ij}}
{\max_jM_{ij}-\min_jM_{ij}},
\]
with \(r_i=0\) for a constant row.

For arbitrary \(E\subseteq(0,1)\), rank by
\[
s_i=\mathbf1_{\{r_i\in E\}}.
\]
These rules satisfy \(N,F,S,O\), and even separate positive affine transformations of rows.

On every \(2\times2\) matrix, all scores are zero: each \(r_i\) is an endpoint, \(0\) or \(1\). Yet on
\[
\begin{pmatrix}
t&0&1\\
1&0&1\\
1&1&0
\end{pmatrix},
\qquad 0<t<1,
\]
the scores are \((\mathbf1_{\{t\in E\}},0,0)\).

Thus \(2^{\mathfrak c}\) different rules have **identical behavior on every binary problem**.

The useful taxonomy is therefore:

| Assumptions beyond A0 | Size of rule family / certification |
|---|---|
| \(N,F,O\) | \(2^{\mathfrak c}\); finite tests cannot certify A3 or A4 |
| \(N,F,B\), without \(O\) | \(2^{\mathfrak c}\); finite tests cannot certify A4 |
| \(N,F,S,O\) | \(2^{\mathfrak c}\); all binary behavior can leave the rule undetermined |
| \(N,F,B,O\) | Exactly three ranking rules; one unequal-diagonal test distinguishes them |

---

# 7. Mixed policies: rigorous extensions and changed obstructions

A pure matrix does not determine how prediction responds to a mixed policy. Continuity alone does not specify that extension.

Here is one precise extension:
\[
\mu_p=\sum_i p_i\mu_i,
\]
with the actual action drawn independently from \(p\), conditional on the announced distribution. Then
\[
g(p)=p^\top M,\qquad V(p)=p^\top Mp.
\]

This differs from predicting the same sampled action, which can instead yield the linear value \(\sum_i p_iM_{ii}\).

Define:

- \(D_m\): maximize \(p^\top Mp\);
- \(J_m\): every supported action maximizes \(p^\top M\);
- \(P_m\): assign zero probability to weakly dominated columns.

## 7.1 Ratifiable mixed policies exist, including Pareto-compliant ones

For continuous causal values \(g\), the correspondence
\[
BR(p)=\arg\max_{q\in\Delta(I)}q\cdot g(p)
\]
has nonempty convex values and a closed graph. Kakutani gives \(p\in BR(p)\).

In the canonical matrix extension, \(P_m+J_m\) are jointly satisfiable. To prove this, let
\[
\Delta_\eta=\{p:p_i\ge\eta\},
\qquad 0<\eta<1/|I|.
\]
Kakutani supplies
\[
p^\eta\in
\arg\max_{q\in\Delta_\eta}(p^\eta)^\top Mq.
\]

If column \(a\) weakly dominates \(b\), full support makes \(a\)’s expected causal payoff strictly larger. Hence \(p^\eta_b=\eta\); otherwise moving mass from \(b\) to \(a\) improves the response.

Take a convergent subsequence as \(\eta\downarrow0\). Its limit assigns zero mass to every dominated column. For arbitrary \(q\), compare against
\[
q^\eta=(1-|I|\eta)q+\eta\mathbf1
\]
and pass to the limit. This gives
\[
p^\top Mp\ge p^\top Mq,
\]
so the limit is ratifiable as well.

## 7.2 The ex-ante/causal conflict survives

For
\[
M=
\begin{pmatrix}
2&3\\
0&1
\end{pmatrix},
\qquad p=(x,1-x),
\]
we have
\[
V(p)=1+x.
\]
Thus \(D_m\) uniquely selects \(x=1\), while both \(P_m\) and \(J_m\) select \(x=0\). The pairs
\[
\{P_m,D_m\},\qquad \{J_m,D_m\}
\]
remain inconsistent.

## 7.3 Single mixed policies introduce a new neutrality obstruction

For a rule selecting one probability vector, \(N+D_m\) is already inconsistent.

Take \(M=I_2\). Neutrality forces \(p=(1/2,1/2)\), but
\[
V(p)=p_1^2+p_2^2
\]
is maximized only at the two pure endpoints.

A neutral **correspondence of maximizing lotteries** exists; a single neutral maximizing lottery need not. Therefore the pure consistency map cannot simply be relabeled as a mixed map.

## 7.4 The four-axiom theorem survives a specified probabilistic contraction

For a single lottery rule \(L\), impose
\[
C_m:\qquad
L(M|_K)
=
\frac{L(M)|_K}{L(M)(K)}
\quad\text{whenever }L(M)(K)>0.
\]
This is conditional-renormalization consistency, stronger than merely preserving support.

Then
\[
\boxed{\{N,R,C_m,Q\}}
\]
is a minimal inconsistent family.

The circulant proof applies: neutrality forces the uniform lottery on the transitive extension; conditioning forces uniformity on every embedded normalized matrix; row translations force universal uniformity.

The deletion witnesses are uniform distributions over the winners of, respectively, the fixed-label rule, diagonal maximization, row-range maximization, and the all-tied rule.

By contrast, support contraction alone permits the nonconstant rule
\[
p_i\propto1+\frac{r_i}{r_{\max}},
\]
using row ranges and the uniform lottery when \(r_{\max}=0\). It has full support everywhere, satisfies \(N,F,R\), and automatically preserves support under restriction.

Thus a complete mixed consistency map requires choosing among genuinely different output and contraction semantics. The pure map above is complete; these mixed results are the extensions established here, rather than a claim that all mixed interpretations share it.

---

# 8. Optional evidential semantics

The matrix does not supply a unique evidential criterion without identifying the conditioning experiment.

Two natural choices illustrate the difference.

**Reference-policy law.** Choose a full-support reference distribution \(\rho\) and set
\[
P(I=i,s)=\rho_i\mu_i(s).
\]
Conditioning on policy index \(i\) yields \(\mu_i\), so the evidential value of \(i\) is
\[
E[U(s,i)\mid I=i]=M_{ii}.
\]
This semantics gives diagonal optimality.

**Conditioning on the realized action under a known mixed policy.** Under the independent-draw mixed model, the environment has law \(\mu_p\). Observing a positive-probability realized action does not change that law, so its conditional value is
\[
g_i(p).
\]
With an explicit completion for zero-probability alternatives, the resulting support-optimality condition is ratifiability.

These condition on different variables under different joint laws. Neither can be silently substituted for the other.

---

# 9. Final thesis and closure

The defensible conclusion is:

> **On the unrestricted domain of well-defined finite causal matrices, ex-ante optimization remains universally satisfiable. With global affine invariance, every inconsistency among the precisely defined A-family contains a singleton or pairwise core. Adding independent row translations yields a minimal four-axiom impossibility: no nonempty, neutral, contraction-consistent choice correspondence can both ignore row-specific additive constants and make a nontrivial selection.**

The status of the requested closure items is:

| Item | Result |
|---|---|
| P1: Briggs and Skalse | Verified and translated; Briggs is \(A3+A6b\), while Skalse requires self-referential realizability absent from the extensional model |
| P2: Complete pure consistency map | Given for both global affine invariance and the optional row-translation extension |
| P3: Sharp theorem or reduction | Both: a pairwise-core reduction for the base family, and independent four-axiom theorems for the extension |
| P4: Coupling gap | Resolved, including all binary couplings and the distinction between C2 and A3 |
| P5: Taxonomy | No finite real parameterization in the broad classes; exactly three rules under strong binary independence and ordering |
| P6–P7 | Precise mixed extensions and two evidential semantics, with their additional stipulations identified |

The central historical claims should remain modest. The Pareto/self-sovereignty pair is Briggs’s theorem. The contraction cycle uses established choice-theoretic machinery. The row-translation theorem and complete consistency classification are proved here, but the circulant construction has an explicit antecedent, and I have not established priority for the exact resulting theorem. The mathematical conclusion does not depend on a novelty claim.