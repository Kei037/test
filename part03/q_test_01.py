import pprint

import requests
import json

# 1. 공공데이터 포털(data.go.kr)에서 '대구광역시 북구_둘레길‘를 API 연결을 통해 데이터를 수집하시오.
#    데이터중에 도덕산과 함지산의 데이터를 뽑아서 산 명, 노선, 거리, 소요시간을 csv로 저장하시오.
#    파일명은 bukgu_trail.csv로 하시오.

service_key = 'eClc8eKTygrd%2BejSIWt%2FbEA7ZN4R7xuAnGOIVXmUfHlDlCC%2FjZtjwaiFe1mjMj770Rwkd9mGI26k9nMogdJoeg%3D%3D'

mountain_list = ['도덕산', '함지산']

url = 'http://apis.data.go.kr/3450000/bukguDulleRoadService/getBukguDulleRoad'
parameter = f'?serviceKey={service_key}&currentPage=1&perPage=100&MNTN_NM='

dict_list: list[dict] = list()
for mountain in mountain_list:
    response = requests.get(url + parameter + mountain)
    json_data = response.text
    dict_data = json.loads(json_data)

    for data in dict_data['body']:
        new_dict: dict = dict()
        new_dict['산 명'] = data['MNTN_NM']
        new_dict['노선'] = data['ROUTE']
        new_dict['거리'] = data['DSTNC']
        new_dict['소요 시간'] = data['REQRE_TIME']
        dict_list.append(new_dict)

# pprint.pprint(dict_list)

from share import save_csv
save_csv('./output/bukgu_trail.csv', dict_list)