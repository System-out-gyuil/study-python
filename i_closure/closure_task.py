# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.
def set_product(*args):
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break

    def select_all():
        return args

    return {'insert': insert, 'update': update, 'select_all': select_all}


products = [
    {'name': '마우스', 'price': 5000},
    {'name': '키보드', 'price': 25000}
]

product_service = set_product(*products)
print(products)
product_service.get('insert')(name='모니터', price=80000)
print(product_service.get('select_all')())
product_service.get('update')(name='키보드', price=20000, number=2)
print(product_service.get('select_all')())