import pprint
import requests
from bs4 import BeautifulSoup as bs

# 3. cgv 홈페이지(cgv.co.kr)의 무비차트에서 순위별로 영화 제목과 개봉일, 예매율을 requests를 이용해서
# 데이터와 영화 포스터 이미지를 수집하시오.
# 영화 제목과 개봉일, 예매율을 데이터 베이스에 저장할 수 있는 테이블 생성 쿼리를 생성하고,
# 반복문을 이용하여 영화 제목과 개봉일, 예매율을 저장하는 insert 쿼리를 출력하는 코드를 작성하시오.

url = 'http://www.cgv.co.kr/movies/'

response = requests.get(url)
soup = bs(response.content, 'html.parser')

chart_list = soup.select('.wrap-movie-chart .sect-movie-chart ol li')

dict_list: list[dict] = list()
for idx, chart in enumerate(chart_list):
    new_dict: dict = dict()
    new_dict['영화 제목'] = chart.select_one('.title').text.strip()
    release_date = chart.select_one('.txt-info > strong').text

    if release_date.find('개봉') >= 0:
        new_dict['개봉일'] = release_date.replace('개봉', '').strip()
    elif release_date.find('재개봉') >= 0:
        new_dict['개봉일'] = release_date.replace('재개봉', '').strip()

    new_dict['예매율'] = chart.select_one('.score span').text.strip()

    dict_list.append(new_dict)

    # 이미지 저장
    response = requests.get(chart.select_one('.thumb-image img').get('src'))
    with open(f'./output_image/cgv/{idx + 1}_{new_dict["영화 제목"]}_{new_dict["개봉일"]}.png', 'wb') as image_file:
        image_file.write(response.content)
        print(f'{idx + 1} / {len(chart_list)}')

pprint.pprint(dict_list)

"""
데이터 베이스 쿼리
create table ranking_cgv(
    rno              bigint auto_increment primary key,
    movie_name       varchar(40)  not null,
    release_date     varchar(10)  not null,
    reservation_rate varchar(20)  not null
);

INSERT INTO ranking_cgv (movie_name, release_date, reservation_rate) 
VALUES (new_dict['영화 제목'], new_dict['개봉일'], new_dict['예매율']);
"""