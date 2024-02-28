from typing import Any

"""
english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
english = input('영어 단어를 입력하세요 >>> ')
print(f'{english}: {english_dict[english]}')


s = set()
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
print('조사된 수학여행지는 {}입니다.'.format(s))

li = list()
li.append(input('희망하는 수학여행지를 입력하세요 >>> '))
li.append(input('희망하는 수학여행지를 입력하세요 >>> '))
li.append(input('희망하는 수학여행지를 입력하세요 >>> '))
print(f'조사된 수학여행지는 {set(li)}입니다.')


number = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
print(f'십의 자리: {number // 10}')
print(f'일의 자리: {number % 10}')

number_str = input('10 ~ 99 사이의 정수를 입력하세요 >>> ')
print(f'십의 자리: {number_str[0]}')
print(f'일의 자리: {number_str[1]}')

times = int(input('초를 입력하세요 >>> '))
hour = times // 3600
min = times % 3600 // 60
sec = times % 60

print(f'변환 결과는 {hour}시간 {min}분 {sec}초 입니다.')


number = input('4자리 사원번호를 입력하세요 >>> ')
last_num = int(number[3])
time = '오전' if last_num >= 5 else '오후'
print(f'근무 시간은 {time}입니다.')
print()

kr = int(input('국어 점수를 입력하세요 >>> '))
eng = int(input('영어 점수를 입력하세요 >>> '))
math = int(input('수학 점수를 입력하세요 >>> '))
avg = float((kr + eng + math) / 3)
result = '합격' if avg >= 80 else '불합격'
print(f'평균은 {avg}점 이고, 결과는 {result}입니다.')
print()


print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
ramen = int(input('라면의 개수를 입력하세요 >>> '))
box = ramen // 20 if ramen % 20 == 0 else ramen // 20 + 1
print(f'{ramen}개의 라면을 담으려면 {box}박스가 필요합니다.')
print()

age = int(input('몇 살입니까? >>> '))
if age <= 7:
    print('미취학')
elif age <= 13:
    print('초등학생')
elif age <= 16:
    print('중학생')
elif age <= 19:
    print('고등학생')
else:
    print('성인')

if age >= 20:
    print('성인')
elif age >= 17:
    print('고등학생')
elif age >= 14:
    print('중학생')
elif age >= 8:
    print('초등학생')
else:
    print('미취학')


scores = int(input('점수를 입력하세요 >>> '))
if scores >= 90:
    grade = 'A'
elif scores >= 80:
    grade = 'B'
elif scores >= 70:
    grade = 'C'
elif scores >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'점수는 {scores}점이고, 학점은 {grade} 학점입니다.')
print()

num = int(input('정수를 입력하세요 >>> '))
if num % 3 == 0:
    print(f'{num}는 3의 배수입니다.')
else:
    print(f'{num}는 3의 배수가 아닙니다.')
print()

num1 = int(input('정수1 입력 >>> '))
num2 = int(input('정수2 입력 >>> '))
num3 = int(input('정수3 입력 >>> '))

if num1 > num2 and num1 > num3:
    big_num = num1
elif num2 > num1 and num2 > num3:
    big_num = num2
elif num3 > num1:
    big_num = num3
print(f'가장 큰 수는 {big_num}입니다.')



# 사용자로 부터 임으의 정수를 입력받아 모두 리스트에 보관
# 단 사용자가 0을 입력하면 프로그램을 종료. 이 때 입력받은 0은 리스트에 보관하지 않음

my_list = []

n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

print(my_list)



num_for = int(input('정수를 입력하세요 >>> '))
if num_for <= -0:
    print('잘못된 입력입니다.')
else:
    n = 1
    while n <= num_for:
     print(f'{n}번째 Hello')
     n += 1


money = int(input('자판기에 얼마를 넣을까요? >>> '))
n = 1
while money >= 300:
    money -= 300
    print(f'커피{n}잔, 잔돈{money}')
    n += 1

numbers = set()
while len(numbers) < 5:
    s_num = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    numbers.add(s_num)
print('모두 입력되었습니다.')
print(f'입력된 값은 {numbers}입니다.')



# 문자열로 비밀번호를 입력 받아 숫자와 문자가 모두 포함이 되었는지 확인
pwd = input('비밀번호를 입력하세요 >>> ')

ch_count = 0  # 문자의 개수 저장
num_count = 0  # 숫자의 개수 저장

for ch in pwd:  # 반복가능객체가 문자열
    if ch.isalpha():  # ch가 문자인 경우 True를 반환
        ch_count += 1
    elif ch.isnumeric():  # ch가 숫자인 경우 True를 반환
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')

"""


"""

dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print(f'{dan} x {n} = {dan * n}')

"""
"""
for num in range(5, 0, -1):
    print(num)

f_num = int(input('임의의 양수를 입력하세요 >>> '))
sum = 0;
for n in range(0, f_num + 1):
    sum += n
print(f'1부터 {f_num}사이의 모든 정수의 합계는 {sum}입니다.')

fruit_list = list()
s_num = int(input('몇 개의 과일을 보관할까요? >>> '))
for n in range(1, s_num + 1):
    fruit = input(f'{n}번재 과일을 입력하세요 >>> ')
    fruit_list.append(fruit)
print(f'입력 받은 과일들은 {fruit_list}입니다.')

# break
while True:
    city = input('대한민국의 수도는 어디인가요? >>> ')
    city = city.strip()  # 문자열의 양쪽끝에서 공백을 없앰
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')
        

hobbies = []
while True:
    hobby = input('취미를 입력하세요(종료는 그냥 q) >> ')
    if hobby == 'q':
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else:
        hobbies.append(hobby)

    if len(hobbies) >= 5:
        print('5개 입력!')
        break
print(hobbies)

fruits = ['사과', '감귤']
count = 3

while count > 0:
    fruit = input('어떤 과일을 저장할까요? >>> ')

    if fruit in fruits:  # fruits 리스트에 fruit 변수에 있는 값이 있다면
        print('동일한 과일이 있습니다.')
        continue  # while문의 시작 지점으로 돌아가서 다시 과일 이름을 입력

    fruits.append(fruit)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')
print(f'5개 과일은 {fruits}입니다.')
"""
"""
money = 10000
while money > 0:
    print(f'현재 {money}원이 있습니다.')
    amount = int(input('사용할 금액 입력 >>> '))
    if amount <= 0:
        print('0이하의 금액은 사용할 수 없습니다.')
        continue
    if amount > money:
        print(f'{amount - money}원이 무족합니다.')
        continue
    money -= amount
print(f'현재 {money}원이 있습니다.')
print()

flag = True
while flag:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 0 >= score or score >= 6:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
        continue
    print('평점: {}'.format(score * '*'))
    flag = False
print()

while True:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1 <= score <= 5:
        print(f'평점: {"*" * score}')
        break
    print('평점은 1~5 사이만 입력할 수 있습니다.')
print()

password = 'qwerty'
count = 5

while True:
    ipw = input('비밀번호를 입력하세요 >>> ')
    count -= 1
    if ipw == password:
        print('비밀번호를 맞혔습니다.')
        break
    if count == 0:
        print('비밀번호 입력 횟수를 초과했습니다.')
        break

"""

"""
print('점수를 입력하세요.')
print('더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
scores = 0
exam = []
while True:
    scores = int(input('점수 입력 >>> '))
    if scores < 0:
        break
    exam.append(scores)
print(f'평균 = {sum(exam) / len(exam)}, 최대 = {max(exam)}, 최소 = {min(exam)}')

"""
"""

months_eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# range() 사용
for idx in range(len(months_eng)):
    print(f'{months_eng[idx]} = {months[idx]}')
print()

# enumerate() 사용
for idx, v in enumerate(months_eng):
    print(f'{v} = {months[idx]}')
print()

# dict 사용
months_dict = dict()
for i, v in enumerate(months_eng):
    months_dict.update({v: months[i]})

for k, v in months_dict.items():
    print(f'{k} = {v}일')

"""
"""

# 주민등록번호에서 생년월일 6자리를 추출하는 프로그램
# 사용자로부터 하이픈을 포함한 전체 주민등록번호를 입력받아 처리하는데
# 만약 하이픈의 위치가 올바르지 않다면 오류 메시지를 출력하고 다시 입력 받도록 처리

while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-') != 6:  # 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
        print('하이픈의 위치가 잘못되었습니다.')
        continue

    birthday = p.split('-')
    print(birthday)
    print(f'생년월일은 {birthday[0]}입니다.')
    print(f'생년월일은 {p[0:6]}입니다.')
    break

"""

"""
1. 우리나라의 전화번호는 '지역번호-국번-가입자 개별번호'형식으로 되어 있습니다.

02-543-2109
02-2345-6789
032-789-0123
031-4567-8900

어떤 형식의 전화번호를 입력하더라도 '국번'을 추출하여 출력하는 프로그램을 구현하세요.

실행 예)
전화번호를 입력하세요 >>> 02-1234-5678
1234

# 1. find() 메서드와 슬라이싱 사용
phone = input('전화번호를 입력하세요 >>> ')
start = phone.find('-') + 1
end = phone.find('-', start)
code = phone[start:end]
print(code)

# 2. split() 메소드 활용
number = input('전화번호를 입력하세요 >>> ')
num_sp = number.split('-')[1]
print(num_sp)
"""

"""
2. '숫자3자리-숫자2자리-숫자5자리' 형식(예: 123-45-67890)의 사업자등록번호를 입력받아서 형식이 
맞는지 점검하는 프로그램을 구현하세요.
다음 지시사항을 모두 점검해야 합니다.

지시사항
1. 전체 글자 수를 점검합니다.
2. 모든 하이픈(-)의 위치가 올바른지 점검합니다.
3. 하이픈(-)을 제외하면 모두 숫자인지 점검합니다.

실행 예) 
사업자등록번호를 입력하세요(예: 123-45-67890) >>> 123-사오-67890
올바른 형식이 아닙니다.
--------------------
사업자등록번호를 입력하세요(예: 123-45-67890) >>> 123-4-67890
올바른 형식이 아닙니다
--------------------
사업자등록번호를 입력하세요(예: 123-45-67890) >>> 123-45-67890
올바른 형식입니다.

힌트 : 숫자인지는 점검할 때는 isdecimal() 메서드를 이용합니다.
"""
"""
# case1
while True:
    num = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
    if len(num) != 12:
        print('올바른 형식이 아닙니다.')
        continue
    if num.find('-') != 3:
        print('올바른 형식이 아닙니다.')
        continue
    if num.rfind('-') != 6:
        print('올바른 형식이 아닙니다.')
        continue
    r_num = num.replace('-', '')
    if not r_num.isdecimal():
        print('올바른 형식이 아닙니다')
        continue
    print('올바른 형식입니다.')
    break

# case2
no = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
condition1 = (no.find('-') == 3)
condition2 = (no.find('-', 4) == 6)
condition3 = (len(no) == 12)
condition4 = (no.replace('-', '').isdecimal())
if condition1 and condition2 and condition3 and condition4:
    print('올바른 형식입니다.')
else:
    print('올바른 형식이 아닙니다')
"""
"""
# 커피 자판기 프로그램.
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# '아메리카노': 1000,
# '카페라떼': 1500,
# '카푸치노': 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환
"""
"""
def coffee_machine(money: int, pick: str) -> tuple[int, str]:
    print(f'{money}원에 {pick}를 선택하셧습니다.')
    # 커피와 가격을 하나의 데이터로 처리하기 위해 딕셔너리 dict를 사용
    menu = {
        '아메리카노': 1000,
        '카페라떼': 1500,
        '카푸치노': 2000
    }
    # 없는 커피를 주문하는 경우
    if pick not in menu:  # 없는 커피를 주문하는 경우
        print(f'{pick}는 판매하지 않습니다.')
        return money, '없는 메뉴'
    elif menu[pick] > money:  # 구매할 금액이 부족한 경우
        print(f'{pick}는 {menu[pick]}원 입니다.')
        return money, '금액 부족'
    else:  # 정상 주문이면 잔돈과 선택한 커피를 반환
        return money - menu[pick], pick

order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ')
pay = int(input('얼마를 내시나요? >>> '))

change, coffee = coffee_machine(pay, order)
print(f'잔돈 {change}원, 커피 {coffee}')
"""

"""
1. 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

함수 정의
* 반환값 : 없음
* 함수 이름 : vending_machine()
* 매개변수 : 정수 money

코드 구성
def vending_machine(money):
 # 함수 구현

vending_machine(3000)

실행 예)
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
"""
"""
def vending_machine(money: int) -> None:
    count: int = 0
    price: int = 700
    while True:
        print(f'음료수 = {count}개, 잔돈 = {money}')
        money = money - price
        count += 1
        if money < price:
            print(f'음료수 = {count}개, 잔돈 = {money}')
            break

vending_machine(3000)
"""
"""
2. 키(key)가 '과목명', 값(value)이 '점수'인 marks 딕셔너리를 전달하면
해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average() 함수를 구현하세요.

함수 정의
* 반환값 : 평균
* 함수 이름 :get_average()
* 매개변수 : 딕셔너리 marks

코드 구성
def get_average(marks):
 # 함수 구현

marks = {'국어':90, '영어':80, '수학':85}
average = get_average(marks)
print(f'평균은 {average}입니다.')

실행 예)
평균은 85.0점입니다.
"""
"""
def get_average(marks: dict[Any, int]) -> float:
    return sum(marks.values()) / len(marks)

marks = {'국어':90, '영어':80, '수학':85}
average = get_average(marks)
print(f'평균은 {average}입니다.')
"""
"""
1. 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

지시사항
1. 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
2. 다음 과정을 6번 반복합니다.
 * pot 리스트를 무작위로 섞어줍니다.
 * pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
 * 2초 동안 잠시 멈춥니다.
3. jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
4. jackpot 리스트의 모든 요소를 출력합니다.

실행 예)
1번째 당첨번호는 4입니다.
2번째 당첨번호는 34입니다.
3번째 당첨번호는 13입니다.
4번째 당첨번호는 36입니다.
5번째 당첨번호는 44입니다.
6번째 당첨번호는 31입니다.
이번 당첨번호는 [4, 13, 31, 34, 36, 44] 입니다.
"""
import time
import random
jackpot = []
pot = list(range(1, 46))
# print(pot)
for n in range(6):
    random.shuffle(pot)
    # print(pot)
    jackpot_num = pot.pop()
    jackpot.append(jackpot_num)
    time.sleep(2)
    print(f'{n + 1}번째 당첨번호는 {jackpot_num}입니다.')

jackpot.sort()
print(f'이번 당첨번호는 {jackpot} 입니다.')

"""
2. 다음 지시사항에 따라 UpDown게임을 구현하세요.

지시사항
1. 1에서 100 사이의 정수 중 하나를 임의로 생성하면
사용자는 그 숫자를 맞힐 때까지 값을 예상하여 입력합니다.
2. 사용자가 입력한 값이 정답보다 작으면 Up, 정답보다 크면 Down을 출력합니다.
3. 정답을 맞히면 몇 초 만에 정답을 맞혔는지 출력하세요.
이때 소수 아래 값은 내림 처리하여 정수로 출력하세요.

실행 예)
UpDown게임을 시작합니다.
어떤 값일까요? >>> 30
Up
어떤 값일까요? >>> 70
Down
어떤 값일까요? >>> 60
Down
어떤 값일까요? >>> 50
Up
어떤 값일까요? >>> 55
Up
어떤 값일까요? >>> 56
Up
어떤 값일까요? >>> 57
Up
어떤 값일까요? >>> 58
58! 정답입니다.
34초 만에 성공했습니다.
"""
import math
result = random.randint(1, 100)
print(result)
print('UpDown게임을 시작합니다.')
while True:
    start = time.time()
    answer = int(input('어떤 값일까요? >>> '))
    if answer < result:
        print('UP')
        continue
    elif answer > result:
        print('DOWN')
        continue
    elif answer == result:
        print(f'{result}! 정답입니다.')
        end = time.time()
        stop = end - start
        stop_ceil = math.ceil(stop)
        print(f'{stop_ceil}초 만에 성공했습니다.')
        break


