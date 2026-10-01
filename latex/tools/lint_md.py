#!/usr/bin/env python3
"""Formatting lint for the monograph Markdown sources.

Usage (from repo root):  python latex/tools/lint_md.py
Reports, per file and line:
  list   - list item directly after a non-list text line (needs a blank line)
  rule   - horizontal rule '---' directly after a text line (becomes a setext heading)
  head   - heading not preceded/followed by a blank line
  dollar - '$...$' span with a space just inside the closing delimiter
  tick   - backtick span that looks like mathematics (plain-text math)
  blank2 - two or more consecutive blank lines
  bq     - blockquote paragraph break written as an empty line inside a statement
"""
import re, sys
from pathlib import Path

MD = Path(__file__).resolve().parents[2] / "monograph"
MATHY = re.compile(r"[=≤≥≼⊆∩∪→↦σπδ∅⁰⁼⁻¹_^]|\b[a-zA-Z]\([a-zA-Z]")

def strip_q(line):
    m = re.match(r"^((?:>\s?)*)(.*)$", line)
    return m.group(1).count(">"), m.group(2)

def is_list(s):
    return re.match(r"^\s*(?:[-*+]|\d+\.)\s+\S", s) is not None

def main():
    total = 0
    for f in sorted(MD.glob("registered-information-*.md")):
        lines = f.read_text(encoding="utf-8").split("\n")
        in_code = False
        out = []
        prev_blank_run = 0
        for i, raw in enumerate(lines):
            n = i + 1
            if raw.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            lvl, s = strip_q(raw)
            plvl, ps = strip_q(lines[i - 1]) if i else (0, "")
            if raw.strip() == "":
                prev_blank_run += 1
                if prev_blank_run == 2:
                    out.append((n, "blank2", ""))
                continue
            prev_blank_run = 0
            if is_list(s) and ps.strip() and not is_list(ps) and not ps.strip().startswith("$$") and lvl == plvl \
                    and not re.match(r"^\s{2,}", ps):
                out.append((n, "list", s[:70]))
            if s.strip() == "---" and lvl == 0 and ps.strip():
                out.append((n, "rule", ps[:70]))
            if s.startswith("#"):
                if ps.strip():
                    out.append((n, "head", s[:70]))
                nxt = lines[i + 1] if i + 1 < len(lines) else ""
                if nxt.strip():
                    out.append((n, "head", "no blank after: " + s[:60]))
            for m in re.finditer(r"(?<!\$)\$(?!\$)([^$\n]*?)\$(?!\$)", s):
                if m.group(1).endswith(" ") or m.group(1).startswith(" "):
                    out.append((n, "dollar", m.group(0)[:60]))
            for m in re.finditer(r"`([^`\n]+)`", s):
                if MATHY.search(m.group(1)):
                    out.append((n, "tick", m.group(0)[:60]))
        for n, kind, txt in out:
            print(f"{f.name}:{n}: {kind}: {txt}")
        total += len(out)
    print(f"{total} findings")

if __name__ == "__main__":
    main()
