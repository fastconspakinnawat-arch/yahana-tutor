"""เตรียมสอบเข้า ม.4"""
from core import *
import math
R = lambda rng, a, b: rng.randint(a, b)
TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (20, 21, 29), (9, 40, 41), (12, 16, 20), (15, 20, 25)]

def sgn(x, first=False):
    """format +x / −x term"""
    return (('−' if x < 0 else '') if first else (' − ' if x < 0 else ' + ')) + str(abs(x))

# ---------- e4-alg ----------
def sys_xy(rng, mc):
    x, y = R(rng, 2, 15), R(rng, 1, 12)
    return NUM(f'ถ้า x + y = {x+y} และ x − y = {num(x-y)} แล้ว xy มีค่าเท่าใด', x * y,
               ol(f'บวกสองสมการ: 2x = {2*x} → x = {x}', f'y = {x+y} − {x} = {y}', f'xy = {x*y}'))

def recip_sq(rng, mc):
    k = R(rng, 3, 9)
    return NUM(f'ถ้า x + {fr(1,"x")} = {k} แล้ว x² + {fr(1,"x²")} มีค่าเท่าใด', k * k - 2,
               ol(f'ยกกำลังสอง: x² + 2 + {fr(1,"x²")} = {k*k}', f'x² + {fr(1,"x²")} = {k*k} − 2 = {k*k-2}'), h='ยกกำลังสองทั้งสองข้าง')

def double_root(rng, mc):
    b = R(rng, 2, 14)
    return NUM(f'สมการ x² − {b}x + k = 0 มีคำตอบเป็นจำนวนจริงซ้ำกัน k มีค่าเท่าใด', Fr(b * b, 4),
               ol('มีรากซ้ำเมื่อ b² − 4ac = 0', f'({b})² − 4(1)(k) = 0 → k = {fr(b*b,4) if b%2 else b*b//4}' + (f' = {num(Fr(b*b,4))}' if b % 2 else '')))

def vieta_sq(rng, mc):
    r1, r2 = R(rng, -6, 9), R(rng, 1, 9)
    s, p = r1 + r2, r1 * r2
    return NUM(f'ถ้า a และ b เป็นคำตอบของสมการ x²{sgn(-s)}x{sgn(p)} = 0 แล้ว a² + b² มีค่าเท่าใด', s * s - 2 * p,
               ol(f'a + b = {s}, ab = {p}', f'a² + b² = (a + b)² − 2ab = {s*s} − ({2*p}) = {s*s-2*p}'), h='ใช้ผลบวกและผลคูณของราก')

def lin_eq(rng, mc):
    x = R(rng, -8, 12); a, b, c = R(rng, 2, 6), R(rng, 1, 9), R(rng, 1, 5)
    if a == c: a += 1
    d = a * (x - b) - c * x
    return NUM(f'ถ้า {a}(x − {b}) = {c}x{sgn(d)} แล้ว x มีค่าเท่าใด', x,
               ol(f'{a}x − {a*b} = {c}x{sgn(d)}', f'{a-c}x = {d + a*b}', f'x = {x}'))

def factor_mc(rng, mc):
    m, n = rng.sample([-7, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 8], 2)
    B, C = m + n, m * n
    f = lambda p, q: f'(x{sgn(p)})(x{sgn(q)})'
    if B == 0: return factor_mc(rng, mc)
    return mc(f'x²{sgn(B)}x{sgn(C)} แยกตัวประกอบได้ตรงกับข้อใด', f(m, n), [f(-m, -n), f(m, -n), f(-m, n), f(m + 1, n - 1), f(B, 1)],
              ol(f'หาสองจำนวนที่คูณกันได้ {num(C)} และบวกกันได้ {num(B)} คือ {num(m)} และ {num(n)}', f'x²{sgn(B)}x{sgn(C)} = {f(m,n)}'))

def ab_sq(rng, mc):
    s, p = R(rng, 3, 12), R(rng, 1, 20)
    return NUM(f'ถ้า a + b = {s} และ ab = {p} แล้ว a² + b² มีค่าเท่าใด', s * s - 2 * p,
               ol(f'(a + b)² = a² + 2ab + b²', f'a² + b² = {s}² − 2({p}) = {s*s-2*p}'))

def exp_laws(rng, mc):
    a, b, c = R(rng, 2, 9), R(rng, 1, 6), R(rng, 1, 5)
    n = a + 2 * b - 3 * c
    return NUM(f'ถ้า {fr(f"2<sup>{a}</sup> × 4<sup>{b}</sup>", f"8<sup>{c}</sup>")} = 2<sup>n</sup> แล้ว n มีค่าเท่าใด', n,
               ol(f'4<sup>{b}</sup> = 2<sup>{2*b}</sup>, 8<sup>{c}</sup> = 2<sup>{3*c}</sup>', f'n = {a} + {2*b} − {3*c} = {n}'), h='เขียนทุกตัวเป็นฐาน 2')

def cube_sum(rng, mc):
    s, p = R(rng, 2, 8), R(rng, 1, 10)
    return NUM(f'ถ้า a + b = {s} และ ab = {p} แล้ว a³ + b³ มีค่าเท่าใด', s**3 - 3 * p * s,
               ol('a³ + b³ = (a + b)³ − 3ab(a + b)', f'= {s**3} − 3({p})({s}) = {s**3 - 3*p*s}'))

# ---------- e4-geo ----------
def sim_area(rng, mc):
    a, b = rng.choice([(2, 3), (3, 5), (2, 5), (3, 4), (4, 5), (1, 3), (5, 7)]); k = R(rng, 1, 6)
    small = a * a * k
    return NUM(f'สามเหลี่ยมสองรูปคล้ายกัน อัตราส่วนความยาวด้านที่สมนัยกันเป็น {a} : {b} ถ้ารูปเล็กมีพื้นที่ {small} ตร.หน่วย รูปใหญ่มีพื้นที่กี่ตร.หน่วย', b * b * k,
               ol(f'อัตราส่วนพื้นที่ = {a}² : {b}² = {a*a} : {b*b}', f'พื้นที่รูปใหญ่ = {small} × {fr(b*b, a*a)} = {b*b*k}'), h='อัตราส่วนพื้นที่ = (อัตราส่วนด้าน)²')

def pyth_hyp(rng, mc):
    a, b, c = rng.choice(TRIPLES)
    if rng.random() < .5:
        return NUM(f'สามเหลี่ยมมุมฉากมีด้านประกอบมุมฉากยาว {a} และ {b} หน่วย ด้านตรงข้ามมุมฉากยาวกี่หน่วย', c,
                   ol(f'c² = {a}² + {b}² = {a*a+b*b}', f'c = {c}'))
    return NUM(f'บันไดยาว {c} เมตร พิงกำแพงตั้งฉาก เท้าบันไดห่างกำแพง {a} เมตร ปลายบันไดสูงจากพื้นกี่เมตร', b,
               ol(f'สูง² = {c}² − {a}² = {c*c-a*a}', f'สูง = {b} เมตร'), u='m')

def ladder30(rng, mc):
    L = 2 * R(rng, 2, 15)
    return NUM(f'บันไดยาว {L} m พิงกำแพง ทำมุม 30° กับพื้นราบ ปลายบันไดสูงจากพื้นกี่เมตร', L // 2,
               ol(f'สูง = {L} × sin 30°', f'= {L} × {fr(1,2)} = {L//2} m'), u='m')

SPECIAL = {('sin', 30): fr(1, 2), ('sin', 45): fr('√2', 2), ('sin', 60): fr('√3', 2), ('cos', 30): fr('√3', 2), ('cos', 45): fr('√2', 2),
           ('cos', 60): fr(1, 2), ('tan', 30): fr(1, '√3'), ('tan', 45): '1', ('tan', 60): '√3'}
def trig_val(rng, mc):
    f, a = rng.choice(list(SPECIAL))
    corr = SPECIAL[(f, a)]
    return mc(f'{f} {a}° มีค่าเท่าใด', corr, [v for v in [fr(1,2), fr('√2',2), fr('√3',2), fr(1,'√3'), '1', '√3', '2'] if v != corr][:: 1 if rng.random() < .5 else -1],
              ol('ใช้สามเหลี่ยม 30°-60°-90° (ด้าน 1 : √3 : 2) และ 45°-45°-90° (ด้าน 1 : 1 : √2)', f'{f} {a}° = {corr}'))

def trapezoid(rng, mc):
    a, b, h = R(rng, 3, 15), R(rng, 6, 25), 2 * R(rng, 2, 9)
    return NUM(f'สี่เหลี่ยมคางหมูมีด้านคู่ขนานยาว {a} ซม. และ {b} ซม. สูง {h} ซม. มีพื้นที่กี่ตารางเซนติเมตร', (a + b) * h // 2,
               ol(f'พื้นที่ = {fr(1,2)} × (ผลบวกด้านคู่ขนาน) × สูง', f'= {fr(1,2)} × ({a} + {b}) × {h} = {(a+b)*h//2} ตร.ซม.'), u='ตร.ซม.')

def cylinder(rng, mc):
    r, h = 7 * R(rng, 1, 3), R(rng, 2, 20)
    return NUM(f'ทรงกระบอกรัศมีฐาน {r} ซม. สูง {h} ซม. มีปริมาตรกี่ลูกบาศก์เซนติเมตร (ใช้ π ≈ {fr(22,7)})', Fr(22, 7) * r * r * h,
               ol(f'ปริมาตร = πr²h = {fr(22,7)} × {r}² × {h}', f'= {num(Fr(22,7)*r*r*h)} ลบ.ซม.'), u='ลบ.ซม.')

def sphere_cone(rng, mc):
    if rng.random() < .5:
        r = 3 * R(rng, 1, 4)
        k = Fr(4, 3) * r**3
        return NUM(f'ทรงกลมรัศมี {r} ซม. มีปริมาตร kπ ลูกบาศก์เซนติเมตร k มีค่าเท่าใด', k,
                   ol(f'ปริมาตรทรงกลม = {fr(4,3)}πr³', f'= {fr(4,3)} × {r}³ π = {num(k)}π', f'k = {num(k)}'))
    r, h = R(rng, 2, 9), 3 * R(rng, 1, 6)
    k = Fr(1, 3) * r * r * h
    return NUM(f'กรวยรัศมีฐาน {r} ซม. สูง {h} ซม. มีปริมาตร kπ ลูกบาศก์เซนติเมตร k มีค่าเท่าใด', k,
               ol(f'ปริมาตรกรวย = {fr(1,3)}πr²h', f'= {fr(1,3)} × {r}² × {h} π = {num(k)}π', f'k = {num(k)}'))

def inscribed(rng, mc):
    c = 2 * R(rng, 20, 85)
    if rng.random() < .5:
        return NUM(f'มุมที่จุดศูนย์กลางของวงกลมรองรับส่วนโค้ง AB มีขนาด {c}° มุมในส่วนโค้งของวงกลมที่รองรับส่วนโค้ง AB เดียวกันมีขนาดกี่องศา', c // 2,
                   ol('มุมในส่วนโค้ง = ครึ่งหนึ่งของมุมที่จุดศูนย์กลางที่รองรับส่วนโค้งเดียวกัน', f'= {c} ÷ 2 = {c//2}°'), u='องศา')
    a = R(rng, 50, 130)
    return NUM(f'ABCD เป็นรูปสี่เหลี่ยมแนบในวงกลม ถ้ามุม A = {a}° มุม C มีขนาดกี่องศา', 180 - a,
               ol('มุมตรงข้ามของรูปสี่เหลี่ยมแนบในวงกลมรวมกันได้ 180°', f'C = 180 − {a} = {180-a}°'), u='องศา')

# ---------- e4-ps ----------
def balls(rng, mc):
    r, b, g = R(rng, 1, 8), R(rng, 1, 8), R(rng, 0, 5); n = r + b + g
    p = Fr(r, n)
    desc = f'สีแดง {r} ลูก สีน้ำเงิน {b} ลูก' + (f' สีเขียว {g} ลูก' if g else '')
    wr = [fr(Fr(b, n)), fr(Fr(r, n - r)) if n - r else '0', fr(Fr(1, n)), fr(1 - p), fr(Fr(r, n + 1))]
    return mc(f'ในถุงมีลูกบอล{desc} หยิบ 1 ลูก ความน่าจะเป็นที่ได้สีแดงเท่ากับเท่าใด', fr(p), wr,
              ol(f'ลูกบอลทั้งหมด {n} ลูก สีแดง {r} ลูก', f'P = {fr(r,n)}' + (f' = {fr(p)}' if p != Fr(r, n) or math.gcd(r, n) > 1 else '')))

def mean_add(rng, mc):
    n, m = R(rng, 4, 9), R(rng, 8, 20); d = R(rng, 1, 3); x = (n + 1) * (m + d) - n * m
    return NUM(f'ข้อมูล {n} จำนวนมีค่าเฉลี่ย {m} เพิ่มข้อมูลอีก 1 จำนวน ค่าเฉลี่ยกลายเป็น {m+d} จำนวนที่เพิ่มคือเท่าใด', x,
               ol(f'ผลรวมเดิม = {n} × {m} = {n*m}', f'ผลรวมใหม่ = {n+1} × {m+d} = {(n+1)*(m+d)}', f'จำนวนที่เพิ่ม = {(n+1)*(m+d)} − {n*m} = {x}'))

def die1(rng, mc):
    kinds = [('เป็นจำนวนเฉพาะ', [2, 3, 5]), ('เป็นจำนวนคู่', [2, 4, 6]), ('มากกว่า 4', [5, 6]), ('หารด้วย 3 ลงตัว', [3, 6]), ('น้อยกว่า 5', [1, 2, 3, 4]), ('เป็นจำนวนประกอบ', [4, 6])]
    d, s = rng.choice(kinds); p = Fr(len(s), 6)
    return mc(f'ทอยลูกเต๋า 1 ลูก ความน่าจะเป็นที่แต้ม{d}เท่ากับเท่าใด', fr(p), [fr(x) for x in [Fr(1,6), Fr(1,3), Fr(1,2), Fr(2,3), Fr(5,6), Fr(1,4)] if x != p],
              ol(f'แต้มที่เข้าเงื่อนไข: {", ".join(map(str, s))} = {len(s)} แบบ', f'P = {fr(len(s),6)}' + (f' = {fr(p)}' if math.gcd(len(s), 6) > 1 else '')),
              h='1 ไม่ใช่จำนวนเฉพาะและไม่ใช่จำนวนประกอบ')

def dice2(rng, mc):
    s = R(rng, 3, 11); c = 6 - abs(7 - s); p = Fr(c, 36)
    pairs = [f'({i},{s-i})' for i in range(1, 7) if 1 <= s - i <= 6]
    return mc(f'ทอยลูกเต๋า 2 ลูก ความน่าจะเป็นที่ผลรวมแต้มเท่ากับ {s}', fr(p), [fr(x) for x in [Fr(c + 1, 36), Fr(c - 1, 36) if c > 1 else Fr(1, 12), Fr(1, 6), Fr(c, 12), Fr(1, 11), Fr(s, 36)] if x != p],
              ol(f'คู่ที่ได้ผลรวม {s}: {", ".join(pairs)} = {c} แบบ', f'ผลลัพธ์ทั้งหมด 36 แบบ', f'P = {fr(c,36)}' + (f' = {fr(p)}' if math.gcd(c, 36) > 1 else '')))

def median_l(rng, mc):
    n = rng.choice([5, 7, 6, 8]); xs = [R(rng, 1, 40) for _ in range(n)]; s = sorted(xs)
    med = Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)
    return NUM(f'มัธยฐานของข้อมูล {", ".join(map(str, xs))} คือเท่าใด', med,
               ol(f'เรียงข้อมูล: {", ".join(map(str, s))}', (f'ข้อมูล {n} ตัว ตัวกลางคือตัวที่ {(n+1)//2}' if n % 2 else f'ข้อมูล {n} ตัว มัธยฐาน = ค่าเฉลี่ยของตัวที่ {n//2} และ {n//2+1} = ({s[n//2-1]} + {s[n//2]}) ÷ 2'),
                  f'มัธยฐาน = {num(med)}'), h='เรียงข้อมูลจากน้อยไปมากก่อน')

def mean_l(rng, mc):
    n = R(rng, 5, 8); m = R(rng, 10, 40); xs = [m + R(rng, -8, 8) for _ in range(n - 1)]; xs.append(n * m - sum(xs))
    if xs[-1] < 0: return mean_l(rng, mc)
    rng.shuffle(xs)
    return NUM(f'ค่าเฉลี่ยเลขคณิตของ {", ".join(map(str, xs))} คือเท่าใด', m, ol(f'ผลรวม = {sum(xs)}, มี {n} จำนวน', f'ค่าเฉลี่ย = {sum(xs)} ÷ {n} = {m}'))

def range_mode(rng, mc):
    xs = [R(rng, 2, 30) for _ in range(6)]; mo = rng.choice(xs); xs += [mo, mo]; rng.shuffle(xs)
    if rng.random() < .5:
        return NUM(f'พิสัยของข้อมูล {", ".join(map(str, xs))} เท่ากับเท่าใด', max(xs) - min(xs), ol(f'พิสัย = ค่ามากสุด − ค่าน้อยสุด = {max(xs)} − {min(xs)} = {max(xs)-min(xs)}'))
    from collections import Counter
    c = Counter(xs).most_common()
    if len(c) > 1 and c[0][1] == c[1][1]: return range_mode(rng, mc)
    return NUM(f'ฐานนิยมของข้อมูล {", ".join(map(str, xs))} คือเท่าใด', c[0][0], ol(f'{c[0][0]} ปรากฏ {c[0][1]} ครั้ง มากที่สุด', f'ฐานนิยม = {c[0][0]}'))

# ---------- e4-phy ----------
def weight(rng, mc):
    m = R(rng, 2, 80)
    return NUM(f'วัตถุมวล {m} kg มีน้ำหนักกี่นิวตัน (g = 10 m/s²)', 10 * m, ol(f'W = mg = {m} × 10 = {10*m} N'), u='N')

def bill(rng, mc):
    P, h, d, rate = rng.choice([800, 1000, 1200, 1500, 2000, 2500]), R(rng, 2, 8), rng.choice([1, 30]), rng.choice([4, 5])
    E = Fr(P, 1000) * h * d
    return NUM(f'เครื่องใช้ไฟฟ้า {num(P)} W เปิดวันละ {h} ชั่วโมง เป็นเวลา {d} วัน ค่าไฟหน่วยละ {rate} บาท เสียค่าไฟกี่บาท', E * rate,
               ol(f'{num(P)} W = {num(Fr(P,1000))} kW', f'พลังงาน = {num(Fr(P,1000))} × {h} × {d} = {num(E)} หน่วย', f'ค่าไฟ = {num(E)} × {rate} = {num(E*rate)} บาท'), u='บาท')

def moment(rng, mc):
    m1, d1 = R(rng, 20, 50), R(rng, 1, 4); m2 = rng.choice([x for x in range(20, 80) if (m1 * d1 * 10) % x == 0 and x != m1])
    d2 = Fr(m1 * d1, m2)
    if d2 > 6 or Fr(d2 * 100).denominator != 1: return moment(rng, mc)
    return NUM(f'กระดานหกสมดุลในแนวระดับ เด็กมวล {m1} kg นั่งห่างจุดหมุน {d1} m เด็กอีกคนมวล {m2} kg ต้องนั่งห่างจุดหมุนอีกข้างกี่เมตร', d2,
               ol('โมเมนต์ทวน = โมเมนต์ตาม', f'{m1} × {d1} = {m2} × d', f'd = {m1*d1} ÷ {m2} = {num(d2)} m'), u='m')

def ohm(rng, mc):
    R_, I = R(rng, 2, 20), R(rng, 1, 6)
    k = rng.randrange(3)
    if k == 0: return NUM(f'ตัวต้านทาน {R_} Ω มีกระแสไหลผ่าน {I} A ความต่างศักย์คร่อมตัวต้านทานกี่โวลต์', R_ * I, ol(f'V = IR = {I} × {R_} = {R_*I} V'), u='V')
    if k == 1: return NUM(f'ต่อตัวต้านทาน {R_} Ω กับความต่างศักย์ {R_*I} V มีกระแสไหลกี่แอมแปร์', I, ol(f'I = V ÷ R = {R_*I} ÷ {R_} = {I} A'), u='A')
    return NUM(f'ความต่างศักย์ {R_*I} V ทำให้กระแส {I} A ไหลผ่านลวด ลวดมีความต้านทานกี่โอห์ม', R_, ol(f'R = V ÷ I = {R_*I} ÷ {I} = {R_} Ω'), u='Ω')

def density(rng, mc):
    rho, V = rng.choice([Fr(1, 2), Fr(4, 5), 1, Fr(27, 10), Fr(79, 10), Fr(113, 10), 2, 3]), 10 * R(rng, 1, 20)
    m = rho * V
    return NUM(f'วัตถุมวล {num(m)} g มีปริมาตร {V} cm³ มีความหนาแน่นกี่ g/cm³', rho, ol(f'ρ = m ÷ V = {num(m)} ÷ {V} = {num(rho)} g/cm³'), u='g/cm³')

def pressure(rng, mc):
    h = rng.choice([2, 3, 5, 8, 10, 12, 20, Fr(5, 2)])
    return NUM(f'ความดันเนื่องจากน้ำที่ความลึก {num(h)} m มีค่ากี่ปาสคาล (ρ<sub>น้ำ</sub> = 1000 kg/m³, g = 10 m/s²)', 10000 * h,
               ol('P = ρgh', f'= 1000 × 10 × {num(h)} = {num(10000*h)} Pa'), u='Pa')

def kmh(rng, mc):
    v = 18 * R(rng, 1, 8)
    return NUM(f'{v} กิโลเมตรต่อชั่วโมง เท่ากับกี่เมตรต่อวินาที', Fr(5 * v, 18), ol(f'{v} × {fr(5,18)} = {num(Fr(5*v,18))} m/s'), u='m/s', h='km/h × 5/18 = m/s')

def energy(rng, mc):
    m = R(rng, 1, 10)
    if rng.random() < .5:
        v = R(rng, 2, 12)
        return NUM(f'วัตถุมวล {m} kg เคลื่อนที่ด้วยอัตราเร็ว {v} m/s มีพลังงานจลน์กี่จูล', Fr(m * v * v, 2), ol(f'E<sub>k</sub> = {fr(1,2)}mv² = {fr(1,2)} × {m} × {v}² = {num(Fr(m*v*v,2))} J'), u='J')
    h = R(rng, 2, 30)
    return NUM(f'วัตถุมวล {m} kg อยู่สูงจากพื้น {h} m มีพลังงานศักย์โน้มถ่วงกี่จูล (g = 10 m/s²)', 10 * m * h, ol(f'E<sub>p</sub> = mgh = {m} × 10 × {h} = {10*m*h} J'), u='J')

def resist(rng, mc):
    a, b = rng.choice([(6, 3), (12, 4), (4, 4), (10, 15), (6, 12), (20, 5), (3, 6), (30, 20), (8, 8), (12, 6)])
    if rng.random() < .5:
        return NUM(f'ตัวต้านทาน {a} Ω และ {b} Ω ต่อแบบขนาน ความต้านทานรวมเท่ากับกี่โอห์ม', Fr(a * b, a + b),
                   ol(f'R = {fr("R₁R₂","R₁ + R₂")} = {fr(f"{a} × {b}", f"{a} + {b}")} = {num(Fr(a*b,a+b))} Ω'), u='Ω')
    V = (a + b) * R(rng, 1, 3)
    return NUM(f'ตัวต้านทาน {a} Ω และ {b} Ω ต่อแบบอนุกรมกับแบตเตอรี่ {V} V กระแสในวงจรเป็นกี่แอมแปร์', Fr(V, a + b),
               ol(f'R รวม = {a} + {b} = {a+b} Ω', f'I = {V} ÷ {a+b} = {num(Fr(V,a+b))} A'), u='A')

def power_w(rng, mc):
    m, h, t = R(rng, 10, 60), R(rng, 2, 10), rng.choice([2, 4, 5, 10, 20])
    return NUM(f'ยกกล่องมวล {m} kg ขึ้นสูง {h} m ในแนวดิ่งด้วยอัตราเร็วคงตัว ใช้เวลา {t} s กำลังที่ใช้เฉลี่ยกี่วัตต์ (g = 10 m/s²)', Fr(10 * m * h, t),
               ol(f'งาน W = mgh = {m} × 10 × {h} = {10*m*h} J', f'กำลัง P = W ÷ t = {10*m*h} ÷ {t} = {num(Fr(10*m*h,t))} W'), u='W')

# ---------- e4-challenge ----------
def incl_excl(rng, mc):
    a, b = rng.choice([(3, 5), (2, 3), (4, 6), (3, 7), (5, 7), (2, 5), (4, 10), (6, 9)]); N = rng.choice([50, 100, 200, 300, 500, 1000])
    L = math.lcm(a, b); v = (N - 1) // a + (N - 1) // b - (N - 1) // L
    return NUM(f'จำนวนเต็มบวกที่น้อยกว่า {N} ที่หารด้วย {a} หรือ {b} ลงตัว มีกี่จำนวน', v,
               ol(f'หาร {a} ลงตัว: {(N-1)//a} จำนวน', f'หาร {b} ลงตัว: {(N-1)//b} จำนวน', f'หารทั้งคู่ (หาร {L} ลงตัว): {(N-1)//L} จำนวน', f'{(N-1)//a} + {(N-1)//b} − {(N-1)//L} = {v}'),
               h='หลักการเพิ่มเข้า-ตัดออก')

def zeros(rng, mc):
    n = R(rng, 20, 200); z = n // 5 + n // 25 + n // 125
    return NUM(f'{n}! (n แฟกทอเรียล) ลงท้ายด้วยเลขศูนย์ติดกันกี่ตัว', z,
               ol('นับจำนวนตัวประกอบ 5 (มีตัวประกอบ 2 มากกว่าเสมอ)', f'⌊{n}/5⌋ + ⌊{n}/25⌋ + ⌊{n}/125⌋ = {n//5} + {n//25} + {n//125} = {z}'), u='ตัว')

def remainder(rng, mc):
    a, m, k = rng.choice([2, 3, 4, 7]), rng.choice([5, 7, 9, 11]), R(rng, 20, 120)
    if math.gcd(a, m) != 1: m = 13
    cyc, x = [], a % m
    while x not in cyc: cyc.append(x); x = x * a % m
    return NUM(f'เศษจากการหาร {a}<sup>{k}</sup> ด้วย {m} เท่ากับเท่าใด', pow(a, k, m),
               ol(f'เศษของ {a}¹, {a}², … เมื่อหารด้วย {m} วนเป็นรอบ: {", ".join(map(str, cyc))} (รอบละ {len(cyc)})',
                  f'{k} ÷ {len(cyc)} เหลือเศษ {k % len(cyc)} → เศษ = {pow(a, k, m)}'))

def diag(rng, mc):
    n = R(rng, 6, 25)
    if rng.random() < .5:
        return NUM(f'รูป {n} เหลี่ยมนูนมีเส้นทแยงมุมทั้งหมดกี่เส้น', n * (n - 3) // 2, ol(f'จำนวนเส้นทแยงมุม = {fr("n(n − 3)",2)} = {fr(f"{n} × {n-3}",2)} = {n*(n-3)//2}'), u='เส้น')
    return NUM(f'มีคน {n} คนในงานเลี้ยง ทุกคนจับมือกันคู่ละ 1 ครั้ง จะจับมือกันทั้งหมดกี่ครั้ง', n * (n - 1) // 2, ol(f'จำนวนคู่ = {fr("n(n − 1)",2)} = {fr(f"{n} × {n-1}",2)} = {n*(n-1)//2} ครั้ง'), u='ครั้ง')

def mult_sum(rng, mc):
    k = R(rng, 3, 9); lo, hi = R(rng, 10, 50), R(rng, 100, 300)
    f, l = -(-lo // k) * k, hi // k * k; n = (l - f) // k + 1
    return NUM(f'ผลบวกของจำนวนนับตั้งแต่ {lo} ถึง {hi} ที่หารด้วย {k} ลงตัว มีค่าเท่าใด', n * (f + l) // 2,
               ol(f'พจน์แรก {f} พจน์สุดท้าย {l} มี {n} พจน์', f'ผลบวก = {fr(f"{n}({f} + {l})", 2)} = {num(n*(f+l)//2)}'), h='เป็นอนุกรมเลขคณิต')

def digits_count(rng, mc):
    n = R(rng, 20, 500)
    d = sum(len(str(i)) for i in range(1, n + 1))
    return NUM(f'เขียนจำนวนนับตั้งแต่ 1 ถึง {n} เรียงต่อกัน ต้องใช้ตัวเลขทั้งหมดกี่ตัว', d,
               ol('1–9 ใช้ 9 ตัว', '10–99 ใช้ 90 × 2 = 180 ตัว' if n >= 99 else f'10–{n} ใช้ {n-9} × 2 = {2*(n-9)} ตัว', *( [f'100–{n} ใช้ {n-99} × 3 = {3*(n-99)} ตัว'] if n >= 100 else []), f'รวม {d} ตัว'), u='ตัว')

TOPICS = {
    'e4-alg':       [sys_xy, recip_sq, double_root, vieta_sq, lin_eq, factor_mc, ab_sq, exp_laws, cube_sum],
    'e4-geo':       [sim_area, pyth_hyp, ladder30, trig_val, trapezoid, cylinder, sphere_cone, inscribed],
    'e4-ps':        [balls, mean_add, die1, dice2, median_l, mean_l, range_mode],
    'e4-phy':       [weight, bill, moment, ohm, density, pressure, kmh, energy, resist, power_w],
    'e4-challenge': [cube_sum, incl_excl, zeros, remainder, diag, mult_sum, digits_count, vieta_sq],
}
NEW = {}
NOPT = 4
