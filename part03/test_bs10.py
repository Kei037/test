import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select() 메소드 이용하기

# select() 메소드
# 네이버 -> '환율' 검색 -> 환율 더보기

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())

nations = soup.select('#exchangeList > li > a.head > h3 > span')  # 국가
print(nations)

exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value')  # 환율 가져옴
print(exchange_rates)

for idx, item in enumerate(nations):
    print(f'{item.text} : {exchange_rates[idx].text}')

# 미국 USD : 1,326.00
# 일본 JPY(100엔) : 895.61
# 유럽연합 EUR : 1,451.64
# 중국 CNY : 184.18
