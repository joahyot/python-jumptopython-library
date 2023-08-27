#017_math

#math.gcd.py
#최대공약수(gcd, greatest common divisor)를 쉽게 구할 수 있다.

#<문제>
#어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 아이들이 서로 싸우지 않도록 똑같이 나누어 봉지에 담는다고 하면 최대 몇 봉지까지 만들 수 있을까? 
print("---math.gcd(최대공약수)---")
import math
print(math.gcd(60, 80, 100))

print(60/20, 100/20, 80/20)

#math.lcm.py
#최소공배수(lcm, least common multiple)를 구하는 함수이다.

#문제
#어느 버스 정류장에 시내버스는 15분마다 도착하고 마을버스는 25분마다 도착한다고 한다. 
#오후 1시에 두 버스가 동시에 도착했다고 할 때 두 버스가 동시에 도착할 다음 시각을 알려면 어떻게 해야 할까?
#2시 15분
print("---math.lcm(최소공배수)---")
print(math.lcm(15,25))


#decimal.Decimal은 숫자를 10진수로 처리하여 정확한 소수점 자릿수를 표현할 때 사용하는 모듈이다.
print("---math.isclose---")
#같은지를 비교하는 == 연산자 대신 두 값이 가까운지를 확인하는 math.isclose() 함수를 사용하는 방법
print(math.isclose(0.1*3, 0.3))
print(math.isclose(1.2-0.1, 1.1))
print(math.isclose(0.1*0.1, 0.01))

#하지만, 두 값이 서로 가까우면 True를 반환하는 math.isclose()는 완전한 해결이 될 수 없다. 
#그러므로 십진수 연산을 사용하는 decimal.Decimal을 사용하여 문제를 해결해야 한다. 
print("---decimal.Decimal---")
from decimal import Decimal
print(Decimal('0.1') * 3)
print(Decimal('1.2') - Decimal('0.1'))
print(Decimal('0.1') * Decimal('0.1'))

print(float(Decimal('1.2')-Decimal('0.1'))==1.1)


#fractions는 유리수를 계산할 때 사용하는 모듈
print("---fractions.Fraction---")
from fractions import Fraction
a = Fraction(1, 5)
print(a)

b = Fraction('1/5')
print(a)

print(a.numerator) # 분자의 값
print(a.denominator) # 분모의 값

result = Fraction(1,5) + Fraction(3,5)
print(result)

print(float(result))

# tatistics는 평균값과 중앙값을 구할 때 사용하는 모듈이다.
print("---statistics---")

# 다른 반과 비교하고자 이 데이터를 이용하여 A반 수학 점수의 평균값과 중앙값을 구하려면 어떻게 해야 할까?

import statistics
marks = [ 70, 34, 77, 89, 90, 100, 55, 81]
print(statistics.mean(marks)) # 평균값
print(statistics.median(marks)) # 중앙값


