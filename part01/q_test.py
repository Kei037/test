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

"""

