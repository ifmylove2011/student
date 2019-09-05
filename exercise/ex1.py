# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# def num():
#     for i in range(1, 5):
#         for j in range(1, 5):
#             for k in range(1, 5):
#                 yield str(i) + str(j) + str(k)
#
#
# def exclude():
#     return lambda s: s[0] != s[1] and s[0] != s[2] and s[1] != s[2]
# f = filter(exclude(), num())

# *********************************************************************************

# f = filter(lambda s: s[0] != s[1] and s[0] != s[2] and s[1] != s[2],
#            [str(i) + str(j) + str(k) for i in range(1, 5) for j in range(1, 5) for k in range(1, 5)])
# try:
#     while True:
#         print(next(f))
# except:
#     print("done")

# *********************************************************************************

l = [str(i) + str(j) + str(k) for i in range(1, 5) for j in range(1, 5) for k in range(1, 5) if
     i != j and j != k and i != k]
print(l)

# *********************************************************************************
from itertools import permutations
from itertools import combinations

print("排列")
for i in permutations([1, 2, 3, 4], 3):
    print(i)

print("组合")
for i in combinations([1, 2, 3, 4], 3):
    print(i)

