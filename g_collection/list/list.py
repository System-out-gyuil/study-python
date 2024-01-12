animals = ['dog', 'cat', 'bird', 'fish']

print(animals)
print(type(animals))

# 인덱스로 접근
print(animals[0])
print(animals[1])
print(animals[2])

# 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
print(animals[-1])

# len()
print(len(animals))

# append()
animals.append('hamster')
print(animals[4])
print(len(animals))
print(animals)

# 중복값 추가
animals.append('cat')
# 중복도 상관 없음
print(animals)

# insert()
animals.insert(1, 'chiken')
print(animals)

# remove()
animals.remove('fish')
print(animals)

# del()
del(animals[-1])
print(animals)

# clear()
# animals.clear()
# print(animals)

# index()
print(animals.index('bird'))
# print(animals.index('tiger')) # 없는 값을 검색하면 오류로 나온다

# 수정
index = animals.index('bird')
animals[index] = 'lion'

# 그 외
animals = ['dog', 'cat', 'bird', 'fish']
print(animals * 2)

print('dog' in animals) # 값이 boolean타입으로 나옴
print('tiger' in animals)

for i in animals:
    print(i, end=' ')
print()
# list 안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j], end=' ')