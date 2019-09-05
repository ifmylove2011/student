def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# t = odd_iter()
# for i in range(10):
#     print(next(t))


def not_divisible(n):
    return lambda x: x % n == 0


def not_divi_3():
    return lambda x: x % 3 == 0


# test = filter(not_divi_3(), odd_iter())
# for i in range(10):
#     print(next(test))


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


# p = primes()
# for i in range(10):
#     print(next(p))

print(sorted([1, -2, 3, -5], key=abs))

print(sorted(['a','A','b','B']))
print(sorted(['a','A','b','B'],key=str.lower))
print(sorted(['a','A','b','B'],key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L,key=lambda ))


