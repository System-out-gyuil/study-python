from crud_module import *
from papago_api import *
from send_sms import *
from random import *
from ocr import *
import hashlib

if __name__ == '__main__':

# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 아이디(이메일) 중복 검사
#     phone_num = input('전화번호 입력 : ')
#     send_message(phone_num)

# 로그인 후 마이페이지로 이동
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사

    # check_login = False
    # message = "이메일: "
    # member_email = input(message)
    # find_by_id_query = "select email, password, name from tbl_member where email = %s"
    # find_by_id_params = member_email,
    # member = find_by_id(find_by_id_query, find_by_id_params)
    #
    # if member:
    #     message = "비밀번호: "
    #     member_password = input(message)
    #     encryption = hashlib.sha256()
    #     encryption.update(member_password.encode('utf-8'))
    #     member_password = encryption.hexdigest()
    #
    #     if member.get("password") == member_password:
    #         print(f"{member.get('name')}님 환영합니다~!")
    #         for key in member:
    #             if key == 'password':
    #                 continue
    #             print(member.get(key))
    #             check_login = True
    #
    #         message = "비밀번호 변경 [Y/n]: "
    #         check = input(message)
    #
    #         if check == 'Y':
    #             code = "".join([chr(i + 65) for i in range(0, 26)] + [str(i) for i in range(0, 10)])
    #             certification_number = ""
    #             for i in range(10):
    #                 certification_number += code[randint(0, len(code))]
    #             send_email(member.get("email"), certification_number)
    #             message = f"{member.get('email')}로 인증코드를 전송했습니다.\n10자리 인증번호: "
    #             certification_number_input = input(message)
    #             if certification_number_input == certification_number:
    #
    #                 message = "새로운 비밀번호: "
    #                 member_password = input(message)
    #                 message = "재입력: "
    #                 member_password2 = input(message)
    #
    #                 if member_password == member_password2:
    #                     encryption = hashlib.sha256()
    #                     encryption.update(member_password.encode('utf-8'))
    #                     member_password = encryption.hexdigest()
    #
    #                     update_query = "update tbl_member set password = %s where email = %s"
    #                     update_params = member_password, member.get("email")
    #                     update(update_query, update_params)
    #
    #                 else:
    #                     print("비밀번호가 다릅니다.")
    #
    #             else:
    #                 print("인증번호를 다시 확인해주세요.")
    #
    # if not check_login:
    #     print("아이디 또는 비밀번호를 다시 확인해주세요.")




# 사용자가 입력한 한국어를 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 전체 조회
#     data_papago = input('입력 : ')
#     en_papago = get_data(data_papago)
#
#     insert_query = "insert into tbl_papago(papago_translate_before, papago_translate_after) values (%s, %s)"
#     insert_params = [data_papago, en_papago]
#     save(insert_query, insert_params)
#
#     find_all_query = "select papago_translate_after from tbl_papago"
#     datas = find_all(find_all_query)
#
#     for data in datas:
#         print(data)

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# 이미지 경로 : https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
# 경로와 추출한 텍스트 전체 조회

    image_url = 'https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/'
    image_result = image_ocr(image_url)

    insert_query = "insert into tbl_image(image_name, image_content, image_url) values(%s, %s, %s)"
    insert_params = ('전쟁시 불쌍한 사람', image_result, image_url)
    save(insert_query, insert_params)

    select_all_query = "select * from tbl_image"
    datas = find_all(select_all_query)

    for data in datas:
        print(data)