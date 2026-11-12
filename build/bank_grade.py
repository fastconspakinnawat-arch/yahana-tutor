"""ชุดตามระดับชั้น: ประถม ม.ต้น ม.ปลาย"""
from core import *
import math
from bank_m1 import frac_add, frac_of, frac_div, gcd3, lcm3, gcd_lcm_other, pct_of, pct_change, circle_area, circ, rect_perim, cube_sa, fac
from bank_m4 import exp_laws, lin_eq, factor_mc, pyth_hyp, mean_l, median_l, range_mode, mean_add, kmh, density, pressure, ohm, resist, bill, energy, power_w, trig_val, balls, sgn, weight
from bank_a1 import MCN, log_vals, log_rule, change_base, exp_eq, log_eq, trig_quad, trig_tri, rad, tri_area, cos_law, ar_nth, ge_nth, ar_sum, inf_geo, two_terms, deriv_at, lim0, integ, rel_min, lim_inf, tangent, word_arr, poly
from bank_m1 import gauss
from bank_a2 import f_lin, compo, inv_val, vertex, intercepts, solve_exp, dice_sum, at_least_head, choose, fact_arr, together
from bank_ap import friction, max_h, stick, impulse, vfl, echo, freq, beats, string_f, coulomb, power_r, fall_speed
R = lambda rng, a, b: rng.randint(a, b)

# ================= ประถม =================
def frac_sub(rng, mc):
    b, d = rng.sample([2, 3, 4, 5, 6, 8, 10, 12], 2); a, c = R(rng, 1, b - 1), R(rng, 1, d - 1)
    if Fr(a, b) < Fr(c, d): a, b, c, d = c, d, a, b
    v = Fr(a, b) - Fr(c, d); L = math.lcm(b, d)
    if v == 0: return frac_sub(rng, mc)
    return mc(f'{fr(a,b)} − {fr(c,d)} มีค่าเท่าใด', fr(v), [fr(Fr(abs(a - c), abs(b - d) or 1)), fr(v + Fr(1, L)), fr(Fr(a, b) + Fr(c, d)), fr(v * 2), fr(v + Fr(1, 2))],
              ol(f'ค.ร.น. ของ {b} และ {d} คือ {L}', f'{fr(a*L//b, L)} − {fr(c*L//d, L)} = {fr(a*L//b - c*L//d, L)}' + (f' = {fr(v)}' if v.denominator != L else '')))

def mixed(rng, mc):
    w, d = R(rng, 1, 9), R(rng, 2, 9); n = R(rng, 1, d - 1)
    v = Fr(w * d + n, d)
    if v.denominator != d: return mixed(rng, mc)
    return mc(f'{w}{fr(n,d)} เขียนเป็นเศษเกินได้ตรงกับข้อใด', fr(w * d + n, d), [fr(w + n, d), fr(w * n + d, d), fr(w * d - n, d), fr(w * d + n, n)],
              ol(f'นำจำนวนเต็มคูณตัวส่วนแล้วบวกตัวเศษ: {w} × {d} + {n} = {w*d+n}', f'ได้ {fr(w*d+n, d)}'))

def compare(rng, mc):
    fs = []
    while len(fs) < 4:
        d = rng.choice([3, 4, 5, 6, 7, 8, 9, 10]); n = R(rng, 1, d - 1); x = Fr(n, d)
        if all(x != y for _, _, y in fs): fs.append((n, d, x))
    big = max(fs, key=lambda t: t[2])
    return mc('เศษส่วนใดมีค่ามากที่สุด', fr(big[0], big[1]), [fr(n, d) for n, d, _ in fs if (n, d) != big[:2]],
              ol('ทำให้ตัวส่วนเท่ากัน หรือแปลงเป็นทศนิยมเพื่อเปรียบเทียบ', ', '.join(f'{fr(n,d)} ≈ {round(n/d,3)}' for n, d, _ in fs), f'มากที่สุดคือ {fr(big[0], big[1])}'))

def frac_word(rng, mc):
    q = rng.choice([3, 4, 5, 6, 8]); p = R(rng, 1, q - 1); N = q * R(rng, 4, 25)
    return NUM(f'แม่มีเงิน {N} บาท ใช้ไป {fr(p,q)} ของเงินทั้งหมด เหลือเงินกี่บาท', N - N * p // q,
               ol(f'ใช้ไป {fr(p,q)} × {N} = {N*p//q} บาท', f'เหลือ {N} − {N*p//q} = {N - N*p//q} บาท'), u='บาท')

def gcd2(rng, mc):
    g = R(rng, 2, 15); a, b = rng.sample([x for x in range(2, 12)], 2)
    while math.gcd(a, b) != 1: a, b = rng.sample(range(2, 12), 2)
    return NUM(f'ห.ร.ม. ของ {g*a} และ {g*b} คือเท่าใด', g, ol(f'{g*a} = {fac(g*a)}', f'{g*b} = {fac(g*b)}', f'ตัวประกอบร่วมคูณกัน = {g}'))

def lcm2(rng, mc):
    a, b = rng.sample(range(4, 25), 2)
    return NUM(f'ค.ร.น. ของ {a} และ {b} คือเท่าใด', math.lcm(a, b), ol(f'{a} = {fac(a)}', f'{b} = {fac(b)}', f'ค.ร.น. = {fac(math.lcm(a,b))} = {math.lcm(a,b)}'))

def ribbon(rng, mc):
    g = rng.choice([4, 5, 6, 8, 10, 12, 15]); a, b = rng.sample([2, 3, 5, 7], 2)
    return NUM(f'มีริบบิ้นยาว {g*a} ซม. และ {g*b} ซม. ต้องการตัดเป็นเส้นยาวเท่ากันโดยไม่เหลือเศษ และให้แต่ละเส้นยาวที่สุด แต่ละเส้นยาวกี่เซนติเมตร', g,
               ol('ยาวที่สุดและหารลงตัว → ใช้ ห.ร.ม.', f'ห.ร.ม.({g*a}, {g*b}) = {g}'), u='ซม.', h='"มากที่สุด ที่แบ่งได้ลงตัว" ใช้ ห.ร.ม.')

def bus(rng, mc):
    a, b = rng.sample([6, 8, 9, 10, 12, 15, 20], 2); h = R(rng, 6, 8)
    L = math.lcm(a, b)
    return NUM(f'รถเมล์สาย ก ออกทุก {a} นาที สาย ข ออกทุก {b} นาที ถ้าออกพร้อมกันเวลา {h}:00 น. จะออกพร้อมกันอีกครั้งในอีกกี่นาที', L,
               ol('"พร้อมกันอีกครั้ง" ใช้ ค.ร.น.', f'ค.ร.น.({a}, {b}) = {L} นาที'), u='นาที')

def disc_price(rng, mc):
    P, d = rng.choice([200, 300, 450, 600, 800, 1200]), rng.choice([10, 15, 20, 25, 30, 40])
    return NUM(f'กระเป๋าราคา {P} บาท ลดราคา {d}% ต้องจ่ายกี่บาท', P * (100 - d) // 100 if P * (100 - d) % 100 == 0 else Fr(P * (100 - d), 100),
               ol(f'ส่วนลด = {fr(d,100)} × {P} = {num(Fr(P*d,100))} บาท', f'จ่าย = {P} − {num(Fr(P*d,100))} = {num(Fr(P*(100-d),100))} บาท'), u='บาท')

def score_pct(rng, mc):
    T = rng.choice([20, 25, 40, 50, 80]); p = rng.choice([60, 70, 75, 80, 85, 90, 95])
    s = Fr(T * p, 100)
    if s.denominator != 1: return score_pct(rng, mc)
    return NUM(f'สอบได้ {s} คะแนน จากคะแนนเต็ม {T} คิดเป็นร้อยละเท่าใด', p, ol(f'{fr(int(s), T)} × 100 = {p}'))

def whole(rng, mc):
    p, x = rng.choice([10, 20, 25, 40, 50, 75]), rng.choice([20, 40, 60, 80, 120, 200])
    part = Fr(p * x, 100)
    if part.denominator != 1: return whole(rng, mc)
    return NUM(f'{p}% ของจำนวนหนึ่งเท่ากับ {part} จำนวนนั้นคือเท่าใด', x, ol(f'{fr(p,100)} × x = {part}', f'x = {part} × {fr(100,p)} = {x}'))

def rect_area(rng, mc):
    w, l = R(rng, 3, 20), R(rng, 5, 30)
    return NUM(f'สี่เหลี่ยมผืนผ้ากว้าง {w} ซม. ยาว {l} ซม. มีพื้นที่กี่ตารางเซนติเมตร', w * l, ol(f'พื้นที่ = กว้าง × ยาว = {w} × {l} = {w*l} ตร.ซม.'), u='ตร.ซม.')

def tri_area_p(rng, mc):
    b, h = R(rng, 4, 24), 2 * R(rng, 2, 12)
    return NUM(f'สามเหลี่ยมมีฐานยาว {b} ซม. สูง {h} ซม. มีพื้นที่กี่ตารางเซนติเมตร', b * h // 2, ol(f'พื้นที่ = {fr(1,2)} × ฐาน × สูง = {fr(1,2)} × {b} × {h} = {b*h//2} ตร.ซม.'), u='ตร.ซม.')

def box_vol(rng, mc):
    a, b, c = R(rng, 2, 12), R(rng, 2, 12), R(rng, 2, 10)
    return NUM(f'กล่องทรงสี่เหลี่ยมมุมฉาก กว้าง {a} ซม. ยาว {b} ซม. สูง {c} ซม. มีปริมาตรกี่ลูกบาศก์เซนติเมตร', a * b * c, ol(f'ปริมาตร = {a} × {b} × {c} = {a*b*c} ลบ.ซม.'), u='ลบ.ซม.')

def sq_perim(rng, mc):
    a = R(rng, 3, 25)
    if rng.random() < .5:
        return NUM(f'สี่เหลี่ยมจัตุรัสยาวด้านละ {a} ซม. มีความยาวรอบรูปกี่เซนติเมตร', 4 * a, ol(f'ความยาวรอบรูป = 4 × {a} = {4*a} ซม.'), u='ซม.')
    return NUM(f'สี่เหลี่ยมจัตุรัสมีความยาวรอบรูป {4*a} ซม. มีพื้นที่กี่ตารางเซนติเมตร', a * a, ol(f'ด้านยาว {4*a} ÷ 4 = {a} ซม.', f'พื้นที่ = {a} × {a} = {a*a} ตร.ซม.'), u='ตร.ซม.')

def l_shape(rng, mc):
    W, H, w, h = R(rng, 8, 20), R(rng, 8, 20), 0, 0
    w, h = R(rng, 2, W - 3), R(rng, 2, H - 3)
    return NUM(f'รูปสี่เหลี่ยมผืนผ้าขนาด {W} × {H} ซม. ถูกตัดมุมออกเป็นสี่เหลี่ยมผืนผ้าขนาด {w} × {h} ซม. พื้นที่ที่เหลือกี่ตารางเซนติเมตร', W * H - w * h,
               ol(f'พื้นที่เต็ม = {W} × {H} = {W*H}', f'พื้นที่ที่ตัดออก = {w} × {h} = {w*h}', f'เหลือ {W*H} − {w*h} = {W*H - w*h} ตร.ซม.'), u='ตร.ซม.')

# ================= ม.ต้น =================
def exp_prod(rng, mc):
    b, m, n = rng.choice([2, 3, 5, 10, 'a', 'x']), R(rng, 2, 9), R(rng, 2, 9)
    corr = f'{b}<sup>{m+n}</sup>'
    return mc(f'{b}<sup>{m}</sup> × {b}<sup>{n}</sup> เท่ากับข้อใด', corr, [f'{b}<sup>{m*n}</sup>', f'{b}<sup>{abs(m-n) or 1}</sup>', f'{b}<sup>{m+n+1}</sup>', f'({b}²)<sup>{m+n}</sup>'],
              ol('ฐานเท่ากันคูณกัน นำเลขชี้กำลังมาบวกกัน', f'{b}<sup>{m}+{n}</sup> = {corr}'))

def exp_pow(rng, mc):
    b, m, n, p = rng.choice([2, 3]), R(rng, 2, 4), R(rng, 2, 3), 0
    p = m * n - R(rng, 1, 3)
    return NUM(f'({b}<sup>{m}</sup>)<sup>{n}</sup> ÷ {b}<sup>{p}</sup> มีค่าเท่าใด', b**(m * n - p), ol(f'({b}<sup>{m}</sup>)<sup>{n}</sup> = {b}<sup>{m*n}</sup>', f'{b}<sup>{m*n} − {p}</sup> = {b}<sup>{m*n-p}</sup> = {b**(m*n-p)}'))

def exp_neg(rng, mc):
    b, n = rng.choice([2, 3, 4, 5, 10]), R(rng, 1, 3)
    v = Fr(1, b**n)
    return mc(f'{b}<sup>−{n}</sup> มีค่าเท่าใด', fr(v), [num(-b**n), num(-b * n), fr(Fr(1, b * n)), fr(Fr(b, n)) if n > 1 else fr(Fr(1, b + 1)), num(b**n), fr(Fr(1, b**n + 1)), fr(Fr(1, 2 * b**n))],
              ol('a<sup>−n</sup> = ' + fr(1, 'a<sup>n</sup>'), f'{b}<sup>−{n}</sup> = {fr(1, f"{b}<sup>{n}</sup>")} = {fr(v)}'))

def sci(rng, mc):
    m, e = R(rng, 11, 99) / 10, R(rng, -7, 8)
    if e == 0: e = 3
    val = Fr(str(m)) * Fr(10)**e
    s = f'{float(val):.10f}'.rstrip('0').rstrip('.') if e < 0 else f'{int(val):,}'
    sup = lambda x: str(x).replace('-', '−')
    return mc(f'{s} เขียนในรูปสัญกรณ์วิทยาศาสตร์ได้ตรงกับข้อใด', f'{m} × 10<sup>{sup(e)}</sup>',
              [f'{m} × 10<sup>{sup(e+1)}</sup>', f'{m} × 10<sup>{sup(e-1)}</sup>', f'{int(m*10)} × 10<sup>{sup(e-1)}</sup>', f'{m} × 10<sup>{sup(-e)}</sup>'],
              ol('สัญกรณ์วิทยาศาสตร์: A × 10<sup>n</sup> โดย 1 ≤ A &lt; 10', f'เลื่อนจุดทศนิยม {abs(e)} ตำแหน่ง ได้ {m} × 10<sup>{sup(e)}</sup>'), h=f'{int(m*10)} × 10<sup>{sup(e-1)}</sup> มีค่าเท่ากัน แต่ไม่ใช่รูปสัญกรณ์วิทยาศาสตร์')

def exp_zero(rng, mc):
    a, b, c = R(rng, 2, 9), R(rng, 2, 5), R(rng, 2, 4)
    v = 1 + b**c
    return NUM(f'{a}<sup>0</sup> + {b}<sup>{c}</sup> มีค่าเท่าใด', v, ol(f'{a}<sup>0</sup> = 1 (จำนวนใดที่ไม่ใช่ 0 ยกกำลัง 0 เท่ากับ 1)', f'1 + {b**c} = {v}'))

def lin_simple(rng, mc):
    a, x, b = R(rng, 2, 9), R(rng, -6, 15), R(rng, -20, 20)
    return NUM(f'ถ้า {a}x{sgn(b)} = {num(a*x+b)} แล้ว x มีค่าเท่าใด', x, ol(f'{a}x = {num(a*x+b)}{sgn(-b)} = {num(a*x)}', f'x = {num(x)}'))

def consec(rng, mc):
    n, k = R(rng, 5, 60), rng.choice([3, 4, 5])
    s = sum(range(n, n + k))
    return NUM(f'จำนวนนับเรียงติดกัน {k} จำนวน รวมกันได้ {s} จำนวนที่น้อยที่สุดคือเท่าใด', n,
               ol(f'ให้จำนวนน้อยสุดเป็น x: x + (x+1) + … + (x+{k-1}) = {s}', f'{k}x + {k*(k-1)//2} = {s} → x = {n}'))

def rect_w(rng, mc):
    w, d = R(rng, 3, 20), R(rng, 2, 15); l = w + d
    return NUM(f'สี่เหลี่ยมผืนผ้ามีด้านยาวมากกว่าด้านกว้าง {d} ซม. ความยาวรอบรูป {2*(w+l)} ซม. ด้านกว้างยาวกี่เซนติเมตร', w,
               ol(f'ให้กว้าง x ยาว x + {d}', f'2(x + x + {d}) = {2*(w+l)} → 4x = {2*(w+l) - 2*d}', f'x = {w}'), u='ซม.')

def coins(rng, mc):
    a, b = R(rng, 3, 20), R(rng, 3, 20); n, T = a + b, 5 * a + 10 * b
    return NUM(f'มีเหรียญห้าบาทและเหรียญสิบบาทรวม {n} เหรียญ คิดเป็นเงิน {T} บาท มีเหรียญสิบบาทกี่เหรียญ', b,
               ol(f'ให้เหรียญสิบบาท x เหรียญ เหรียญห้าบาท {n} − x', f'10x + 5({n} − x) = {T} → 5x = {T - 5*n}', f'x = {b}'), u='เหรียญ')

def triple_mc(rng, mc):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41), (20, 21, 29)])
    k = rng.choice([1, 2, 3])
    wr = [(4, 5, 6), (2, 3, 4), (6, 7, 9), (5, 6, 8), (7, 8, 11), (4, 6, 9), (10, 11, 15)]
    rng.shuffle(wr)
    f = lambda t: ', '.join(map(str, t))
    return mc('ความยาวด้านชุดใดประกอบเป็นสามเหลี่ยมมุมฉากได้', f((a * k, b * k, c * k)), [f(t) for t in wr],
              ol('ตรวจว่า ด้านสั้น² + ด้านสั้น² = ด้านยาวสุด² หรือไม่', f'{(a*k)**2} + {(b*k)**2} = {(c*k)**2} = {c*k}²'))

def diag(rng, mc):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)])
    return NUM(f'สี่เหลี่ยมผืนผ้ากว้าง {a} ซม. ยาว {b} ซม. เส้นทแยงมุมยาวกี่เซนติเมตร', c, ol(f'd² = {a}² + {b}² = {a*a+b*b}', f'd = {c} ซม.'), u='ซม.')

def dist(rng, mc):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15)])
    x1, y1 = R(rng, -5, 5), R(rng, -5, 5)
    x2, y2 = x1 + a * rng.choice([1, -1]), y1 + b * rng.choice([1, -1])
    return NUM(f'ระยะห่างระหว่างจุด ({num(x1)}, {num(y1)}) และ ({num(x2)}, {num(y2)}) เท่ากับกี่หน่วย', c,
               ol(f'd = √[({num(x2)} − ({num(x1)}))² + ({num(y2)} − ({num(y1)}))²]', f'= √({a*a} + {b*b}) = {c}'))

def iso_h(rng, mc):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (12, 16, 20)])
    return NUM(f'สามเหลี่ยมหน้าจั่วมีด้านเท่ายาว {c} ซม. ฐานยาว {2*a} ซม. มีความสูงกี่เซนติเมตร', b, ol(f'ส่วนสูงแบ่งฐานครึ่ง: {a} ซม.', f'สูง = √({c}² − {a}²) = {b} ซม.'), u='ซม.')

def diff_sq(rng, mc):
    a, k = R(rng, 2, 12), rng.choice([1, 4, 9, 16, 25])
    rk = math.isqrt(k); A = f'{rk if rk>1 else ""}x'
    return mc(f'{k if k>1 else ""}x² − {a*a} แยกตัวประกอบได้ตรงกับข้อใด', f'({A} − {a})({A} + {a})', [f'({A} − {a})²', f'({A} + {a})²', f'({A} − {a*a})({A} + 1)', f'{k if k>1 else ""}(x − {a})(x + {a})' if k > 1 else f'(x − {a})(x + {a*a})'],
              ol('ผลต่างกำลังสอง: A² − B² = (A − B)(A + B)', f'({A})² − {a}² = ({A} − {a})({A} + {a})'))

def common(rng, mc):
    k, a, b = R(rng, 2, 9), R(rng, 2, 9), R(rng, 1, 9)
    if math.gcd(a, b) != 1: b += 1
    if math.gcd(a, b) != 1: return common(rng, mc)
    return mc(f'{k*a}x² + {k*b}x แยกตัวประกอบได้ตรงกับข้อใด', f'{k}x({a}x + {b})', [f'{k}({a}x² + {b}x)', f'x({a}x + {k*b})', f'{k}x({a}x + {b}x)', f'{k*a}x(x + {b})'],
              ol(f'ตัวร่วมมากที่สุดคือ {k}x', f'{k*a}x² + {k*b}x = {k}x({a}x + {b})'))

def perfect(rng, mc):
    a = R(rng, 1, 9); s = rng.choice([1, -1])
    corr = f'(x {"+" if s>0 else "−"} {a})²'
    return mc(f'x² {"+" if s>0 else "−"} {2*a}x + {a*a} แยกตัวประกอบได้ตรงกับข้อใด', corr, [f'(x {"−" if s>0 else "+"} {a})²', f'(x + {a})(x − {a})', f'(x {"+" if s>0 else "−"} {2*a})²', f'(x {"+" if s>0 else "−"} {a*a})(x + 1)'],
              ol('กำลังสองสมบูรณ์: A² ± 2AB + B² = (A ± B)²', f'= {corr}'))

def big_root(rng, mc):
    p, q = rng.sample([x for x in range(-8, 12) if x], 2)
    if p + q == 0: return big_root(rng, mc)
    return NUM(f'คำตอบที่มากกว่าของสมการ x²{sgn(-(p+q))}x{sgn(p*q)} = 0 คือเท่าใด'.replace(' + 0x', '').replace(' − 0x', ''), max(p, q),
               ol(f'(x − ({p}))(x − ({q})) = 0', f'x = {p} หรือ {q}', f'คำตอบที่มากกว่าคือ {max(p,q)}'))

def avg_speed(rng, mc):
    d1, t1, d2, t2 = R(rng, 20, 150), R(rng, 1, 3), R(rng, 20, 150), R(rng, 1, 3)
    v = Fr(d1 + d2, t1 + t2)
    if Fr(v * 100).denominator != 1: return avg_speed(rng, mc)
    return NUM(f'รถวิ่งได้ {d1} กม. ในเวลา {t1} ชั่วโมง แล้ววิ่งต่ออีก {d2} กม. ในเวลา {t2} ชั่วโมง อัตราเร็วเฉลี่ยตลอดทางกี่ กม./ชม.', v,
               ol(f'ระยะทางรวม = {d1+d2} กม., เวลารวม = {t1+t2} ชม.', f'อัตราเร็วเฉลี่ย = {d1+d2} ÷ {t1+t2} = {num(v)} กม./ชม.'), u='km/h', h='อัตราเร็วเฉลี่ย = ระยะทางรวม ÷ เวลารวม (ไม่ใช่เฉลี่ยของอัตราเร็ว)')

def dvt(rng, mc):
    v, t = R(rng, 2, 30), R(rng, 3, 60)
    k = rng.randrange(2)
    if k: return NUM(f'วัตถุเคลื่อนที่ด้วยอัตราเร็วคงตัว {v} m/s เป็นเวลา {t} s ได้ระยะทางกี่เมตร', v * t, ol(f's = vt = {v} × {t} = {v*t} m'), u='m')
    return NUM(f'นักวิ่งวิ่งด้วยอัตราเร็วคงตัว {v} m/s ต้องใช้เวลากี่วินาทีในการวิ่ง {v*t} m', t, ol(f't = s ÷ v = {v*t} ÷ {v} = {t} s'), u='s')

def disp(rng, mc):
    a, b, t = R(rng, 10, 60), R(rng, 5, 40), rng.choice([5, 10, 20])
    if a == b: a += 5
    D = abs(a - b); d = 'ตะวันออก' if a > b else 'ตะวันตก'
    v = Fr(D, t)
    corr = f'{num(v)} m/s ทิศ{d}'
    return mc(f'เดินไปทางตะวันออก {a} m แล้วเดินกลับทางตะวันตก {b} m ใช้เวลารวม {t} s ความเร็วเฉลี่ยเป็นเท่าใด', corr,
              [f'{num(Fr(a+b, t))} m/s ทิศ{d}', f'{num(v)} m/s ทิศ{"ตะวันตก" if d=="ตะวันออก" else "ตะวันออก"}', f'{num(Fr(a+b, t))} m/s ทิศตะวันออก' if d != 'ตะวันออก' else f'{num(Fr(a+b,t))} m/s ทิศตะวันตก', f'{num(v*2)} m/s ทิศ{d}'],
              ol(f'การกระจัด = {a} − {b} = {num(a-b)} m → {D} m ทิศ{d}', f'ความเร็วเฉลี่ย = {D} ÷ {t} = {num(v)} m/s ทิศ{d}'), h='ความเร็วใช้การกระจัด ไม่ใช่ระยะทาง')

def p_fa(rng, mc):
    F, A = R(rng, 50, 2000), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), 1, 2, Fr(1, 4)])
    return NUM(f'แรง {F} N กดลงบนพื้นที่ {num(A)} m² ความดันเป็นกี่ปาสคาล', F / A, ol(f'P = F ÷ A = {F} ÷ {num(A)} = {num(F/A)} Pa'), u='Pa')

def buoy_s(rng, mc):
    V = rng.choice([Fr(1, 1000), Fr(2, 1000), Fr(5, 1000), Fr(1, 100), Fr(2, 100)])
    return NUM(f'วัตถุปริมาตร {num(V)} m³ จมมิดในน้ำ (ρ = 1000 kg/m³, g = 10 m/s²) ได้รับแรงลอยตัวกี่นิวตัน', 10000 * V, ol(f'F<sub>B</sub> = ρVg = 1000 × {num(V)} × 10 = {num(10000*V)} N'), u='N')

def mass_rho(rng, mc):
    rho, V = rng.choice([(Fr(27, 10), 'อะลูมิเนียม'), (Fr(79, 10), 'เหล็ก'), (Fr(193, 10), 'ทองคำ'), (1, 'น้ำ'), (Fr(9, 10), 'น้ำแข็ง')]), 10 * R(rng, 1, 20)
    return NUM(f'{rho[1]} (ความหนาแน่น {num(rho[0])} g/cm³) ปริมาตร {V} cm³ มีมวลกี่กรัม', rho[0] * V, ol(f'm = ρV = {num(rho[0])} × {V} = {num(rho[0]*V)} g'), u='g')

def pvi(rng, mc):
    V, I = rng.choice([12, 110, 220, 9, 6]), rng.choice([Fr(1, 2), 1, 2, 3, 5, Fr(1, 4)])
    if rng.random() < .5:
        return NUM(f'เครื่องใช้ไฟฟ้าต่อกับ {V} V มีกระแส {num(I)} A ใช้กำลังไฟฟ้ากี่วัตต์', V * I, ol(f'P = VI = {V} × {num(I)} = {num(V*I)} W'), u='W')
    P = V * I
    return NUM(f'เครื่องใช้ไฟฟ้า {num(P)} W ต่อกับ {V} V มีกระแสไหลกี่แอมแปร์', I, ol(f'I = P ÷ V = {num(P)} ÷ {V} = {num(I)} A'), u='A')

def work_fs(rng, mc):
    F, s = R(rng, 5, 200), R(rng, 2, 30)
    return NUM(f'ออกแรง {F} N ดันกล่องไปตามทิศของแรงเป็นระยะ {s} m งานที่ทำเป็นกี่จูล', F * s, ol(f'W = Fs = {F} × {s} = {F*s} J'), u='J')

def power_t(rng, mc):
    W, t = rng.choice([600, 1200, 1500, 3000, 4800]), rng.choice([2, 3, 5, 10, 12, 20, 30])
    return NUM(f'เครื่องยนต์ทำงาน {W} J ในเวลา {t} s มีกำลังกี่วัตต์', Fr(W, t), ol(f'P = W ÷ t = {W} ÷ {t} = {num(Fr(W,t))} W'), u='W')

# ================= ม.ปลาย =================
def subsets(rng, mc):
    n = R(rng, 2, 7); els = ', '.join(map(str, range(1, n + 1)))
    if rng.random() < .5:
        return NUM(f'A = {{{els}}} จำนวนสับเซตทั้งหมดของ A มีกี่เซต', 2**n, ol(f'n(A) = {n}', f'จำนวนสับเซต = 2<sup>{n}</sup> = {2**n}'))
    return NUM(f'A = {{{els}}} จำนวนสับเซตแท้ของ A มีกี่เซต', 2**n - 1, ol(f'จำนวนสับเซตทั้งหมด = 2<sup>{n}</sup> = {2**n}', f'สับเซตแท้ไม่นับ A เอง: {2**n} − 1 = {2**n-1}'))

def union(rng, mc):
    i, a, b = R(rng, 2, 15), R(rng, 3, 25), R(rng, 3, 25)
    return NUM(f'n(A) = {a+i}, n(B) = {b+i}, n(A ∩ B) = {i} แล้ว n(A ∪ B) เท่ากับเท่าใด', a + b + i, ol(f'n(A ∪ B) = {a+i} + {b+i} − {i} = {a+b+i}'))

def venn(rng, mc):
    both, m, p, none = R(rng, 3, 15), R(rng, 5, 20), R(rng, 5, 20), R(rng, 0, 10)
    N = both + m + p + none
    return NUM(f'นักเรียน {N} คน ชอบคณิต {m+both} คน ชอบฟิสิกส์ {p+both} คน ชอบทั้งสองวิชา {both} คน มีกี่คนที่ไม่ชอบทั้งสองวิชา', none,
               ol(f'ชอบอย่างน้อยหนึ่งวิชา = {m+both} + {p+both} − {both} = {m+p+both}', f'ไม่ชอบทั้งสอง = {N} − {m+p+both} = {none}'), u='คน', h='วาดแผนภาพเวนน์')

def diffset(rng, mc):
    A = sorted(rng.sample(range(1, 15), R(rng, 4, 7))); B = sorted(rng.sample(range(1, 15), R(rng, 4, 7)))
    d = [x for x in A if x not in B]
    return NUM(f'A = {{{", ".join(map(str,A))}}} และ B = {{{", ".join(map(str,B))}}} แล้ว n(A − B) เท่ากับเท่าใด', len(d),
               ol('A − B คือสมาชิกที่อยู่ใน A แต่ไม่อยู่ใน B', f'A − B = {{{", ".join(map(str,d))}}}' if d else 'A − B = ∅', f'n(A − B) = {len(d)}'))

def inter(rng, mc):
    A = sorted(rng.sample(range(1, 20), 6)); B = sorted(rng.sample(range(1, 20), 6))
    I = [x for x in A if x in B]
    if not I: return inter(rng, mc)
    s = lambda X: '{' + ', '.join(map(str, X)) + '}'
    U = sorted(set(A) | set(B))
    return mc(f'A = {s(A)} และ B = {s(B)} แล้ว A ∩ B คือข้อใด', s(I), [s(U), s([x for x in A if x not in B]) if any(x not in B for x in A) else '∅', s([x for x in B if x not in A]) if any(x not in A for x in B) else '{0}', s(I[:-1]) if len(I) > 1 else '∅'],
              ol('A ∩ B คือสมาชิกที่อยู่ทั้งใน A และ B', f'= {s(I)}'))

def vuat(rng, mc):
    u, a, t = R(rng, 0, 15), R(rng, 1, 6), R(rng, 2, 10)
    return NUM(f'รถมีความเร็วต้น {u} m/s เร่งด้วยความเร่งคงตัว {a} m/s² เป็นเวลา {t} s ความเร็วสุดท้ายกี่ m/s', u + a * t, ol(f'v = u + at = {u} + {a}({t}) = {u+a*t} m/s'), u='m/s')

def suat(rng, mc):
    u, a, t = R(rng, 0, 10), 2 * R(rng, 1, 3), R(rng, 2, 8)
    s = u * t + a * t * t // 2
    return NUM(f'วัตถุมีความเร็วต้น {u} m/s ความเร่ง {a} m/s² ในเวลา {t} s เคลื่อนที่ได้ระยะทางกี่เมตร', s, ol(f's = ut + {fr(1,2)}at² = {u}({t}) + {fr(1,2)}({a})({t})² = {s} m'), u='m')

def ff_time(rng, mc):
    t = R(rng, 1, 6); h = 5 * t * t
    return NUM(f'ปล่อยวัตถุตกอย่างอิสระจากที่สูง {h} m ใช้เวลากี่วินาทีจึงถึงพื้น (g = 10 m/s²)', t, ol(f'{h} = {fr(1,2)}(10)t² = 5t²', f't² = {t*t} → t = {t} s'), u='s')

def stopping(rng, mc):
    u, a = rng.choice([10, 20, 30, 40]), rng.choice([2, 4, 5, 8, 10])
    s = Fr(u * u, 2 * a)
    return NUM(f'รถวิ่งด้วยความเร็ว {u} m/s เบรกด้วยความหน่วง {a} m/s² จนหยุด เคลื่อนที่ได้ระยะทางกี่เมตรขณะเบรก', s, ol(f'v² = u² − 2as → 0 = {u*u} − 2({a})s', f's = {fr(u*u, 2*a)} = {num(s)} m'), u='m')

def fma(rng, mc):
    m, a = R(rng, 1, 20), R(rng, 1, 8)
    k = rng.randrange(2)
    if k: return NUM(f'แรงลัพธ์ {m*a} N กระทำต่อวัตถุมวล {m} kg วัตถุมีความเร่งกี่ m/s²', a, ol(f'a = F ÷ m = {m*a} ÷ {m} = {a} m/s²'), u='m/s²')
    return NUM(f'ต้องใช้แรงลัพธ์กี่นิวตันทำให้วัตถุมวล {m} kg มีความเร่ง {a} m/s²', m * a, ol(f'F = ma = {m} × {a} = {m*a} N'), u='N')

def lift(rng, mc):
    m, a = R(rng, 40, 80), R(rng, 1, 3); up = rng.random() < .5
    N = m * (10 + a) if up else m * (10 - a)
    return NUM(f'คนมวล {m} kg ยืนในลิฟต์ที่กำลังเคลื่อนที่{"ขึ้นด้วยความเร่ง" if up else "ลงด้วยความเร่ง"} {a} m/s² พื้นลิฟต์ดันคนด้วยแรงกี่นิวตัน (g = 10 m/s²)', N,
               ol(f'{"N − mg = ma → N = m(g + a)" if up else "mg − N = ma → N = m(g − a)"}', f'N = {m}(10 {"+" if up else "−"} {a}) = {N} N'), u='N')

def two_blocks(rng, mc):
    m1, m2 = R(rng, 1, 6), R(rng, 1, 6); F = (m1 + m2) * R(rng, 1, 5)
    a = Fr(F, m1 + m2)
    return NUM(f'กล่องมวล {m1} kg และ {m2} kg ผูกติดกันวางบนพื้นลื่น ดึงด้วยแรง {F} N ระบบมีความเร่งกี่ m/s²', a, ol(f'a = {fr("F","m₁ + m₂")} = {F} ÷ {m1+m2} = {num(a)} m/s²'), u='m/s²')

def p_mv(rng, mc):
    m, v = R(rng, 1, 60), R(rng, 2, 30)
    return NUM(f'วัตถุมวล {m} kg เคลื่อนที่ด้วยความเร็ว {v} m/s มีโมเมนตัมกี่ kg·m/s', m * v, ol(f'p = mv = {m} × {v} = {m*v} kg·m/s'), u='kg·m/s')

def recoil(rng, mc):
    mb, vb, mg = rng.choice([Fr(1, 100), Fr(1, 50), Fr(1, 20)]), rng.choice([200, 300, 400, 500]), rng.choice([2, 4, 5])
    v = mb * vb / mg
    return NUM(f'ปืนมวล {mg} kg ยิงกระสุนมวล {num(mb)} kg ออกไปด้วยความเร็ว {vb} m/s ปืนสะท้อนถอยหลังด้วยความเร็วกี่ m/s', v,
               ol('โมเมนตัมก่อนยิง = 0', f'{mg}V = {num(mb)} × {vb} → V = {num(v)} m/s'), u='m/s')

def charge_i(rng, mc):
    Q, t = R(rng, 2, 60), rng.choice([2, 4, 5, 10, 20])
    return NUM(f'ประจุ {Q} C ไหลผ่านลวดในเวลา {t} s กระแสไฟฟ้ากี่แอมแปร์', Fr(Q, t), ol(f'I = Q ÷ t = {Q} ÷ {t} = {num(Fr(Q,t))} A'), u='A')

TOPICS = {
    'p-frac':     [frac_add, frac_sub, frac_of, frac_div, mixed, compare, frac_word],
    'p-gcd':      [gcd2, lcm2, gcd3, lcm3, ribbon, bus, gcd_lcm_other],
    'p-percent':  [pct_of, disc_price, score_pct, whole, pct_change],
    'p-geo':      [rect_area, tri_area_p, box_vol, sq_perim, l_shape, rect_perim, circle_area, circ, cube_sa],
    'm-exp':      [exp_prod, exp_pow, exp_neg, sci, exp_zero, exp_laws],
    'm-linear':   [lin_simple, lin_eq, consec, rect_w, coins],
    'm-pyth':     [pyth_hyp, triple_mc, diag, dist, iso_h],
    'm-factor':   [factor_mc, diff_sq, common, perfect, big_root],
    'm-stat':     [mean_l, median_l, range_mode, mean_add],
    'mp-speed':   [kmh, avg_speed, dvt, disp],
    'mp-pressure':[density, pressure, p_fa, buoy_s, mass_rho],
    'mp-elec':    [ohm, resist, bill, pvi],
    'mp-work':    [work_fs, energy, power_w, power_t, fall_speed],
    'h-set':      [subsets, union, venn, diffset, inter],
    'h-func':     [f_lin, compo, inv_val, vertex, intercepts],
    'h-log':      [log_vals, log_rule, change_base, exp_eq, solve_exp, log_eq],
    'h-trig':     [trig_val, trig_quad, trig_tri, rad, tri_area, cos_law],
    'h-seq':      [ar_nth, ge_nth, ar_sum, inf_geo, gauss, two_terms],
    'h-prob':     [dice_sum, at_least_head, choose, fact_arr, word_arr, together, balls],
    'h-calc':     [deriv_at, lim0, integ, rel_min, lim_inf, tangent],
    'hp-kin':     [vuat, suat, ff_time, max_h, stopping],
    'hp-newton':  [fma, friction, lift, two_blocks, weight],
    'hp-mom':     [p_mv, stick, impulse, recoil],
    'hp-wave':    [vfl, echo, freq, beats, string_f],
    'hp-elec':    [coulomb, power_r, charge_i, resist, ohm],
}
NEW = {}
NOPT = 4
