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


