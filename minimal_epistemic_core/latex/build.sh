#!/bin/sh
# Build epistemic_core.pdf: lualatex, biber, lualatex x2.  Run from this directory.
export PATH="$PATH:/c/Users/Datision/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
mkdir -p build
run() {
  lualatex -interaction=nonstopmode -halt-on-error -output-directory=build epistemic_core.tex > build/pass$1.log 2>&1 \
    || { echo "pass $1 failed"; grep -n -A6 '^!' build/epistemic_core.log | head -30; exit 1; }
}
run 1
biber build/epistemic_core > build/biber.log 2>&1 || { echo "biber failed"; grep -i error build/biber.log; exit 1; }
grep -i warn build/biber.log
run 2
run 3
cp build/epistemic_core.pdf .
grep -c 'Overfull' build/epistemic_core.log | sed 's/^/overfull boxes: /'
grep -E 'undefined|Missing character' build/epistemic_core.log | head
tail -3 build/pass3.log | head -1
