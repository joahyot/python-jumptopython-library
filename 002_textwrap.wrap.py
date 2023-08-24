#002_textwrap.wrap().py
#textwrap.warp()함수는 긴 문자열을 width 길이만큼 자르고 리스트로 반환
import textwrap
long_text = 'Life is too short, you need python. ' * 10
result = textwrap.wrap(long_text, width=70)
print(result)

# '\n\.join()는 리스트 요소 사이에 줄 바꿈 문자를 넣어 하나로 합친다.  
print('\n'.join(result))

# width; 각 줄의 길이를 뜻함
result = textwrap.fill(long_text, width=100) 
print(result)


data = 'python is fun. ' * 20
result2 = textwrap.wrap(data, width=50)
print('\n'.join(result2))

