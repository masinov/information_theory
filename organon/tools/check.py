"""Check the organon graph and bibliography. Exit status 1 if there are errors.

    python tools/check.py            errors and warnings
    python tools/check.py --quiet    errors only
"""
import os
import re
import sys
from lib import (load, load_bib, resolve, expected_id, opener, effective_method, TYPES, LINKS, REQUIRED,
                 BASIS, VERIFIED, PEOPLE, OPENERS, FRICTION_KINDS, RESOLUTIONS, EFFECTS, ORGANON, REPO)

errors, warnings = [], []


def err(e, msg):
    errors.append(f'{os.path.relpath(e.path, ORGANON)}: {msg}')


def warn(where, msg):
    warnings.append(f'{where}: {msg}')


def main():
    entries = load()
    bib = load_bib()
    ids = {}
    for e in entries:
        if not e.id:
            err(e, 'no id')
            continue
        if e.id in ids:
            err(e, f'duplicate id {e.id} (also {os.path.relpath(ids[e.id].path, ORGANON)})')
        ids[e.id] = e
        if expected_id(e.path) != e.id:
            err(e, f'id {e.id} does not match its path (expected {expected_id(e.path)})')

    # File names that differ only in case overwrite each other on case-insensitive file systems.
    seen_paths = {}
    for d in ('graph', 'method', 'library/sources', 'views', 'journal'):
        for root, _, files in os.walk(os.path.join(ORGANON, d)):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), ORGANON).replace(os.sep, '/')
                if rel.lower() in seen_paths:
                    errors.append(f'{rel}: differs only in case from {seen_paths[rel.lower()]}')
                seen_paths[rel.lower()] = rel
    lower_ids = {}
    for i in ids:
        if i.lower() in lower_ids and lower_ids[i.lower()] != i:
            errors.append(f'ids {i} and {lower_ids[i.lower()]} differ only in case')
        lower_ids[i.lower()] = i

    for e in entries:
        t, s = e.get('type'), e.get('status')
        if t not in TYPES:
            err(e, f'unknown type "{t}"')
            continue
        if s not in TYPES[t]:
            err(e, f'status "{s}" not allowed for {t} (allowed: {", ".join(TYPES[t])})')
        if not e.get('title'):
            err(e, 'no title')
        for status, fields in REQUIRED.get(t, {}).items():
            if status in ('*', s):
                for f in fields:
                    if not e.get(f):
                        err(e, f'{t} with status {s} needs field "{f}"')
        if e.get('basis') and e.get('basis') not in BASIS:
            err(e, f'basis must be one of {", ".join(BASIS)}')
        if e.get('by') and e.get('by') not in PEOPLE:
            err(e, f'by must be one of {", ".join(PEOPLE)}')
        if e.get('verified') and e.get('verified') not in VERIFIED:
            err(e, f'verified must be one of {", ".join(VERIFIED)}')
        for field in LINKS:
            for ref in e.list(field):
                if not resolve(ref, e.ns, ids):
                    err(e, f'{field}: no entry "{ref}"')
        for ref in re.findall(r'\[\[([^\]]+)\]\]', e.body):
            if not resolve(ref, e.ns, ids):
                err(e, f'body link [[{ref}]]: no entry')
        for key in e.list('cites'):
            if key not in bib:
                err(e, f'cites "{key}", which is not in library/refs.bib')
            elif bib[key]['verified'] in ('memory', 'unknown') and s not in ('withdrawn', 'retired'):
                warn(os.path.relpath(e.path, ORGANON), f'cites {key}, verified only at level {bib[key]["verified"]}')

        if t == 'friction':
            if e.get('kind') not in FRICTION_KINDS:
                err(e, f'kind must be one of {", ".join(FRICTION_KINDS)}')
            if e.get('effect') and e.get('effect') not in EFFECTS:
                err(e, f'effect must be one of {", ".join(EFFECTS)}')
            if e.get('resolution') and e.get('resolution') not in RESOLUTIONS:
                err(e, f'resolution must be one of {", ".join(RESOLUTIONS)}')
            if e.get('resolution') == 'sublate':
                for ref in e.list('resolved_by'):
                    r = ids.get(resolve(ref, e.ns, ids))
                    if r is not None and not r.list('sublates'):
                        err(e, f'resolved by sublation, but {r.id} has no sublates link')
        if e.list('sublates'):
            for sec in ('Kept', 'Dropped', 'Raised'):
                if not e.section(sec):
                    err(e, f'sublates entries, so it needs a "## {sec}" section')
        if e.list('translates') and not e.section('Lost'):
            warn(os.path.relpath(e.path, ORGANON), 'translates an entry but has no "## Lost" section')
        if t == 'investigation' and s == 'finished' and not e.section('Result'):
            err(e, 'a finished investigation needs a "## Result" section')

    # Namespaces: each one in graph/ is opened by an investigation or a frame.
    for ns in sorted({e.ns for e in entries if os.path.relpath(e.path, ORGANON).startswith('graph')}):
        op = opener(ns, ids)
        if op is None:
            errors.append(f'graph/{ns}: no _investigation.md or _frame.md opens this namespace')
            continue
        if op.get('type') != OPENERS[op.id.split('/', 1)[1]]:
            err(op, f'must have type {OPENERS[op.id.split("/", 1)[1]]}')
        if op.get('type') == 'frame':
            inv = ids.get(resolve(op.get('investigation'), ns, ids))
            if inv is None or inv.get('type') != 'investigation':
                err(op, 'investigation: must name an investigation entry')
            for field in ('accepts', 'rejects', 'reinterprets'):
                for ref in op.list(field):
                    if resolve(ref, ns, ids) and resolve(ref, ns, ids).split('/')[0] == ns:
                        err(op, f'{field}: {ref} is in the frame itself; imports name entries of other namespaces')
            base = inv.ns if inv is not None else None
            stated = {resolve(r, ns, ids) for f in ('accepts', 'rejects', 'reinterprets', 'divided') for r in op.list(f)}
            for b in entries:
                if (b.ns == base and b.get('type') in ('claim', 'concept', 'decision', 'position')
                        and b.get('status') != 'withdrawn' and b.id not in stated):
                    warn(f'graph/{ns}', f'does not say whether it accepts, rejects or reinterprets {b.id}')
            for ref in op.list('divided'):
                target = resolve(ref, ns, ids)
                if target and not any(target in {resolve(x, o.ns, ids) for x in o.list('accepts') + o.list('rejects')}
                                      for o in entries if o.ns == ns and o is not op):
                    warn(f'graph/{ns}', f'divided on {ref}, but no branch of the frame accepts or rejects it')
            for ref in op.list('reinterprets'):
                target = resolve(ref, ns, ids)
                if target and not any(target in {resolve(x, o.ns, ids) for x in o.list('translates') + o.list('corresponds')}
                                      for o in entries if o.ns == ns):
                    warn(f'graph/{ns}', f'reinterprets {ref}, but no entry of the frame translates or corresponds to it')
        # Method links must point to method entries in force in this namespace, and a method entry in
        # force must not require one that this namespace has overridden.
        in_force = {m.id for m in effective_method(ns, entries)}
        for mid in sorted(in_force):
            for ref in ids[mid].list('requires'):
                target = resolve(ref, ids[mid].ns, ids)
                if target and ids[target].get('type') == 'method' and target not in in_force:
                    warn(f'graph/{ns}', f'{mid} requires {target}, which is not in force here: override or replace {mid}')
        for e in (x for x in entries if x.ns == ns and x is not op):
            for field in LINKS:
                for ref in e.list(field):
                    target = resolve(ref, ns, ids)
                    if target and ids[target].get('type') == 'method' and target not in in_force:
                        err(e, f'{field}: {ref} is not in force in {ns} (overridden or retired)')

    # Cycles among requires links (reported, not errors: see meta/Q-shape).
    graph = {e.id: [resolve(r, e.ns, ids) for r in e.list('requires')] for e in entries}
    state, stack = {}, []

    def visit(n):
        state[n] = 1
        stack.append(n)
        for m in graph.get(n, []):
            if m is None:
                continue
            if state.get(m) == 1:
                warn('requires', 'cycle: ' + ' -> '.join(stack[stack.index(m):] + [m]))
            elif m not in state:
                visit(m)
        stack.pop()
        state[n] = 2

    for n in graph:
        if n not in state:
            visit(n)

    # Bibliography: every entry carries a verification level.
    for key, b in bib.items():
        if b['verified'] not in VERIFIED:
            errors.append(f'library/refs.bib: {key} has no valid verified field')

    # Papers: every key cited in a .tex file outside organon should be in the central bibliography,
    # and should not rest on memory.
    cite = re.compile(r'\\(?:auto|text|paren|foot|full)?cite[a-z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}')
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in ('build', 'venv', 'nltk_data', '.git', 'organon')]
        for f in files:
            if not f.endswith('.tex'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, REPO).replace(os.sep, '/')
            for m in cite.finditer(open(path, encoding='utf-8', errors='replace').read()):
                for key in (k.strip() for k in m.group(1).split(',')):
                    if not key:
                        continue
                    if key not in bib:
                        warn(rel, f'cites {key}, not in the central bibliography')
                    elif bib[key]['verified'] == 'memory':
                        warn(rel, f'cites {key}, verified only from memory')

    quiet = '--quiet' in sys.argv
    for line in errors:
        print('ERROR  ', line)
    if not quiet:
        seen = set()
        for line in warnings:
            if line not in seen:
                seen.add(line)
                print('warning', line)
    print(f'{len(entries)} entries, {len(bib)} references: {len(errors)} errors, {len(set(warnings))} warnings')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
