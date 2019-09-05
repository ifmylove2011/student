# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

from fractions import Fraction

# print(Fraction('1/3')+Fraction('2/5'))
# print(Fraction('1'+'/'+'3'))
def fib_order(k):
    m = 1
    n = 1
    i = 1
    while i < k:
        m, n = n, m + n
        i +=1
    return n

l = [Fraction(str(fib_order(x+1))+'/'+str(fib_order(x))) for x in range(1,3)]
print(sum(l))
