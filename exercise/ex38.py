# 求一个3*3矩阵对角线元素之和

# 在n*n的矩阵上，对角线是1,n+1+1,2*(n+1)+1

def ex38(n):
    l = [x for x in range(1, 101)]
    for i in range(1, n * n + 1):
        if i % n == 1:
            print()
        print('{0:4d}'.format(i), end="")
    print('\n对角线和：', end="")
    ll = []
    for i in range(n):
        ll.append(l[(n + 1) * i])
    print(sum(ll))


ex38(10)
