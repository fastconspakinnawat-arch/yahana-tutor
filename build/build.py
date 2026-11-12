import json, sys, importlib, re
sys.path.insert(0, '.')
from core import build_topic, num_wrongs, num, fr
import random
from fractions import Fraction as Fr
CONVERT = {'bank_grade': .35, 'bank_m1': .5, 'bank_m4': .7, 'bank_a1': 0, 'bank_a2': .2, 'bank_ap': .75}
def to_mc(q, rng, nopt, phys=False):
    v = Fr(q['a']).limit_denominator(10**6)
    if phys:
        ws = [2 * v, v / 2, 10 * v, v / 10, 4 * v, v / 4, 3 * v, v / 3, v * Fr(3, 2), v * Fr(2, 3)]
        head = ws[:6]; rng.shuffle(head); ws = head + ws[6:]
    else:
        ws = num_wrongs(v)
    ws = [w for w in ws if w != v and ((w > 0) == (v > 0) or v == 0)]
    ws = [w for w in ws if Fr(w * 10**6).denominator == 1]
    u = (' ' + q['u']) if q.get('u') else ''
    show = lambda x: num(x) + u
    opts, seen = [], {show(v)}
    for w in ws:
        if show(w) not in seen: seen.add(show(w)); opts.append(show(w))
        if len(opts) == nopt - 1: break
    if len(opts) < nopt - 1: return q
    k = rng.randrange(nopt); opts.insert(k, show(v))
    d = {'t': 'mc', 'q': q['q'], 'c': opts, 'a': k, 's': q['s']}
    if 'h' in q: d['h'] = q['h']
    return d


MODULES = sys.argv[1:] or ['bank_m1', 'bank_m4', 'bank_a1', 'bank_a2', 'bank_ap', 'bank_grade']
bank, new = {}, {}
def fix(t):
    t = t.replace(' < ', ' &lt; ').replace('− -', '+ ').replace('+ -', '− ').replace('= -', '= −').replace('(-', '(−').replace(', -', ', −')
    return re.sub(r'(?<![\w"=#])-(\d)', r'−\1', t)
def clean(q):
    q['q'], q['s'] = fix(q['q']), fix(q['s'])
    if 'c' in q: q['c'] = [fix(c) for c in q['c']]
    if 'h' in q: q['h'] = fix(q['h'])

for mi, mod in enumerate(MODULES):
    m = importlib.import_module(mod)
    for ti, (tid, tpls) in enumerate(m.TOPICS.items()):
        qs = build_topic(tpls, 30, seed=1000 * (mi + 1) + ti, nopt=m.NOPT)
        crng = random.Random(77 + ti)
        qs = [to_mc(q, crng, m.NOPT, mod == 'bank_ap' or tid[:3] in ('mp-', 'hp-')) if q['t'] == 'num' and crng.random() < CONVERT.get(mod, 0) else q for q in qs]
        for q in qs:
            clean(q)
            txt = json.dumps(q, ensure_ascii=False)
            assert not re.search(r'None|nan|inf\b', txt), txt
            if q['t'] == 'mc':
                assert len(set(q['c'])) == len(q['c']) == m.NOPT and 0 <= q['a'] < m.NOPT, q
            else:
                assert isinstance(q['a'], (int, float)), q
        bank[tid] = qs
    for tid, (lvl, subj, name) in m.NEW.items():
        new[tid] = {'level': lvl, 'subj': subj, 'name': name}
    print(mod, {k: len(v) for k, v in bank.items() if k in m.TOPICS},
          'mc:', sum(q['t'] == 'mc' for k in m.TOPICS for q in bank[k]))
json.dump({'bank': bank, 'new': new}, open('bank.json', 'w'), ensure_ascii=False)
print('total', sum(map(len, bank.values())))
