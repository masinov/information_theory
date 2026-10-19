#!/bin/sh
# Build decision_theory.pdf: lualatex, biber, lualatex x2.  Run from this directory.
export PATH="$PATH:/c/Users/Datision/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
mkdir -p build
run() {
  lualatex -interaction=nonstopmode -halt-on-error -output-directory=build decision_theory.tex > build/pass$1.log 2>&1 \
    || { echo "pass $1 failed"; grep -n -A6 '^!' build/decision_theory.log | head -30; exit 1; }
}
run 1
biber build/decision_theory > build/biber.log 2>&1 || { echo "biber failed"; grep -i error build/biber.log; exit 1; }
grep -i warn build/biber.log
run 2
run 3
run 4
cp build/decision_theory.pdf .
grep -c 'Overfull' build/decision_theory.log | sed 's/^/overfull boxes: /'
grep -E 'undefined|Missing character' build/decision_theory.log | head
tail -3 build/pass4.log | head -1
