import pprint
import requests
import json

# 공공데이터 포털(data.go.kr)에서 '대구광역시_음식골목‘를 API 연결을 통해 데이터를 수집하시오.
# 데이터중에 동구의 음식골목 데이터중 추출하여 각 음식골목의 대표음식점의 상호와 주소를 골라내 음식골목명, 음식점 상호,
# 음식점 주소를 csv로 저장하시오.
# 파일명은 daegufood_street.csv로 하시오.

url = 'https://www.daegufood.go.kr/kor/api/Alley.html?mode=json'
food_url = 'https://www.daegufood.go.kr/kor/api/Alley_food.html?mode=json&OPENDATA_ID='

response = requests.get(url)
json_data = response.text
dict_data = json.loads(json_data)

dict_list: list[dict] = list()
for item in dict_data['data']:
    response = requests.get(food_url + item['OPENDATA_ID'])
    json_data = response.text
    food_dict_data = json.loads(json_data)

    for food in food_dict_data['data']:
        if food['FD_CS'].find('(동구)') >= 0:
            new_dict: dict = dict()
            new_dict['음식골목명'] = food['FD_CS']
            new_dict['음식점 상호'] = food['BZ_NM']
            new_dict['음식점 주소'] = food['GNG_CS']

            dict_list.append(new_dict)

pprint.pprint(dict_list)

from share import save_csv
save_csv('./output/daegufood_street.csv', dict_list)
