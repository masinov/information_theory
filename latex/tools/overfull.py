#!/usr/bin/env python3
"""List the worst overfull boxes in ri.log with file and source line (run from latex/)."""
import re, sys
thr = float(sys.argv[1]) if len(sys.argv) > 1 else 12
L = open("ri.log", encoding="utf-8", errors="replace").read().split("\n")
cur = "?"
for i, l in enumerate(L):
    for m in re.finditer(r"\(\./((?:parts|appendices|manual|frontmatter)/[\w\-]+\.tex)", l):
        cur = m.group(1)
    m = re.match(r"Overfull .hbox \(([\d.]+)pt too wide\) (.*)", l)
    if m and float(m.group(1)) > thr:
        where = re.search(r"lines? (\d+)", m.group(2))
        print(m.group(1), cur, where.group(1) if where else "?", "|", m.group(2)[:30])
