# NumPy : 배열 데이터를 효과적으로 다룸
# 파이썬으로 과학 연산을 쉽고 빠르게 할 수 있게 만든 패키지.
# NumPy를 이용하면 파이썬의 기본 데이터 형식과 내장 함수를 이용하는 것보다 다차원 배열 데이터를 효과적으로 처리할 수 있음.
# NumPy 홈페이지 : https://numpy.org/

# 1. 배열생성하기.
# Numpy는 파이썬의 내장 모듈이 아니라서 별도로 설치

import numpy as np

# 배열 Array 이란 1) 순서가 있는 2)같은 종류의 데이터가 저장된 집합.
# Numpy를 이용해 배열을 처리하기 위해서는 우선 NumPy로 배열을 생성해야 함.

# 다양한 방법으로 배열을 생성하는 방법 보기

# 1) 시퀀스 데이터로부터 배열 생성하기. array()
# 시퀀스 데이터 seq_data를 인자로 받아 NumPy의 배열 객체 array object를 생성.
# arr_obj = np.array(seq_data)

# 정수 리스트로 배열 생성
data1 = [0, 1, 2, 3, 4, 5]
print(data1)  # [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print(a1)  # [0 1 2 3 4 5]
print(a1.dtype)  # data type이 int64

# 정수와 실수가 혼합된 경우
data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)  # [ 0.1  5.   4.  12.   0.5]
print(a2.dtype)  # float64.  정수와 실수가 혼합돼 있을 때 모두 실수로 변환.

# 숫자와 문자가 있는 경우
data3 = [0.1, 5, 4, 12, 'test']
a3 = np.array(data3)
print(a3)  # ['0.1' '5' '4' '12' 'test']
print(a3.dtype)  # <U32   -> 길이가 32인 유니코드 문자열

# array()에 직접 리스트를 넣어서 배열 객체도 생성 가능.
a3 = np.array([0.5, 2, 0.01, 8])
print(a3)  # [0.5  2.   0.01 8.  ]

# 다차원 배열의 생성 예.
a4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a4)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 2) 범위를 지정해 배열 생성. arange()
# arange() 를 이용해 NumPy 배열을 생성. 파이썬의 range() 와 사용방법이 비슷.
# arr_obj = np.arange([start,] stop[, step])
# start 부터 시작해서 stop 전까지 step만큼 계속 더해 Numpy 배열을 생성
# start가 0인 경우에는 생략가능
# step 이 1인경우 생략가능.

a1 = np.arange(0, 10, 2)
print(a1)  # [0 2 4 6 8]

a2 = np.arange(1, 10)
print(a2)  # [1 2 3 4 5 6 7 8 9]

a3 = np.arange(5)
print(a3)  # [0 1 2 3 4]

# Numpy 배열의 arange()를 이용해 생성한 1차원 배열에 reshape(m, n)을 추가하면 m * n 형태의 2차원 배열(행렬)로 변경
# 주의할 점은 arange()로 생성되는 배열의 원소 개수와 reshape(m, n)의 m * n 개수가 같아야함
a4 = np.arange(12).reshape(4, 3)
print(a4)

# NumPy 배열의 형태를 알기 위해서는 'nbarray.shape'를 실행.
print(a4.shape)  # (4, 3)

# 1차원 배열의 경우 '(n, )'처럼 표시
print(a1.shape)  # (5,)

# ndarray.linspace()
# 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 배열을 생성.
# arr_obj = np.linspace(start, stop[, num])
# linspace()는 start 부터 stop까지 num개의 배열을 같은 간격으로 생성. num을 지정하지 않으면 50이 기본값

a1 = np.linspace(1, 10, 10)
print(a1)  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
a2 = np.linspace(1, 10, 4)
print(a2)  # [ 1.  4.  7. 10.]  간격이 3

# 0부터 파이까지 동일한 간격으로 20개를 나눈 배열 생성
a3 = np.linspace(0, np.pi, 20)
print(a3)
# [0.         0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
#  0.99208189 1.15742887 1.32277585 1.48812284 1.65346982 1.8188168
#  1.98416378 2.14951076 2.31485774 2.48020473 2.64555171 2.81089869
#  2.97624567 3.14159265]

# 3) 특별한 형태의 배열 생성.
# 모든 원소가 0 혹은 1인 다차원 배열을 만들기 위해서는 zeros() 와 ones()를 이용

# 원소가 0이고 개수가 10개인 1차원 배열 생성.
a1 = np.zeros(10)
print(a1)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 3 * 4의 2차원 배열을 생성
a2 = np.zeros((3, 4))
print(a2)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

a3 = np.ones(5)
print(a3)  # [1. 1. 1. 1. 1.]

# 4) 배열의 데이터 타입 변환.
# 배열은 숫자뿐만 아니라 문자열도 원소를 가질 수 있음.

# 문자열이 원소인 배열 생성 예.
a1 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a1)  # ['1.5' '0.62' '2' '3.14' '3.141592']
print(a1.dtype)  # <U8. 데이터 형식이 유니코드이며 문자의 수는 최대 8개라는 것을 의미.

# NumPy 데이터의 형식.
# b : 불. bool
# i : 기호가 있는 정수. (signed) integer
# u : 기호가 없는 정수. unsigned integer
# f : 실수. floating-point
# c : 복소수. complex-floating point
# M : 날짜. datetime
# O : 파이썬 객체. (Python) objects
# S or a : 바이트 문자열. (byte) string
# U : 유니코드. Unicode

# 배열이 문자열(숫자 표시)로 돼 있다면 연산을 위해서는 문자열을 숫자(정수나 실수)로 변환해야 함.
# 형 변환은 astpye()로 가능
# num_arr = str_arr.astype(dtype)

# 실수가 입력된 문자열을 원소로 갖는 배열을 실수 타입으로 변환하는 예
str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
print(num_a1)  # [1.567 0.123 5.123 9.    8.   ]
print(str_a1.dtype)  # <U5
print(num_a1.dtype)  # float64

# 5) 난수 배열 생성
# NumPy에서 난수를 발생시킬 수 있는 다양한 함수가 있음
# rand() 함수를 이용하며 실수 난수를 요소로 갖는 배열을 생성
# randint() 함수를 이용하면 정수 난수를 요소로 갖는 배열을 생성
# rand_num = np.random.rand([d0, d1, ..., dn])
# rand_num = np.random.randint([low,] high [, size])

# rand() 함수는 [0, 1) 사이의 실수 난수를 갖는 배열을 생성.
# * [a, b)의 표현은 값의 범위가 a이상이고 b 미만 이라는 의미.

# randint() 함수는 [low, high) 사이의 정수 난수를 갖는 배열을 생성.
# size 는 배열의 형태 지정.
# low가 입력하지 않으면 0으로 간주.
# size가 입력하지 않으면 1로 간주.

a1 = np.random.rand(2, 3)
print(a1)
# [[0.25316051 0.89317248 0.13059639]
#  [0.07719349 0.74098886 0.14953911]]

a2 = np.random.rand()
print(a2)  # 0.764731264643677
print()

a3 = np.random.rand(2, 3, 4)
print(a3)
# [[[0.55321921 0.09329367 0.48692914 0.62449984]
#   [0.34787149 0.71475794 0.26332157 0.6183308 ]
#   [0.6192792  0.07923302 0.28153496 0.13910185]]
#
#  [[0.42923821 0.91757834 0.9492461  0.31893151]
#   [0.96585553 0.31617405 0.82746328 0.52779486]
#   [0.86085052 0.34890074 0.69848205 0.43751829]]]

a4 = np.random.randint(10, size=(3, 4))  # 0부터 9까지의 정수 난수를 요소로 가지는 3 * 4배열을 생성
print(a4)
# [[0 7 4 6]
#  [7 1 4 9]
#  [0 8 5 5]]

a5 = np.random.randint(1, 30)
print(a5)  # 15

a6 = np.random.randint(1, 30, 3)
print(a6)  # [16  4  1]

