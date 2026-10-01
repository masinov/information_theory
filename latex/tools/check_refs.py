#!/usr/bin/env python3
"""Report textual references to numbered statements or sections that have no target (run from latex/).

A reference that the xref filter could not link stays as plain text in the generated TeX; this script lists them.
"""
import re, glob
BS = chr(92)
labels = set(re.findall(r'\["([^"]+)"\]=true', open("build/labels.lua", encoding="utf-8").read()))
kinds = r"(?:Definition|Theorem|Proposition|Lemma|Corollary|Fact|Remark|Example)s?"
bad = []
for f in sorted(glob.glob("parts/*.tex") + glob.glob("appendices/*.tex")):
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        plain = re.sub(re.escape(BS) + r"hyperlink\{[^}]*\}\{[^}]*\}", "", line)
        plain = re.sub(re.escape(BS) + r"hypertarget\{[^}]*\}\{[^}]*\}", "", plain)
        for m in re.finditer(kinds + r"[~ ]([A-D]?\.?\d+\.\d+[a-z]?)", plain):
            if m.group(1) not in labels:
                bad.append((f, n, m.group(0)))
        for m in re.finditer(r"§(\d+(?:\.\d+)?)", plain):
            if m.group(1) not in labels:
                bad.append((f, n, m.group(0)))
for b in bad:
    print(*b)
print(len(bad), "unresolved references")
