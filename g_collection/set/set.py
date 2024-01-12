# 중복이 없고, 순서가 없다

world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
print(len(world_set))

# 순서가 없어서 가져올 수 없다
# print(world_set[1])
world_set.add('korea')
# 다른 자료구조를 사용해서 가져온다
print(world_set)

# 중복을 제거할 때 효과적이다
datas = [1,1,1,3,3,2,4,2,2,3,4,]
print(list(set(datas)))