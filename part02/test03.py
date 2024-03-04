# CSV 파일 입출력

# 1. CSV 파일이란?
# Comma Separated Values 의 약자로 '쉼표로 분리한 값들'
# 데이터베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식
# 내부는 실제 쉼표(,)를 이용해서 모든 항목이 구분되어 있으며
# 쉼표로 구성된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
# 메모장에서는 텍스틀, 엑셀에서는 각 셀로 나누어서 보임

# * 장점
# 단순함
# 많은 프로그램에서 지원을하고, 텍스트 편집기에서 볼 수 있으며, 스프레드 시트 데이터를 표현하는 간단한 방법

# * 주의점
# 텍스트로 구성이 되어 있어서, 각 줄에 대해 split(',')을 호출하여 쉼표로 구분된 값에서 문자열 리스트를 얻을 수 있음.
# 그러나 CSV 파일의 모든 쉼표가 두 셀의 경계를 나타내지 않고, 값의 일부인 경우도 있음.
# 이런 잠재적인 문제 때문에 CSV 파일을 읽거나 쓸 때 CSV 모듈을 사용하는 것이 좋음.

# * 단점
# 값에 유형이 없음. 모든것은 다 문자열
# 글꼴 크기나 색상을 설정할 수 없음.
# 여러 개의 워크시트를 가질 수 없음.
# 셀의 너비나 높이를 지정할 수 없음
# 셀을 병합할 수 없음
# 그림이나 차트를 포함 할 수 없음.

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

# 3. csv 모듈로 CSV 파일 생성하기
# import csv 를 통해서 csv 파일을 쉽게 처리할수 있는 csv 모듈을 사용

import csv

# w모드로 열고 생성된 파일 객체를 csv.writer() 메소드에 전달
# 그러면 CSV파일을 생성할 수 있는 객체가 생성되는데 이 객체를 이용해서
# writerow() 메소드를 호출하면 CSV 파일에 데이터를 저장할 수 있음

with open('./output/차량관리_01.csv', 'w') as file:
    # delimiter=',' : 콤마로 데이터 구분. tab을 사용하는 경우도 있음.tsv.
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_writer.writerow([2, '25러1234', '2020-10-20,14:10'])
    csv_writer.writerow([3, '28러1234', '2020-10-20,14:20'])
print('차량관리_01.csv 파일이 생성되었습니다.')

# 불필요한 라인이 하나씪 추가되어 있는데 이를 막기 위해서 새로운 라인을
# 추가하지 못하도록 newline 옵션을 사용할 수 있음
# 줄 바꿈이 되지 않도록 newline 옵션에 빈 문자열을 지정하고 이를 코드에 반영

with open('./output/차량관리_02.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_writer.writerow([2, '25러1234', '2020-10-20,14:10'])
    csv_writer.writerow([3, '28러1234', '2020-10-20,14:20'])
print('차량관리_01.csv 파일이 생성되었습니다.')
print()

# 4. csv 모듈로 CSV 파일 읽기

# CSV 파일을 읽기 위해서는 r모드로 파일을 열고 생성된 파일 객체를 csv.reader() 메소드에 전달
# csv.reader() 메소드는 CSV파일을 읽고 그 내용을 읽고 저장한 객체 iterator를 반환

with open('./output/차량관리_02.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_reader:
        print(line)
print()

# csv 묘듈을 사용해서 csv 파일을 읽으려면 다른 텍스트 파일처럼 open() 함수로 파일을 열어야 함
example_file = open('./input/example.csv')  # mode를 생략하면 rt가 기본값

# read() 대신 csv.reader() 함수에 전달. reader() 객체가 반환.
example_reader = csv.reader(example_file)

# list로 변환하여 값에 접근
print(example_reader)
example_data = list(example_reader)
print(example_data)
print(example_data[0][1])  # Apples

example_file.close()
print()

# 2. for 반복문을 활용해 reader 객체로부터 데이터 읽기
# CSV 파일이 큰 경우에는, 전체 파일을 한 번에 메모리에 로드하지 않고
# for 반복문에서 reader 객체 사용
# reader 객체는 한 번만 사용가능하기 때문에 다시 사용할려면 새로 reader 객체 생성.
example_file = open('./input/example.csv')
example_reader = csv.reader(example_file)
# print(example_reader)
print('example.csv 출력')
for row in example_reader:
    # 각 행의 번호를 얻으려면 reader 객체의 line_num 변수를 사용.
    print(f'Row #{str(example_reader.line_num)} {str(row)} {str(row[0])}')
example_file.close()
print('=' * 20)

# 3. writer 객체
# writer 객체를 사용하면 데이텅를 csv 파일에 저장할 수 있음.

output_file = open('./output/output.csv', 'w', newline='')  # newline=''  : 빈줄이 들어가는 것 방지
output_writer = csv.writer(output_file)  # csv.writer 에 전달할 객체 생성.
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])  # writer.writerow() : 리스트에 인자를 전달.
output_writer.writerow(['hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3, 3.141592, 4])
output_file.close()

# 4. 키워드 인지 delimiter와 lineterminator
# 쉼표가 아닌 탭문자로 셀을 구분하고 줄 간격을 한 줄씩 띄우려는 상황을 가정.
# 구분자 (delimiter)와 줄 끝 문자 (lineterminator)를 변경.
# delimiter의 기본값은 쉼표이고, lineterminator의 기본값은 개행문자
# 셀들이 탭으로 구분되어 있기 때문에 탭으로 구분된 값을 의미하는 .tsv 파일 확장자 사용
csv_file = open('./output/example.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['apples', 'oranges', 'grapes'])
csv_writer.writerow(['eggs', 'bacon', 'ham'])
csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csv_file.close()
print()

# 5. CSV 객체의 DictReader와 DictWriter
# 헤더 행이 있는 csv 파일의 경우 reader나 writer 객체보다 DictReader나 DictWriter 객체를 사용하는 것이 작업하기 편함.
example_file = open('./input/example_with_header.csv')
example_dict_reader = csv.DictReader(example_file)
# DictReader 객체는 1) row를 딕셔너리 객체로 설정하고, 2) 첫 번째 행에 있는 정보를 건너 뜀.
# 3) 첫 번째 행에 있는 정보를 키값으로 사용
print('example_with_header.csv 출력')
for row in example_dict_reader:
    print(f'{row["Timestamp"]}, {row["Fruit"]}, {row["Quantity"]}')
print('=' * 20)
example_file.close()

# 헤더 정보가 없는 파일의 경우 DictReader() 생성자의 두 번째 인자로 헤더 이름을 지어서 전달.
example_file = open('./input/example.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
print('example.csv 출력')
for row in example_dict_reader:
    print(f'{row["time"]}, {row["name"]}, {row["amount"]}')
print('=' * 20)

# DictWriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용
output_file = open('./output/output_with_header.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader()를 호출
output_dict_writer.writeheader()
# writerow() 메서드를 호출하여 각 행을 쓸 수 있는데, 이 때 딕셔너리를 사용
# 딕셔너리의 키는 헤더이고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어감
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})  # 누락된 키는 빈 상태로 나옴
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})  # 순서는 중요하지 않음
output_file.close()






