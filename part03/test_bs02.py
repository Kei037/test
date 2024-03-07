import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find() 메소드 이용하기

# 1) find() 메소드
# 지정된 태그들 중에 가장 첫 번째 태그만 가져오는 메소드(하나의 값만 반환). 문자열 형태로 반환.
# 일반적으로 하나의 태그만 존재하는 경우에 사용. 만약 여러 태그가 있으면 첫 번째 태그만 가져옴

# 위키피디아 '대구광역시' 페이지
url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')

first_img = soup.find(name='img')  # img 태그 중에 제일 먼저 나오는 것
print(type(first_img))
print(first_img)

target_img = soup.find('img', attrs={'alt': 'Daedongyeojido (Gyujanggak) 17-02.jpg'})
print(target_img)