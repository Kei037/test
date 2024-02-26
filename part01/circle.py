"""
1. 파일명: circle.py
2. 개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area()함수
3. 작성자: 홍길동
4. 작성일: 2022-08-25
"""
# 삼중 큰 따옴표(""")는 여러 줄의 주석을 만들때 사용

# math 모듈 포함 : #은 한 줄 주석을 사용
import math

# get_area() 함수 정의
def get_area(radius): # 파이썬은 표기법으로 카멜법 보다는 언더바법을 선호.
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2)
    return area

# 1) 클래스안에 있는 메서드와 다르게 독립적으로 함수를 사용할 수 있음
# 2) 표기법은 언더바법을 사용
# 3) 데이터타입이 없음

radius = 1.5
# get_area() 함수 호출 결과를 area 변수에 저장
area_result = get_area(radius)
print(area_result)
print(get_area.__doc__) # get_area의 Docstring 확인
print()


