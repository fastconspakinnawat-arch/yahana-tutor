"""A-Level คณิตศาสตร์ประยุกต์ 2 (สายศิลป์)"""
from core import *
from bank_a1 import MCN, ar_nth, ge_nth, ar_sum, inf_geo, two_terms, zscore, word_arr, poly
import math
R = lambda rng, a, b: rng.randint(a, b)

# ---------- a2-real ----------
def abs_lt(rng, mc):
    a, b = R(rng, -5, 8), R(rng, 1, 7)
    L, U = num(a - b), num(a + b)
    A = f'x − {a}' if a >= 0 else f'x + {-a}'
    return mc(f'เซตคำตอบของอสมการ |{A}| < {b} คือข้อใด', f'({L}, {U})', [f'[{L}, {U}]', f'(−∞, {L}) ∪ ({U}, ∞)', f'({num(-b)}, {b})', f'({num(a-b-1)}, {num(a+b+1)})', f'({L}, ∞)'],
              ol(f'−{b} < {A} < {b}', f'{L} < x < {U}'))

def quad_le(rng, mc):
    p, q = sorted(rng.sample(range(-6, 9), 2))
    B, C = -(p + q), p * q
    expr = 'x²' + (f' {"−" if B<0 else "+"} {abs(B) if abs(B)!=1 else ""}x' if B else '') + (f' {"−" if C<0 else "+"} {abs(C)}' if C else '')
    P, Q = num(p), num(q)
    if rng.random() < .5:
        return mc(f'เซตคำตอบของอสมการ {expr} ≤ 0 คือข้อใด', f'[{P}, {Q}]', [f'({P}, {Q})', f'(−∞, {P}] ∪ [{Q}, ∞)', f'[{num(-q)}, {num(-p)}]', f'(−∞, {P}) ∪ ({Q}, ∞)', 'ℝ'],
                  ol(f'{expr} = (x − ({P}))(x − ({Q})) ≤ 0', f'ค่าไม่เป็นบวกเมื่อ x อยู่ระหว่างราก: {P} ≤ x ≤ {Q}'))
    return mc(f'เซตคำตอบของอสมการ {expr} > 0 คือข้อใด', f'(−∞, {P}) ∪ ({Q}, ∞)', [f'({P}, {Q})', f'[{P}, {Q}]', f'(−∞, {P}] ∪ [{Q}, ∞)', f'({num(-q)}, {num(-p)})', 'ℝ'],
              ol(f'{expr} = (x − ({P}))(x − ({Q})) > 0', f'ค่าเป็นบวกเมื่อ x อยู่นอกช่วงระหว่างราก: x < {P} หรือ x > {Q}'))

def abs_count(rng, mc):
    a, b = R(rng, 1, 9), R(rng, 2, 9)
    lo, hi = Fr(a - b, 2), Fr(a + b, 2)
    cnt = math.floor(hi) - math.ceil(lo) + 1
    return NUM(f'จำนวนเต็ม x ที่สอดคล้องกับอสมการ |2x − {a}| ≤ {b} มีทั้งหมดกี่จำนวน', cnt,
               ol(f'−{b} ≤ 2x − {a} ≤ {b} → {num(a-b)} ≤ 2x ≤ {a+b}', f'{num(lo)} ≤ x ≤ {num(hi)}', f'จำนวนเต็มตั้งแต่ {math.ceil(lo)} ถึง {math.floor(hi)} มี {cnt} จำนวน'), u='จำนวน')

def lin_ineq(rng, mc):
    a, b, c = R(rng, 2, 7), R(rng, -9, 9), R(rng, -10, 30)
    bound = Fr(c - b, a); x = math.floor(bound) + 1
    return NUM(f'จำนวนเต็มที่น้อยที่สุดที่สอดคล้องกับอสมการ {a}x {"+" if b>=0 else "−"} {abs(b)} > {c} คือเท่าใด', x,
               ol(f'{a}x > {c - b}', f'x > {fr(bound) if bound.denominator>1 else num(bound)}', f'จำนวนเต็มที่น้อยที่สุดคือ {x}'))

def abs_eq(rng, mc):
    a, b = R(rng, -8, 10), R(rng, 1, 9)
    return NUM(f'ผลบวกของคำตอบทั้งหมดของสมการ |x {"−" if a>=0 else "+"} {abs(a)}| = {b}', 2 * a,
               ol(f'x {"−" if a>=0 else "+"} {abs(a)} = {b} หรือ −{b}', f'x = {a+b} หรือ {a-b}', f'ผลบวก = {2*a}'))

def int_between(rng, mc):
    m, n = sorted(rng.sample(range(-5, 12), 2))
    if n - m < 2: n = m + 4
    s = sum(range(m + 1, n))
    B, C = -(m + n), m * n
    expr = 'x²' + (f' {"−" if B<0 else "+"} {abs(B)}x' if B else '') + (f' {"−" if C<0 else "+"} {abs(C)}' if C else '')
    return NUM(f'ผลบวกของจำนวนเต็มทั้งหมดที่สอดคล้องกับอสมการ {expr} < 0', s,
               ol(f'(x − ({m}))(x − ({n})) < 0 → {m} < x < {n}', f'จำนวนเต็ม: {", ".join(map(str, range(m+1, n)))}', f'ผลบวก = {s}'))

# ---------- a2-fin ----------
def compound(rng, mc):
    P, r, n = rng.choice([10000, 20000, 50000, 100000, 8000]), rng.choice([2, 4, 5, 10]), R(rng, 2, 3)
    A = P * Fr(100 + r, 100)**n
    return NUM(f'ฝากเงิน {num(P)} บาท ดอกเบี้ยทบต้นร้อยละ {r} ต่อปี เมื่อครบ {n} ปี มีเงินรวมกี่บาท', A,
               ol(f'S = P(1 + r)<sup>n</sup> = {num(P)}({num(Fr(100+r,100))})<sup>{n}</sup>', f'= {num(A)} บาท'), u='บาท')

def simple(rng, mc):
    P, r, t = rng.choice([5000, 10000, 20000, 40000, 60000]), rng.choice([2, 3, 4, 5, 6, Fr(5, 2)]), R(rng, 2, 6)
    I = P * Fr(r) / 100 * t
    return NUM(f'ฝากเงิน {num(P)} บาท ดอกเบี้ยเชิงเดียวร้อยละ {num(r)} ต่อปี เป็นเวลา {t} ปี ได้ดอกเบี้ยกี่บาท', I,
               ol(f'I = Prt = {num(P)} × {num(Fr(r)/100)} × {t}', f'= {num(I)} บาท'), u='บาท')

def semi(rng, mc):
    P, r, y = rng.choice([10000, 20000, 50000]), rng.choice([4, 6, 8, 10]), R(rng, 1, 2)
    k = 2 * y; A = P * Fr(200 + r, 200)**k
    return NUM(f'ฝากเงิน {num(P)} บาท ดอกเบี้ยร้อยละ {r} ต่อปี คิดทบต้นทุกครึ่งปี ครบ {y} ปีมีเงินรวมกี่บาท', A,
               ol(f'อัตราต่องวด = {r} ÷ 2 = {num(Fr(r,2))}%, จำนวนงวด = {k}', f'{num(P)}({num(Fr(200+r,200))})<sup>{k}</sup> = {num(A)} บาท'), u='บาท', h='ทบต้นทุกครึ่งปี: อัตราต่องวด = r/2, จำนวนงวด = 2n')

def pv(rng, mc):
    P, r, n = rng.choice([10000, 20000, 40000, 100000]), rng.choice([5, 10, 20]), R(rng, 2, 3)
    F = P * Fr(100 + r, 100)**n
    return NUM(f'ต้องการมีเงิน {num(F)} บาท ในอีก {n} ปี ด้วยดอกเบี้ยทบต้นร้อยละ {r} ต่อปี ต้องฝากเงินตอนนี้กี่บาท (มูลค่าปัจจุบัน)', P,
               ol(f'P = {fr("S","(1 + r)<sup>n</sup>")} = {num(F)} ÷ ({num(Fr(100+r,100))})<sup>{n}</sup>', f'= {num(P)} บาท'), u='บาท')

def monthly(rng, mc):
    P, r, m = rng.choice([12000, 24000, 30000, 60000]), rng.choice([2, 3, 4, 5, 6]), rng.choice([3, 4, 6, 8, 9])
    I = P * Fr(r, 100) * Fr(m, 12)
    return NUM(f'ฝากเงิน {num(P)} บาท ดอกเบี้ยเชิงเดียวร้อยละ {r} ต่อปี เป็นเวลา {m} เดือน ได้ดอกเบี้ยกี่บาท', I,
               ol(f'เวลา = {fr(m,12)} ปี', f'I = {num(P)} × {num(Fr(r,100))} × {fr(m,12)} = {num(I)} บาท'), u='บาท')

def effective(rng, mc):
    r = rng.choice([4, 6, 8, 10, 12, 20])
    e = (Fr(200 + r, 200)**2 - 1) * 100
    return NUM(f'ดอกเบี้ยร้อยละ {r} ต่อปี คิดทบต้นทุกครึ่งปี เทียบเท่าอัตราดอกเบี้ยที่แท้จริงร้อยละเท่าใดต่อปี', e,
               ol(f'(1 + {num(Fr(r,200))})² − 1 = {num(Fr(200+r,200)**2 - 1)}', f'คิดเป็นร้อยละ {num(e)}'), h='คิดว่าเงิน 1 บาทโตเป็นเท่าไรใน 1 ปี')

def annuity(rng, mc):
    A, n = rng.choice([1000, 2000, 5000, 10000]), R(rng, 2, 3); r = rng.choice([10, 20])
    g = Fr(100 + r, 100)
    S = A * sum(g**k for k in range(n))
    return NUM(f'ฝากเงินสิ้นปีละ {num(A)} บาท เป็นเวลา {n} ปี ดอกเบี้ยทบต้นร้อยละ {r} ต่อปี ณ สิ้นปีที่ {n} (หลังฝากครั้งสุดท้าย) มีเงินรวมกี่บาท', S,
               ol(*[f'เงินงวดที่ {k+1} โตเป็น {num(A)}({num(g)})<sup>{n-1-k}</sup> = {num(A*g**(n-1-k))}' for k in range(n)], f'รวม = {num(S)} บาท'), u='บาท')

# ---------- a2-stat ----------
def q1(rng, mc):
    n = rng.choice([7, 11, 15, 9]); xs = sorted(rng.sample(range(1, 60), n))
    pos = Fr(n + 1, 4)
    i = math.floor(pos)
    v = xs[i - 1] + (pos - i) * (xs[i] - xs[i - 1])
    sh = xs[:]; rng.shuffle(sh)
    return NUM(f'ข้อมูล {", ".join(map(str, sh))} มีควอร์ไทล์ที่ 1 เท่ากับเท่าใด (ใช้ตำแหน่ง {fr("n + 1",4)})', v,
               ol(f'เรียง: {", ".join(map(str, xs))}', f'ตำแหน่ง Q₁ = {fr(n+1,4)} = {num(pos)}', f'Q₁ = {num(v)}'))

def transform(rng, mc):
    m, s, k = R(rng, 10, 50), R(rng, 2, 9), R(rng, 2, 5)
    if rng.random() < .5:
        c = R(rng, 3, 10)
        corr = f'ค่าเฉลี่ยเป็น {m+c} และส่วนเบี่ยงเบนมาตรฐานเป็น {s}'
        wr = [f'ค่าเฉลี่ยเป็น {m+c} และส่วนเบี่ยงเบนมาตรฐานเป็น {s+c}', f'ค่าเฉลี่ยเป็น {m} และส่วนเบี่ยงเบนมาตรฐานเป็น {s+c}', f'ค่าเฉลี่ยเป็น {m} และส่วนเบี่ยงเบนมาตรฐานเป็น {s}', f'ค่าเฉลี่ยเป็น {m*c} และส่วนเบี่ยงเบนมาตรฐานเป็น {s}', f'ค่าเฉลี่ยเป็น {m+c} และส่วนเบี่ยงเบนมาตรฐานเป็น {s*c}']
        return mc(f'ข้อมูลชุดหนึ่งมีค่าเฉลี่ย {m} ส่วนเบี่ยงเบนมาตรฐาน {s} ถ้านำ {c} ไปบวกข้อมูลทุกค่า ข้อใดถูกต้อง', corr, wr,
                  ol(f'บวกค่าคงที่ → ค่าเฉลี่ยเพิ่มตาม: {m} + {c} = {m+c}', 'การกระจายไม่เปลี่ยน → ส่วนเบี่ยงเบนมาตรฐานเท่าเดิม'))
    corr = f'ค่าเฉลี่ยเป็น {m*k} และส่วนเบี่ยงเบนมาตรฐานเป็น {s*k}'
    wr = [f'ค่าเฉลี่ยเป็น {m*k} และส่วนเบี่ยงเบนมาตรฐานเป็น {s}', f'ค่าเฉลี่ยเป็น {m} และส่วนเบี่ยงเบนมาตรฐานเป็น {s*k}', f'ค่าเฉลี่ยเป็น {m*k} และส่วนเบี่ยงเบนมาตรฐานเป็น {s*k*k}', f'ค่าเฉลี่ยเป็น {m+k} และส่วนเบี่ยงเบนมาตรฐานเป็น {s}', f'ค่าเฉลี่ยเป็น {m+k} และส่วนเบี่ยงเบนมาตรฐานเป็น {s*k}']
    return mc(f'ข้อมูลชุดหนึ่งมีค่าเฉลี่ย {m} ส่วนเบี่ยงเบนมาตรฐาน {s} ถ้านำ {k} ไปคูณข้อมูลทุกค่า ข้อใดถูกต้อง', corr, wr,
              ol(f'คูณด้วยค่าคงที่ k → ค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานถูกคูณด้วย |k|', f'ค่าเฉลี่ย {m*k}, ส่วนเบี่ยงเบนมาตรฐาน {s*k} (ความแปรปรวนถูกคูณด้วย k² = {k*k})'))

CARDS = [('โพดำหรือ King', 16), ('ไพ่หน้าคน (J, Q, K)', 12), ('ไพ่สีแดง', 26), ('King หรือ Queen', 8), ('ไพ่โพแดงหรือไพ่ A', 16), ('ไพ่สีดำที่เป็นตัวเลข 2–10', 18), ('ไพ่ข้าวหลามตัด', 13)]
def cards(rng, mc):
    d, c = rng.choice(CARDS); p = Fr(c, 52)
    return MCN(mc, f'สุ่มไพ่ 1 ใบจากสำรับมาตรฐาน 52 ใบ ความน่าจะเป็นที่ได้{d}', p,
               ol(f'นับไพ่ที่เข้าเงื่อนไข (ระวังนับซ้ำ) ได้ {c} ใบ', f'P = {fr(c,52)} = {fr(p)}'), extra=[Fr(c + 1, 52), Fr(c - 1, 52), Fr(c, 13) if c < 13 else Fr(1, 52)], prob=True)

def mmm(rng, mc):
    xs = [R(rng, 1, 20) for _ in range(7)]; s = sorted(xs)
    k = rng.choice(['ค่าเฉลี่ย', 'มัธยฐาน', 'พิสัย'])
    if k == 'ค่าเฉลี่ย':
        v = Fr(sum(xs), 7)
        if Fr(v * 100).denominator != 1: return mmm(rng, mc)
        return NUM(f'ค่าเฉลี่ยเลขคณิตของ {", ".join(map(str, xs))} เท่ากับเท่าใด', v, ol(f'ผลรวม {sum(xs)} ÷ 7 = {num(v)}'))
    if k == 'มัธยฐาน':
        return NUM(f'มัธยฐานของ {", ".join(map(str, xs))} เท่ากับเท่าใด', s[3], ol(f'เรียง: {", ".join(map(str, s))}', f'ตัวที่ 4 คือ {s[3]}'))
    return NUM(f'พิสัยของ {", ".join(map(str, xs))} เท่ากับเท่าใด', s[-1] - s[0], ol(f'{s[-1]} − {s[0]} = {s[-1]-s[0]}'))

def weighted(rng, mc):
    ws = [R(rng, 1, 4) for _ in range(3)]; sc = [R(rng, 40, 95) for _ in range(3)]
    v = Fr(sum(w * s for w, s in zip(ws, sc)), sum(ws))
    if Fr(v * 100).denominator != 1: return weighted(rng, mc)
    return NUM(f'นักเรียนได้คะแนนวิชา A, B, C เป็น {sc[0]}, {sc[1]}, {sc[2]} โดยวิชาทั้งสามมีหน่วยกิต {ws[0]}, {ws[1]}, {ws[2]} ตามลำดับ ค่าเฉลี่ยถ่วงน้ำหนักเท่ากับเท่าใด', v,
               ol(f'Σwx = {" + ".join(f"{w}×{s}" for w, s in zip(ws, sc))} = {sum(w*s for w, s in zip(ws, sc))}', f'Σw = {sum(ws)}', f'ค่าเฉลี่ย = {num(v)}'))

# ---------- a2-func ----------
def f_lin(rng, mc):
    a, b, k = R(rng, -5, 7), R(rng, -9, 9), R(rng, -5, 8)
    if a == 0: a = 3
    return MCN(mc, f'ถ้า f(x) = {poly([(a,1),(b,0)])} แล้ว f({k}) มีค่าเท่าใด', a * k + b, ol(f'f({k}) = {a}({k}) {"+" if b>=0 else "−"} {abs(b)} = {a*k+b}'))

def compo(rng, mc):
    a, b, c, k = R(rng, 1, 4), R(rng, -5, 5), R(rng, -4, 6), R(rng, -3, 4)
    g = k + c; v = a * g * g + b
    return MCN(mc, f'f(x) = {poly([(a,2),(b,0)])} และ g(x) = {poly([(1,1),(c,0)])} แล้ว (f ∘ g)({k}) เท่ากับเท่าใด', v,
               ol(f'g({k}) = {g}', f'f({g}) = {a}({g})² {"+" if b>=0 else "−"} {abs(b)} = {v}'), extra=[a * k * k + b + c])

def inv_val(rng, mc):
    a, b, y = R(rng, 2, 6), R(rng, -9, 9), R(rng, -3, 6)
    k = a * y + b
    return NUM(f'f(x) = {poly([(a,1),(b,0)])} แล้ว f<sup>−1</sup>({k}) มีค่าเท่าใด', y, ol(f'หา x ที่ทำให้ f(x) = {k}', f'{a}x {"+" if b>=0 else "−"} {abs(b)} = {k} → x = {y}'))

def expo_simpl(rng, mc):
    b, m, n, p = rng.choice([2, 3]), R(rng, 2, 4), R(rng, 2, 3), 0
    p = m * n - R(rng, 1, 3)
    v = b**(m * n - p)
    return MCN(mc, f'{fr(f"({b}<sup>{m}</sup>)<sup>{n}</sup>", f"{b}<sup>{p}</sup>")} มีค่าเท่าใด', v,
               ol(f'({b}<sup>{m}</sup>)<sup>{n}</sup> = {b}<sup>{m*n}</sup>', f'{b}<sup>{m*n} − {p}</sup> = {b}<sup>{m*n-p}</sup> = {v}'), extra=[b**(m + n - p) if m + n > p else 1, b**(m * n)])

def vertex(rng, mc):
    h, c = R(rng, -5, 6), R(rng, -10, 20)
    return MCN(mc, f'ค่าต่ำสุดของฟังก์ชัน f(x) = {poly([(1,2),(-2*h,1),(c,0)])} เท่ากับเท่าใด', c - h * h,
               ol(f'ทำเป็นกำลังสองสมบูรณ์: (x − ({h}))² + {c - h*h}', f'ค่าต่ำสุด = {c - h*h} เมื่อ x = {h}'), extra=[c, h, -h * h])

def intercepts(rng, mc):
    p, q = rng.sample(range(-6, 9), 2)
    return MCN(mc, f'กราฟ y = {poly([(1,2),(-(p+q),1),(p*q,0)])} ตัดแกน X ที่จุด (a, 0) และ (b, 0) แล้ว a + b เท่ากับเท่าใด', p + q,
               ol(f'แยกตัวประกอบ: (x − ({p}))(x − ({q})) = 0', f'a + b = {p} + ({q}) = {p+q}'), extra=[p * q, -(p + q)])

def solve_exp(rng, mc):
    b, x = rng.choice([2, 3, 5]), R(rng, 2, 6); c = R(rng, -2, 3)
    return MCN(mc, f'ถ้า {b}<sup>x {"+" if c>=0 else "−"} {abs(c)}</sup> = {b**(x+c) if x + c >= 0 else fr(1, b**(-(x+c)))} แล้ว x เท่ากับเท่าใด', x,
               ol(f'{b**(x+c) if x + c >= 0 else fr(1, b**(-(x+c)))} = {b}<sup>{x+c}</sup>', f'x {"+" if c>=0 else "−"} {abs(c)} = {x+c} → x = {x}'))

# ---------- a2-count ----------
def menu(rng, mc):
    a, b, c = R(rng, 2, 6), R(rng, 2, 6), R(rng, 2, 5)
    return MCN(mc, f'ร้านอาหารมีอาหารคาว {a} อย่าง ของหวาน {b} อย่าง และเครื่องดื่ม {c} อย่าง ถ้าสั่งอย่างละ 1 รายการ จะสั่งได้กี่แบบ', a * b * c,
               ol('ใช้หลักการคูณ', f'{a} × {b} × {c} = {a*b*c}'), extra=[a + b + c])

def fact_arr(rng, mc):
    n = R(rng, 4, 7)
    return MCN(mc, f'จัดหนังสือที่แตกต่างกัน {n} เล่มเรียงบนชั้นเป็นแถวเดียว ได้กี่วิธี', math.factorial(n), ol(f'{n}! = {math.factorial(n)}'), extra=[math.factorial(n - 1), n * n])

def choose(rng, mc):
    n, k = R(rng, 6, 12), R(rng, 2, 4)
    return MCN(mc, f'เลือกนักเรียน {k} คนจาก {n} คน ไปเป็นตัวแทน (ไม่สนใจลำดับ) ได้กี่วิธี', math.comb(n, k),
               ol(f'C({n}, {k}) = {fr(f"{n}!", f"{k}! {n-k}!")} = {math.comb(n,k)}'), extra=[math.perm(n, k)])

def dice_sum(rng, mc):
    s = R(rng, 2, 12); c = 6 - abs(7 - s); p = Fr(c, 36)
    return MCN(mc, f'ทอยลูกเต๋า 2 ลูก ความน่าจะเป็นที่ผลรวมแต้มเท่ากับ {s}', p, ol(f'จำนวนคู่ที่รวมได้ {s} มี {c} แบบ จาก 36 แบบ', f'P = {fr(p)}'), extra=[Fr(c + 1, 36), Fr(1, 6), Fr(1, 12)], prob=True)

def at_least_head(rng, mc):
    n = R(rng, 2, 6); p = 1 - Fr(1, 2**n)
    return MCN(mc, f'โยนเหรียญ {n} เหรียญ ความน่าจะเป็นที่ขึ้นหัวอย่างน้อย 1 เหรียญ', p, ol(f'P(ไม่มีหัวเลย) = {fr(1, 2**n)}', f'P(อย่างน้อย 1 หัว) = 1 − {fr(1, 2**n)} = {fr(p)}'), extra=[Fr(1, 2**n), Fr(1, 2), Fr(n, 2**n)], prob=True)

def together(rng, mc):
    n = R(rng, 4, 7)
    v = 2 * math.factorial(n - 1)
    return MCN(mc, f'จัดคน {n} คนนั่งเรียงแถว โดย ก และ ข ต้องนั่งติดกัน ได้กี่วิธี', v,
               ol(f'มัด ก-ข เป็น 1 หน่วย → จัด {n-1} หน่วยได้ {n-1}! = {math.factorial(n-1)}', f'ก-ข สลับกันได้ 2 แบบ', f'รวม {v} วิธี'), extra=[math.factorial(n - 1), math.factorial(n)])

TOPICS = {
    'a2-real':  [abs_lt, quad_le, abs_count, lin_ineq, abs_eq, int_between],
    'a2-fin':   [compound, simple, semi, pv, monthly, effective, annuity],
    'a2-seq':   [ar_nth, ge_nth, ar_sum, inf_geo, two_terms],
    'a2-stat':  [q1, transform, cards, mmm, weighted, zscore],
    'a2-func':  [f_lin, compo, inv_val, expo_simpl, vertex, intercepts, solve_exp],
    'a2-count': [menu, fact_arr, choose, dice_sum, at_least_head, together, word_arr],
}
NEW = {'a2-func': ('alevel-m2', 'math', 'ฟังก์ชันและเลขยกกำลัง'), 'a2-count': ('alevel-m2', 'math', 'หลักการนับและความน่าจะเป็น')}
NOPT = 5
