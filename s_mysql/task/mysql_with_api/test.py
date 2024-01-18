from crud_module import *
while True:
    create_account_email, create_account_password = input('이메일과 비밀번호를 입력하세요 : ').split(', ')

    find_all_query = "select user_email from tbl_user"
    check_email = find_all(find_all_query)

    if create_account_email in check_email:
        print('중복된 이메일입니다 다시 입력해주세요')
        continue
    else:
        insert_query = "insert into tbl_user(user_email, user_password) values (%s, %s)"
        insert_params = (create_account_email, create_account_password)
        save(insert_query, insert_params)
        break
