import requests

# requests 사용법

url = 'http://www.naver.com/'
response = requests.get(url)  # get() 또는 post() 메서드를 이용해서 html 정보를 받아옴

html = response.text  # response 객체의 text 속성을 지정하면 html 정보 반환.
# print(html)  # html 소스가 출력

headers = response.headers  # response 객체의 headers 속성 지정하면 헤더 정보 반환.
print(headers)

import requests

# 모든 크롤링이 불법은 아님.
# 하지만 운영자의 의사에 상관없이 무단으로 크롤링하는 것은 불법.
#
# 운영자의 의사를 알수 있는 방법.
# robot.txt 에서 확인
#
# allow는 허용
# disallow는 검색 불가

# https://searchadvisor.naver.com/guide/seo-basic-robots
# https://developers.google.com/search/docs/advanced/robots/intro?hl=ko

urls = ['https://www.naver.com/', 'https://ko.wikipedia.org/']
filename = 'robots.txt'


for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")