# 공공데이터 포탈에서 '한국환경공단_에어코리아_측정소 정보' 검색후 활용신청. 키사용.
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073877
# 측정소 목록 조회 서비스를 이용
# 파일명 : daegu_air_list.csv
from typing import List
import requests
import json
import csv

# 초기값 설정
# 서비스 키 : requests 사용시 자동으로 인코딩되어서 Decoding된 키를 사용.
service_key: str = 'eClc8eKTygrd%2BejSIWt%2FbEA7ZN4R7xuAnGOIVXmUfHlDlCC%2FjZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg%3D%3D'

city = '대구'
dong = '삼덕동1가'

# url 설정
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'
# params = {'service_key': service_key, 'returnTpye': 'json', 'numOfRows': '50', 'pageNo': '1', 'addr': '대구'}
parameter = f'?umdName={dong}&&pageNo=1&numOfRows=50&serviceKey={service_key}&returnType=json'
# print(url + parameter)

# 서버에서 요청값을 받은 후 파싱
# 딕셔너리 데이터를 분석해서 원하는 값을 추출
response = requests.get(url + parameter)
# print(response.url)
json_data = response.text
dict_data = json.loads(json_data)

tmX: str = ''
tmY: str = ''

for item in dict_data['response']['body']['items']:
    if item['sidoName'].find(city) == 0:
        tmX = item['tmX']
        tmY = item['tmY']
print(tmX, tmY)
print()

# 근접측정소 목록 조회
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'
parameter = f'?tmX={tmX}&tmY={tmY}&returnType=json&serviceKey={service_key}'
response = requests.get(url + parameter)
json_data = response.text
dict_data = json.loads(json_data)
print(dict_data)

