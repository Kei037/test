# 공공 데이터 포탈에서 '대구광역사 오페라하우스 공연일정' 검색. 키 필요없음
# https://www.data.go.kr/data/15057055/openapi.do
# 제목과 링크를 csv로 저장
# 파일명 daeguoperahouse_오늘날짜.csv 예) daeguoperahoues_240306.csv
import csv
import time
from typing import List

import requests
import xmltodict
import pprint

url = 'https://www.daeguoperahouse.org/rss.php'
response = requests.get(url)
# print(response.url)
data_dict = xmltodict.parse(response.text, xml_attribs=True)
# pprint.pprint(data_dict)

item_list: List[dict] = list()
name_list: List[str] = ['title', 'link']

for entry in data_dict['rss']['channel']['item']:
    new_item: dict = dict()
    # print(entry['title'])
    # print(entry['link'])
    new_item[name_list[0]] = entry['title']
    new_item[name_list[1]] = entry['link']
    item_list.append(new_item)

for item in item_list:
    print(item)
today = time.strftime("%Y%m%d")

with open(f'./output/daeguoperahoues_{today}.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=name_list)
    writer.writeheader()
    for data in item_list:
        data: dict
        writer.writerow(data)
print('daeguoperahoues_240306.csv 파일이 생성 되었습니다.')