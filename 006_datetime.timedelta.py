#006_datetime.timedelta.py
#datetime.timedelta()는 두 날짜의 차이를 계산할 때 사용하는 함수

import datetime
today = datetime.date.today()
print(today)

diff_days = datetime.timedelta(days=100)
print(diff_days)

# 오늘 날짜 + 100일
print(today + diff_days)
# 오늘 날짜 - 100일
print(today - diff_days)

#기혼 몇일차
after_m = today - datetime.date(2023, 5, 5)
print(after_m.days)