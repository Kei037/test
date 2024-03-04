# 조건 : 롯데캐슬 단지만 검색
# 출력조건 : 구(구만 나오도록 할 것), 단지명, 전용면적, 층, 거래금액
# 저장 파일명: apt_2403_조건2.csv
# with로 파일 처리
# 예) 달서구, 롯데캐슬레이크, 84.91, 3, "32,100"

import csv
from typing import List

new_datas: List[dict] = list()
with open('./input/아파트(매매)_실거래가_20240304154528.csv', encoding='cp949') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        if row["단지명"].find('롯데캐슬') >= 0:
            new_data: dict = dict()
            new_data['시군구'] = row['시군구'].split()[1]
            new_data['단지명'] = row['단지명']
            new_data['전용면적(㎡)'] = row['전용면적(㎡)']
            new_data['층'] = row['층']
            new_data['거래금액(만원)'] = row['거래금액(만원)']
            new_datas.append(new_data)
# print(new_datas)
header: list = list(new_datas[0].keys())

file_name = 'apt_2403_조건2.csv'
with open(f'./output/{file_name}', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print(f'{file_name}파일이 생성 되었습니다.')