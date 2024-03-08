import pprint
import requests
from bs4 import BeautifulSoup as bs

# 야후 이미지 검색 이용
# https://www.yahoo.com/ 에서 이미지 검색을 한 후 url을 들고 올 것

# 1. 이미지 태그 가져오기
url = 'https://images.search.yahoo.com/search/images;_ylt=AwrOtgccpOplEFAJa52JzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRmcgN5ZnAtdARmcjIDcDpzLHY6aSxtOnNiLXRvcARncHJpZAN0RlNUZWRrSlR2YWlBTWR5Mkhhb01BBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzUEcXVlcnkDbW92aWUEdF9zdG1wAzE3MDk4NzY1ODI-?p=movie&fr=yfp-t&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt'
response = requests.get(url)
soup = bs(response.content, 'html.parser')
# print(soup.prettify())

tag_images = soup.select('li.ld a > img')
# pprint.pprint(tag_images)

# 2. 이미지 저장
dir_save = './output_image/yahoo/'  # 저장 경로

for idx, tag in enumerate(tag_images):
    # print(tag.get('data-src'))
    response = requests.get(tag.get('data-src'))
    with open(f'{dir_save}{idx + 1}.png', 'wb') as image_file:
        image_file.write(response.content)
        print(f'{idx + 1} / {len(tag_images)}')
