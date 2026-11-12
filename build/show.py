import json,re,sys
b=json.load(open('bank.json'))['bank']
strip=lambda s:re.sub('<[^>]+>',' ',re.sub(r'<span class="fr"><span>(.*?)</span><span>(.*?)</span></span>',r'(\1/\2)',s))
step=int(sys.argv[1]) if len(sys.argv)>1 else 6
for t,qs in b.items():
    print('==',t)
    for q in qs[::step]:
        ans = q['c'][q['a']] if q['t']=='mc' else q['a']
        opts = ' / '.join(strip(c) for c in q['c']) if q['t']=='mc' else ''
        print(' Q:',strip(q['q'])[:140],'| A:',strip(str(ans)),'| opts:',opts[:90],'|',strip(q['s'])[:170])
