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
