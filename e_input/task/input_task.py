# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# message1 = '이메일을 입력하세요'
# example1 = 'ex) abcd@gmail.com'
#
# mail_id, mail_domain = input(message1 + '\n' + example1 + '\n').split('@')
#
#
# print(f'{mail_id}, {mail_domain}')
'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
message2 = 'yard 입력 : '
message3 = 'inch 입력 : '
# example2 = '\n ex) yard 입력: 10 inch 입력: 10'

cm_yard = 91.44
cm_inch = 2.54

yard = float(input(message2))
inch = float(input(message3))

formating = f'{yard} yard = {round(yard * cm_yard, 2)}cm,\n{inch} inch = {round(inch * cm_inch, 2)}cm'

print(formating)
