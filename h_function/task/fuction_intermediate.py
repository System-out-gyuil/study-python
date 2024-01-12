


user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]

number = len(user_info)

# 추가
def insert(name):

    global number
    number += 1
    user_info.append({'number': number, 'name': name})

# 목록
def info_list():

    return user_info

info_list()

# 조회(번호로 조회)
def info_search(number):

    # for i in user_info:
    #     if i['number'] == number:
    #         return i['number'],i['name']

    search = [user for user in user_info if user['number'] == number]
    print(f'조회 : {search}')

info_search(4)

# 수정(번호로 이름 수정)
# def info_update(number, name):
#     for i in user_info:
#         if i['number'] == number:
#             i['name'] = name
#
#     print(f'수정 : {user_info}')
#
# info_update(3, 'tedhan')
def info_update(**kwargs):
    '''

    :param kwargs:{'number' : 기존 회원 번호, 'name' : '새로운 회원 이름'}
    '''

    info_search(kwargs.get('number'))['name'] = kwargs.get('name')

# 삭제(번호로 삭제)
def info_delete(number):
            del user_info[number-1]

info_delete(3)
insert(name='abc')

info_search(number=3, name='tedhan')


















