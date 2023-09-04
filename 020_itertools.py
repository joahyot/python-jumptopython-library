#020_itertools.cycle.py

# (1)itertools.cycle.py - 상담원을 순서대로 배정하려면? 

# itertools.cycle(iterable)은 반복 가능한 객체를 순서대로 무한히 반복하는 이터레이터를 생성하는 함수

import itertools

emp_pool = itertools.cycle(['이다빈', '이연복', '이유빈'])
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))
print(next(emp_pool))

# next() 함수는 파이썬 내장함수로, 이터레이터의 다음 요소를 반환하는 함수

# (2)itertools.accumulate.py  - 연간 매출액을 계산하려면?
# 반복 가능한 객체의 누적합을 계산하여 이터레이터로 변환하는 함수

# 어떤 회사의 1월부터 12월까지의 매출 데이터(단위는 만원) 
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))

print(result) # [1161, 2975, 4245, 6501, 7914, 9756, 11977, 14184, 16634, 19457, 21997, 24131] 

result1 = list(itertools.accumulate(monthly_income, max)) # 1월부터 12월까지 그때까지의 최대 월수입을 표시하고 싶다면 max
print(result1)

# (3) itertools.groupby  - 키값으로 데이터를 묶으려면?
# itertools.groupby은 반복 간으한 객체를 키값으로 분류하고 그 결과를 반환하는 함수 

import itertools
import operator
import pprint

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]

data = sorted(data, key = operator.itemgetter('blood'))  # groupby 전 분류 기준으로 정렬
grouped_data = itertools.groupby(data, key = operator.itemgetter('blood'))

result2 = {}
for key, group_data in grouped_data:
    result2[key] = list(group_data)  # group_data는 이터레이터이므로 리스트로 변경

print(pprint.pprint(result))


# (4) itertools.zip_longest  - 부족한 것을 채워 묶으려면?
# 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip()과 똑같이 동작한다. 
# 하지만, itertools.zip_longest 함수는 전달한 반복 가능 객체(*iterables)의 길이가 다르다면 긴 것을 기준으로 빠진 값은 fillvalue에서 설정한 값으로 채운다

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초콜릿', '젤리']

result3 = zip(students, rewards)
print(list(result3))

result4 = itertools.zip_longest(students, rewards, fillvalue= '새우깡') 
print(list(result4))


# (5) itertools.permutations  - 순서를 생각하며 카드를 뽑으려면?
# itertools.permutations은 반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수

print(list(itertools.permutations(['1', '2', '3'], 2))) 

for a, b in itertools.permutations(['1', '2', '3'], 2):
    print(a+b)


# (6) itertools.combinations - 로또의 모든 가짓수를 구하려면? 
# 반복 가능한 객체 중에서 r개를 선택한 조합을 iterator로 변환하는 함수

# 3장의 카드에서 순서 상관없이 2장을 고르는 조합 : itertools.combinations() 
print(list(itertools.combinations(['1', '2', '3'], 2)))

# 1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고 그 개수를 출력하면 어떻게 해야할까?
lotto = itertools.combinations(range(1, 46), 6)

# for num in lotto: 
#     print(num) 

print(len(list(itertools.combinations(range(1, 46), 6)))) # 중복 불허용시 경우의 수 : 8145060

print(len(list(itertools.combinations_with_replacement(range(1, 46), 6))))  # 중복 허용시 경우의 수 : 15890700
