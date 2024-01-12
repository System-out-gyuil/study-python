# 인간(부모)
# 이름, 나이
# 걷기(walk)
# '두 발로 걷습니다' 출력

# Person 클래스 생성(부모)
class Person:
    # 타입 지정 힌트, ex) name 에는 string 타입, age 에는 int 타입이라는 힌트
    def __init__(self, name: str, age: int):
        # self : 자기 자신을 참조하는 매개변수, 자바의 This객체, __new__ 또는 __init__ 등
        # 앞뒤로 밑줄 두개가 붙은 메소드는 스페셜 메소드 또는 매직 메소드라고 부른다.
        self.name = name
        self.age = age

    # 메소드 선언
    def walk(self):
        print('두 발로 걷습니다')
        # init의 name과 age를 참조해(?) 사용
        print(f'{self.name}, {self.age}')

# 원숭이(자식)
# 이름, 나이, 동물원 이름
# 걷기(walk)
# '두 발로 걷습니다', '네 발로 걷습니다' 출력

# Monkey 클래스 선언(자식)
class Monkey(Person):

    def __init__(self, name, age, zoo):
        # super() 함수를 이용해 부모 클래스의 __init__을 가져옴
        super().__init__(name, age)
        # 그 이후 zoo를 추가
        self.zoo = zoo

    def walk(self):
        # super() 함수로 부모 클래스의 walk 메소드 사용
        super().walk()
        print(f'{self.zoo}')
        print('네 발로 걷습니다')

person = Person('name', 10)
person.walk()

monkey = Monkey('monkey_name', 10, 'some where')
monkey.walk()