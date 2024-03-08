import csv
import pprint
import requests
from bs4 import BeautifulSoup as bs
from requests import Response

# 멜론차트 가져오기
# user-agent를 확인해서 bot의 접근을 막음.
# 1. user-agent를 변경해서 결과 값을 가지고 올것
# 2. 구현후에 이 부분을 함수화 할 것.
# 3. 순위 부분을 가지고 오도록 select() / select_one() 을 사용해서 구현.

def requests_get(url: str) -> Response:
    request_header = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'),
        'Referer': '',
    }
    return requests.get(url, headers=request_header)

url = 'https://www.melon.com/chart/'

response = requests_get(url)
soup = bs(response.content, 'html.parser')
# print(soup.prettify())

chart_list = soup.select('table > tbody tr')
# pprint.pprint(chart_list)

dict_list: list[dict] = list()
for idx, chart in enumerate(chart_list):
    new_dict: dict = dict()
    # print(chart.select('div.ellipsis.rank01 > span > a')[0].text)
    # print(chart.select('div.ellipsis.rank02 > span > a')[0].text)
    # print(chart.select('td:nth-child(7) > div > div > div > a')[0].text)
    # print(chart.select_one('.image_typeAll img').get('src'))
    new_dict['순위'] = idx + 1
    new_dict['곡 제목'] = chart.select_one('.rank01').text.strip()
    new_dict['아티스트'] = chart.select_one('.rank02 a').text.strip()
    new_dict['앨범'] = chart.select_one('.rank03').text.strip()

    # 앨범 이미지 저장
    response = requests.get(chart.select_one('.image_typeAll img').get('src'))
    with open(f'./output_image/melon/{idx + 1}_{new_dict["곡 제목"]}_{new_dict["아티스트"]}.png', 'wb') as image_file:
        image_file.write(response.content)
        print(f'{idx + 1} / {len(chart_list)}')

    dict_list.append(new_dict)

# pprint.pprint(dict_list)

from part02.share import save_csv
save_csv('./output/melon_chart.csv', dict_list)
