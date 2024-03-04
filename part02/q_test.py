# 다음 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.
#
# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다.
# 5번째 데이터가 카메라 대수 입니다.
#
# 실행 예 :
# 서울특별시 마포구에 설치된 CCTV는 총 2167대입니다.
import csv
""" 주석
with open('./input/cctv.csv', 'r', encoding='cp949') as file:
    datas = csv.DictReader(file)  # dict로 읽음
    total_cctv = 0
    for data in datas:
        total_cctv += int(data['카메라대수'])  # value가 문자열이여서 형 변환을 해야 함

print(f'서울특별시 마포구에 설치된 CCTV는 총 {format(total_cctv, ",")}대입니다.')
"""

# 구, 한국인, 외국인, 노인이 있는 csv파일 (pop_seoul.csv) 를 읽은 후에
# 1) 외국인 비율(%)을 구해서 비율이 3% 이상인 구만
# 2) 구, 한국인, 외국인, 외국인 비율(%) 순서로 csv 저장

# 개발 절차
# 1. pop_seoul.csv 파일을 읽어서 딕셔너리로 출력
# 2. 반복문을 돌려서 한 행씩 출력
# 3. 한 행씩 출력하는 코드에서 외국인 비율을 구해서 출력
# 4. 조건(비율이 3% 이상)에 해당하는 데이터만 리스트나 딕셔너리로 저장
# 5. 저장된 데이터를 csv로 저장

new_datas: list = []
with open('./input/pop_seoul.csv', 'r', encoding='cp949') as csvfile:
    reader = csv.DictReader(csvfile)
    # 총 인구수
    for row in reader:
        row: dict
        total_population: int = int(row['Korean'].replace(',', '')) + int(row['Foreigner'].replace(',', ''))
        print(f'{row["Gu"]}의 총 인구수 : {total_population}')

        # 외국인 비율
        rate_foreigner: float = int(row['Foreigner'].replace(',', '')) / total_population * 100
        print(f'{row["Gu"]}의 외국인 비율: {rate_foreigner}')

        if rate_foreigner >= 3.0:  # 조건이 맞는 경우 딕셔너리를 생성해서 리스트에 저장
            new_data: dict = dict()
            new_data['Gu'] = row['Gu']
            new_data['Korean'] = row['Korean']
            new_data['Foreigner'] = row['Foreigner']
            new_data['Rate'] = round(rate_foreigner, 1)
            new_datas.append(new_data)
print(new_datas)

with open('./output/pop_seoul.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Gu', 'Korean', 'Foreigner', 'Rate'])
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)


