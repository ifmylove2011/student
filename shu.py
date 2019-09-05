# 回数
# def circle_number():

# print(str(12345))
# n = '1221'


# def justify(nubmer):
#     flag = True
#     n = str(nubmer)
#     for i in range(int(len(n) / 2)):
#         # print(str(i)+":")
#         # print(n[i])
#         # print(n[-i-1])
#         if n[i] != n[-i - 1]:
#             flag = False
#     if flag:
#         return n

# e = '123'
# print(list(e))
# print(list(reversed(e)))
# print(list(reversed(e))==list(e))
#
# print(e)
# print(e[::-1])
def shu_iter():
    n = 1
    while True:
        n = n + 1
        yield n

def judge():
    return lambda n:str(n)==str(n)[::-1] and n>10


f = filter(judge(),shu_iter())
for i in range(100):
    print(next(f))




