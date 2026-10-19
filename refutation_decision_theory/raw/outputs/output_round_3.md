# Verdict

**The dichotomy is false as stated.** Three distinct results survive:

1. **Principal binary independence**, together with neutrality, affine invariance, ordering, nontriviality, and diagonal monotonicity, characterizes increasing-diagonal ranking.
2. **Principal contraction**, together with neutrality and row-translation invariance, forces the rule to recommend every option on a sufficiently rich domain. Ordering is unnecessary.
3. **Column contraction with a fixed belief model** permits nontrivial causal averaging satisfying neutrality, affine invariance, row invariance, Pareto, ordering, and monotonicity simultaneously.

Moreover, contraction—even principal contraction—does **not** by itself force diagonal evaluation when combined with ordering and monotonicity.

There is also an important attribution correction: **Podgorski’s Self-Esteem Theorem already establishes T3’s central diagonal-dependence result.** [abelardpodgorski.com](https://www.abelardpodgorski.com/uploads/5/4/0/0/54000997/tournament_decision_theory.pdf?utm_source=chatgpt.com)

Below I give the menu semantics, complete consistency maps, proofs, domain conditions, and literature assessment.

---

# 1. Definitions and menu semantics

I retain your model and matrix orientation:
\[
M_{ij}=\mathbb E_{\mu_i}[U(s,j)].
\]

The rule supplies a reflexive relation \(\succeq_M\), with strict part \(\succ_M\), and
\[
G(M)=\{i:\nexists j\text{ with }j\succ_M i\}\ne\varnothing.
\]

The invariance and independence axioms govern the **whole relation**. Contraction, diagonal optimality, and nontriviality govern its induced choice set. Ordering means a complete transitive relation **at each input**; it does not already assume one ranking shared across menus.

## 1.1 Principal restriction is the canonical reduced matrix

Suppose the surviving policies are \(K\subseteq\Pi_D\), and stipulate that their response laws and consequences remain unchanged:
\[
\mu'_i=\mu_i,\qquad U'(s,i)=U(s,i),\qquad i\in K.
\]
Then necessarily
\[
M_{D'}=M_D|_{K\times K}.
\]

Thus **principal restriction is forced by the definition of the causal matrix once this law-preserving interpretation of policy removal is stipulated**.

There are two qualifications.

First, arbitrary subsets of policies need not arise by pruning local action sets: local pruning generally produces product-shaped subsets of the policy space. An arbitrary \(K\) can instead be realized by treating the surviving policies as macroactions in a new one-choice predictive problem. That preserves the desired response laws, but need not preserve the original extensive-form tree.

Second, an actual intervention that announces a smaller menu may change how a predictor responds. The model itself does not require
\(\mu_i^{D'}=\mu_i^D\). Law preservation is an additional cross-problem assumption.

This macroaction construction must also be distinguished from **commitment before prediction**: moving the causal choice before the predictor changes the counterfactual structure and need not yield a principal submatrix.

## 1.2 Column restriction retains additional reference information

A precise rectangular domain is
\[
(J,A,M),\qquad \varnothing\ne A\subseteq J,\qquad M\in\mathbb R^{J\times A}.
\]

Here \(J\) indexes retained belief perspectives, \(A\) indexes available alternatives, and alternative \(a\) has distinguished “own row” \(a\). This association is needed to retain meaningful versions of \(D\), \(S\), and Mon.

Define
\[
(J,A,M)|_K=(J,K,M_{J\times K}),\qquad \varnothing\ne K\subseteq A.
\]

The off-menu rows are retained descriptions of the old conditional or counterfactual laws. They are **additional data**, not rows of the canonical causal matrix of the smaller problem: that canonical matrix remains square.

Accordingly, column restriction can describe a fair augmented decision problem, but it does not follow from reduction to \(M_{D'}\) alone.

## 1.3 Fixed-reference restriction

Supply a probability vector \(w\in\Delta(J)\), and evaluate
\[
v_a(M,w)=\sum_{j\in J}w_jM_{ja}.
\]

For genuinely fixed-reference restriction, retain \(J\) and \(w\) and delete only unavailable columns:
\[
(J,A,M,w)|_K=(J,K,M_{J\times K},w).
\]

Under relabeling, \(w\) must be relabeled too. Uniform weights give a rule depending only on the rectangular matrix.

A reference distribution over belief perspectives need not be the agent’s probability distribution over its **actually available choices**. If the latter is intended, eliminating possible choices ordinarily requires conditioning; keeping positive weight on eliminated choices requires a different interpretation.

### A useful exact result about changing the reference

Suppose \(w,w'\) are probability vectors on the same belief universe, with at least two surviving columns. Assume the update \(w\mapsto w'\) is determined independently of payoff entries.

> **Weight-preservation theorem.** Weighted averaging preserves all rankings for every payoff matrix iff \(w'=w\). The same condition is necessary for contraction to hold for every payoff matrix under that update.

**Proof.** A difference between two columns can be any \(x\in\mathbb R^J\). Identical rankings require
\[
\operatorname{sign}(w^\top x)=\operatorname{sign}(w'^\top x)
\quad\text{for every }x.
\]
The two linear functionals must therefore be positive scalar multiples. Normalization gives \(w'=w\).

If \(w'\ne w\), choose \(x\) with \(w^\top x=0<w'^\top x\), then replace \(x\) by \(x-\varepsilon\mathbf1\) for sufficiently small \(\varepsilon>0\). The two weightings strictly reverse the comparison. Set all removed columns sufficiently low to make the previously preferred surviving option a full-menu maximizer. Contraction then fails. ∎

Deleting rows and renormalizing their weights preserves all rankings only when the deleted rows originally had zero total weight. With full-support weights, proper row deletion changes the reference.

| Menu operation | Available columns | Belief rows/reference | Canonical law-preserving causal matrix? |
|---|---|---|---|
| Principal | Delete unavailable options | Delete their corresponding rows | Yes, subject to the policy-removal qualification |
| Column | Delete unavailable options | Retain every row | Requires augmented reference data |
| Fixed reference | Delete unavailable options | Retain \(J,w\) | Requires a supplied reference distribution |
| Delete rows and renormalize | Delete unavailable options | Change the reference | A different belief-update operation |

---

# 2. The complete consistency map under column restriction

There are **two inequivalent binary-independence axioms** on the rectangular domain.

- \(B_{\rm pr}\): compare \(a,b\) using their principal square \(2\times2\) matrix. This retains your original \(B\) literally.
- \(B_{\rm col}\): compare \(a,b\) after deleting other columns while retaining every row in \(J\).

They must not be conflated. In particular,
\[
B_{\rm pr}\Longrightarrow S,
\qquad
B_{\rm col}\not\Longrightarrow S.
\]

Both imply \(C_{\rm col}\).

For rectangular inputs, \(P\) quantifies over all \(J\), \(D\) maximizes \(M_{aa}\) over \(a\in A\), and \(Q\) means different choice sets for two numerical matrices on some fixed \((J,A)\).

## 2.1 Map with the original \(B=B_{\rm pr}\)

> **Theorem 1.** On all finite rectangular inputs just defined, the inclusion-minimal inconsistent subsets of
> \[
> \{N,F,R,P,D,B_{\rm pr},S,C_{\rm col},O,Q\}
> \]
> are exactly
> \[
> \boxed{
> \{P,D\},\quad
> \{P,B_{\rm pr}\},\quad
> \{P,S\},\quad
> \{R,D\},\quad
> \{N,R,B_{\rm pr},Q\}.
> }
> \]

The maximal consistent subsets and explicit witnesses are:

| Maximal consistent subset | Witness |
|---|---|
| \(\{N,F,R,P,C_{\rm col},O,Q\}\) | Rank by column sums |
| \(\{N,F,D,B_{\rm pr},S,C_{\rm col},O,Q\}\) | Rank by the diagonal |
| \(\{N,F,R,S,C_{\rm col},O,Q\}\) | Full-menu relative-score rule below |
| \(\{F,R,B_{\rm pr},S,C_{\rm col},O,Q\}\) | Responsive fixed-label rule below |
| \(\{N,F,R,B_{\rm pr},S,C_{\rm col},O\}\) | Universal indifference |

All these witnesses also satisfy Mon as defined in §4.

### Witness definitions

**Column sums.**
\[
s_a(M)=\sum_{j\in J}M_{ja}.
\]
Row additions add the same number to every score. Deleting columns leaves surviving scores unchanged. Positive weights establish \(P\).

**Diagonal ranking.**
\[
a\succeq_M b\iff M_{aa}\ge M_{bb}.
\]

**Full-menu relative-score rule.** If \(A=J\), rank by
\[
s_a(M)=M_{aa}-\frac1{|A|}\sum_{c\in A}M_{ac}.
\]
If \(A\subsetneq J\), tie every available option. Proper column contraction leads to universal choice, establishing \(C_{\rm col}\). Comparisons on full menus depend only on the candidates’ two rows, establishing \(S\).

**Responsive fixed-label rule.** Fix two labels \(u,v\), placed together above all other labels in a permanent priority order. Their mutual comparison is determined by the sign of
\[
M_{uu}-M_{uv}.
\]
All other comparisons follow the permanent priority order. This rule is responsive, row invariant, ordered, and independent under either restriction, but not neutral.

### Proofs of inconsistency

**\(\{P,D\}\).** On
\[
\begin{pmatrix}
2&3\\
0&1
\end{pmatrix},
\]
\(D\) permits only option 1, while \(P\) requires \(2\succ1\).

**\(\{R,D\}\).** Independent row additions can change which diagonal entry is uniquely largest while \(R\) requires the output to remain unchanged.

**\(\{P,S\}\).** Consider
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
The candidates’ first two rows are identical across problems. Pareto requires \(1\succ2\) in the first and \(2\succ1\) in the second, contradicting \(S\). This is the Briggs obstruction. [Download on Academia](https://www.academia.edu/2307714/Decision_Theoretic_Paradoxes_as_Voting_Paradoxes?utm_source=chatgpt.com)

**\(\{P,B_{\rm pr}\}\).** Follows from \(B_{\rm pr}\Rightarrow S\).

**\(\{N,R,B_{\rm pr},Q\}\).** Nontrivial choice requires some strict comparison. By \(B_{\rm pr}\), it occurs in a binary matrix; by \(R\), normalize its diagonal to zero:
\[
H=\begin{pmatrix}0&x\\y&0\end{pmatrix}.
\]
Relabel so that \(1\succ2\). Now form
\[
C=
\begin{pmatrix}
0&x&y\\
y&0&x\\
x&y&0
\end{pmatrix}.
\]
Neutrality and binary independence force
\[
1\succ2,\qquad2\succ3,\qquad3\succ1.
\]
Then \(G(C)=\varnothing\), a contradiction. Thus every option must always be chosen, violating \(Q\).

### Why the map is complete

Any axiom set avoiding the displayed cores is contained in one of the five maximal sets:

- If it contains \(P\), it excludes \(D,B_{\rm pr},S\), and column sums witness it.
- Without \(P\), if it excludes \(R\), diagonal ranking witnesses it.
- With \(R\), it excludes \(D\), and must omit at least one of \(N,B_{\rm pr},Q\). The last three witnesses cover those cases.

This proves both exhaustiveness and independence.

## 2.2 Map if binary restriction also retains the belief rows

Replace \(B_{\rm pr}\) by \(B_{\rm col}\), retaining the original existential \(Q\).

> **Theorem 2.** The minimal inconsistent subsets are exactly
> \[
> \boxed{\{P,D\},\quad\{P,S\},\quad\{R,D\}.}
> \]

| Maximal consistent subset | Witness |
|---|---|
| \(\{N,F,R,P,B_{\rm col},C_{\rm col},O,Q\}\) | Column sums |
| \(\{N,F,D,B_{\rm col},S,C_{\rm col},O,Q\}\) | Diagonal ranking |
| \(\{N,F,R,B_{\rm col},S,C_{\rm col},O,Q\}\) | Binary-universe rule below |

For the last witness, use the relative scores
\[
s_a=M_{aa}-M_{ab}
\]
when \(J=A=\{a,b\}\); tie everyone whenever \(|J|\ge3\). Singleton menus are automatic.

This satisfies \(Q\) on a two-row universe. \(B_{\rm col}\) never connects different belief universes, so it does not force the rule’s two-row behavior to extend to three rows.

The same containment argument proves exhaustiveness.

### A stronger, genuinely independent replacement

The weakness of existential \(Q\) matters. Fix a belief universe \(J\) with \(|J|\ge3\), allow all its menus, and require numerical responsiveness on that universe. Call this \(Q_J\).

Then
\[
\boxed{\{N,R,B_{\rm col},S,Q_J\}}
\]
is a **minimal inconsistent family of five axioms**.

**Proof.** On a binary menu, \(S\) removes dependence on the other belief rows. Row invariance normalizes the candidates’ two diagonal entries. Neutrality permits cyclic replication of any strict binary comparison; \(B_{\rm col}\) transfers the resulting comparisons to a three-option menu. Every option is then strictly beaten. Hence no strict comparison can occur, contradicting \(Q_J\).

Every one-axiom deletion is witnessed respectively by:

| Omitted axiom | Witness satisfying the other four |
|---|---|
| \(N\) | Responsive fixed-label rule |
| \(R\) | Diagonal ranking |
| \(B_{\rm col}\) | Full-menu relative-score rule |
| \(S\) | Column sums |
| \(Q_J\) | Universal indifference |

The witnesses can additionally satisfy \(F,C_{\rm col},O,\mathrm{Mon}\).

Thus the strongest replacement depends on whether nontriviality is required on a universe large enough to support the obstruction.

---

# 3. What survives of T2 under the three semantics?

## 3.1 Principal contraction

> **Theorem 3 — principal-contraction triviality.** On all finite real square matrices,
> \[
> N+R+C_{\rm pr}
> \quad\Longrightarrow\quad
> G(M)=I_M\text{ for every }M.
> \]
> Therefore \(\{N,R,C_{\rm pr},Q\}\) is inconsistent.

Here is the full embedding proof. Normalize
\[
A_{ij}=M_{ij}-M_{ii}.
\]
Choose \(g_i=2^i\), \(i=0,\ldots,n-1\), and
\[
m>2(2^{n-1}-1).
\]
The nonzero ordered differences \(g_j-g_i\bmod m\) are distinct: their powers of two and odd parts identify the ordered pair, and the bound prevents wraparound collisions.

Define a circulant
\[
C_{xy}=f(y-x\bmod m)
\]
by
\[
f(0)=0,\qquad f(g_j-g_i)=A_{ij},
\]
filling unused entries arbitrarily. Its indicated principal submatrix is \(A\). Neutrality and nonempty choice force every vertex of the circulant to be chosen. Contraction forces \(G(A)=I_A\); row invariance gives \(G(M)=I_M\). ∎

The graph-embedding precedent is Fink and Ruiz; the real-weighted construction above supplies the version required here. [dml.cz](https://dml.cz/bitstream/handle/10338.dmlcz/102080/CzechMathJ_36-1986-2_2.pdf?utm_source=chatgpt.com)

Without \(O\), the conclusion is **universal choice**, not necessarily universal indifference: incomparabilities could remain.

The four-axiom family is minimal. Omitting \(N,R,C_{\rm pr},Q\), respectively, permits the fixed-label rule, diagonal ranking, square relative-score ranking, and universal indifference.

## 3.2 Column contraction

The theorem fails strongly. Uniform column averaging satisfies
\[
\boxed{N,F,R,P,B_{\rm col},C_{\rm col},O,Q,\mathrm{Mon}.}
\]

Consequently, no impossibility can be obtained from any subset of these axioms under this semantics. The remaining obstructions are exactly those in §2.

A small matrix makes the semantic difference visible:
\[
W=
\begin{pmatrix}
0&-1&1\\
1&0&-1\\
-1&1&0
\end{pmatrix}.
\]
Its column sums tie. Under principal binary restriction, Pareto successively forces \(1\) over \(2\), \(2\) over \(3\), and \(3\) over \(1\), establishing \(\{P,C_{\rm pr}\}\) inconsistency. Under column restriction, the third row remains and prevents those binary Pareto judgments; column averaging continues to tie.

## 3.3 Fixed-reference contraction

With \(J,w\) retained, weighted averaging supplies the same counterexample. Full support gives \(P\).

If instead rows are removed and the prior renormalized, the weight-preservation theorem shows why averaging loses universal contraction. That is a change of reference, not the fixed-reference operation defined above.

These distinctions settle the first half of the proposed dichotomy: **row-invariant evaluation can be menu coherent when the belief model remains fixed**.

---

# 4. Exact characterization under binary independence

Define Mon precisely. If
\[
M'=M+\delta E_{ii},\qquad\delta\ge0,
\]
then:

- \(i\in G(M)\Rightarrow i\in G(M')\);
- every previously true \(i\succeq_M j\) remains true;
- every previously true \(i\succ_M j\) remains true.

The choice-preservation clause alone suffices to eliminate decreasing-diagonal ranking below.

## 4.1 Characterization before affine invariance

> **Theorem 4 — relational Self-Esteem characterization.** On the unrestricted square domain, \(N+B_{\rm pr}+O\) holds iff there is a single complete transitive relation \(\succeq^\ast\) on \(\mathbb R\) such that
> \[
> i\succeq_M j
> \iff
> M_{ii}\succeq^\ast M_{jj}.
> \]

This is the relational version of the central result in **Abelard Podgorski, “Tournament Decision Theory,” *Noûs* 56(1):176–203 (2022; online 2020)**, “The Self-Esteem Theorem,” author-version pp. 22–23, proof p. 38. His common binary-comparison function and scalar overall evaluation supply the corresponding neutrality and ordering conditions. [abelardpodgorski.com](https://www.abelardpodgorski.com/uploads/5/4/0/0/54000997/tournament_decision_theory.pdf?utm_source=chatgpt.com)

**Proof.** Consider
\[
H=
\begin{pmatrix}
p&r&p\\
q&s&u\\
p&t&p
\end{pmatrix}.
\]
The principal pair \(\{1,3\}\) is constant. Neutrality, ordering, and \(B_{\rm pr}\) imply \(1\sim3\). Transitivity therefore makes their comparisons with option 2 identical. Binary independence gives the same comparison for
\[
\begin{pmatrix}p&r\\q&s\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}p&t\\u&s\end{pmatrix}.
\]
Since \(r,q,t,u\) are arbitrary, off-diagonal entries are irrelevant. Completeness and transitivity on arbitrary diagonal triples establish \(\succeq^\ast\). The converse is immediate. ∎

No global real-valued utility representation of \(\succeq^\ast\) is assumed.

## 4.2 Affine classification and monotonicity

> **Corollary 4.1.** Adding \(F\) leaves exactly:
> \[
> \text{increasing diagonal},\qquad
> \text{decreasing diagonal},\qquad
> \text{universal indifference}.
> \]

Every unequal pair \(x>y\) can be positively affinely mapped to \((1,0)\), so all unequal pairs receive the same orientation. Equal values tie by neutrality.

> **Corollary 4.2.**
> \[
> \boxed{N+F+B_{\rm pr}+O+Q+\mathrm{Mon}}
> \]
> characterizes increasing-diagonal ranking.

\(Q\) eliminates universal indifference; Mon eliminates decreasing-diagonal ranking.

Because \(M_{ii}=V_D(i)\), this is exactly ex-ante policy-value ranking under your stipulated matrix semantics.

## 4.3 Exact domain requirements

For **full matrix domains up to a size ceiling**, three is the sharp threshold:

- With only one- and two-option matrices, the characterization fails.
- With every matrix of sizes \(1,2,3\), it holds; \(B_{\rm pr}\) propagates it to any additional sizes.

A binary counterrule is
\[
s_i=M_{ii}-M_{ij}.
\]
It satisfies \(N,F,O,Q,\mathrm{Mon}\), and binary independence is vacuous. On
\[
\begin{pmatrix}1&100\\0&0\end{pmatrix}
\]
it chooses option 2.

An explicit sufficient richness requirement is: all binary matrices, all clone extensions \(H\) displayed above, and their relabelings. For the affine conclusion, require the relevant affine comparisons as well. Merely having some three-option problems is insufficient.

The proof also works on all \([0,1]\)-valued matrices of sizes up to three, interpreting \(F\) internally: after eliminating off-diagonals, canonical binary representatives use only the two diagonal values.

Under the known axioms \(N,F,B_{\rm pr},O\), one unequal-diagonal binary benchmark identifies which of the three rules applies. A finite benchmark does not, however, certify that those axioms hold universally.

---

# 5. Replacing binary independence by contraction

The answer to S2 is negative under every menu semantics.

## 5.1 A natural family under principal or column contraction

Write \(d_i=M_{ii}\). For \(\lambda\ge0\), introduce an auxiliary elimination relation:
\[
i\to_\lambda j
\iff
d_i-d_j>\lambda|M_{ij}-M_{ji}|.
\]

Let \(W_\lambda(M)\) be the options with no incoming elimination edge. Define the final weak order by:

- tying all members of \(W_\lambda\) at the top;
- ranking rejected options by their diagonals.

> **Theorem 5.** Every finite \(\lambda\ge0\) yields a rule satisfying
> \[
> N,F,C_{\rm pr},C_{\rm col},O,Q,\mathrm{Mon}.
> \]
> At \(\lambda=0\), it is increasing-diagonal ranking. At every \(\lambda>0\), it sometimes recommends a nonmaximal diagonal.

**Proof.** Every edge strictly lowers the diagonal, so the elimination graph is acyclic and \(W_\lambda\ne\varnothing\). Pairwise elimination edges persist under either restriction, so a chosen survivor remains chosen.

Raising \(d_i\) can only remove incoming edges to \(i\) and add outgoing edges from \(i\). Its chosen status can improve, while others’ chosen status can only worsen. If it remains rejected, its rank among rejected options improves. This proves full Mon. Neutrality and affine invariance follow directly from the inequality. Equal off-diagonals and unequal diagonals establish \(Q\). ∎

Thus even an ordered, neutral, affine-invariant, monotone, contraction-consistent rule need not maximize ex-ante value.

### Finite benchmarks do not certify diagonal optimality

Given finitely many benchmarks, choose \(\lambda>0\) sufficiently small that every nonmaximal-diagonal option in every benchmark is eliminated by some maximal-diagonal option. Then the **entire ranking** agrees with diagonal ranking on all benchmarks.

A new binary matrix with a sufficiently large off-diagonal difference relative to its positive diagonal gap defeats \(D\).

This failure already occurs inside a one-parameter family.

## 5.2 The unrestricted family has maximum possible cardinality

Let \(\mathfrak c=|\mathbb R|\). There are
\[
\boxed{2^{\mathfrak c}}
\]
rules satisfying the S2 axioms under principal or column contraction.

For an explicit construction, choose arbitrary \(E\subseteq\mathbb R\). Put \(i\to j\) when
\[
d_i>d_j,\qquad s=M_{ji}-M_{ij}>0,
\]
and either
\[
d_i-d_j>s,
\]
or
\[
d_i-d_j=s
\quad\text{and}\quad
\frac{d_j-M_{ij}}s\in E.
\]
Use the same chosen-top, rejected-by-diagonal completion.

Edges descend diagonals, persist under restriction, and respond monotonically to diagonal increases. Positive affine transformations preserve the boundary parameter. Hence all the required axioms hold.

On
\[
M_r=
\begin{pmatrix}
r+1&0\\
1&r
\end{pmatrix},
\qquad
G_E(M_r)=
\begin{cases}
\{1\},&r\in E,\\
\{1,2\},&r\notin E.
\end{cases}
\]
Distinct \(E\)'s give distinct rules. This reaches the upper bound for rules on finite real matrices over a countable label universe.

Therefore the whole class cannot be parameterized by finitely many real numbers. The cardinality construction uses unrestricted boundary choices; the preceding \(\lambda\)-family establishes nonrigidity without that feature.

## 5.3 Even collapsing everything to fixed-reference scores does not restore rigidity

Suppose only the vector
\[
v_a=\sum_jw_jM_{ja}
\]
remains available, and restriction deletes coordinates.

A simple family chooses the top \(k\) scores, including boundary ties:
\[
G_k(v)=
\{a:\#\{b:v_b>v_a\}<k\},
\qquad k\ge2.
\]
Tie chosen options above the others and rank the others by \(v\). This satisfies neutrality, affine invariance, contraction, ordering, nontriviality, and monotonicity.

There are again \(2^{\mathfrak c}\) such rules on all finite score vectors. A complete construction is as follows.

For candidate \(j\), consider each triple of other options with gaps
\[
g=(v_i-v_j)_{i\in T}.
\]
Reject \(j\) if some triple has positive gap sum, or has zero sum, is nonzero, and its sorted normalized shape belongs to an arbitrary set \(E\). Choose all nonrejected options and complete the ranking as above.

A score maximizer cannot be rejected. Deletion removes rejection witnesses. Raising \(v_j\) decreases its witness sums, while it increases only the relevant witness sums for other candidates. Thus Mon holds, including at arbitrarily designated boundary shapes.

On
\[
v=(0,-1,t,1-t),\qquad0<t<\tfrac12,
\]
the zero-valued option is rejected exactly according to membership of the shape \((-1,t,1-t)\) in \(E\). These shapes are distinct. Four-option vectors therefore already support the full cardinality.

With fixed \(w\), raising \(M_{jj}\) raises only \(v_j\), so the matrix version of Mon follows.

---

# 6. An exact necessary-and-sufficient domain condition for T2

Symmetric embeddings give a convenient sufficient condition. A more general criterion is exact.

Assume the matrix domain \(\mathcal D\) is closed under relabeling. On a restricted domain, invariances apply whenever both transformed matrices belong to the domain.

Form a directed graph of **pointed matrices**
\[
\mathcal P_{\mathcal D}=\{(M,i):M\in\mathcal D,\ i\in I_M\}.
\]

Add:

1. bidirectional edges for admissible relabelings;
2. bidirectional edges for admissible row translations;
3. extension edges
   \[
   (M|_K,i)\longrightarrow(M,i),\qquad i\in K.
   \]

Let \(\operatorname{Reach}(x)\) be forward reachability. Let
\[
F_M=\{(M,i):i\in I_M\}
\]
be the action fiber of \(M\).

> **Theorem 6 — exact domain criterion.**
> \[
> N+R+C_{\rm pr}+Q
> \]
> is inconsistent exactly when
> \[
> \boxed{
> \forall x\in\mathcal P_{\mathcal D}\quad
> \exists M\in\mathcal D:
> F_M\subseteq\operatorname{Reach}(x).
> }
> \tag{DR}
> \]

**Proof.** Rejection propagates along invariance edges. It propagates from a restriction to an extension by the contrapositive of contraction. Under (DR), any rejection would therefore reject an entire fiber, violating nonempty choice.

Conversely, if (DR) fails at \(x\), define
\[
G_x(M)=\{i:(M,i)\notin\operatorname{Reach}(x)\}.
\]
Every choice set is nonempty. The invariance edges establish \(N,R\), and extension edges establish contraction. The distinguished action in \(x\) is rejected. Relabeling a nonempty proper choice set gives different choices on the same label set, establishing \(Q\). Tying chosen options above rejected ones supplies \(O\) too. ∎

This is a condition on admissible matrices and operations, with no quantification over unknown decision rules.

The circulant condition is sufficient for (DR), but not necessary. If \(F\) is also required, add admissible affine transformations as bidirectional edges.

---

# 7. Physical and numerical domain restrictions

## 7.1 Bounded payoffs: the answer changes depending on \(F\)

On the domain \(M\in[0,1]^{n\times n}\), interpreted internally, **\(N+R+C_{\rm pr}+Q\) is consistent**.

Fix \(r\in[1/2,1)\), and put
\[
i\to j
\iff
M_{ii}-M_{ij}>r
\quad\text{and}\quad
M_{ji}-M_{jj}>r.
\]
Choose options with no incoming edge, tie them at the top, and tie rejected options below them.

An edge implies
\[
M_{ii}>r,\qquad M_{jj}<1-r,
\]
so edges cannot cycle. The conditions use only within-row differences, proving \(R\); they persist under restriction, proving contraction. The rule is neutral and responsive. Raising a diagonal removes incoming edges and adds outgoing edges, proving Mon. It also satisfies \(O\).

It fails \(F\).

**Adding \(F\) restores triviality.** Compress and row-normalize to
\[
A_{ij}=\frac12+\alpha(M_{ij}-M_{ii})
\]
with sufficiently small \(\alpha>0\). Embed this bounded common-diagonal matrix in a bounded circulant, filling unused entries with \(1/2\). The principal proof then applies.

Thus bounded payoffs preserve T2 **with \(F\) added**, but not under the original four axioms alone.

## 7.2 Predictors bounded away from perfect accuracy

An accuracy bound alone does not destroy richness.

Consider
\[
P_n=(1-\eta)I+\eta\frac{\mathbf1\mathbf1^\top}{n},
\qquad0<\eta<1.
\]
The correct-label probability is
\[
1-\eta+\frac{\eta}{n}\le1-\frac{\eta}{2},
\qquad n\ge2.
\]
Nevertheless \(P_n\) is invertible. Given any desired causal matrix \(M\), choose the state/action payoff table
\[
U=P_n^{-1}M.
\]
Then \(P_nU=M\). With unrestricted real payoffs, the entire matrix domain remains realizable despite uniformly imperfect prediction.

If latent payoffs must also lie in \([0,1]\), full realizability disappears. But with \(F\), the required compressed matrices remain realizable. Indeed,
\[
P_n^{-1}
=
\frac1{1-\eta}I-
\frac{\eta}{(1-\eta)n}\mathbf1\mathbf1^\top.
\]
A sufficiently small neighborhood of the constant \(1/2\) matrix maps back into \([0,1]\), uniformly in \(n\). The bounded circulant argument survives.

Completely uninformative prediction is different: when all induced laws coincide, the channel loses rank. An accuracy bound does not itself guarantee an informative channel.

## 7.3 At most \(k\) actions per information set

For \(k\ge2\), with unboundedly many information sets, the requisite symmetric extensions still exist—even with perfect recall.

Use a complete binary decision tree of depth \(m\), with prediction outcomes hidden. There are \(N=2^m\) realized action paths. Every path is induced by the same number
\[
L=2^{2^m-1-m}
\]
of complete deterministic policies, because prescriptions off that path are free.

Predict the eventual path and let payoff depend on predicted and actual paths. Any desired path matrix \(C\) is realizable. The full policy matrix is
\[
C\otimes J_L.
\]

If \(C\) is circulant, this full matrix has a transitive automorphism group: rotate path blocks and permute duplicate policies within blocks. Any target matrix can be embedded in a sufficiently large power-of-two circulant and recovered by selecting one policy representative from each designated block.

Thus the symmetric-extension argument survives the per-information-set action bound. It requires the stipulated principal restrictions between admissible matrices; restricting contraction to literal local tree pruning is a different axiom.

## 7.4 At most one information set

With an unbounded action set, one information set already realizes every square matrix.

Combining one information set with a finite action bound creates a genuine size ceiling.

For the full domain of sizes at most \(k\ge2\), define:

- universal indifference below size \(k\);
- at size \(k\), rank by
  \[
  M_{ii}-\frac1k\sum_jM_{ij}.
  \]

This satisfies \(N,F,R,C_{\rm pr},O,Q,\mathrm{Mon}\). Every proper restriction lands in the universally indifferent part of the domain.

Therefore no finite size ceiling forces global triviality under existential \(Q\). If nontriviality is specifically required on binary menus, three-option symmetric extensions already suffice to block it.

---

# 8. What row invariance does—and does not—mean

## 8.1 Exact factorization theorem

> **Theorem 7.**
> \[
> R
> \iff
> \text{the rule factors through }
> Z_{ij}=M_{ij}-M_{ii}.
> \]

**Proof.** Row additions leave \(Z\) unchanged. Conversely, if \(Z(M)=Z(M')\), then
\[
M'_{ij}-M_{ij}=M'_{ii}-M_{ii}
\]
is constant within each row. Thus \(M'\) is a row translation of \(M\). ∎

On a restricted domain, this is factorization through the image of \(Z\); the zero-diagonal representative need not itself be admissible. Additional inputs such as \(w\) remain additional arguments.

## 8.2 Classification

| Criterion or rule | Explicit matrix semantics | \(R\)? |
|---|---|---|
| Fixed-reference CDT | Rank by \(w^\top M\), with \(w\) fixed | Yes |
| Pure global ratifiability | Admit \(i\) iff \(M_{ii}\ge M_{ij}\) for every \(j\) | Yes, as an admissibility criterion |
| Affine mixed ratifiability | \(p\in\operatorname{BR}(p^\top M)\) | Yes, as an equilibrium set |
| Deliberational CDT | Requires initial beliefs, update dynamics, and final selection | Depends on that extra specification |
| EDT under a reference-policy joint law | Maximize \(M_{ii}\) where \(P(i,s)=\rho_i\mu_i(s)\) | No |
| Ex-ante policy maximization | Maximize \(M_{ii}=V(i)\) | No |
| “FDT-style” ex-ante maximization | The preceding rule under stipulated functional-counterfactual semantics | No under that stipulation |

Ratifiability’s invariance does not establish nonemptiness or supply a complete ranking.

For deliberation, fixed-belief causal comparisons and difference-based update dynamics preserve row baselines. Arbitrary update dynamics need not. Joyce discusses multiple admissible update schemes and distinguishes equilibrium credences from the subsequent act or mixture chosen; Arntzenius explicitly identifies update rules as additional structure needed to define equilibrium. These are not fully specified matrix selectors merely by virtue of their names. [websites.umich.edu](https://websites.umich.edu/~jjoyce/papers/rscdt.pdf?utm_source=chatgpt.com)

### \(R\) does not characterize causal rationality

Rank by negative own-row regret:
\[
r_i=M_{ii}-\max_jM_{ij}.
\]
This satisfies \(N,F,R,O\). But on
\[
M=
\begin{pmatrix}
0&10&-1\\
10&0&-1\\
0&0&-1
\end{pmatrix}
\]
its scores are \((-10,-10,-1)\), so it chooses option 3, which both other columns strictly dominate.

Thus “\(R=\) causal evaluation” is **false as a characterization**. The exact meaning is invariance to row-specific baselines. It captures a feature of several causal evaluation procedures, but supplies neither causal expected-utility maximization nor dominance by itself.

---

# 9. Literature verification and novelty

## 9.1 Requested sources

| Source | Verified result and location | Relation to this problem |
|---|---|---|
| **Rachael Briggs, “Decision-Theoretic Paradoxes as Voting Paradoxes,” *Philosophical Review* 119(1):1–30, 2010. DOI 10.1215/00318108-2009-024.** | §6 begins p. 21; \(P,S\) are formalized p. 22; incompatibility is proved pp. 23–24. \(S\) preserves the two candidates’ entire evaluation rows on the same action set. | Establishes the \(P+S\) obstruction. Her §5, pp. 19–20, also distinguishes diagonal EDT from weighted causal evaluation and notes the need for weights beyond the matrix rows. [Download on Academia](https://www.academia.edu/2307714/Decision_Theoretic_Paradoxes_as_Voting_Paradoxes?utm_source=chatgpt.com) |
| **John Frederick Fink and Sergio Ruiz, “Every graph is an induced isopart of a circulant,” *Czechoslovak Mathematical Journal* 36(2):172–176, 1986. DOI 10.21136/CMJ.1986.102080.** | §2, p. 174: Lemma 2 uses powers-of-two labels; Theorem 1 gives rotational decomposition into copies of a nonempty graph; Corollary 1 makes those copies induced. §3, p. 175, gives a directed extension. Full paper verified. | Supplies the embedding precedent; it does not state the real-matrix choice theorem. [dml.cz](https://dml.cz/bitstream/handle/10338.dmlcz/102080/CzechMathJ_36-1986-2_2.pdf?utm_source=chatgpt.com) |
| **Arkarup Basu Mallik and Mihir Bhattacharya, “Consistency and social choice: Possibilities and impossibilities,” *Mathematical Social Sciences*, 2026, article 102582. DOI 10.1016/j.mathsocsci.2026.102582.** | Existence and publisher summary verified. The summary reports impossibilities involving contraction consistency, Pareto efficiency, and anonymity/nondictatorship. **Full published theorem statements and proofs could not be verified**; the public working-paper URL also returned an access error. | Its preference-aggregation framework must not be silently identified with these cardinal rectangular matrices. No exact theorem translation is claimed here. [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0165489626000892?utm_source=chatgpt.com) |
| **Joseph Y. Halpern, “A Note on Existence of Ratifiable Acts,” *Review of Symbolic Logic* 13(3):503–508, 2020. DOI 10.1017/S175502031800028X.** | Author PDF: Definition 2.1 p. 2; assumptions (3),(4) p. 3; Theorem 2.2 p. 4. Costless statewise mixtures and affine conditional state laws imply existence of a mixed ratifiable act. | Not an unconditional claim that allowing randomization restores existence. No menu-invariance characterization. [cs.cornell.edu](https://www.cs.cornell.edu/info/people/halpern/papers/newcomb.pdf?utm_source=chatgpt.com) |
| **James Bell, Linda Linsefors, Caspar Oesterheld, Joar Skalse, “Reinforcement Learning in Newcomblike Environments,” NeurIPS 2021.** | §2.1, p. 5, Definition 1 and Theorem 3: every continuous NDP has a strongly ratifiable policy in their policy-dependent transition/reward framework. | A mixed-policy existence theorem, separate from optimality and convergence. The PDF title says **Environments**; some retrieval metadata incorrectly says “Problems.” [proceedings.neurips.cc](https://proceedings.neurips.cc/paper/2021/file/b9ed18a301c9f3d183938c451fa183df-Paper.pdf?utm_source=chatgpt.com) |

## 9.2 Closest work on the menu issue

**J. Dmitri Gallow, “Comparativism About Instrumental Value,” *Philosophy and Phenomenological Research* 113(2):346–363, 2026, DOI 10.1111/phpr.70139**, is particularly relevant. In the author version, §4, pp. 28–29, he studies downward and upward preservation. Footnote 38 explicitly defines a binary subdecision by removing other options **and conditioning credences on their surviving disjunction**. That directly recognizes the semantic choice at issue here. His principles are not simply Sen’s choice-set contraction. [jdmitrigallow.com](https://jdmitrigallow.com/papers/pdfs/caiv.pdf?utm_source=chatgpt.com)

Other checked sources clarify the surrounding issues:

- **James M. Joyce, “Regret and Instability in Causal Decision Theory,” *Synthese* 187:123–145, 2012**, §2, author pp. 9–11: deliberation, updating, and final selection require separate treatment. [websites.umich.edu](https://websites.umich.edu/~jjoyce/papers/rscdt.pdf?utm_source=chatgpt.com)
- **Frank Arntzenius, “No Regrets, or: Edith Piaf Revamps Decision Theory,” *Erkenntnis* 68:277–297, 2008**, especially publisher notes 18 and 20: continuity and update-rule structure matter for equilibrium claims. [Springer Nature Link](https://link.springer.com/article/10.1007/s10670-007-9084-8?utm_source=chatgpt.com)
- **Andy Egan, “Some Counterexamples to Causal Decision Theory,” *Philosophical Review* 116(1):93–114, 2007**: counterexamples and ratifiability discussion, rather than the present matrix characterization. [tomwilk.net](https://tomwilk.net/wp-content/uploads/2019/01/Egan2007.pdf?utm_source=chatgpt.com)
- **Ralph Wedgwood, “Gandalf’s Solution to the Newcomb Problem,” *Synthese* 190:2643–2675, 2013**: benchmark dependence is relevant; no exact T2/T3 theorem is attributed to it here. [Springer Nature Link](https://link.springer.com/article/10.1007/s11229-011-9900-1?utm_source=chatgpt.com)
- **Jack Spencer and Ian Wells, “Why Take Both Boxes?”, *Philosophy and Phenomenological Research* 99:27–48, 2019**, §4 and author-version footnote 23: converting a simultaneous problem into a sequential one can create a different decision problem. [jackspencer.org](https://www.jackspencer.org/uploads/1/4/0/3/14038590/why_take_both_boxes_final.pdf?utm_source=chatgpt.com)
- **Arif Ahmed, “Push the Button,” *Philosophy of Science* 79(3):386–395, 2012**: the verified abstract links rejection of a CDT verdict to a transitivity problem; this is not the present principal-menu theorem. [Cambridge Core](https://www.cambridge.org/core/journals/philosophy-of-science/article/abs/push-the-button/8F2E5D84D6AF6AE914592A52A8A96D65?utm_source=chatgpt.com)

## 9.3 Tournament and social-choice precedents

**Felix Brandt, *Tournament Solutions: Extensions of Maximality and Their Applications to Decision-Making*, habilitation thesis, 2009**, §2.4, p. 11, explicitly observes that neutral nonempty tournament solutions select every vertex of a vertex-transitive tournament. §8.1.1, pp. 49–50, discusses contraction impossibilities. [pub.dss.in.tum.de](https://pub.dss.in.tum.de/brandt-research/habil.pdf?utm_source=chatgpt.com)

The related **Brandt–Brill–Harrenstein, “Tournament Solutions,” *Handbook of Computational Social Choice*, 2016, chapter 3, §3.2.2**, treats nonempty isomorphism-invariant selectors and set-stability conditions. Its \(\widehat\alpha\) conditions must not be substituted for Sen’s \(\alpha\). [pub.dss.in.tum.de](https://pub.dss.in.tum.de/brandt-research/tsolutions.pdf?utm_source=chatgpt.com)

There is a direct tournament specialization of the embedding argument: embed any finite tournament in an odd-order circulant tournament, using distinct differences and completing each unused difference pair with opposite orientations. Neutrality chooses every vertex of the extension; Sen contraction chooses every vertex of the original tournament.

I did **not** locate an explicit published statement of this full choose-all conclusion, or of the exact matrix theorem \(N+R+C_{\rm pr}\Rightarrow G(M)=I\). Its symmetry and embedding ingredients are established. This search does not justify claiming originality.

---

# 10. The corrected thesis

The strongest defensible statement is:

> **On the unrestricted causal-matrix domain, principal binary independence, neutrality, ordering, common affine invariance, nontriviality, and diagonal monotonicity characterize ex-ante diagonal ranking. Separately, principal contraction and neutrality are incompatible with nontrivial row-baseline-invariant choice whenever the domain satisfies (DR). Neither result extends unchanged to menu restriction that retains a fixed belief model.**

This resolves the mathematical question under the stated semantics:

- **M1–M4:** principal restriction is canonical conditional on law preservation; rectangular and fixed-reference restrictions require additional data; the dichotomy fails across those semantics; complete column maps are given above.
- **S1–S3:** increasing diagonal is characterized under principal binary independence; contraction admits maximally many alternatives; three-option clone richness is the sharp full-domain threshold for T3.
- **Q1–Q2:** (DR) is necessary and sufficient; bounded payoffs, affine invariance, imperfect prediction, and action-count restrictions have the distinct effects proved above.
- **I1–I2:** \(R\) exactly means factorization through within-row differences, and does not characterize causal rationality.
- **L1–L2:** T3’s core is prior work by Podgorski; Briggs supplies \(P+S\); T2’s exact published status remains unestablished, and the full Basu Mallik–Bhattacharya text remains unverified.

The key correction is that **preserving choices when options disappear and preserving comparisons when their associated belief perspectives disappear are different requirements**. The impossibilities concern the latter operation in essential ways.