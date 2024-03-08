import requests
from bs4 import BeautifulSoup as bs
import pprint

# BeautifulSoup 실습 : select_one() 메소드 이용하기

# find가 원하는 태그를 찾는게 목적이라면 select는 CSS selector로 tag 객체를 찾아 반환
# select_one()은 원하는 태그 하나만 가져오고, 태그가 많은 경우에는 맨 앞의 것만 가져옴.

# 대구광역시 위키피디아에서 상징 > 시조 > 독수리 들고 오기
url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# select 계열의 메서드는 css selector 이용 가능.
# '.' -> class 속성, '#' -> id 속성
# class : 하나의 html에서 여러 태그에 중복 사용 가능.
# id : 하나의 html에서 한번만 사용. 권장사항.

tag_symbol = soup.select_one('.mw-parser-output ul')
print(tag_symbol)

text_symbol = soup.find('a').text
print(text_symbol)
