# 输入某年某月某日，判断这一天是这一年的第几天？

def judge(y, m, d):
    curd = 0
    m_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if m < 1 or m > 12 or d < 1 or d > 31:
        print("日期有误")
    else:
        for i in range(1, m):
            if i == 2 and judge1(y):
                curd += 1
            curd += m_dict[i]
        curd += d
    return curd


# 判断闰年
def judge1(y):
    if y % 100 == 0:
        return y % 400 == 0
    else:
        return y % 4 == 0

print(judge(2017,3,1))