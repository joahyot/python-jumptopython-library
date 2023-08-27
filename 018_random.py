#018_random.py
#난수를 생성할 때 사용하는 모듈

#문제
#1부터 45 사이의 서로 다른 숫자 6개로 이루어진 로또 번호를 추첨하는 프로그램을 만들려면 어떻게 해야 할까?
#단, 숫자는 중복될 수 없다.

import random

result = []
while len(result) < 6:
    num = random.randint(1,45) #1~45 사이의 숫자 중 임의의 숫자 생성
    if num not in result: #중복 숫자 뽑기 방지
        result.append(num)

print(result) #무작위의 6개 숫자 출력

# sample과 choice
# 리스트 요소를 무작위로 섞고 싶다면 random.sample()
a = [1, 2, 3, 4, 5]
print(random.sample(a, len(a))) #len(a)는 무작위로 추출할 원소 갯수

# 리스트 요소에서 무작위로 하나를 선택하려면 random.choice()
b = [6,7,8,9,10]
print(random.choice(b))



