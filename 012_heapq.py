#012_heapq.py
#heapq는 순위가 가장 높은 자료를 가장 먼저 꺼내는 우선순위 큐를 구현한 모듈.

import heapq

data = [
    (11.20, "이다빈"),
    (10.29, "이연복"),
    (14.11, "최인녕"),
    (12.11, "이유빈"),
    (10.12, "메에리"),
    (10.00, "꼬오리")
]

h = []  #힙생성
for score in data:
    heapq.heappush(h, score)   #힙에 데이터 저장

for i in range(3):
    print(heapq.heappop(h))    #최솟값부터 힙 반환


heapq.heapify(data)
for i in range(3):
    print(heapq.heappop(data))

# print(heapq.nsmallest(3,data))
#heapq.nsmallest(n, iterable)는 반복 가능한 객체 데이터 집합에서 n개의 가장 작은 요소로 구성된 리스트
#heapq.nlargest(n,data) : 꼴찌부터 순서대로 반환 
print(heapq.nlargest(3,data))