# 021_functools.py  --> 어려움 / 다시 복습 필요 

# (1) 순서대로 좌표를 정렬하려면? - functools.cmp_to_key
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:     # y 좌표가 크면
        return 1 
    elif n1[1] == n2[1] :
        if n1[0] > n2[0] : 
            return 1
        elif n1[0] == n2[0] : # x 좌표가 크면
            return 0
    else:
        return -1 

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key = functools.cmp_to_key(xy_compare))

print(result)

# xy_compare()와 같이 정렬에 사용하는 함수는 반드시 3가지 중 하나를 반환해야한다. 
# 크다(양수반환) / 작다(음수반환) / 같다(0반환) 

# (2) web page를 임시로 저장하려면? - functools.lru_cache
# 함수의 반환 결과를 캐시하는 데코레이터. 
# LRU(Least Recently Used); 최근에 참조되지 않은 데이터가 교체 시점에 먼저 나가는 방식 

# 위키독스의 특정 페이지를 가져오는 프로그램이다. 이 프로그램의 성능을 향상하고자 같은 페이지를 다시 요청할 때는 캐시를 사용하도록 하려면 어떻게 해야할까? 

import urllib.request

def get_wikidocs(page):                     # get_wikidocs() 함수는 위키독스의 페이지 번호를 입력받아 해당 페이지의 내용을 읽어 반환하는 함수
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력 
    resource = 'http://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'
    

# (3) 기존 함수로 새로운 함수를 만들려면? - functools.partial 
# 하나 이상의 인수가 이미 채워진 새 버전의 함수를 만들 때 사용하는 함수 

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + 1
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

def add(*args): 
    return add_mul('add', *args)

def mul(*args):
    return add_mul('mul', *args)

print(add(1, 2, 3, 4, 5))
print(mul(1, 2, 3, 4, 5))

# functools.partial()을 사용

from functools import partial

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + 1
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1, 2, 3, 4, 5))
print(mul(1, 2, 3, 4, 5))



# (4) 함수를 적용하여 하나의 값으로 줄이려면? - functools.reduce
# funtion을 반복 가능한 객체의 요소에 차례대로(왼쪽에서 오른쪽) 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수

data = [1, 2, 3, 4, 5]
result2 = functools.reduce(lambda x, y: x + y, data) 
print(result2)  # 15 출력 --> ((((1+2)+3)+4)+5)

# functools.reduce()로 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num) 

## functools.reduce()로 최솟값 구하기
num_list = [3, 2, 8, 1, 6, 7]
min_num = functools.reduce(lambda x, y: x if x < y else y, num_list)
print(min_num)



# (5) 다양한 기준으로 정렬하려면? - operator.itemgetter
# 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬될 수 있도록 하는 모듈

from operator import itemgetter

students = [('Dab', 30, 'A'),
            ('Bok', 35, 'B'),
            ('Yoo', 28, 'B')]

result3 = sorted(students, key = itemgetter(1)) # itemgetter(1)은 튜플의 2번째 요소를 기준으로 정렬하겠다는 의미
print(result3)


# operator.attrgetter() : 리스트의 요소가 튜플이 아닌 클래스의 객체라면 attrgetter()를 적용해야한다. 

from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result4 = sorted(students, key=attrgetter('age'))  # Student 객체의 age속성으로 정렬하겠다는 의미
print(result4)
