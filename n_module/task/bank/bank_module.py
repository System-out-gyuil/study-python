# 계좌번호, 휴대폰 번호 중복 검사에 필요한 메소드
def check(*, key: str, value: str) -> dict:
    # 은행의 갯수만큼 반복하고 값을 하나씩 가져옴
    for bank in Bank.banks:
        for user in bank:
            # user에 있는 키 값이 value 와 같은지 검사
            if user[key] == value:
                # 만약 값을 찾았으면 그값을 리턴
                return user

    # 값이 없으면 None 리턴
    return None

# 은행 클래스 선언
class Bank:
    # 은행의 종류(갯수)
    total_count = 3
    # total_count를 컴프리핸션을 이용해 2중배열 선언
    banks = [[] for i in range(total_count)]

    # 기본 생성자, 초기화
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # 각 회원의 object 필드에는 필드의 주소값이 담긴다.
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # classmethod 데코레이터를 사용해 클래스에 직접 접근해 값 가져오기
    @classmethod
    # bank_choice로 어떤 은행을 사용할지 선택, kwargs로
    def open_account(cls, bank_choice, **kwargs):
        # bank에 세 은행을 넣고 bank_choice-1로 인덱스 번호를 구한 후 생성자로 사용
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 받아온 bank_choice번호를 받아오고, 딕셔너리 객체로 변환해서 값을 담아준다
        # check 함수에서 원하는 key로 값을 찾기 위함
        cls.banks[bank_choice - 1].append(user.__dict__)
        # 개설된 회원 정보를 리턴한다
        return user

    # self에 접근하는 메소드가 아니기 떄문에 static 메소드 데코레이터를 사용한다
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check 함수에 검사할 key와 value 전달
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone: str) -> dict:
        # check 함수에 검사할 key와 value 전달
        return check(key='phone', value=phone)

    def deposit(self, money: int):
        self.money += money

    def withdraw(self, money: int):
        self.money -= money

    def balance(self):
        return self.money

    # 객체를 출력해도 __str__()가 실행되기 때문에 편하고 빠르게 회원 정보를 확인할 수 있다.
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    # Overring
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)


class KookMin(Bank):
    # Overring
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    # Overring
    def balance(self):
        self.money //= 2
        return super().balance()