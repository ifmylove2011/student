# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之
# 间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到
# 100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

def salary(n):
    t = 0
    if n > 100:
        t += (n - 100) * 0.01
        n = 100
    if 60 < n:
        t += (n - 60) * 0.015
        n = 60
    if 40 < n:
        t += (n - 40) * 0.03
        n = 40
    if 20 < n:
        t += (n - 20) * 0.05
        n = 20
    if 10 < n:
        t += (n - 10) * 0.075
        n = 10
    if n <= 10:
        t += n * 0.1
    return t


print(salary(30))


def salary1(n):
    level = [0, 10, 20, 40, 60, 100]
    weight = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    level = list(reversed(level))
    weight = list(reversed(weight))
    t = 0
    for i in range(len(level)):
        if n > level[i]:
            t += (n - level[i]) * weight[i]
            n = level[i]
    return t


print(salary1(30))

# l = [1,2,3,4]
# print(list(reversed(l)))
