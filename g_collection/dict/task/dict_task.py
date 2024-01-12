# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "안녕"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
delete_message = '삭제하실 상품명을 입력하세요.'
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 제목(?)
    print('\n',title)
    # 메뉴 선택
    menu_data = input(menu)

    # 상품 추가
    if menu_data == '1':
        # 상품명, 상품 가격 입력
        append_data, price_data = input(append_message).split()

        # 상품 추가하기
        if append_data not in data_dict:
            data_dict[append_data] = price_data
            print(data_dict)

        # 같은 이름의 상품이 있을경우
        else:
            print(append_error_message)

    # 상품 수정
    elif menu_data == '2':
        # 수정할 상품 검색
        update_data = input(search_name_message_for_update)

        # 수정할 상품명이 없을때
        if update_data not in data_dict:
            print(update_error_message1)

        # 상품 수정
        elif update_data in data_dict:
            update_data_new_name, update_data_new_price = input(update_message).split()

            # 수정할 상품명이 중복되었다면
            if update_data_new_name in data_dict:
                print(update_error_message2)

            # 상품명 변경
            else:
                del data_dict[append_data]
                data_dict[update_data_new_name] = update_data_new_price
                print(data_dict)
    # 상품 삭제
    elif menu_data == '3':
        delete_data = input(delete_message)

        # 삭제할 상품명이 없을때
        if delete_data not in data_dict:
            print(delete_error_message)

        # 상품 삭제
        else :
            del data_dict[delete_data]
            print("해당 상품이 삭제되었습니다.")
            print(data_dict)

    # 상품 검색
    elif menu_data == '4':
        search_data = input(search_menu)

        # 상품명으로 검색
        if search_data == '1':
            name_search_data = input(search_name_message)

            # 검색한 상품명이 있을경우
            if name_search_data in data_dict:
                for name, price in data_dict.items():
                    print(f'{name}, {price}')

            # 검색한 상품명이 없을때
            else :
                print(search_error_message)

        # 가격으로 검색
        elif search_data == '2':
            check = False
            price_search_data = input(search_price_message)
            min = int(price_search_data) * 0.5
            max = int(price_search_data) * 1.5

            # 상품 가격의 ±50% 범위내에 상품이 있다면
            for name, price in data_dict.items():
                if min <= int(price) <= max:
                    check = True
                    print(f'{name}, {price}')

            # 검색한 상품이 없다면
            if not check:
                print(search_error_message)

        # 잘못된 숫자를 입력한 경우
        else :
            print(error_message)

        # 목록 보기
    elif menu_data == '5':

        # 목록에 상품이 없을경우
        if not data_dict :
            print(no_item_message)

        # 목록에 상품이 있을경우
        else :
            print(data_dict)

    # 나가기
    elif menu_data == '6':
        break






