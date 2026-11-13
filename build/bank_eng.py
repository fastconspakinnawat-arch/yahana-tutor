"""ภาษาอังกฤษ: Tenses, Grammar, Vocabulary, Conversation (แนว A-Level / TGAT)"""
from core import ol
from factkit import facts_tpl, pair_tpls

NOPT = 4
B = '_____'

# (sentence with blank, correct, [wrongs], why)
TENSE = [
    (f'She {B} to school every day.', 'walks', ['walk', 'is walking', 'walked'], 'every day = กิจวัตร → Present Simple; ประธานเอกพจน์บุรุษที่ 3 เติม -s'),
    (f'Look! The baby {B}.', 'is sleeping', ['sleeps', 'slept', 'has slept'], 'Look! = กำลังเกิดขึ้นขณะพูด → Present Continuous'),
    (f'I {B} this movie three times already.', 'have seen', ['saw', 'see', 'am seeing'], 'already / three times ถึงปัจจุบัน → Present Perfect'),
    (f'They {B} in Chiang Mai since 2019.', 'have lived', ['live', 'lived', 'are living'], 'since + จุดเวลา → Present Perfect'),
    (f'We {B} football yesterday afternoon.', 'played', ['play', 'have played', 'are playing'], 'yesterday = อดีตที่ระบุเวลา → Past Simple'),
    (f'When I arrived, the train {B}.', 'had already left', ['already leaves', 'has already left', 'is already leaving'], 'เหตุการณ์ที่เกิดก่อนอีกเหตุการณ์ในอดีต → Past Perfect'),
    (f'While I {B} dinner, the phone rang.', 'was cooking', ['cooked', 'am cooking', 'have cooked'], 'เหตุการณ์ที่กำลังดำเนินอยู่ในอดีตแล้วมีเหตุการณ์อื่นแทรก → Past Continuous'),
    (f'Water {B} at 100 °C.', 'boils', ['is boiling', 'boiled', 'has boiled'], 'ความจริงทั่วไป → Present Simple'),
    (f'I {B} you tomorrow, I promise.', 'will call', ['called', 'have called', 'am calling to'], 'คำสัญญา/ตัดสินใจทันที → will + V1'),
    (f'Look at those dark clouds! It {B} rain.', 'is going to', ['will be', 'has', 'was going'], 'คาดการณ์จากหลักฐานที่เห็น → be going to'),
    (f'By next year, she {B} from university.', 'will have graduated', ['graduates', 'has graduated', 'graduated'], 'By + เวลาในอนาคต → Future Perfect'),
    (f'He {B} for two hours when it finally stopped raining.', 'had been waiting', ['has waited', 'waits', 'is waiting'], 'ทำต่อเนื่องมาจนถึงจุดหนึ่งในอดีต → Past Perfect Continuous'),
    (f'Tom usually {B} coffee, but today he is drinking tea.', 'drinks', ['drink', 'is drinking', 'drank'], 'usually = นิสัย → Present Simple'),
    (f'I {B} my homework yet.', "haven't finished", ["didn't finish", "don't finish", "wasn't finishing"], 'yet ในประโยคปฏิเสธ → Present Perfect'),
    (f'Columbus {B} America in 1492.', 'reached', ['reaches', 'has reached', 'had been reaching'], 'ปีในอดีต → Past Simple'),
    (f'This time tomorrow, I {B} on the beach.', 'will be lying', ['lie', 'have lain', 'lay'], 'ช่วงเวลาที่กำลังเกิดในอนาคต → Future Continuous'),
    (f'She {B} English for five years and still studies it.', 'has been learning', ['learned', 'learns', 'had learned'], 'ทำต่อเนื่องจากอดีตถึงปัจจุบัน → Present Perfect Continuous'),
    (f'The film {B} at 8 p.m. tonight according to the schedule.', 'starts', ['started', 'has started', 'had started'], 'ตารางเวลาที่กำหนดไว้ → Present Simple ใช้แทนอนาคตได้'),
    (f'Last night I {B} a strange noise outside.', 'heard', ['hear', 'have heard', 'am hearing'], 'last night → Past Simple (hear → heard)'),
    (f'My brother {B} his leg, so he can\'t play today.', 'has broken', ['breaks', 'is breaking', 'will break'], 'ผลของเหตุการณ์ยังส่งถึงปัจจุบัน → Present Perfect'),
    (f'Listen! Someone {B} the piano.', 'is playing', ['plays', 'played', 'has played'], 'Listen! → Present Continuous'),
    (f'Before she moved to Bangkok, she {B} in Phuket.', 'had lived', ['has lived', 'lives', 'is living'], 'เกิดก่อนเหตุการณ์ในอดีตอีกเหตุการณ์ → Past Perfect'),
    (f'How long {B} you known each other?', 'have', ['did', 'do', 'are'], 'How long + Present Perfect: How long have you known…'),
    (f'I {B} to Japan twice, but never to Korea.', 'have been', ['went', 'go', 'am going'], 'ประสบการณ์ (twice / never) → Present Perfect'),
    (f'They {B} TV when the lights went out.', 'were watching', ['watched', 'are watching', 'have watched'], 'กำลังทำในอดีตแล้วมีเหตุการณ์แทรก → Past Continuous'),
    (f'If it rains tomorrow, we {B} at home.', 'will stay', ['stayed', 'would stay', 'stay'], 'If + Present Simple, will + V1 (Conditional Type 1)'),
    (f'Every morning, my parents {B} the news.', 'read', ['reads', 'are reading', 'have read'], 'ประธานพหูพจน์ + กิจวัตร → Present Simple ไม่เติม -s'),
    (f'I {B} the keys. Can you help me look for them?', 'have lost', ['lose', 'was losing', 'had been lost'], 'ผลยังอยู่ (ยังหาไม่เจอ) → Present Perfect'),
    (f'The museum {B} in 1850.', 'was built', ['built', 'has built', 'is building'], 'อาคารถูกสร้าง → Passive Past Simple'),
    (f'Next week, we {B} a test on Unit 5.', 'are having', ['had', 'have had', 'were having'], 'แผนที่นัดหมายไว้แล้ว → Present Continuous ใช้แทนอนาคต'),
    (f'Since she was a child, Mali {B} dancing.', 'has loved', ['loves', 'loved', 'is loving'], 'since + อดีตถึงปัจจุบัน → Present Perfect (love ไม่ใช้รูป -ing)'),
    (f'By the time we got to the cinema, the movie {B}.', 'had started', ['started', 'has started', 'starts'], 'By the time + Past → Past Perfect'),
]

GRAMMAR = [
    (f'If I {B} a bird, I would fly to you.', 'were', ['am', 'will be', 'have been'], 'Conditional Type 2 (สมมติตรงข้ามความจริงปัจจุบัน): If + V2 (be ใช้ were)'),
    (f'If she had studied harder, she {B} the exam.', 'would have passed', ['will pass', 'would pass', 'passed'], 'Conditional Type 3: If + had V3, would have V3'),
    (f'The letter {B} by my sister yesterday.', 'was written', ['wrote', 'is written', 'has written'], 'Passive Past: was/were + V3'),
    (f'English {B} in many countries.', 'is spoken', ['speaks', 'is speaking', 'spoke'], 'Passive Present: is + V3'),
    (f'The man {B} lives next door is a doctor.', 'who', ['which', 'whose', 'whom'], 'แทนคน ทำหน้าที่ประธาน → who'),
    (f'This is the book {B} I told you about.', 'which', ['who', 'whose', 'where'], 'แทนสิ่งของ → which/that'),
    (f'That is the girl {B} father is a pilot.', 'whose', ['who', 'which', 'whom'], 'แสดงความเป็นเจ้าของ → whose'),
    (f'This is the hotel {B} we stayed last summer.', 'where', ['which', 'who', 'whose'], 'แทนสถานที่ (stayed in the hotel) → where'),
    (f'Elephants are {B} than horses.', 'bigger', ['big', 'biggest', 'more big'], 'เปรียบเทียบสองสิ่ง + than → comparative (big → bigger)'),
    (f'Mount Everest is the {B} mountain in the world.', 'highest', ['higher', 'high', 'most high'], 'the + superlative'),
    (f'This exam is {B} than the last one.', 'more difficult', ['difficulter', 'most difficult', 'difficult'], 'คำคุณศัพท์ยาว → more + adj + than'),
    (f'I enjoy {B} books in my free time.', 'reading', ['to read', 'read', 'reads'], 'enjoy + V-ing'),
    (f'She decided {B} abroad.', 'to study', ['studying', 'study', 'studied'], 'decide + to V1'),
    (f'He is interested {B} science.', 'in', ['on', 'at', 'for'], 'be interested in'),
    (f'We arrived {B} the airport at noon.', 'at', ['in', 'on', 'to'], 'arrive at + สถานที่เฉพาะจุด'),
    (f'My birthday is {B} 5 May.', 'on', ['in', 'at', 'by'], 'on + วันที่'),
    (f'You {B} wear a seatbelt. It\'s the law.', 'must', ['might', 'could', 'would'], 'ข้อบังคับ/กฎหมาย → must'),
    (f'Neither the teacher nor the students {B} here.', 'are', ['is', 'was', 'be'], 'neither … nor … กริยาผันตามประธานตัวใกล้ (students → are)'),
    (f'Each of the boys {B} a bicycle.', 'has', ['have', 'are having', 'having'], 'Each of + พหูพจน์ ใช้กริยาเอกพจน์'),
    (f'She asked me where I {B}.', 'lived', ['live', 'do I live', 'did I live'], 'Reported speech: เลื่อน tense และไม่สลับกริยาช่วย'),
    (f'I wish I {B} more free time.', 'had', ['have', 'will have', 'am having'], 'wish (ปัจจุบัน) + V2'),
    (f'It\'s time we {B} home.', 'went', ['go', 'will go', 'going'], "It's time + S + V2"),
    (f'She is used to {B} up early.', 'getting', ['get', 'got', 'gets'], 'be used to + V-ing (เคยชิน)'),
    (f'He {B} smoke, but he quit last year.', 'used to', ['is used to', 'uses to', 'was used'], 'used to + V1 = เคยทำในอดีต ปัจจุบันไม่ทำแล้ว'),
    (f'I had my car {B} yesterday.', 'repaired', ['repair', 'repairing', 'to repair'], 'have + สิ่งของ + V3 (ให้ผู้อื่นทำให้)'),
    (f'Not only {B} late, but he also forgot his homework.', 'was he', ['he was', 'he is', 'is he'], 'Not only ขึ้นต้นประโยค → inversion (was he)'),
    (f'There isn\'t {B} milk left in the fridge.', 'any', ['some', 'many', 'a few'], 'ประโยคปฏิเสธ + นามนับไม่ได้ → any'),
    (f'I have {B} friends in this city, so I never feel lonely.', 'a lot of', ['much', 'a little', 'little'], 'friends นับได้ พหูพจน์ → a lot of / many'),
    (f'She speaks English very {B}.', 'fluently', ['fluent', 'fluency', 'more fluent'], 'ขยายกริยา speaks → adverb'),
    (f'Although it was raining, {B}.', 'we went out', ['but we went out', 'so we went out', 'because we went out'], 'Although ไม่ใช้คู่กับ but'),
    (f'The more you practise, the {B} you become.', 'better', ['good', 'best', 'more good'], 'The + comparative …, the + comparative …'),
    (f'He suggested {B} a taxi.', 'taking', ['to take', 'take', 'took'], 'suggest + V-ing'),
]

VOCAB = [('abundant', 'plentiful', 'มีมากมาย'), ('accurate', 'correct', 'แม่นยำ ถูกต้อง'), ('ancient', 'very old', 'โบราณ'),
         ('brave', 'courageous', 'กล้าหาญ'), ('cautious', 'careful', 'ระมัดระวัง'), ('diligent', 'hard-working', 'ขยันหมั่นเพียร'),
         ('enormous', 'huge', 'ใหญ่โตมาก'), ('fragile', 'easily broken', 'เปราะบาง แตกง่าย'), ('generous', 'giving', 'ใจกว้าง ชอบให้'),
         ('hazardous', 'dangerous', 'อันตราย'), ('obvious', 'clear', 'ชัดเจน เห็นได้ชัด'), ('rapid', 'fast', 'รวดเร็ว'),
         ('reluctant', 'unwilling', 'ไม่เต็มใจ'), ('scarce', 'rare', 'ขาดแคลน หายาก'), ('vital', 'essential', 'จำเป็นอย่างยิ่ง'),
         ('purchase', 'buy', 'ซื้อ'), ('assist', 'help', 'ช่วยเหลือ'), ('commence', 'begin', 'เริ่มต้น'), ('reside', 'live', 'อาศัยอยู่'),
         ('obtain', 'get', 'ได้รับ'), ('reduce', 'decrease', 'ลดลง'), ('expand', 'grow larger', 'ขยาย'), ('predict', 'forecast', 'ทำนาย คาดการณ์'),
         ('postpone', 'delay', 'เลื่อนออกไป'), ('conceal', 'hide', 'ซ่อน ปกปิด'), ('anxious', 'worried', 'วิตกกังวล'),
         ('furious', 'very angry', 'โกรธจัด'), ('exhausted', 'very tired', 'เหนื่อยมาก'), ('delighted', 'very happy', 'ยินดีมาก'),
         ('humble', 'modest', 'ถ่อมตัว'), ('wealthy', 'rich', 'ร่ำรวย'), ('evident', 'apparent', 'ประจักษ์ชัด'), ('sufficient', 'enough', 'เพียงพอ'),
         ('beneficial', 'helpful', 'เป็นประโยชน์'), ('pollution', 'contamination', 'มลพิษ'), ('opportunity', 'chance', 'โอกาส')]
VOCAB_SYN = [(w, s) for w, s, _ in VOCAB]
VOCAB_TH = [(w, t) for w, _, t in VOCAB]

CONV = [
    ('A: Thank you so much for your help.<br>B: ' + B, "You're welcome.", ['Yes, please.', 'Never mind me.', 'I agree with you.'], 'ตอบรับคำขอบคุณ → You\'re welcome.'),
    ('A: I\'m sorry I\'m late.<br>B: ' + B, "That's all right.", ["You're welcome.", 'Congratulations!', 'Same to you.'], 'ตอบรับคำขอโทษ → That\'s all right / No problem.'),
    ('A: Would you like some more cake?<br>B: ' + B, 'No, thanks. I\'m full.', ['Yes, I would like.', "I don't mind you.", 'Help yourself.'], 'ปฏิเสธข้อเสนออย่างสุภาพ'),
    ('A: Could you pass me the salt, please?<br>B: ' + B, 'Sure, here you are.', ['Yes, I could.', "You're welcome.", 'It doesn\'t matter.'], 'ส่งของให้ → Here you are.'),
    ('A: I passed the exam!<br>B: ' + B, 'Congratulations!', ['Bless you!', 'Never mind.', 'Excuse me.'], 'แสดงความยินดี → Congratulations!'),
    ('A: Achoo!<br>B: ' + B, 'Bless you!', ['Congratulations!', 'Cheers!', 'Good luck!'], 'เมื่อมีคนจาม → Bless you!'),
    ('A: I have a job interview tomorrow.<br>B: ' + B, 'Good luck!', ['Well done!', 'Bless you!', 'Same here.'], 'อวยพรก่อนทำสิ่งสำคัญ → Good luck!'),
    ('A: How do you do?<br>B: ' + B, 'How do you do?', ["I'm fine, thanks.", 'I do my homework.', 'Very well done.'], 'การทักทายครั้งแรกแบบทางการ ตอบด้วย How do you do?'),
    ('A: Do you mind if I open the window?<br>B: ' + B, 'Not at all. Go ahead.', ['Yes, please open it.', 'Yes, I do. Go ahead.', 'No, I mind.'], 'Do you mind…? ถ้าอนุญาตตอบ Not at all / No, go ahead.'),
    ('A: What does your father do?<br>B: ' + B, "He's an engineer.", ['He is doing fine.', 'He likes swimming.', "He's in the kitchen."], 'What does … do? ถามอาชีพ'),
    ('A: How often do you go to the gym?<br>B: ' + B, 'Three times a week.', ['For two hours.', 'By bus.', 'Last Monday.'], 'How often ถามความถี่'),
    ('A: How long does it take to get there?<br>B: ' + B, 'About twenty minutes.', ['Twice a day.', 'It is 5 km.', 'At eight o\'clock.'], 'How long ถามระยะเวลา'),
    ('A: My grandmother passed away last week.<br>B: ' + B, "I'm sorry to hear that.", ["That's great news.", 'Good for you.', 'Never mind.'], 'แสดงความเสียใจ'),
    ('A: Let\'s go to the beach this weekend.<br>B: ' + B, 'That sounds like a great idea.', ['Yes, I went.', "You're right, I'm busy.", 'Thank you, too.'], 'ตอบรับคำชวน'),
    ('A: Excuse me, how can I get to the post office?<br>B: ' + B, 'Go straight and turn left at the corner.', ["It's open until five.", 'I sent a letter yesterday.', 'Yes, you can.'], 'ถามทาง → บอกเส้นทาง'),
    ('A: What\'s the matter? You look pale.<br>B: ' + B, "I've got a terrible headache.", ["I'm looking at you.", 'Nothing is pale.', 'It matters a lot.'], 'What\'s the matter? ถามว่าเป็นอะไร'),
    ('A: Can I speak to Mr. Lee, please?<br>B: ' + B, 'Hold on, please.', ['Speaking slowly.', 'Yes, you speak.', 'Leave me alone.'], 'ภาษาโทรศัพท์: Hold on = รอสักครู่'),
    ('A: I don\'t like spicy food.<br>B: ' + B, 'Neither do I.', ['So do I.', 'Me too, I like it.', 'So am I.'], 'เห็นด้วยกับประโยคปฏิเสธ → Neither do I.'),
    ('A: I love watching football.<br>B: ' + B, 'So do I.', ['Neither do I.', 'So am I.', 'Me neither.'], 'เห็นด้วยกับประโยคบอกเล่า → So do I.'),
    ('A: Have a nice weekend!<br>B: ' + B, 'Thanks, you too.', ["You're welcome.", 'Yes, I have.', 'Same weekend.'], 'ตอบคำอวยพร → You too / Same to you.'),
    ('A: Would you mind closing the door?<br>B: ' + B, 'Of course not.', ['Yes, I close it.', 'Of course I mind, sure.', 'No, thanks.'], 'Would you mind…? ถ้ายินดีทำให้ ตอบ Of course not / Not at all.'),
    ('A: How much is this T-shirt?<br>B: ' + B, "It's 250 baht.", ["It's very much.", 'Two shirts.', "It's made of cotton."], 'How much ถามราคา'),
    ('A: Whose bag is this?<br>B: ' + B, "It's Nida's.", ["It's on the table.", "It's blue.", "It's a bag."], 'Whose ถามความเป็นเจ้าของ'),
    ('A: I\'m afraid I can\'t come to your party.<br>B: ' + B, "That's a pity. Maybe next time.", ["Great! See you there.", "You're welcome.", 'Yes, you can.'], 'ผิดหวังอย่างสุภาพเมื่อถูกปฏิเสธ'),
    ('A: Shall we have lunch now?<br>B: ' + B, "Yes, let's.", ['Yes, we shall have.', 'No, we have.', 'Yes, I shall.'], 'Shall we…? ตอบรับ → Yes, let\'s.'),
    ('A: May I borrow your pen?<br>B: ' + B, 'Sure, go ahead.', ['Yes, you borrow.', 'No, thanks.', "You're welcome."], 'ขออนุญาต → Sure / Go ahead.'),
    ('A: What\'s the weather like today?<br>B: ' + B, "It's hot and sunny.", ['I like weather.', "It's Monday.", 'It is like a cloud.'], 'What\'s … like? ถามลักษณะ'),
    ('A: Nice to meet you.<br>B: ' + B, 'Nice to meet you, too.', ["I'm fine, thank you.", 'See you later.', 'How are you?'], 'ตอบการทักทายเมื่อพบครั้งแรก'),
    ('A: Could you help me with this box?<br>B: ' + B, 'Sure, no problem.', ['No, thank you.', "You're welcome.", 'Yes, I could not.'], 'ตอบรับคำขอความช่วยเหลือ'),
    ('A: Which do you prefer, tea or coffee?<br>B: ' + B, "I'd rather have tea.", ['Yes, I prefer.', 'Both are drinks.', 'I prefer than coffee.'], "บอกความชอบ → I'd rather / I prefer"),
    ('A: I think we should leave early to avoid traffic.<br>B: ' + B, 'I agree with you.', ['I agree to you.', "You're welcome.", 'Same to you.'], 'แสดงความเห็นด้วย → I agree with you.'),
    ('A: How are you getting on with your new job?<br>B: ' + B, "Pretty well, thanks.", ['By car.', 'At nine o\'clock.', 'Getting on a bus.'], 'How are you getting on? = เป็นอย่างไรบ้าง'),
]


def fill(pool):
    def t(rng, mc):
        q, a, w, why = rng.choice(pool)
        return mc(q, a, w, ol(why))
    return t


TOPICS = {
    'en-tense': [fill(TENSE)],
    'en-gram': [fill(GRAMMAR)],
    'en-vocab': pair_tpls(VOCAB_SYN, 'Choose the word closest in meaning to “{k}”.', None, lambda k, v: f'{k} ≈ {v}')
                + pair_tpls(VOCAB_TH, 'คำว่า “{k}” แปลว่าอะไร', 'ข้อใดแปลว่า “{v}”', lambda k, v: f'{k} = {v}'),
    'en-conv': [fill(CONV)],
}
NEW = {
    'en-tense': ('alevel-eng', 'eng', 'Tenses'),
    'en-gram': ('alevel-eng', 'eng', 'Grammar & Structure'),
    'en-vocab': ('alevel-eng', 'eng', 'Vocabulary'),
    'en-conv': ('alevel-eng', 'eng', 'Conversation'),
}
