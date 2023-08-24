#008_collection.deque.py
#collection.deque 모듈은 deque 자료형을 생성하는 모듈 

# 리스트를 n만큼 회전할때 x가 나오려면?

from collections import deque
a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)
result = list(q)
print(result)


