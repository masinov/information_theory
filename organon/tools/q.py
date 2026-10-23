"""Query entries by field, or show what links to an entry.

    python tools/q.py type=position status=open      entries matching all conditions
    python tools/q.py ns=mec role=branch
    python tools/q.py --links mec/C                  entries that link to mec/C, and how
    python tools/q.py --show mec/C                   one entry, with its links in both directions
    python tools/q.py --method mec                   method entries in force in a namespace
"""
import sys
from lib import load, resolve, effective_method, LINKS


def main(args):
    entries = load()
    ids = {e.id: e for e in entries}
    if args and args[0] == '--method':
        for m in effective_method(args[1], entries):
            print(f'{m.id:28} {m.get("role"):14} {m.get("title")}')
        return
    if args and args[0] in ('--links', '--show'):
        target = args[1]
        if args[0] == '--show':
            e = ids[target]
            print(open(e.path, encoding='utf-8').read())
            print('--- linked from:')
        for e in entries:
            for field in LINKS:
                for ref in e.list(field):
                    if resolve(ref, e.ns, ids) == target:
                        print(f'{e.id:28} {field:12} {e.get("title")}')
        return
    conds = [a.split('=', 1) for a in args]
    for e in entries:
        if all((e.ns if k == 'ns' else e.get(k)) == v or v in e.list(k) for k, v in conds):
            print(f'{e.id:28} {e.get("type"):10} {e.get("status"):10} {e.get("title")}')


if __name__ == '__main__':
    main(sys.argv[1:])
