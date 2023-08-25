#collections.Counter.py
#collections.Counter()는 리스트나 문자열과 같은 자료형의 요소 중 값이 같은 요소가 몇개인지 확인하는 클래스

from collections import Counter
import re

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""


#정규표현식 \w+는 단어를 의미
#re.findall()함수를 이용하여 모든 단어를 리스트로 반환 
words = re.findall(r'\w+', data)
counter = Counter(words)

print(counter)
print(counter.most_common(1))
print(counter.most_common(2))

data2 = """
Programming exercises run directly 
in your browser (no setup required!) 
using the Colaboratory platform. 
Colaboratory is supported on most major 
browsers, and is most thoroughly tested 
on desktop versions of Chrome and Firefox. 
If you'd prefer to download and run the 
exercises offline, see these instructions 
for setting up a local environment."""

words2 = re.findall(r'\w+', data2)
counter2 = Counter(words2)
print(counter2)
print(counter2.most_common(2))
