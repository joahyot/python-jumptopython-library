# 040~047_data install and management.py
# 데이터 저장하고 관리하기 

# 044_객체를 파일로 저장하고 불러오려면? -- pickle
# 파이썬에서 사용하는 딕셔너리, 리스트, 클래스 등의 자료형을 변환없이 그대로 파일로 저장하고 이를 불러올 때 사용하는 모듈 

# add_data(no, subject, content)  # no: 번호, subject: 제목, content: 내용 
import pickle

data = {}
data[1] = {'no':1, 'subject': '안녕 피클', 'content': '피클은 매우 간단하다'}

with open('pickle_install.p', 'wb') as f:
    pickle.dump(data, f)

with open('pickle_install.p', 'rb') as f:
    data = pickle.load(f)

print(data)



# 045_객체 변경에 따른 오류를 방지하려면? -- copyreg
# pickle로 저장한 객체를 불러올 때 객체를 생성하는 함수를 실행하게 해주는 모듈 

import pickle

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Student('이다빈', 30)

with open('student_dabin.p', 'wb') as f:
    pickle.dump(a, f)

with open('student_dabin.p', 'rb') as f:
    student = pickle.load(f)

print(student.name)


import copyreg
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def pickle_student(student):
    kwargs = student.__dict__
    return unpickle_student, (kwargs, )

def unpickle_student(kwargs):
    return Student(**kwargs)

copyreg.pickle(Student, pickle_student)

a = Student('이다빈', 30)
with open('student_dabin_copyreg.p','wb') as f:
    pickle.dump(a, f)

import pickle
import copyreg


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dummy = 'dummy'  # dummy 속성을 새로 추가!


def pickle_student(student):
    kwargs = student.__dict__
    return unpickle_student, (kwargs, )


def unpickle_student(kwargs):
    return Student(**kwargs)


copyreg.pickle(Student, pickle_student)

with open('student_dabin_copyreg.p', 'rb') as f:
    student = pickle.load(f)  # unpickle_student() 함수를 호출한다.

print(student.dummy)  # 오류가 발생하지 않고 'dummy' 가 출력된다.



# 046_딕셔너리를 파일로 저장하려면? -- shelve 
# 딕셔너리를 파일로 저장할 때 사용하는 모듈로, 키에 해당하는 값을 저장할 수 있다.

import shelve

def save(key, value):
    with shelve.open('shelve.dat') as d:
        d[key] = value

def get(key):
    with shelve.open('shelve.dat') as d:
        return d[key]

save('number', [1, 2, 3, 4, 5])
print(get('number')) 

# pickle과 shelve의 차이 
# shelve는 pickle을 이용하여 작성된 모듈로, pickle의 하위개념이라 할 수 있다. 
# pickle은 파이썬의 모든 객체를 처리할 수 있지만, shelve는 딕셔너리만 처리하는 모듈이다. 


# 047_블로그 데이터를 저장하려면 ? -- sqlite3
# SQLite 데이터 베이스를 사용하는데 필요한 인터페이스 모듈

import sqlite3
conn = sqlite3.connect('blog.db')

c = conn.cursor()   # 커서 생성
# c.execute('''CREATE TABLE blog(id integer PRIMARY KEY, subject text, content text, date text)''')
# 테이블을 생성하려면 CREATE TABLE 테이블명 (...)과 같은 쿼리분을 실행해야한다. 

c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그', '첫 번째 블로그 입니다.', '20190827')")
c.execute("INSERT INTO blog VALUES (2, '두 번째 블로그', '두 번째 블로그입니다.', '20190827')")

c.execute('SELECT * FROM blog')
all = c.fetchall()  # fetchall()은 한 번 수행하면 끝이다. 다시 수행하면 같은 결과가 반환되는 것이 아니라 빈 리스트를 출력한다. 
print(all)


# 데이터 수정
c.execute("UPDATE blog SET subject = '최초의 블로그' WHERE id = 1")

c.execute('SELECT * FROM blog WHERE id = 1')
one = c.fetchone()
print(one)

# 데이터 삭제
c.execute('DELETE FROM blog WHERE id=5')

# 데이터 저장과 취소 
conn.commit()              # 데이터 저장을 위한 마지막 결정 서명 
conn.rollback()            # 이전 상태로 되돌리기

# 데이터 베이스 접속 종료 
conn.close()               # 단, close()는 자동으로 commit() 수행하지 않기 때문에 커밋 없이 close()를 하면 변경된 내용이 모두 사라진다는 점 주의. 



# 최종

import sqlite3
import time

def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()
        return rv
    return wrapper

@with_cursor
def get_blog_list(c):
    c.execute("SELECT * FROM blog")
    return c.fetchall()

@with_cursor
def add_blog(c, subject, content):
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)",
              (subject, content, time.strftime('%Y%m%d')))

@with_cursor
def read_blog(c, _id):
    c,execute("SELECT * FROM blog WHERE id=?", (_id))
    return c.fetchone()

@with_cursor
def modify_blog(c, _id, subject, content):
    c,execute("UPDATE blog SET subject =?, content =? WHERE id =?",
              (subject, content, _id))

@with_cursor
def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,))


