# -*- coding: utf-8 -*-

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-24))

def justify(age):
    if (age > 18):
        pass


def power(x, n):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


def power2(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


print(power2(2))


# 指定不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可指定可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc((1, 2, 3, 4)))
print(calc1(1, 2, 3, 4))


# 关键字函数（自动组装dict)
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("h", 28)
person("h", 28, city="xxx", pro='yyy')


# 只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, job='Engineer')  # 少参数


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# *args接收tuple，**kw接收dict
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# func(*args,**kw)对于任意函数都适用

args = (1, 2, 3)
kw = {'x': 1, 'y:': 2}

x = 1
y = 2
(x,y) = (y,x)
print(x,y)
