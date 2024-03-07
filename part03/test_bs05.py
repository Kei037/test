import requests
from bs4 import BeautifulSoup as bs
import pprint

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 네이버 뉴스 : IT/과학에서 오른쪽 섹션의 언로사별 가장 많이 본 뉴스 제목 들고오기.

url = 'https://news.naver.com/section/105'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

section_list = soup.find_all('ul', {'class': 'ranking_list'})
# print(section_list)
for section in section_list:
    news_list = section.find_all('p', {'class': 'rl_txt'})
    for news in news_list:
        print(news.text.strip())
    print()