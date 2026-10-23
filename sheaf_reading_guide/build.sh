#!/bin/sh
# Build sheaves_guide.pdf: lualatex, biber, lualatex x2.  Run from this directory.
export PATH="$PATH:/c/Users/Datision/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
mkdir -p build
run() {
  lualatex -interaction=nonstopmode -halt-on-error -output-directory=build sheaves_guide.tex > build/pass$1.log 2>&1 \
    || { echo "pass $1 failed"; grep -n -A6 '^!' build/sheaves_guide.log | head -30; exit 1; }
}
run 1
biber build/sheaves_guide > build/biber.log 2>&1 || { echo "biber failed"; grep -i error build/biber.log; exit 1; }
grep -i warn build/biber.log
run 2
run 3
cp build/sheaves_guide.pdf .
grep -c 'Overfull' build/sheaves_guide.log | sed 's/^/overfull boxes: /'
grep -E 'undefined|Missing character' build/sheaves_guide.log | head
tail -3 build/pass3.log | head -1
