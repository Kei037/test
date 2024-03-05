# 대구광역시_맛집
# 공공데이터 포탈에서 '대구광역시_맛집' 검색 (키사용이 없음)
# https://www.data.go.kr/data/15057236/openapi.do
# 중구의 맛집 목록을 json 타입으로 받아서 처리

# 1. 음식카테고리 출력
# {'한식', '일식', '세계요리', '중식', '전통차/커피전문점', '특별한 술집', '디저트/베이커리', '양식'}

# 2. 일식의 음식점명, 연락처, 메뉴 출력
# --------------------
# 음식점명: 종로초밥
# 연락처: 053-252-0321
# 메뉴: 광어회 50,000원 <br />모둠회 40,000원 <br />무침회 20,000원<br />
# --------------------
# 음식점명: 삼삼구이초밥
# 연락처: 053-425-3392
# 메뉴: 회덮밥 9,000원 <br />미주구리 30,000원 <br />점심특선 6,000원<br />
# --------------------
import urllib.request as request
import json
from typing import List

# 대구푸드 API 정보(대구푸드 맛집정보)
#
# https://www.daegufood.go.kr/kor/api/ajax.html?mode=json&addr=중구
#
# parameter의 각 역할 설명
# ' 필수 파라미터
# ' mode: json
# ' addr : 지역(중구,동구,남구 등등),
#
# '선택 파라미터
#
# 위의 URL에 각 parameter를 전송 하게 되면  각 항목에 맞는 데이터가 json 형식으로 리턴 됩니다.
#
# 1차
# status : 상태값 (DONE 리턴)
# total : 총 데이터수
#
# 2차(배열)
# data -> cnt, OPENDATA_ID, GNG_CS, FD_CS, BZ_NM, TLNO, MBZ_HR, SEAT_CNT, PKPL, HP, PSB_FRN, BKN_YN,
# INFN_FCL, BRFT_YN, DSSRT_YN, MNU, SMPL_DESC, SBW, BUS
#
# cnt: 순번
# OPENDATA_ID : 고유 번호
# GNG_CS : 주소
# FD_CS : 음식카테고리
# BZ_NM : 음식점명
# TLNO : 연락처
# MBZ_HR : 영업시간
# SEAT_CNT : 좌석수
# PKPL : 주차장
# HP : 웹사이트
# PSB_FRN : 가능언어
# BKN_YN : 예약가능여부
# INFN_FCL : 놀이시설여부
# BRFT_YN : 조식여부
# DSSRT_YN : 후식여부
# MNU : 메뉴
# SMPL_DESC : 설명
# SBW : 지하철 오시는길
# BUS : 버스 오시는길

# https://www.data.go.kr/data/15057236/openapi.do

url: str = f'https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr=%EC%A4%91%EA%B5%AC'
# print(url)

json_data = request.urlopen(url).read()
dict_data = json.loads(json_data)
# print(dict_data)
# print(dict_data['total'])

# 음식카테고리 출력
food_catagory: set = set()
for data in dict_data['data']:
    food_catagory.add(data['FD_CS'])
print(food_catagory)
print()
for data in dict_data['data']:
    if data['FD_CS'] == '일식':
        print(f'음식점명: {data["BZ_NM"]}')
        print(f'연락처: {data["TLNO"]}')
        print(f'메뉴: {data["MNU"]}')
        print('-' * 20)

# 음식점명: 종로초밥
# 연락처: 053-252-0321
# 메뉴: 광어회 50,000원 <br />모둠회 40,000원 <br />무침회 20,000원<br />
# --------------------

# 3. csv 파일로 저장
# 파일명 : daegu_food_jonggu_list.csv
# 인코딩 : utf-8
# 헤더 : '음식카테고리', '음식점명', '연락처', '메뉴'
jp_food_list: List[dict] = list()
name_list: List[str] = ['음식카테고리', '음식점명', '연락처', '메뉴']
for data in dict_data['data']:
    if data['FD_CS'] == '일식':
        jp_food: dict = dict()
        jp_food['음식카테고리'] = data["FD_CS"]
        jp_food['음식점명'] = data["BZ_NM"]
        jp_food['연락처'] = data["TLNO"]
        jp_food['메뉴'] = data["MNU"]
        jp_food_list.append(jp_food)
# print(jp_food_list)

import csv

with open('./output/daegu_food_jonggu_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=name_list)
    writer.writeheader()
    for data in jp_food_list:
        data: dict
        writer.writerow(data)
print('daegu_food_jonggu_list.csv 파일이 생성 되었습니다.')