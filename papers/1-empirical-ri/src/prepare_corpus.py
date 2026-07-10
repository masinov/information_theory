"""prepare_corpus.py — export SemCor sense-annotated tokens to tokens.jsonl,
per INSTRUCTIONS.md §2.

For a set of polysemous target words (>=3 senses, >=300 tokens), each token line:
    {"word","sense","split","features":{prev_pos,next_pos,prev_lemma,next_lemma,frame}}

Feature discipline: 5 context types, each bucketed to the top-(k-1) symbols + OTHER
with k=8 (alphabet <= 8). The bucketing VOCAB is fit on the train split only
(design note in §2); we tag each token with split in {train, eval} so the
experiment can estimate channels on eval while the buckets stay frozen from train.
Only senses with >= MIN_SENSE tokens are kept; rarer senses are logged as refusals.

emb8 (contextual-embedding k-means cluster) is optional per §2 and omitted here to
avoid a transformer dependency; the five symbolic context types suffice for the
covering / selection / certificate protocol.
"""
import json, os, sys
from collections import Counter, defaultdict
from nltk.corpus import semcor
from nltk.tree import Tree
from nltk.corpus.reader.wordnet import Lemma

TARGET_WORDS = ["give", "take", "tell", "think", "go", "time", "first"]
MIN_SENSE = 30          # keep senses with >= this many tokens
K_BUCKET = 8            # feature alphabet cap: top-(K-1) + OTHER
TRAIN_FRAC = 0.5        # fraction of a word's tokens used to fit bucket vocab
FEATURE_TYPES = ["prev_pos", "next_pos", "prev_lemma", "next_lemma", "frame"]


def linearize(sent):
    """Flatten a semcor tagged_sents(tag='both') sentence into ordered tokens:
    list of dict(pos, lemma, sense) where sense is a WordNet key or None."""
    toks = []
    for chunk in sent:
        if isinstance(chunk, Tree):
            lab = chunk.label()
            if isinstance(lab, Lemma):                 # sense-tagged content word
                inner = chunk[0]
                pos = inner.label() if isinstance(inner, Tree) else "X"
                try:
                    key = lab.key()
                except Exception:
                    key = None
                toks.append(dict(pos=pos, lemma=lab.name(), sense=key))
            elif isinstance(lab, str):                 # untagged word: label is POS
                leaves = chunk.leaves()
                toks.append(dict(pos=lab, lemma=(leaves[0].lower() if leaves else "?"),
                                 sense=None))
        else:  # bare token
            toks.append(dict(pos="X", lemma=str(chunk).lower(), sense=None))
    return toks


def raw_features(toks, i):
    prev = toks[i-1] if i > 0 else None
    nxt = toks[i+1] if i+1 < len(toks) else None
    pp = prev["pos"] if prev else "BOS"
    npos = nxt["pos"] if nxt else "EOS"
    return dict(prev_pos=pp, next_pos=npos,
                prev_lemma=prev["lemma"] if prev else "BOS",
                next_lemma=nxt["lemma"] if nxt else "EOS",
                frame=pp + "_" + npos)


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "data/tokens.jsonl"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    print("scanning SemCor ...")
    sents = semcor.tagged_sents(tag="both")

    # pass 1: collect raw tokens (with raw features) per target word
    raw = defaultdict(list)  # word -> list of (sense, raw_features)
    for sent in sents:
        toks = linearize(sent)
        for i, t in enumerate(toks):
            if t["sense"] and t["lemma"] in TARGET_WORDS:
                raw[t["lemma"]].append((t["sense"], raw_features(toks, i)))

    refusals = []
    all_lines = []
    summary = {}
    for word in TARGET_WORDS:
        items = raw.get(word, [])
        sense_counts = Counter(s for s, _ in items)
        keep = {s for s, n in sense_counts.items() if n >= MIN_SENSE}
        dropped = {s: n for s, n in sense_counts.items() if n < MIN_SENSE}
        items = [(s, f) for s, f in items if s in keep]
        if len(keep) < 3:
            refusals.append(f"{word}: only {len(keep)} senses with >= {MIN_SENSE} tokens -> skipped")
            continue
        # deterministic split by position
        n = len(items)
        split = ["train" if (idx * 997) % 1000 < TRAIN_FRAC * 1000 else "eval"
                 for idx in range(n)]
        # fit bucket vocab per feature type on TRAIN split only
        vocab = {}
        for ft in FEATURE_TYPES:
            c = Counter(items[idx][1][ft] for idx in range(n) if split[idx] == "train")
            top = [v for v, _ in c.most_common(K_BUCKET - 1)]
            vocab[ft] = set(top)
        # emit
        for idx, (sense, feats) in enumerate(items):
            bucketed = {ft: (feats[ft] if feats[ft] in vocab[ft] else "OTHER")
                        for ft in FEATURE_TYPES}
            all_lines.append(dict(word=word, sense=sense, split=split[idx],
                                  features=bucketed))
        summary[word] = dict(n_tokens=len(items), n_senses=len(keep),
                             senses=dict(Counter(s for s, _ in items)),
                             dropped_rare=dropped)
        print(f"  {word}: {len(items)} tokens, {len(keep)} senses "
              f"(dropped {len(dropped)} rare)")

    with open(out_path, "w") as f:
        for line in all_lines:
            f.write(json.dumps(line) + "\n")
    with open("data/corpus_summary.json", "w") as f:
        json.dump(dict(summary=summary, refusals=refusals,
                       feature_types=FEATURE_TYPES, k_bucket=K_BUCKET), f, indent=2)
    print(f"\nwrote {len(all_lines)} tokens to {out_path}")
    if refusals:
        print("refusals:", *refusals, sep="\n  ")


if __name__ == "__main__":
    main()
