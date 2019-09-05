# -*- coding: UTF-8 -*-

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1

    return None


# example = [1, 2, 5, 7, 12, 14, 18]
#
# print(binary_search(example, 5))
# print(binary_search(example, 6))


def select_sort(array):
    for i in range(len(array)):
        min = array[i]
        for j in range((i + 1), len(array)):
            if array[j] < min:
                min = array[j]
                array[i], array[j] = array[j], array[i]

    return array


def select_sort_1(array):
    newarray = []
    for i in range(len(array)):
        minv = min(array)
        newarray.append(minv)

    return newarray


example1 = [7, 1, 6, 3, 12, 8, 0]


# print(select_sort(example1))
# print(select_sort_1(example1))


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(example1))
