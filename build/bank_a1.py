"""A-Level คณิตศาสตร์ประยุกต์ 1"""
from core import *
import math
R = lambda rng, a, b: rng.randint(a, b)

def MCN(mc, q, v, s, h=None, extra=(), prob=False):
    ws = num_wrongs(v, extra)
    if prob:
        ws = [x for x in ws if 0 < x < 1] + [Fr(1, 2), Fr(1, 4), Fr(3, 4), Fr(1, 3), Fr(2, 3), Fr(1, 8), Fr(1, 5)]
    return mc(q, fr(v), [fr(x) for x in ws], s, h)

def poly(cs, var='x'):
    """cs: list of (coef, power) → string"""
    out = ''
    for c, p in cs:
        if c == 0: continue
        sign = ' − ' if c < 0 else (' + ' if out else '')
        if c < 0 and not out: sign = '−'
        a = abs(c)
        coef = '' if (a == 1 and p) else str(a)
        term = coef + ('' if p == 0 else var + ('' if p == 1 else {2: '²', 3: '³', 4: '⁴'}[p]))
        out += sign + term
    return out or '0'

# ---------- a1-explog ----------
def log_eq(rng, mc):
    b = rng.choice([2, 3]); k = R(rng, 1, 4); target = b**k
    pairs = [(x, p) for x in range(2, 40) for p in range(1, x) if x * x - p * p == target]
    if not pairs: return log_eq(rng, mc)
    x, p = rng.choice(pairs)
    return NUM(f'ถ้า log<sub>{b}</sub>(x − {p}) + log<sub>{b}</sub>(x + {p}) = {k} แล้ว x มีค่าเท่าใด', x,
               ol(f'log<sub>{b}</sub>[(x − {p})(x + {p})] = {k} → x² − {p*p} = {b}<sup>{k}</sup> = {target}', f'x² = {target+p*p} → x = ±{x}', f'ต้องมี x > {p} จึงได้ x = {x}'),
               h='รวม log แล้วอย่าลืมตรวจโดเมน')

def exp_quad(rng, mc):
    m, n = rng.sample([0, 1, 2, 3, 4, 5], 2); A, B = 2**m, 2**n
    S, P = A + B, A * B
    return NUM(f'ผลบวกของคำตอบทั้งหมดของสมการ 4<sup>x</sup> − {S}·2<sup>x</sup> + {P} = 0', m + n,
               ol('ให้ A = 2<sup>x</sup> จะได้ A² − ' + f'{S}A + {P} = 0', f'(A − {A})(A − {B}) = 0 → 2<sup>x</sup> = {A} หรือ {B}', f'x = {m} หรือ {n} ผลบวก = {m+n}'),
               h='ให้ A = 2ˣ')

def log_vals(rng, mc):
    a, b = R(rng, 2, 7), R(rng, 2, 5); c = rng.choice([2, 4, 8, 16])
    v = a + b - Fr(int(math.log2(c)), 2)
    return MCN(mc, f'log<sub>2</sub> {2**a} + log<sub>3</sub> {3**b} − log<sub>4</sub> {c} มีค่าเท่าใด', v,
               ol(f'log<sub>2</sub> {2**a} = {a}', f'log<sub>3</sub> {3**b} = {b}', f'log<sub>4</sub> {c} = {fr(Fr(int(math.log2(c)),2))} (เพราะ 4 = 2²)', f'รวม = {fr(v)}'))

def exp_eq(rng, mc):
    a, b = R(rng, 1, 4), R(rng, 1, 9)
    x = 3 * a - b
    return NUM(f'ถ้า 3<sup>2x − {b}</sup> = 27<sup>x − {a}</sup> แล้ว x มีค่าเท่าใด', x,
               ol(f'27<sup>x − {a}</sup> = 3<sup>3(x − {a})</sup> = 3<sup>3x − {3*a}</sup>', f'2x − {b} = 3x − {3*a}', f'x = {3*a} − {b} = {num(x)}'), h='ทำฐานให้เท่ากัน')

def log_rule(rng, mc):
    a, b = rng.choice([(2, 50), (4, 25), (5, 20), (8, 125), (20, 50), (25, 40), (2, 5)]); c = rng.choice([1, 10, 100])
    v = round(math.log10(a * b / c))
    return MCN(mc, f'log {a} + log {b} − log {c} มีค่าเท่าใด (log ฐาน 10)', v,
               ol(f'= log {fr(f"{a} × {b}", c)} = log {num(Fr(a*b, c))}', f'= {v}'))

def change_base(rng, mc):
    a, b = rng.choice([(4, 8), (8, 4), (9, 27), (27, 9), (16, 8), (8, 32), (25, 125), (4, 32)])
    import math as M
    base = {4: 2, 8: 2, 16: 2, 32: 2, 9: 3, 27: 3, 25: 5, 125: 5}
    p, q = round(M.log(a, base[a])), round(M.log(b, base[b]))
    v = Fr(q, p)
    return MCN(mc, f'log<sub>{a}</sub> {b} มีค่าเท่าใด', v, ol(f'{a} = {base[a]}<sup>{p}</sup>, {b} = {base[b]}<sup>{q}</sup>', f'log<sub>{a}</sub> {b} = {fr(q, p)}' + (f' = {fr(v)}' if math.gcd(p, q) > 1 else '')))

def domain(rng, mc):
    a, b = R(rng, -5, 4), R(rng, 5, 12)
    A, B = num(a), num(b)
    return mc(f'โดเมนของ f(x) = {fr(f"√(x − {a})".replace("− -","+ "), f"x − {b}")} คือข้อใด', f'[{A}, ∞) − {{{B}}}',
              [f'({A}, ∞)', f'[{A}, {B})', f'({B}, ∞)', f'ℝ − {{{B}}}', f'[{A}, {B}]', f'({A}, ∞) − {{{B}}}'],
              ol(f'ใต้รากต้องไม่ติดลบ: x ≥ {A}', f'ตัวส่วนต้องไม่เป็นศูนย์: x ≠ {B}', f'โดเมน = [{A}, ∞) − {{{B}}}'))

# ---------- a1-calc ----------
def deriv_at(rng, mc):
    a, b, c = R(rng, 1, 4), R(rng, -6, 6), R(rng, -9, 9); x0 = R(rng, -3, 3)
    v = 3 * a * x0 * x0 + 2 * b * x0 + c
    return MCN(mc, f'ถ้า f(x) = {poly([(a,3),(b,2),(c,1),(R(rng,-5,9),0)])} แล้ว f′({x0}) มีค่าเท่าใด', v,
               ol(f"f′(x) = {poly([(3*a,2),(2*b,1),(c,0)])}", f"f′({x0}) = {v}"))

def lim0(rng, mc):
    a = R(rng, 1, 9); k = rng.choice([2, 3])
    if k == 2:
        return MCN(mc, f'lim<sub>x→{a}</sub> {fr(f"x² − {a*a}", f"x − {a}")} มีค่าเท่าใด', 2 * a,
                   ol(f'{fr(f"(x − {a})(x + {a})", f"x − {a}")} = x + {a} เมื่อ x ≠ {a}', f'ลิมิต = {a} + {a} = {2*a}'))
    return MCN(mc, f'lim<sub>x→{a}</sub> {fr(f"x³ − {a**3}", f"x − {a}")} มีค่าเท่าใด', 3 * a * a,
               ol(f'x³ − {a**3} = (x − {a})(x² + {a}x + {a*a})', f'ลิมิต = {a*a} + {a*a} + {a*a} = {3*a*a}'))

def integ(rng, mc):
    a, b, c = R(rng, 1, 3), R(rng, -4, 4), R(rng, -5, 6); u = R(rng, 1, 3)
    F = lambda x: a * x**3 + b * x**2 + c * x
    v = F(u) - F(0)
    return MCN(mc, f'∫<sub>0</sub><sup>{u}</sup> ({poly([(3*a,2),(2*b,1),(c,0)])}) dx มีค่าเท่าใด', v,
               ol(f'ปฏิยานุพันธ์ = {poly([(a,3),(b,2),(c,1)])}', f'แทนค่า x = {u} ลบ x = 0 ได้ {v}'))

def rel_min(rng, mc):
    a, c = R(rng, 1, 3), R(rng, -10, 30)
    fmin = -2 * a**3 + c
    return NUM(f'f(x) = x³ − {3*a*a}x{" + " if c>=0 else " − "}{abs(c)} มีค่าต่ำสุดสัมพัทธ์เท่ากับเท่าใด', fmin,
               ol(f'f′(x) = 3x² − {3*a*a} = 0 → x = ±{a}', f'f″(x) = 6x, f″({a}) > 0 → ต่ำสุดสัมพัทธ์ที่ x = {a}', f'f({a}) = {a**3} − {3*a**3} {"+" if c>=0 else "−"} {abs(c)} = {fmin}'))

def area_par(rng, mc):
    k = R(rng, 1, 6); v = Fr(k**3, 6)
    return MCN(mc, f'พื้นที่ที่ปิดล้อมด้วยกราฟ y = x² และ y = {k if k>1 else ""}x เท่ากับกี่ตารางหน่วย', v,
               ol(f'จุดตัด: x² = {k}x → x = 0, {k}', f'∫<sub>0</sub><sup>{k}</sup> ({k}x − x²) dx = {fr(k**3,2)} − {fr(k**3,3)} = {fr(v)}'), extra=[Fr(k**3, 3), Fr(k**3, 2), Fr(k**2, 6)])

def lim_inf(rng, mc):
    a, b = R(rng, 1, 9), R(rng, 1, 5); v = Fr(a, b)
    return MCN(mc, f'lim<sub>x→∞</sub> {fr(f"{a}x² + {R(rng,1,9)}x − 1", f"{b}x² − {R(rng,1,7)}")} มีค่าเท่าใด', v,
               ol('หารทั้งเศษและส่วนด้วย x² พจน์ที่เหลือมี 1/x หรือ 1/x² ซึ่งเข้าใกล้ 0', f'ลิมิต = {fr(a,b)}' + (f' = {fr(v)}' if math.gcd(a,b)>1 else '')), extra=[0, 1])

def tangent(rng, mc):
    a, b = R(rng, 1, 3), R(rng, -4, 4); x0 = R(rng, 1, 3); c = R(rng, -5, 5)
    f = lambda x: a * x * x + b * x + c
    m = 2 * a * x0 + b; y0 = f(x0); icpt = y0 - m * x0
    return NUM(f'เส้นสัมผัสเส้นโค้ง y = {poly([(a,2),(b,1),(c,0)])} ที่ x = {x0} ตัดแกน y ที่จุด (0, k) k มีค่าเท่าใด', icpt,
               ol(f'ความชัน m = y′({x0}) = {2*a}({x0}) {"+" if b>=0 else "−"} {abs(b)} = {m}', f'จุดสัมผัส ({x0}, {y0})', f'สมการ y − {y0} = {m}(x − {x0}) แทน x = 0: k = {y0} − {m*x0} = {icpt}'))

def lin(c0, c1):
    return f"{' − ' if c0 < 0 else ' + '}{abs(c0)}{c1}"
def crit_sum(rng, mc):
    p, q = rng.sample(range(-4, 6), 2)
    B, C = 3 * (p + q), 3 * p * q
    expr = '3x²' + (lin(-B, 'x') if B else '') + (lin(C, '') if C else '')
    return MCN(mc, f'ถ้า f′(x) = {expr} ผลบวกของค่าวิกฤตทั้งหมดของ f เท่ากับเท่าใด', p + q,
               ol(f'{expr} = 3(x − ({num(p)}))(x − ({num(q)})) = 0', f'ค่าวิกฤต x = {num(p)}, {num(q)} ผลบวก = {num(p+q)}'), extra=[p * q, -(p + q)])

# ---------- a1-vec ----------
QUAD = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (2, 10, 11, 15), (6, 6, 7, 11), (3, 4, 12, 13), (2, 5, 14, 15), (1, 12, 12, 17)]
def vmag(rng, mc):
    a, b, c, d = rng.choice(QUAD); k = rng.choice([1, 1, 2])
    sg = [rng.choice([1, -1]) for _ in range(3)]
    v = [a * k * sg[0], b * k * sg[1], c * k * sg[2]]
    return MCN(mc, f'ขนาดของเวกเตอร์ u = ({", ".join(num(x) for x in v)}) เท่ากับเท่าใด', d * k,
               ol(f'|u| = √({" + ".join(f"{abs(x)}²" for x in v)}) = √{(d*k)**2}', f'= {d*k}'))

def dot(rng, mc):
    u = [R(rng, -5, 6) for _ in range(3)]; v = [R(rng, -5, 6) for _ in range(3)]
    d = sum(x * y for x, y in zip(u, v))
    return MCN(mc, f'u = ({", ".join(map(num,u))}) และ v = ({", ".join(map(num,v))}) แล้ว u · v มีค่าเท่าใด', d,
               ol(f'u · v = ' + ' + '.join(f'({num(x)})({num(y)})' for x, y in zip(u, v)), f'= {num(d)}'))

def cmod(rng, mc):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (7, 24, 25), (20, 21, 29)])
    a, b = a * rng.choice([1, -1]), b * rng.choice([1, -1])
    return MCN(mc, f'|{num(a)} {"+" if b>0 else "−"} {abs(b)}i| เท่ากับเท่าใด', c, ol(f'|a + bi| = √(a² + b²) = √({a*a} + {b*b}) = {c}'))

def one_i(rng, mc):
    k = rng.choice([2, 4, 6, 8, 10]); n = 2 * k
    v = (2j) ** k
    val = int(round(v.real)) if abs(v.imag) < 1e-9 else None
    if val is None: return one_i(rng, mc)
    return MCN(mc, f'(1 + i)<sup>{n}</sup> เท่ากับเท่าใด', val, ol('(1 + i)² = 1 + 2i + i² = 2i', f'(1 + i)<sup>{n}</sup> = (2i)<sup>{k}</sup> = {2**k} · i<sup>{k}</sup> = {num(val)}'), h='หา (1 + i)² ก่อน')

def perp(rng, mc):
    a, b, c = R(rng, 1, 6), R(rng, -6, 6), R(rng, 1, 6)
    if b == 0: b = 2
    m_num = -a * b
    if m_num % c: return perp(rng, mc)
    m = m_num // c
    return NUM(f'เวกเตอร์ ({a}, m) ตั้งฉากกับเวกเตอร์ ({num(b)}, {c}) ค่า m เท่ากับเท่าใด', m,
               ol('ตั้งฉาก ⇔ ผลคูณเชิงสเกลาร์ = 0', f'{a}({num(b)}) + m({c}) = 0', f'm = {m}'))

def ipow(rng, mc):
    n = R(rng, 10, 200); v = ['1', 'i', '−1', '−i'][n % 4]
    return mc(f'i<sup>{n}</sup> เท่ากับข้อใด', v, [x for x in ['1', 'i', '−1', '−i', '0'] if x != v],
              ol('i¹ = i, i² = −1, i³ = −i, i⁴ = 1 วนรอบละ 4', f'{n} ÷ 4 เหลือเศษ {n%4} → i<sup>{n}</sup> = {v}'))

def para_area(rng, mc):
    a, b, c, d = [R(rng, -5, 7) for _ in range(4)]
    A = abs(a * d - b * c)
    if A == 0: return para_area(rng, mc)
    return MCN(mc, f'พื้นที่ของรูปสามเหลี่ยมที่มีด้านประกอบเป็นเวกเตอร์ u = ({num(a)}, {num(b)}) และ v = ({num(c)}, {num(d)}) เท่ากับกี่ตารางหน่วย', Fr(A, 2),
               ol(f'พื้นที่สี่เหลี่ยมด้านขนาน = |{num(a)}·{num(d)} − {num(b)}·{num(c)}| = {A}', f'พื้นที่สามเหลี่ยม = {fr(A,2)}' + (f' = {num(Fr(A,2))}' if A % 2 == 0 else '')), extra=[A, 2 * A])

def cmul(rng, mc):
    a, b, c, d = [R(rng, -5, 6) for _ in range(4)]
    re_, im = a * c - b * d, a * d + b * c
    z = lambda x, y: f'({num(x)} {"+" if y>=0 else "−"} {abs(y)}i)'
    return MCN(mc, f'ส่วนจริงของ {z(a,b)}{z(c,d)} เท่ากับเท่าใด', re_, ol(f'ส่วนจริง = ac − bd = ({num(a)})({num(c)}) − ({num(b)})({num(d)})', f'= {num(re_)}'), extra=[a * c + b * d, im])

# ---------- a1-mat ----------
def det2(rng, mc):
    a, b, c, d = [R(rng, -6, 9) for _ in range(4)]
    return MCN(mc, f'det {M(f"{num(a)} {num(b)};{num(c)} {num(d)}")} มีค่าเท่าใด', a * d - b * c, ol(f'= ({num(a)})({num(d)}) − ({num(b)})({num(c)}) = {num(a*d-b*c)}'), extra=[a * d + b * c])

def M(s):
    return '<span class="mx">' + ''.join('<span class="mr">' + ''.join(f'<span>{c}</span>' for c in r.split()) + '</span>' for r in s.split(';')) + '</span>'

def detk(rng, mc):
    n, k, d = rng.choice([2, 3]), rng.choice([2, 3, -2]), R(rng, -5, 6)
    if d == 0: d = 3
    v = k**n * d
    return MCN(mc, f'A เป็นเมทริกซ์มิติ {n} × {n} ที่ det A = {num(d)} แล้ว det({num(k)}A) เท่ากับเท่าใด', v,
               ol(f'det(kA) = k<sup>n</sup> det A', f'= ({num(k)})<sup>{n}</sup> × ({num(d)}) = {num(v)}'), h='ระวัง k ต้องยกกำลังตามมิติ', extra=[k * d, k * k * d if n == 3 else k**3 * d])

def detinv(rng, mc):
    d, e = R(rng, 2, 6), R(rng, 2, 5); k = rng.randrange(3)
    if k == 0:
        return MCN(mc, f'A และ B เป็นเมทริกซ์มิติ 3 × 3 ที่ det A = {d} และ det B = {e} แล้ว det(AB<sup>t</sup>) เท่ากับเท่าใด', d * e, ol('det(B<sup>t</sup>) = det B', f'det(AB<sup>t</sup>) = {d} × {e} = {d*e}'))
    if k == 1:
        return MCN(mc, f'A เป็นเมทริกซ์มิติ 3 × 3 ที่ det A = {d} แล้ว det(A<sup>−1</sup>) เท่ากับเท่าใด', Fr(1, d), ol(f'det(A<sup>−1</sup>) = {fr(1,"det A")} = {fr(1,d)}'), extra=[-d, d, Fr(1, d**3)])
    return MCN(mc, f'A เป็นเมทริกซ์มิติ 2 × 2 ที่ det A = {d} แล้ว det(A²) + det(A<sup>−1</sup>) เท่ากับเท่าใด', d * d + Fr(1, d), ol(f'det(A²) = {d}² = {d*d}', f'det(A<sup>−1</sup>) = {fr(1,d)}', f'รวม = {fr(d*d + Fr(1,d))}'))

def det3(rng, mc):
    while True:
        m = [[R(rng, -3, 4) for _ in range(3)] for _ in range(3)]
        m[2][0] = 0 if rng.random() < .5 else m[2][0]
        d = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
        if d: break
    s = ';'.join(' '.join(num(x) for x in r) for r in m)
    return MCN(mc, f'det {M(s)} มีค่าเท่าใด', d, ol('กระจายโคแฟกเตอร์ตามแถวที่ 1 (หรือใช้วิธีลากเส้นทแยง)', f'= {num(m[0][0])}({num(m[1][1]*m[2][2]-m[1][2]*m[2][1])}) − ({num(m[0][1])})({num(m[1][0]*m[2][2]-m[1][2]*m[2][0])}) + ({num(m[0][2])})({num(m[1][0]*m[2][1]-m[1][1]*m[2][0])})', f'= {num(d)}'))

def matmul(rng, mc):
    A = [[R(rng, -3, 5) for _ in range(2)] for _ in range(2)]; B = [[R(rng, -3, 5) for _ in range(2)] for _ in range(2)]
    i, j = R(rng, 0, 1), R(rng, 0, 1)
    v = A[i][0] * B[0][j] + A[i][1] * B[1][j]
    S = lambda X: M(';'.join(' '.join(num(x) for x in r) for r in X))
    return MCN(mc, f'ถ้า A = {S(A)} และ B = {S(B)} สมาชิกในแถวที่ {i+1} หลักที่ {j+1} ของ AB เท่ากับเท่าใด', v,
               ol(f'นำแถวที่ {i+1} ของ A คูณกับหลักที่ {j+1} ของ B', f'({num(A[i][0])})({num(B[0][j])}) + ({num(A[i][1])})({num(B[1][j])}) = {num(v)}'), extra=[A[i][j] * B[i][j]])

def singular(rng, mc):
    a, b, c = R(rng, -6, 8), R(rng, -6, 8), R(rng, 1, 6)
    if (a * b) % c or a == 0: return singular(rng, mc)
    x = a * b // c
    return NUM(f'เมทริกซ์ {M(f"x {num(a)};{num(b)} {c}")} ไม่มีตัวผกผัน ค่า x เท่ากับเท่าใด', x,
               ol('ไม่มีตัวผกผัน ⇔ det = 0', f'{c}x − ({num(a)})({num(b)}) = 0 → x = {num(x)}'))

# ---------- a1-stat ----------
def atleast(rng, mc):
    m, w, k = R(rng, 4, 8), R(rng, 2, 6), R(rng, 3, 5)
    if k > m: k = m
    v = math.comb(m + w, k) - math.comb(m, k)
    return NUM(f'เลือกคณะทำงาน {k} คน จากชาย {m} คนและหญิง {w} คน โดยต้องมีหญิงอย่างน้อย 1 คน ได้กี่วิธี', v,
               ol(f'เลือกแบบใดก็ได้: C({m+w}, {k}) = {math.comb(m+w,k)}', f'ชายล้วน: C({m}, {k}) = {math.comb(m,k)}', f'{math.comb(m+w,k)} − {math.comb(m,k)} = {v}'), u='วิธี', h='ทั้งหมด − ไม่มีหญิงเลย')

def zscore(rng, mc):
    mu, sd, z = R(rng, 40, 70), rng.choice([4, 5, 8, 10, 12]), rng.choice([Fr(-3, 2), -1, Fr(-1, 2), Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2)])
    x = mu + z * sd
    if Fr(x).denominator != 1: return zscore(rng, mc)
    return MCN(mc, f'คะแนนสอบมีค่าเฉลี่ย {mu} ส่วนเบี่ยงเบนมาตรฐาน {sd} นักเรียนได้ {num(x)} คะแนน มีค่ามาตรฐาน (z) เท่าใด', z, ol(f'z = {fr("x − μ","σ")} = {fr(f"{num(x)} − {mu}", sd)} = {num(z)}'))

BASES = [([-3, -1, -1, -1, 0, 0, 2, 4], 2), ([-1, -1, 1, 1], 1), ([-2, 0, 0, 2, 0, 0, -2, 2], Fr(1)), ([-3, -3, 3, 3], 3)]
def sd_data(rng, mc):
    dev, s = rng.choice(BASES[:2] + BASES[3:]); k = rng.choice([1, 2, 3]); mu = R(rng, 5, 30)
    xs = sorted(mu + k * d for d in dev); sd = s * k
    ss = sum((x - mu)**2 for x in xs)
    return MCN(mc, f'ส่วนเบี่ยงเบนมาตรฐาน (ประชากร) ของข้อมูล {", ".join(map(str, xs))} เท่ากับเท่าใด', sd,
               ol(f'ค่าเฉลี่ย = {sum(xs)} ÷ {len(xs)} = {mu}', f'Σ(x − μ)² = {ss}', f'σ² = {ss} ÷ {len(xs)} = {num(Fr(ss,len(xs)))} → σ = {num(sd)}'), extra=[sd * sd, Fr(ss, len(xs) - 1)])

def binom(rng, mc):
    n, k = R(rng, 3, 7), 0
    k = R(rng, 1, n - 1)
    p = Fr(math.comb(n, k), 2**n)
    return MCN(mc, f'โยนเหรียญเที่ยงตรง {n} ครั้ง ความน่าจะเป็นที่ขึ้นหัวพอดี {k} ครั้ง', p,
               ol(f'เลือกครั้งที่ขึ้นหัว: C({n}, {k}) = {math.comb(n,k)}', f'ผลลัพธ์ทั้งหมด 2<sup>{n}</sup> = {2**n}', f'P = {fr(math.comb(n,k), 2**n)}' + (f' = {fr(p)}' if p.denominator != 2**n else '')),
               extra=[Fr(k, n), Fr(1, 2**n), Fr(k, 2**n), Fr(math.comb(n, k) + 1, 2**n), Fr(math.comb(n, k) - 1, 2**n)], prob=True)

def word_arr(rng, mc):
    w = rng.choice(['BANANA', 'LETTER', 'SCHOOL', 'COFFEE', 'APPLE', 'MISSISSIPPI', 'BOOKKEEPER', 'STATISTICS', 'ASSESS', 'PEPPER'])
    from collections import Counter
    c = Counter(w); v = math.factorial(len(w))
    den = 1
    for x in c.values(): den *= math.factorial(x)
    rep = [f'{k} ซ้ำ {n} ตัว' for k, n in c.items() if n > 1]
    return NUM(f'นำตัวอักษรทั้งหมดของคำว่า {w} มาเรียงสับเปลี่ยนได้ทั้งหมดกี่แบบ', v // den,
               ol(f'มี {len(w)} ตัว โดย {", ".join(rep)}', f'{fr(f"{len(w)}!", " ".join(f"{n}!" for n in c.values() if n > 1))} = {num(v//den)}'), u='แบบ')

def npr(rng, mc):
    n, r = R(rng, 5, 10), R(rng, 2, 4)
    v = math.perm(n, r)
    return NUM(f'มีนักกีฬา {n} คน คัดเลือกตำแหน่งที่ 1 ถึงที่ {r} (ไม่มีอันดับร่วม) ได้กี่แบบ', v,
               ol(f'P({n}, {r}) = ' + ' × '.join(str(n - i) for i in range(r)) + f' = {num(v)}'), u='แบบ')

def no_replace(rng, mc):
    r, b = R(rng, 2, 7), R(rng, 2, 7); n = r + b
    p = Fr(r * (r - 1), n * (n - 1))
    return MCN(mc, f'กล่องมีลูกแก้วแดง {r} ลูก น้ำเงิน {b} ลูก หยิบ 2 ลูกพร้อมกัน ความน่าจะเป็นที่ได้สีแดงทั้งคู่', p,
               ol(f'C({r}, 2) ÷ C({n}, 2) = {math.comb(r,2)} ÷ {math.comb(n,2)}', f'= {fr(p)}'), extra=[Fr(r * r, n * n), Fr(r, n), Fr(r - 1, n - 1)], prob=True)

def combined_mean(rng, mc):
    n1, n2 = R(rng, 10, 40), R(rng, 10, 40); m1, m2 = R(rng, 40, 80), R(rng, 40, 80)
    v = Fr(n1 * m1 + n2 * m2, n1 + n2)
    if Fr(v * 100).denominator != 1: return combined_mean(rng, mc)
    return NUM(f'ห้อง A มีนักเรียน {n1} คน คะแนนเฉลี่ย {m1} ห้อง B มี {n2} คน คะแนนเฉลี่ย {m2} คะแนนเฉลี่ยรวมทั้งสองห้องเท่ากับเท่าใด', v,
               ol(f'ผลรวมคะแนน = {n1}×{m1} + {n2}×{m2} = {n1*m1+n2*m2}', f'ค่าเฉลี่ยรวม = {n1*m1+n2*m2} ÷ {n1+n2} = {num(v)}'))

# ---------- a1-trig ----------
QV = {0: ('0', '1', '0'), 30: (fr(1, 2), fr('√3', 2), fr(1, '√3')), 45: (fr('√2', 2), fr('√2', 2), '1'), 60: (fr('√3', 2), fr(1, 2), '√3'), 90: ('1', '0', None)}
def neg(s): return s[1:] if s.startswith('−') else ('0' if s == '0' else '−' + s)
def trig_quad(rng, mc):
    ref = rng.choice([30, 45, 60]); q = rng.choice([2, 3, 4]); f = rng.choice(['sin', 'cos', 'tan'])
    ang = {2: 180 - ref, 3: 180 + ref, 4: 360 - ref}[q]
    base = QV[ref][['sin', 'cos', 'tan'].index(f)]
    sign = {('sin', 2): 1, ('sin', 3): -1, ('sin', 4): -1, ('cos', 2): -1, ('cos', 3): -1, ('cos', 4): 1, ('tan', 2): -1, ('tan', 3): 1, ('tan', 4): -1}[(f, q)]
    v = base if sign > 0 else neg(base)
    pool = [fr(1, 2), fr('√2', 2), fr('√3', 2), '1', '√3', fr(1, '√3')]
    wr = [neg(v)] + [x for x in pool if x != base] + [neg(x) for x in pool if x != base]
    rng.shuffle(wr); wr.insert(0, neg(v))
    return mc(f'{f} {ang}° มีค่าเท่าใด', v, wr, ol(f'{ang}° อยู่ในจตุภาคที่ {q} มุมอ้างอิง {ref}°', f'{f} ในจตุภาคที่ {q} เป็น{"บวก" if sign>0 else "ลบ"}', f'{f} {ang}° = {v}'), h='ASTC: จตุภาค 1 บวกหมด, 2 sin บวก, 3 tan บวก, 4 cos บวก')

TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
def trig_tri(rng, mc):
    a, b, c = rng.choice(TR)
    f = rng.choice(['tan', 'cos'])
    if f == 'tan':
        v = Fr(a, b); return mc(f'ถ้า sin θ = {fr(a,c)} และ 0° < θ < 90° แล้ว tan θ เท่ากับเท่าใด', fr(v), [fr(Fr(b, a)), fr(Fr(b, c)), fr(Fr(c, b)), fr(Fr(a, c)), fr(Fr(c, a))],
                                ol(f'cos θ = √(1 − sin²θ) = {fr(b,c)}', f'tan θ = {fr("sin θ","cos θ")} = {fr(a,b)}'))
    v = Fr(b, c); return mc(f'ถ้า tan θ = {fr(a,b)} และ 0° < θ < 90° แล้ว cos θ เท่ากับเท่าใด', fr(v), [fr(Fr(a, c)), fr(Fr(c, b)), fr(Fr(b, a)), fr(Fr(a, b)), fr(Fr(c, a))],
                            ol(f'สามเหลี่ยมมุมฉากด้านตรงข้าม {a} ชิด {b} → ด้านตรงข้ามมุมฉาก = {c}', f'cos θ = {fr(b,c)}'))

def sin2x(rng, mc):
    p, q = rng.choice([(1, 2), (3, 2), (4, 3), (5, 4), (7, 5), (6, 5), (1, 3)])
    k = Fr(p, q)
    if k * k > 2: return sin2x(rng, mc)
    v = k * k - 1
    return MCN(mc, f'ถ้า sin x + cos x = {fr(k)} แล้ว sin 2x มีค่าเท่าใด', v,
               ol('ยกกำลังสอง: sin²x + 2 sin x cos x + cos²x = ' + fr(k * k), f'1 + sin 2x = {fr(k*k)}', f'sin 2x = {fr(v)}'), extra=[k * k, 1 - k * k, k - 1])

def cos_law(rng, mc):
    a, b, c = rng.choice([(3, 8, 7), (5, 8, 7), (8, 15, 13), (7, 15, 13), (5, 21, 19), (16, 21, 19), (3, 5, 7), (5, 16, 19), (7, 8, 13)])
    ang = 60 if c * c == a * a + b * b - a * b else 120
    return NUM(f'สามเหลี่ยม ABC มี a = {a}, b = {b} และมุม C = {ang}° ด้าน c ยาวเท่าใด', c,
               ol('c² = a² + b² − 2ab cos C', f'= {a*a} + {b*b} − 2({a})({b})({fr(1,2) if ang==60 else "−" + fr(1,2)})', f'= {c*c} → c = {c}'))

def tri_area(rng, mc):
    a, b = R(rng, 2, 14), R(rng, 2, 14)
    return MCN(mc, f'สามเหลี่ยมมีด้านยาว {a} และ {b} หน่วย มุมระหว่างสองด้านนี้เท่ากับ 30° มีพื้นที่กี่ตารางหน่วย', Fr(a * b, 4),
               ol(f'พื้นที่ = {fr(1,2)}ab sin C = {fr(1,2)}({a})({b})({fr(1,2)})', f'= {fr(Fr(a*b,4))}'), extra=[Fr(a * b, 2), a * b])

def rad(rng, mc):
    p, q = rng.choice([(1, 6), (1, 4), (1, 3), (2, 3), (3, 4), (5, 6), (7, 6), (5, 4), (4, 3), (5, 3), (7, 4), (11, 6), (1, 12), (5, 12)])
    return NUM(f'มุม {fr(f"{p if p>1 else ""}π", q)} เรเดียน เท่ากับกี่องศา', Fr(180 * p, q), ol(f'π เรเดียน = 180°', f'{fr(f"{p if p>1 else ""}π", q)} = {fr(180*p, q)} = {num(Fr(180*p,q))}°'), u='องศา')

def period(rng, mc):
    k = R(rng, 2, 8); f = rng.choice(['sin', 'cos', 'tan'])
    base = 'π' if f == 'tan' else '2π'
    v = Fr(1 if f == 'tan' else 2, k)
    show = lambda x: fr(f'{x.numerator if x.numerator>1 else ""}π', x.denominator) if x.denominator > 1 else f'{x.numerator if x.numerator>1 else ""}π'
    corr = show(v)
    wr = [show(v * 2), show(v / 2), show(Fr(k)), show(Fr(k, 2)), show(v * 4), show(v * 3), show(v / 3), show(Fr(2 * k))]
    return mc(f'คาบของฟังก์ชัน y = {f} {k}x เท่ากับข้อใด', corr, wr, ol(f'คาบของ {f} x คือ {base}', f'คาบของ {f} kx = {base} ÷ k = {corr}'))

# ---------- a1-seq ----------
def ar_nth(rng, mc):
    a, d, n = R(rng, -10, 20), rng.choice([2, 3, 4, 5, 7, -3, -4]), R(rng, 15, 60)
    return MCN(mc, f'ลำดับเลขคณิต {num(a)}, {num(a+d)}, {num(a+2*d)}, … พจน์ที่ {n} คือเท่าใด', a + (n - 1) * d,
               ol(f'a₁ = {num(a)}, d = {num(d)}', f'a<sub>{n}</sub> = {num(a)} + {n-1}({num(d)}) = {num(a+(n-1)*d)}'), extra=[a + n * d])

def ge_nth(rng, mc):
    a, r, n = R(rng, 1, 5), rng.choice([2, 3, -2]), R(rng, 5, 8)
    return MCN(mc, f'ลำดับเรขาคณิต {a}, {num(a*r)}, {num(a*r*r)}, … พจน์ที่ {n} คือเท่าใด', a * r**(n - 1),
               ol(f'a₁ = {a}, r = {num(r)}', f'a<sub>{n}</sub> = {a}({num(r)})<sup>{n-1}</sup> = {num(a*r**(n-1))}'), extra=[a * r**n, a * r**(n - 2)])

def ar_sum(rng, mc):
    a, d, n = R(rng, 1, 10), R(rng, 2, 6), R(rng, 10, 30)
    S = n * (2 * a + (n - 1) * d) // 2
    return MCN(mc, f'ผลบวก {n} พจน์แรกของอนุกรม {a} + {a+d} + {a+2*d} + … เท่ากับเท่าใด', S,
               ol(f'S<sub>n</sub> = {fr("n","2")}[2a₁ + (n − 1)d]', f'= {fr(n,2)}[2({a}) + {n-1}({d})] = {num(S)}'), extra=[S + a, S - a + d])

def inf_geo(rng, mc):
    a = R(rng, 2, 20); r = rng.choice([Fr(1, 2), Fr(1, 3), Fr(-1, 2), Fr(2, 3), Fr(1, 4), Fr(-1, 3)])
    S = a / (1 - r)
    terms = [Fr(a), a * r, a * r * r]
    ser = fr(terms[0]) + ''.join((' − ' + fr(-t)) if t < 0 else (' + ' + fr(t)) for t in terms[1:])
    return MCN(mc, f'อนุกรมเรขาคณิตอนันต์ {ser} + … มีผลบวกเท่าใด', S,
               ol(f'a₁ = {a}, r = {fr(r)} (|r| < 1)', f'S<sub>∞</sub> = {fr("a₁","1 − r")} = {fr(a)} ÷ {fr(1-r)} = {fr(S)}'), extra=[a / (1 + r), a * r / (1 - r)])

def sq_sum(rng, mc):
    n = R(rng, 5, 20); v = n * (n + 1) * (2 * n + 1) // 6
    return MCN(mc, f'1² + 2² + 3² + … + {n}² มีค่าเท่าใด', v, ol(f'Σk² = {fr("n(n + 1)(2n + 1)", 6)}', f'= {fr(f"{n}({n+1})({2*n+1})", 6)} = {num(v)}'), extra=[n * (n + 1) // 2, v + n * n])

def two_terms(rng, mc):
    a, d = R(rng, -5, 10), R(rng, 2, 6); p, q, k = R(rng, 3, 6), R(rng, 8, 14), R(rng, 18, 40)
    t = lambda n: a + (n - 1) * d
    return MCN(mc, f'ลำดับเลขคณิตมี a<sub>{p}</sub> = {num(t(p))} และ a<sub>{q}</sub> = {num(t(q))} แล้ว a<sub>{k}</sub> เท่ากับเท่าใด', t(k),
               ol(f'a<sub>{q}</sub> − a<sub>{p}</sub> = {q-p}d = {t(q)-t(p)} → d = {d}', f'a₁ = {num(t(p))} − {p-1}({d}) = {num(a)}', f'a<sub>{k}</sub> = {num(a)} + {k-1}({d}) = {num(t(k))}'))

# ---------- a1-challenge ----------
def ab_poly(rng, mc):
    a, b = 3 * R(rng, -2, 3), R(rng, -4, 6)
    if a == 0: a = 3
    return NUM(f'ถ้า f(x) = ax² + bx มี f′(1) = {2*a+b} และ ∫<sub>0</sub><sup>2</sup> f(x) dx = {num(Fr(8*a,3)+2*b)} แล้ว a + b เท่ากับเท่าใด', a + b,
               ol(f'f′(1) = 2a + b = {2*a+b}', f'∫<sub>0</sub><sup>2</sup> (ax² + bx) dx = {fr("8a",3)} + 2b = {num(Fr(8*a,3)+2*b)}', f'แก้ระบบสมการได้ a = {a}, b = {b}', f'a + b = {a+b}'),
               h='สร้างสมการ 2 สมการจากเงื่อนไขทั้งสอง')

def coef(rng, mc):
    n, k, c = R(rng, 4, 8), 0, rng.choice([1, 2, 3])
    k = R(rng, 1, n - 1)
    v = math.comb(n, k) * c**k
    return NUM(f'สัมประสิทธิ์ของ x<sup>{k}</sup> ในการกระจาย ({c if c>1 else ""}x + 1)<sup>{n}</sup> เท่ากับเท่าใด', v,
               ol(f'พจน์ที่มี x<sup>{k}</sup> คือ C({n}, {k})({c if c>1 else ""}x)<sup>{k}</sup>', f'สัมประสิทธิ์ = {math.comb(n,k)} × {c}<sup>{k}</sup> = {num(v)}'))

def det_log(rng, mc):
    a, b, c, d = R(rng, 2, 6), R(rng, 1, 5), R(rng, 1, 5), R(rng, 2, 5)
    v = a * d - b * c
    return MCN(mc, f'det {M(f"log<sub>2</sub>{2**a} {b};{c} log<sub>3</sub>{3**d}")} มีค่าเท่าใด', v, ol(f'log<sub>2</sub>{2**a} = {a}, log<sub>3</sub>{3**d} = {d}', f'det = {a}({d}) − {b}({c}) = {v}'))

def ap_count(rng, mc):
    a, d = R(rng, 2, 20), R(rng, 3, 9); n = R(rng, 20, 80); last = a + (n - 1) * d
    return NUM(f'ลำดับเลขคณิต {a}, {a+d}, {a+2*d}, …, {last} มีกี่พจน์', n, ol(f'{last} = {a} + (n − 1)({d})', f'n − 1 = {(last-a)//d} → n = {n}'), u='พจน์')

TOPICS = {
    'a1-explog':    [log_eq, exp_quad, log_vals, exp_eq, log_rule, change_base, domain],
    'a1-calc':      [deriv_at, lim0, integ, rel_min, area_par, lim_inf, tangent, crit_sum],
    'a1-vec':       [vmag, dot, cmod, one_i, perp, ipow, para_area, cmul],
    'a1-mat':       [det2, detk, detinv, det3, matmul, singular],
    'a1-stat':      [atleast, zscore, sd_data, binom, word_arr, npr, no_replace, combined_mean],
    'a1-trig':      [trig_quad, trig_tri, sin2x, cos_law, tri_area, rad, period],
    'a1-seq':       [ar_nth, ge_nth, ar_sum, inf_geo, sq_sum, two_terms],
    'a1-challenge': [ab_poly, coef, det_log, ap_count, binom, exp_quad, sin2x, rel_min],
}
NEW = {'a1-trig': ('alevel-m1', 'math', 'ตรีโกณมิติ'), 'a1-seq': ('alevel-m1', 'math', 'ลำดับและอนุกรม')}
NOPT = 5
