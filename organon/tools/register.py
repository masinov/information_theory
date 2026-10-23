"""Render views: Markdown templates in views/ whose directives are replaced by tables built from entries.

    python tools/register.py           render every view
    python tools/register.py --check   exit 1 if any rendered view differs from the file on disk

A template begins with a line '<!-- out: path -->' (relative to the repository) and may contain:

  <!-- table filter="k=v k=v" cols="Label:source|Label:source" ns="mec" -->
  <!-- arguments filter="..." ns="mec" -->     "Argument for X (§n): ..." paragraphs
  <!-- deps filter="..." ns="mec" -->          "- X ← a, b" list of requires links
  <!-- compare filter="..." ns="mec" frame="mec.process" -->
                                               each selected entry with the frame's stance on it
  <!-- entry id="ns/local" -->                 the full body of one entry, its sections as ####
  <!-- frames spaces="mec,mec.process" -->     the namespaces side by side: what each holds fixed and
                                               which method entries are in force, local or overridden

A source is a front-matter field, 'statement' (first paragraph of the body), 'titled' ("*Title.* statement"),
'role' (capitalized), or '#Section' (a body section). 'a?b' uses b when a is empty; a trailing '!b' makes
the cell bold. Rows are sorted by the 'order' field.
"""
import os
import re
import sys
from lib import load, short, resolve, opener, effective_method, ORGANON, REPO

DIRECTIVE = re.compile(r'<!--\s*(table|arguments|deps|compare|entry|frames)\s+(.*?)-->')
ATTR = re.compile(r'(\w+)="([^"]*)"')


def select(entries, spec):
    conds = [c.split('=', 1) for c in spec.split()]
    out = [e for e in entries
           if all((e.ns if k == 'ns' else e.get(k)) == v or v in e.list(k) for k, v in conds)]
    return sorted(out, key=lambda e: int(e.get('order', 0) or 0))


def cell(e, source, ns):
    bold = source.endswith('!b')
    source = source[:-2] if bold else source
    value = ''
    for alt in source.split('?'):
        if alt == 'id':
            value = short(e.id, ns)
        elif alt == 'statement':
            value = e.statement()
        elif alt == 'titled':
            value = e.statement() if e.get('untitled') else f'*{e.get("title")}.* {e.statement()}'
        elif alt == 'role':
            value = e.get('role').capitalize()
        elif alt.startswith('#'):
            value = e.section(alt[1:])
        else:
            v = e.fm.get(alt, '')
            value = ', '.join(short(x, ns) for x in v) if isinstance(v, list) else v
        if value:
            break
    value = value.replace('|', '\\|')
    return f'**{value}**' if bold and value else value


def render_directive(kind, attrs, entries):
    a = dict(ATTR.findall(attrs))
    ns = a.get('ns', '')
    rows = select(entries, a.get('filter', ''))
    if kind == 'table':
        cols = [c.split(':', 1) for c in a['cols'].split('|')]
        lines = ['| ' + ' | '.join(label for label, _ in cols) + ' |', '|' + '---|' * len(cols)]
        for e in rows:
            lines.append('| ' + ' | '.join(cell(e, src, ns) or a.get('empty', '') for _, src in cols) + ' |')
        return '\n'.join(lines)
    if kind == 'arguments':
        return '\n\n'.join(
            f'Argument for **{", ".join(short(x, ns) for x in e.list("supports"))}** (§{e.get("where")}): {e.statement()}'
            for e in rows)
    if kind == 'frames':
        spaces = a['spaces'].split(',')
        ids = {e.id: e for e in entries}
        openers = [opener(s, ids) for s in spaces]
        lines = ['| | ' + ' | '.join(f'`{s}`' for s in spaces) + ' |', '|---|' + '---|' * len(spaces)]
        lines.append('| Opened by | ' + ' | '.join(op.get('title') for op in openers) + ' |')
        lines.append('| Holds fixed | ' + ' | '.join(', '.join(short(x, s) for x in op.list('holds_fixed'))
                                                      for s, op in zip(spaces, openers)) + ' |')
        in_force = [{m.id for m in effective_method(s, entries)} for s in spaces]
        methods = sorted({m for f in in_force for m in f} | {resolve(r, op.ns, ids) for op in openers for r in op.list('overrides')},
                         key=lambda m: (ids[m].ns != 'method', int(ids[m].get('order', 0) or 0)))
        for m in methods:
            if ids[m].get('role') == 'protocol':
                continue
            cells = []
            for s, f, op in zip(spaces, in_force, openers):
                if m in f:
                    cells.append('local' if ids[m].ns == s else 'in force')
                elif m in {resolve(r, op.ns, ids) for r in op.list('overrides')}:
                    cells.append('**overridden**')
                else:
                    cells.append('')
            lines.append(f'| {short(m, spaces[0])} | ' + ' | '.join(cells) + ' |')
        return '\n'.join(lines)
    if kind == 'entry':
        e = {x.id: x for x in entries}[a['id']]
        return re.sub(r'^## ', '#### ', e.body.strip(), flags=re.M)
    if kind == 'compare':
        frame = a['frame']
        ids = {e.id: e for e in entries}
        op = ids[f'{frame}/_frame']
        stance = {}
        for field in ('accepts', 'rejects', 'reinterprets', 'divided'):
            for ref in op.list(field):
                stance[resolve(ref, frame, ids)] = field
        local = [e for e in entries if e.ns == frame and e is not op]
        lines = ['| Id | Entry | Stance | In the frame |', '|---|---|---|---|']
        for e in rows:
            if e.get('type') not in ('claim', 'concept', 'decision', 'position', 'question') or e.get('status') == 'withdrawn':
                continue
            st = stance.get(e.id, 'not addressed')
            if e.get('type') == 'question':
                answering = [x for x in local if e.id in {resolve(r, frame, ids) for r in x.list('answers')}]
                st = 'answered' if answering else 'open'
            detail = ''
            if e.get('type') == 'question':
                about = [x for x in local if e.id in {resolve(r, frame, ids) for r in x.list('about')}]
                detail = '; '.join(filter(None, [
                    'by ' + ', '.join(short(x.id, frame) for x in answering) if answering else '',
                    'see ' + ', '.join(short(x.id, frame) for x in about) if about else '']))
            elif st == 'reinterprets':
                detail = ', '.join(short(x.id, frame) for x in local
                                   if e.id in {resolve(r, frame, ids) for r in x.list('translates') + x.list('corresponds')})
            elif st == 'divided':
                parts = []
                for x in local:
                    for f in ('accepts', 'rejects'):
                        if e.id in {resolve(r, frame, ids) for r in x.list(f)}:
                            parts.append(f'{short(x.id, frame)} {f}')
                detail = '; '.join(parts)
            else:
                detail = ', '.join(short(x.id, frame) for x in local
                                   if e.id in {resolve(r, frame, ids) for r in x.list('answers') + x.list('about')})
            text = e.statement()
            label = e.get('title') if e.get('title') != short(e.id, ns) else text[:90] + ('…' if len(text) > 90 else '')
            label = label.replace('|', '\\|')
            lines.append(f'| {short(e.id, ns)} | {label} | {st} | {detail} |')
        return '\n'.join(lines)
    if kind == 'deps':
        return '\n'.join(f'- **{short(e.id, ns)}** ← {", ".join(short(x, ns) for x in e.list("requires"))}'
                         for e in rows if e.list('requires'))


def render(template, entries):
    text = open(template, encoding='utf-8').read()
    m = re.match(r'<!--\s*out:\s*(\S+)\s*-->\n', text)
    if not m:
        raise SystemExit(f'{template}: first line must be <!-- out: path -->')
    body = DIRECTIVE.sub(lambda d: render_directive(d.group(1), d.group(2), entries), text[m.end():])
    rel = os.path.relpath(template, REPO).replace(os.sep, '/')
    head = f'<!-- Generated by organon/tools/register.py from {rel} and the organon entries. Edit those, not this file. -->\n\n'
    return os.path.join(REPO, m.group(1)), head + body


def main():
    entries = load()
    check = '--check' in sys.argv
    stale = 0
    views = os.path.join(ORGANON, 'views')
    for f in sorted(os.listdir(views)):
        if not f.endswith('.md'):
            continue
        out, text = render(os.path.join(views, f), entries)
        old = open(out, encoding='utf-8').read() if os.path.exists(out) else None
        if check:
            if old != text:
                stale += 1
                print('stale:', os.path.relpath(out, REPO))
        elif old != text:
            open(out, 'w', encoding='utf-8', newline='\n').write(text)
            print('wrote', os.path.relpath(out, REPO))
    sys.exit(1 if stale else 0)


if __name__ == '__main__':
    main()
