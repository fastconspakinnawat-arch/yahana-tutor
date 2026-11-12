"""A-Level ฟิสิกส์"""
from core import *
from bank_a1 import MCN
import math
R = lambda rng, a, b: rng.randint(a, b)
G = 'g = 10 m/s²'

# ---------- ap-mech ----------
def projectile(rng, mc):
    t, v = R(rng, 1, 5), R(rng, 4, 25); h = 5 * t * t
    return NUM(f'ขว้างวัตถุในแนวระดับด้วยความเร็ว {v} m/s จากหน้าผาสูง {h} m วัตถุตกห่างจากฐานหน้าผากี่เมตร ({G})', v * t,
               ol(f'แนวดิ่ง: {h} = {fr(1,2)}(10)t² → t = {t} s', f'แนวราบ: x = {v} × {t} = {v*t} m'), u='m', h='หาเวลาจากแนวดิ่งก่อน')

def centri(rng, mc):
    m, r, v = rng.choice([Fr(1, 2), 1, 2, 3, Fr(1, 5)]), R(rng, 1, 5), R(rng, 2, 10)
    F = m * v * v / r
    return NUM(f'วัตถุมวล {num(m)} kg เคลื่อนที่เป็นวงกลมรัศมี {r} m ด้วยอัตราเร็ว {v} m/s แรงสู่ศูนย์กลางมีขนาดกี่นิวตัน', F,
               ol(f'F<sub>c</sub> = {fr("mv²","r")} = {fr(f"{num(m)} × {v*v}", r)} = {num(F)} N'), u='N')

def g_height(rng, mc):
    k = R(rng, 1, 4); v = Fr(1, (k + 1)**2)
    return MCN(mc, f'ที่ความสูงจากผิวโลก {k if k>1 else ""}R (R = รัศมีโลก) ความเร่งโน้มถ่วงมีค่าเป็นกี่เท่าของที่ผิวโลก', v,
               ol(f'g ∝ {fr(1,"r²")} โดย r วัดจากจุดศูนย์กลางโลก', f'r = {k+1}R → g เป็น {fr(1, (k+1)**2)} เท่า'), extra=[Fr(1, k + 1), Fr(1, k * k), Fr(1, (k + 2)**2)], prob=True)

def friction(rng, mc):
    m, mu = R(rng, 2, 10), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(3, 10), Fr(1, 2)])
    F = 10 * m * mu + m * R(rng, 1, 5)
    a = (F - mu * m * 10) / m
    return NUM(f'ออกแรง {num(F)} N ลากกล่องมวล {m} kg บนพื้นราบ สัมประสิทธิ์ความเสียดทานจลน์ {num(mu)} กล่องมีความเร่งกี่ m/s² ({G})', a,
               ol(f'f = μmg = {num(mu)} × {m} × 10 = {num(mu*m*10)} N', f'a = {fr(f"{num(F)} − {num(mu*m*10)}", m)} = {num(a)} m/s²'), u='m/s²')

def incline(rng, mc):
    ang, m = rng.choice([30, 30, 37, 53]), R(rng, 1, 8)
    s = {30: Fr(1, 2), 37: Fr(3, 5), 53: Fr(4, 5)}[ang]
    return NUM(f'วัตถุมวล {m} kg ไถลลงพื้นเอียงลื่นที่ทำมุม {ang}° กับแนวระดับ มีความเร่งกี่ m/s² ({G}' + (', sin 37° = 0.6, sin 53° = 0.8)' if ang != 30 else ')'), 10 * s,
               ol('แรงลัพธ์ตามพื้นเอียง = mg sin θ', f'a = g sin θ = 10 × {num(s)} = {num(10*s)} m/s² (ไม่ขึ้นกับมวล)'), u='m/s²')

def fall_speed(rng, mc):
    v = 10 * R(rng, 1, 5); h = v * v // 20
    return NUM(f'ปล่อยวัตถุจากที่สูง {h} m ทันทีก่อนถึงพื้นวัตถุมีอัตราเร็วกี่ m/s (ไม่คิดแรงต้านอากาศ, {G})', v,
               ol('mgh = ½mv²', f'v = √(2gh) = √(2 × 10 × {h}) = {v} m/s'), u='m/s')

def stick(rng, mc):
    m1, v1, m2 = R(rng, 1, 6), R(rng, 2, 12), R(rng, 1, 6)
    v = Fr(m1 * v1, m1 + m2)
    if Fr(v * 100).denominator != 1: return stick(rng, mc)
    return NUM(f'รถทดลองมวล {m1} kg วิ่งด้วยความเร็ว {v1} m/s ชนรถมวล {m2} kg ที่หยุดนิ่ง แล้วติดไปด้วยกัน ความเร็วหลังชนกี่ m/s', v,
               ol(f'อนุรักษ์โมเมนตัม: {m1}({v1}) = ({m1} + {m2})v', f'v = {m1*v1} ÷ {m1+m2} = {num(v)} m/s'), u='m/s')

def impulse(rng, mc):
    m, dv, t = rng.choice([Fr(1, 2), Fr(1, 5), Fr(1, 10), 1, 2]), R(rng, 5, 30), rng.choice([Fr(1, 10), Fr(1, 20), Fr(1, 50), Fr(1, 5)])
    F = m * dv / t
    return NUM(f'ลูกบอลมวล {num(m)} kg ความเร็วเปลี่ยนไป {dv} m/s ในเวลา {num(t)} s แรงเฉลี่ยที่กระทำต่อลูกบอลมีขนาดกี่นิวตัน', F,
               ol(f'F = {fr("Δp","Δt")} = {fr(f"{num(m)} × {dv}", num(t))} = {num(F)} N'), u='N')

def max_h(rng, mc):
    v = 10 * R(rng, 1, 4) if rng.random() < .5 else rng.choice([5, 15, 25])
    h = Fr(v * v, 20)
    return NUM(f'โยนลูกบอลขึ้นตรง ๆ ด้วยความเร็วต้น {v} m/s ลูกบอลขึ้นไปได้สูงสุดกี่เมตร ({G})', h,
               ol('ที่จุดสูงสุด v = 0: 0 = u² − 2gh', f'h = {fr("u²","2g")} = {fr(v*v,20)} = {num(h)} m'), u='m')

# ---------- ap-shm ----------
def spring_T(rng, mc):
    m, k = rng.choice([(1, 100), (2, 200), (4, 100), (1, 25), (9, 100), (1, 400), (2, 50), (8, 200)])
    c = Fr(2) * Fr(math.isqrt(m * 10**6 // k), 1000)
    show = lambda x: f'{num(x)}π s'
    return mc(f'มวล {m} kg ติดสปริงที่มีค่านิจ {k} N/m คาบการสั่นเท่ากับข้อใด', show(c), [show(c * 2), show(c / 2), show(c * 4), show(c + Fr(1, 10)), show(c * 10), show(c * 3)],
              ol(f'T = 2π√(m/k) = 2π√({fr(m,k)})', f'= 2π × {num(c/2)} = {num(c)}π s'))

def pend_scale(rng, mc):
    k = rng.choice([4, 9, 16, Fr(1, 4)]); v = Fr(math.isqrt(int(k * 16)), 4)
    w = lambda x: f'{fr(x)} เท่า' if Fr(x).denominator > 1 else f'{num(x)} เท่า'
    return mc(f'ถ้าเปลี่ยนความยาวเชือกลูกตุ้มอย่างง่ายเป็น {fr(k)} เท่าของเดิม คาบจะเป็นกี่เท่าของเดิม', w(v), [w(k), w(k * k), w(1 / v), 'เท่าเดิม', w(v * 2), w(v / 2)],
              ol('T = 2π√(L/g) → T ∝ √L', f'√{fr(k)} = {fr(v)} เท่า'))

def freq(rng, mc):
    T = rng.choice([Fr(1, 2), Fr(1, 4), Fr(1, 5), Fr(2, 5), Fr(1, 10), 2, 4, Fr(1, 20)])
    return NUM(f'วัตถุสั่นแบบฮาร์มอนิกอย่างง่ายครบ 1 รอบใช้เวลา {num(T)} s มีความถี่กี่เฮิรตซ์', 1 / T, ol(f'f = {fr(1,"T")} = {fr(1, num(T))} = {num(1/T)} Hz'), u='Hz')

def spring_E(rng, mc):
    k, x = rng.choice([100, 200, 400, 500, 50]), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 20), Fr(3, 10)])
    if rng.random() < .5:
        return NUM(f'สปริงค่านิจ {k} N/m ถูกยืดออก {num(x)} m มีพลังงานศักย์ยืดหยุ่นกี่จูล', Fr(1, 2) * k * x * x, ol(f'E = {fr(1,2)}kx² = {fr(1,2)} × {k} × ({num(x)})² = {num(Fr(1,2)*k*x*x)} J'), u='J')
    return NUM(f'สปริงค่านิจ {k} N/m ถูกยืดออก {num(x)} m ต้องใช้แรงกี่นิวตัน', k * x, ol(f'F = kx = {k} × {num(x)} = {num(k*x)} N'), u='N')

def vmax(rng, mc):
    A, w = rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 20), Fr(1, 2)]), R(rng, 2, 20)
    return NUM(f'วัตถุสั่นแบบฮาร์มอนิกอย่างง่ายด้วยแอมพลิจูด {num(A)} m และความถี่เชิงมุม {w} rad/s อัตราเร็วสูงสุดเท่ากับกี่ m/s', A * w, ol(f'v<sub>max</sub> = Aω = {num(A)} × {w} = {num(A*w)} m/s'), u='m/s')

def planet_pend(rng, mc):
    k, root = rng.choice([(4, 2), (9, 3), (16, 4), (Fr(1, 4), Fr(1, 2))])
    v = 1 / Fr(root)
    w = lambda x: f'{fr(x)} เท่า' if Fr(x).denominator > 1 else f'{num(x)} เท่า'
    return mc(f'นำลูกตุ้มอย่างง่ายไปแกว่งบนดาวที่มีความเร่งโน้มถ่วงเป็น {fr(k)} เท่าของโลก คาบจะเป็นกี่เท่าของบนโลก', w(v), [w(Fr(root)), w(k), w(1 / Fr(k)), 'เท่าเดิม', w(v * 2), w(v / 2)],
              ol(f'T = 2π√(L/g) → T ∝ {fr(1, "√g")}', f'คาบเป็น {fr(1, "√(" + str(num(k) if Fr(k).denominator == 1 else "1/4") + ")")} = {fr(v)} เท่า'))

# ---------- ap-em ----------
def cap(rng, mc):
    C, V = rng.choice([1, 2, 4, 5, 10, 20, 50]), rng.choice([3, 6, 9, 10, 12, 20, 100])
    if rng.random() < .5:
        return NUM(f'ตัวเก็บประจุ {C} μF ต่อกับความต่างศักย์ {V} V เก็บประจุได้กี่ไมโครคูลอมบ์', C * V, ol(f'Q = CV = {C} μF × {V} V = {C*V} μC'), u='μC')
    return NUM(f'ตัวเก็บประจุ {C} μF ต่อกับความต่างศักย์ {V} V สะสมพลังงานกี่ไมโครจูล', Fr(C * V * V, 2), ol(f'U = {fr(1,2)}CV² = {fr(1,2)} × {C} × {V}² = {num(Fr(C*V*V,2))} μJ'), u='μJ')

def ilb(rng, mc):
    I, L, B = R(rng, 1, 10), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), 1, 2]), rng.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), 1])
    return NUM(f'ลวดยาว {num(L)} m มีกระแส {I} A วางตั้งฉากกับสนามแม่เหล็ก {num(B)} T แรงที่กระทำต่อลวดกี่นิวตัน', I * L * B, ol(f'F = ILB sin 90° = {I} × {num(L)} × {num(B)} = {num(I*L*B)} N'), u='N')

def trafo(rng, mc):
    Np, Ns = rng.choice([(1000, 50), (500, 100), (200, 1000), (2000, 100), (100, 500), (1200, 60), (400, 20)])
    Vp = rng.choice([220, 110, 240, 12])
    Vs = Fr(Vp * Ns, Np)
    return NUM(f'หม้อแปลงอุดมคติมีขดลวดปฐมภูมิ {Np} รอบ ทุติยภูมิ {Ns} รอบ ต่อไฟ {Vp} V ด้านทุติยภูมิได้ความต่างศักย์กี่โวลต์', Vs,
               ol(f'{fr("V<sub>s</sub>","V<sub>p</sub>")} = {fr("N<sub>s</sub>","N<sub>p</sub>")}', f'V<sub>s</sub> = {Vp} × {fr(Ns, Np)} = {num(Vs)} V'), u='V')

def coulomb(rng, mc):
    a, b = rng.choice([(2, 1), (1, 2), (3, 1), (1, 3), (2, 2), (4, 2)])  # ประจุคูณ a เท่า, ระยะคูณ b เท่า
    c = rng.choice([1, 2])
    v = Fr(a * c, b * b)
    w = lambda x: f'{fr(x)} เท่า' if Fr(x).denominator > 1 else f'{num(x)} เท่า'
    parts = ([f'ประจุตัวหนึ่งเพิ่มเป็น {a} เท่า'] if a > 1 else []) + ([f'อีกตัวเพิ่มเป็น {c} เท่า'] if c > 1 else []) + ([f'ระยะห่างเพิ่มเป็น {b} เท่า'] if b > 1 else [])
    if not parts: return coulomb(rng, mc)
    return mc(f'ประจุสองตัวออกแรงต่อกัน F ถ้า{" และ".join(parts)} แรงใหม่เป็นกี่เท่าของ F', w(v), [w(Fr(a * c, b)), w(Fr(b * b, a * c)), w(Fr(a * c * b * b)), w(v * 2), w(v / 2), w(v * 4), w(v / 4), 'เท่าเดิม'],
              ol(f'F = {fr("kq₁q₂","r²")} → F ∝ {fr("q₁q₂","r²")}', f'= {fr(f"{a} × {c}", f"{b}²")} = {fr(v)} เท่า'))

def power_r(rng, mc):
    V, P = rng.choice([(220, 1100), (220, 2200), (220, 880), (220, 440), (110, 550), (12, 24), (12, 36), (220, 1000)])
    return NUM(f'เครื่องใช้ไฟฟ้าระบุ {V} V {P} W มีความต้านทานกี่โอห์ม', Fr(V * V, P), ol(f'R = {fr("V²","P")} = {fr(f"{V}²", P)} = {num(Fr(V*V,P))} Ω'), u='Ω')

def efield(rng, mc):
    V, d, q = rng.choice([100, 200, 500, 1000]), rng.choice([Fr(1, 100), Fr(1, 50), Fr(1, 10), Fr(1, 20)]), R(rng, 1, 9)
    E = V / d
    return NUM(f'แผ่นโลหะขนานห่างกัน {num(d)} m มีความต่างศักย์ {V} V ประจุ {q} μC ระหว่างแผ่นได้รับแรงกี่มิลลินิวตัน', E * q / 1000,
               ol(f'E = V/d = {V} ÷ {num(d)} = {num(E)} V/m', f'F = qE = {q} × 10<sup>−6</sup> × {num(E)} = {num(E*q/10**6)} N = {num(E*q/1000)} mN'), u='mN')

def circuit(rng, mc):
    a, b, r3 = rng.choice([(6, 3), (12, 6), (4, 4), (6, 12), (20, 5), (3, 6)]), None, R(rng, 1, 8)
    a, b = a
    Rp = Fr(a * b, a + b); Rt = Rp + r3
    V = Rt * R(rng, 1, 4)
    if Fr(V).denominator != 1: return circuit(rng, mc)
    return NUM(f'ตัวต้านทาน {a} Ω และ {b} Ω ต่อขนานกัน แล้วต่ออนุกรมกับตัวต้านทาน {r3} Ω และแบตเตอรี่ {num(V)} V กระแสจากแบตเตอรี่เท่ากับกี่แอมแปร์', V / Rt,
               ol(f'R<sub>ขนาน</sub> = {fr(f"{a} × {b}", f"{a} + {b}")} = {num(Rp)} Ω', f'R<sub>รวม</sub> = {num(Rp)} + {r3} = {num(Rt)} Ω', f'I = {num(V)} ÷ {num(Rt)} = {num(V/Rt)} A'), u='A')

# ---------- ap-modern ----------
def halflife(rng, mc):
    T, n = rng.choice([2, 3, 5, 8, 10]), R(rng, 2, 5)
    v = Fr(1, 2**n)
    return MCN(mc, f'สารกัมมันตรังสีมีครึ่งชีวิต {T} วัน เมื่อผ่านไป {T*n} วัน จะเหลือสารกี่ส่วนของเดิม', v,
               ol(f'{T*n} ÷ {T} = {n} ช่วงครึ่งชีวิต', f'เหลือ ({fr(1,2)})<sup>{n}</sup> = {fr(v)}'), extra=[Fr(1, 2 * n), Fr(1, n), Fr(1, 2**(n + 1)), Fr(1, 2**(n - 1))], prob=True)

def photon_ratio(rng, mc):
    k = rng.choice([2, 3, 4, Fr(1, 2), Fr(1, 3)])
    w = lambda x: f'{fr(x)} เท่า' if Fr(x).denominator > 1 else f'{num(x)} เท่า'
    word = f'ลดลงเหลือ {fr(1/Fr(k))}' if k > 1 else f'เพิ่มเป็น {num(1/Fr(k))}'
    return mc(f'ถ้าความยาวคลื่นของแสง{word}เท่าของเดิม พลังงานของโฟตอนจะเป็นกี่เท่าของเดิม', w(k), [w(1 / Fr(k)), w(Fr(k) ** 2), 'เท่าเดิม', w(Fr(k) * 2), w(1 / Fr(k) ** 2), w(Fr(k) * 4)],
              ol(f'E = {fr("hc","λ")} → E ∝ {fr(1,"λ")}', f'พลังงานเป็น {fr(k)} เท่า'))

def decay_time(rng, mc):
    T, n, m0 = R(rng, 2, 6), R(rng, 2, 5), rng.choice([16, 32, 64, 80, 96, 160])
    m = Fr(m0, 2**n)
    return NUM(f'สารกัมมันตรังสี {m0} g มีครึ่งชีวิต {T} ชั่วโมง ต้องใช้เวลากี่ชั่วโมงจึงเหลือ {num(m)} g', T * n,
               ol(f'{m0} → ' + ' → '.join(num(Fr(m0, 2**i)) for i in range(1, n + 1)) + f' g = {n} ช่วงครึ่งชีวิต', f'เวลา = {n} × {T} = {T*n} ชั่วโมง'), u='ชั่วโมง')

def ev(rng, mc):
    lam = rng.choice([620, 496, 310, 248, 1240, 400, 500, 155])
    return NUM(f'โฟตอนความยาวคลื่น {lam} nm มีพลังงานกี่อิเล็กตรอนโวลต์ (ใช้ E(eV) = {fr(1240,"λ(nm)")})', Fr(1240, lam), ol(f'E = {fr(1240, lam)} = {num(Fr(1240,lam))} eV'), u='eV')

def photoelec(rng, mc):
    E, W = rng.choice([4, 5, Fr(9, 2), 6, Fr(7, 2), 3]), rng.choice([Fr(23, 10), 2, Fr(5, 2), Fr(21, 10), Fr(14, 5)])
    if E <= W: return photoelec(rng, mc)
    return NUM(f'แสงที่มีพลังงานโฟตอน {num(E)} eV ตกกระทบโลหะที่มีฟังก์ชันงาน {num(W)} eV โฟโตอิเล็กตรอนมีพลังงานจลน์สูงสุดกี่ eV', E - W, ol(f'E<sub>k,max</sub> = hf − W = {num(E)} − {num(W)} = {num(E-W)} eV'), u='eV')

def bohr(rng, mc):
    a, b = rng.choice([(2, 1), (4, 2), (4, 1), (3, 1)])
    E = Fr(136, 10) * (Fr(1, b * b) - Fr(1, a * a))
    if Fr(E * 10000).denominator != 1: return bohr(rng, mc)
    return NUM(f'อะตอมไฮโดรเจนมีพลังงาน E<sub>n</sub> = −{fr("13.6","n²")} eV อิเล็กตรอนเปลี่ยนระดับจาก n = {a} ไป n = {b} ปล่อยโฟตอนพลังงานกี่ eV', E,
               ol(f'E<sub>{a}</sub> = −{num(Fr(136,10)/(a*a))} eV, E<sub>{b}</sub> = −{num(Fr(136,10)/(b*b))} eV', f'ΔE = {num(E)} eV'), u='eV')

def nucleus(rng, mc):
    A, Z = rng.choice([(238, 92), (232, 90), (226, 88), (234, 90), (222, 86)])
    na, nb = R(rng, 1, 4), R(rng, 0, 3)
    A2, Z2 = A - 4 * na, Z - 2 * na + nb
    corr = f'A = {A2}, Z = {Z2}'
    wr = [f'A = {A2}, Z = {Z - 2*na - nb}', f'A = {A - 2*na}, Z = {Z2}', f'A = {A2 - nb}, Z = {Z2}', f'A = {A2}, Z = {Z2 + 1}', f'A = {A - 4*na - 4*nb}, Z = {Z - 2*na - 2*nb}']
    return mc(f'นิวเคลียส (A = {A}, Z = {Z}) สลายให้อนุภาคแอลฟา {na} ตัว และบีตาลบ {nb} ตัว นิวเคลียสที่ได้มีเลขมวล A และเลขอะตอม Z เท่าใด', corr, wr,
              ol('แอลฟา: A ลด 4, Z ลด 2 · บีตาลบ: A เท่าเดิม, Z เพิ่ม 1', f'A = {A} − {4*na} = {A2}', f'Z = {Z} − {2*na} + {nb} = {Z2}'))

# ---------- ap-wave ----------
def vfl(rng, mc):
    f, lam = rng.choice([50, 100, 200, 256, 340, 500, 680]), rng.choice([Fr(1, 2), 1, 2, Fr(1, 4), Fr(17, 10)])
    v = f * lam
    k = rng.randrange(2)
    if k: return NUM(f'คลื่นความถี่ {f} Hz ความยาวคลื่น {num(lam)} m มีอัตราเร็วกี่ m/s', v, ol(f'v = fλ = {f} × {num(lam)} = {num(v)} m/s'), u='m/s')
    return NUM(f'คลื่นเสียงอัตราเร็ว {num(v)} m/s ความถี่ {f} Hz มีความยาวคลื่นกี่เมตร', lam, ol(f'λ = v/f = {num(v)} ÷ {f} = {num(lam)} m'), u='m')

def echo(rng, mc):
    v, t = rng.choice([340, 330, 1500]), rng.choice([Fr(1, 2), 1, 2, 3, 4, Fr(3, 2)])
    medium = 'ในน้ำ' if v == 1500 else 'ในอากาศ'
    return NUM(f'ส่งคลื่นเสียง{medium} (อัตราเร็ว {v} m/s) ไปกระทบสิ่งกีดขวาง ได้ยินเสียงสะท้อนกลับมาหลังส่ง {num(t)} s สิ่งกีดขวางอยู่ห่างกี่เมตร', v * t / 2,
               ol(f'ระยะไป-กลับ = {v} × {num(t)} = {num(v*t)} m', f'ระยะทางเดียว = {num(v*t/2)} m'), u='m', h='เสียงเดินทางไปและกลับ')

def refr(rng, mc):
    v = rng.choice([(2, 3, Fr(3, 2)), (Fr(9, 4), 3, Fr(4, 3)), (Fr(5, 4), 3, Fr(12, 5)), (2, 3, Fr(3, 2))])
    vv, c, n = v
    return MCN(mc, f'แสงเคลื่อนที่ในตัวกลางด้วยอัตราเร็ว {num(vv)} × 10⁸ m/s ดรรชนีหักเหของตัวกลางเท่ากับเท่าใด (c = {c} × 10⁸ m/s)', n, ol(f'n = {fr("c","v")} = {fr(c, num(vv))} = {fr(n)}'), extra=[1 / n, n + Fr(1, 2)])

def db(rng, mc):
    k = R(rng, 1, 4)
    return NUM(f'ถ้าความเข้มเสียงเพิ่มขึ้น {10**k:,} เท่า ระดับความเข้มเสียงเพิ่มขึ้นกี่เดซิเบล', 10 * k, ol(f'Δβ = 10 log({10**k:,}) = 10 × {k} = {10*k} dB'), u='dB')

def lens(rng, mc):
    u, f = rng.choice([(30, 10), (20, 10), (60, 20), (12, 4), (15, 10), (40, 8), (36, 12), (24, 8), (30, 20), (45, 9)])
    v = Fr(u * f, u - f)
    return NUM(f'วางวัตถุหน้าเลนส์นูนความยาวโฟกัส {f} cm ห่างจากเลนส์ {u} cm ภาพจริงเกิดห่างจากเลนส์กี่เซนติเมตร', v,
               ol(f'{fr(1,"f")} = {fr(1,"u")} + {fr(1,"v")}', f'{fr(1,"v")} = {fr(1,f)} − {fr(1,u)} = {fr(1/v)}', f'v = {num(v)} cm'), u='cm')

def string_f(rng, mc):
    v, L = rng.choice([100, 120, 200, 240, 300, 400]), rng.choice([Fr(1, 2), 1, 2, Fr(3, 2), Fr(4, 5)])
    n = R(rng, 1, 3)
    f = n * v / (2 * L)
    lab = {1: 'ความถี่มูลฐาน', 2: 'ฮาร์มอนิกที่ 2', 3: 'ฮาร์มอนิกที่ 3'}[n]
    return NUM(f'เส้นเชือกยาว {num(L)} m ตรึงปลายทั้งสองข้าง คลื่นในเชือกมีอัตราเร็ว {v} m/s {lab}มีค่ากี่เฮิรตซ์', f,
               ol(f'f<sub>n</sub> = {fr("nv","2L")}', f'= {fr(f"{n} × {v}", f"2 × {num(L)}")} = {num(f)} Hz'), u='Hz')

def beats(rng, mc):
    f1 = R(rng, 250, 520); d = R(rng, 1, 8)
    return NUM(f'ส้อมเสียงความถี่ {f1} Hz และ {f1+d} Hz เคาะพร้อมกัน จะได้ยินเสียงบีตส์กี่ครั้งต่อวินาที', d, ol(f'f<sub>บีตส์</sub> = |f₁ − f₂| = {d} Hz'), u='ครั้ง/วินาที')

# ---------- ap-fluid ----------
def rho_gh(rng, mc):
    rho, h = rng.choice([(1000, 'น้ำ'), (800, 'น้ำมัน'), (13600, 'ปรอท')]), rng.choice([Fr(1, 10), Fr(1, 2), 2, 5, 10])
    p = rho[0] * 10 * h
    return NUM(f'ความดันเนื่องจาก{rho[1]} (ρ = {rho[0]:,} kg/m³) ที่ความลึก {num(h)} m มีค่ากี่ปาสคาล ({G})', p, ol(f'P = ρgh = {rho[0]:,} × 10 × {num(h)} = {num(p)} Pa'), u='Pa')

def buoy(rng, mc):
    V = rng.choice([Fr(1, 1000), Fr(2, 1000), Fr(5, 1000), Fr(1, 100), Fr(1, 10), Fr(1, 2)])
    F = 1000 * V * 10
    return NUM(f'วัตถุปริมาตร {num(V)} m³ จมมิดในน้ำ (ρ = 1000 kg/m³) ได้รับแรงลอยตัวกี่นิวตัน ({G})', F, ol(f'F<sub>B</sub> = ρVg = 1000 × {num(V)} × 10 = {num(F)} N'), u='N')

def hydraulic(rng, mc):
    a1, a2, F1 = rng.choice([(1, 50), (2, 100), (5, 200), (1, 20), (4, 100)]) + (R(rng, 10, 100),)
    return NUM(f'เครื่องอัดไฮดรอลิกมีพื้นที่ลูกสูบเล็ก {a1} cm² และลูกสูบใหญ่ {a2} cm² ออกแรงกดลูกสูบเล็ก {F1} N ลูกสูบใหญ่ยกน้ำหนักได้กี่นิวตัน', Fr(F1 * a2, a1),
               ol(f'{fr("F₁","A₁")} = {fr("F₂","A₂")}', f'F₂ = {F1} × {fr(a2, a1)} = {num(Fr(F1*a2, a1))} N'), u='N')

def heat(rng, mc):
    m, dT = rng.choice([Fr(1, 2), 1, 2, Fr(1, 5), Fr(3, 2)]), R(rng, 5, 60)
    Q = 4200 * m * dT
    return NUM(f'ต้องใช้ความร้อนกี่จูลทำให้น้ำมวล {num(m)} kg อุณหภูมิเพิ่มขึ้น {dT} °C (c<sub>น้ำ</sub> = 4200 J/kg·K)', Q, ol(f'Q = mcΔT = {num(m)} × 4200 × {dT} = {num(Q)} J'), u='J')

def boyle(rng, mc):
    P1, V1, k = rng.choice([1, 2, 3]), rng.choice([2, 4, 6, 12]), rng.choice([2, 3, 4, Fr(1, 2)])
    P2 = P1 * k; V2 = Fr(P1 * V1) / P2
    return NUM(f'แก๊สอุดมคติปริมาตร {V1} L ความดัน {P1} atm อัดที่อุณหภูมิคงตัวจนความดันเป็น {num(P2)} atm ปริมาตรใหม่กี่ลิตร', V2, ol(f'P₁V₁ = P₂V₂ → V₂ = {fr(f"{P1} × {V1}", num(P2))} = {num(V2)} L'), u='L')

def charles(rng, mc):
    T1, T2, V1 = rng.choice([(300, 400), (300, 450), (200, 300), (400, 600), (250, 500), (300, 600)]) + (R(rng, 2, 12),)
    V2 = Fr(V1 * T2, T1)
    return NUM(f'แก๊สอุดมคติปริมาตร {V1} L ที่ {T1} K ถูกทำให้ร้อนที่ความดันคงตัวจนมีอุณหภูมิ {T2} K ปริมาตรใหม่กี่ลิตร', V2, ol(f'{fr("V₁","T₁")} = {fr("V₂","T₂")} → V₂ = {V1} × {fr(T2, T1)} = {num(V2)} L'), u='L')

def continuity(rng, mc):
    A1, A2, v1 = rng.choice([(4, 1), (6, 2), (10, 2), (9, 3), (8, 2), (5, 1)]) + (R(rng, 1, 5),)
    return NUM(f'ของเหลวไหลในท่อจากส่วนที่มีพื้นที่หน้าตัด {A1} cm² ด้วยอัตราเร็ว {v1} m/s ไปยังส่วนที่มีพื้นที่หน้าตัด {A2} cm² จะมีอัตราเร็วกี่ m/s', Fr(A1 * v1, A2),
               ol(f'A₁v₁ = A₂v₂ → v₂ = {A1} × {v1} ÷ {A2} = {num(Fr(A1*v1, A2))} m/s'), u='m/s')

TOPICS = {
    'ap-mech':   [projectile, centri, g_height, friction, incline, fall_speed, stick, impulse, max_h],
    'ap-shm':    [spring_T, pend_scale, freq, spring_E, vmax, planet_pend],
    'ap-em':     [cap, ilb, trafo, coulomb, power_r, efield, circuit],
    'ap-modern': [halflife, photon_ratio, decay_time, ev, photoelec, bohr, nucleus],
    'ap-wave':   [vfl, echo, refr, db, lens, string_f, beats],
    'ap-fluid':  [rho_gh, buoy, hydraulic, heat, boyle, charles, continuity],
}
NEW = {'ap-wave': ('alevel-phys', 'phys', 'คลื่น เสียง แสง'), 'ap-fluid': ('alevel-phys', 'phys', 'ของไหล ความร้อน แก๊ส')}
NOPT = 5
