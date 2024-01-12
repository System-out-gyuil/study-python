# def set_key(name):
#     formatting = ''
#     formatting2 = ''
#     # closure
#     def set_value(name_value):
#         nonlocal formatting
#         nonlocal formatting2
#         formatting = f'{name} : {name_value}'
#         # formatting2 = f'{age} : {age_value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formating_name = set_name("한동석")
# print(formating_name)
#
# # '나이: 00살'
# # print(set_key('이름', '나이')('김규일', 20))
# set_age = set_key('나이')
# formating_age = set_age(20)
# print(formating_age)

# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

def set_topic(**kwargs):

    if 'name' in kwargs:
        def set_format(name_value):

            name = f'{kwargs["name"]}{kwargs["comma"]}{name_value}'
            return name
    else:
        def set_format(point_value):

            point = f'{kwargs["topic"]}{kwargs["comma"]}{point_value}'
            return point

    return set_format
print(set_topic(topic='주제', comma=', ')('요약내용'))
print(set_topic(name='name', comma=', ')('김ㄱ일'))

