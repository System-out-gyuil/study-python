# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

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

        # 같은 이름의 상품이 있을경우
        if append_data in name_list:
            print(append_error_message)

        # 상품 추가하기
        else:
            name_list.append(append_data)
            price_list.append(price_data)
            print(f'상품이 추가되었습니다\n상품명  : {name_list} \n상품 가격:{price_list}')

    # 상품 수정
    elif menu_data == '2':
        # 수정할 상품 검색
        update_data = input(search_name_message_for_update)

        # 수정할 상품명이 없을때
        if update_data not in name_list:
            print(update_error_message1)

        # 상품 수정
        elif update_data in name_list:
            update_data_new_name, update_data_new_price = input(update_message).split()

            # 수정할 상품명이 중복되었다면
            if update_data_new_name in name_list:
                print(update_error_message2)

            # 상품명 변경
            else:
                index = name_list.index(update_data)
                name_list[index] = update_data_new_name
                price_list[index] = update_data_new_price
                print(f'상품이 수정되었습니다.\n상품명  : {name_list[index]} \n상품 가격:{price_list[index]}')

    # 상품 삭제
    elif menu_data == '3':
        delete_data = input(delete_message)

        # 삭제할 상품명이 없을때
        if delete_data not in name_list:
            print(delete_error_message)

        # 상품 삭제
        else :
            index = name_list.index(delete_data)
            del name_list[index]
            del price_list[index]
            print("해당 상품이 삭제되었습니다.")

    # 상품 검색
    elif menu_data == '4':
        search_data = input(search_menu)

        # 상품명으로 검색
        if search_data == '1':
            name_search_data= input(search_name_message)

            # 검색한 상품명이 있을경우
            if name_search_data in name_list:
                index = name_list.index(name_search_data)
                print(f'검색하신 상품입니다\n상품명  : {name_list[index]} \n상품 가격 : {price_list[index]}')

            # 검색한 상품명이 없을때
            else :
                print(search_error_message)

        # 가격으로 검색
        elif search_data == '2':
            price_search_data = input(search_price_message)
            min = int(price_search_data) * 0.5
            max = int(price_search_data) * 1.5

            # 상품 가격의 ±50% 계산
            result_price = [price_list.index(i) for i in [price for price in price_list if min <= int(price_search_data) <= max]]

            # 검색 금액 범위에 맞는 상품이 있다면
            if len(result_price) != 0:
                for i in result_price:
                    print(f'검색하신 상품입니다\n상품명 :  {name_list[i]} \n상품 가격 : {price_list[i]}')

            # 상품이 없다면
            else :
                print(search_error_message)

            # # 검색한 가격이 있을경우
            # if price_search_data in price_list:
            #     index = price_list.index(price_search_data)
            #     print(f'검색하신 상품입니다\n상품명 :  {name_list[index]} \n상품 가격 : {price_list[index]}')
            #
            # # 입력한 가격이 없을경우
            # else :
            #     print(search_error_message)

        # 잘못된 숫자를 입력한 경우
        else :
            print(error_message)

        # 목록 보기
    elif menu_data == '5':

        # 목록에 상품이 없을경우
        if not name_list :
            print(no_item_message)

        # 목록에 상품이 있을경우
        else :
            print(name_list, price_list, sep='\n')

    # 나가기
    elif menu_data == '6':
        break






