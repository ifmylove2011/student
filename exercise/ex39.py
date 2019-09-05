# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

org = list(range(1, 10))
print(org)


def insert_and_sort(list, num):
    # 考虑顺序逆序
    so = sort_flag(list)
    j = 0
    while j < len(list) - 1:
        if so:
            if num > list[j]:
                j += 1
                break
        else:
            if num < list[j]:
                j += 1
                break
    list.insert(j, num)
    return list


def sort_flag(list):
    for i in range(len(list)):
        if i < len(list) - 1:
            if list[i] > list[i + 1]:
                return False
            if list[i] < list[i + 1]:
                return True


print(insert_and_sort(org, 2))
