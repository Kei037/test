import requests
from bs4 import BeautifulSoup as bs
import pprint

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 1) find_all() 메소드
# 지정된 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관

# 네이버 스포츠 페이지에서 박스 뉴스 제목 들고 옴
url = 'https://sports.news.naver.com/index.nhn'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# today_list = soup.find('ul', {'class': 'today_list'}).find_all('strong', {'class': 'title'})
today_list = soup.find('ul', {'class': 'today_list'})
# print(today_list)

today_list_title = today_list.find_all('strong', {'class', 'title'})
# pprint.pprint(today_list_title)

for title in today_list_title:
    print(title.text.strip())
