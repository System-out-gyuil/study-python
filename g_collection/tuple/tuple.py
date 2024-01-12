# mutable
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1

data_list2[0] = 10
print(data_list2)
print(data_list1)

# immutable
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1

# data_tuple2[0] = 10
data_tuple2 = data_tuple1 + (5, 6)

print(data_tuple1)
print(data_tuple2)

datas = 1, 2
print(type(datas))
print(datas[0])

ERROR_CODE = 1,
print(type(ERROR_CODE))