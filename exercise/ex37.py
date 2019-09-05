# 对10个数进行排序

'''
拿到当前值，像打牌一样，把当前值排在他对应的位置
'''
def insert_sort(list):
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            flag = list[i]
            j = i - 1
            while j >= 0 and flag < list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = flag
        print(list)
    print(list)


insert_sort([1, 3, 2, 8, 12, 5, 7, 3, 0])

'''
拿到当前序列中的最小值，放在最前面
'''
def select_sort(list):
    for i in range(1, len(list)):
        min = list[i]
        k = i
        j = i
        for ii in list[i + 1:len(list)]:
            k = k + 1
            if ii < min:
                min = ii
                j = k  # 最小值索引
        if min < list[i - 1]:
            list[j] = list[i - 1]
            list[i - 1] = min
        print(list)
    print(list)

# select_sort([1, 3, 2, 8, 12, 5, 7, 3, 0])
