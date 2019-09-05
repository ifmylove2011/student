# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# def num():
#     n = 0
#     while True:
#         n = n + 1
#         yield n

l = [x * x for x in range(1000)]
f = [x for x in range(-10000, 10000) if x + 100 in l and x + 100 + 168 in l]
for i in f:
    print(i)
# for i in num(): +
#     if i+100 in l and i+100+168 in l:
#         print(i)

# f = lambda x: x + 100 in l and x + 100 + 168 in l
# ss = filter(f,l)
# s = map(lambda x:x*x ,num())
