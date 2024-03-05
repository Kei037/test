# 부동산 실거래 파일 http://rtdown.molit.go.kr/ 다운 받아 사용.
# 24년 update : 홈페이지 접근 후 [자료제공 바로가기] 클릭
# 전국은 1달치, 지역을 지정하면 1년치
# 대구 1년치로 작업
# 계약일자는 기본 값, 파일 구분은 CSV, 나머지는 기본 값 사용.
# 다운 받은 후 메모장에서 파일을 열고 15행까지는 삭제

# 조건 : 래미안 단지만 검색
# 출력조건 : 시군구, 단지명, 전용명적, 층, 거래금액
# 저장 파일명: apt_2403_조건1.csv
# with로 파일 처리

import csv
from typing import List

new_datas: List[dict] = list()
with open('./input/아파트(매매)_실거래가_20240304154528.csv', encoding='cp949') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        if row["단지명"].find('래미안') >= 0:
            new_data: dict = dict()
            new_data['시군구'] = row['시군구']
            new_data['단지명'] = row['단지명']
            new_data['전용면적(㎡)'] = row['전용면적(㎡)']
            new_data['층'] = row['층']
            new_data['거래금액(만원)'] = row['거래금액(만원)']
            new_datas.append(new_data)
print(new_datas)
header: list = list(new_datas[0].keys())
print(header)
file_name = 'apt_2403_조건1.csv'
with open(f'./output/{file_name}', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print(f'{file_name}파일이 생성 되었습니다.')