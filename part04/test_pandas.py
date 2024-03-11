# pandas 라이브러리 : 파이썬에서 데이터 분석과 처리를 쉽게 처리할 수 있게 도와줌.,

# pandas 는 numpy를 기반으로 만들어졌지만 좀 더 복잡한 데이터 분석에 특화
# numpy가 같은 데이터 타입의 배열만 처리할 수 있는데 반해 pandas는 데이터 타입이 다양하게 섞여 있을 때도 처리 가능

# 공식 홈페이지 : https://pandas.pydata.org/

# 1. 구조적 데이터 생성하기

# 1) Seroes를 활용한 데이터 생성
import pandas as pd

# pandas에서 데이터를 생성하는 가장 기본적인 방법은 Series()를 이용하는 것.
# Series()를 이용하면 Series형식의 구조적 데이터(라벨을 갖는 1차원 데이터)를 생성할 수 있음.
# 다음은 Series()를 이용해 Series형식의 데이털르 생성하는 방법.
# s = pd.Series(seq_data)
# Series()의 인자로는 시퀀스 데이터가 들어감
# 시퀀스 데이터로는 리스트와 튜플 타입의 데이터를 모두 사용할 수 있지만 주로 리스트 데이터를 이용

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
