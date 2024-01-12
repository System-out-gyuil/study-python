# 람다(lambda) : 이름이 없는 함수
# lambda 매개변수, ... : 값

# 일반 함수
# def add(number1, number2):
#     return number1 + number2

# 익명 함수
# lambda number1, number2: number1 + number2

print(list(map(lambda number : number + 2, [1, 2, 3, 4])))

# 사용 예시
# 아래의 list에 각 요소에 2를 곱하여 변경
datas = [2, 4, 6 ,8]
print(list(map(lambda num : num * 2, datas)))

urls = ['/game', '/news', '/fashion', '/ranking']
print(list(map(lambda url : url.replace('/','/app/'), urls)))

# filter(function, iterator)
# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number % 2 == 0, [i + 1 for i in range(10)])))

urls2 = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
print([i.split('/') for i in urls2])
# print(filter(lambda url : url, [i.split('/') for i in urls2]))
print(list(filter(lambda url : url.split('/')[-1] == 'game', urls2)))