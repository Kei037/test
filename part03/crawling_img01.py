import requests
import os.path

# 파이썬 공식 홈페이지에서 이미지 링크 가져옴

url = 'https://www.python.org/static/img/python-logo@2x.png'
response = requests.get(url)

# 1. 파일 이름 가지고 오기
image_file_name = os.path.basename(url)  # 파일 이름 가져오기
print(image_file_name)  # python-logo@2x.png

# 2. 파일 저장. response.content
with open(f'./output_image/{image_file_name}', 'wb') as image_file:
    image_file.write(response.content)
    print('이미지 파일로 저장하였습니다.')
