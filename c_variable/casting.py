data = 10
print(bin(data))
print(oct(data))
print(hex(data))
print(float(data))

data = 10.93
print(int(data))
print(type(str(data)))
print(str(data))
print(bool(data))

# 0 이외엔 True
bool(0)
bool(1)
bool(1213)

# 빈문자열은 False
print(bool(""))
print(bool("d"))
