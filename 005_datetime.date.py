#005_datetime.date.py
#datetime.date는 년,월,일로 날짜를 표현할 때 사용하는 모듈

import datetime
day1 = datetime.date(2019, 12, 14)
print(day1)

day2 = datetime.date(2021, 6, 5)
print(day2)

diff = day2 - day1
print(diff.days)

#요일 판별하기 
#weekday(): 0:월요일, 1:화요일 , 2:수요일, 3:목요일, 4:금요일, 5:토요일, 6:일요일
day = datetime.date(2019, 12, 15)
print(day.weekday())

#isoweekday(): 1:월요일, 2:화요일 , 3:수요일, 4:목요일, 5:금요일, 6:토요일, 7:일요일
print(day.isoweekday())

