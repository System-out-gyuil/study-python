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

# 이 파일이 실행하는 파일이다. 라고 알려준다
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 변경\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"
    new_account_message = "새 계좌번호: "

    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        # 나가기
        if bank_choice == 4:
            break

        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 못하게 막는다
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))
            # 은행 메뉴로 돌아가기
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    # None은 False 값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break

                money = int(input(money_message))

                # 계좌가 개설된다.
                # 어떤 은행에서 개설했는 지를 bank_choice에 담아서 전달한다
                # open_account()는 회원의 정보를 **kwargs로 받기 때문에 모두 풀어서 전달해준다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)

                # 재정의한 __str__()이 사용되고 전체 정보를 확인한다.
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능
            elif menu_choice == 2:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)

                if isinstance(user.get('object'), ShinHan):
                    if bank_choice != 1:
                        print('개설한 은행에서만 입금 서비스를 사용하실 수 있습니다')
                        continue

                if user is not None:
                    if user['password'] == input(password_message):
                        deposit_money = int(input(deposit_message))
                        user['object'].deposit(deposit_money)

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                print('들어옴')
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        withdraw_money = int(input(withdraw_message))
                        # 로그인한 회원의 은행이 국민 은행이라면 출금 수수료가 50%이기 때문에,
                        # 잔액 검사 시 1.5를 곱해준다.(삼항연산)
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)
                            continue
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                phone_number = input(phone_message)
                user = Bank.check_phone(phone_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            new_account = input(new_account_message)
                            if Bank.check_account_number(new_account) is None:
                                break
                        user['account_number'] = new_account
                        continue

                print(error_message)

            else:
                print(error_message)













