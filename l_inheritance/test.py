class Customer:
    number1 = 0
    number2 = 0
    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
        Customer.number1 += 1
        Customer.number2 += 1
    @classmethod
    def admin(cls, id, password, name):
        cls.id = 'admin_' + id
        cls.password = password
        cls.name = name
        return cls('admin_'+id, password, name)
    def print_info(self):
        print(self.number2, id, self.password, self.name)
customer = Customer.admin('qwe', '1234', 'wefwef')
print(customer.number1, customer.id, customer.password, customer.name)
customer = Customer('abc', '33434','kljkl')
print(customer.number2, customer.id, customer.password, customer.name)
customer = Customer('wer','3444', 'tfgsd')
print(customer.number2, customer.id, customer.password, customer.name)