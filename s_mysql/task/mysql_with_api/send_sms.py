import json
import message
import random
from crud_module import *

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
def send_message(phone_number: str):
    random_number = random.randrange(100000, 1000000)
    data = {
        'messages': [
            {
                'to': phone_number,
                'from': '01046342519',
                'text': str(random_number)
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
    check_random_number = int(input('발송된 인증번호를 입력하세요 : '))
    if check_random_number == random_number:
        while True:
            create_account_email = input('이메일과 비밀번호를 입력하세요 : ')

            find_by_id_query = "select user_email from tbl_user where %s"
            find_by_id_param = create_account_email
            check_email = find_by_id(find_by_id_query, find_by_id_param)

            if create_account_email in check_email:
                print('중복된 이메일입니다 다시 입력해주세요')
                continue
            else:
                create_account_password = input('비밀번호를 입력하세요 : ')
                insert_query = "insert into tbl_user(user_email, user_password) values (%s, %s)"
                insert_params = (create_account_email, create_account_password)
                save(insert_query, insert_params)
                break

