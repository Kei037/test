# 오늘의 스케줄을 입력하면 그 내용이 모두 파일에 보관되는 프로그램입니다.
# 스케줄을 입력하지 않고 enter를 누르면 프로그램은 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2020-10-22.txt' 와 같은 형식을 갖추고 있습니다.
"""
import time

file = open(f'./output/{time.strftime("%Y-%m-%d")}.txt', 'at')

while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    if not schedule:
        break
    file.write(schedule + '\n')

file.close()
"""
# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서
# '꿀' 이라는 글자가 몇 번 나오는지 찾는 프로그램입니다.

file = open('./input/엄마돼지아기돼지.txt', 'rt', encoding='EUC-KR')

line_list = file.readlines() # 줄 단위로 읽어서 리스트로 반환
print(line_list)
count = 0
for line in line_list:  # 줄 단위 문자열 추출
    for ch in line:  # 개별 문자 추출
        # print(ch)
        if ch == '꿀':
            count += 1

print(f'꿀은 전체 {count}번 나타납니다.')