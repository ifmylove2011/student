# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math

def analyze(n):
    factor = 2
    print(n,"=",end=" ")
    while factor <= math.sqrt(n):
        if (n % factor == 0):
            n = int(n / factor)
            print(factor,"*",end=" ")
            factor = 2
        else:
            factor += 1
    print(n)


analyze(6)
