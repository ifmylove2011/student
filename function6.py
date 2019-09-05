# -*- coding: utf-8 -*-

l =[x for x in range(1,2000) if '7' not in str(x)  and x%7!=0]
# for i in range(1,400):
#     print(l[i])

def test7():
    n = 1
    while True:
        if '7' not in str(n) and n%7!=0:
            yield n
        n = n+1

f = test7()
for i in range(100):
    try:
        print(next(f))
    except:
        print('done')