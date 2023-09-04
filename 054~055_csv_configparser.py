# 054~055_csv_configparser.py

# 054 csv 파일을 읽고 쓰려면? -- csv

import csv

result = []
with open('score.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.reader(f)
    for line in reader:
        average = sum(map(int, line[1].split(','))) / 2
        line.append(average)
        result.append(line)

with open('score_result.csv', 'w', newline ='') as f:
    writer = csv.writer(f)
    writer.writerows(result)


# 055 설정 파일에서 정보를 읽으려면? -- configparser
# ini 파일은 프로그램 정보를 저장하는 텍스트 문서로, [섹션]과 그 섹션에 해당하는 키 = 값으로 구성된다.
# configparser는 이러한 형식의 ini 파일을 처리할 때 사용하는 모듈 

[FTP1]
SERVER_IP = 111.23.56.78
PORT = 21
USERNAME = foo
PASSWORD = bar

[FTP2]
SERVER_IP = 111.23.56.79
PORT = 22221
USERNAME = admin
PASSWORD = hello

import configparser

config = configparser.ConfigParser()
config.read('ftp.ini')
config.['FTP2']['PORT']

print(ftp2_port) 