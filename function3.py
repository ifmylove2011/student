from functools import reduce


def f(x):
    return x * x


# 迭代器
r = map(f, [1, 2, 3, 4])

print(list(r))


# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

def add(x, y):
    return x + y


# 累加add(add(add(1,2)),3),4)
print(add(add(add(1, 2), 3), 4))
print(reduce(add, [1, 2, 3, 4]))


def combine(x, y):
    return x * 10 + y


print(reduce(combine, [1, 2, 3, 4]))

test = lambda str: str[0].upper() + str[1:].lower()
# def test(str):
#     return str[0].upper() + str[1:].lower()

print(list(map(test, ['jim', 'Jiiii'])))

print(sum([1, 2, 3, 4]))


# f = lambda x, y: x*y
def test(x, y):
    return x * y


def prod(xx):
    return reduce(lambda x, y: x * y, xx)


print(prod([1, 2, 3]))


def str2float(str):
    f = lambda x: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
    l1, l2 = str.split('.')
    n1 = reduce(lambda x, y: x * 10 + y, map(f, l1))
    n2 = reduce(lambda x, y: x * 0.1 + y, map(f, reversed(l2)))
    return n1 + n2 * 0.1


# f = lambda x:{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
# # 类似C中的define
# print(reduce(lambda x,y:x*10+y,map(f,'123')))
# print(reduce(lambda x,y:x*0.1+y,map(f,'123')))

print(str2float('123.123'))


# 允许奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3])))


# 滤除空字符
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', 'b', ' ', None])))

