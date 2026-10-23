"""Shared reading of organon entries and the central bibliography. Standard library only.

An entry is a Markdown file that begins with a front-matter block between '---' lines. Front matter is
a restricted YAML: one 'key: value' per line, where a value is a plain string or a list '[a, b, c]'.
"""
import os
import re

ORGANON = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ORGANON)
ENTRY_DIRS = ['graph', 'method', 'library/sources']

TYPES = {
    'claim':      ['unexamined', 'proposed', 'adopted', 'examined', 'withdrawn', 'refuted'],
    'concept':    ['proposed', 'adopted', 'withdrawn'],
    'argument':   ['proposed', 'accepted', 'rejected'],
    'position':   ['open', 'adopted', 'closed'],
    'objection':  ['open', 'answered', 'conceded'],
    'question':   ['open', 'answered', 'dissolved'],
    'decision':   ['taken', 'revised'],
    'dissent':    ['standing', 'withdrawn', 'vindicated', 'overruled'],
    'prediction': ['pending', 'right', 'wrong', 'mixed'],
    'test':       ['planned', 'run', 'abandoned'],
    'method':     ['in-force', 'revised', 'retired'],
    'convention': ['in-force', 'retired'],
    'excerpt':    ['recorded'],
    'source':     ['to-read', 'reading', 'read'],
    'investigation': ['exploring', 'deciding', 'paused', 'finished'],
    'frame':      ['active', 'paused', 'abandoned', 'concluded'],
    'friction':   ['open', 'resolved'],
}
# Fields whose values are entry ids.
LINKS = ['requires', 'supports', 'attacks', 'refines', 'contradicts', 'answers', 'about',
         'excluded_by', 'closed_by', 'against', 'test', 'reopens', 'closes', 'see', 'revises',
         'question', 'builds_on', 'investigation', 'accepts', 'rejects', 'reinterprets', 'overrides',
         'corresponds', 'translates', 'between', 'resolved_by', 'sublates', 'divided', 'holds_fixed']
# Every namespace in graph/ is opened by one of these entries.
OPENERS = {'_investigation': 'investigation', '_frame': 'frame'}
FRICTION_KINDS = ['contradiction', 'tension', 'collapse', 'underdetermination', 'gap', 'regress',
                  'triviality', 'anomaly', 'ambiguity', 'overreach']
RESOLUTIONS = ['reject', 'distinguish', 'restrict', 'accept', 'dissolve', 'sublate']
EFFECTS = ['blocks', 'prompts']
REQUIRED = {
    'investigation': {'*': ['question', 'folder']},
    'frame':      {'*': ['investigation']},
    'friction':   {'*': ['kind', 'between', 'effect'], 'resolved': ['resolved_by', 'resolution']},
    'position':   {'closed': ['closed_by', 'basis']},
    'decision':   {'*': ['basis', 'by']},
    'dissent':    {'*': ['by', 'against']},
    'prediction': {'*': ['by', 'test']},
    'test':       {'run': ['protocol', 'result']},
    'excerpt':    {'*': ['cites', 'location', 'verified']},
}
BASIS = ['commitment', 'method', 'both']
VERIFIED = ['text', 'secondary', 'record', 'memory', 'unknown']
PEOPLE = ['mario', 'claude', 'both']


class Entry:
    def __init__(self, path, fm, body):
        self.path, self.fm, self.body = path, fm, body
        self.id = fm.get('id', '')
        self.ns = self.id.split('/')[0] if '/' in self.id else ''

    def get(self, key, default=''):
        return self.fm.get(key, default)

    def list(self, key):
        v = self.fm.get(key, [])
        return v if isinstance(v, list) else [v]

    def statement(self):
        """The first paragraph of the body, on one line."""
        para = self.body.strip().split('\n\n')[0]
        return ' '.join(line.strip() for line in para.splitlines())

    def section(self, name):
        """Text of the body section '## name', on one line ('' if absent). Matching ignores case."""
        m = re.search(r'^##\s+' + re.escape(name) + r'\s*$(.*?)(?=^##\s|\Z)', self.body, re.M | re.S | re.I)
        if not m:
            return ''
        return ' '.join(line.strip() for line in m.group(1).strip().splitlines())


def parse_value(v):
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        return [x.strip() for x in v[1:-1].split(',') if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        return v[1:-1]
    return v


def read_entry(path):
    text = open(path, encoding='utf-8').read()
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError(f'{path}: unterminated front matter')
    fm = {}
    for n, line in enumerate(text[4:end].splitlines(), 2):
        if not line.strip():
            continue
        if ':' not in line:
            raise ValueError(f'{path}:{n}: expected "key: value"')
        k, v = line.split(':', 1)
        fm[k.strip()] = parse_value(v)
    return Entry(path, fm, text[end + 5:])


def expected_id(path):
    rel = os.path.relpath(path, ORGANON).replace(os.sep, '/')[:-3]
    if rel.startswith('graph/'):
        return rel[len('graph/'):]
    if rel.startswith('method/'):
        return rel
    if rel.startswith('library/sources/'):
        return 'src/' + rel[len('library/sources/'):]
    return None


def load():
    entries = []
    for d in ENTRY_DIRS:
        for root, _, files in os.walk(os.path.join(ORGANON, d)):
            for f in sorted(files):
                if f.endswith('.md'):
                    e = read_entry(os.path.join(root, f))
                    if e is not None:
                        entries.append(e)
    return entries


def resolve(ref, ns, ids):
    """A link may be a full id (ns/local) or, within the same namespace, a local id."""
    if ref in ids:
        return ref
    if f'{ns}/{ref}' in ids:
        return f'{ns}/{ref}'
    return None


def load_bib(path=None):
    path = path or os.path.join(ORGANON, 'library', 'refs.bib')
    text = open(path, encoding='utf-8').read()
    bib = {}
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        if m.group(1).lower() in ('comment', 'string', 'preamble'):
            continue
        depth, j = 0, text.index('{', m.start())
        while True:
            c = text[j]
            depth += (c == '{') - (c == '}')
            if depth == 0:
                break
            j += 1
        body = text[m.start():j + 1]
        v = re.search(r'\bverified\s*=\s*\{([^}]*)\}', body)
        bib[m.group(2)] = {'verified': v.group(1).strip() if v else None, 'raw': body}
    return bib


def opener(ns, ids):
    """The _investigation or _frame entry that opens namespace ns, if any."""
    for local in OPENERS:
        if f'{ns}/{local}' in ids:
            return ids[f'{ns}/{local}']
    return None


def effective_method(ns, entries):
    """Method entries in force in namespace ns: the general ones in method/, minus those its opener
    (and, for a frame, its investigation's opener) overrides, plus method entries local to ns."""
    ids = {e.id: e for e in entries}
    overridden, chain, seen = set(), [], set()
    op = opener(ns, ids)
    while op is not None and op.id not in seen:
        seen.add(op.id)
        chain.append(op)
        parent = op.list('investigation')
        op = ids.get(resolve(parent[0], op.ns, ids)) if parent else None
    for op in chain:
        overridden |= {resolve(r, op.ns, ids) for r in op.list('overrides')}
    general = [e for e in entries if e.ns == 'method' and e.get('type') == 'method'
               and e.get('status') == 'in-force' and e.id not in overridden]
    local = [e for e in entries if e.get('type') == 'method' and e.get('status') == 'in-force'
             and e.ns in {o.ns for o in chain} and e.ns != 'method']
    return general + local


def short(ref, ns):
    """An id as shown in a view of namespace ns."""
    for prefix in (ns + '/', 'method/'):
        if ref.startswith(prefix):
            return ref[len(prefix):]
    return ref
