#016_graphlib.TopologicalSorter.py
#위상 정렬에 사용하는 클래스
#위상 정렬(topological sorting)은 유향 그래프의 꼭짓점(vertex)을 변의 방향을 거스르지 않도록 나열하는 것을 의미한다.
#선후 관계가 정의된 그래프 구조에서 선후 관계에 따라 정렬하고자 위상 정렬을 이용한다.

#규칙1: 영어 초급 - 영어 중급 - 영어 고급
#규칙2: 영어 중급 - 영어 문법 - 영어 고급
#규칙3: 영어 문법 - 영어 회화

from graphlib import TopologicalSorter
ts = TopologicalSorter()

#규칙 1
ts.add('영어 중급', '영어 초급') # 영어 중급의 선수과목은 영어 초급 
ts.add('영어 고급', '영어 중급') # 영어 고급의 선수과목은 영어 중급

#규칙 2
ts.add('영어 문법', '영어 중급') # 영어 문법의 선수과목은 영어 중급
ts.add('영어 고급', '영어 문법') # 영어 고급의 선수과목은 영어 문법

#규칙 3 
ts.add('영어 회화', '영어 문법') # 영어 회화의 선수과목은 영어 문법

print(list(ts.static_order()))
