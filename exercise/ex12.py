# 判断101-200之间有多少个素数，并输出所有素数。

# i = 2
# while i < 100:
#     j = 2
#     while j <= (i / j):
#         if not (i % j):
#             break
#         j += 1
#     if j > i / j:
#         print(i, " 是素数")
#     i += 1

def sushu(n):
    j = 2
    while j <= (n / j):
        if not (n % j):  # 能整除则跳出
            break
        j += 1
    if j > n / j:
        return n


f = filter(sushu, range(101, 200))
for i in range(100):
    try:
        print(next(f))
    except:
        print("done")
        break
