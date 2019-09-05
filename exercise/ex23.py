# 打印出如下图案（菱形）

def diamond(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(int((n - i) / 2) * ' ', end="")
            print(i * '*')
    for i in list(reversed(range(1, n - 1))):
        if i % 2 != 0:
            print(int((n - i) / 2) * ' ', end="")
            print(i * '*')


diamond(13)
