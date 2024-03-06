# 공공데이터포탈에서 '한국공항공사_노선별 소요시간 및 거리정보' 검색
# xml만 지원, 키 필요
# https://www.data.go.kr/data/15007809/openapi.do
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15007809
# 한국공항공사(https://www.airport.co.kr/www/index.do)에서 제공하는 API라, 인천공항은 지원하지 않음 인청공항은 인천국제공항항송사 소속
import datetime
import pprint

# 당일 부산에서 출발하는 국제선 정보 구하기
# 도착공항명, 운항거리 운항시간을 csv로 저장
# 파일명 : pus_international_air.csv

import requests
import xmltodict

service_key: str = 'eClc8eKTygrd+ejSIWt/bEA7ZN4R7xuAnGOIVXmUfHlDlCC/jZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg=='

today = datetime.datetime.now().strftime('%Y%m%d')

url = 'http://openapi.airport.co.kr/service/rest/serviceLine/serviceLines'
parameter = f'?schStDate={today}&schEdDate={today}&schLineType=D&ServiceKey={service_key}'
response = requests.get(url + parameter)
print(response.text)
data_dict = xmltodict.parse(response.text, xml_attribs=True)
pprint.pprint(data_dict)