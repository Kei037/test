import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.naver.com/'
response = requests.get(url)  # get() 또는 post() 메서드를 이용해서 html 정보를 받아옴
# html = response.text  # response 객체의 text 속성을 지정하면 html 정보 반환.
soup = bs(response.text, 'html.parser')
print(soup)  # html 소스가 출력
