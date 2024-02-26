# 하나만 출력합니다!!
print('# 하나만 출력합니다.')
print('Hello Python Programming...!')
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "홍길동입니다!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")


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

# pop() : 인덱스를 전달하지 않으면 마지막 요소를 삭제
# 인덱스를 전달하면 전달된 인덱스의 요소 삭제
scores.pop()  # 마지막 요소를 제거
print(scores)  # [90, 50, 40, 30]
scores.pop(0)  # 0번 인덱스 요소를 제거
print(scores)  # [50, 40, 30]

# 튜플 tuple
# 저장된 값을 변경할 수 없는 리스트
# 리스트와 마찬가지로 각 요소를 구분하기 위한 인덱스가 부여되고 슬라이싱도 지원
# 이미 저장된 값 이외에는 추가, 수정, 삭제가 불가능

# 튜플은 소괄호(()) 나 tuple()함수를 이용해서 생성
# 값들을 콤마(,)로 분리하여 전달하면 자동으로 튜플이 생성

t1 = (1, 2, 3)
print(t1) # (1, 2, 3)

# 괄호 없이 사용 가능
t2 = 1, 2, 3
print(t2)

def sample():
    return 1, 2
print(sample())

t3 = tuple([100, 3.14, 'hello'])
print(t3)  # (100, 3.14, 'hello')

# 값을 1개만 보관하는 튜플을 생성할 경우에는 값과 콤마(,)를 반드시 함께 작성
t4 = (100)
print(t4)  # 100 / 값으로 인식
print(type(t4)) # <class 'int'>

t5 = (100,)
print(t5)  # (100,) / 튜플로 인식
print(type(t5))  # <class 'tuple'>

# 값을 swap 교환
a = 10
b = 20
print(a, b)  # 10 20
a, b = b, a  # (a, b) = (b, a)
print(b, a)  # 20 10

a, b = 100, 200
print(a)
print(b)
print()

# 딕셔너리 dict
# 사전처럼 어떤 단어와 그 단어의 의미로 구성
# '키 key' 와 '값 value' 를 '단어'와 '단어의 의미'처럼 사용
# 딕셔너리는 인덱스가 존재하지 않는 대신 키를 인덱스처럼 사용함
# 키 값을 알면 저장된 값을 확인할 수 있는 구조

d = {'a': 'apple', 'b': 'banana'}  # {key:value, key:value}
print(d)  # {'a': 'apple', 'b': 'banana'}
print(type(d))  # <class 'dict'>
print(d['a'])  # apple / 인덱스 대신 key를 사용하면 value가 반환
print(d['b'])  # banana

# 키값의 자료형이 문자열(str) 이라면 dict() 함수를 이용해서 생성가능
d = dict(a='apple', b='banana')
print(d) # {'a': 'apple', 'b': 'banana'}

# 딕셔너리 요소의 추가와 삭제
#새로운 키와 값을 조합해서 작성
print()
dic = {'apple': '사과'}
dic['watermelon'] = '멜론'
print(dic)  # {'apple': '사과', 'watermelon': '멜론'}

# 존재하는 키값을 이용해서 정의하면, value 수정으로 인식
dic['watermelon'] = '수박'
print(dic)  # {'apple': '사과', 'watermelon': '수박'}

# setdefault() 메소드를 이용한 추가
me = {'name': 'james'}
me.setdefault('age', 20)
print(me)  # {'name': 'james', 'age': 20}
me.setdefault('age', 30)  # 동일한 키가 있는 경우에 무시
print(me)  # {'name': 'james', 'age': 20}

# update() 메소드의 경우 존재하는 키값이면 수정
me.update(age=25)
print(me)  # {'name': 'james', 'age': 25}

# update() 메소드의 경우 존재하지 않는 키값이면 추가
me.update(address='seoul')
print(me)  # {'name': 'james', 'age': 25, 'address': 'seoul'}

# pop() 메소드에 키값을 전달하면 해당 키값의 데이터가 삭제
me.pop('address')
print(me)  # {'name': 'james', 'age': 25}

# get() 메소드에 전달한 key에 해당하는 value를 반환
print(me.get('name'))  # james
print()

# mutable 과 immutable
# mutalbe : 생성된 후에도 변경이 가능한 자료형 : list, set, dict
# immutable : 생성된 후에는 변경이 불가능한 자료형 : int, float, str, tuple

# mutable
# 할당받는 메모리에 저장된 값을 다른 값으로 바꿀 수 있음
# id() : 객체의 고유값 반환. 메모리 주소를 구별하기 위한 용도로 사용
me = [1, 2, 3]
print(id(me))  # 4384655744
me.append(4)
print(id(me))  # 4384655744 / 할당된 메모리 주소는 변경이 되지 않음

# immutable
# 한 번 생성하면 최초로 저장된 값을 다른 값으로 바꿀 수 없음
obj = 10
print(id(obj))  # 4314382864
obj = obj + 1
print(obj)  # 11
print(id(obj))  # 4314382896 / 할당된 메모리 주소가 변경이 됨
# 메모리에 저장된 데이터를 수정하는 것이 아니라, 새로 할당을 받아서 데이터를 저장

# print() 함수
# end : value 출력 후 출력할 문자
# end 속성을 사용하지 않고 print()함수를 사용하면 출력 후 자동으로 줄 바꿈이 진행
# sep : 출력할 value의 구분자
# sep 속성을 사용하지 않고 print()함수를 사용하면 출력 대상은 공백으로 구분
# file : 출력 방향 지정
# file 속성을 사용하지 않고 print()함수를 사용하면 출력 대상은 모니터에 출력
print()
print('재미있는', '파이썬')  # sep 값을 지정하지 않으면 공백이 들어감
print('재미있는', '파이썬', sep=' ')  # 재미있는 파이썬/ 콤마(,)로 구분된 출력 대상은 공백으로 구분
print('Python', 'Java', 'C', sep=':')  # Python:Java:C / sep 속성으로 구분

print()
print('영화 타이타닉', end='\n')  # 지정하지 않았을때 기본은 \n
print('평점', end=':')
print('5점')  # 평점:5점 / value 출력 후 end 속성 출력. 줄 바꿈이 되지 않음

fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)  # file 속성으로 대상 출력. 파일 출력
fos.close()
print()
# % 연산자
name = 'Kai'
print('내 이름은 %s입니다.' % name) # 내 이름은 Kai입니다. / %s : string
print('내 이름은 ', name, '입니다.', sep='')
print('내 이름은 ' + name + '입니다.')

height = 120.5
print('내 키는 %fcm입니다.' % height)  # 내 키는 120.500000cm입니다. / %f : float

weight = 23.55
print('내 몸무게는 %.1fkg입니다.' % weight)  # 내 몸무게는 23.6kg입니다.

year, month, day = 2014, 8, 25
print('내 생일은 %d년 %d월 %d일 입니다.' % (year, month, day))
# 내 생일은 2014년 8월 25일 입니다. / %d : decimal (십진법)
print()

# format 메소드
# format() 메소드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식

zipcode = '06236'
print('우편번호 : {}'.format(zipcode)) # format() 메소드를 이용해 출력

zipcode_str = '우편번호 : {}'.format(zipcode)
print(zipcode_str)

address = '''서울특별시 강남구
테헤안로 146'''  # multi line

print('주소 : {addr}'.format(addr=address))  # format() 메소드의 변수 이용
print('주소 : ' + address)

# f-strings (formatted strings) : 파이썬 3.6 이후 버젼에서 사용 가능
who = 'you'
how = 'happy'
print(f'{who} make me {how}')  # you make me happy / 문자열에 f 또는 F라는 접두어 prefix를 붙임

age = 25
print(f'내년엔 {age + 1}살이 됩니다.')  # 내년엔 26살이 됩니다.
print()
# 표준입력
# input() 함수 : 표준 입력 장치(키보드)로 부터 입력받을 때 사용
# n = input('')
# print(n)

n = input('정수를 입력하세요.') # 100
print(n) # '100'
print(type(n))  # <class 'str'> / input() 함수는 모든 입력을 '문자열 str'로 저장

n = int(input('정수를 입력하세요.'))  # 정수로 변환
# n = input('정수를 입력하세요')  # 100
# n = int(n)
print(type(n))  # <class 'int'>

name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')

print('입력된 이름은 {}입니다.'.format(name))  # format 메서드를 이용한 출력
print('입력된 나이는 {}살 입니다.'.format(age))

print(f'입력된 이름은 {name}입니다.')  # f-strings 메서드를 이용한 출력
print(f'입력된 나이는 {age}살 입니다.')

first = float(input('첫 번째 실수를 입력하세요 >>> '))
second = float(input('두 번째 실수를 입력하세요 >>> '))

print(f'{first}와 {second}의 합은 {first + second}입니다.')

month = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# 1. 리스트 사용
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(f'{month}는 {days[month - 1]}일까지 있습니다.')

# 2. 딕셔너리 사용
days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31, 12: 31}
print(f'{month}는 {days_dict[month]}일까지 있습니다.')



