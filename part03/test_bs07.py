import requests
from bs4 import BeautifulSoup as bs
import pprint

# BeautifulSoup 실습 : select_one() 메소드 이용하기

# 다음 -> 뉴스 -> IT -> 오늘의 연재의 첫번재 글 제목과 신문사 들고오기
url = 'https://news.daum.net/digital#1'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

tag_series = soup.select_one('.list_todayseries li')
# print(tag_series)
print()

tag_series_title = tag_series.select_one('.link_txt').text
print(f'제목: {tag_series_title}')

tag_series_info = tag_series.select_one('.txt_info').text
print(f'신문사: {tag_series_info}')