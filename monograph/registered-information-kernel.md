# Registered Information over Contrast Domains

> **Integrated edition, 2026-10-01.** Statements, proofs, and scope conditions in this manuscript are authoritative. Results are finite unless explicitly stated otherwise. Appendix D contains the supplementary theorems; the external review documents record the revision history.

## Part I: The Deterministic Kernel

---

## 0. Purpose and scope

These notes develop, constructively and progressively, a theory of how raw presentations of things become information about those things, relative to questions. The long-term aim is a framework rich enough to (i) supply the layer that classical information theory and information algebra both presuppose — the passage from raw material to constituted information pieces — and (ii) support practical analyses such as dataset sufficiency auditing, missing-information analysis, model interpretability, and principled criteria for when a system overclaims relative to its inputs.

This first part builds only the **deterministic kernel**: the smallest closed mathematical system in which the theory's central object — the quotient of a contrast domain induced by a family of views — can be defined, and in which its basic structural theorems can be stated and proved exactly. Everything that makes the intended theory distinctive but difficult (anchoring, admissible registration, noise, sheaf-theoretic gluing) is deliberately excluded from the kernel, but each exclusion is recorded as a named standing assumption with an explicit attachment point for later relaxation (§8). The discipline throughout is: the kernel must be provable and closed before any extension is attempted, so that extensions become controlled relaxations of named assumptions rather than renegotiations of the framework.

Prerequisites are elementary set theory and basic order theory. All order-theoretic and information-theoretic notions actually used are defined in §3, with references to standard sources.

---

## 1. The problem: information before the algebra of information

Most formal theories of information begin after information has already been constituted.

Shannon's theory begins with a set of possible messages and a probability distribution over them; it studies the selection, coding, and transmission of signals, and explicitly brackets meaning: "semantic aspects of communication are irrelevant to the engineering problem" [Shannon 1948]. Semantic theories of information begin with propositions, truth-conditions, or content-bearing states [Bar-Hillel & Carnap 1952; Dretske 1981; Floridi 2004]. Information algebra — the most developed algebraic account of information as such — begins with a set $\Phi$ of *information pieces* equipped with operations of combination and extraction [Kohlas 2003].

Each of these frameworks is powerful within its remit. But all of them presuppose a prior step that is central to real epistemic practice and largely unformalized:

> **How does a raw presentation — a sentence, a measurement, an image, a sensor trace, a model activation — become information *about* a target, *for* a question?**

A sensor reading is information only under a calibration protocol. A photograph is information only once it is taken to be *of* something. A dataset is task-relevant information only relative to a space of alternatives it is supposed to discriminate among, and a family of questions it is supposed to answer. A hidden-layer activation of a neural network may *encode* something, but whether that something is registered, extractable, or actually usable to answer a given question is a further matter.

The theory developed here models this prior step explicitly. Its two governing theses are:

1. **Information is produced, not merely present.** A raw presentation becomes information through two operations: *anchoring* (assignment of aboutness — determining which target the presentation presents) and *registration* (conversion of the anchored presentation into an explicit information piece within an algebra of such pieces).

2. **Information content is relative to a contrast domain.** What a body of data "contains" is not an absolute quantity but a structure of *distinctions*: given a domain $D$ of relevant alternatives, the data contains exactly the distinctions over $D$ that survive registration. Formally, the content of a view-family is a quotient of $D$, and a question is answerable exactly when it factors through that quotient.

The second thesis is the mathematical backbone of the kernel developed below. The first thesis is, in the kernel, deliberately suppressed by standing assumption (views arrive pre-anchored, and registration is canonical), because its formalization requires the surrounding structure the kernel provides; §8 records the attachment points.

---

## 2. Position among existing theories

The kernel is not built in a vacuum. This section states, briefly and with sources, what each neighboring tradition contributes and what it leaves open. The reader interested only in the mathematics may skip to §3.

**Shannon information.** [Shannon 1948; Cover & Thomas 2006] gives the quantitative theory of uncertainty reduction, coding, and channel capacity. It abstracts from aboutness and question-relativity by design. Less well known and directly relevant here: Shannon himself later proposed a non-quantitative, order-theoretic picture in which an information *element* is an equivalence relation (a partition) on a space of possibilities, and information elements form a lattice under refinement [Shannon 1953]. The kernel below can be read as a systematic development of that picture, with the partition generated by *views of a target* rather than posited directly.

**Semantic information.** [Bar-Hillel & Carnap 1952] quantify semantic content via logical possibility; [Dretske 1981] ties information to reliable correlation and knowledge; [Floridi 2004] adds truth-oriented constraints ("strongly semantic" information). These theories restore meaning and aboutness but generally take contentful items (propositions) as their starting units; they do not model the conversion of heterogeneous raw presentations into such units.

**Situation theory and information flow.** [Barwise & Perry 1983; Barwise & Seligman 1997] model information as partial, situated, and flowing across systems via classifications and channels. They motivate partiality and situatedness — commitments shared here — but with a different formal base and without an algebraic registration layer.

**Erotetic semantics: questions as partitions.** In the partition semantics of questions [Groenendijk & Stokhof 1984; Hamblin 1958], a question over a logical space *is* a partition of that space, and an answer is information locating the actual world within a cell. The kernel adopts this identification (§4, P6): questions and data are placed in the *same* lattice of partitions, which is what makes "answerability" a lattice inequality rather than an unformalized relation. The interrogative tradition in epistemology treats inquiry as the strategic posing of questions [Hintikka 2007; Wiśniewski 1995]; the kernel supplies the statics such a dynamics presupposes — which questions the available data can answer at all.

**Contrastivism.** In contrastivist epistemology, knowledge and explanation are irreducibly contrastive: one knows that $p$ *rather than* $q$, relative to a class of alternatives [Schaffer 2005], and why-questions are answered only against contrast classes [van Fraassen 1980]; Bateson's dictum that information is "a difference that makes a difference" [Bateson 1972] is the same commitment in embryo. The contrast domain $D$ (Definition 4.1) is a formalization of this position: content is defined only against a space of alternatives, and "the information in the data" *simpliciter* is deliberately assigned no meaning (§4.2). Conversely, the kernel offers contrastivism a formal apparatus it has lacked: contrasts are partitions, and contrastive knowledge from data is answerability (Definition 5.4).

**Measurement theory.** The representational theory of measurement [Krantz, Luce, Suppes & Tversky 1971] formalizes the assignment of representatives in a formal structure to empirical objects, and its *meaningfulness* tradition [Narens 2002] identifies legitimate content with invariance under the admissible transformations of the representation. Registration (P5) is measurement in exactly this sense — the conversion of presentations into pieces of a formal algebra — and the admissibility layer of Part II, in particular its invariance ceilings (§16.1), recovers the meaningfulness criterion inside the present framework: admissible content is invariant content. The connection grounds admissibility classes in a century of worked examples of admissible-transformation structures.

**Theories of reference.** Anchoring — the assignment of aboutness — is the formal home of the problem of reference: causal-historical theories [Kripke 1980; Putnam 1975] and teleosemantics [Millikan 1984] propose mechanisms by which a token comes to be *of* its object, with reference failure and ambiguity as their standing test cases. The kernel suppresses anchoring by assumption (A4); the interface of Part III (§19) and the substantive theory of Part IV type exactly the objects — correspondences, selection policies, mis-anchoring, leakage — that this literature describes informally, and the status taxonomy of Definition 19.4 (unambiguous, ambiguous, failed) formalizes the failure modes it catalogues.

**Statistical sufficiency and comparison of experiments.** A statistic is *sufficient* when it retains everything the sample says about the parameter; the factorization theorem [Halmos & Savage 1949] and Blackwell's ordering of experiments [Blackwell 1951, 1953] constitute the probabilistic theory of "which reductions of data lose nothing relative to a family of inference questions." The kernel is, in its exact and deterministic setting, the possibilistic skeleton of this theory; the probabilistic refinement is a named deferred extension (§8, H3).

**Epistemic partitions.** In epistemic logic and the economics of information, an agent's information is standardly modeled as a partition of a state space, with knowledge as constancy on cells [Aumann 1976]. The kernel derives such partitions from an explicit substrate of views and registrations instead of positing them.

**Observability.** Control theory asks when hidden state can be recovered from outputs [Kalman 1963; Hermann & Krener 1977]. This is the special case of the kernel in which the target is a dynamical state and the question-family is state recovery.

**Multi-view learning and Formal Concept Analysis.** Multi-view learning studies inference from multiple feature views [Xu, Tao & Xu 2013; Zhao et al. 2017]; FCA derives concept lattices from object–attribute incidence [Wille 1982; Ganter & Wille 1999]. Both support the guiding intuition that no single view exhausts a target, but neither provides a general account of what makes a view *information about* a target, nor a bridge into an information algebra.

**Rough set theory.** Pawlak's rough sets [Pawlak 1982; Pawlak 1991] are the closest existing formalism to the kernel's central construction — closer than FCA. In an information system (a single object–attribute table), each attribute subset $B$ induces the indiscernibility relation $\mathrm{IND}(B)$, and lower and upper approximations of subsets are taken relative to the resulting partition; that partition is *exactly* the induced quotient $\sigma(S)$ of §5 for the attribute-projection views corresponding to $B$. The kernel should accordingly be read not as overlooking rough sets but as lifting them: where rough set theory takes the table as primitive and derives indiscernibility from attribute subsets, the kernel takes arbitrary generating maps (views) as primitive, equips them with a refinement preorder (P3), and derives the same quotient; rough sets reappear as the degenerate case in which every view is a column projection of one fixed table. What the lift adds is exactly what the later layers use: views not presentable as attributes of a single table, questions and answerability as factorization, the registration interface into an information algebra, and the admissibility and graded extensions. Pawlak's approximation operators also transfer verbatim: for any $E \subseteq D$, the union of the $\sigma(S)$-blocks contained in $E$ and the union of those meeting $E$ are, respectively, the largest answerable inner bound and the smallest answerable outer bound on the (generally unanswerable) membership question of $E$; Proposition 6.11 organizes these operators into the information algebra the kernel generates.

**Information algebra.** [Kohlas 2003; Kohlas 2017; Shenoy & Shafer 1990] axiomatize information pieces $\phi \in \Phi$ with combination $\phi_1 \cdot \phi_2$, extraction (focusing) onto questions, and an information order $\phi \le \psi$. This is the closest formal neighbor and the intended downstream algebra. It begins, however, at $\phi \in \Phi$: the pieces exist. The present theory targets the interface *before* that point. In the kernel, the algebra is instantiated in its simplest canonical form (the subset algebra, §3.4), which is sufficient for all kernel results; the general algebra re-enters as a deferred extension (§8, H5).

**Sheaf-theoretic accounts of local data.** Sheaf theory formalizes local data on overlapping contexts and the conditions under which local data glue to a global description; failures of gluing have been used to characterize contextuality [Abramsky & Brandenburger 2011] and to fuse heterogeneous sensor data [Robinson 2017]. The kernel's view-refinement preorder (§4, P3) is designed to serve as the future base site for such semantics, and the kernel's coherence law (Proposition 6.3) is the exact-case shadow of the gluing axiom. This is a named deferred extension (§8, H4), executed in Part V.

**The gap targeted.** None of the above provides a general, formal account of the passage
$$
\text{raw presentation} \to \text{anchored presentation} \to \text{registered information piece},
$$
relative to a contrast domain and a question-family. The kernel below builds the exact deterministic core on which that account will be erected.

---

## 3. Mathematical preliminaries

All material in this section is standard; sources are given for each notion. Throughout, "map" means total function.

### 3.1 Partitions and kernels of maps

Let $D$ be a set. A **partition** $\pi$ of $D$ is a set of nonempty, pairwise disjoint subsets of $D$ (its **blocks** or **cells**) whose union is $D$. Partitions of $D$ correspond bijectively to equivalence relations on $D$ and to surjections out of $D$ up to isomorphism of codomain; we pass freely among the three descriptions. $\mathrm{Part}(D)$ denotes the set of all partitions of $D$. For $Z \in D$, $[Z]_\pi$ denotes the block of $\pi$ containing $Z$. The **quotient map** of $\pi$ is $\pi^\natural : D \to D/\pi$, $Z \mapsto [Z]_\pi$, where $D/\pi$ is the set of blocks.

For any map $f : D \to Y$, the **kernel** of $f$ is the partition
$$
\ker(f) \;=\; \{\, f^{-1}(y) \;:\; y \in f(D) \,\} \in \mathrm{Part}(D),
$$
i.e., the partition induced by the equivalence $Z \sim Z' \iff f(Z) = f(Z')$.

> **Fact 3.1 (image factorization).** Every map $f : D \to Y$ factors as $f = m \circ e$ with $e : D \twoheadrightarrow D/\ker(f)$ the quotient surjection and $m : D/\ker(f) \rightarrowtail Y$ injective; the factorization is unique up to unique isomorphism. (See, e.g., [Davey & Priestley 2002].)

> **Fact 3.2 (factorization criterion).** For maps $f : D \to Y$ and $g : D \to A$: there exists $h : f(D) \to A$ with $g = h \circ f$ if and only if $\ker(f)$ refines $\ker(g)$, i.e., $f(Z) = f(Z') \Rightarrow g(Z) = g(Z')$; and $h$ is then unique on $f(D)$.

### 3.2 The partition lattice

Order $\mathrm{Part}(D)$ by **refinement**: for $\pi, \rho \in \mathrm{Part}(D)$,
$$
\rho \le \pi \quad :\iff \quad \pi \text{ refines } \rho \quad (\text{every block of } \pi \text{ is contained in a block of } \rho).
$$

**Orientation convention.** Under this convention, *finer is greater*: the top element is the discrete partition $\top = \{\{Z\} : Z \in D\}$ (every element distinguished; maximal information) and the bottom element is the indiscrete partition $\bot = \{D\}$ (nothing distinguished; null information). The convention is chosen so that the order agrees with the *information order*: more distinctions $=$ more information. (Some sources orient the partition lattice the opposite way; nothing depends on the choice beyond bookkeeping.)

> **Fact 3.3.** $(\mathrm{Part}(D), \le)$ is a complete lattice [Ore 1942; Birkhoff 1967]. The join $\bigvee_i \pi_i$ is the **common refinement**: its blocks are the nonempty intersections $\bigcap_i B_i$ with $B_i$ a block of $\pi_i$. Equivalently, $Z, Z'$ lie in the same block of $\bigvee_i \pi_i$ iff they lie in the same block of every $\pi_i$. The meet is the finest partition simultaneously coarsened by all $\pi_i$ (transitive closure of the union of the equivalences). In particular, for a family of maps $f_i : D \to Y_i$ with pairing $\langle f_i \rangle : D \to \prod_i Y_i$,
> $$
> \ker \langle f_i \rangle_{i \in I} \;=\; \bigvee_{i \in I} \ker(f_i).
> \tag{3.1}
> $$

Shannon's information lattice [Shannon 1953] is precisely a lattice of equivalence relations under this kind of order, with join as the combination of information.

### 3.3 Galois connections

Let $(P, \le)$ and $(Q, \le)$ be posets. A (monotone) **Galois connection** or adjunction $\sigma \dashv \tau$ between $P$ and $Q$ is a pair of maps $\sigma : P \to Q$, $\tau : Q \to P$ such that
$$
\sigma(p) \le q \quad \iff \quad p \le \tau(q) \qquad \text{for all } p \in P,\; q \in Q.
$$

> **Fact 3.4 (properties of Galois connections).** [Davey & Priestley 2002, ch. 7; Erné et al. 1993] If $\sigma \dashv \tau$, then: (i) both maps are monotone; (ii) $\sigma$ preserves all existing joins and $\tau$ all existing meets; (iii) $\tau \sigma$ is a closure operator on $P$ (inflationary, monotone, idempotent) and $\sigma \tau$ is an interior operator on $Q$ (deflationary, monotone, idempotent; the alternative name "kernel operator" is avoided throughout to keep "kernel" unambiguous); (iv) $\sigma \tau \sigma = \sigma$ and $\tau \sigma \tau = \tau$; (v) the fixed points of $\tau\sigma$ and of $\sigma\tau$ form complete lattices when $P, Q$ are complete, and $\sigma, \tau$ restrict to mutually inverse isomorphisms between them.

### 3.4 The subset information algebra

The simplest nontrivial instance of an information algebra in the sense of [Kohlas 2003] is the **subset algebra** (there also called the algebra of constraints, and the single-domain case of the relational algebra example): information about an unknown element of a set $D$ is represented by the set of possibilities not yet excluded.

> **Definition 3.5.** The **subset algebra over $D$** is $\Phi_D = \mathcal{P}(D)$ with:
>
> - **combination** $\phi \cdot \psi := \phi \cap \psi$ (pooling two pieces of information excludes what either excludes);
> - **information order** $\phi \le \psi :\iff \psi \subseteq \phi$ ($\psi$ is at least as informative: it excludes more);
> - **null information** $1 = D$ (nothing excluded); **contradiction** $0 = \varnothing$.

Combination is associative, commutative, and idempotent, with $1$ neutral; $\phi \le \psi \iff \phi \cdot \psi = \psi$. This is a (domain-free, idempotent) information algebra. Taken by itself it has no nontrivial extraction (focusing) structure; Proposition 6.11 shows that a view family induces a labeled version of it with nontrivial focusing, and the multi-domain version is hook H5 (§8). A piece $\phi \in \Phi_D$ is **true of** $Z \in D$ iff $Z \in \phi$.

---

## 4. The kernel: standing assumptions and primitives

### 4.1 Standing assumptions

The kernel operates under five standing assumptions. They are not claims about the intended final theory; they are simplifications adopted so that the core can be built exactly. All but (A1) are relaxed later in the monograph; §8 explains what a relaxation is and lists every assumption the monograph introduces, including those added in later parts.

- **(A1) Totality.** Every view is defined on the whole contrast domain. *(In force throughout; never relaxed.)*
- **(A2) Determinism.** Views are functions: a target yields exactly one presentation per view; there is no noise. *(Relaxed in Part III.)*
- **(A3) Canonical registration.** Registration is the canonical one (Definition 4.6); the general theory of admissible registration classes is deferred. *(Relaxed in Part II.)*
- **(A4) Anchoring suppressed.** Each view arrives *pre-anchored*: it is given as a function on $D$, so the assignment of aboutness has already succeeded. The theory of anchoring — including ambiguity and failure — is deferred. *(Interface in Part III, §19; relaxed in Part IV.)*
- **(A5) Single fixed domain.** One contrast domain $D$ is fixed throughout; the interaction of multiple domains (and, with it, nontrivial extraction) is deferred. *(Relaxed in Part XI.)*

### 4.2 Primitives

**P1. Contrast domain.**

> **Definition 4.1.** A **contrast domain** is a nonempty set $D$. Its elements $Z \in D$ are called **candidates**.

$D$ is the space of alternatives relative to which information is assessed: possible states of the world, possible identities of a target, possible diagnoses, possible database states, possible meanings. The relativity is essential and deliberate: the kernel assigns no meaning to "the information in the data" *simpliciter*, only to "the information in the data over $D$." The ambient class of all targets, from which contrast domains are carved, is not needed in the kernel and enters only with the multi-domain extension (§8, H5).

**P2. Views.**

> **Definition 4.2.** A **view** on $D$ is a pair $(Y_v, v)$ where $Y_v$ is a set (the **presentation space**) and $v : D \to Y_v$ is a map. For $Z \in D$, the value $v(Z) \in Y_v$ is the **presentation** of $Z$ through $v$. A **view family** is a set $V$ of views on $D$; subsets $S \subseteq V$ are the **available views** in a given epistemic situation.

Views are the modes of partial access: a measurement procedure, a document field, a sensor, an annotation protocol, a probe applied to a model layer. By (A1)–(A2) they are total functions; by (A4) they are already functions *on $D$* — the anchoring step that produced this state of affairs is outside the kernel.

**P3. Refinement preorder on views.**

> **Definition 4.3.** For views $v, v'$ on $D$: $v' \preceq v$ ("$v$ **refines** $v'$", "$v$ determines $v'$") iff there exists $r : Y_v \to Y_{v'}$ with $v' = r \circ v$.

> **Lemma 4.4.** $\preceq$ is a preorder on views, and $v' \preceq v \iff \ker(v') \le \ker(v)$ in $\mathrm{Part}(D)$. Consequently the equivalence $v \approx v'$ ($v \preceq v'$ and $v' \preceq v$) holds iff $\ker(v) = \ker(v')$.
>
> *Proof.* Reflexivity via $r = \mathrm{id}$; transitivity by composing the mediating maps. ($\Rightarrow$) If $v' = r \circ v$ and $v(Z) = v(Z')$ then $v'(Z) = v'(Z')$; so every block of $\ker(v)$ lies inside a block of $\ker(v')$, i.e. $\ker(v') \le \ker(v)$. ($\Leftarrow$) Suppose $\ker(v') \le \ker(v)$. By Fact 3.2 applied to $f = v$, $g = v'$, there is $h : v(D) \to Y_{v'}$ with $v' = h \circ v$; extend $h$ to all of $Y_v$ by sending $Y_v \setminus v(D)$ to any fixed value of $Y_{v'}$ (which is nonempty since $D$ is nonempty and $v'$ is total). $\square$

The preorder is promoted to primitive structure — rather than left as a derived remark — because it is the designated future *base site* for the sheaf-theoretic extension (§8, H4): coverages will be placed on $(V, \preceq)$, so the kernel must fix this structure correctly. (Part V locates the site precisely: the preorder enters through its content shadow $\mathrm{Ach}(V)$; Corollary 35.6.)

**P4. Information algebra (kernel instantiation).**

> **Definition 4.5.** The kernel's information algebra over $D$ is the subset algebra $\Phi_D = (\mathcal{P}(D), \cap, \le)$ of Definition 3.5.

The choice is a deliberate stub: the subset algebra is the minimal genuine information algebra, it is universal for the exact case (any exact information about "which candidate?" is a set of surviving candidates), and it keeps the kernel closed — no external algebra to negotiate with. General $\Phi$ re-enters at §8, H5.

**P5. Registration.**

> **Definition 4.6.** A **registration** for a view $v$ is a map $\kappa_v : Y_v \to \Phi_D$, converting presentations into information pieces. A registration is **sound** if for all $Z \in D$:
> $$
> Z \in \kappa_v(v(Z)).
> \tag{S}
> $$
> The **canonical registration** for $v$ is
> $$
> \kappa^{\mathrm{can}}_v(y) \;=\; v^{-1}(y) \;=\; \{\, Z \in D : v(Z) = y \,\}.
> $$

(S) is the one substantive axiom retained in the kernel: registered information must be true of the candidate that produced the presentation. It is the kernel residue of the eventual admissibility theory.

> **Lemma 4.7 (the canonical registration is the most informative sound one).** $\kappa^{\mathrm{can}}_v$ is sound, and for every sound registration $\kappa_v$ and every realized presentation $y \in v(D)$,
> $$
> v^{-1}(y) \;\subseteq\; \kappa_v(y),
> \qquad\text{equivalently}\qquad
> \kappa_v(y) \;\le\; \kappa^{\mathrm{can}}_v(y)
> \qquad \text{in the information order.}
> $$
> Every sound registration is at most as informative as the canonical one: $\kappa^{\mathrm{can}}$ extracts from a presentation everything that can soundly be extracted from that presentation alone.
>
> *Proof.* Soundness of $\kappa^{\mathrm{can}}$: $Z \in v^{-1}(v(Z))$ trivially. Now let $\kappa_v$ be sound and $y \in v(D)$. For every $Z \in v^{-1}(y)$, soundness gives $Z \in \kappa_v(v(Z)) = \kappa_v(y)$. Hence $v^{-1}(y) \subseteq \kappa_v(y)$, which is $\kappa_v(y) \le \kappa^{\mathrm{can}}_v(y)$ in the order of Definition 3.5. $\square$

A bookkeeping caution, worth internalizing here because it recurs throughout: the set inclusion and the information order run in opposite directions — larger subsets of $D$ exclude less and are therefore *weaker* as information (Definition 3.5).

By (A3), the kernel henceforth fixes $\kappa_v = \kappa^{\mathrm{can}}_v$ for all views and drops the superscript. Lemma 4.7 is what will later give the admissibility class $K$ a birthplace: general admissible registrations will be carved out of the sound ones, with the canonical registration as the extremal case (§8, H2).

**P6. Questions.**

> **Definition 4.8.** A **question** on $D$ is a map $q : D \to A_q$ into a set of **answers**. A **question family** is a set $Q$ of questions on $D$. The **content** of $q$ is its kernel $\ker(q) \in \mathrm{Part}(D)$; two questions with the same kernel are **equivalent** (they demand the same distinctions).

Identifying a question with the partition it induces follows the partition semantics of questions [Hamblin 1958; Groenendijk & Stokhof 1984]. The design decision embodied here is that questions and data will live in the *same* lattice $\mathrm{Part}(D)$, so that answerability becomes an order relation.

---

## 5. Derived objects

No new primitives are introduced from this point on; everything below is defined from P1–P6.

> **Definition 5.1 (registered representation).** For $S \subseteq V$ and $Z \in D$, the **registered representation** of $Z$ through $S$ is the combined information piece
> $$
> R_S(Z) \;=\; \prod_{v \in S} \kappa_v(v(Z)) \;=\; \bigcap_{v \in S} v^{-1}(v(Z)) \;\in\; \Phi_D,
> $$
> with the convention $R_\varnothing(Z) = 1 = D$.

$R_S(Z)$ is the set of candidates not excluded by any available registered presentation of $Z$: everything the data leaves open.

> **Definition 5.2 (induced indistinguishability and quotient).** For $S \subseteq V$, define on $D$:
> $$
> Z \sim_S Z' \quad :\iff \quad v(Z) = v(Z') \ \text{ for all } v \in S,
> $$
> and let
> $$
> \sigma(S) \;:=\; D/\!\sim_S \;=\; \bigvee_{v \in S} \ker(v) \;\in\; \mathrm{Part}(D)
> $$
> (the equality with the join is (3.1)). The map
> $$
> \sigma : \mathcal{P}(V) \to \mathrm{Part}(D)
> $$
> is the **content map** of the view family; $\sigma(S)$ is the **induced quotient** of $D$ by $S$; $\pi_S := \sigma(S)^\natural : D \twoheadrightarrow D/\sigma(S)$ is its quotient map.

> **Lemma 5.3 (representation computes indistinguishability).** For all $Z, Z' \in D$:
> $$
> Z \sim_S Z' \iff R_S(Z) = R_S(Z') \iff Z' \in R_S(Z),
> $$
> and $R_S(Z) = [Z]_{\sigma(S)}$, the $\sigma(S)$-block of $Z$.
>
> *Proof.* $R_S(Z) = \bigcap_{v\in S} v^{-1}(v(Z))$ is exactly $\{Z' : \forall v \in S,\ v(Z') = v(Z)\} = [Z]_{\sigma(S)}$, using (3.1). Blocks are equal iff they meet iff the candidates are equivalent. $\square$

Lemma 5.3 licenses conflating, in the kernel, the "algebraic" description (equality of registered pieces) with the "relational" description (joint indistinguishability): under canonical registration they coincide. Under general registrations they will not, and the gap between them is one of the phenomena the full theory is meant to measure.

> **Definition 5.4 (answerability).** A question $q$ on $D$ is **answerable from** $S \subseteq V$ iff there exists an **answer map** $\alpha_q : D/\sigma(S) \to A_q$ with
> $$
> q \;=\; \alpha_q \circ \pi_S ,
> $$
> i.e., iff $q$ factors through the induced quotient.

> **Definition 5.5 (unresolved pairs).** For $q$ and $S$ as above, the set of **unresolved pairs** is
> $$
> U(S, q) \;=\; \{\, (Z, Z') \in D \times D \;:\; Z \sim_S Z' \ \text{and}\ q(Z) \neq q(Z') \,\}.
> $$

Unresolved pairs are the exact witnesses of missing information: candidates the data cannot separate but the question must.

> **Proposition 5.6 (equivalent characterizations of answerability).** The following are equivalent:
>
> 1. $q$ is answerable from $S$;
> 2. $\ker(q) \le \sigma(S)$ in $\mathrm{Part}(D)$;
> 3. $U(S, q) = \varnothing$;
> 4. $q$ is constant on $R_S(Z)$ for every $Z \in D$.
>
> When these hold, the answer map $\alpha_q$ is unique.
>
> *Proof.* (1) $\iff$ (2) is Fact 3.2 applied to $f = \pi_S$, $g = q$, noting $\ker(\pi_S) = \sigma(S)$; uniqueness of $\alpha_q$ on the (full) image likewise. (2) $\iff$ (3): $\ker(q) \le \sigma(S)$ says every $\sigma(S)$-block lies inside a $\ker(q)$-block, i.e. $Z \sim_S Z' \Rightarrow q(Z) = q(Z')$, i.e. $U(S,q) = \varnothing$. (3) $\iff$ (4) by Lemma 5.3, since $R_S(Z)$ is the $\sim_S$-class of $Z$. $\square$

---

## 6. Structure theorems

### 6.1 The Galois connection

> **Definition 6.1.** Define $\tau : \mathrm{Part}(D) \to \mathcal{P}(V)$ by
> $$
> \tau(\pi) \;=\; \{\, v \in V \;:\; \ker(v) \le \pi \,\},
> $$
> the set of views **determined by** $\pi$: those that factor through the quotient $D \twoheadrightarrow D/\pi$ (Fact 3.2).

> **Theorem 6.2 (T1: adjunction between view sets and quotients).** The pair $(\sigma, \tau)$ is a Galois connection between $(\mathcal{P}(V), \subseteq)$ and $(\mathrm{Part}(D), \le)$:
> $$
> \sigma(S) \le \pi \quad \iff \quad S \subseteq \tau(\pi) \qquad \text{for all } S \subseteq V,\ \pi \in \mathrm{Part}(D).
> $$
> Consequently:
>
> 1. **(Compositionality of content.)** $\sigma$ preserves arbitrary unions as joins: $\sigma\big(\bigcup_i S_i\big) = \bigvee_i \sigma(S_i)$; in particular $\sigma(S \cup S') = \sigma(S) \vee \sigma(S')$ and $\sigma(\varnothing) = \bot$.
> 2. **(Informational closure of view sets.)** $\mathrm{cl} := \tau\sigma$ is a closure operator on $\mathcal{P}(V)$; $\mathrm{cl}(S)$ is the set of all views in $V$ whose presentations are determined by the views in $S$. Adding to $S$ any view it already determines does not change content: $\sigma(\mathrm{cl}(S)) = \sigma(S)$.
> 3. **(Achievable quotients.)** $\mathrm{int} := \sigma\tau$ is an interior operator on $\mathrm{Part}(D)$; its fixed points — equivalently, the image of $\sigma$ — are the **achievable quotients**: the distinction-structures realizable by some subset of the available views. They form a complete lattice $\mathrm{Ach}(V)$ with joins computed as in $\mathrm{Part}(D)$ and bottom $\bot$; and $\sigma, \tau$ restrict to an isomorphism between $\mathrm{Ach}(V)$ and the lattice of closed view sets.
>
> *Proof.* The adjunction: $\sigma(S) \le \pi \iff \bigvee_{v \in S}\ker(v) \le \pi \iff \forall v \in S:\ \ker(v) \le \pi \iff \forall v \in S:\ v \in \tau(\pi) \iff S \subseteq \tau(\pi)$. Items 1–3 are then instances of Fact 3.4, with the join-preservation in 1 also verifiable directly from $\sigma(S) = \bigvee_{v\in S} \ker(v)$: joins of joins regroup. That $\mathrm{Ach}(V)$ is closed under arbitrary joins: $\bigvee_i \sigma(S_i) = \sigma(\bigcup_i S_i) \in \mathrm{Im}\,\sigma$; it contains $\bot = \sigma(\varnothing)$; a complete join-subsemilattice with bottom of a complete lattice is a complete lattice (meets given by $\mathrm{int}$ of the ambient meet). $\square$

Item 1 deserves emphasis. Read through Definition 5.1 it says: *registering views separately and combining the pieces yields the same content as registering the combined view* — the kernel's first genuine coherence law between registration and combination. The next proposition states this at the level of individual pieces.

> **Proposition 6.3 (coherence of canonical registration with combination).** For views $v, w$ on $D$, let $\langle v, w \rangle : D \to Y_v \times Y_w$ be the pairing. Then for all $Z \in D$:
> $$
> \kappa_{\langle v, w \rangle}\big( (v(Z), w(Z)) \big) \;=\; \kappa_v(v(Z)) \cdot \kappa_w(w(Z)),
> $$
> and inductively likewise for arbitrary pairings. Register-then-combine equals combine-then-register.
>
> *Proof.* $\langle v,w\rangle^{-1}(v(Z), w(Z)) = v^{-1}(v(Z)) \cap w^{-1}(w(Z))$, and combination in $\Phi_D$ is intersection. $\square$

Proposition 6.3 is the exact-deterministic shadow of the sheaf-theoretic gluing condition: locally registered data cohere into a unique combined piece. In the extensions where registration is non-canonical or views are noisy, this law can fail, and the two modes of its failure (no coherent combination; multiple coherent combinations) are the phenomena the sheaf layer is designed to classify (§8, H4; classified in Part V, §39, as contextual evidence and underdetermination).

### 6.2 The structure of answerable questions

> **Theorem 6.4 (T2: the answerable questions form a principal down-set generated by the data).** Fix $S \subseteq V$ and let
> $$
> \mathcal{A}(S) \;=\; \{\, \rho \in \mathrm{Part}(D) \;:\; \rho \text{ is the kernel of a question answerable from } S \,\}.
> $$
> Then
> $$
> \mathcal{A}(S) \;=\; {\downarrow}\,\sigma(S) \;=\; \{\, \rho \in \mathrm{Part}(D) : \rho \le \sigma(S) \,\}.
> $$
> Consequently:
>
> 1. $\mathcal{A}(S)$ is closed under arbitrary joins and nonempty ambient meets of its members (it is a complete lattice in its own right, whose empty meet is $\sigma(S)$ rather than the ambient $\top$): any combination of answerable questions is answerable, and any coarsening of an answerable question is answerable.
> 2. The quotient map $\pi_S : D \to D/\sigma(S)$, regarded as a question, is itself answerable and is the **maximally informative answerable question**: every answerable $q$ factors uniquely through it. In this precise sense, $\sigma(S)$ *is* the total exact information content of $S$ over $D$.
>
> *Proof.* The identification $\mathcal{A}(S) = {\downarrow}\sigma(S)$ is Proposition 5.6 (1)$\iff$(2), noting every $\rho \in \mathrm{Part}(D)$ is the kernel of some question, e.g. its own quotient map. Nonempty families in a principal down-set have their ambient meet in that down-set; closure under joins holds because $\rho_i \le \sigma(S)$ for all $i$ implies $\bigvee_i \rho_i \le \sigma(S)$. For item 2: $\ker(\pi_S) = \sigma(S) \le \sigma(S)$, so $\pi_S$ is answerable; the factorization of any answerable $q$ through $\pi_S$, with uniqueness, is Proposition 5.6 again. $\square$

Theorem 6.4 turns "dataset audit" into a definite mathematical task: to audit $S$ over $(D, Q)$ is to compute (or bound) the single partition $\sigma(S)$ and compare it against $\{\ker(q) : q \in Q\}$.

### 6.3 Marginal value of a view

> **Theorem 6.5 (T3: exact characterization of when a new view helps).** Let $S \subseteq V$, let $q$ be a question, and let $w$ be a view on $D$. Then:
>
> 1. $U(S \cup \{w\},\, q) \;=\; U(S, q) \,\cap\, \{\, (Z,Z') : w(Z) = w(Z') \,\}$.
> 2. $w$ **strictly helps** $q$ given $S$ — i.e. $U(S \cup \{w\}, q) \subsetneq U(S, q)$ — iff there is an unresolved pair $(Z, Z') \in U(S, q)$ with $w(Z) \neq w(Z')$.
> 3. $q$ becomes answerable upon adding $w$ iff $w$ separates *every* unresolved pair: $\forall (Z,Z') \in U(S,q):\ w(Z) \neq w(Z')$.
>
> *Proof.* $Z \sim_{S \cup \{w\}} Z'$ iff $Z \sim_S Z'$ and $w(Z) = w(Z')$; intersecting with the condition $q(Z) \neq q(Z')$ gives 1. Items 2 and 3 are immediate from 1 and Proposition 5.6 (3). $\square$

This is the kernel form of **active data acquisition**: given a target question family, the next view to acquire should be chosen to separate remaining unresolved pairs — the theory says exactly which pairs those are, namely the elements of $\bigcup_{q \in Q} U(S, q)$.

### 6.4 Universal property of the induced quotient

The final kernel theorem upgrades the induced quotient from a construction to an object characterized by what it does: it is the coarsest lossless consolidation of the available views.

> **Definition 6.6.** A surjection $e : D \twoheadrightarrow Q_e$ is an **$S$-consolidation** if every view $v \in S$ factors through $e$ (i.e. $v = f_v \circ e$ for some $f_v : Q_e \to Y_v$): the consolidation retains everything each available view presents.

> **Theorem 6.7 (T4: the induced quotient is the terminal consolidation).**
>
> 1. $\pi_S : D \twoheadrightarrow D/\sigma(S)$ is an $S$-consolidation.
> 2. For every $S$-consolidation $e : D \twoheadrightarrow Q_e$ there is a unique surjection $u : Q_e \twoheadrightarrow D/\sigma(S)$ with $\pi_S = u \circ e$. Thus $\pi_S$ is the **coarsest** $S$-consolidation, and every other one maps onto it; it is terminal in the evident category of $S$-consolidations (objects: consolidations; morphisms: surjections commuting with the maps from $D$).
> 3. Concretely, $D/\sigma(S) \cong \mathrm{Im}\, \langle v \rangle_{v \in S} \subseteq \prod_{v \in S} Y_v$: the induced quotient is (isomorphic to) the image of the joint presentation map, i.e. the set of presentation profiles actually realized over $D$.
>
> *Proof.* 1: $\ker(v) \le \sigma(S) = \ker(\pi_S)$ for each $v \in S$, so Fact 3.2 gives the factorization. 2: If $e$ is an $S$-consolidation, then for each $v \in S$ the factorization $v = f_v \circ e$ gives $e(Z) = e(Z') \Rightarrow v(Z) = v(Z')$, i.e. $\ker(v) \le \ker(e)$. As this holds for all $v \in S$, $\sigma(S) = \bigvee_{v \in S} \ker(v) \le \ker(e)$. By Fact 3.2 (with $f = e$, $g = \pi_S$) there is $u : Q_e \to D/\sigma(S)$, unique since $e$ is surjective, with $\pi_S = u \circ e$; $u$ is surjective because $\pi_S$ is. 3: Image factorization (Fact 3.1) of the pairing $\langle v \rangle_{v \in S}$, whose kernel is $\sigma(S)$ by (3.1). $\square$

Theorem 6.7 is the result that makes "answerability as factorization" contentful rather than definitional: the induced quotient is not merely *a* structure through which answerable questions factor; it is *the* universal such structure — the free lossless summary of the data over the contrast domain. It is also the precise point at which the sheaf-theoretic extension will attach a second universal construction (sheafification as registration-plus-consolidation; §8, H4).

### 6.5 Corollaries: the kernel's operational content

The following restatements collect what the kernel already delivers for the motivating applications. Each is an immediate corollary of §§6.1–6.4.

> **Corollary 6.8 (dataset sufficiency).** A dataset, modeled as a view set $S$, is sufficient for a question family $Q$ over $D$ iff $\ker(q) \le \sigma(S)$ for every $q \in Q$; equivalently iff $\bigvee_{q \in Q} \ker(q) \le \sigma(S)$.

> **Corollary 6.9 (missing-information analysis).** If $q$ is not answerable from $S$, the failure is witnessed exactly by the nonempty set $U(S, q)$ of unresolved pairs, and any remedy must separate them (Theorem 6.5).

> **Corollary 6.10 (entailment discipline).** Call an answer $a$ to $q$ **entailed by $S$ at $Z$** if $q$ is answerable from $S$ and $a = \alpha_q(\pi_S(Z))$. A system answering $q$ from the registered content of $S$ alone can be correct on all of $D$ only for answerable $q$; for unanswerable $q$, any answering policy is wrong on at least one member of some unresolved pair. This grounds, in the exact case, the normative distinction between answers *entailed* by the data and answers that add information beyond it — the kernel form of an anti-overclaiming criterion. (Graded and probabilistic versions of this distinction belong to extension H3.)

One further result belongs here, because it converts the positioning claim of §2 — that the kernel supplies the layer information algebra presupposes — into a theorem: the passage from views to pieces does not merely interface with an information algebra; it *generates* one.

> **Proposition 6.11 (the kernel generates its downstream information algebra).** For $\pi \in \mathrm{Part}(D)$ call $E \subseteq D$ **$\pi$-saturated** if it is a union of $\pi$-blocks, write $\Phi_\pi \subseteq \mathcal{P}(D)$ for the $\pi$-saturated sets (canonically $\Phi_\pi \cong \mathcal{P}(D/\pi)$), and for $\rho \in \mathrm{Part}(D)$ let $s_\rho(E)$ denote the **$\rho$-saturation** of $E$: the union of the $\rho$-blocks meeting $E$. Over the achievable-quotient lattice $\mathrm{Ach}(V)$ of Theorem 6.2(3), set
> $$
> \Phi \;=\; \bigsqcup_{\pi \in \mathrm{Ach}(V)} \Phi_\pi, \qquad d(E, \pi) = \pi, \qquad (E, \pi) \otimes (F, \rho) \;=\; (E \cap F,\ \pi \vee \rho), \qquad (E, \pi)^{\Rightarrow \rho} \;=\; \big(s_\rho(E),\ \rho\big).
> $$
> Since the union is disjoint, a **piece is formally the labeled pair** $(E, \pi)$ — the same subset is saturated for many partitions (any $\pi$-saturated set is $\pi'$-saturated for every finer $\pi'$), and the label is part of the datum; the unlabeled abbreviations $\phi \otimes \psi = \phi \cap \psi$ and $\phi^{\Rightarrow\rho} = s_\rho(\phi)$ used below always carry the label composition displayed here.
> Then:
>
> 1. **(Labeling.)** $\phi \otimes \psi \in \Phi_{d(\phi) \vee d(\psi)}$, and $\phi^{\Rightarrow\rho} \in \Phi_\rho$.
> 2. **(Transitivity of focusing.)** $(\phi^{\Rightarrow\rho})^{\Rightarrow\rho'} = \phi^{\Rightarrow\rho'}$ for $\rho' \le \rho$.
> 3. **(Combination axiom.)** For $\phi \in \Phi_\pi$ and $\psi \in \Phi_\rho$ with $\rho \le \pi$: $(\phi \otimes \psi)^{\Rightarrow \rho} = \phi^{\Rightarrow\rho} \otimes \psi$.
>
> Consequently $(\Phi, \mathrm{Ach}(V); d, \otimes, \Rightarrow)$ is a labeled idempotent information algebra over the domain lattice $\mathrm{Ach}(V)$ in the generalized set-algebra sense of [Kohlas 2017, §§2.5–3.1]. The canonical registration of each $v$ lands in the fiber $\Phi_{\ker(v)}$ (its values $v^{-1}(y)$ are $\ker(v)$-saturated), and the registered representation $R_S(Z)$ of Definition 5.1 is the combination of the per-view pieces, landing in $\Phi_{\sigma(S)}$ by item 1 — Proposition 6.3 in algebra-typed form. The focusing operator $s_\rho$ is exactly Pawlak's upper approximation relative to $\rho$ (§2), so the generated algebra is the rough-set approximation calculus organized over the achievable quotients. The generation is functorial in the view family: enlarging $V$ enlarges $\mathrm{Ach}(V)$ (Theorem 6.2) and embeds the corresponding algebras.
>
> *Proof.* 1: Let $x \in \phi \cap \psi$ and let $y$ lie in $x$'s $(d(\phi) \vee d(\psi))$-block, i.e. in both $x$'s $d(\phi)$-block and $x$'s $d(\psi)$-block (Fact 3.3); saturation gives $y \in \phi$ and $y \in \psi$. That $s_\rho(\phi)$ is $\rho$-saturated is immediate from its definition. 2: For $\rho' \le \rho$ every $\rho$-block lies inside a $\rho'$-block; a $\rho'$-block meets $s_\rho(E)$ iff it meets $E$ — it contains any $\rho$-block witnessing the former, and that block meets $E$; conversely $E \subseteq s_\rho(E)$. 3: ($\subseteq$) If $x$'s $\rho$-block $B$ meets $\phi \cap \psi$, then $B$ meets $\phi$, so $x \in s_\rho(\phi)$; and $B$ meets $\psi$, which is $\rho$-saturated, so $B \subseteq \psi$ and $x \in \psi$. ($\supseteq$) If $x \in s_\rho(\phi) \cap \psi$, then $B$ meets $\phi$ at some $z$; since $x \in \psi$ and $\psi$ is $\rho$-saturated, $B \subseteq \psi$, so $z \in \phi \cap \psi$ and $x \in s_\rho(\phi \cap \psi)$. The remaining axioms (commutative idempotent semigroup with the unit piece $D \in \Phi_\pi$ neutral and $\varnothing$ absorbing in each fiber) are immediate; see [Kohlas 2017, §§2.5–3.1] for the generalized set-algebra formulation. $\square$

**Mathematical scope.** The full saturation law is $s_\rho(E\cap s_\rho(F))=s_\rho(E)\cap s_\rho(F)$, proved by considering each $\rho$-block. Also $E\subseteq s_\rho(E)$, $s_\rho(\varnothing)=\varnothing$, and every piece has a supporting label by construction. These establish the generalized set-algebra realization. Arbitrary focusing operators need not commute: on $D=\{1,2,3\}$, $a=12|3$, $b=1|23$, $s_a s_b(\{1\})=\{1,2\}$ but $s_b s_a(\{1\})=D$. Appendix D.13 proves the exact rectangular block-intersection criterion for two extractions to commute. Standard variable-domain propagation requires the corresponding conditional-independence/extension hypotheses. Moreover $\mathrm{Ach}(V)$ is join-closed but need not be closed under ambient meets; Part XI must preserve this distinction.

---

## 7. What the kernel does and does not establish

It is worth being precise about the epistemic status of §6. The individual proofs are short, and several facts (notably Proposition 5.6) are elementary once the definitions are in place; the kernel's contribution is not their difficulty but their *arrangement*: a fixed, closed base of primitives (P1–P6), a derived layer provably adequate to the operational notions (sufficiency, missing information, marginal value, entailment), and two structural results — the adjunction (Theorem 6.2) and the universal property (Theorem 6.7) — that characterize the central object rather than merely constructing it. These are the load-bearing walls on which every planned extension rests, and the discipline that nothing in §§4–6 refers to anything deferred is what will keep the extensions modular.

It is also worth pre-empting a deflationary reading. The kernel's ingredients are classical — kernels of maps, partition lattices, factorization, Galois connections — and none is claimed as new; in the special case of a single object–attribute table the induced quotient is Pawlak's indiscernibility partition (§2). The novelty claimed is architectural: the role this quotient is assigned. It is simultaneously the registration target of raw presentations, the audit object for datasets, the base object that the admissibility layer bounds, the designated zero-noise fiber of the graded theory, and the attachment interface for anchoring, extraction, and gluing. The contribution is the load-bearing arrangement; the anomaly and stratification results of the later parts are its returns.

What the kernel does **not** contain, by design:

- an account of aboutness (anchoring is suppressed by (A4));
- a theory of which registrations are legitimate ((A3) fixes the canonical one; Lemma 4.7 only bounds the sound ones);
- any treatment of noise, approximation, or degree ((A2));
- any interaction between contrast domains ((A5));
- a quantitative layer connecting the induced quotient to entropic or decision-theoretic quantities.

Extraction over a single domain, by contrast, is already present: Proposition 6.11 equips the registered pieces with a nontrivial focusing operation. Each absence is deliberate and localized; §8 explains how the later parts supply them.

---

## 8. How the theory grows from the kernel

The kernel is never revised. No later part redefines $\sigma$, answerability, registration, or the partition lattice. What later parts do is *generalize a primitive* — a view becomes a channel, the canonical registration becomes a class of admissible registrations, a pre-anchored view becomes an emission with an attribution step — and then show that the kernel reappears, unchanged, as a special case of the generalized theory. This section makes that relationship precise, lists every standing assumption the monograph introduces, and records where each kernel theorem is re-examined.

### 8.1 Extensions and recovery

An **extension** of the kernel consists of three pieces of data:

1. **generalized primitives** replacing one or more of P1–P6 (for example, channels $D \to \Pr(Y)$ in place of maps $D \to Y$);
2. an **embedding** of kernel data into the generalized primitives (a map $v$ is the channel $Z \mapsto \delta_{v(Z)}$);
3. a **recovery theorem**: on embedded data, every construction of the extension coincides with its kernel counterpart, so that the kernel's definitions and theorems hold verbatim there.

An extension **relaxes** a standing assumption when the embedded data are exactly the data satisfying that assumption: the kernel is the sub-theory on which the assumption holds, and the extension studies what happens off it. Relaxing an assumption therefore never weakens a kernel theorem; it asks which kernel theorems remain true *in the larger setting*, and in what form. Each part answers this question in a "fate of the kernel theorems" section, classifying each result as surviving exactly, surviving laxly (an inequality replaces an equation), or failing, and locating the mechanism responsible.

The kernel enters the later parts in three ways: as the **target of recovery** (what each extension must reduce to), as a **template** (the kernel theorems T1–T4 of §6 are the questions every extension is asked), and as an **ingredient** (for example, the canonical content $\sigma(T)$ is the upper bound in the admissibility axiom (K1), and the achievable quotients $\mathrm{Ach}(V)$ label the information algebras of Parts V and XI).

Not every part is an extension in this sense. Parts V, VII, and IX introduce no new primitive; they ask new questions of the existing layers — whether local content glues into global content (Part V), and how the resulting intervals are measured in bits (Part VII) or by Le Cam deficiency (Part IX). Parts VI and VIII study two or three relaxations at once.

### 8.2 The assumption ledger

The table lists every standing assumption in the monograph, where it is introduced, where it is relaxed, and the theorem that recovers the more restricted theory. The assumptions (A4′), (A6), and (A7) and the view-set finiteness convention are introduced by later parts, each in order to build its extension exactly.

| assumption | introduced | relaxed in | recovery | remarks |
|---|---|---|---|---|
| (A1) totality | §4.1 | never | — | in force throughout |
| (A2) determinism | §4.1 | Part III (graded views) | Theorem 24.2 | deterministic channels are the embedded kernel views |
| (A3) canonical registration | §4.1 | Part II (admissibility structures) | Proposition 14.6 | full admissibility $K^{\mathrm{can}}$ is the embedded kernel |
| (A4) anchoring suppressed | §4.1 | Part III, §19 (interface); Part IV (theory) | Theorem 32.1 | recovery of all records additionally requires sterile context |
| (A5) single fixed domain | §4.1 | Part XI (domain families) | Theorem 88.1 | the singleton family is the embedded kernel |
| finite view sets | §14 | partly: Theorem 15.1, Corollary 15.4 | — | a convention, not a modelling assumption |
| (A4′) sound unique anchoring | Definition 19.7 | Part IV | Theorem 32.1 | graded form of (A4) |
| (A6) finite domains and presentation spaces | §20 | partly: Appendix A | Proposition A.1 | the general measurable case is open (§86, P6) |
| (A7) reduced-form corruption | §29 | Part X (dynamical scenes) | Theorem 80.1 | horizon one recovers the static theory |

The parts that ask questions rather than relax assumptions are: descent and obstruction (Part V, hook H4), the Shannon evaluation (Part VII), and the decision-theoretic evaluation (Part IX). Their kernel cases are recorded in Theorem 42.1 and in the evaluation of degenerate intervals (Proposition 53.2).

### 8.3 The hooks

The five hooks below name the extensions that the kernel was designed to accept, the primitive each attaches to, and the assumption it relaxes. They are stated as programmes; the later parts carry them out.

**H1. Anchoring (attaches at P2; relaxes (A4)).** In the kernel a view is a function $v : D \to Y_v$, so aboutness is presupposed. The anchoring extension replaces this with raw presentations $(y, c)$, whose attribution to an origin is itself an operation depending on the context $c$ and admitting ambiguity (several admissible origins) and failure (none, or the wrong one). Mis-anchoring — reference failure, entity-resolution error, dataset mislabeling — becomes representable, and its effect on content becomes a definite mathematical question. The interface is fixed in Part III, §19; the theory is Part IV, with corruption studied further in Parts VIII and X.

**H2. Admissible registration (attaches at P5; relaxes (A3)).** The kernel fixes canonical registration, which Lemma 4.7 shows is extremal among sound registrations. The extension introduces a class of admissible registrations — sound maps satisfying further constraints such as invariance or resource bounds — and studies the content they induce, which lies between $\bot$ and $\sigma$. This is the formal home of the distinction, important for model interpretability, between what a representation *encodes* and what an *admissible decoder can extract* (the probe-power problem). The extension is Part II.

**H3. Noise and degree (attaches at P2; relaxes (A2)).** Views become stochastic: channels $v : D \to \Pr(Y_v)$. Exact indistinguishability is replaced by statistical structure — sufficient statistics and the factorization theorem [Halmos & Savage 1949], the Blackwell order on experiments [Blackwell 1951, 1953], and soft quotients in the sense of the information bottleneck [Tishby, Pereira & Bialek 1999]. The target results are graded analogues of Theorems 6.2–6.7, with the kernel as the zero-noise case, together with the connection to Shannon quantities. The extension is Part III, §§20–24, with the Shannon bridge in §22.4.

**H4. Local-to-global semantics (attaches at P3; relaxes no assumption).** Given content attached to subsets of a view family, when does local content determine global content, and when do locally coherent data admit a global description? The kernel's coherence law (Proposition 6.3) is the trivial case. This hook asks a question of every layer rather than relaxing an assumption; it is answered in Part V.

**H5. Multiple domains and information algebra (attaches at P1 and P4; relaxes (A5)).** Reintroduce the ambient class of targets and a family of related contrast domains, and establish coherence of registration with extraction, and functoriality of $\sigma$ along maps between contrast domains (restriction, refinement, and coarsening of $D$), extending Theorem 6.2. Proposition 6.11 already supplies the single-domain algebra. The extension is Part XI.

### 8.4 The kernel theorems as a template

The table indicates where the kernel's structure theorems are re-examined and what they become. Entries are summaries; the cited results state the hypotheses.

| kernel result | admissibility (Part II) | noise (Part III) |
|---|---|---|
| T1, adjunction (Thm 6.2) | holds for separable content (Thm 15.1); for joint content iff the structure is separable (Cor 15.4) | fails for zero-error content even under conditional independence (Prop 22.3), restored for its confusability graph (Prop 22.3′); holds for statistical content on conditionally independent families (Prop 22.4); no join law for full experiments (Prop 22.5) |
| T2, answerable questions form ${\downarrow}\sigma(S)$ (Thm 6.4) | holds for separable content (§15.1) | zero-error and asymptotic answerability are principal ideals (Thms 22.1, 22.2); $\varepsilon$-answerability is not (§22.1) |
| T3, marginal value (Thm 6.5) | holds for separable content (§15.1) | marginal value is conditional mutual information (Thm 22.7(3)) |
| T4, terminal consolidation (Thm 6.7) | terminal among per-view consolidations (§15.1) | minimal sufficient statistic (Thm 22.6) |
| coherence law (Prop 6.3) | fails: the registration anomaly (Prop 15.2, §16) | conditional: holds for statistical content under conditional independence |
| canonical registration is extremal (Lemma 4.7) | bracketing $\bot \le \sigma^{\mathrm{sep}}_K \le \sigma^{\mathrm{jnt}}_K \le \sigma$ (Prop 14.6) | minimal sufficiency is the coarsest lossless registration (§22.3) |

For anchoring (Part IV), the analogue of Theorem 6.4 is Corollary 28.1 — attribution is itself a question, with zero-error and asymptotic criteria of the same form — and the analogue of Lemma 4.7 is Theorem 30.4: loyal policies are extremal under sterile context, and Proposition 30.2 shows that they need not be otherwise.

The kernel is complete relative to its assumptions: no statement in §§4–6 depends on H1–H5.

---

## 9. Notation summary

| Symbol | Meaning | Defined in |
|---|---|---|
| $D$ | contrast domain; candidates $Z, Z' \in D$ | Def. 4.1 |
| $v : D \to Y_v$ | view with presentation space $Y_v$ | Def. 4.2 |
| $V$, $S \subseteq V$ | view family; available views | Def. 4.2 |
| $v' \preceq v$ | view refinement (determination) | Def. 4.3 |
| $\mathrm{Part}(D)$, $\le$, $\vee$, $\top$, $\bot$ | partition lattice; refinement order (finer $=$ greater) | §3.2 |
| $\ker(f)$ | kernel partition of a map | §3.1 |
| $\Phi_D = (\mathcal{P}(D), \cap, \le)$ | subset information algebra; $1 = D$, $0 = \varnothing$ | Def. 3.5 |
| $\kappa_v$, (S) | registration; soundness axiom | Def. 4.6 |
| $q : D \to A_q$, $\ker(q)$ | question; its content | Def. 4.8 |
| $R_S(Z)$ | registered representation of $Z$ through $S$ | Def. 5.1 |
| $\sim_S$, $\sigma(S)$, $\pi_S$ | induced indistinguishability, quotient, quotient map | Def. 5.2 |
| $U(S, q)$ | unresolved pairs | Def. 5.5 |
| $\tau$, $\mathrm{cl}$, $\mathrm{Ach}(V)$ | upper adjoint; view-set closure; achievable quotients | §6.1 |

---

## References

- Abramsky, S., and Brandenburger, A. (2011). "The Sheaf-Theoretic Structure of Non-Locality and Contextuality." *New Journal of Physics* 13, 113036.
- Aumann, R. J. (1976). "Agreeing to Disagree." *The Annals of Statistics* 4(6), 1236–1239.
- Bar-Hillel, Y., and Carnap, R. (1952). "An Outline of a Theory of Semantic Information." Technical Report 247, Research Laboratory of Electronics, MIT.
- Barwise, J., and Perry, J. (1983). *Situations and Attitudes.* MIT Press.
- Barwise, J., and Seligman, J. (1997). *Information Flow: The Logic of Distributed Systems.* Cambridge University Press.
- Bateson, G. (1972). *Steps to an Ecology of Mind.* Ballantine Books.
- Birkhoff, G. (1967). *Lattice Theory*, 3rd ed. American Mathematical Society Colloquium Publications, vol. 25.
- Blackwell, D. (1951). "Comparison of Experiments." *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*, 93–102.
- Blackwell, D. (1953). "Equivalent Comparisons of Experiments." *The Annals of Mathematical Statistics* 24(2), 265–272.
- Cover, T. M., and Thomas, J. A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
- Davey, B. A., and Priestley, H. A. (2002). *Introduction to Lattices and Order*, 2nd ed. Cambridge University Press.
- Dretske, F. I. (1981). *Knowledge and the Flow of Information.* MIT Press.
- Erné, M., Koslowski, J., Melton, A., and Strecker, G. E. (1993). "A Primer on Galois Connections." *Annals of the New York Academy of Sciences* 704, 103–125.
- Floridi, L. (2004). "Outline of a Theory of Strongly Semantic Information." *Minds and Machines* 14(2), 197–221.
- Ganter, B., and Wille, R. (1999). *Formal Concept Analysis: Mathematical Foundations.* Springer.
- Groenendijk, J., and Stokhof, M. (1984). *Studies on the Semantics of Questions and the Pragmatics of Answers.* PhD thesis, University of Amsterdam.
- Halmos, P. R., and Savage, L. J. (1949). "Application of the Radon–Nikodym Theorem to the Theory of Sufficient Statistics." *The Annals of Mathematical Statistics* 20(2), 225–241.
- Hamblin, C. L. (1958). "Questions." *Australasian Journal of Philosophy* 36(3), 159–168.
- Hermann, R., and Krener, A. J. (1977). "Nonlinear Controllability and Observability." *IEEE Transactions on Automatic Control* 22(5), 728–740.
- Hintikka, J. (2007). *Socratic Epistemology: Explorations of Knowledge-Seeking by Questioning.* Cambridge University Press.
- Kalman, R. E. (1963). "Mathematical Description of Linear Dynamical Systems." *SIAM Journal on Control* 1(2), 152–192.
- Kohlas, J. (2003). *Information Algebras: Generic Structures for Inference.* Springer.
- Kohlas, J. (2017). "Algebras of Information. A New and Extended Axiomatic Foundation." arXiv:1701.02658.
- Krantz, D. H., Luce, R. D., Suppes, P., and Tversky, A. (1971). *Foundations of Measurement, Vol. I: Additive and Polynomial Representations.* Academic Press.
- Kripke, S. A. (1980). *Naming and Necessity.* Harvard University Press.
- Millikan, R. G. (1984). *Language, Thought, and Other Biological Categories.* MIT Press.
- Narens, L. (2002). *Theories of Meaningfulness.* Lawrence Erlbaum Associates.
- Ore, O. (1942). "Theory of Equivalence Relations." *Duke Mathematical Journal* 9(3), 573–627.
- Pawlak, Z. (1982). "Rough Sets." *International Journal of Computer and Information Sciences* 11(5), 341–356.
- Pawlak, Z. (1991). *Rough Sets: Theoretical Aspects of Reasoning about Data.* Kluwer.
- Putnam, H. (1975). "The Meaning of 'Meaning'." In K. Gunderson (ed.), *Language, Mind, and Knowledge* (Minnesota Studies in the Philosophy of Science 7), 131–193. University of Minnesota Press.
- Robinson, M. (2017). "Sheaves Are the Canonical Data Structure for Sensor Integration." *Information Fusion* 36, 208–224.
- Schaffer, J. (2005). "Contrastive Knowledge." In T. S. Gendler and J. Hawthorne (eds.), *Oxford Studies in Epistemology*, vol. 1, 235–271. Oxford University Press.
- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal* 27, 379–423 and 623–656.
- Shannon, C. E. (1953). "The Lattice Theory of Information." *Transactions of the IRE Professional Group on Information Theory* 1(1), 105–107.
- Shenoy, P. P., and Shafer, G. (1990). "Axioms for Probability and Belief-Function Propagation." In *Uncertainty in Artificial Intelligence 4*, 169–198. North-Holland.
- Tishby, N., Pereira, F. C., and Bialek, W. (1999). "The Information Bottleneck Method." *Proceedings of the 37th Allerton Conference on Communication, Control and Computing*, 368–377.
- van Fraassen, B. C. (1980). *The Scientific Image.* Oxford University Press.
- Wille, R. (1982). "Restructuring Lattice Theory: An Approach Based on Hierarchies of Concepts." In I. Rival (ed.), *Ordered Sets*, 445–470. Reidel.
- Wiśniewski, A. (1995). *The Posing of Questions: Logical Foundations of Erotetic Inferences.* Kluwer.
- Xu, C., Tao, D., and Xu, C. (2013). "A Survey on Multi-view Learning." arXiv:1304.5634.
- Zhao, J., Xie, X., Xu, X., and Sun, S. (2017). "Multi-view Learning Overview: Recent Progress and New Challenges." *Information Fusion* 38, 43–54.
