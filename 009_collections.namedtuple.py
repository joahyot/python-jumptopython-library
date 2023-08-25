#009_collections.namedtuple.py
#tuple()은 인덱스를 통해서만 접근 가능하지만 namedtuple()은 키로도 데이터에 접근할 수 있는 자료형


from collections import namedtuple

data = [
    ('이다빈', 30, '01000011112'),
    ('이연복', 35, '01051644258'),
    ('이유빈', 28, '01031254568')
]

emp = data[0]

Family = namedtuple('Family', 'name, age, cellphone')

data = [Family(emp[0], emp[1], emp[2]) for emp in data]
data = [Family._make(emp) for emp in data]
# 튜플의 요소가 많다면 _make() 함수를 사용하는 것이 유리함

emp = data[0]
print(emp.name)
print(emp.age)
print(emp.cellphone)

print(emp._asdict())

# namedtuple은 인덱스로 접근할 수 있음
print(emp[0])
print(emp[1])
print(emp[2])

#namedtuple은 값을 변경할 수 없기 때문에 _replace() 함수로만 값을 바꿀 수 있음
new_emp = emp._replace(name="이정우", age="55", cellphone="01096541236")
print(new_emp)