# 클래스와 객체
# 1. 객체의 개념
# 개발을 하다 보면 정수나 실수 또는 문자열 등 기본적인 자료형으로 표현하기 힘든 것들이 존재
# 예를 들어 어떤 게시글을 파이썬으로 표현을 한다면
# 게시글 번호, 제목, 작성자, 비밀번호, 내용, 최초작성일자, 최종수정일자, 조회수가 필요한데
# 이를 손쉽게 관리 하려면 8개의 항목을 하나의 이름을 가진 객체 object로 만들어서 사용하는 것이 좋다

# 2. 클래스의 개념
# 클래스 class를 한 마디로 정의하면 객체를 만드는 도구
# 하나의 클래스를 만들어 두면 그 클래스를 통해서 (동일한 구조를 가진) 여러 개의 객체를 만들수 있슴
# 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질수 있슴
# 인스턴스 instance 역시 클래스를 이용해서 생성한 객체를 가르키는 용어

# 객체와 인스턴스의 미묘한 차이
# 1) 와플머신 클래스로 만든 와플은 객체 object
# 2) 와플은 와플머신 클래스의 인스턴스 instance

# 3. 클래스 정의
# 클래스 정의 방법
# 1) class 키워드로 클래스를 정의
# 2) 클래스 이름은 Upper Camel Case 규칙을 다름
# 파이썬은 변수나 함수의 이름을 네이밍할 때 언더바 (_)를 이용해 단어를 연결하는 Snake Case 방식을 사용하지만
# 클래스는 Upper Camel Case 규칙을 따름
# print + member : printMember  1) print_member 2) printMember 3) PrintMember

# 클래스는 다음과 같은 형식으로 정의
# class 클래스 :
#   본문

# 4. 객체 생성
# 클래스가 정의되었다면 다음과 같은 형식으로 객체를 생성
# 객체 = 클래스()

# 2개의 객체를 만들고 싶으면
# 객체1 = 클래스()
# 객체2 = 클래스()

# 5. 클래스 정의와 객체 생성
class WaffleMachine:  # WaffleMachine 이라는 클래스 정의
    pass

waffle1 = WaffleMachine()  # WaffleMachine 이라는 클래스를 이용해 waffle이라는 객체 생성
waffle2 = WaffleMachine()

print(waffle1)  # <__main__.WaffleMachine object at 0x100aceec0>
# 메모리의 0x100aceec0 번지에 저장된 WaffleMachine의 객체라는 의미
print(waffle2)
print()


# 클래스의 구성
# 1. 클래스의 기본 구성
# 객체를 만들어내는 클래스는 객체가 가져야 할 값과 기능을 가지고 있어야 함
# 값은 변수, 기능은 함수
# 정리하면 클래스는 변수와 함수로 구성된다고 볼 수 있음

# 클래스를 구성하는 변수는 1) 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 '클래스 변수'와
# 2) 모든 인스턴스들이 개별적으로 가지는 변수인 '인스턴스 변수'로 분리됨

# 클래스를 구성하는 함수는 메소드 method라고 하고
# 1) 클래스 메소드 2) 정적 메소드 3) 인스턴스 메소드로 분리

# 2. 인스턴스 변수와 인스턴스 메소드
# 인스턴스 변수란 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수
# 모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줌
# 인스턴스 메소드란 인스턴스 변수를 사용하는 메소드
# 인스턴스 메소드는 반드시 첫 번째 매개변수로 self를 추가해야 함

class Person:  # Person 클래스를 정의
    # 첫 번째 매개변수가 self 이므로 인스턴스 메소드
    # 모든 인스턴스는 who_am_i() 메소드를 호출할 수있음
    # 매개변수 self에는 메서드를 호출하는 인스턴스가 전달
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달
    def who_am_i(self, name, age, tel, address):
        # 인스턴스 변수 = 매개변수 . 모든 인스턴스 변수는 최초에 값이 대입되는 시점에 알아서 생성
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()  # 인스턴스 boy가 생성. 클래스의 생성자가 호출
# print(boy.name)  # AttributeError: 'Person' object has no attribute 'name'
print(boy.who_am_i('john', 15, '123-1234', 'toronto'))  # 인스턴스 메서드 호출
print(boy.name)  # john
print(boy.age)  # 15
print(boy.tel)  # 123-1234
print(boy.address)  # toronto
print()

# 클래스에 없는 속성도 추가가 가능함. 다른 언어의 객체와는 다른 방식.
boy.email = 'test@test.com'
print(boy.email)  # test@test.com

# CPU, RAM, VGA, SSD를 구성요소로 가지고 있는 Computer 클래스를 사용해서 인스턴스를 생성하는 프로그램.
# Computer 클래스는 각 구성요소의 값을 저장할 수 있는 set_spec() 메서드와 구성요소의 값을
# 출력할 수 있는 hardware_info() 메소드로 구성

class Computer:
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')

desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX1060', '512GM')
desktop.hardware_info()
print(desktop.cpu)

notebook = Computer()
notebook.set_spec('i5', '8G', 'MX300', '256GB')
notebook.hardware_info()
print(notebook.cpu)

