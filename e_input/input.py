# 문자열 끼리만 연결이 가능하다
# data = 3
# print('안' + str(data))

# print(name)
# name, hight = input('이름 : '), input('키 : ')
# print(name + '님 환영합니다')

# 제 이름은 ???, 키는 ???cm입니다
# name = input('이름 : ')
# hight = input('키 : ')
#
# print(f'제 이름은 {name}, 키는 {hight}cm 입니다.')

# 두 정수를 입력받은 후 곱셈 결과 출력

# num1 = int(input('숫자1 : '))
# num2 = int(input('숫자2 : '))
# num3 = num1 * num2
# data1 = '%d * %d = %d' % (num1, num2, num1 * num2)
# data2 = f'{num1} * {num2} = {num3}'
#
# print(data1)
# print(data2)

# message = '두 정수를 입력하세요'
# example_message = '예) 1, 3'
#
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# formating = f'{number1} * {number2} = {result}'
#
# print(formating)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message1 = '현재 시간을 입력하세요'
example1 = '예) 11:29'
time1, time2 = input(message1 + '\n' + example1 + '\n').split(':')

print(f'{time1}시{time2}분')

# 핸드폰 번호를 -(하이픈)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
message2 = '휴대폰 번호를 입력하세요'
example2 = '010-3333-2222'
number1, number2, number3 = input(message2 + '\n' + example2 + '\n').split('-')

print(f'{number1}, {number2}, {number3}')

# 이름과 나이를 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
message3 = '이름과 나이를 입력하세요'
example3 = 'ex) 홍길동 30'

# split() 디폴트값은 공백
name, age = input(message3 + '\n' + example3 + '\n').split()

print(f'{name}님의 나이는 {age}살')

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message4 = '3개의 정수를 입력하세요'
example4 = 'ex) 3, 6, 9'

num1, num2, num3 = map(int, input(message4 + '\n' + example4 + '\n').split(', '))

print(f'{num1} + {num2} + {num3 } = {num1 + num2 + num3}')