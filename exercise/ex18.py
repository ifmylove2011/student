# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

def cultivate(num, order):
    s = 0
    for i in range(1, order + 1):
        s += int(i * str(num))
    return s


print(cultivate(2, 3))
