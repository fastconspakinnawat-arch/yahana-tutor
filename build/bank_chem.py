"""เคมี (แนว A-Level เคมี): คำนวณทุกข้อด้วย Fraction"""
from core import ol, NUM, num, fr
from fractions import Fraction as Fr
from factkit import facts_tpl
import math

NOPT = 4
R = lambda rng, a, b: rng.randint(a, b)
AM = {'H': 1, 'C': 12, 'N': 14, 'O': 16, 'Na': 23, 'Mg': 24, 'Al': 27, 'S': 32, 'Cl': Fr(71, 2), 'K': 39, 'Ca': 40, 'Fe': 56, 'Cu': Fr(127, 2)}
AMS = 'H = 1, C = 12, N = 14, O = 16, Na = 23, Mg = 24, Al = 27, S = 32, Cl = 35.5, K = 39, Ca = 40, Fe = 56, Cu = 63.5'

# (HTML formula, Thai name, composition)
CPD = [('H<sub>2</sub>O', 'น้ำ', {'H': 2, 'O': 1}), ('CO<sub>2</sub>', 'คาร์บอนไดออกไซด์', {'C': 1, 'O': 2}),
       ('NaCl', 'โซเดียมคลอไรด์', {'Na': 1, 'Cl': 1}), ('NaOH', 'โซเดียมไฮดรอกไซด์', {'Na': 1, 'O': 1, 'H': 1}),
       ('CaCO<sub>3</sub>', 'แคลเซียมคาร์บอเนต', {'Ca': 1, 'C': 1, 'O': 3}), ('H<sub>2</sub>SO<sub>4</sub>', 'กรดซัลฟิวริก', {'H': 2, 'S': 1, 'O': 4}),
       ('NH<sub>3</sub>', 'แอมโมเนีย', {'N': 1, 'H': 3}), ('CH<sub>4</sub>', 'มีเทน', {'C': 1, 'H': 4}),
       ('C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>', 'กลูโคส', {'C': 6, 'H': 12, 'O': 6}), ('MgO', 'แมกนีเซียมออกไซด์', {'Mg': 1, 'O': 1}),
       ('HCl', 'กรดไฮโดรคลอริก', {'H': 1, 'Cl': 1}), ('KOH', 'โพแทสเซียมไฮดรอกไซด์', {'K': 1, 'O': 1, 'H': 1}),
       ('Al<sub>2</sub>O<sub>3</sub>', 'อะลูมิเนียมออกไซด์', {'Al': 2, 'O': 3}), ('Fe<sub>2</sub>O<sub>3</sub>', 'เหล็ก(III)ออกไซด์', {'Fe': 2, 'O': 3}),
       ('CuSO<sub>4</sub>', 'คอปเปอร์(II)ซัลเฟต', {'Cu': 1, 'S': 1, 'O': 4}), ('HNO<sub>3</sub>', 'กรดไนตริก', {'H': 1, 'N': 1, 'O': 3}),
       ('C<sub>2</sub>H<sub>5</sub>OH', 'เอทานอล', {'C': 2, 'H': 6, 'O': 1}), ('O<sub>2</sub>', 'แก๊สออกซิเจน', {'O': 2})]


def M(comp):
    return sum(AM[e] * n for e, n in comp.items())


def mstep(comp):
    return ' + '.join(f'{n}({num(AM[e])})' if n > 1 else num(AM[e]) for e, n in comp.items())


def molar_mass(rng, mc):
    f, n, c = rng.choice(CPD)
    return NUM(f'มวลโมเลกุล (มวลต่อโมล) ของ {f} ({n}) เท่ากับกี่กรัมต่อโมล<br><small>มวลอะตอม: {AMS}</small>', M(c),
               ol(f'รวมมวลอะตอมทุกตัว: {mstep(c)}', f'= {num(M(c))} g/mol'), u='g/mol')


def nice_n(rng):
    return rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(4), Fr(5)])


def mol_from_mass(rng, mc):
    f, n, c = rng.choice(CPD); m = M(c); k = nice_n(rng); g = k * m
    return NUM(f'{f} มวล {num(g)} กรัม มีกี่โมล<br><small>มวลอะตอม: {AMS}</small>', k,
               ol(f'มวลต่อโมลของ {f} = {num(m)} g/mol', f'n = มวล ÷ มวลต่อโมล = {num(g)} ÷ {num(m)} = {num(k)} mol'), u='mol', h='n = m / M')


def mass_from_mol(rng, mc):
    f, n, c = rng.choice(CPD); m = M(c); k = nice_n(rng)
    return NUM(f'{f} จำนวน {num(k)} โมล มีมวลกี่กรัม<br><small>มวลอะตอม: {AMS}</small>', k * m,
               ol(f'มวลต่อโมลของ {f} = {num(m)} g/mol', f'มวล = n × M = {num(k)} × {num(m)} = {num(k*m)} g'), u='g')


def sci(x):
    """Fraction > 0 → 'a × 10<sup>b</sup>' with a in [1,10)."""
    e = 0
    while x >= 10: x /= 10; e += 1
    while x < 1: x *= 10; e -= 1
    return f'{num(x)} × 10<sup>{e}</sup>'


def particles(rng, mc):
    f, n, c = rng.choice([x for x in CPD if not set(x[2]) & {'Na', 'K', 'Ca', 'Mg', 'Al', 'Fe', 'Cu'}]); k = nice_n(rng)
    N = k * Fr(602, 100) * Fr(10) ** 23
    wrong = [N * 2, N / 2, N * 10, N / 10, k * Fr(10) ** 23, N * 3]
    return mc(f'{f} จำนวน {num(k)} โมล มีกี่โมเลกุล (N<sub>A</sub> = 6.02 × 10<sup>23</sup>)', sci(N), [sci(w) for w in wrong if w != N],
              ol('จำนวนอนุภาค = n × N<sub>A</sub>', f'= {num(k)} × 6.02 × 10<sup>23</sup> = {sci(N)} โมเลกุล'))


def stp_vol(rng, mc):
    gases = [('O<sub>2</sub>', 32), ('CO<sub>2</sub>', 44), ('N<sub>2</sub>', 28), ('H<sub>2</sub>', 2), ('CH<sub>4</sub>', 16), ('NH<sub>3</sub>', 17)]
    f, m = rng.choice(gases); k = nice_n(rng)
    if rng.random() < .5:
        return NUM(f'แก๊ส {f} จำนวน {num(k)} โมล มีปริมาตรกี่ลูกบาศก์เดซิเมตรที่ STP', k * Fr(224, 10),
                   ol('ที่ STP แก๊ส 1 mol มีปริมาตร 22.4 dm³', f'V = {num(k)} × 22.4 = {num(k*Fr(224,10))} dm³'), u='dm³')
    g = k * m
    return NUM(f'แก๊ส {f} มวล {num(g)} กรัม มีปริมาตรกี่ลูกบาศก์เดซิเมตรที่ STP (มวลโมเลกุล {f} = {m})', k * Fr(224, 10),
               ol(f'n = {num(g)} ÷ {m} = {num(k)} mol', f'V = {num(k)} × 22.4 = {num(k*Fr(224,10))} dm³'), u='dm³')


# (equation, A, coefA, M_A, B, coefB, M_B)
RXN = [('2H<sub>2</sub> + O<sub>2</sub> → 2H<sub>2</sub>O', 'H<sub>2</sub>', 2, 2, 'H<sub>2</sub>O', 2, 18),
       ('CH<sub>4</sub> + 2O<sub>2</sub> → CO<sub>2</sub> + 2H<sub>2</sub>O', 'CH<sub>4</sub>', 1, 16, 'CO<sub>2</sub>', 1, 44),
       ('CaCO<sub>3</sub> → CaO + CO<sub>2</sub>', 'CaCO<sub>3</sub>', 1, 100, 'CO<sub>2</sub>', 1, 44),
       ('2Mg + O<sub>2</sub> → 2MgO', 'Mg', 2, 24, 'MgO', 2, 40),
       ('N<sub>2</sub> + 3H<sub>2</sub> → 2NH<sub>3</sub>', 'N<sub>2</sub>', 1, 28, 'NH<sub>3</sub>', 2, 17),
       ('Zn + 2HCl → ZnCl<sub>2</sub> + H<sub>2</sub>', 'HCl', 2, Fr(73, 2), 'H<sub>2</sub>', 1, 2),
       ('4Al + 3O<sub>2</sub> → 2Al<sub>2</sub>O<sub>3</sub>', 'Al', 4, 27, 'Al<sub>2</sub>O<sub>3</sub>', 2, 102),
       ('C<sub>3</sub>H<sub>8</sub> + 5O<sub>2</sub> → 3CO<sub>2</sub> + 4H<sub>2</sub>O', 'C<sub>3</sub>H<sub>8</sub>', 1, 44, 'H<sub>2</sub>O', 4, 18)]


def stoich(rng, mc):
    eq, A, a, MA, B, b, MB = rng.choice(RXN)
    nA = a * rng.choice([Fr(1, 2), Fr(1), Fr(2), Fr(3), Fr(1, 4)])
    gA = nA * MA; nB = nA * Fr(b, a); gB = nB * MB
    return NUM(f'จากสมการ {eq}<br>ใช้ {A} {num(gA)} กรัม ทำปฏิกิริยาหมด จะได้ {B} กี่กรัม (มวลต่อโมล {A} = {num(MA)}, {B} = {num(MB)})', gB,
               ol(f'mol {A} = {num(gA)} ÷ {num(MA)} = {num(nA)} mol', f'อัตราส่วนโมล {A} : {B} = {a} : {b} → mol {B} = {num(nB)} mol',
                  f'มวล {B} = {num(nB)} × {num(MB)} = {num(gB)} g'), u='g', h='แปลงเป็นโมล → ใช้อัตราส่วนสัมประสิทธิ์ → แปลงกลับเป็นกรัม')


def percent(rng, mc):
    f, n, c = rng.choice(CPD)
    e = rng.choice(list(c))
    p = Fr(AM[e] * c[e] * 100) / M(c)
    show = lambda x: f'{float(x):.1f}%'
    ws = [Fr(AM[e] * 100) / M(c), 100 - p, Fr(c[e] * 100, sum(c.values())), p * Fr(3, 2), p / 2]
    return mc(f'ร้อยละโดยมวลของธาตุ {e} ใน {f} ประมาณเท่าใด<br><small>มวลอะตอม: {AMS}</small>', show(p),
              [show(w) for w in ws if show(w) != show(p) and 0 < w < 100] + ['50.0%', '25.0%', '75.0%'],
              ol(f'มวลต่อโมลของ {f} = {num(M(c))}', f'มวลของ {e} ในสูตร = {c[e]} × {num(AM[e])} = {num(AM[e]*c[e])}',
                 f'ร้อยละ = {num(AM[e]*c[e])} ÷ {num(M(c))} × 100 ≈ {show(p)}'))


# ---------- สารละลาย กรด-เบส ----------
def molarity(rng, mc):
    sol = [('NaOH', 40), ('NaCl', Fr(117, 2)), ('KOH', 56), ('glucose (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>)', 180), ('CuSO<sub>4</sub>', Fr(319, 2))]
    f, m = rng.choice(sol); V = rng.choice([100, 200, 250, 500, 1000]); c = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), Fr(1), Fr(2)])
    g = c * Fr(V, 1000) * m
    return NUM(f'ละลาย {f} {num(g)} กรัม ในน้ำจนได้สารละลาย {V} cm³ ความเข้มข้นเป็นกี่ mol/dm³ (มวลต่อโมล = {num(m)})', c,
               ol(f'n = {num(g)} ÷ {num(m)} = {num(c*Fr(V,1000))} mol', f'V = {V} cm³ = {num(Fr(V,1000))} dm³', f'C = n ÷ V = {num(c)} mol/dm³'),
               u='mol/dm³', h='C = n / V (V หน่วย dm³)')


def dilute(rng, mc):
    c1 = rng.choice([1, 2, 5, 10]); v1 = rng.choice([10, 20, 25, 50]); k = rng.choice([2, 4, 5, 10])
    v2 = v1 * k; c2 = Fr(c1, k)
    if rng.random() < .5:
        return NUM(f'นำสารละลาย HCl เข้มข้น {c1} mol/dm³ ปริมาตร {v1} cm³ มาเติมน้ำจนมีปริมาตร {v2} cm³ ความเข้มข้นใหม่เป็นกี่ mol/dm³', c2,
                   ol('C₁V₁ = C₂V₂', f'{c1} × {v1} = C₂ × {v2}', f'C₂ = {num(c2)} mol/dm³'), u='mol/dm³')
    return NUM(f'ต้องการ HCl เข้มข้น {num(c2)} mol/dm³ ปริมาตร {v2} cm³ จากสารละลายเข้มข้น {c1} mol/dm³ ต้องใช้สารละลายเข้มข้นกี่ cm³', v1,
               ol('C₁V₁ = C₂V₂', f'{c1} × V₁ = {num(c2)} × {v2}', f'V₁ = {v1} cm³'), u='cm³')


def ph_calc(rng, mc):
    k = R(rng, 1, 5); m = rng.choice([1, 1, 1])
    t = rng.randrange(3)
    if t == 0:
        return NUM(f'สารละลาย HCl เข้มข้น 1 × 10<sup>−{k}</sup> mol/dm³ มี pH เท่าใด', k,
                   ol('HCl เป็นกรดแก่ แตกตัวสมบูรณ์ → [H<sub>3</sub>O<sup>+</sup>] = 10<sup>−' + str(k) + '</sup>', f'pH = −log[H<sub>3</sub>O<sup>+</sup>] = {k}'))
    if t == 1:
        return NUM(f'สารละลาย NaOH เข้มข้น 1 × 10<sup>−{k}</sup> mol/dm³ มี pH เท่าใด (ที่ 25 °C)', 14 - k,
                   ol('NaOH เป็นเบสแก่ → [OH<sup>−</sup>] = 10<sup>−' + str(k) + '</sup>', f'pOH = {k}', f'pH = 14 − pOH = {14-k}'), h='pH + pOH = 14')
    p = R(rng, 1, 13)
    nature = 'กรด' if p < 7 else ('เบส' if p > 7 else 'กลาง')
    return mc(f'สารละลายที่มี pH = {p} มี [H<sub>3</sub>O<sup>+</sup>] เท่าใด และเป็นสารละลายประเภทใด',
              f'1 × 10<sup>−{p}</sup> mol/dm³ เป็น{nature}',
              [f'1 × 10<sup>−{14-p}</sup> mol/dm³ เป็น{"เบส" if p < 7 else "กรด"}', f'1 × 10<sup>−{p}</sup> mol/dm³ เป็น{"เบส" if p < 7 else "กรด"}',
               f'1 × 10<sup>{p}</sup> mol/dm³ เป็น{nature}', f'1 × 10<sup>−{p+1}</sup> mol/dm³ เป็น{nature}'],
              ol(f'[H<sub>3</sub>O<sup>+</sup>] = 10<sup>−pH</sup> = 10<sup>−{p}</sup> mol/dm³', 'pH < 7 เป็นกรด, pH = 7 เป็นกลาง, pH > 7 เป็นเบส'))


def titrate(rng, mc):
    ca = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2)]); va = rng.choice([10, 20, 25])
    cb = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2)])
    acid = rng.choice([('HCl', 1), ('H<sub>2</sub>SO<sub>4</sub>', 2)])
    vb = ca * va * acid[1] / cb
    if vb.denominator != 1 and (vb * 10).denominator != 1: vb = None
    if vb is None: return titrate(rng, mc)
    return NUM(f'สารละลาย {acid[0]} เข้มข้น {num(ca)} mol/dm³ ปริมาตร {va} cm³ ทำปฏิกิริยาพอดีกับ NaOH เข้มข้น {num(cb)} mol/dm³ ต้องใช้ NaOH กี่ cm³', vb,
               ol(f'mol {acid[0]} = {num(ca)} × {va}/1000 = {num(ca*va/1000)} mol',
                  f'{acid[0]} 1 mol ทำปฏิกิริยากับ NaOH {acid[1]} mol → NaOH = {num(ca*va*acid[1]/1000)} mol',
                  f'V = {num(ca*va*acid[1]/1000)} ÷ {num(cb)} = {num(vb/1000)} dm³ = {num(vb)} cm³'), u='cm³')


ACID = [('ตามทฤษฎีของเบรินสเตด-ลาวรี กรดคือสารที่ทำหน้าที่ใด', 'ให้โปรตอน (H<sup>+</sup>)', ['รับโปรตอน', 'ให้อิเล็กตรอนคู่โดดเดี่ยว', 'ให้ไอออน OH<sup>−</sup> เท่านั้น']),
        ('คู่กรด-เบสของ NH<sub>3</sub> (คู่กรดคอนจูเกต) คือข้อใด', 'NH<sub>4</sub><sup>+</sup>', ['NH<sub>2</sub><sup>−</sup>', 'H<sub>2</sub>O', 'OH<sup>−</sup>']),
        ('เบสคอนจูเกตของ H<sub>2</sub>O คือข้อใด', 'OH<sup>−</sup>', ['H<sub>3</sub>O<sup>+</sup>', 'O<sup>2−</sup>', 'H<sub>2</sub>']),
        ('สารละลายใดนำไฟฟ้าได้ดีที่สุดเมื่อความเข้มข้นเท่ากัน', 'HCl', ['CH<sub>3</sub>COOH', 'C<sub>2</sub>H<sub>5</sub>OH', 'C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>']),
        ('ฟีนอล์ฟทาลีนในสารละลายเบสมีสีใด', 'ชมพู', ['ไม่มีสี', 'เหลือง', 'น้ำเงิน']),
        ('เกลือใดเมื่อละลายน้ำแล้วสารละลายเป็นเบส', 'CH<sub>3</sub>COONa', ['NaCl', 'NH<sub>4</sub>Cl', 'KNO<sub>3</sub>']),
        ('สารละลายบัฟเฟอร์มีสมบัติสำคัญคือข้อใด', 'รักษาระดับ pH ให้เปลี่ยนแปลงน้อยเมื่อเติมกรดหรือเบสเล็กน้อย', ['ทำให้ pH เท่ากับ 7 เสมอ', 'เร่งปฏิกิริยา', 'ทำให้สารละลายนำไฟฟ้าไม่ได้'])]


# ---------- อะตอมและตารางธาตุ ----------
EL = [('H', 1), ('He', 2), ('Li', 3), ('Be', 4), ('B', 5), ('C', 6), ('N', 7), ('O', 8), ('F', 9), ('Ne', 10), ('Na', 11), ('Mg', 12),
      ('Al', 13), ('Si', 14), ('P', 15), ('S', 16), ('Cl', 17), ('Ar', 18), ('K', 19), ('Ca', 20)]
ISO = [('C', 6, 12), ('C', 6, 14), ('O', 8, 16), ('Na', 11, 23), ('Mg', 12, 24), ('Al', 13, 27), ('Cl', 17, 35), ('Cl', 17, 37), ('K', 19, 39),
       ('Ca', 20, 40), ('Fe', 26, 56), ('Cu', 29, 64), ('Zn', 30, 65), ('Br', 35, 80), ('Ag', 47, 108), ('U', 92, 238)]


def shells(z):
    out = []
    for cap in (2, 8, 8, 2):
        if z <= 0: break
        out.append(min(z, cap)); z -= min(z, cap)
    return out


def iso_q(rng, mc):
    s, z, a = rng.choice(ISO); ch = rng.choice([0, 0, 1, 2, -1]) if s in ('Na', 'Mg', 'Al', 'Cl', 'Ca', 'K', 'O') else 0
    if s in ('Na', 'K'): ch = rng.choice([0, 1])
    if s in ('Mg', 'Ca'): ch = rng.choice([0, 2])
    if s == 'Al': ch = rng.choice([0, 3])
    if s in ('Cl',): ch = rng.choice([0, -1])
    if s == 'O': ch = rng.choice([0, -2])
    cs = '' if ch == 0 else (f'{abs(ch) if abs(ch) > 1 else ""}{"+" if ch > 0 else "−"}')
    sym = f'<sup>{a}</sup><sub>{z}</sub>{s}' + (f'<sup>{cs}</sup>' if cs else '')
    if rng.random() < .5:
        return NUM(f'{sym} มีจำนวนนิวตรอนเท่าใด', a - z, ol(f'เลขมวล {a} = โปรตอน + นิวตรอน', f'นิวตรอน = {a} − {z} = {a-z}'))
    e = z - ch
    return NUM(f'{sym} มีจำนวนอิเล็กตรอนเท่าใด', e, ol(f'โปรตอน = เลขอะตอม = {z}', f'ประจุ {cs or "0"} → อิเล็กตรอน = {z} − ({ch}) = {e}'))


def config(rng, mc):
    s, z = rng.choice(EL[2:])
    c = shells(z); show = lambda x: ', '.join(map(str, x))
    ws = [shells(z + 1), shells(z - 1), [z] if z <= 8 else [2, z - 2], c[:-1] + [c[-1] + 1] if len(c) > 1 else [c[0] + 1], [2, 8, z - 10] if z > 10 else [1, z - 1]]
    return mc(f'ธาตุ {s} (เลขอะตอม {z}) มีการจัดเรียงอิเล็กตรอนในระดับพลังงานหลักเป็นอย่างไร', show(c), [show(w) for w in ws if w != c and all(x > 0 for x in w)] + ['2, 8, 8, 8'],
              ol(f'บรรจุระดับละไม่เกิน 2, 8, 8, … (สำหรับธาตุ 20 ตัวแรก)', f'{s}: {show(c)}'))


def group_period(rng, mc):
    s, z = rng.choice(EL)
    c = shells(z); p = len(c); v = c[-1]
    g = {1: 'IA', 2: 'IIA', 3: 'IIIA', 4: 'IVA', 5: 'VA', 6: 'VIA', 7: 'VIIA', 8: 'VIIIA'}[v] if s != 'He' else 'VIIIA'
    allg = ['IA', 'IIA', 'IIIA', 'IVA', 'VA', 'VIA', 'VIIA', 'VIIIA']
    opts = [f'หมู่ {x} คาบ {y}' for x in allg for y in (1, 2, 3, 4) if (x, y) != (g, p)]
    rng.shuffle(opts)
    near = [f'หมู่ {g} คาบ {p+1}', f'หมู่ {g} คาบ {max(1,p-1)}', f'หมู่ {allg[(allg.index(g)+1)%8]} คาบ {p}']
    return mc(f'ธาตุ {s} (เลขอะตอม {z}) อยู่หมู่และคาบใดในตารางธาตุ', f'หมู่ {g} คาบ {p}', [x for x in near if x != f'หมู่ {g} คาบ {p}'] + opts,
              ol(f'การจัดเรียงอิเล็กตรอน: {", ".join(map(str, c))}', f'มี {p} ระดับพลังงาน → คาบ {p}',
                 f'เวเลนซ์อิเล็กตรอน {v if s != "He" else 2} → หมู่ {g}' + (' (He เป็นแก๊สมีตระกูล)' if s == 'He' else '')))


TREND = [('ในคาบเดียวกัน เมื่อเลขอะตอมเพิ่มขึ้น (จากซ้ายไปขวา) ขนาดอะตอมเปลี่ยนแปลงอย่างไร', 'เล็กลง', ['ใหญ่ขึ้น', 'เท่าเดิม', 'ใหญ่ขึ้นแล้วเล็กลง']),
         ('ในหมู่เดียวกัน เมื่อเลขอะตอมเพิ่มขึ้น (จากบนลงล่าง) ขนาดอะตอมเปลี่ยนแปลงอย่างไร', 'ใหญ่ขึ้น', ['เล็กลง', 'เท่าเดิม', 'เล็กลงแล้วใหญ่ขึ้น']),
         ('ธาตุใดมีค่าอิเล็กโทรเนกาติวิตีสูงที่สุด', 'F', ['O', 'Cl', 'N']),
         ('ธาตุหมู่ใดเรียกว่า “โลหะแอลคาไล”', 'หมู่ IA', ['หมู่ IIA', 'หมู่ VIIA', 'หมู่ VIIIA']),
         ('ธาตุหมู่ VIIA เรียกว่าอะไร', 'แฮโลเจน', ['โลหะแอลคาไล', 'แก๊สมีตระกูล', 'โลหะแอลคาไลน์เอิร์ท']),
         ('ในคาบเดียวกัน พลังงานไอออไนเซชันลำดับที่ 1 มีแนวโน้มอย่างไรจากซ้ายไปขวา', 'เพิ่มขึ้น', ['ลดลง', 'คงที่', 'ลดลงแล้วเพิ่มขึ้น']),
         ('ไอออนบวกมีขนาดเป็นอย่างไรเมื่อเทียบกับอะตอมเดิม', 'เล็กกว่าอะตอมเดิม', ['ใหญ่กว่าอะตอมเดิม', 'เท่ากับอะตอมเดิม', 'ไม่แน่นอน']),
         ('อนุภาคใดในนิวเคลียสไม่มีประจุไฟฟ้า', 'นิวตรอน', ['โปรตอน', 'อิเล็กตรอน', 'โพซิตรอน']),
         ('ไอโซโทปของธาตุเดียวกันมีสิ่งใดต่างกัน', 'จำนวนนิวตรอน', ['จำนวนโปรตอน', 'เลขอะตอม', 'จำนวนอิเล็กตรอนในอะตอมที่เป็นกลาง']),
         ('ผู้เสนอแบบจำลองอะตอมที่มีนิวเคลียสอยู่ตรงกลางจากการทดลองยิงอนุภาคแอลฟาผ่านแผ่นทองคำ คือใคร', 'รัทเทอร์ฟอร์ด', ['ทอมสัน', 'ดอลตัน', 'โบร์'])]


# ---------- พันธะเคมี ----------
CAT = [('Na', 1), ('K', 1), ('NH<sub>4</sub>', 1), ('Mg', 2), ('Ca', 2), ('Cu', 2), ('Al', 3), ('Fe', 3)]
AN = [('Cl', 1), ('OH', 1), ('NO<sub>3</sub>', 1), ('O', 2), ('S', 2), ('SO<sub>4</sub>', 2), ('CO<sub>3</sub>', 2), ('PO<sub>4</sub>', 3)]
POLY = ('NH<sub>4</sub>', 'OH', 'NO<sub>3</sub>', 'SO<sub>4</sub>', 'CO<sub>3</sub>', 'PO<sub>4</sub>')


def part(s, n):
    if n == 1: return s
    return (f'({s})' if s in POLY else s) + f'<sub>{n}</sub>'


def formula(c, a, x, y):
    return part(c, x) + part(a, y)


def ionic(rng, mc):
    (c, p), (a, q) = rng.choice(CAT), rng.choice(AN)
    g = math.gcd(p, q); x, y = q // g, p // g
    ans = formula(c, a, x, y)
    ws = [formula(c, a, y, x), formula(c, a, 1, 1), formula(c, a, p, q), formula(c, a, x, y + 1), formula(c, a, x + 1, y), formula(c, a, 2, 3), formula(c, a, 3, 2)]
    sup = lambda n, sgn: (f'{n}{sgn}' if n > 1 else sgn)
    return mc(f'สารประกอบไอออนิกที่เกิดจาก {c}<sup>{sup(p,"+")}</sup> และ {a}<sup>{sup(q,"−")}</sup> มีสูตรเคมีเป็นอย่างไร', ans, ws,
              ol('ประจุรวมต้องเป็นศูนย์', f'{x} × (+{p}) + {y} × (−{q}) = 0', f'สูตร = {ans}'), h='ไขว้เลขประจุ แล้วทำให้เป็นอัตราส่วนอย่างต่ำ')


SHAPE = [('CH<sub>4</sub>', 'ทรงสี่หน้า'), ('NH<sub>3</sub>', 'พีระมิดฐานสามเหลี่ยม'), ('H<sub>2</sub>O', 'มุมงอ'), ('CO<sub>2</sub>', 'เส้นตรง'),
         ('BF<sub>3</sub>', 'สามเหลี่ยมแบนราบ'), ('BeCl<sub>2</sub>', 'เส้นตรง'), ('CCl<sub>4</sub>', 'ทรงสี่หน้า'), ('SO<sub>3</sub>', 'สามเหลี่ยมแบนราบ'),
         ('PCl<sub>5</sub>', 'พีระมิดคู่ฐานสามเหลี่ยม'), ('SF<sub>6</sub>', 'ทรงแปดหน้า'), ('H<sub>2</sub>S', 'มุมงอ'), ('PH<sub>3</sub>', 'พีระมิดฐานสามเหลี่ยม')]
SHAPES = sorted(set(s for _, s in SHAPE))


def shape(rng, mc):
    f, s = rng.choice(SHAPE)
    return mc(f'โมเลกุล {f} มีรูปร่างแบบใด (ตามทฤษฎี VSEPR)', s, rng.sample([x for x in SHAPES if x != s], len(SHAPES) - 1),
              ol(f'นับคู่อิเล็กตรอนรอบอะตอมกลาง (คู่สร้างพันธะและคู่โดดเดี่ยว)', f'{f} มีรูปร่าง{s}'))


BOND = [('สารใดเกิดพันธะไอออนิก', 'NaCl', ['HCl', 'CH<sub>4</sub>', 'Cl<sub>2</sub>']),
        ('สารใดเกิดพันธะโคเวเลนต์', 'CO<sub>2</sub>', ['MgO', 'KCl', 'CaF<sub>2</sub>']),
        ('โมเลกุลใดเป็นโมเลกุลไม่มีขั้ว', 'CO<sub>2</sub>', ['H<sub>2</sub>O', 'NH<sub>3</sub>', 'HCl']),
        ('โมเลกุลใดเป็นโมเลกุลมีขั้ว', 'NH<sub>3</sub>', ['CH<sub>4</sub>', 'CO<sub>2</sub>', 'BF<sub>3</sub>']),
        ('สารใดมีพันธะไฮโดรเจนระหว่างโมเลกุล', 'H<sub>2</sub>O', ['CH<sub>4</sub>', 'H<sub>2</sub>S', 'CO<sub>2</sub>']),
        ('น้ำมีจุดเดือดสูงกว่า H<sub>2</sub>S เพราะเหตุใด', 'น้ำมีพันธะไฮโดรเจนระหว่างโมเลกุล', ['น้ำมีมวลโมเลกุลมากกว่า', 'น้ำเป็นสารไอออนิก', 'น้ำไม่มีขั้ว']),
        ('ในโมเลกุล N<sub>2</sub> อะตอมไนโตรเจนยึดกันด้วยพันธะชนิดใด', 'พันธะสาม', ['พันธะเดี่ยว', 'พันธะคู่', 'พันธะไอออนิก']),
        ('สมบัติใดเป็นของสารประกอบไอออนิก', 'ของแข็งไม่นำไฟฟ้า แต่เมื่อหลอมเหลวหรือละลายน้ำนำไฟฟ้าได้', ['นำไฟฟ้าได้ในทุกสถานะ', 'จุดหลอมเหลวต่ำมาก', 'ไม่ละลายน้ำทุกชนิด']),
        ('โลหะนำไฟฟ้าได้ดีเพราะเหตุใด', 'มีเวเลนซ์อิเล็กตรอนที่เคลื่อนที่ได้อิสระ', ['มีไอออนลบเคลื่อนที่ได้', 'มีพันธะโคเวเลนต์แข็งแรง', 'มีโปรตอนเคลื่อนที่ได้']),
        ('เพชรและแกรไฟต์เป็นอะไรต่อกัน', 'อัญรูปของคาร์บอน', ['ไอโซโทปของคาร์บอน', 'ไอโซเมอร์', 'สารประกอบต่างชนิด'])]


# ---------- อัตราและสมดุล ----------
def kc(rng, mc):
    a, b, c = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), Fr(1), Fr(2)]), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), Fr(1)]), rng.choice([Fr(1, 5), Fr(1, 2), Fr(1), Fr(2), Fr(4)])
    k = rng.randrange(2)
    if k == 0:
        K = c / (a * b)
        if (K * 1000).denominator != 1: return kc(rng, mc)
        return NUM(f'ปฏิกิริยา A(g) + B(g) ⇌ C(g) ที่สมดุลมี [A] = {num(a)}, [B] = {num(b)} และ [C] = {num(c)} mol/dm³ ค่าคงที่สมดุล K<sub>c</sub> เท่ากับเท่าใด', K,
                   ol('K<sub>c</sub> = ' + fr('[C]', '[A][B]'), f'= {num(c)} ÷ ({num(a)} × {num(b)}) = {num(K)}'))
    K = c * c / a
    if (K * 1000).denominator != 1: return kc(rng, mc)
    return NUM(f'ปฏิกิริยา A(g) ⇌ 2B(g) ที่สมดุลมี [A] = {num(a)} และ [B] = {num(c)} mol/dm³ ค่า K<sub>c</sub> เท่ากับเท่าใด', K,
               ol('K<sub>c</sub> = ' + fr('[B]²', '[A]'), f'= {num(c)}² ÷ {num(a)} = {num(K)}'), h='สัมประสิทธิ์เป็นเลขชี้กำลังของความเข้มข้น')


def rate(rng, mc):
    c1 = rng.choice([Fr(2), Fr(1), Fr(8, 10), Fr(5, 10)]); f = rng.choice([Fr(1, 2), Fr(1, 4), Fr(3, 4)]); c2 = c1 * f
    t = rng.choice([10, 20, 25, 40, 50])
    r = (c1 - c2) / t
    if (r * 10**6).denominator != 1: return rate(rng, mc)
    return NUM(f'ความเข้มข้นของสารตั้งต้นลดจาก {num(c1)} เป็น {num(c2)} mol/dm³ ในเวลา {t} s อัตราการเกิดปฏิกิริยาเฉลี่ยเป็นกี่ mol/dm³·s', r,
               ol('อัตราเฉลี่ย = ' + fr('Δ[สารตั้งต้น]', 'Δt'), f'= ({num(c1)} − {num(c2)}) ÷ {t} = {num(r)} mol/dm³·s'), u='mol/dm³·s')


EQF = [('การเติมตัวเร่งปฏิกิริยาส่งผลอย่างไร', 'ลดพลังงานก่อกัมมันต์ ทำให้ปฏิกิริยาเกิดเร็วขึ้น', ['เพิ่มปริมาณผลิตภัณฑ์ที่สมดุล', 'เพิ่มพลังงานก่อกัมมันต์', 'ทำให้สมดุลเลื่อนไปทางขวาเสมอ']),
       ('ข้อใดทำให้อัตราการเกิดปฏิกิริยาเพิ่มขึ้น', 'บดสารให้เป็นผงละเอียดเพื่อเพิ่มพื้นที่ผิว', ['ลดอุณหภูมิ', 'ลดความเข้มข้นของสารตั้งต้น', 'ใช้สารเป็นก้อนใหญ่']),
       ('สำหรับ N<sub>2</sub>(g) + 3H<sub>2</sub>(g) ⇌ 2NH<sub>3</sub>(g) การเพิ่มความดันทำให้สมดุลเลื่อนไปทางใด', 'ไปทางขวา (เกิด NH<sub>3</sub> มากขึ้น)', ['ไปทางซ้าย', 'ไม่เลื่อน', 'เลื่อนไปมาไม่แน่นอน']),
       ('ปฏิกิริยาดูดความร้อนที่สมดุล เมื่อเพิ่มอุณหภูมิ ค่า K จะเป็นอย่างไร', 'เพิ่มขึ้น', ['ลดลง', 'คงที่', 'เป็นศูนย์']),
       ('ปฏิกิริยาคายความร้อนที่สมดุล เมื่อเพิ่มอุณหภูมิ สมดุลจะเลื่อนไปทางใด', 'ทางซ้าย (ทางสารตั้งต้น)', ['ทางขวา', 'ไม่เลื่อน', 'ค่า K เพิ่มขึ้น']),
       ('การเติมสารตั้งต้นลงในระบบที่สมดุล ค่า K เป็นอย่างไร (อุณหภูมิคงที่)', 'คงที่', ['เพิ่มขึ้น', 'ลดลง', 'เป็นศูนย์']),
       ('ที่ภาวะสมดุลเคมี ข้อใดถูกต้อง', 'อัตราการเกิดปฏิกิริยาไปข้างหน้าเท่ากับอัตราย้อนกลับ', ['ปฏิกิริยาหยุดเกิดขึ้น', 'ความเข้มข้นของสารทุกตัวเท่ากัน', 'มีแต่ผลิตภัณฑ์']),
       ('ทฤษฎีการชนกล่าวว่าปฏิกิริยาจะเกิดเมื่อใด', 'อนุภาคชนกันด้วยพลังงานอย่างน้อยเท่ากับพลังงานก่อกัมมันต์และทิศทางเหมาะสม', ['อนุภาคชนกันทุกครั้ง', 'อนุภาคอยู่นิ่ง', 'เติมน้ำเสมอ'])]

TOPICS = {
    'ch-mole': [molar_mass, mol_from_mass, mass_from_mol, particles, stp_vol, stoich, percent],
    'ch-sol': [molarity, dilute, ph_calc, titrate, facts_tpl(ACID)],
    'ch-atom': [iso_q, config, group_period, facts_tpl(TREND)],
    'ch-bond': [ionic, ionic, shape, facts_tpl(BOND)],
    'ch-rate': [kc, rate, facts_tpl(EQF)],
}
NEW = {
    'ch-mole': ('alevel-chem', 'chem', 'โมลและปริมาณสัมพันธ์'),
    'ch-sol': ('alevel-chem', 'chem', 'สารละลาย กรด-เบส และ pH'),
    'ch-atom': ('alevel-chem', 'chem', 'อะตอมและตารางธาตุ'),
    'ch-bond': ('alevel-chem', 'chem', 'พันธะเคมีและรูปร่างโมเลกุล'),
    'ch-rate': ('alevel-chem', 'chem', 'อัตราการเกิดปฏิกิริยาและสมดุลเคมี'),
}
