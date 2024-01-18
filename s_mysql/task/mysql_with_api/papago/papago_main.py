from papago_api import *
from crud_module import *

if __name__ == '__main__':
    # 사용자가 입력한 한국어를 영어로 번역
    # 한국어와 번역된 문장을 DBMS에 저장
    # 번역 내역 전체 조회
        data_papago = input('입력 : ')
        en_papago = get_data(data_papago)

        insert_query = "insert into tbl_papago(papago_translate_before, papago_translate_after) values (%s, %s)"
        insert_params = [data_papago, en_papago]
        save(insert_query, insert_params)

        find_all_query = "select papago_translate_after from tbl_papago"
        datas = find_all(find_all_query)

        for data in datas:
            print(data)