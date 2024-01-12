# [종합 실습]
# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막
#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.

# 계좌, 전화번호 중복 확인
def check(account, make_account):
    isinstance(account, make_account)

class Bank:
    # 총 은행 수
    total_count = 3

    # 컴프리핸셔션으로 2차원 배열선언
    banks = [[] * i for i in range(total_count)]


    def __init__(self, make_account, id, phone_num, money_in=0, money_out=0):
        self.money_in = money_in
        self.money_out = money_out
        self.make_account = make_account
        self.id = id
        self.phone_num = phone_num
        self.account = []

    # 계좌 개설
    @classmethod
    def open_account(cls):
        print(cls.check_account_number())


    # 계좌 중복확인
    @staticmethod
    def check_account_number(account, make_account):
        check(account, make_account)

    # 전화번호 중복확인
    @staticmethod
    def check_phone(account, make_account):
        check(account, make_account)

    # 입금
    def deposit(self):
        pass

    # 출금
    def withdraw(self):
        pass

    # 잔액 조회
    def balance(self):
        pass

    # 한번에 값 확인
    def __str__(self):
        pass

# 신한
class ShinHan():
    pass

# 국민
class KookMin():
    pass

# 카카오
class KaKao():
    pass
