# 048~053_data compression and release.py

# 048. 데이터 크기를 줄여 전송하려면? -- zlib 
# 데이터를 압축하거나 해제할 때 사용하는 모듈 

import zlib

data = "Life is too short, You need python." * 10000
compress_data = zlib.compress(data.encode(encoding='utf-8'))
print(len(compress_data))    # 1077 출력

org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data))     # 350000출력



# 049. 파일을 압축하거나 해제할 때 사용하는 모듈 

import gzip

with gzip.open('data.txt.gz', 'wb') as f:
    f.write(data.encode('utf-8'))  

with gzip.open('data.txt.gz', 'rb') as f:
    read_data = f.read().decode('utf-8')

assert data == read_data

print(len(data))


# 050. bzip2 알고리즘으로 압축하려면? -- bz2
# 압축 알고리즘으로 데이터를 압축하거나 해제할 때 사용하는 모듈
# zlib와 사용법이 같으나 bz2는 스레드 환경에서 안전하다는 특징이 있음

import bz2

data1 = "Today is awsome. I am happy." * 1000
compress_data1 = bz2.compress(data1.encode(encoding='utf-8'))
print(len(compress_data1))     # 118

org_data1 = bz2.decompress(compress_data1).decode('utf-8')
print(len(org_data1))         #28000

assert data1 == org_data1

# 051. lZMA 알고리즘으로 압축하려면? -- lzma

# 052. 여러 파일을 zip으로 합치려면? -- zipfile
# 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈 

import zipfile

# 파일 합치기
with zipfile.Zipfile('mytext.zip','w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zipfile.Zipfile('mytext.zip') as myzip:
    myzip.extrctall()

# 합친 파일에서 특정 파일만 해제하기
with zipfile.Zipfile('mytext.zip') as myzip:
    myzip.extract('a.txt')


# 053. 여러 파일을 tar로 합치려면? -- tarfile