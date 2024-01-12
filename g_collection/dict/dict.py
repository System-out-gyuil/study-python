student = {
    "name" : "김규일",
    "email" : "a46884334@gmail.com"
}

print(student["name"])
print(student.get('name'))

# get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# default 값이 없을 때에는 None을 가져온다
# print(student['phone'])
print(student.get('phone', '01046342519'))

# 이미 'name' key 값이 있으므로 수정.
student['name'] = '홍길동'
print(student)

# 'phone' 이라는 key 값이 없기 때문에 추가.
student['phone'] = '01046342519'
print(student)

if 'email' in student:  # 수정
    student['email'] = 'ghd1234@email.com'
else:   # 추가
    student['email'] = 'ghd1234@gmail.com'

print(student)

my_dict = {
    1:'한동석',
    "two" : "20살",
    False:[10, 20, 30],
    "row" : [
        {'name' : 'ted', 'age' : 40},
        {'name' : 'jack', 'age' : 30},
        {'name' : 'john', 'age' : 20}
    ]
}

# row 안에 있는 회원 3명의 정보를 모두 출력
print(my_dict['row'])

for i in my_dict['row']:
    print(f'{i["name"]} : {i["age"]}')

# if 'row' in my_dict:
#     # print(type(my_dict['row']))
#     for data in my_dict['row']:
#         print(f'{data['name']}, {data['age']}')

# 1~10 까지 중 홀수와 짝수가 있다
# 사용자가 '짝수' 를 입력하면, 짝수만 출력하고
# '홀수' 를 입력하면, 홀수만 출력된다
# dict를 사용해라
# message = '홀수인지 짝수인지 입력하시오'
# num_dict = {
#     # '홀수' : [i * 2 + 1 for i in range(5)],
#     # '짝수' : [(i + 1) * 2 for i in range(5)],
#     '홀수' : [1, 3, 5, 7, 9],
#     '짝수' : [2, 4, 6, 8, 10]
# }
#
# num_data = input(message)
#
# print(num_dict.get(num_data))

student = {
    "name" : "김규일",
    "email" : "a46884334@gmail.com"
}

# key 분리
print(list(student.keys()))

# value 분리
print(list(student.values()))

# item 분리
print(list(student.items()))

for key, value in student.items():
    print(f'{key} : {value}')