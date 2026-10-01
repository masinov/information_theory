import re, glob
def est(m):
    m = re.sub(r"\\(?:text|mathrm|operatorname)\{([^}]*)\}", r"\1", m)
    m = re.sub(r"\\(?:big|Big|bigg|Bigg|left|right)[lr]?|\\[;:,!> ]|\\q?quad|\\[a-zA-Z]+|[{}\\_^&]", lambda x: "X" if x.group(0).startswith("\\") and len(x.group(0)) > 2 and x.group(0) not in ("\\quad", "\\qquad") else "", m)
    return len(re.sub(r"\s+", "", m))
rows = []
for f in sorted(glob.glob("parts/*.tex")):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r"\\\[(.*?)\\\]", t, re.S):
        line = t[:m.end()].count("\n") + 1
        rows.append((est(m.group(1)), f, line, "\\qquad" in m.group(1)))
rows.sort(reverse=True)
for r in rows[:30]:
    print(r)
