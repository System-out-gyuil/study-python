# f(x) = 2X+ 1

# def f(x):
#     return 2 * x + 1
#
#
# result = f(2)
# print(result)

# 두 정수의 곱셈
def multiple(num1, num2):
    return num1 * num2

result1 = multiple(3, 6)
print(result1)

# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
def divide(num1, num2):
    result2 = f'{num1}/{num2} = {num1 / num2} 몫 = {num1 // num2} 나머지 = {num1 % num2}'
    return result2

result2 = divide(9, 3)

print(result2)

# 1~10까지 print()로 출력하는 함수
def get_print():
    for i in range(10):
        print(i+1, end=' ')

get_print()

# 이름을 n번 print()로 출력하는 함수
# def print_n(n):
#     for i in range(n):
#         print('김규일', end=' ')
#
# data = int(input("\n숫자 입력 : "))
# print(print_n(data))

# 1~n 까지의 합을 구해주는 함수
# def sum(number):
#     num = 0
#     for i in range(number+1):
#         num += i
#     return num
#
# number = int(input("숫자 입력 : "))
# print(sum(number))

# 1~100까지 중 n의 배수를 print()로 출력하는 함수
def print100(time):
    for i in range(100):
        if(i + 1) % time == 0:
            print(i + 1)
print100(6)
# 두 정수의 뺄셈 함수
def subtract(num1, num2):
    return num1 - num2

print('\n', subtract(3, 6))


# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
# def string(str1, str2):
#     result = str1.count(str2)
#     return result
#
# str1, str2 = input("문자열과 원하는 문자를 입력 : ").split(', ')
# print(string(str1, str2))
'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
    만약 해당 문자가 없으면 -1을 리턴하는 함수
'''
def string(str1, str2):
    for i in range(len(str1)):
        if str2 == str1[i]:
            return i + 1
    return -1

str1, str2 = input("문자열과 원하는 문자를 입력 : ").split(', ')
print(string(str1, str2))
