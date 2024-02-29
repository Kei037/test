# 생성자와 소멸자
# 1. 생성자

# 값을 가진 인스턴스를 생성하기 위해 생성자를 이용
# 생성자는 인스턴스를 생성할 때 자동으로 호출되는 특별한 메소드
# 모든 클래스는 __init__() 이라는 이름을 가진 생성자를 가지고 있음
# __init__() 메소드(생성자)는 인스턴스가 생성될 때 자동으로 호출되기 때문에 인스턴스 변수의 초기화 용도로 사용

# **__init__
# 새로운 인스턴스가 만들어질때 자동으로 호출되는 메서드
# 생성자는 아님. 생성자는 '__new__'이고, 생성자가 객체를 메모리에 할당해서 리턴을 하는데,
# 리턴을 하기전에 __init__ 메소드를 호출
# __init__ 에서는 '새로운 속성을 추가하는 일' 을 해야함

class Candy:
    def __init__(self, shape, color):
        print('실행이 될까?')
        self.shape = shape
        self.color = color

satang = Candy('circle', 'brown')
print(satang.color)

# 2. 소멸자
# 인스턴스가 생성될 때 자동으로 호출되는 생성자와 마찬가지로
# 인스턴스가 소멸될 때 자동으로 호출되는 메소드
# 소멸자는 __del__()

class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다')

sample = Sample()

del sample  # 인스턴스가 소멸됩니다

# 매직 메서드 샘플
class Sample:
    def __int__(self):
        pass
    def __len__(self):
        return 6
    def __str__(self):
        return 'what?'

li = [1, 2, 3]
print(len(li))  # 3

sample = Sample()
print(len(sample))  # 6
print(sample)  # what
print()

# 클래스 메소드와 정적 메소드
# 1. 클래스 변수
# 클래스를 구현할 때 인스턴스마다 서로 다른 값을 가지는 경우에는 인스턴스 변수를 사용
# 모든 인스턴스 변수들은 self 키워드를 붙여서 사용
# 모든 인스턴스가 동일한 값을 사용할 때는 클래스 변수로 처리해서 모든 인스턴스들이 공유하도록 처리하는 것이 좋음
# 인스턴스 변수는 인스턴스마다 값을 별도로 저장해야 하지만 클래스 변수는 하나의 값을 모든 인스턴스가
# 공유하기 대문에 메모리 공간의 낭비를 막을 수 있음

# * self
# 관례적으로 모든 메소드의 첫 번째 매개변수 이름을 self로 지정
# self가 파이썬의 예약어는 아님
# self라는 명칭은 관례적으로 사용하는 단어일 뿐

class Korean:
    country = '한국'  # 클래스 변수 country

    def __init__(self, name, age, address):
        self.name = name  # 인스턴스 변수
        self.age = age
        self.address = address

print(Korean.country)  # 객체 생성전에도 사용 가능

man = Korean('홍길동', 35, '서울')
print(man.name)
# print(Korean.name)  # AttributeError: type object 'Korean' has no attribute 'name'

print(man.country)  # 인스턴스 man을 통한 클래스 변수 접근
print(Korean.country)  # 클래스 Korean을 통한 클래스 변수 접근
print()

man.country = '중국'
print(man.country)
print(Korean.country)
print()

print('객체 프로퍼티 생성과 동일한 이름의 클래스 변수')
man.country = '중국'  # 객체의 인스턴스 변수 생성
print(man.country)  # 중국. 클래스 변수가 아니라 인스턴스 변수를 불러옴. man 객체의 country 라는 인스턴스 변수와 country클래스 변수
print(man.__class__.country)  # 한국. 객체를 사용해서 클래스 변수 불러오기
print(Korean.country)

print('객체를 이용해서 클래스 변수 값 변경')
man.__class__.country = '영국'
print(Korean.country)  # 영국
print()

print('클래스를 이용해서 클래스 변수 값 변경')
Korean.country = '미국'
print(Korean.country)  # 미국

man2 = Korean('홍길동2', 35, '서울')
print(man2.country)  # 미국
print(Korean.country)  # 미국
print()

# 클래스 변수는 클래스를 통해서 접근하는 것이 권장사항

# 2. 클래스 메소드
# 클래스 변수를 사용하는 메소드를 의미
# 주요 특징
# 1. 인스턴스 혹은 클래스로 호출
# 2. 생성된 인스턴스가 없어도 호출할 수 있음
# 3. @classmethod 데코레이터 decorator 를 표시하고 작성
# 4. 매개변수 self를 사용하지 않고 cls를 사용
# 클래스 메소드는 self를 사용하지 않기 때문에 인스턴스 변수에 접근할 수 없지만,
# cls를 통해서 클래스 변수에 접근할 수 있음

class Korean:
    country = '한국'  # 클래스 변수 country

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print('국내여행입니다.')
        else:
            print('해외여행입니다.')

Korean.trip('한국')
Korean.trip('미국')
print()


# 3. 정적 메소드
# 1) 인스턴스 또는 클래스로 호출
# 2) 생성된 인스턴스가 없어도 호출 가능
# 3) @staticmethod 데코레이터 decorator를 표시하고 작성
# 4) 반드시 작성해야 할 매개변수가 없음

# 정적 메소드는 self와 cls를 모두 사용하지 않기 때문에 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메소드를
# 정의하는 경우에 적절
# 정적 메소드는 클래스에 소속이 되어 있지만, 인스턴스에는 영향을 주지 않고 또 인스턴스로 부터 영향을 받지도 안흥ㅁ

class Korean:
    country = '한국'  # 클래스 변수 country

    @staticmethod
    def slogan():
        print('Imagine your korea')

Korean.slogan()  # Imagine your korea

# 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스

class Bag:
    count = 0  # 클래스 변수

    def __init__(self):  # 생서자가 실행될 때 마다 증가
        Bag.count += 1
        # __class__.count += 1

    @classmethod
    def sell(cls):  # 판매시 감소
        cls.count -= 1

    @classmethod
    def remain_bag(cls):  # 남은 가방의 갯수 반환
        return cls.count

print(f'현재 가방: {Bag.remain_bag()}개')  # 0개
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방: {Bag.remain_bag()}개')  # 0개
bag1.sell()
bag2.sell()
print(f'현재 가방: {Bag.remain_bag()}개')  # 0개
print()


# 상속
# 1. 상속이란?
# 어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 만들 수 있슴
# 다른 클래스의 기능을 물려받을 때 상속받는다는 표현을 사용
# 그래서 상속 관계에 있는 클래스를 표현할 때 부모 클래스와 자식 클래스하는 말을 사용

# 부모 클래스 : 상속해 주는 클래스 / 슈퍼 클래스 super class , 기반 클래스 base class
# 자식 클래스 : 상속 받는 클래스 / 서브 클래스 sub class, 파생 클래스 derived class

# 2. 상속 관계 구현
# 기본적으로 두 클래스가 상속 관계에 놓이려면 IS-A 관계가 성해야 함
# IS-A 관계란 '~은 ~ 이다.'로 해설할 수 있는 관계를 의미
# '학생은 사람이다 Student is a Person'처럼 해석되는 것이 IS-A 관계
# 이때 Student 는 서브 클래스가 되고, Person은 슈퍼 클래스가 됨

# 컴퓨터 과학에서 상속은 is-a 관계를 갖고 있을 때 사용.
# is-a 관계는 '직원은 사람이다 employee is-a person' 또는 '자동차는 차량이다 car is-a vehicle'이라고 부르며,
# has-a 관계는 컴퓨터 과학 용어도 '그릇이 스쿱을 갖는다 Bowl has-a Scoop'라고 부르고,
# has-a 관계는 상속이 아니라 구성 Composition으로 구현함.
#
# 객체 지향 프로그래밍을 처음 접하면 두 클래스가 어떤 관계를 갖고 있을 때, 반드시 상속 관계가 만들어져야 한다고 생각하는 경우가 많음.
# is-a 관계를 가질 경우에는 상속, has-a 관계를 가질 경우에는 구성을 사용한다고 구분해서 생각하면
# 어떤 경우에 상속등을 활용해야 하는 지 조금 더 쉽게 구분.

# 상속의 기본적인 형식
# class 슈퍼 클래스 :
#   본문
#
# class 서브 클래스(슈퍼 클래스):
#   본문

# 서브 클래스를 구현할 때는 괄호 안에 어떤 슈퍼 클래스를 상속 받는지 명시
# 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용할 수 있음

class Person:  # 슈퍼 클래스
    def __init__(self, name: str):
        self.name = name

    def eat(self, food: str) -> None:
        print(f'{self.name}가 {food}를 먹습니다.')

class Student(Person):
    def __init__(self, name: str, school: str):
        super().__init__(name)  # 슈퍼 클래스의 생성자 실행
        self.school = school

    def study(self) -> None:
        print(f'{self.name}는 {self.school}에서 공부를 합니다.')

potter = Student('해리포터', '호그와트')
potter.eat('감자')  # 해리포터가 감자를 먹습니다.
potter.study()     # 해리포터는 호그와트에서 공부를 합니다.


# 3. 서브 클래스의 __init__()
# 서브 클래스의 생성자를 구혀할 때는 반드시 슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야 함
# super라는 키워드는 슈퍼 클래스를 의미

class Computer:  # 슈퍼 클래스
    def __init__(self):
        print('슈퍼 클래스가 생성자가 실행되었습니다.')

class NoteBook(Computer):
    def __init__(self):
        super().__init__()
        print('서브 클래스의 생성자가 실행되었습니다.')

n = NoteBook()


# 4. 서브 클래스의 인스턴스 자료형
# 슈퍼 클래스 객체는 슈퍼 클래스의 인스턴스
# 그에 비해 서브 클래스 객체는 서브 클래스의 인스턴스이면서 동시에 수퍼 클래스의 인스턴스
# 즉 서브 클래스 Student의 객체는 서브 클래스 Student의 인스턴스 이면서
# 동시에 슈퍼 클래스 Person의 인스턴스

# 어떤 객체가 어떤 클래스의 인스턴스인지 확인하기 위해서 isinstance() 함수를 사용
# 객체가 인스턴스 일 경우에는 True 아니면 False 반환
# isinstance(객체, 클래스)
print(isinstance(potter, Student))  # True
print(isinstance(potter, Person))   # True
print()

# 원두 (bean)를 저장하는 Coffee 클래스와 원두(bean)에 물을 섞은 Espresso 클래스를 상속
class Coffee:
    def __init__(self, bean: str):
        self.bean = bean

    def coffee_info(self):
        print(f'원두: {self.bean}')

class Espresso(Coffee):
    def __init__(self, bean: str, water: str):
        super().__init__(bean)  # 슈퍼클래스의 생성자 실행
        self.water = water

    def espresso_info(self):
        super().coffee_info()  # 슈퍼클래스의 메소드 실행
        print(f'물: {self.water}ml')

class Americano(Espresso):
    def __init__(self, bean: str, water: str, more_water: str):
        super().__init__(bean, water)
        # Espresso.__init__(self, bean, more_water) # 클래스이름으로도 접근 가능. 객체를 매개변수로 전달
        self.more_water = more_water

    def americano_info(self):
        super().espresso_info()  # 슈퍼클래스의 메소드 실행
        # Espresso.espresso_info(self) # 클래스이름으로도 접근 가능. 객체를 매개변수로 전달
        print(f'물 더: {self.more_water}ml')

coffee = Espresso('콜롬비아', '30')
coffee.espresso_info()
# 원두: 콜롬비아
# 물: 30ml
print()

coffee = Americano('파나마', '20', '200')
coffee.americano_info()
# 원두: 파나마
# 물: 20ml
# 물 더: 200ml
print()

Espresso.espresso_info(coffee)  # 인스턴스 메서드이지만 클래스 이름으로 호출 가능. 대신 객체를 매개 변수 self로 전달해야함






