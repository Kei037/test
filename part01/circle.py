"""
1. 파일명: circle.py
2. 개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area()함수
3. 작성자: 홍길동
4. 작성일: 2022-08-25
"""
# 삼중 큰 따옴표(""")는 여러 줄의 주석을 만들때 사용

# math 모듈 포함 : #은 한 줄 주석을 사용
import math

# get_area() 함수 정의
def get_area(radius): # 파이썬은 표기법으로 카멜법 보다는 언더바법을 선호.
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2)
    return area

# 1) 클래스안에 있는 메서드와 다르게 독립적으로 함수를 사용할 수 있음
# 2) 표기법은 언더바법을 사용
# 3) 데이터타입이 없음

radius = 1.5
# get_area() 함수 호출 결과를 area 변수에 저장
area_result = get_area(radius)
print(area_result)
print(get_area.__doc__) # get_area의 Docstring 확인
print()

"""
변수 variable : 어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장소

변수명 생성 규칙
1. 영문, 한글, 숫자, 언더바(_)로 구성
2. 특수문자는 사용 안됨
3. 대소문자는 구분이 됨 예) number와 Number는 다른 변수로 취급
4. 변수명의 첫 글자는 숫자를 사용할 수 없음 my2020 (o) / 2002my (x)
5. 키워드(list, dict, if, for, and등)은 사용 할 수 없음

권장하는 변수명
1. 가급적 영문 소문자로 작성
2. 한글은 사용하지 않고 영어 변수명 사용
3. 변수명으로 저장된 데이터 유추가 가능하도록
4. 클래스 이름을 제외하고는 첫 글자는 소문자
5. 변수명으로 저장된 데이터 유추가 가능하도록
예) a = 25, age = 26
"""

name = 'Alice' # single line 문자열 저장
age = 25 # 정수를 저장
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호'''  # multiple line 문자열 저장
boyfriend = None  # 아무 값도 저장하지 않음
height = 168.5  # 실수를 저장

age = 'Alice'  # 값을 변경 (변수선언과 수정이 구분이 안됨)

print(name)
print(age)
print(address)
print(boyfriend)
print(height)
print()

"""
파이선의 기본 데이터 타입 4가지 : 정수, 실수, 불, 문자열
파이썬의 컬렉션 데이터 타입 4가지 : list, tuple, set, dict
"""

# 정수 int
# int() 함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환할 수 있음
print(int(1.9))  # 1 / 1.9의 소수점 (.9) 이하를 제거하여 정수 1로 변환
print(int(True))  # 1 / True는 1로 변환
print(int(False))  # 1 / False 는 0으로 변환
print(int('100'))  # 100 / 문자열 '100'을 정수 100으로 변환
print(type(199))  # <class 'int'>

# 10진수를 2진수, 8진수, 16진수로 변환하는 방법
print()
n = 95
print(type(n))  # <class 'int'>
print()

# 실수 float
# 소수점이 있는 숫자를 실수 (floating point number) 라고 함

#float() 함수를 이용하면 다른 자료형의 값을 실수형 데이터로 변환 할수 있음
print(float(1))  # 1.0 / 정수 1을 실수 1.0으로 변환
print(float(True))  # 1.0 / True는 1.0으로 변환
print(float(False))  # 1.0 / False 는 0.0으로 변환
print(float('3.14'))  # 3.14 / 문자열 '3.14'를 실수 3.14로 변환
print(float('100'))  # 100.0 / 문자열 '100'을 실수 100.0으로 변환
print(type(3.14))  # <class 'float'>

# 실수의 연산은 부정확
print(0.1 + 0.2)

# 논리 bool
# 논리 자료형. 참과 거짓을 의미하는 True와 False 값을 가질수 있음
# True 나 False 모두 첫 글자는 반드시 대문자로 작성

# 파이썬에는 False는 값이 없는 모든 경우를 의미. 숫자0, 빈 문자열'', 빈 리스트[] 등은 모두 False로 인식
print(bool(0)) # False
print(bool('')) # False
print(bool([])) # False
print(type(True)) # <class 'bool'>

print(3 > 4)
print(3 < 4)
print()


# 문자열 str
# 문자열 자료형. 기본적으로 따음표로 묶어서 데이터를 표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따음표(')와 큰 따음표(")를 모두 사용할 수 있음
# 각 따옴표율 3개씩 사용하는 삼중 따옴표(''' ''', """ """)도 사용할 수 있음
# single line : 한 줄의 문자열 : 작은 따음표(')와 큰 따옴표(")
# multiple line : 여러 줄의 문자열 : 삼중 따옴표(''' ''', """ """)

# 문자열 변환
# str() 함수를 사용하면 다른 자료형의 값을 문자열 데이터로 변환 할 수 있음
print(str(100)) # 100'/ 정수 100을 문자열 '180'으로 변환
print(str(True)) #'True' / 논리 True를 문자열 'True'로 변환
print(str(False)) #'False'/ 논리 False를 문자열 'False'로 변환
print(type(str(3.14))) # ccLass stn'> 3.14' / 실수 3.14를 문자열 3.14'로 변환
print()

# 문자열 인덱싱 indexing
# 0번 부터 시작
s = 'hello'
print(s[1]) # e
# 마이너스(-) 인덱스는 문자열 뒤에서 부터 부여, 마지막 인덱스는 -1이 됨
print(s[1] == s[-4]) # True

# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
# s[start:stop:step]
# start : 시작 인덱스를 지정. 생략하면 처음부터 추출
# stop : 종료 인덱스를 지정, 생략하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화

print()
s = 'banana'
print(s[0:3]) # ban / 종료 인덱스는 포함하지 않음
print(s[0:6:2]) # bnn
print(s[:6:2]) # bnn
print(s[::]) # banana
print(s[2::2]) # nn

student = '31025'
grade_no = student[0]
class_no = student[1:3]
stu_no = student[3:]  # stu_np[-2:]도 가능
print(grade_no, '학년', class_no, '반', stu_no, '번')
# 3 학년 10 반 25 번

# 리스트 list
# 여러 값을 저장할 때 가장 많이 사용하는 자료형
# 저장하고자 하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장

# 대괄호([]) 또는 list() 함수를 이용해서 생성
# 정수, 실수, 문자열을 각 1개씩 저장하고 있는 리스트 생성
li = [100, 3.14, 'hello']
print(li) # [100, 3.14, 'hello']
print(type(li)) # <class 'list'>

print()
print(li[0]) # 100
print(li[1]) # 3.14
print(li[2]) # 'hello'

# 슬라이싱
print()
li = [10, 20, 30, 40]
print(li[0:3]) # [10, 20, 30]
print(li[:2]) # [10, 20]
print(li[::2]) # [10, 30]
print(li[-2::]) # [30, 40]

# 요소의 추가와 삭제
# 새로운 요소를 추가할때는 append()와 insert() apthemfmf tkdyd
# append() : 항상 마지막 요소로 추가
# insert() : 추가할 인덱스(위치 정보)를 저장
print()
scores = [50, 40, 30]
scores.append(100)  # 마지막 요소에 100을 추가
print(scores)  # [50, 40, 30, 100]
print(scores[1])  # 40
scores.insert(0, 90)  # 인덱스 0 에 90을 추가
print(scores)  # [90, 50, 40, 30, 100]
print(scores[1])  # 50



