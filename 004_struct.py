#004_struct.py (X)
#struct는 C언어로 만든 구조체 이진 데이터를 처리할 때 활용하는 모듈

# struck 모듈의 unpack()함수를 사용하면 C구조체 데이터를 쉽게 읽을 수 있다
import struct
with open('output','rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)

