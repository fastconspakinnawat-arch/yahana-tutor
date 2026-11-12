"""เตรียมสอบเข้า ม.1"""
from core import *
import math

R = lambda rng, a, b: rng.randint(a, b)

# ---------- e1-num จำนวนและการคิดคำนวณ ----------
def odd_sum(rng, mc):
    n = R(rng, 8, 40); last = 2 * n - 1
    return NUM(f'1 + 3 + 5 + … + {last} มีค่าเท่าใด', n * n,
               ol(f'มีจำนวนคี่ตั้งแต่ 1 ถึง {last} อยู่ ({last} + 1) ÷ 2 = {n} ตัว', f'ผลบวกจำนวนคี่ n ตัวแรก = n² = {n}² = {n*n}'),
               h='ผลบวกจำนวนคี่ n ตัวแรก = n²')

def unit_digit(rng, mc):
    a = rng.choice([2, 3, 4, 7, 8, 9, 12, 13, 17]); k = R(rng, 11, 99)
    b = a % 10
    cyc = []; x = b
    while x not in cyc:
        cyc.append(x); x = x * b % 10
    L = len(cyc); r = (k - 1) % L
    return NUM(f'หลักหน่วยของ {a}<sup>{k}</sup> คือเลขใด', pow(a, k, 10),
               ol(f'หลักหน่วยของกำลังของ {a} วนเป็นรอบ: {", ".join(map(str, cyc))} (รอบละ {L} ตัว)',
                  f'{k} ÷ {L} เหลือเศษ {k % L}' + (' → ตรงกับตัวสุดท้ายของรอบ' if k % L == 0 else f' → ตรงกับตัวที่ {k % L} ของรอบ'),
                  f'หลักหน่วย = {pow(a, k, 10)}'),
               h='ดูหลักหน่วยของกำลัง 1, 2, 3, … แล้วหาแบบรูปที่วนซ้ำ')

def gcd_lcm_other(rng, mc):
    g = R(rng, 2, 9)
    while True:
        p, q = R(rng, 2, 9), R(rng, 2, 9)
        if p != q and math.gcd(p, q) == 1: break
    x, y, L = g * p, g * q, g * p * q
    return NUM(f'จำนวนนับสองจำนวนมี ห.ร.ม. เท่ากับ {g} และ ค.ร.น. เท่ากับ {L} ถ้าจำนวนหนึ่งคือ {x} อีกจำนวนหนึ่งคือเท่าใด', y,
               ol('ห.ร.ม. × ค.ร.น. = ผลคูณของสองจำนวน', f'{x} × ข = {g} × {L} = {g*L}', f'ข = {g*L} ÷ {x} = {y}'),
               h='ห.ร.ม. × ค.ร.น. = ผลคูณของสองจำนวน')

def gcd3(rng, mc):
    g = rng.choice([4, 6, 8, 9, 12, 14, 15, 18])
    ms = rng.sample([2, 3, 5, 7, 11], 3)
    nums = [g * m for m in ms]
    return NUM(f'ห.ร.ม. ของ {nums[0]}, {nums[1]} และ {nums[2]} คือเท่าใด', g,
               ol(*[f'{n} = {g} × {m}' for n, m in zip(nums, ms)], f'{", ".join(map(str, ms))} ไม่มีตัวประกอบร่วมกัน', f'ห.ร.ม. = {g}'))

def lcm3(rng, mc):
    nums = sorted(rng.sample([4, 6, 8, 9, 10, 12, 14, 15, 18, 20], 3))
    L = math.lcm(*nums)
    return NUM(f'ค.ร.น. ของ {nums[0]}, {nums[1]} และ {nums[2]} คือเท่าใด', L,
               ol(*[f'{n} = {fac(n)}' for n in nums], 'เลือกตัวประกอบเฉพาะแต่ละตัวที่กำลังสูงสุดมาคูณกัน', f'ค.ร.น. = {fac(L)} = {L}'))

def fac(n):
    out, p = [], 2
    while n > 1:
        c = 0
        while n % p == 0: n //= p; c += 1
        if c: out.append(f'{p}' + (f'<sup>{c}</sup>' if c > 1 else ''))
        p += 1
    return ' × '.join(out)

def divisors(rng, mc):
    a, b, c = R(rng, 1, 4), R(rng, 0, 3), R(rng, 0, 2)
    N = 2**a * 3**b * 5**c
    if N < 12: N, a, b, c = 72, 3, 2, 0
    ans = (a + 1) * (b + 1) * (c + 1)
    return NUM(f'{N} มีตัวประกอบที่เป็นจำนวนนับทั้งหมดกี่ตัว', ans,
               ol(f'{N} = {fac(N)}', 'จำนวนตัวประกอบ = ผลคูณของ (เลขชี้กำลัง + 1)', f'= ' + ' × '.join(str(e + 1) for e in (a, b, c) if e) + f' = {ans}'),
               u='ตัว', h='แยกตัวประกอบเฉพาะก่อน')

def gauss(rng, mc):
    n = rng.choice([20, 30, 40, 50, 60, 80, 99, 200])
    return NUM(f'1 + 2 + 3 + … + {n} มีค่าเท่าใด', n * (n + 1) // 2,
               ol(f'จับคู่หัว-ท้าย: 1 + {n} = {n+1} มีทั้งหมด {fr(n,2)} คู่', f'ผลบวก = {fr(f"{n} × {n+1}", 2)} = {num(n*(n+1)//2)}'))

def order_ops(rng, mc):
    b, c = R(rng, 3, 12), R(rng, 3, 12); e = R(rng, 2, 9); d = e * R(rng, 2, 12); a = R(rng, 5, 60)
    v = a + b * c - d // e
    return NUM(f'{a} + {b} × {c} − {d} ÷ {e} มีค่าเท่าใด', v,
               ol('ทำคูณ-หารก่อน บวก-ลบทีหลัง', f'{b} × {c} = {b*c} และ {d} ÷ {e} = {d//e}', f'{a} + {b*c} − {d//e} = {v}'))

def multiples_count(rng, mc):
    k = R(rng, 3, 13); lo = R(rng, 10, 60); hi = lo + R(rng, 60, 300)
    cnt = hi // k - (lo - 1) // k
    return NUM(f'จำนวนนับตั้งแต่ {lo} ถึง {hi} ที่หารด้วย {k} ลงตัว มีกี่จำนวน', cnt,
               ol(f'ตั้งแต่ 1 ถึง {hi} มี {hi // k} จำนวน', f'ตั้งแต่ 1 ถึง {lo-1} มี {(lo-1)//k} จำนวน', f'{hi//k} − {(lo-1)//k} = {cnt}'), u='จำนวน')

# ---------- e1-word โจทย์ปัญหา ----------
def ages(rng, mc):
    c = R(rng, 5, 15); d = R(rng, 20, 35); S = 2 * c + d
    return NUM(f'แม่อายุมากกว่าลูก {d} ปี อายุรวมกันเป็น {S} ปี ลูกอายุกี่ปี', c,
               ol(f'ให้ลูกอายุ x ปี แม่อายุ x + {d} ปี', f'x + x + {d} = {S} → 2x = {S-d}', f'x = {c}'), u='ปี')

def ages2(rng, mc):
    c = R(rng, 4, 12); m = R(rng, 3, 4); y = R(rng, 3, 15)
    f = m * c
    # อีก y ปี พ่ออายุเป็น k เท่า ต้องเป็นจำนวนเต็ม
    if (f + y) % (c + y): return ages(rng, mc)
    k = (f + y) // (c + y)
    if k < 2 or k >= m: return ages(rng, mc)
    return NUM(f'ปัจจุบันพ่ออายุเป็น {m} เท่าของลูก อีก {y} ปีพ่อจะมีอายุเป็น {k} เท่าของลูก ปัจจุบันลูกอายุกี่ปี', c,
               ol(f'ให้ลูกอายุ x ปี พ่ออายุ {m}x ปี', f'{m}x + {y} = {k}(x + {y})', f'{m}x − {k}x = {k*y} − {y} → {m-k}x = {k*y-y}', f'x = {c}'), u='ปี')

def work(rng, mc):
    a, b = rng.choice([(6, 3), (12, 6), (10, 15), (20, 30), (4, 12), (6, 12), (12, 24), (15, 30), (9, 18), (8, 24), (12, 4), (18, 9)])
    t = Fr(a * b, a + b)
    return NUM(f'ก ทำงานชิ้นหนึ่งคนเดียวเสร็จใน {a} วัน ข ทำคนเดียวเสร็จใน {b} วัน ถ้าช่วยกันทำจะเสร็จในกี่วัน', t,
               ol(f'1 วัน ก ทำได้ {fr(1,a)} ของงาน ข ทำได้ {fr(1,b)} ของงาน', f'รวมกัน 1 วัน = {fr(Fr(1,a)+Fr(1,b))} ของงาน', f'ใช้เวลา = {num(t)} วัน'),
               u='วัน', h='หางานที่แต่ละคนทำได้ใน 1 วัน')

def profit(rng, mc):
    cost = rng.choice([200, 250, 400, 500, 800, 1200, 1500, 2000]); p = rng.choice([10, 15, 20, 25, 30, 40, 50])
    sell = cost * (100 + p) // 100
    return NUM(f'ซื้อสินค้ามา {num(cost)} บาท ขายไป {num(sell)} บาท ได้กำไรร้อยละเท่าใด', p,
               ol(f'กำไร = {num(sell)} − {num(cost)} = {num(sell-cost)} บาท', f'ร้อยละของกำไร = {fr(sell-cost, cost)} × 100 = {p}'),
               h='ร้อยละของกำไรคิดจากราคาทุน')

def meet(rng, mc):
    v1, v2 = R(rng, 40, 70), R(rng, 50, 90); t = rng.choice([2, 3, 4, Fr(3, 2), Fr(5, 2)])
    D = (v1 + v2) * t
    if Fr(D).denominator != 1: return meet(rng, mc)
    return NUM(f'เมือง ก และ ข ห่างกัน {num(D)} กม. รถคันหนึ่งออกจาก ก ด้วยอัตราเร็ว {v1} กม./ชม. อีกคันออกจาก ข สวนทางมาด้วยอัตราเร็ว {v2} กม./ชม. พร้อมกัน จะพบกันหลังออกเดินทางกี่ชั่วโมง', t,
               ol(f'วิ่งเข้าหากัน ระยะลดลงชั่วโมงละ {v1} + {v2} = {v1+v2} กม.', f'เวลา = {num(D)} ÷ {v1+v2} = {num(t)} ชั่วโมง'), u='ชั่วโมง')

def chick_rabbit(rng, mc):
    r, c = R(rng, 3, 20), R(rng, 3, 25); H, L = r + c, 4 * r + 2 * c
    return NUM(f'ในฟาร์มมีไก่และกระต่ายรวม {H} ตัว นับขาได้ {L} ขา มีกระต่ายกี่ตัว', r,
               ol(f'สมมติทุกตัวเป็นไก่ จะมีขา {H} × 2 = {2*H} ขา', f'ขาเกินมา {L} − {2*H} = {L-2*H} ขา', f'กระต่ายแต่ละตัวมีขามากกว่าไก่ 2 ขา → กระต่าย = {L-2*H} ÷ 2 = {r} ตัว'),
               u='ตัว', h='ลองสมมติว่าทุกตัวเป็นไก่')

def double_disc(rng, mc):
    P = rng.choice([1000, 2000, 2500, 4000, 5000]); a, b = rng.choice([(10, 10), (20, 10), (20, 20), (10, 5), (25, 20), (30, 10)])
    p1 = P * (100 - a) // 100; p2 = Fr(p1 * (100 - b), 100)
    return NUM(f'สินค้าราคา {num(P)} บาท ลดราคา {a}% แล้วลดซ้ำอีก {b}% จากราคาที่ลดแล้ว ต้องจ่ายกี่บาท', p2,
               ol(f'ลดครั้งแรก: {num(P)} × {fr(100-a,100)} = {num(p1)}', f'ลดครั้งที่สอง: {num(p1)} × {fr(100-b,100)} = {num(p2)} บาท',
                  f'สังเกต: ไม่เท่ากับลด {a+b}% ทีเดียว'), u='บาท')

def share(rng, mc):
    r = sorted(rng.sample(range(1, 8), 3)); unit = R(rng, 50, 400); T = sum(r) * unit
    return NUM(f'แบ่งเงิน {num(T)} บาท ให้ ก : ข : ค ในอัตราส่วน {r[0]} : {r[1]} : {r[2]} ค ได้เงินกี่บาท', r[2] * unit,
               ol(f'รวมส่วน = {r[0]} + {r[1]} + {r[2]} = {sum(r)} ส่วน', f'1 ส่วน = {num(T)} ÷ {sum(r)} = {unit} บาท', f'ค ได้ {r[2]} × {unit} = {num(r[2]*unit)} บาท'), u='บาท')

# ---------- e1-geo เรขาคณิต ----------
def third_angle(rng, mc):
    a, b = R(rng, 25, 85), R(rng, 25, 85)
    return NUM(f'สามเหลี่ยมมีมุมสองมุมขนาด {a}° และ {b}° มุมที่เหลือมีขนาดกี่องศา', 180 - a - b,
               ol('มุมภายในสามเหลี่ยมรวมกันได้ 180°', f'180 − {a} − {b} = {180-a-b}°'), u='องศา')

def poly_sum(rng, mc):
    n = R(rng, 5, 15)
    return NUM(f'ผลบวกของมุมภายในรูป {n} เหลี่ยม เท่ากับกี่องศา', (n - 2) * 180,
               ol('ผลบวกมุมภายใน = (n − 2) × 180°', f'= ({n} − 2) × 180 = {num((n-2)*180)}°'), u='องศา')

def poly_reg(rng, mc):
    n = rng.choice([5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36])
    return NUM(f'รูป {n} เหลี่ยมด้านเท่ามุมเท่า มีมุมภายในแต่ละมุมกี่องศา', Fr((n - 2) * 180, n),
               ol(f'ผลบวกมุมภายใน = ({n} − 2) × 180 = {(n-2)*180}°', f'แต่ละมุม = {(n-2)*180} ÷ {n} = {num(Fr((n-2)*180, n))}°'), u='องศา')

def circle_area(rng, mc):
    r = 7 * R(rng, 1, 6)
    return NUM(f'วงกลมรัศมี {r} ซม. มีพื้นที่กี่ตารางเซนติเมตร (ใช้ π ≈ {fr(22,7)})', Fr(22, 7) * r * r,
               ol(f'พื้นที่ = πr² = {fr(22,7)} × {r} × {r}', f'= {num(Fr(22,7)*r*r)} ตร.ซม.'), u='ตร.ซม.')

def circ(rng, mc):
    r = 7 * R(rng, 1, 8)
    return NUM(f'วงกลมรัศมี {r} ซม. มีความยาวรอบวงกี่เซนติเมตร (ใช้ π ≈ {fr(22,7)})', Fr(44, 7) * r,
               ol(f'ความยาวรอบวง = 2πr = 2 × {fr(22,7)} × {r}', f'= {num(Fr(44,7)*r)} ซม.'), u='ซม.')

def rect_perim(rng, mc):
    w, l = R(rng, 3, 15), R(rng, 8, 30)
    return NUM(f'สี่เหลี่ยมผืนผ้ามีพื้นที่ {w*l} ตร.ซม. กว้าง {w} ซม. มีความยาวรอบรูปกี่เซนติเมตร', 2 * (w + l),
               ol(f'ยาว = {w*l} ÷ {w} = {l} ซม.', f'ความยาวรอบรูป = 2 × ({w} + {l}) = {2*(w+l)} ซม.'), u='ซม.')

def cube_sa(rng, mc):
    a = R(rng, 2, 12)
    return NUM(f'ลูกบาศก์มีปริมาตร {a**3} ลูกบาศก์เซนติเมตร มีพื้นที่ผิวทั้งหมดกี่ตารางเซนติเมตร', 6 * a * a,
               ol(f'ความยาวด้าน = ∛{a**3} = {a} ซม.', f'พื้นที่ผิว = 6 × {a}² = {6*a*a} ตร.ซม.'), u='ตร.ซม.')

def clock(rng, mc):
    h = R(rng, 1, 11); m = rng.choice([0, 30, 0, 30, 20, 40])
    ang = abs(30 * h - Fr(11, 2) * m)
    if ang > 180: ang = 360 - ang
    return NUM(f'เวลา {h}:{m:02d} น. เข็มชั่วโมงและเข็มนาทีทำมุมกันกี่องศา (มุมที่ไม่เกิน 180°)', ang,
               ol(f'เข็มนาทีอยู่ที่ {m} × 6 = {6*m}°', f'เข็มชั่วโมงอยู่ที่ {h} × 30 + {m} × 0.5 = {num(30*h+Fr(m,2))}°', f'มุมระหว่างเข็ม = {num(ang)}°'),
               u='องศา', h='เข็มชั่วโมงเดินชั่วโมงละ 30° หรือนาทีละ 0.5°')

def triangle_ext(rng, mc):
    a, b = R(rng, 30, 80), R(rng, 30, 80)
    return NUM(f'สามเหลี่ยม ABC มีมุม A = {a}° และมุม B = {b}° ต่อด้าน BC ออกไปทาง C มุมภายนอกที่จุด C มีขนาดกี่องศา', a + b,
               ol('มุมภายนอก = ผลบวกมุมภายในที่ไม่ใช่มุมประชิด', f'= {a} + {b} = {a+b}°'), u='องศา')

# ---------- e1-pattern แบบรูป ----------
def sq_plus(rng, mc):
    k = R(rng, -3, 5); s = R(rng, 1, 4)
    seq = [n * n + k for n in range(s, s + 5)]; nxt = (s + 5) ** 2 + k
    return NUM(f'{", ".join(num(x) for x in seq)}, … จำนวนถัดไปคือเท่าใด', nxt,
               ol(f'ผลต่างระหว่างพจน์: {", ".join(str(seq[i+1]-seq[i]) for i in range(4))} เพิ่มขึ้นทีละ 2', f'ผลต่างถัดไป = {seq[4]-seq[3]+2}', f'{seq[4]} + {seq[4]-seq[3]+2} = {nxt}'),
               h='ดูผลต่างระหว่างพจน์ที่อยู่ติดกัน')

def arith_next(rng, mc):
    a, d = R(rng, -10, 20), rng.choice([3, 4, 5, 6, 7, 9, 11, -3, -4])
    n = R(rng, 15, 60)
    return NUM(f'ลำดับ {num(a)}, {num(a+d)}, {num(a+2*d)}, {num(a+3*d)}, … พจน์ที่ {n} คือเท่าใด', a + (n - 1) * d,
               ol(f'เพิ่มขึ้นทีละ {num(d)}', f'พจน์ที่ n = {num(a)} + (n − 1)({num(d)})', f'พจน์ที่ {n} = {num(a)} + {n-1} × ({num(d)}) = {num(a+(n-1)*d)}'))

def geo_next(rng, mc):
    a, r = R(rng, 1, 5), rng.choice([2, 3, -2])
    seq = [a * r**i for i in range(5)]
    return NUM(f'{", ".join(num(x) for x in seq)}, … จำนวนถัดไปคือเท่าใด', a * r**5,
               ol(f'แต่ละพจน์คูณด้วย {num(r)}', f'{num(seq[-1])} × {num(r)} = {num(a*r**5)}'))

def fib_like(rng, mc):
    a, b = R(rng, 1, 6), R(rng, 1, 9); s = [a, b]
    for _ in range(4): s.append(s[-1] + s[-2])
    return NUM(f'{", ".join(map(str, s))}, … จำนวนถัดไปคือเท่าใด', s[-1] + s[-2],
               ol('แต่ละพจน์ = ผลบวกของสองพจน์ก่อนหน้า', f'{s[-2]} + {s[-1]} = {s[-1]+s[-2]}'))

def tri_num(rng, mc):
    n = R(rng, 8, 30)
    return NUM(f'จัดเหรียญเป็นรูปสามเหลี่ยม แถวที่ 1 มี 1 เหรียญ แถวที่ 2 มี 2 เหรียญ … ถ้ามี {n} แถว ใช้เหรียญทั้งหมดกี่เหรียญ', n * (n + 1) // 2,
               ol(f'จำนวนเหรียญ = 1 + 2 + … + {n}', f'= {fr(f"{n} × {n+1}", 2)} = {n*(n+1)//2} เหรียญ'), u='เหรียญ')

def matchsticks(rng, mc):
    n = R(rng, 10, 50)
    return NUM(f'ต่อไม้ขีดเป็นรูปสี่เหลี่ยมจัตุรัสเรียงเป็นแถวยาวติดกัน รูปที่ 1 ใช้ 4 ก้าน รูปที่ 2 (สองช่อง) ใช้ 7 ก้าน รูปที่ 3 ใช้ 10 ก้าน รูปที่ {n} ใช้ไม้ขีดกี่ก้าน', 3 * n + 1,
               ol('เพิ่มช่องละ 3 ก้าน', 'จำนวนก้าน = 3n + 1', f'n = {n}: 3({n}) + 1 = {3*n+1} ก้าน'), u='ก้าน')

# ---------- e1-frac เศษส่วน ทศนิยม ร้อยละ ----------
def frac_add(rng, mc):
    b, d = rng.sample([2, 3, 4, 5, 6, 8, 9, 10, 12], 2); a, c = R(rng, 1, b - 1), R(rng, 1, d - 1)
    v = Fr(a, b) + Fr(c, d)
    wr = [fr(Fr(a + c, b + d)), fr(v + Fr(1, math.lcm(b, d))), fr(v - Fr(1, math.lcm(b, d))), fr(Fr(a * c, b * d)), fr(v * 2)]
    return mc(f'{fr(a,b)} + {fr(c,d)} มีค่าเท่าใด', fr(v), wr,
              ol(f'ค.ร.น. ของ {b} และ {d} คือ {math.lcm(b,d)}', f'{fr(a,b)} + {fr(c,d)} = {fr(a*math.lcm(b,d)//b, math.lcm(b,d))} + {fr(c*math.lcm(b,d)//d, math.lcm(b,d))} = {fr(v)}'),
              h='ทำตัวส่วนให้เท่ากัน ห้ามบวกตัวส่วน')

def frac_of(rng, mc):
    q = rng.choice([3, 4, 5, 6, 8]); p = R(rng, 1, q - 1); N = q * R(rng, 3, 30)
    return NUM(f'{fr(p,q)} ของ {N} เท่ากับเท่าใด', Fr(p * N, q), ol(f'{fr(p,q)} × {N} = {fr(p*N, q)} = {num(Fr(p*N,q))}'))

def pct_of(rng, mc):
    p = rng.choice([5, 12, 15, 25, 35, 40, 45, 60, 75, 120, 150]); N = rng.choice([40, 60, 80, 120, 200, 240, 360, 480, 800])
    return NUM(f'{p}% ของ {N} เท่ากับเท่าใด', Fr(p * N, 100), ol(f'{fr(p,100)} × {N} = {num(Fr(p*N,100))}'))

def dec_mul(rng, mc):
    a = rng.choice([0.25, 0.5, 0.75, 1.5, 2.5, 0.2, 0.4, 1.25]); b = rng.choice([12, 16, 24, 36, 48, 64, 80])
    fa = Fr(str(a))
    return NUM(f'{a} × {b} มีค่าเท่าใด', fa * b, ol(f'{a} = {fr(fa)}', f'{fr(fa)} × {b} = {num(fa*b)}'))

def pct_change(rng, mc):
    A = rng.choice([40, 50, 80, 120, 200, 250, 400, 500]); p = rng.choice([10, 20, 25, 30, 50, 75, -10, -20, -25, -40])
    if A * (100 + p) % 100: return pct_change(rng, mc)
    B = A * (100 + p) // 100
    word = 'เพิ่มขึ้น' if p > 0 else 'ลดลง'
    return NUM(f'ราคาสินค้าเปลี่ยนจาก {A} บาท เป็น {B} บาท ราคา{word}ร้อยละเท่าใด', abs(p),
               ol(f'ผลต่าง = {abs(B-A)} บาท', f'คิดเทียบราคาเดิม: {fr(abs(B-A), A)} × 100 = {abs(p)}'), h='ร้อยละการเปลี่ยนแปลงคิดจากค่าเดิม')

def frac_div(rng, mc):
    a, b, c, d = R(rng, 1, 7), R(rng, 2, 9), R(rng, 1, 7), R(rng, 2, 9)
    if Fr(a, b).denominator == 1 or Fr(c, d).denominator == 1: return frac_div(rng, mc)
    v = Fr(a, b) / Fr(c, d)
    wr = [fr(Fr(a, b) * Fr(c, d)), fr(1 / v), fr(v + 1), fr(v * 2), fr(Fr(a * d + 1, b * c))]
    return mc(f'{fr(a,b)} ÷ {fr(c,d)} มีค่าเท่าใด', fr(v), wr,
              ol('หารด้วยเศษส่วน = คูณด้วยส่วนกลับ', f'{fr(a,b)} × {fr(d,c)} = {fr(v)}'))

TOPICS = {
    'e1-num':     [odd_sum, unit_digit, gcd_lcm_other, gcd3, lcm3, divisors, gauss, order_ops, multiples_count],
    'e1-word':    [ages, ages2, work, profit, meet, chick_rabbit, double_disc, share],
    'e1-geo':     [third_angle, poly_sum, poly_reg, circle_area, circ, rect_perim, cube_sa, clock, triangle_ext],
    'e1-pattern': [sq_plus, arith_next, geo_next, fib_like, tri_num, matchsticks],
    'e1-frac':    [frac_add, frac_of, pct_of, dec_mul, pct_change, frac_div],
}
NEW = {'e1-frac': ('exam-m1', 'math', 'เศษส่วน ทศนิยม ร้อยละ')}
NOPT = 4
