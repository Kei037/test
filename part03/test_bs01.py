from bs4 import BeautifulSoup as bs

# BeautifulSoup : 구문을 분석해서 필요한 내용만 추출 할 수 있는 기능을 가지고 있는 외부 패키지

with open('./sample.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = bs(html, 'html.parser')  # html.parser : html 코드를 사용하기 쉽게 BeautifulSoup의 객체로 파싱

# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup)  # html 출력

print(soup.find('title').text)  # 문서의 제목
print(soup.find('div').text)
print(soup.find('h1').text.strip())


