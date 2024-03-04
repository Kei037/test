# CSV 파일 입출력

# 1. CSV 파일이란?
# Comma Separated Values 의 약자로 '쉼표로 분리한 값들'
# 데이터베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식
# 내부는 실제 쉼표(,)를 이용해서 모든 항목이 구분되어 있으며
# 쉼표로 구성된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
# 메모장에서는 텍스틀, 엑셀에서는 각 셀로 나누어서 보임

# UTF-8 형식으로 저장된 CSV의 경우, 엑셀에서는 버젼에 따라서 기본읽기로는 한글이 깨지는 경우가 있음.
# 한컴 Cell에서는 에러없이 잘 열림

# 2. CSV 파일 읽기
# CSV 파일은 쉼표(,)로 데이터가 구분되어 있어서 문자열 처리 메소드를 활용하면
# 별도의 외부 모듈이 없어도 충분히 읽을 수 있음
# 1) 한 줄에 한 데이터가 있기 때문에 readline() 메소드로 한 줄씩 읽음
# 2) 쉼표(,)로 분리하기 위해서 split() 메소드를 이용

student_list = []
with open('./input/학생명단.csv', 'rt', encoding='cp949') as file:
    file.readline()  # 학번, 이름, 주소, 연락처 (첫번째 줄을 먼저 읽어와 밑에서 안 읽기위해 실행)
    while True:
        line = file.readline()
        if not line:  # 더 이상 읽을 내용이 없으면 반복문을 빠져 나옴
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)
print()

# CSV 파일을 사용하다 보면 간혹 큰 따옴표(")를 이용해서 텍스트를 묶는 경우가 있음
# 큰 따옴표를 제거하기 위해서 회원명에 추가로 strip() 메소드를 사용

member_list = []
with open('./input/회원명단.csv', 'rt', encoding='cp949') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')  # 큰 따옴표를 제거
        member_list.append(member)
print(member_list)

# member[0]에는 큰 따옴표가 포함된 회원명이 저장되어 있기 때문에 member[0].strip('"') 으로
# 큰 따옴표를 제거

# 영어는 문제가 없는데 한글의 경우 표현하는 방식이 2가지
# cp949 : 윈도우의 기본 인코딩. 예전방식. 한글에만 특수화된 한국에서만 사용. 모든 한글을 표현하지 못함
# utf-8 : 파이참 기본 인코딩. 상대적으로 새로운 방식. 한글 및 기타 외국어 문자를 하나의 인코딩으로 모두 표현하기 개발