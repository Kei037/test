import pprint

import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 다음 뉴스에서 제목, 링크, 뉴스 본문 추출하기

# 다음 뉴스에서 제목, 링크, 뉴스 본문 추출해서 파일로 저장하기
# 1) 이전 예제를 활용할 것
# 2) 링크를 추출한 for 안에서 제목을 추출
# 3) 뉴스 본문은 링크를 이용
# 4) 링크를 타고 뉴스 본문을 들고 와야 된
# for문 안에서 requests, BeatifulSoup가 실행이 되어야 함.
# 5) 제목, 링크, 뉴스 순으로 csv 저장

# 기사 모으기
url = 'https://news.daum.net/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

tags = soup.find_all('div', {'class': 'item_issue'})
# for news in news_list:
#     print(news)

dict_list: list[dict] = list()

for tag in tags:
    new_dict: dict = dict()
    title = tag.find_all('a')[1].text.strip()
    link = tag.find_all('a')[1].get('href')
    # print(f'title: {title}, link: {link}')
    new_dict['제목'] = title
    new_dict['링크'] = link

    response = requests.get(link)
    soup = bs(response.text, 'html.parser')

    news_line = soup.find('div', {'class': 'article_view'}).find_all('p')
    news_line_save = ''
    for news_line_depth in news_line:
        # print(news_line_depth.text)
        news_line_save = news_line_depth.text
    new_dict['뉴스'] = news_line_save
    news_line_save = ''
    dict_list.append(new_dict)
    print('*' * 20)
pprint.pprint(dict_list)
