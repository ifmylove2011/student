# 输出 9*9 乘法口诀表。


for x in range(1, 10):
    for y in range(1, x + 1):
        print(y, "x", x, "=", x * y, "\t", end="")  # end表示不换行
    print()
