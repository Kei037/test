# 공공데이터 포탈에서 '한국환경공단_에어코리아_측정소 정보' 검색후 활용신청. 키사용.
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877
# 측정소 목록 조회 서비스를 이용
# 대구에 있는 측정소의 측정소 명, 측정소 주소, 위도, 경도, 설치년도를 csv파일로 저장
# 파일명 : daegu_air_list.csv
from typing import List
import requests
import json
import datetime
import csv

# 초기값 설정
# 1) 서비스 키 : requests 사용시 자동으로 인코딩되어서 Decoding된 키를 사용.
service_key: str = 'eClc8eKTygrd%2BejSIWt%2FbEA7ZN4R7xuAnGOIVXmUfHlDlCC%2FjZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg%3D%3D'

# url 설정
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'
# params = {'service_key': service_key, 'returnTpye': 'json', 'numOfRows': '50', 'pageNo': '1', 'addr': '대구'}
parameter = f'?addr=대구&&pageNo=1&numOfRows=50&serviceKey={service_key}&returnType=json'
# print(url + parameter)

# 2. 서버에서 요청값을 받은 후 파싱
# 딕셔너리 데이터를 분석해서 원하는 값을 추출
# response = requests.get(url, params=params)  # params= : 딕셔너리를 쿼리 스트링으로 변경
response = requests.get(url + parameter)
# print(response.url)
json_data = response.text
dict_data = json.loads(json_data)
# print(dict_data)

item_list: List[dict] = list()  # 목록을 저장할 리스트
name_list: List[str] = ['측정소 명', '측정소 주소', '위도', '경도', '설치년도']  # csv의 헤더 및 딕셔너리의 key값으로 사용

for item in dict_data['response']['body']['items']:
    if item['addr'][0:2] == '대구':
        new_item: dict = dict()
        print(item['stationName'])
        print(item['addr'])
        print(item['dmX'])
        print(item['dmY'])
        print(item['year'])

        new_item[name_list[0]] = item['stationName']
        new_item[name_list[1]] = item['addr']
        new_item[name_list[2]] = item['dmX']
        new_item[name_list[3]] = item['dmY']
        new_item[name_list[4]] = item['year']
        item_list.append(new_item)
print(item_list)

with open('./output/daegu_air_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=name_list)
    writer.writeheader()
    for data in item_list:
        data: dict
        writer.writerow(data)
print('daegu_air_list.csv 파일이 생성 되었습니다.')