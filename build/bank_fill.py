"""เติมวิชาที่ขาดในแต่ละระดับชั้น + ชุดแนวสอบ RT ป.1, NT ป.3, O-NET ป.6 / ม.3 / ม.6"""
from core import ol
from factkit import facts_tpl, pair_tpls
import bank_m1, bank_m4, bank_a1, bank_a2, bank_ap, bank_grade, bank_more, bank_chem, bank_bio
import bank_thai as T, bank_eng as E, bank_soc as S, bank_kids as K, bank_entr as N

NOPT = 4
MODS = [bank_m1, bank_m4, bank_a1, bank_a2, bank_ap, bank_grade, bank_more, bank_chem, bank_bio, K]


def tpls(level, subjs):
    """รวม template ทุกเรื่องของระดับชั้น/วิชาที่กำหนด (ข้ามเรื่องที่ใช้ตัวสร้างแบบพิเศษ)"""
    out = []
    for m in MODS:
        for tid, (lv, sj, _) in m.NEW.items():
            if lv == level and sj in subjs and isinstance(m.TOPICS.get(tid), list):
                out += m.TOPICS[tid]
    assert out, (level, subjs)
    return out


def fill(pool):
    def t(rng, mc):
        q, a, w, why = rng.choice(pool)
        return mc(q, a, w, ol(why))
    return t


B = '_____'
ENG46 = [
    (f'My father {B} to work by car every day.', 'goes', ['go', 'going', 'is go'], 'every day + ประธานเอกพจน์ → goes'),
    (f'Look! The children {B} football.', 'are playing', ['play', 'plays', 'played'], 'Look! → กำลังทำ (are + V-ing)'),
    (f'We {B} to the zoo last Sunday.', 'went', ['go', 'goes', 'going'], 'last Sunday → อดีต (go → went)'),
    (f'There {B} three books on the table.', 'are', ['is', 'am', 'be'], 'three books เป็นพหูพจน์ → There are'),
    (f'There {B} a cat under the chair.', 'is', ['are', 'am', 'were'], 'a cat เอกพจน์ → There is'),
    (f'The ball is {B} the box. (อยู่ข้างใน)', 'in', ['on', 'under', 'at'], 'ข้างใน = in'),
    (f'The book is {B} the desk. (อยู่บนโต๊ะ)', 'on', ['in', 'under', 'between'], 'บนพื้นผิว = on'),
    (f'The shoes are {B} the bed. (อยู่ใต้เตียง)', 'under', ['on', 'in', 'above them'], 'ใต้ = under'),
    (f'I go to school {B} 7 o\'clock.', 'at', ['on', 'in', 'by'], 'at + เวลา'),
    (f'My birthday is {B} July.', 'in', ['on', 'at', 'to'], 'in + เดือน'),
    (f'We have English {B} Monday.', 'on', ['in', 'at', 'of'], 'on + วัน'),
    (f'An elephant is {B} than a dog.', 'bigger', ['big', 'biggest', 'more big'], 'เปรียบเทียบ 2 สิ่ง → bigger than'),
    (f'Somchai is the {B} boy in our class.', 'tallest', ['taller', 'tall', 'most tall'], 'the + -est (ขั้นสูงสุด)'),
    (f'{B} you like ice cream?', 'Do', ['Does', 'Are', 'Is'], 'you ใช้ Do'),
    (f'{B} she have a brother?', 'Does', ['Do', 'Is', 'Are'], 'she ใช้ Does'),
    (f'She {B} like spicy food.', "doesn't", ["don't", "isn't", "aren't"], "she + ปฏิเสธ → doesn't + V1"),
    (f'{B} is your favourite colour? – Blue.', 'What', ['Where', 'Who', 'When'], 'ถามสิ่งของ/สี → What'),
    (f'{B} do you live? – In Chiang Mai.', 'Where', ['What', 'When', 'Who'], 'ถามสถานที่ → Where'),
    (f'{B} is that man? – He is my uncle.', 'Who', ['What', 'Where', 'Which'], 'ถามบุคคล → Who'),
    (f'{B} is your birthday? – On 5 May.', 'When', ['Where', 'Who', 'How'], 'ถามเวลา/วัน → When'),
    (f'{B} much is this pen? – Ten baht.', 'How', ['What', 'Which', 'Who'], 'ถามราคา → How much'),
    (f'I can {B} English very well.', 'speak', ['speaks', 'speaking', 'spoke'], 'can + V1'),
    (f'Yesterday I {B} a nice movie.', 'watched', ['watch', 'watches', 'watching'], 'yesterday → V2 (watched)'),
    (f'This bag is {B}. It belongs to me.', 'mine', ['my', 'me', 'I'], 'ของฉัน (ใช้แทนคำนาม) → mine'),
    (f'Please give {B} the book. (ให้ฉัน)', 'me', ['I', 'my', 'mine'], 'กรรมของ I → me'),
    (f'Tom and I {B} good friends.', 'are', ['is', 'am', 'be'], 'Tom and I = we → are'),
    (f'She is reading {B} book now.', 'a', ['an', 'some', 'many'], 'book ขึ้นต้นด้วยเสียงพยัญชนะ → a'),
    (f'I eat {B} egg every morning.', 'an', ['a', 'many', 'two'], 'egg ขึ้นต้นด้วยเสียงสระ → an'),
    (f'How many {B} do you have?', 'pencils', ['pencil', 'a pencil', 'pencil\'s'], 'How many + คำนามพหูพจน์'),
    (f'They are {B} their homework now.', 'doing', ['do', 'does', 'did'], 'are + V-ing'),
    (f'Mali usually {B} breakfast at 7 a.m.', 'has', ['have', 'having', 'is have'], 'usually + ประธานเอกพจน์ → has'),
    (f'Last year we {B} in Bangkok.', 'were', ['was', 'are', 'is'], 'we + อดีต → were'),
]
VOC46 = [('teacher', 'ครู'), ('doctor', 'หมอ'), ('farmer', 'ชาวนา/เกษตรกร'), ('police officer', 'ตำรวจ'), ('nurse', 'พยาบาล'), ('cook', 'พ่อครัว/แม่ครัว'),
         ('hospital', 'โรงพยาบาล'), ('market', 'ตลาด'), ('library', 'ห้องสมุด'), ('post office', 'ที่ทำการไปรษณีย์'), ('temple', 'วัด'), ('airport', 'สนามบิน'),
         ('breakfast', 'อาหารเช้า'), ('vegetable', 'ผัก'), ('rice', 'ข้าว'), ('noodles', 'ก๋วยเตี๋ยว'), ('kitchen', 'ห้องครัว'), ('bedroom', 'ห้องนอน'),
         ('happy', 'มีความสุข'), ('hungry', 'หิว'), ('tired', 'เหนื่อย'), ('beautiful', 'สวยงาม'), ('cheap', 'ราคาถูก'), ('expensive', 'ราคาแพง'),
         ('run', 'วิ่ง'), ('swim', 'ว่ายน้ำ'), ('sleep', 'นอนหลับ'), ('wash', 'ล้าง'), ('buy', 'ซื้อ'), ('sell', 'ขาย'),
         ('Monday', 'วันจันทร์'), ('Wednesday', 'วันพุธ'), ('Friday', 'วันศุกร์'), ('January', 'มกราคม'), ('August', 'สิงหาคม'), ('December', 'ธันวาคม')]

SOC46 = S.REL[:16] + S.HIST[:16] + S.GEO[:16] + S.CIVIC[:12]
SCI46_LIFE = N.PSCI
P_THAI_MIX = [K.matra, K.classifier, T.tone] + pair_tpls(K.ANTONYM, 'คำใดมีความหมายตรงข้ามกับคำว่า “{k}”', None, lambda k, v: f'{k} ตรงข้ามกับ {v}')
ROYAL_F = pair_tpls(T.ROYAL, 'คำราชาศัพท์ “{k}” หมายถึงข้อใด', 'คำราชาศัพท์ของคำว่า “{v}” คือข้อใด', lambda k, v: f'{k} แปลว่า {v}')
IDIOM_F = pair_tpls(T.IDIOM, 'สำนวน “{k}” มีความหมายตรงกับข้อใด', 'ข้อใดเป็นสำนวนที่มีความหมายว่า “{v}”', lambda k, v: f'“{k}” หมายถึง {v}')
ENG_MS = [fill(E.TENSE), fill(E.GRAMMAR[:20]), fill(E.CONV)]
ENG_US = [fill(E.GRAMMAR), fill(E.TENSE[10:])] + pair_tpls(E.VOCAB_SYN, 'Choose the word closest in meaning to “{k}”.', None, lambda k, v: f'{k} ≈ {v}')
SOC_MS = [facts_tpl(S.REL + S.CIVIC), facts_tpl(S.HIST + S.GEO), S.era, S.time_zone, S.map_scale]
SOC_US = [facts_tpl(S.ECON + S.CIVIC), facts_tpl(S.HIST + S.REL + S.GEO), S.trade_bal, S.interest, S.century]

TOPICS = {
    # ป.4–6
    'p4-thai': P_THAI_MIX + ROYAL_F[:1] + IDIOM_F[:1],
    'p4-eng': [fill(ENG46), fill(ENG46)] + pair_tpls(VOC46, 'คำว่า “{k}” แปลว่าอะไร', 'ข้อใดแปลว่า “{v}”', lambda k, v: f'{k} = {v}'),
    'p4-sci': [facts_tpl(SCI46_LIFE), facts_tpl(SCI46_LIFE), bank_more.light_fact, bank_more.heat_fact, bank_more.earth_fact],
    'p4-soc': [facts_tpl(SOC46)],
    # ม.ต้น
    'm-thai': [T.word_kind, T.tone] + ROYAL_F + IDIOM_F,
    'm-eng': ENG_MS,
    'm-soc': SOC_MS,
    # ม.ปลาย
    'u-thai': [T.word_kind, T.tone] + IDIOM_F + ROYAL_F[1:],
    'u-eng': ENG_US,
    'u-soc': SOC_US,
    'u-chem': bank_chem.TOPICS['ch-mole'] + bank_chem.TOPICS['ch-atom'] + bank_chem.TOPICS['ch-sol'],
    'u-bio': bank_bio.TOPICS['bi-cell'] + bank_bio.TOPICS['bi-gen'] + [facts_tpl(bank_bio.BODY)],
    # RT ป.1
    'rt-word': [K.matra, K.k_thai] + pair_tpls(K.ANTONYM, 'คำใดมีความหมายตรงข้ามกับคำว่า “{k}”', None, lambda k, v: f'{k} ตรงข้ามกับ {v}'),
    # NT ป.3
    'nt-math': tpls('primary-low', ['math']),
    'nt-thai': [K.matra, K.classifier] + pair_tpls(K.ANTONYM, 'คำใดมีความหมายตรงข้ามกับคำว่า “{k}”', 'คำใดมีความหมายตรงข้ามกับคำว่า “{v}”', lambda k, v: f'{k} ตรงข้ามกับ {v}'),
    # O-NET ป.6
    'o6-math': tpls('primary', ['math']),
    'o6-thai': P_THAI_MIX + ROYAL_F + IDIOM_F,
    'o6-eng': [fill(ENG46), fill(E.CONV[:20])] + pair_tpls(VOC46, 'คำว่า “{k}” แปลว่าอะไร', None, lambda k, v: f'{k} = {v}'),
    'o6-sci': [facts_tpl(SCI46_LIFE), bank_more.light_fact, bank_more.heat_fact, bank_more.earth_fact, facts_tpl(K.SCI_LOW)],
    # O-NET ม.3
    'o3-math': tpls('lower-sec', ['math']),
    'o3-thai': [T.word_kind, T.tone] + ROYAL_F + IDIOM_F,
    'o3-eng': [fill(E.TENSE), fill(E.CONV), fill(E.GRAMMAR[:24])],
    'o3-sci': tpls('lower-sec', ['sci', 'phys']),
    # O-NET ม.6
    'o6m-math': tpls('upper-sec', ['math']),
    'o6m-thai': [T.word_kind, T.tone] + IDIOM_F + ROYAL_F,
    'o6m-eng': [fill(E.GRAMMAR), fill(E.CONV)] + pair_tpls(E.VOCAB_SYN, 'Choose the word closest in meaning to “{k}”.', None, lambda k, v: f'{k} ≈ {v}'),
    'o6m-sci': tpls('upper-sec', ['phys']) + bank_chem.TOPICS['ch-mole'] + bank_chem.TOPICS['ch-bond'] + [facts_tpl(bank_bio.ECO), facts_tpl(bank_bio.BODY)],
    'o6m-soc': [facts_tpl(S.REL), facts_tpl(S.CIVIC), facts_tpl(S.ECON), facts_tpl(S.HIST), facts_tpl(S.GEO), S.era, S.time_zone],
}
CUSTOM = {'rt-read': K.read_build, 'nt-read': K.read_build}
TOPICS.update(CUSTOM)

NEW = {
    'p4-thai': ('primary', 'thai', 'ภาษาไทย ป.4–6: ตัวสะกด ลักษณนาม วรรณยุกต์ คำตรงข้าม'),
    'p4-eng': ('primary', 'eng', 'English ป.4–6: Grammar & Vocabulary'),
    'p4-sci': ('primary', 'sci', 'วิทยาศาสตร์ ป.4–6'),
    'p4-soc': ('primary', 'soc', 'สังคมศึกษา ป.4–6'),
    'm-thai': ('lower-sec', 'thai', 'ภาษาไทย ม.ต้น: หลักภาษา ราชาศัพท์ สำนวน'),
    'm-eng': ('lower-sec', 'eng', 'English ม.ต้น: Tenses, Grammar, Conversation'),
    'm-soc': ('lower-sec', 'soc', 'สังคมศึกษา ม.ต้น'),
    'u-thai': ('upper-sec', 'thai', 'ภาษาไทย ม.ปลาย'),
    'u-eng': ('upper-sec', 'eng', 'English ม.ปลาย: Grammar & Vocabulary'),
    'u-soc': ('upper-sec', 'soc', 'สังคมศึกษา ม.ปลาย: เศรษฐศาสตร์ กฎหมาย ประวัติศาสตร์'),
    'u-chem': ('upper-sec', 'chem', 'เคมี ม.ปลาย: อะตอม โมล สารละลาย'),
    'u-bio': ('upper-sec', 'bio', 'ชีววิทยา ม.ปลาย: เซลล์ พันธุศาสตร์ ร่างกาย'),
    'rt-read': ('exam-rt', 'thai', 'RT ป.1: อ่านรู้เรื่อง'),
    'rt-word': ('exam-rt', 'thai', 'RT ป.1: อ่านออก (คำ พยัญชนะ ตัวสะกด)'),
    'nt-math': ('exam-nt', 'math', 'NT ป.3: ความสามารถด้านคำนวณ'),
    'nt-thai': ('exam-nt', 'thai', 'NT ป.3: ความสามารถด้านภาษาไทย'),
    'nt-read': ('exam-nt', 'thai', 'NT ป.3: การอ่านจับใจความ'),
    'o6-math': ('onet-p6', 'math', 'O-NET ป.6 คณิตศาสตร์'),
    'o6-thai': ('onet-p6', 'thai', 'O-NET ป.6 ภาษาไทย'),
    'o6-eng': ('onet-p6', 'eng', 'O-NET ป.6 ภาษาอังกฤษ'),
    'o6-sci': ('onet-p6', 'sci', 'O-NET ป.6 วิทยาศาสตร์'),
    'o3-math': ('onet-m3', 'math', 'O-NET ม.3 คณิตศาสตร์'),
    'o3-thai': ('onet-m3', 'thai', 'O-NET ม.3 ภาษาไทย'),
    'o3-eng': ('onet-m3', 'eng', 'O-NET ม.3 ภาษาอังกฤษ'),
    'o3-sci': ('onet-m3', 'sci', 'O-NET ม.3 วิทยาศาสตร์'),
    'o6m-math': ('onet-m6', 'math', 'O-NET ม.6 คณิตศาสตร์'),
    'o6m-thai': ('onet-m6', 'thai', 'O-NET ม.6 ภาษาไทย'),
    'o6m-eng': ('onet-m6', 'eng', 'O-NET ม.6 ภาษาอังกฤษ'),
    'o6m-sci': ('onet-m6', 'sci', 'O-NET ม.6 วิทยาศาสตร์'),
    'o6m-soc': ('onet-m6', 'soc', 'O-NET ม.6 สังคมศึกษา'),
}
