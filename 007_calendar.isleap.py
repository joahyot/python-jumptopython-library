#007_calendar.isleap.py
#calendar.isleap()은 인수로 입력한 연도가 윤년인지를 확인할 때 사용하는 함수

# 윤년 정하는 규칙
#1. 서력 기원 연수가 4로 나누어 떨어지는 해는 우선 윤년으로 한다.
#2. 그 중에서 100으로 나누어 떨어지는 해는 평년으로 한다.
#3. 400으로 나누어 떨어지는 해는 다시 윤년으로 한다. 

# 윤년의 2월달 일수는 28일이 아닌 29일이다.

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 ==0:
        return False
    
import calendar
print(calendar.isleap(0))
print(calendar.isleap(1))
print(calendar.isleap(4))
print(calendar.isleap(1200))
print(calendar.isleap(2000))
print(calendar.isleap(2023))

