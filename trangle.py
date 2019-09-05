def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)  # 为了增加L的长度，且可错位相加
        # print("-------------")
        # for i in range(len(L)):
        #     print(L[i-1],L[i])
        # print("-------------")
        L = [L[i - 1] + L[i] for i in range(len(L))]

# t = triangles()
# for i in range(5):
#     print(next(t))

def trii(m):
    
    return "done"
