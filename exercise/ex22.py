# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单

# l = [m + n for m in ['a', 'b', 'c'] for n in ['x', 'y', 'z']]
# print(l)

# for i in range(ord('x'), ord('z') + 1):
#     for j in range(ord('x'), ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'), ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print('order is a-%s b-%s c-%s' % (chr(i), chr(j), chr(k)))

l1 = ['x', 'y', 'z']

# i,j,k本身所在的位置顺序影响了配对的顺序，故排列xyz本身的顺序即可得到结果
for i in l1:
    for j in l1:
        if i != j:
            for k in l1:
                if (i != k) and (j != k):
                    if (i != 'x') and (k != 'x') and (k != 'z'):
                        print('order is a-%s b-%s c-%s' % (i, j, k))
