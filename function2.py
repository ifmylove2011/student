# -*- coding: utf-8 -*-
import math


# 返回多个值的其实是返回一个tuple
def angle(x):
    return x * 2, x * 3


# 重名会覆盖
def angle(y):
    return math.sin(y), math.cos(y)


print(angle(math.pi / 6))
print(math.sqrt(3) / 2)
print(angle(4))


# 使用递归时，返回语句中不包含表达式则可避免栈溢出
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact2(n, start):
    if 1 == n:
        return start
    return fact2(n - 1, n * start)


print(fact(10))
print(fact2(1000, 1))
