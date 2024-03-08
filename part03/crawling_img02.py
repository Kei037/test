import requests
import os.path
from bs4 import BeautifulSoup as bs

# 할리스 커피에서 태그를 이영해서 이미지 저장

url = 'https://www.hollys.co.kr/menu/espresso.do'
response = requests.get(url)
soup = bs(response.content, 'html.parser')

# 1. 커피이미지 태그 가져오기
image_tag = soup.select_one('#menuView1_877 > img')
# print('HTML 요소: ', image_tag)
print()

# 2. 이미지 경로 가져오기
# img_source = image_tag.get('src')
img_source = image_tag.attrs['src']
print('이미지 파일 경로: ', img_source)
print()

response = requests.get('https:' + img_source)
with open('./output_image/download_image.png', 'wb') as image_file:
    image_file.write(response.content)
    print('이미지 파일로 저장하였습니다.')
