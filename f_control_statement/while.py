# 사용자가 입력한 정수가 몇 자리수인지 출력
# 1. 사용자에게 정수를 입력받는다.
# 2. 입력받은 정수의 각 자리수를 잰다
# 3. 자리수를 출력한다
flag = True
num = 0
count = 0
data = input('숫자 입력 : ')
while flag:
    num += 1
    if num == int(len(data)):
        flag = False

print(len(data),'자리 숫자입니다')

# while int(data) != 0:
#     int(data) //= 10
#     count += 1
#
# print(count)

