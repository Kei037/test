import requests
from bs4 import BeautifulSoup as bs
import pprint

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 1) find_all() 메소드

# 다음 뉴스
url = 'https://news.daum.net/?nil_profile=mini&nil_src=news'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# a 태그의 갯수 출력
# print('1. a 태그의 갯수')
# print(len(soup.find_all('a')))
# print()

# a 태그 20개만 출력
# print('2. a 태그 20개만 출력')
# for news in soup.find_all('a')[:20]:
#     print(news.text.split())

# a 태그 링크 5개 출력
# print('3. a 태그 링크 5개 출력')
# for i in soup.find_all('a')[:5]:
#     print(i.attrs['href'])
#     print(i.get('href'))
# print("=" * 20)

# 특정 클래스 속성을 출력하기
# print('4. 특정 클래스 속성을 출력')
# print(soup.find_all('div', {'class': 'item_issue'}))
# print("=" * 20)

# 링크를 텍스트 파일로 저장
print('5. 링크를 텍스트 파일로 저장')
file = open('./output/links.txt', 'w', encoding='utf-8')  # 쓰기 전용 파일 생성

for i in soup.find_all('div', {'class': 'item_issue'}):
    file.write(i.find('a').get('href') + '\n')

file.close()

# 문제 : with 사용. 뉴스 타이틀 추출. 파일명은 news_title.txt
# 넘버링 붙도록 예) 1. 日증시, 차익매물에 사흘만에 40,000 아래로…장중엔 한때 최고(종합)

url = 'https://news.daum.net/?nil_profile=mini&nil_src=news'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

with open('./output/news_title.txt', 'w', encoding='utf-8') as file:
    for i, news in enumerate(soup.find_all('div', {'class': 'item_issue'})):
        file.write(f'{i + 1}. {news.find_all("a")[1].text.strip()}\n')

