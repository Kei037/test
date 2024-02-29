# 파일 입출력의 개요
# 파일 입출력 : 컴퓨터에 저장된 파일을 읽어 들이는 것은 물론 파일을 생성해서 컴퓨터에 저장하는 것도 가능
# 파일 입력 input : 기존의 파일 내용을 읽어 들이는 것
# 파일 출력 output : 기존 파일에 새로운 내용을 추가하거나 새로운 파일을 생성하는 것

# 1. 파일 열기
# 입출력 파일을 지정하는것을 의미. 파일 객체 생성
# 파일 입력과 파일 출력 모두 반드시 파일 열기 작업을 가장 먼저 수행

# 파일객체 = open(파일명, 모드)

# 1) 파일명
# 입출력 작업을 수행할 파일을 의미
# 파일명만 작성할 수도 있고 경로를 함께 작성할 수도 있음

# 파일명만 작성하는 경우 : 파이썬 소스 파일과 같은 경로에 존재하는 경우
# open('sample.txt')

# 전체 경로를 작성하는 경우 : 빈도가 적음
# open('C:/sample.txt')

# 현재 디렉터리(.)를 기준으로 경로를 결정
# open('./sample.txt')
# open('./input/hello.txt')

# 상위 디렉터리(..)를 기준으로 경로를 결정
# open('../sample.txt')

# 2) 모드
# 입력
# r (read) 읽기
# 출력
# w (write) 쓰기 (파일이 있으면 새로 생성, 없으면 새로 생성)
# a (append) 추가 (파일이 있으면 추가, 없으면 새로 생성)
# x (exclusive) 베타적 추가 (파일이 있으면 오류, 없으면 새로 생성)

# 파일의 종류
# t (text) 텍스트 파일 : 메모장으로 열수 있는파일
# b (binary) 바이너리 파일 (텍스트 파일 외의 모든 파일)

# 2. 파일 닫기
# 파일을 더 이상 사용하지 않거나 프로그램을 종료하고자 할 때
# 파일객체.close()

# 3. 파일의 생성
file = open('./output/my_file.txt', 'wt')  # 빈 파일 생성
print('my_file.txt 파일이 생성되었습니다.')
file.close()

# 텍스트 파일을 새로 만들수 있는 모드인 wt 모드를 사용하여 my_file.txt라는 이름의
# 텍스트 파일을 output 이라는 디렉터리에 생성하는 코드

# with 문
# close() 메소드를 자동으로 호출할 수 있는 문법을 제공
# with문을 사용하면 with문이 끝날 때 언제나 close() 메소드가 자동으로 호출하기 때문에
# 별도의 예외 처리를 하지 않더라도 프로그램이나 파일의 에러로 close()가 호출이 안되는
# 상황을 방지

# 기본 구성
# with open(파일명, 모드) as 파일객체:
#   파일처리코드

with open('./output/my_file_1.txt', 'wt') as file:
    print('my_file_1.txt 파일이 생성되었습니다.')

# 파일 출력 output

# 1. 텍스트 파일 생성하기
file = open('./output/hello.txt', 'wt')

# hello.txt에 글쓰기
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')  # 진행 상황을 알기 위해서 화면 출력

file.close()

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a 모드
file = open('./output/hello.txt', 'at')

file.write('Hello.\n')
file.write('Nice to meet you. \n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')
file.close()

# utf-8 로 문서 작성하기 (인코딩을 ansi -> utf-8)
file = open('./output/한글파일.txt', 'w', encoding='utf-8')
file.write('오늘 나는 학교에 갔습니다.')
file.close()

# 1. 텍스트 파일 읽기

# 1) read() 메소드
# file.read(size)
# 파일로부터 데이터를 읽어 들이는 메소드
# 텍스트 모드와 바이너리 모드에서 다른 방식으로 동작

# 반환값 : 텍스트 모드 / 읽어 들인 문자열, 바이너리 모드 / 읽어 들인 바이트열
# 매개변수 size : 텍스트 모드 / 읽어 들일 최대 문자의 개수, 바이너리 모드 / 읽어 들일 최대 바이트 수
# 매개변수 size 생략 : 파일 전체 읽음
# 파일의 끝에 도달 : 빈 문자열 ('') 반환
file = open('./output/hello.txt', 'rt')

str = file.read()  # 파일 전체를 한 번에 읽어 들임
print(str, end='')

file.close()

# 2) readline() 메소드
# 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈 문자열('')을 읽어 들임
# 반복문을 이용해서 여러 번 읽어 들어야 파일 전체를 읽어 들일 수 있음
print()
file = open('./input/hello.txt', 'rt', encoding='cp949')
while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')
file.close()

# 3) readlines() 메소드
# 라인 line 하나가 아니라 전체 라인 lines을 모두 읽어 각 라인 line 단위로 리스트에 저장하는 메소드
print()
file = open('input/hello.txt', 'rt' , encoding='cp949')

line_list = file.readlines()
print(line_list) # ['안녕하세요.\n', '반갑습니다.\n', 'Hello.\n', 'Nice to meet you.\n']
for line in line_list:
    print(line, end='')

file.close()

# enumrate() 함수를 이용하면 라인 번호 line number 도 함께 출력할 수 있슴
print()
file = open('input/hello.txt', 'rt', encoding='cp949')

line_list = file.readlines()
for no, line in enumerate(line_list):
    print('{} {}'.format(no + 1, line), end='')

file.close()

# sys 모듈을 이용하면 보다 쉽게 파일을 읽을 수 있슴
# sys 모듈에는 표준 입출력을 위한 stdin과 stdout 객체가 포함
# stdout은 출력을 위한 객체이며 화면 출력 메소드인 write()와 writelines() 메소드를 사용할 수 있슴
# writelines() 메소드를 사용하면 리스트와 같은 반복 가능한 객체의 각 요소를 한 줄씩 자동으로 출력
print()
import sys

file = open('input/hello.txt', 'rt', encoding='cp949')

line_list = file.readlines()
sys.stdout.writelines(line_list)

file.close()

