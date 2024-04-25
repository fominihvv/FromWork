import random

l = 'йфяцычувскамепинртгоьшлбщдюзжхэъ'
e = ['','ея']

word = [''.join(random.choice(l) for _ in range(random.randint(3,20))) + random.choice(e) for j in range(4_000)]
with open('words_4k.txt', 'w', encoding='utf-8') as fi:
    print(*word, file=fi, sep='\n')

