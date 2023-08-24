#003_re().py

# 파이썬에서 정규 표현식을 이용하려면 re모듈을 사용한다. 

# re_normal_sample.py
data = """
이다빈의 주민번호는 940117-1234567 입니다.
이연복의 주민번호는 890715-2134567 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# re_sample.py

import re 

data2 = """
이다빈의 주민번호는 940117-1234567 입니다.
이연복의 주민번호는 890715-2134567 입니다.
그렇다면 누가 형님일까요?
"""

#(\d{6})[-]\d{7}: 정규 표현식. 숫자6 +붙임표(-) +숫자7
pat = re.compile("(\d{6})[-]\d{7}")
#g<1>은 주민등록번호형식 문자열에서 바꾸지 않고 그대로 사용할 앞부분을 뜻함
print(pat.sub("\g<1>-*******", data2))

# re_sample02.py

data3 = """
이다빈의 핸드폰 번호는 010-5678-1258이고,
이연복의 핸드폰 번호는 010-2960-5107이다.
마지막 뒷번호 4자리 마스킹처리 해봐
"""

pat2 = re.compile("(\d{3})[-](\d{4})[-]\d{4}")
print(pat2.sub("\g<1>-\g<2>-****", data3))
