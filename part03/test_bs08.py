import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select_one() 메소드 이용하기

# 할리스 커피 : 매장검색
url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())

# 매장 테이블 가져오기
# stores = soup.select_one('#contents > div.content > fieldset > fieldset > div.tableType01 > table')
stores = soup.select_one('table.tb_store')
# print(stores)

first_store = stores.select_one('#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1)')
print(first_store)

# tr:nth-child(1) -> td 태그중 첫번째
first_store_name = first_store.select_one('td:nth-child(2)')
# print(second_store_name.text)

first_store_address = first_store.select_one('td:nth-child(4)')
print(first_store_address.text)



