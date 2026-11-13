"""Helpers for building question banks. Every answer is computed, never typed by hand."""
from fractions import Fraction as Fr
import math, random

def fr(a, b=None):
    """HTML fraction from Fraction or (a,b) strings."""
    if b is not None:
        return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'
    x = Fr(a)
    if x.denominator == 1:
        return num(x.numerator)
    s = '−' if x < 0 else ''
    return f'{s}<span class="fr"><span>{abs(x.numerator)}</span><span>{x.denominator}</span></span>'

def num(x):
    """Plain text number (ints with comma groups when large, − sign)."""
    if isinstance(x, Fr):
        if x.denominator == 1:
            x = x.numerator
        else:
            x = float(x)
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    if isinstance(x, int):
        s = f'{abs(x):,}' if abs(x) >= 10000 else str(abs(x))
    else:
        s = f'{abs(x):,.6f}'.rstrip('0').rstrip('.') if abs(x) >= 10000 else f'{abs(x):.6f}'.rstrip('0').rstrip('.')
    return ('−' if x < 0 else '') + s

def ol(*steps):
    return '<ol>' + ''.join(f'<li>{s}</li>' for s in steps) + '</ol>'

def NUM(q, a, s, u=None, h=None):
    a = Fr(a)
    d = {'t': 'num', 'q': q, 'a': float(a) if a.denominator != 1 else int(a), 's': s}
    if a.denominator != 1 and round(float(a), 6) != float(a):
        raise ValueError('non-terminating numeric answer: ' + q)
    if u: d['u'] = u
    if h: d['h'] = h
    return d

class MCBuilder:
    def __init__(self, rng, nopt):
        self.rng, self.nopt = rng, nopt
    def __call__(self, q, correct, wrongs, s, h=None):
        """correct/wrongs are display strings (HTML). Picks nopt-1 unique wrongs."""
        seen, opts = {correct}, []
        for w in wrongs:
            if w not in seen:
                seen.add(w); opts.append(w)
            if len(opts) == self.nopt - 1:
                break
        if len(opts) < self.nopt - 1:
            raise ValueError('not enough distractors: ' + q)
        k = self.rng.randrange(self.nopt)
        opts.insert(k, correct)
        d = {'t': 'mc', 'q': q, 'c': opts, 'a': k, 's': s}
        if h: d['h'] = h
        return d

def num_wrongs(v, extra=()):
    """Plausible wrong values around a numeric answer, as Fractions."""
    v = Fr(v)
    c = list(extra) + [v + 1, v - 1, 2 * v, v / 2, -v, v + 2, v - 2, 3 * v, v * Fr(3, 2), v + 10, v - 10, v * 10, v + 5]
    return [Fr(x) for x in c if Fr(x) != v]

def build_topic(templates, n, seed, nopt=4, exclude=()):
    """Cycle templates until n unique questions (by text)."""
    rng = random.Random(seed)
    mc = MCBuilder(rng, nopt)
    out, seen, tries = [], set(exclude), 0
    while len(out) < n:
        tries += 1
        if tries > 5000:
            if len(out) >= 12: break
            raise RuntimeError(f'only {len(out)} unique questions for seed {seed}')
        t = templates[(tries - 1) % len(templates)]
        try:
            q = t(rng, mc)
        except ValueError as e:
            if 'non-terminating' in str(e): continue
            raise
        if q['q'] in seen:
            continue
        seen.add(q['q']); out.append(q)
    return out

def sq(x):
    r = math.isqrt(x)
    return r if r * r == x else None
