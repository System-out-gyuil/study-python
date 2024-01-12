# 인덱스 슬라이싱
animals = ['cat', 'dog', 'dog', 'horse', 'fish']

print(animals)

# list[inclucive_start-0 : exclusive_end-len(list)] -> list
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])

# list[inclucive_start-0 : exclusive_end-len(list) : step-1] -> list
food = ['noodle', 'meat', 'bread', 'chiken']
print(food[:3:2])
print(food[2::2])

print(food[::-1])

nuber_list = list(range(1, 11))
print(nuber_list)
print()
# [1, 3, 5, 7, 9]
print(nuber_list[:10:2])
# [6, 5, 4, 3, 2]
print(nuber_list[5:0:-1])
# [2, 4, 6]
print(nuber_list[1:7:2])
# [2, 3, 4, 5, 6, 7]
print(nuber_list[1:7])

animals = ['cat', 'dog', 'dog', 'horse', 'bird']
zoo = ['panda', 'giraffe']

# 값이 삽입되는게 아닌 대체가 됌
animals[1:2] = zoo
print(animals)

animals.insert(animals.index('dog') + 1, 'giraffe')
print(animals)

# 슬라이싱, insert, del를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']
animals2 = ['hamster', 'fish', 'whale']

animals.insert(animals.index('dog') + 1, animals2[0])
animals.insert(animals.index('hamster') + 1, animals2[1])
# animals.insert(animals.index('dog') + 1, animals2[2])
# animals.remove('cat')
animals[4:5] = animals2[2]
print(animals)
print(animals[6])

