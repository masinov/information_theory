#!/bin/sh
# Full rebuild: convert Markdown -> TeX, then lualatex + biber + lualatex x2.  Run from latex/.
export PATH="$PATH:/c/Users/Datision/AppData/Local/Pandoc:/c/Users/Datision/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
python tools/md2tex.py > build/convert.log 2>&1
grep -E "rc=|EDIT not|Traceback|Error" build/convert.log
lualatex -jobname=ri -interaction=nonstopmode -halt-on-error main.tex > build/pass1.log 2>&1 || { echo "pass1 failed"; grep -n -A6 '^!' build/pass1.log | head -40; exit 1; }
biber ri > build/biber.log 2>&1
lualatex -jobname=ri -interaction=nonstopmode main.tex > build/pass2.log 2>&1
lualatex -jobname=ri -interaction=nonstopmode main.tex > build/pass3.log 2>&1
grep -c 'Overfull' ri.log | sed 's/^/overfull boxes: /'
grep -n 'undefined' ri.log | head
tail -2 build/pass3.log | head -1
