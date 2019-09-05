# 求1+2!+3!+...+20!的和\

from functools import reduce

l = lambda x: reduce(lambda x, y: x * y, range(1, x + 1))
print(sum(map(l,range(1,5))))