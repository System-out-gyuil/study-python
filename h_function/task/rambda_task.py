# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
datas = ['aPPle', 'BananA', 'meLON']
print(list(map(lambda data : data.lower() ,datas)))

# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
kor_list = "공일이삼사오육칠팔구"
kor = "삼오일구"
print(int("".join(map(lambda s : str(kor_list.index(s)), kor))))


# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
num = 351234
print("".join(list(map(lambda s : kor_list[int(s)], str(num)))))

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
urls = 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'

print(filter(lambda service : service != 'user', list(map(lambda url : url[:url.index("/")], urls))))






