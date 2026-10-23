---
id: method/T-circularity
since: 2026-10-23
type: method
role: protocol
title: Circularity check
status: in-force
order: 70
---
Find cycles among requires links.

## Procedure
Run tools/check.py, which reports cycles. For each cycle, judge whether it is vicious or a mutual support (see meta/Q-shape).

## Record
A test entry for each cycle judged.
