# 공공데이터포탈에서 '한국공항공사_노선별 소요시간 및 거리정보' 검색
# xml만 지원, 키 필요
# https://www.data.go.kr/data/15095074/openapi.do
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15095074
#

import datetime
import pprint
import requests
import xmltodict

# 당일 부산에서 출발하는 국제선 정보 구하기
# 도착공항명, 운항거리 운항시간을 csv로 저장
# 파일명 : pus_international_air.csv

service_key: str = 'eClc8eKTygrd%2BejSIWt%2FbEA7ZN4R7xuAnGOIVXmUfHlDlCC%2FjZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg%3D%3D'

today = datetime.datetime.now().strftime('%Y%m%d')

url = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerDeparturesDSOdp'
parameter = f'?serviceKey={service_key}&type=xml'

response = requests.get(url + parameter)
# print(response.text)
# print(response.url)
data_dict = xmltodict.parse(response.text, xml_attribs=True)
# pprint.pprint(data_dict)

dict_list = list()
for data in data_dict['response']['body']['items']['item']:
    pprint.pprint(data)
    if data.get('airline') and data['airline'] == '대한항공':  # airline 키값이 없는 경우도 있어서, 키값부터 확인
        new_data = dict()
        new_data['항공사'] = data['airline']
        new_data['편명'] = data['flightId']
        new_data['예정시간'] = data['scheduleDateTime']
        new_data['도착지공항'] = data['airport']
        dict_list.append(new_data)

pprint.pprint(dict_list)

