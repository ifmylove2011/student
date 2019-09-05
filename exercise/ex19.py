# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数

import math


# 分解因式
def analyze(n):
    factor_l = [1]
    factor = 2
    while factor <= math.sqrt(n):
        if (n % factor == 0):
            n = int(n / factor)
            factor_l.append(factor)
            factor = 2
        else:
            factor += 1
    factor_l.append(n)
    return factor_l


# 分解因子
def analyze1(n):
    factor_l = [1]
    factor = 2
    while factor <= n / 2:
        if n % factor == 0:
            factor_l.append(factor)
        factor += 1
    return factor_l

l = [x for x in range(1000) if x == sum(analyze1(x))]
print(l)
# for i in range(6, 1000):
#     print("num:", i, "factor:", analyze(i), "sum:", sum(analyze(i)))
