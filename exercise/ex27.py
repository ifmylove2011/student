# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

s = '12345'

# print(s[:len(s)-1])

def reve(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s) - 1] + reve(s[:len(s) - 1])

print(reve(s))
