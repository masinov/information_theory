#!/usr/bin/env python3
"""Convert the Markdown monograph to LaTeX part files + refs.bib.

Usage:  python tools/md2tex.py            (run from latex/)
Outputs: parts/*.tex, appendices/*.tex, refs.bib, build/labels.lua, build/report.txt
"""
import re, subprocess, sys, unicodedata, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # latex/
MD = ROOT.parent / "monograph"
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)

PARTS = [  # (md file stem, output path)
    ("kernel", "parts/I.tex"), ("part-II", "parts/II.tex"), ("part-III", "parts/III.tex"),
    ("part-IV", "parts/IV.tex"), ("part-V", "parts/V.tex"), ("part-VI", "parts/VI.tex"),
    ("part-VII", "parts/VII.tex"), ("part-VIII", "parts/VIII.tex"), ("part-IX", "parts/IX.tex"),
    ("part-X", "parts/X.tex"), ("part-XI", "parts/XI.tex"),
    ("appendix-A", "appendices/A.tex"), ("appendix-B", "appendices/B.tex"),
    ("appendix-C", "appendices/C.tex"), ("appendix-D", "appendices/D.tex"),
]

report = []

# ---------------------------------------------------------------- bibliography
def split_names(s):
    s = re.sub(r"\s*\((eds?|trans)\.\)", "", s)
    parts = re.split(r"(?<=\.),\s*(?:and\s+)?|,?\s+and\s+(?=[A-Z])", s.strip().rstrip(","))
    return [p.strip() for p in parts if p.strip()]

def ascii_key(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())

def parse_entry(line):
    line = line.lstrip("- ").strip()
    m = re.match(r"(.+?)\s+\((\d{4}[a-z]?)\)\.\s*(.*)$", line)
    if not m:
        return None
    authors, year, rest = m.groups()
    names = split_names(authors)
    entry = {"author": " and ".join(names), "year": year, "first": names[0].split(",")[0].strip(), "raw": rest}
    mq = re.match(r"[\"“](.+?)[,.]?[\"”]\s*(.*)$", rest)
    mi = re.match(r"\*(.+?)\*\.?\s*(.*)$", rest)
    if mq:
        title, tail = mq.group(1), mq.group(2)
        entry["title"] = title
        mc = re.match(r"In\s+(.*?)\s*(?:\(eds?\.\)|,\s*(?:ed|eds)\.)?,?\s*\*(.+?)\*,?\s*(.*)$", tail)
        mj = re.match(r"\*(.+?)\*\s*(.*)$", tail)
        if tail.startswith("In ") and re.search(r"\*", tail):
            entry["type"] = "incollection"
            mm = re.match(r"In\s+(.*?)\*(.+?)\*,?\s*(.*)$", tail)
            if mm:
                ed, bt, more = mm.groups()
                entry["booktitle"] = bt
                if ed.strip():
                    entry["editor_note"] = ed.strip().rstrip(",")
                entry["note"] = more.strip().rstrip(".")
            else:
                entry["note"] = tail
        elif mj:
            entry["type"] = "article"
            entry["journaltitle"] = mj.group(1)
            more = mj.group(2).rstrip(".")
            mv = re.match(r"(\d+)(?:\((\d+)\))?,?\s*(.*)$", more)
            if mv:
                entry["volume"] = mv.group(1)
                if mv.group(2):
                    entry["number"] = mv.group(2)
                more = mv.group(3)
            if re.fullmatch(r"[\d–\-, and]+", more or ""):
                entry["pages"] = more.replace("–", "--")
            elif more:
                entry["note"] = more
        else:
            entry["type"] = "misc"
            entry["note"] = tail.rstrip(".")
    elif mi:
        entry["type"] = "book"
        entry["title"] = mi.group(1).rstrip(".")
        tail = mi.group(2).rstrip(".")
        entry["publisher"] = tail
    else:
        entry["type"] = "misc"
        entry["title"] = rest.rstrip(".")
    return entry

def bib_escape(s):
    return s.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")

def bib_text(entries):
    out = []
    for e in entries:
        f = {"author": e["author"], "year": e["year"][:4]}
        for k in ("title", "journaltitle", "booktitle", "volume", "number", "pages", "publisher", "note"):
            if k in e:
                f[k] = e[k]
        if "editor_note" in e:
            f["note"] = (f.get("note", "") + " " + e["editor_note"]).strip()
        if e["type"] == "misc" and "title" not in f:
            f["title"] = e["raw"]
        if e["type"] == "book" and "publisher" in f:
            m = re.match(r"(.*?)(?:,\s*(\d+)(?:st|nd|rd|th) ed\.?)?$", f["publisher"])
            f["publisher"] = f["publisher"]
        body = ",\n".join(f"  {k} = {{{bib_escape(v) if k != 'title' else '{' + bib_escape(v) + '}'}}}" for k, v in f.items())
        out.append(f"@{e['type']}{{{e['key']},\n{body}\n}}\n")
    return "\n".join(out)

def collect_bibliography():
    lines = []
    kernel = (MD / "registered-information-kernel.md").read_text(encoding="utf-8")
    sec = kernel.split("\n## References", 1)[1]
    lines += [l for l in sec.splitlines() if l.startswith("- ")]
    for stem, _ in PARTS:
        txt = (MD / f"registered-information-{stem}.md").read_text(encoding="utf-8")
        for m in re.finditer(r"\*\*References added in Part [IVX]+[^\n]*\n\n((?:- .*\n?)+)", txt):
            lines += [l for l in m.group(1).splitlines() if l.startswith("- ")]
    entries, seen = [], {}
    for l in lines:
        e = parse_entry(l)
        if not e:
            report.append("BIB unparsed: " + l[:120]); continue
        base = ascii_key(e["first"]) + e["year"]
        n = seen.get(base, 0)
        seen[base] = n + 1
        e["key"] = base + ("" if n == 0 else chr(ord("a") + n))
        e["id"] = (ascii_key(e["first"]), e["year"])
        entries.append(e)
    return entries

# ------------------------------------------------------------------ citations
def build_cite_index(entries):
    idx = {}
    for e in entries:
        sur = [ascii_key(n.split(",")[0]) for n in e["author"].split(" and ")]
        idx.setdefault(e["id"], []).append((e["key"], sur))
    return idx

def pick(cands, names):
    """Choose among entries sharing first author and year, by co-author surnames mentioned."""
    if len(cands) == 1:
        return cands[0][0]
    words = [ascii_key(w) for w in re.findall(r"[A-Z][\w'\-]+", names)]
    n_auth = len([w for w in re.split(r",|&|and|–", names) if w.strip()])
    def score(c):
        sur = c[1]
        return (sum(1 for w in words if w in sur) - abs(len(sur) - n_auth), -len(sur))
    return max(cands, key=score)[0]

SEG = re.compile(r"^(?P<names>[^\d]+?)\s+(?P<years>\d{4}[a-z]?(?:\s*(?:,|;|and)\s*\d{4}[a-z]?)*)\s*(?P<loc>.*)$")

def first_surname(names):
    names = names.strip().lstrip("(").strip()
    m = re.match(r"((?:(?:van|von|de|der|Le|le|di|del)\s+)*[A-ZÀ-ÿ][\w'’\-\.ÀÿĀ-ž]*)", names)
    return ascii_key(m.group(1)) if m else ""

def convert_citations(text, idx, unresolved):
    def conv_group(inner):
        segs = [s.strip() for s in inner.split(";")]
        keys = []
        for s in segs:
            s = s.rstrip(".")
            m = SEG.match(s)
            if not m:
                return None
            sur = first_surname(m.group("names"))
            for y in re.findall(r"\d{4}[a-z]?", m.group("years")):
                ks = idx.get((sur, y))
                if not ks:
                    return None
                keys.append(pick(ks, m.group("names")))
        return keys
    out, pos = [], 0
    for m in re.finditer(r"(?<!\])\[([^\[\]\n$]*?\d{4}[^\[\]\n$]*?)\](?!\()", text):
        keys = conv_group(m.group(1))
        out.append(text[pos:m.start()])
        if keys:
            before = text[max(0, m.start() - 4):m.start()]
            after = text[m.end():m.end() + 3]
            narrative = (re.search(r"(?:^|\n|\*\* |\. |: )$", before) is not None) and re.match(r"\s[a-z]", after) is not None
            if narrative:
                out.append("`" + chr(92) + "textcite{" + ",".join(keys) + "}`{=latex}")
            else:
                out.append("[" + "; ".join("@" + k for k in keys) + "]")
        else:
            out.append(m.group(0)); unresolved.append(m.group(1))
        pos = m.end()
    out.append(text[pos:])
    return "".join(out)

# --------------------------------------------------------------- pre-processing
BANNER = re.compile(r"^> \*\*Integrated edition.*$", re.M)

# Build-time text edits, per source file: (old, new) pairs. Prefer fixing the Markdown itself;
# this hook exists for edition-only changes. Every pair must match or the report flags it.
EDITS = {}
CHAR_FIXES = {"▸": "$\\triangleright$", "∎": "$\\square$", "\U0001d70e": "$\\sigma$"}

def preprocess(stem, text, idx, unresolved):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"^# Registered Information over Contrast Domains\s*\n", "", text)
    text = BANNER.sub("", text)
    text = re.sub(r"^---\s*$", "", text, flags=re.M)
    if stem == "kernel":
        text = text.split("\n## References", 1)[0]
    # "References added in Part X" blocks (heading line + bullets + trailing remarks) are bibliography only
    text = re.sub(r"^\*\*References added in Part [IVX]+[^\n]*\n(?:\n(?:- .*\n?)+(?:\n(?:All other|Every|The one)[^\n]*\n?)?)?", "", text, flags=re.M)
    # drop external review-document links (keep link text)
    text = re.sub(r"\[([^\]]+)\]\((?:\.\./|registered-information-)[^)]*\)", r"\1", text)
    for old, new in EDITS.get(stem, []):
        if old not in text:
            report.append(f"EDIT not applied in {stem}: {old[:60]}")
        text = text.replace(old, new)
    for old, new in CHAR_FIXES.items():
        text = text.replace(old, new)
    # typography: spaced em dashes -> closed em dashes with a break opportunity after
    text = re.sub(r"[ \t]+" + chr(0x2014) + r"[ \t]+", chr(0x2014) + chr(0x200b), text)
    text = convert_citations(text, idx, unresolved)
    return text

def labels_from(text):
    labs = set()
    for m in re.finditer(r"^(?:> )?\*\*(?:Definition|Theorem|Proposition|Lemma|Corollary|Fact|Remark|Conjecture|Assumption|Example|Problem)s?\s+([A-D]?\.?[\d.]*\d[a-z]?′?)", text, re.M):
        labs.add(m.group(1))
    for m in re.finditer(r"^(?:> )?\*\*Worked example ([A-Z])\b", text, re.M):
        labs.add("ex" + m.group(1))
    secs = set()
    for m in re.finditer(r"^#{2,3} ([A-D]\.)?(\d+(?:\.\d+)?)\.?\s", text, re.M):
        secs.add((m.group(1) or "") + m.group(2))
    return labs, secs

def main():
    entries = collect_bibliography()
    idx = build_cite_index(entries)
    if "--bib" in sys.argv or not (ROOT / "refs.bib").exists():
        (ROOT / "refs.bib").write_text(bib_text(entries), encoding="utf-8")
    else:
        (BUILD / "refs.auto.bib").write_text(bib_text(entries), encoding="utf-8")
    report.append(f"bib entries: {len(entries)}")

    unresolved, texts = [], {}
    all_labels, all_secs = set(), set()
    for stem, out in PARTS:
        raw = (MD / f"registered-information-{stem}.md").read_text(encoding="utf-8")
        t = preprocess(stem, raw, idx, unresolved)
        texts[stem] = t
        l, s = labels_from(t)
        all_labels |= l; all_secs |= s
    lua = "return { stmts = {" + ",".join(f'["{x}"]=true' for x in sorted(all_labels)) + "}, secs = {" + \
          ",".join(f'["{x}"]=true' for x in sorted(all_secs)) + "} }\n"
    (BUILD / "labels.lua").write_text(lua, encoding="utf-8")

    for stem, out in PARTS:
        src = BUILD / f"{stem}.md"
        src.write_text(texts[stem], encoding="utf-8")
        cmd = ["pandoc", str(src), "-f", "markdown+tex_math_dollars+raw_tex+smart+lists_without_preceding_blankline", "-t", "latex", "--biblatex",
               "--syntax-highlighting=none", "--wrap=preserve",
               "--lua-filter", str(ROOT / "tools/stmt.lua"), "--lua-filter", str(ROOT / "tools/mathfix.lua"), "--lua-filter", str(ROOT / "tools/xref.lua"),
               "-o", str(ROOT / out)]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, encoding="utf-8")
        tex = (ROOT / out).read_text(encoding="utf-8")
        tex = tex.replace(chr(10) * 2 + chr(92) + "end{proof}", chr(10) + chr(92) + "end{proof}")
        for env in ("thmplain", "thmdef", "thmrem"):
            tex = tex.replace(chr(10) * 2 + chr(92) + "end{" + env + "}", chr(10) + chr(92) + "end{" + env + "}")
        (ROOT / out).write_text(tex, encoding="utf-8")
        if r.returncode or r.stderr.strip():
            report.append(f"pandoc[{stem}] rc={r.returncode}: {r.stderr.strip()[:500]}")
    report.append(f"unresolved citation groups ({len(unresolved)}):")
    report.extend(["   [" + u + "]" for u in unresolved])
    (BUILD / "report.txt").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))

if __name__ == "__main__":
    main()
