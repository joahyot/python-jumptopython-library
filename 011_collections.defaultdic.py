#011_collections.defaultdic.py
#collections.defaultdic()는 값에 초깃값을 지정하여 딕셔너리를 생성하는 모듈

text = "Life is too short, You need python."

d = dict()
for c in text: 
    if c not in d:
        d[c] = 0
    d[c] +=1 
print(d)

from collections import defaultdict

d1 = defaultdict(int)
for c in text: 
    d1[c] += 1
print(dict(d1))
