"""Helpers for fact-based (non-computed) question banks."""
from core import ol, MCBuilder


def fact_q(mc, item):
    """item = (question, answer, [wrongs...], explanation-or-None)."""
    q, a, w = item[0], item[1], item[2]
    s = item[3] if len(item) > 3 and item[3] else f'คำตอบ: {a}'
    return mc(q, a, w, ol(s) if not s.startswith('<ol>') else s)


def facts_tpl(pool):
    """Template that picks one fact item from pool."""
    def t(rng, mc):
        return fact_q(mc, rng.choice(pool))
    return t


def pair_tpls(pairs, fwd, rev=None, why=None):
    """pairs = [(key, value)]. fwd: question about key -> value; rev: value -> key.
    Distractors come from the other pairs. why(k, v) gives the explanation."""
    why = why or (lambda k, v: f'{k} = {v}')

    def f(rng, mc):
        k, v = rng.choice(pairs)
        others = [p[1] for p in rng.sample(pairs, len(pairs)) if p[1] != v]
        return mc(fwd.format(k=k), v, others, ol(why(k, v)))

    def r(rng, mc):
        k, v = rng.choice(pairs)
        others = [p[0] for p in rng.sample(pairs, len(pairs)) if p[0] != k]
        return mc(rev.format(v=v), k, others, ol(why(k, v)))
    return [f, r] if rev else [f]


def custom_topic(gen, n=30, nopt=4):
    """gen(rng, mc, i) -> question. Returns builder(rng, n) for TOPICS with unique (q, options) combos."""
    def build(rng, n=n):
        mc = MCBuilder(rng, nopt)
        out, seen, tries = [], set(), 0
        while len(out) < n:
            tries += 1
            if tries > 5000:
                raise RuntimeError('custom topic short')
            q = gen(rng, mc, len(out))
            key = q['q'] + '|' + '|'.join(sorted(q.get('c', [])))
            if key in seen:
                continue
            seen.add(key)
            out.append(q)
        return out
    return build
