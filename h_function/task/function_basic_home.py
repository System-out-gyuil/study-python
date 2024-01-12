# pay_data = [2000, 4000, 6000]
def order_info(*args, **kwargs):
    pay_list = list(args)
    count = kwargs.get('count')
    sale = int(kwargs.get('coupon')) / 100
    # ran = len(pay_data)
    discount = 1 - kwargs['coupon'] / 100

    # 그냥 풀었을때
    # if ran >= count:
    #     for i in range(count):
    #         print(pay_list[i] - (pay_list[i] * sale))
    # elif ran < count:
    #     for i in range(ran):
    #         print(pay_list[i] - (pay_list[i] * sale))

    # comprehension 사용
    # result = [int(pay * discount) if idx < count else pay for idx, pay in enumerate(pay_data)]

    # 유진님거
    result = [item * discount if i < count else item for i, item in enumerate(pay_list)]
    print(result)

order_info(2000, 4000, 5000, coupon=30, count=1)

