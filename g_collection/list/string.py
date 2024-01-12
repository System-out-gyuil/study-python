# upper(), lower()

print('Apple123!@#'.upper())
print('AppLe123!@#'.lower())

# split()
data = '사과, 바나나, 복숭아, 포도'
print(data.split(',', maxsplit=2))

print("A B C D E F".split())
print("A      \n      B".split())
print("A     B".split(" "))

# join()
print(":".join(['a', 'b', 'c']))
print("".join(['a', 'b', 'c']))

# replace('기존 값', 새로운 값')
print("A b C d".replace(" ", ""))
print('안녕! 반가워~!'.replace("!", "?"))

# strip(), lstrip(), rstrip()
print("    a      b       c     ".strip())
print("    a      b       c     ".strip(" "))
print("apple".strip("a"))

# index
print("ABC".index("A"))
# print("ABC".index("Z"))

# find()
print("ABC".find("A"))
print("ABC".find("Z"))

# in
print("A" in "ABC")
print("F" in "ABC")

# count()
print("dsadadqffakofmoagndfgfoiewanf".count("o"))

s = "189,000 원"
# for i in s:
#     if '0' <= i <= '9':
#         print(i, end='')

print("".join([i for i in s if '0' <= i <= '9']))

print(ord('0'))