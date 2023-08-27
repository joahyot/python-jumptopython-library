#015_enum.py
#enum은 서로 관련이 있는 여러개의 상수 집합을 정의할 때 사용하는 모듈 

from datetime import date

def get_menu(input_date):
    weekday = input_date.isoweekday()  #1: 월요일, 2: 화요일, ... , 7:일요일
    if weekday == 1:
        menu = "김치찌개"
    elif weekday == 2:
        menu = "비빔밥"
    elif weekday == 3:
        menu = "된장찌개"
    elif weekday == 4:
        menu = "불고기"
    elif weekday == 5:
        menu = "치즈라면"
    elif weekday == 6: 
        menu = "김치볶음밥"
    elif weekday == 7:
        menu = "피자"
    return menu 

print(get_menu(date(2021,9,6)))
print(get_menu(date(2022,12,5)))

# 프로그래밍에서 상수로 선언하지 않은 숫자를 매직넘버라 한다 

from datetime import date
from enum import IntEnum

class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_menu(input_date):
    menu = {
        Week.MONDAY: "김치찌개",
        Week.TUESDAY: "비빔밥",
        Week.WEDNESDAY: "된장찌개",
        Week.THURSDAY: "불고기",
        Week.FRIDAY: "치즈라면",
        Week.SATURDAY: "김치볶음밥",
        Week.SUNDAY: "피자"
    }
    return menu[input_date.isoweekday()]

print(get_menu(date(2020, 6, 4)))
print(get_menu(date(2023, 1 ,17)))

