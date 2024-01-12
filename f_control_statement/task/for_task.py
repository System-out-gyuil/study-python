# 1~15까지 출력
print('1~15까지 출력')
for i in range(1, 16):
    print(i ,end=' ')

# 30~1까지 출력
print('\n30~1까지 출력')
for i in range(30, 0, -1):
    print(i, end=' ')

# 1~100까지 중 홀수만 출력
print('\n1~100까지 중 홀수만 출력')
for i in range(1, 101, 2):
    print(i, end=' ')

# 1~10까지 합출력
num1 = 0
print('\n1~10까지 합출력')
for i in range(11):
    num1 += i
    print(f'{num1}', end=' ')

# 1~n 까지 합 출력
# num2 = 0
# print('\n1~n 까지 합 출력')
# number = int(input('숫자 입력 :'))
# for i in range(number+1):
#     num2 += i
#     print(f'{num2}', end=' ')

# 345634563456출력
print('\n345634563456출력')
for i in range(3):
    for j in range(3,7):
        print(f'{j}', end=' ')

print('\n345634563456출력')
for i in range(12):
    print(i % 4 + 3,end=' ')

print('\n"1,235,500" 를 1235500 으로 출력')
# '1,235,500' 를 1235500 으로 출력
number = '1,235,500'.split(',')
print(number)

for i in range(len(number)):
    print(number[i], end='')