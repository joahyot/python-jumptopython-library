#008_collection.deque.py
#collection.deque 모듈은 deque 자료형을 생성하는 모듈 

# 리스트를 n만큼 회전할때 x가 나오려면?

from collections import deque
a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)
result = list(q)
print(result)

# deque와 list는 매우 비슷
# 스택과 큐로 사용할 수 있는 메소드도 대부분 일치
b = [1, 3, 5, 7, 9, 11, 13, 15]
q1 = deque(b)
q1.rotate(2)
result1 = list(q1)
print(result1)


d = deque([1,2,3,4,5])
d.append(6)
print(d)

d.appendleft(0)
print(d)

print(d.pop())
print(d)
d.popleft()
print(d)

