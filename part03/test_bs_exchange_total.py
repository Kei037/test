import pprint

import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select() 메소드 이용하기

# select() 메소드
# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
datas = soup.select_one('#select_to')

dict_list: list[dict] = list()
for data in datas.select('option'):
    # print(data)
    # print(data.text)
    # print(data.get('value'))
    new_dict: dict = dict()
    nation = data.text.split(' ')[0]
    if nation in '남아프리카':
        new_dict['나라'] = ' '.join(data.text.split(' ')[0:2])
        new_dict['단위'] = ' '.join(data.text.split(' ')[2:])
    else:
        new_dict['나라'] = nation
        new_dict['단위'] = ' '.join(data.text.split(' ')[1:])
    new_dict['환율'] = data.get('value')
    new_dict['원화비율'] = data.get('label')

    dict_list.append(new_dict)

pprint.pprint(dict_list)

# money = int(input('환률 계산할 금액을 입력해주세요. (단위 :원) >> '))
print('== 국가 선택 ==')
for idx, data in enumerate(dict_list):
    print(idx + 1, ')' , data.get('나라'), '\t', end='')

"""
환률 계산할 금액을 입력해주세요. (단위 :원) >> 10000
== 국가 선택 ==
1) 대한민국	2) 미국	3) 미국	4) 유럽연합	5) 일본	6) 중국	7) 홍콩	8) 대만	9) 영국	10) 오만	
11) 캐나다	12) 스위스	13) 스웨덴	14) 호주	15) 뉴질랜드	16) 체코	17) 칠레	18) 튀르키예	19) 몽골	20) 이스라엘	
21) 덴마크	22) 노르웨이	23) 사우디아라비아	24) 쿠웨이트	25) 바레인	26) 아랍에미리트	27) 요르단	28) 이집트	29) 태국	30) 싱가포르	
31) 말레이시아	32) 인도네시아	33) 카타르	34) 카자흐스탄	35) 브루나이	36) 인도	37) 파키스탄	38) 방글라데시	39) 필리핀	40) 멕시코	
41) 브라질	42) 베트남	43) 남아프리카	44) 러시아	45) 헝가리	46) 폴란드	47) 스리랑카	48) 알제리	49) 케냐	50) 콜롬비아	
51) 탄자니아	52) 네팔	53) 루마니아	54) 리비아	55) 마카오	56) 미얀마	57) 에티오피아	58) 우즈베키스탄	59) 캄보디아	60) 피지	
환전한 국가를 선택해 주세요 >> 41
10000원은 브라질로 환전하면 37.2203818811181레알입니다.
"""




# print(exchange_rates[0].text)


# def get_exchange_rate(menu: int) -> float:  # 원하는 환률을 가져옴
#     url = 'https://finance.naver.com/marketindex/'
#     response = requests.get(url)
#     soup = bs(response.text, 'html.parser')
#     exchange_rates = soup.select('#select_to')
#     exchange_rate: float = float(exchange_rates[menu - 1].text.replace(',', ''))
#     return exchange_rate

# money = int(input(f'금액 입력 (단위 : {unit[menu - 1]}) >> '))
#
# if menu == 2:  # 일본을 선택했다면? 네이버에서는 100엔 기준 금액을 제공
#     money = money / 100
#
# print(get_exchange_rate(menu) * money, '원')

