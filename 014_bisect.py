#014_bisect.py
#bisect는 이진 탐색 알고리즘을 구현한 모듈로, bisect.bisect() 함수는 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환한다. 

22, 33, 55, 78, 89, 90, 100

import bisect

# 이상인 경우
result = []
for score in [22, 33, 55, 80, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)  # 점수를 삽입할 위치 반환
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)

# 초과인 경우
result1 = []
for score in [22, 33, 55, 78, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)
    grade = 'FDCBA'[pos]
    result1.append(grade)

print(result1)

#bisect.insort(); 정렬할 수 있는 위치에 해당 항목을 삽입한다 
a = [60, 70, 80, 90]
bisect.insort(a, 85)
print(a)