# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def fx20(h, order, ratio):
    cur_h = h
    s = 0
    for i in range(order):
        s += cur_h
        if i >= 1:
            s += cur_h
        cur_h = cur_h * ratio
    return (s, cur_h)


print('共经过',fx20(100, 10, 0.5)[0],'弹起',fx20(100, 10, 0.5)[1])
