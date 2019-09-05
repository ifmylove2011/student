# 斐波那契数列

def fib():
    m = 0
    n = 1
    while True:
        yield n
        m, n = n, m + n


def fib_order(k):
    m = 1
    n = 1
    i = 1
    while i < k:
        m, n = n, m + n
        i +=1
    return n


f = fib()
for i in range(10):
    print(next(f))
    # print(fib_order(i))
