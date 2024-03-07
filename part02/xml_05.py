# 공공데이터 포털에서 인천국제공항공사_버스정보 검색
# https://www.data.go.kr/data/15095045/openapi.do
# 인천국제공항 여객터미널 T1, T2 버스 정보(공항행 첫차/막차, 종점행 첫차/막차, 성인요금.
# 버스등급, 버스번호, 지역, 운수사, 평일시간, 주말시간, 노선정보, 승차위치) 를 제공

# 인천국제공항에서 대구로 가는 버스 목록
# 버스번호, 버스등급, 성인요금, 평일시간표, 주말시간표를 csv로 저장
# 시간표는 이른 시간에 먼저 나오도록
# 예) '0610, 0630, 0810, 0830, 1130, 1150, 1740, 1800'
# 파일명 air_bus_daegu.csv

import csv
import pprint
from typing import List

import requests
import xmltodict

service_key: str = 'eClc8eKTygrd%2BejSIWt%2FbEA7ZN4R7xuAnGOIVXmUfHlDlCC%2FjZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg%3D%3D'

url = 'http://apis.data.go.kr/B551177/BusInformation/getBusInfo'
params = f'?serviceKey={service_key}&area=6&numOfRows=50&pageNo=1&type=xml'

response = requests.get(url + params)
print(response.url)
data_dict = xmltodict.parse(response.text)
# pprint.pprint(data_dict)

def sort_str(string1: str, string2: str) -> str:
    tmp_list: list[str] = (string1 + ', ' + string2).replace(' ', '').split(',')
    tmp_list = list(set(tmp_list))
    tmp_list.sort()
    return str(tmp_list)[1:-1].replace("'", '')

item_list: List[dict] = list()
name_list: List[str] = ['버스번호', '버스등급', '성인요금', '평일시간표', '주말시간표']

for entry in data_dict['response']['body']['items']['item']:
    new_item: dict = dict()
    # pprint.pprint(entry)
    if entry['routeinfo'].find('대구') > 0:
        new_item[name_list[0]] = entry['busnumber']
        new_item[name_list[1]] = entry['busclass']
        new_item[name_list[2]] = entry['adultfare']

        new_item[name_list[3]] = sort_str(entry['t1wdayt'], entry['t2wdayt'])
        new_item[name_list[4]] = sort_str(entry['t1wt'], entry['t2wt'])

        item_list.append(new_item)
pprint.pprint(item_list)

from share import save_csv

save_csv('./output/air_bus_daegu.csv', item_list)

# with open(f'./output/air_bus_daegu.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=item_list[0].keys())
#     writer.writeheader()
#     for data in item_list:
#         data: dict
#         writer.writerow(data)
# print('air_bus_daegu.csv 파일이 생성 되었습니다.')






