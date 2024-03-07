import requests
from bs4 import BeautifulSoup as bs
# pip install beautifulsoup4 : 경고 메시지 출력을 막기 위해 4.10.0으로 설치

# 서버로 요청을 할때 브라우져의 정보 (User-Agent)가 같이 전달됨
# 서버에서는 브라우져의 정보를 가지고 접속자가 bot인지 일반 사용자임을 구분함.
# 특정 사이트의 경우 요청하는 브라우저의 정보가 일반 사용자가 아니면 접속을 막는 경우가 있음.
# requests의 경우 브라우져의 헤더 정보를 수정해서 일반 브라우져 처럼(?) 접속 할 수 있게 함

# 헤더 정보를 확인
url = 'http://planet-trade.kr/header_info.php'

# 1. requests를 이용해서 접속을 하면, 브라우져의 정보 (User-Agent)
# 서버에서 해당 정보를 보고 크롤링을 판단할 수 있음
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup)
# 접속 IP : 58.149.46.252
# 접속 정보 : python-requests/2.31.0

# 2. requests에서 헤더 정보를 변경할 수 있음
request_header = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'),
    'Referer': '',
}
resp = requests.get(url, headers=request_header)
soup = bs(resp.text, 'html.parser')
print(soup)


