#!/usr/bin/env python3
"""Normalize the layout of the monograph Markdown sources (idempotent).

Usage (from repo root):  python latex/tools/normalize_md.py [--check]

Rules:
  * numbered statements written as plain bold paragraphs (Fact, Definition, Lemma, Proposition,
    Theorem, Corollary) become blockquoted statements, like all other statements; a list that
    directly continues a definition is included;
  * a list item that follows a non-list line at the same quote level gets a blank line before it
    (inside a blockquote the blank line is written as '>');
  * headings and horizontal rules are surrounded by blank lines;
  * runs of blank lines collapse to one; trailing whitespace is removed; files end with one newline.
Code fences are left untouched.
"""
import re, sys
from pathlib import Path

MD = Path(__file__).resolve().parents[2] / "monograph"
STMT = re.compile(r"^\*\*(?:Fact|Definition|Lemma|Proposition|Theorem|Corollary)\s+[A-Z]?\.?\d")
LIST = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\S")


def split_q(line):
    m = re.match(r"^((?:>[ ]?)*)(.*)$", line)
    return m.group(1).count(">"), m.group(2)


def quote_plain_statements(lines):
    out, i = [], 0
    while i < len(lines):
        if STMT.match(lines[i]):
            block = []
            while i < len(lines) and lines[i].strip():
                block.append(lines[i]); i += 1
            # include directly following list blocks (definition bodies)
            while i + 1 < len(lines) and not lines[i].strip() and LIST.match(lines[i + 1]):
                block.append("")
                i += 1
                while i < len(lines) and lines[i].strip():
                    block.append(lines[i]); i += 1
            out.extend("> " + l if l.strip() else ">" for l in block)
        else:
            out.append(lines[i]); i += 1
    return out


def normalize(text):
    lines = [l.rstrip() for l in text.replace("\r\n", "\n").split("\n")]
    lines = quote_plain_statements(lines)
    out, in_code = [], False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line); continue
        if in_code:
            out.append(line); continue
        lvl, s = split_q(line)
        prev = out[-1] if out else ""
        plvl, ps = split_q(prev)
        blank = (">" * lvl) if lvl else ""
        is_heading = s.startswith("#") and lvl == 0
        is_rule = s.strip() == "---" and lvl == 0
        if LIST.match(s) and ps.strip() and not LIST.match(ps) and plvl == lvl and not re.match(r"^\s{2,}", ps):
            out.append(blank)
        if (is_heading or is_rule) and prev.strip():
            out.append("")
        if out and split_q(out[-1])[0] == 0 and (out[-1].startswith("#") or out[-1].strip() == "---") and line.strip():
            out.append("")
        out.append(line)
    # collapse blank runs (a quoted blank '>' between two non-quoted lines is dropped)
    res = []
    for line in out:
        if not line.strip() and res and not res[-1].strip():
            continue
        res.append(line)
    while res and not res[0].strip():
        res.pop(0)
    while res and not res[-1].strip():
        res.pop()
    return "\n".join(res) + "\n"


def main():
    check = "--check" in sys.argv
    changed = 0
    for f in sorted(MD.glob("registered-information-*.md")):
        old = f.read_text(encoding="utf-8")
        new = normalize(old)
        if new != old:
            changed += 1
            if not check:
                f.write_text(new, encoding="utf-8")
            print(("would change " if check else "normalized ") + f.name)
    print(f"{changed} file(s) {'need changes' if check else 'changed'}")


if __name__ == "__main__":
    main()
