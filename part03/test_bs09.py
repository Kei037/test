import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select() 메소드 이용하기

# select() 메소드
# CSS selector로 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관

# 다음 -> 뉴스 -> IT -> 오늘의 연재의 첫번재 글 제목과 신문사 들고오기
url = 'https://news.daum.net/digital#1'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

tag_series = soup.select('.list_todayseries li')
# print(tag_series)
print()

for tag in tag_series:
    tag_series_title = tag.select_one('.link_txt').text
    print(f'제목: {tag_series_title}')

    tag_series_press = tag.select_one('.txt_info').text
    print(f'신문사: {tag_series_press}')







