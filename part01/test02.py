# 전체 차량번호에서 뒤에 숫자 4자리만 출력하는 프로그램을 구현하세요.
# 전체 차량번호는 '서울2가 1234', '10가 1234', '288가 1234'와 같이 다르지만, 모두 차량번호 4자리는 '1234'입니다.
# 실행 예)
# 서울2가 1234의 차량번호 4자리는 1234입니다.

car1 = '서울2가1234'
car2 = '10가1234'
car3 = '288가1234'

car_no1 = car1[-4:]
car_no2 = car2[-4:]
car_no3 = car3[-4:]
print(car1, '의 차량번호 4자리는', car_no1, '입니다.')
print(car2, '의 차량번호 4자리는', car_no2, '입니다.')
print(car3, '의 차량번호 4자리는', car_no3, '입니다.')

""" 연산자 """

# 산술 연산자
a = 7
b = 2
print(f'{a} + {b} = {a + b}') # 9 / + 덧셈
print(f'{a} - {b} = {a - b}') # 5 / - 뺄셈
print(f'{a} * {b} = {a * b}') # 14 / * 곱셈
print(f'{a} ** {b} = {a ** b}') # 49 / ** 거듭제곱
print(f'{a} / {b} = {a / b}') # 3.5 / / 나눗셈
print(f'{a} // {b} = {a // b}') # 3 / // 몫
print(f'{a} % {b} = {a % b}') # 1 / % 나머지
print()

# 대입 연산자
# a = b : b에 있는 값을 a라는 변수에 저장을 하라
a = 10

a, b = 10, 20  # 2개 이상의 변수에 저장. 튜플을 이용
print('a = %d, b = %d' % (a, b))  # 10, 20
print(f'a = {a}, b = {b}')

a, b = b, a  # 값을 교환
print('a = %d, b = %d' % (a, b))  # 20, 10
print()

# 복합 대입 연산자
# 연산을 먼저 진행하고, 그 결과를 변수에 저장
c = 10
c = c + 10
print(c)
c += 10
print(c)

c -= 10  # c = c -10
print(c)  # 20

c //= 10
print(c)

c *= 10
print(c)
print()

# 비교 연산자
# 결과 값은 True 와 False 둘 중 하나
a = 15
print(f'{a} > 10 : {a > 10}')  # True, a가 10보다 크다
print(f'{a} < 10 : {a < 10}')  # False. a가 10보다 작다
print(f'{a} >= 10 : {a >= 10}')  # True. a가 10보다 크거나 같다.
print(f'{a} <= 10 : {a <= 10}')  # False. a가 10보다 작거나 같다.
print(f'{a} == 10 : {a == 10}')  # False. a와 10보이 같다.
print(f'{a} != 10 : {a != 10}')  # True. a와 10이 다르다
print()

# 논리 연산자
# 결과 값은 True 와 False 둘 중 하나
# a 논리연산자 b의 형식. a, b 모두 불형
# a and b : a 와 b가 모두 참(True)dlaus True, 아니면 False
# a or b : a 와 b 중 하나라도 참(True)이면 True, 아니면 False
# not a: a 가 참(True)이면 False, a가 거짓(False)이면 True

a = 10
b = 0
print(f'{a} > 0 and {b} > 0 : {a > 0 and b > 0}')  # False / True and False
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}')  # True / True or False
print('not {} : {}'.format(a, not  a))  # False / 0 이 아니면 True
print('not {} : {}'.format(b, not  b))  # True / 0이면 False
print()

# 시퀀스 연산자 : 순서가 있는 시퀀스 (리스트, 튜플, range, 문자열 등) 에서 사용할 수 있는 연산자
# + : 연결하기
# * : 반복하기

tree = '#'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)
print('-' * 20)

# 삼항 조건 연산자
# 일반적인 삼항 조건 연산자 : 조건식 ? 참 : 거짓
# 파이썬 삼항 조건 연산자 : 참 if 조건식 else 거짓

a = 10
b = 20
result = (a - b) if (a >= b) else (b - a)  # 조건식 a >= b 은 False, b - a 실행
print(f'{a}과 {b}의 차이는 {result}입니다.')
print()

# 조건문

# 1. if문
# if 조건식 :
#     조건식의 결과가 True일 때 실행문

num = 15
if num > 0:
    print('양수')  # 조건식이 True라서 실행이 됨

# 들여쓰기 indentataion 규칙
# 1. 공백 space나 탭 tab을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관이 없음
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 함. 공백과 탭을 혼용하여
# 사용할 수 없고 들여쓰기 수준도 동일해야함
# 5. 주로 사용하는 들여쓰기는 공백 4개, 공백 2개, 탭 1개.

if num > 0: print('양수')  # 실행문이 하나면 한 줄 코드로 가능

# 2. if-else 문
# if 조건식 :
#   조건식의 결과가 True일 때 실행문
# else :
#   조건식의 결과가 False일 때 실행문

print()
num = -1
if num >= 0:
    print('양수')
else:
    print('음수')

# if-elif 문
# if 조건식1 :
#   조건식1의 결과가 True일 때 실행문
# elif 조건식2 :
#   조건식1의 결과가 False이고, 조건식2의 결과가 True일 때 실행문
# elif 조건식3 :
#   조건식1, 2의 결과가 False이고, 조건식3의 결과가 True일 때 실행문
# else :
#   조건식1, 2, 3의 결과가 False일 때 실행문

print()
important = 56

if important >= 100:
    print('상')
elif important >= 50:
    print('중')
else:
    print('하')


# while 문
# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용
# while 조건식 :
#   반복실행문

n = 1
while n <= 10:
    print(n)
    n += 1
print(n)

n = 100
while n >= 50:
    if n % 2 == 0:
        print(n)
    n -= 1

n = 100
while n >= 50:
    print(n)
    n -= 2

# 구구단 2단 부터 9단 까지 출럭
# 단 앞에 제목, 마지막에 구분선을 넣어 볼 것

dan = 2
while dan <= 9:
    n = 1
    print(f'{dan}단')
    while n <= 9:
        print(f'{dan} x {n} = {dan * n}')
        n += 1
    print('==========')
    dan += 1


# for 문
# 값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문
# 1) 특정 횟수 반복
# 2) 데이터 순회

# for 변수 in 반복개능객체 :
# 반복 실행문

for n in [2, 4, 6] :  # 반복될 때 마다 순서대로 전달
    print(n)

# 반복가능객체
# 1. 시퀀스 sequence 자료형 : 순서를 가지고 있는 자료형
# 문자열, 리스트, 튜플, range
# 2. 비시퀸스 non-sequence 자료형 : 순서를 가지고 있지 않은 자료형
# 세트, 딕셔너리

# 1. 문자열
# for 문자 in 문자열 :
#   반복실행문

for ch in 'hello':
    print(ch)

# 2. 리스트
# for 요소 in [리스트]:
#   반복문

li = ['가위', '바위', '보']
for i, v in enumerate(li): # i:index, v:요소의 값 value
    print(f'인덱스: {i} Value값: {v}')

# 리스트 내포
# 리스트 생성할 때 for문을 유용하게 사용할 수 있음
# 기본형식
# 리스트 = [표현식 for 변수 in 반복가능객체]
li = [n * 2 for n in [1, 2, 3]]
print(li)

# 조건에 맞는 데이터만 추출 가능
# 리스트 = [표현식 for 변수 in 반복가능객체 if 조건식]
li = [n * 2 for n in [1, 2, 3, 4, 5]]
print(li)

li = [n * 2 for n in [1, 2, 3, 4, 5] if n % 2 == 1] # 1, 3, 5 만 추출
print(li)

li = []
for n in [1, 2, 3, 4, 5]:
    if n % 2 == 1:
        li.append(n * 2)
print(li)

# 3. 튜플
# 기본형식
# for 요소 in (튜플):
#   반복실행문

four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
for season in four_seasons:
    print(season)

# 4. range() 함수
# '정수 범위'를 만들어 낼 때 유용한 함수. 일정 횟수 반복시에 많이 사용
# 기본 구조
# range(초깃값, 종료값, 증감값)

# 특징
# 1. 초깃값부터 종료값 전까지 숫자(n)들의 컬렉션을 만듬 (초깃값 <= n < 종료값)
# 2. 초깃값을 생략하면 0부터 시작
# 3. 종료값은 생략할 수 없음
# 4. 증감값을 생략하면 1씩 증가

# 예
# range(5) : 0, 1, 2, 3, 4
# range(1, 11) : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# range(1, 10, 2) : 1, 3, 5, 7, 9

print()
print(list(range(1, 6)))
print(tuple(range(1, 6)))

print()
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(n)

# 아래와 같이 변경 가능
for n in range(1, 11):
    print(n)

# range() 함수를 이용해 생성한 값을 사용하지 않는 경우
for n in range(10):
    print('hello')

dan = 2
for dan in range(2, 10):
    print(f'{dan}단')
    for n in range(1, 10):
        print(f'{dan} x {n} = {dan * n}')
    print('==========')


# 세트 set
# 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음
# for 요소 in {세트}:
#   반복실행문

for item in {'가위', '바위', '보'}:
    print(item)


# 딕셔너리
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용을 함
# 키만 출력
print()
person = {'name': '에밀리', 'age': 20}
for item in person:
    print(item)

# value 출력
for key, value in person.items():
    print(f'{key} : {value}')

for key in person:
    print(person[key])

for key in person:  # get() 메소드를 이용해서 해당 key에 해당하는 value를 가져옴
    print(person.get(key))


# 영어 사전을 딕셔너리 자료형으로 구현하고
# 영어 사전에 등록된 모든 단어와 그 단어의 의미를 출력
eng_dict = {
    'sun': '태양',
    'moon': '달',
    'star': '별',
    'space': '우주'
}
for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict.get(word)}')
    print(f'{word}의 뜻: {eng_dict[word]}')


# break
n = 1
while True:
    print(n)
    if n == 10:
        break
    n += 1
print(n)


# continue 문
total = 0
for a in range(1, 101):
    if a % 3 == 0:
        continue
    total += a
print(total)

# 내장 함수
# 파이썬 인터프리터에는 항상 사용할 수 있는 많음 함수가 내장되어 있으며,
# 이를 내장 함수 built-in function 이라고 함
# 외부에 따로 저장해 둔 모듈에서 불러오는 것이 아니기 때문에 import가 필요없음

# 1. 문자열 내장 함수
# chr() : 특정 문자의 유니코드 값을 전달하면 해당 유니코드 값을 가진 문자를 반환하는 함수
# 유니코드의 유효범위 0 ~ 1,114,111 / 아스키코드의 유효 범위 0 ~ 127
print(chr(48))  # 0
print(chr(49))  # 1
print(chr(65))  # A
print(chr(66))  # B
print(chr(97))  # a
print(chr(98))  # b

# ord() : 문자를 전달하면 해당 문자의 유니코드 값을 반환
print()
print(ord('A'))  # 65
print(ord('한'))  # 54620

# eval() : 실행하고자 하는 표현식(expression) 을 문자열로 전달하면 표현식의 결과값을 반환
print()
print(eval('100 + 200'))  # 300
a = 10
print(eval('a * 5'))  # 50
print(eval('min(1, 2, 3)'))  # 1

# format() : 전달받은 인수와 포멧 코드에 따라 형식을 갖춘 문자열을 반환
# 포켓 코드를 전달하지 않으면 str()을 호출한 것과 같음
print()
print(format(10000))  # 10000 / str(10000)과 같음
print(format(10000, '-'))  # 10_000 / 천단위 구분 기호로 밑줄(_)을 사용
print(format(10000, ','))  # 10,000 / 천단위 구분 기호로 밑줄(,)을 사용

# 2. 숫자 내장 함수
# abs() : 전달된 인수 (정수 혹은 실수)의 절대값을 반환
print(abs(10))  # 10
print(abs(-10))  # 10

# divmod() : 전달된 두 인수를 나누어 몫과 나머지를 한 쌍의 결과로 반환. 몫과 나머지는 하나의 튜플(tuple)로 반환
print(divmod(10, 3))  # (3, 1)
print(type(divmod(10, 3)))  # <class 'tuple'>

# float() : 전달된 인수(숫자 또는 문자열)를 실수로 만들어 반환. 전달된 인수가 없는 경우에는 0.0을 반환

# int() : 전달된 인수(숫자 또는 문자열)를 정수로 만들어 반환. 전달된 인수가 없는 경우에는 0을 반환

# max() : 전달된 인수 중 가장 큰 값을 반환
print()
print(max(1, 10))
li = [5, 3, 4, 2, 1]
print(max(li))

# min() : 전달된 인수 중 가장 작은 값을 반환
print()
print(min(1, 10))
li = [5, 3, 4, 2, 1]
print(min(li))

# pow() : 전달된 두 인수의 거듭제곱을 반환. 연산자 중에서 거듭 제곱 연산자 ** 와 같음
print()
print(pow(10, 2))  # 100
print(pow(10, 3))  # 1000
print(pow(10, -2))  # 0.01
print(pow(10, -3))  # 0.001

# round() : 전달된 인수를 이용해 반올림한 값을 반환
# 전달된 인수가 하나이면 정수로 반올림함 값을 반환하고, 전달된 인수가 2개이면 두 번째로 전달한 인수만큼 소수점을 남겨둠
print()
print(round(1.5))  # 2
print(round(1.4))  # 1
print(round(1.55, 1))  # 1.6
print(round(2.675, 2))  # 2.67 -> 부동 소수점 에러로 인해 2.68이 아니라 2.67이 반환
print(round(2.6755, 2))  # 2.68

# sum() : 전달된 리스트나 튜플과 같은 반복가능객체의 합계를 반환
# 숫자가 아닌 값을 전달하면 에러
print()
list1 = [1, 2, 3, 4, 5]
print(sum(list1))

list2 = ['h', 'e', 'l', 'l', 'o']
# print(sum(list2))

# 3. 시퀀스 내장 함수

# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 tuple 형태로 함게 추출
# for item in enumerate([리스트]) :
#   반복실행문

for item in enumerate(['가위', '바위', '보']) :
    print(item)
# (0, '가위')
# (1, '바위')
# (2, '보')

for idx, element in enumerate(['가위', '바위', '보']) :
    print(idx, ' / ', element)
# 0  /  가위
# 1  /  바위
# 2  /  보

# range() : 전달된 인수값에 따라 시퀀스 자료형의 데이터를 생성
# 1) range(stop) / 0부터 stop 사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는 0 <= n < stop
# 2) range(start, stop) / start부터 stop 사이의 모든 정수가 생성. 생성되는 정수를 n이라고 하면 n의 범위는 start <= n < stop
# 3) range(start, stop, step) / start부터 stop 사이의 정수 중에서 step만큼의 차이를 가지고 있는 정수가 생성.

print()
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 5))) # [0, 5, 10, 15, 20, 25]
print(list(range(0, 10, 3))) # [0, 3, 6, 9]
print(list(range(0, -10, -1))) # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(range(0))) # []
print(list(range(1, 0))) # []

# len() : 함수에 전달된 객체의 길이(항목 수)를 반환
print()
li = ['a', 'b', 'c', 'd']
print(len(li))

d = {'a': 'apple', 'b': 'banana'}
print(len(d))

print(len(range(10)))
print(len(range(1, 10)))

# range() 함수와 리스트의 길이를 구하는 len() 함수를 함게 사용하면 리스트의 인덱스를 생성가능
seasons = ['봄', '여름', '가을', '겨울']
seasons_eng = ['spring', 'summer', 'fall', 'winter']
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')



# sorted() : 전달된 반복가능객체의 오름차순 정렬 결과를 반환
# reverse=True 옵션을 추가할 경우 내림차순 정렬 결과를 반환
print()
my_list2 = ['b', 'c', 'a', 'd']
print(sorted(my_list2))  # ['a', 'b', 'c', 'd']
print(sorted(my_list2, reverse=True))  # ['d', 'c', 'b', 'a']

my_list = [6, 3, 1, 2, 5, 4]
print(sorted(my_list))  # [1, 2, 3, 4, 5, 6]
print(sorted(my_list, reverse=False))  # [1, 2, 3, 4, 5, 6]
print(sorted(my_list, reverse=True))  # [6, 5, 4, 3, 2, 1]

print()
print(sorted(my_list))  # [1, 2, 3, 4, 5, 6]
print(my_list)  # [6, 3, 1, 2, 5, 4] / 실제로 정렬이 된건 아님

print()
my_list = sorted(my_list)  # 오름차순 정렬 결과를 덮어쓰기
print(my_list)  # [1, 2, 3, 4, 5, 6]

# zip() : 전달된 여러 개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
# 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체 기준으로 동작
print()
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)
# ('james', 60)
# ('emily', 70)
# ('amanda', 80)

# 튜플은 언패킹이 가능하므로 다음과 같은 모습으로 구성 가능
for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}입니다.')
# james의 점수는 60입니다.
# emily의 점수는 70입니다.
# amanda의 점수는 80입니다.

print()
for idx, name in enumerate(names):
    print(f'{name}의 점수는 {scores[idx]}입니다.')

print()
for idx in range(len(names)):
    print(f'{names[idx]}의 점수는 {scores[idx]}입니다.')


