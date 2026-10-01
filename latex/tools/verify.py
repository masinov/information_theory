#!/usr/bin/env python3
"""Fidelity check: every prose paragraph of the Markdown sources should appear in the PDF text.

Usage (from latex/):  python tools/verify.py [threshold]
Words are compared as 3-grams of alphabetic tokens (math removed on the Markdown side).
Reports paragraphs whose 3-grams are missing from the PDF more than `threshold` (default 0.25).
"""
import re, subprocess, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT.parent / "monograph"
thr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25

subprocess.run(["pdftotext", "-enc", "UTF-8", str(ROOT / "ri.pdf"), str(ROOT / "build/plain.txt")], check=True)
pdf = (ROOT / "build/plain.txt").read_text(encoding="utf-8", errors="replace")
pdf = re.sub(r"-\s*\n\s*", "", pdf)          # hyphenation at line ends
pdf = pdf.replace("­", "")

def tokens(s):
    return [w.lower() for w in re.findall(r"[A-Za-zÀ-ɏ]{3,}", s)]

pdf_tok = tokens(pdf)
pdf_grams = set(zip(pdf_tok, pdf_tok[1:], pdf_tok[2:]))

def clean_md(p):
    p = re.sub(r"\$\$.*?\$\$", " ", p, flags=re.S)
    p = re.sub(r"\$[^$]*\$", " ", p)
    p = re.sub(r"`[^`]*`", " ", p)
    p = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", p)
    p = re.sub(r"\[@[^\]]*\]", " ", p)
    p = re.sub(r"[*_>|#\\]", " ", p)
    return p

skip_stems = ("appendix-A", "appendix-D")   # hand-typeset sections are checked by eye
total = bad = 0
for f in sorted(glob.glob(str(MD / "registered-information-*.md"))):
    stem = Path(f).stem.replace("registered-information-", "")
    text = Path(f).read_text(encoding="utf-8")
    if stem == "kernel":
        text = text.split("\n## References", 1)[0]
    paras = re.split(r"\n\s*\n", text)
    for p in paras:
        if p.lstrip().startswith(("```", "|---", "| ")) or "Integrated edition" in p or "References added" in p:
            continue
        toks = tokens(clean_md(p))
        grams = list(zip(toks, toks[1:], toks[2:]))
        if len(grams) < 6:
            continue
        miss = [g for g in grams if g not in pdf_grams]
        total += 1
        if len(miss) / len(grams) > thr:
            bad += 1
            print(f"[{stem}] {len(miss)}/{len(grams)} missing: " + re.sub(r"\s+", " ", p.strip())[:110])
print(f"checked {total} paragraphs; {bad} above threshold {thr}")
