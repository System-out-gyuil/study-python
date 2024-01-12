# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

class Customer:

    # private : 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자
    # 2. 외부에서 접글할 때 꼭 메소드로 접근하자.
    __user_number1 = 0
    __user_number2 = 0
    def __init__(self, id, pw, name):
        self.number1 = Customer.__user_number1
        self.number2 = Customer.__user_number2
        self.id = id
        self.pw = pw
        self.name = name

    def num_count(self):

        if self.name == '관리자':
            Customer.__user_number1 += 1
        else:
            Customer.__user_number2 += 1

    @classmethod
    def administer(cls, id, pw, name):
        if name == '관리자':
            id = 'admin_' + id
        return cls(id, pw, name)

    def print_info(self):
        print(self.number1,self.number2, self.id, self.pw, self.name)



customer1 = Customer.administer('qazxc', '1234', '관리자')
customer1.print_info()
customer2 = Customer.administer('qazxc', '1234', '홍길동')
customer2.print_info()