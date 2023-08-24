#001_textwrap.shorten()함수

import textwrap
print(textwrap.shorten("Life is too short, you need python", width=15))

print(textwrap.shorten("인생을 짧으니 파이썬이 필요해", width=15, placeholder='...'))

print(textwrap.shorten("Life is too short, you need python", width=15, placeholder='...'))

print(textwrap.shorten("인생을 짧으니 파이썬이 필요해", width=10, placeholder='...'))