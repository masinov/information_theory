import re, glob
BS = chr(92)
pat = re.compile(re.escape(BS) + r"(secn|subsecn|appsection|part)\{")
for f in sorted(glob.glob("parts/*.tex") + glob.glob("appendices/*.tex")):
    for i, l in enumerate(open(f, encoding="utf-8"), 1):
        if pat.match(l) and (BS + "(" in l or "$" in l or "sigma" in l):
            print(f, i, l[:150].strip())
