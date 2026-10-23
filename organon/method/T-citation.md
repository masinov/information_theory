---
id: method/T-citation
since: 2026-10-23
type: method
role: protocol
title: Citation check
status: in-force
order: 72
---
No citation in a text sent to others rests on memory.

## Procedure
Run tools/check.py, which reports cited keys whose entry in library/refs.bib is at level memory or unknown. Check each against a catalogue or publisher record (level record), and quoted or page-specific claims against the text itself (level text).

## Record
The verified and verifiednote fields of the bibliography entry.
