import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select() 메소드 이용하기

# select() 메소드
# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산

def get_exchange_rate(menu: int) -> float:  # 원하는 환률을 가져옴
    url = 'https://finance.naver.com/marketindex/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value')
    exchange_rate: float = float(exchange_rates[menu - 1].text.replace(',', ''))
    return exchange_rate

print('=== 메 뉴 ===')
print('1. 미국')
print('2. 일본')
print('3. 유럽')
print('4. 중국')
print('============')
menu = int(input('선택 >> '))
unit = ['달러', '엔', '유로', '위안']
money = int(input(f'금액 입력 (단위 : {unit[menu - 1]}) >> '))

if menu == 2:  # 일본을 선택했다면? 네이버에서는 100엔 기준 금액을 제공
    money = money / 100

print(get_exchange_rate(menu) * money, '원')





"""

# print(soup.prettify())

nations = soup.select('#exchangeList > li > a.head > h3 > span')  # 국가
print(nations)

  # 환율 가져옴
print(exchange_rates)

for idx, item in enumerate(nations):
    print(f'{item.text} : {exchange_rates[idx].text}')

# 미국 USD : 1,326.00
# 일본 JPY(100엔) : 895.61
# 유럽연합 EUR : 1,451.64
# 중국 CNY : 184.18
"""