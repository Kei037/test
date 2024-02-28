# 메소드
# 메소드 method란 특정 객체 object가 가지고 있는 함수 function을 의미
# 함수는 독립적으로 호출할 수 있지만, 메소드는 특정 객체를 통해서만 호출할 수 있음

# 함수와 다르게 메소드는 특정 객체 소속이어서, 메소드를 호출할려면
# 특정 객체를 통해서만 호출 가능

# 1. 문자열 메소드
# 문자열 str을 처리하기 위해 많은 메소드를 제공

# 1) format()
# 정렬 옵션
# < : 지정된 공간 내에서 왼쪽 정렬
# > : 지정된 공간 내에서 오른쪽 정렬
# ^ : 지정된 공간 내에서 가운데 정렬

# 10d는 10자리의 필드 폭을 의미
print("10자리 폭 왼 쪽 정렬 '{:<10d}'".format(123))  # 10자리 폭 왼 쪽 정렬 '123       '
print("10자리 폭 오른 쪽 정렬 '{:>10d}'".format(123))  # 10자리 폭 오른 쪽 정렬 '       123'
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))  # 10자리 폭 가운데 정렬 '   123    '
print()
# 채움문자를 지정하면 공백 대신 채움문자가 빈자리를 채움
print("10자리 폭 왼 쪽 정렬 채움문자 '{:*<10d}'".format(123))  # 10자리 폭 왼 쪽 정렬 채움문자 '123*******'
print("10자리 폭 오른 쪽 정렬 채움문자 '{:*>10d}'".format(123))  # 10자리 폭 오른 쪽 정렬 채움문자 '*******123'
print("10자리 폭 가운데 쪽 정렬 채움문자 '{:*^10d}'".format(123))  # 10자리 폭 가운데 쪽 정렬 채움문자 '***123****'
print()


# 2) count()
# 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드

s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))

# 인덱스를 지정해서 범위를 지정할 수 있음
s = 'best of best'
print(s.count('best', 5))  # 1 / 인덱스 5번 부터 검색

# 마이너스 인덱스를 사용할 수 있음
s = 'best of best'
print(s.count('best', -7))  # 1 / o  부터 검색
print()


# 3) find()
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# 찾고자 하는 문자열이 있으면 그 문자열이 처음으로 나온 위치 즉 인덱스 index 를 반환

s = 'apple'
print(s.find('p'))  # 1

# 찾는 문자열이 없는 경우 -1 반환
s = 'apple'
print(s.find('z'))  # -1

if s.find('z') == -1:
    print(s)

# 인덱스를 이용해서 검색할 범위를 지정 가능
# 시작할 인덱스를 지정하지 않는 경우에는 문자열의 처음부터 찾고, 시작할 인덱스를 지정하는 경우 지정된 인덱스부터 찾음
s = 'best of best'
print(s.find('best'))  # 0
print(s.find('best', 5))  # 8

# find() 메소드와 찾는 방향이 다른 rfind() 메소드
# right와 find 를 합친 이름으로 오른쪽부터 찾음
s = 'best of best'
print(s.rfind('best'))  # 8
print()


# 4) index()
# find() 메소드와 같은 역할을 수행하며 사용방법도 동일. 두 메소드의 차이점은 문자열이 없을 때 발생
# find() 메소드는 찾는 문자열이 없는 경우 -1을 반환, index() 메소드는 오류 발생

s = 'apple'
print(s.index('p'))  # 1
print()

# 5) 대소문자 변환 메소드
# upper : 모두 대문자로 변환한 결과를 반환
# lower : 모두 소문자로 변환한 결과를 반환
# capitalize : 첫 글자는 대문자로 변환하고 나머지는 소문자로 변환한 결과를 반환

s = 'BEST of best'
print(s.upper())  # BEST OF BEST
print(s.lower())  # best of best
print(s.capitalize())  # Best of best

# 6) join()
# 인수로 전달한 반복가능객체(문자열, 리스트 등)의 각 요소 사이에
# 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 반환
print()

print('-'.join('python'))  # p-y-t-h-o-n

print('+'.join(['a', 'b', 'c', 'd', 'e']))  # a+b+c+d+e

# 포함하는 문자 없이 단순하게 리스트의 요소들을 연결하고자 한다면 빈 문자열 사용
print(' '.join(['x', 'y', 'z']))  # x y z
a = {'a': 'apple', 'b': 'banana'}
print(''.join(a))  # ab / 딕셔너리의 경우 key를 연결
print()


# 7) split()
# 하나의 문자열을 여러 개의 문자열로 분리해서 저장한 리스트를 반환

s = 'Life is too short'
s2 = s.split()  # split() 메소드에 아무 인수도 전달하지 않으면 공백문자를 기준으로 각 문자열이 분리
print(s2)  # ['Life', 'is', 'too', 'short']

s = '010-1234-5678'
s2 = s.split('-')  # 공백대신 특정 문자열을 기준으로 분리하는 방법
print(s2)  # ['010', '1234', '5678']
print()


# 8) replace()
# 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환

s = 'Life is too short'
s2 = s.replace('short', 'long')
print(s2)

# 특정 문자열을 제거하기 위한 용도로 사용
s = '010-1234-5678'
s2 = s.replace('-', '')
print(s2)
print()


# 9) 불필요한 문자열 제거 메소드
# 문자열 양끝에 있는 불필요한 문자열을 제거 (공백제거)
# strip() : 양쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# lstrip() : 왼쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환
# rstrip() : 오른쪽 끝에 있는 불필요한 문자열을 제거한 결과를 반환

s = '     apple'
print(len(s))

s2 = s.lstrip()
print(s2)
print(len(s2))
print()


# 2. 리스트 메소드
# 1) append()
# 리스트의 끝에 인수로 전달된 데이터를 추가
my_list = ['apple', 'banana']
my_list.append('cherry')
print(my_list)  # ['apple', 'banana', 'cherry']
print()

# 2) extend()
# 리스트에 다른 리스트나 튜플과 같은 반복가능객체를 추가하여 기존 리스트를 확장
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])
print(my_list)  # ['apple', 'banana', 'cherry', 'mango']

my_list = ['apple', 'banana']
my_list += ['cherry', 'mango']
print(my_list)  # ['apple', 'banana', 'cherry', 'mango']
print()

# 3) insert()
my_list = ['apple', 'banana']
my_list.insert(0, 'cherry')
print(my_list)  # ['cherry', 'apple', 'banana']
print()

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제
my_list = ['apple', 'banana']
my_list.clear()
print(my_list)  # []

my_list = ['apple', 'banana']
my_list = []
print(my_list)  # []
print()

# 5) pop()
# 리스트의 마지막 요소가 반환되면서 삭제
my_list = ['apple', 'banana']
item = my_list.pop()
print(item)  # banana
print(my_list)  # ['apple']

# 인덱스 값을 인수로 전달하면 해당 인덱스 값이 삭제
my_list = ['apple', 'banana']
item = my_list.pop(0)
print(item)  # apple
print(my_list)  # ['banana']
print()

# 6) remove()
# 인수로 전달된 값과 동일한 요소를 찾아서 제거. 동일한 요소가 여러 개인 경우에는 첫 번째 요소가 제가
my_list = ['apple', 'banana', 'cherry', 'mango']
my_list.remove('cherry')
print(my_list)  # ['apple', 'banana', 'mango']

# 중복된 값이 있는 경우 제일 앞에 있는 것만 삭제
my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
my_list.remove('cherry')
print(my_list)  # ['apple', 'banana', 'mango', 'cherry']

# 특정 값을 전부 삭제를 원할 경우 반복문 사용
my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
for idx in range(my_list.count('cherry')):
    my_list.remove('cherry')
print(my_list)  # ['apple', 'banana', 'mango']
print()


# 사용자 정의 함수
# 사용자가 직접 만든 함수
# 1) 어떤 입력을 받아 2) 특정 연산을 수행한 뒤 3) 결과를 반환하는 기능

# 함수 용어 정리
# 1. 함수 정의 : 사용자 함수를 새로 만드는 것을 의미
# 2. 인수 : 사용자 함수에 전달할 입력(input)을 의미. argument
# 3. 매개변수 : 인수를 받아서 저장하는 변수를 의미. parameter
# 4. 반환값 : 사용자 함수의 출력(output)을 의미. return
# 5. 함수 호출 : 만들어진 사용자 함수를 실제로 사용하는 것을 의미

# 함수 정의
# 함수를 만드는 것을 의미. def 키워드를 이용

# def 함수이름(매개변수) :
#   본문
#   return 반환값
# 함수이름을 개발자가 마음대로 결정
# 매개변수, 반환값을 필수 사항이 아님

# 함수 호출
# 변수 = 함수이름(인수)
# 함수의 호출 결과를 저장할 변수를 생략가능

# 4 가지 함수 호출 형태
# 1) 인수: X, 반환값: X
# 함수이름()
# 2) 인수: O, 반환값: X
# 함수이름(인수)
# 3) 인수: X, 반환값: O
# 변수 = 함수이름()
# 4) 인수: O, 반환값: O
# 변수 = 함수이름(인수)

# welcome() 함수 정의
def welcome():
    print("Hello Python")
    print("Nice to meet you")

welcome() # 함수가 정의한 후에 호출을 해야 함

# 파이썬 함수의 단점 : 데이터 타입이 없어서 다른 작업자가 만든 함수를 사용할 때 주의할 점이 많음
def process(number):
    return number / 1

# process('hello')  # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# 어노테이션 사용 가능. 타입 강제는 아님
def process(number: int) -> float:
    return number / 1


# 인수와 매개변수
# 함수로 전돨되는 인수(arggument)를 저장하는 변수를 매개변수(parameter)라고 함

# 1. 인수가 있는 함수
def introduce(name: str, age: int) -> None:
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('james', 25)  # 내 이름은 james이고, 나이는 25살 입니다.
introduce(age=25, name='james')    # 내 이름은 james이고, 나이는 25살 입니다.
print()

# 2. 가변 매개변수
# 함수로 전달해야 하는 인수의 개수가 정해지지 않아도 매개변수를 선언할 수 있음
# 가변 매개변수를 만드는 키워드는 애스터리스크(*)
# 매개변수 앞에 *를 붙이면 곧바로 가변 매개 변수가 되면서 전달되는 모든 인수를 하나의 튜플(tuple)로 만들어 줌
def show(*args):
    for item in args:
        print(item)

show('python')  # show 함수 호출. 인수가 1개
show('happy', 'birthday')  # show 함수 호출. 인수가 2개
print()

# 3. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용할 수 있도록
# 매개변수에 기본값을 설정할 수 있음
def greet(message='안녕하세요'):
    print(message)
greet('반갑습니다.')
greet()
print()

# 디폴트 매개변수와 일반 매개변수를 같이 사용하는 경우 디폴트 매개변수를 뒤(오른쪽)으로 배치
def greet(name, message='안녕하세요'):
    print(f'{name}님 {message}')

greet('김철수')
greet('김철수', '반갑습니다.')
print()

# 복수의 디폴트 매개변수를 사용하는 경우
def greet(name='이철수', message='안녕하세요'):
    print(f'{name}님 {message}')

greet()  # 이철수님 안녕하세요
greet('김철수')  # 김철수님 안녕하세요
greet('김철수', '반갑습니다')  # 김철수님 반갑습니다
print()

# 반환값
# 함수 호출 결과를 반환값(return value)
# 반환값이 있으면 함수 내부에서 return 문을 통해 값을 반환할 수 있고,
# 반환값이 없으면 함수 내부에 return문을 작성할 필요가 없음

def address():
    string = '우편번호 12345\n'
    string += '서울시 영등포구 여의도동'
    return string
print(address())

def address():
    string = '우편번호 12345\n'
    string += '서울시 영등포구 여의도동'
    print(string)
print(address())
print()

# 2. 다중 반환
# 하나의 반환값도 처리할 수 있고 여러 개의 반환값도 처리할 수 있음

def calculator(*args):
    return sum(args), sum(args) / len(args), max(args), min(args)

a, b, c, d = calculator(1, 2, 3, 4, 5)  # 4개의 반환값을 모두 저장하기 위해 변수 4개 배치
print('합계', a)  # 합계 15
print('평균', b)  # 평균 3.0
print('최댓값', c)  # 최댓값 5
print('최솟값', d)  # 최솟값 1
print()

# result는 4개의 반환값을 저장하는 튜플
result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])  # 합계 15
print('평균', result[1])  # 평균 3.0
print('최댓값', result[2])  # 최댓값 5
print('최솟값', result[3])  # 최솟값 1
print()

# 3. 함수의 종료를 위한 return
# 반환값이 있으면 return문을 사용해 반환하고, 반환값이 없으면 return문을 생략하면 됨
# 반환값이 없을 때도 return문을 작성하는 경우 -> 함수를 종료할 때

def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
        return  # charge() 함수의 종료를 의미
    print()

charge(1)  # 에너지가 충전 되었습니다.
charge(-1)  # 0보다 작은 에너지는 충전할 수 없습니다.


# 4. 파이썬의 함수는 객체이고 자료형이다.
print(charge)  # <function charge at 0x104bce7a0>

def print_charge(fun):
    fun(0)

print_charge(charge)  # 함수를 함수 호출시 인수로 사용이 가능

# 5. 함수안에 함수 선언도 가능하다.
def print_greet(name):
    def get_greet():
        return '안녕하세요'

    print(name + '님 ' + get_greet())

print_greet('김철수')


# 지역변수와 전역변수

# 1. 지역변수 local variable
# 함수 내부에서 선언한 변수는 함수 내부에서만 사용. 함수 외부에서는 지역변수에 접근할 수 없음

def f():
    a = 10
    print(f'f() 내부 : {a}')

f()  # f() 내부 : 10
# print(f'f() 외부 : {a}')  # 함수 외부에서는 a 변수를 사용할 수 없음

# 2. 전역변수 global variable
# 함수 외부에서 선언한 변수는 함수 내부나 함수 외부에서 모두 사용할 수 있음
print()

def f():
    print(f'f() 내부 : {b}')

b = 10  # 전역변수
f()  # f() 내부 : 10
print(f'f() 외부 : {b}')  # f() 외부 : 10
print()

# 1) 전역변수를 단순히 참조만 하는 경우

a = 0
def f():
    print(a)  # 함수 f() 내부에서 전역변수 a를 참조
f()  # 0
print(a)  # 0 / 함수 f() 외부에서 전역변수 a를 참조
print()

# 2) 전역변수의 값을 변경하는 경우
a = 0
def f():
    global a  # 전역변수 a를 사용
    a = 10  # 전역변수 a의 값을 변경

f()  # 함수 f() 실행
print(a)  # 10 / 전역변수의 변경된 값을 확인







