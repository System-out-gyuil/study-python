# 실습
# 1~98 까지 list에 담고 출력
first_list = list(range(1, 99))
print(first_list)

# 1~100 까지 중 짝수만 list에 담고 출력
second_list = list(range(2, 101, 2))
print(second_list)

number_list = [0] * 50
for i in range(len(number_list)):
    number_list[i] = (i + 1) * 2

print(number_list)
# 1~10까지 list에 담은 후 짝수만 출력
tir_list = list(range(1, 11))
print(tir_list)
for i in tir_list:
    if tir_list[i] % 2 == 0:
        print(tir_list[i], end=' ')

# 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
forth_list = ['규일', '동석', '시현', '지원', '우람', '유진']
print(forth_list)

index = forth_list.index('동석')
forth_list[index] = '한동석'
print(forth_list)

del(forth_list[-1])
print(forth_list)

# "189,000 원" 을 189000으로 변경, 제네레이터 사용