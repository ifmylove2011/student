# -*- coding: UTF-8 -*-
import random

# 现有9个集合，每个集合中各有几个10以内的自然数，现要求尽量用到少的集合凑齐1-10的所有数

set_list = {}

set_list['a'] = set()
set_list['b'] = set()
set_list['c'] = set()
set_list['d'] = set()
set_list['e'] = set()
set_list['f'] = set()
set_list['g'] = set()
set_list['h'] = set()
set_list['i'] = set()
set_list['j'] = set()

for k, v in set_list.items():
    """
    初始化所有集合，每个集合均有3~5个元素，元素值在1~10之间
    """
    while len(v) < random.randint(3, 5):
        v.add(random.randint(1, 10))

for k, v in set_list.items():
    print(k, v)

# 筛选出的key集合
best_keys = set()
# 需要得到的数值集合
num_need = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def find_best_candidate_set(dict_nums, nums):
    """
    选出当前所有集合中，可得到最多‘可用’数字的一个集合(key)
    :param dict_nums: 待筛选的集合字典
    :param nums: 用于筛选的数字集合
    :return: 筛选出的key
    """
    best_coverd = set()  # 最佳的数字集合
    best_coverd_key = None  # 最佳的集合所对应的key
    for k, v in dict_nums.items():
        temp_coverd = nums & v  # 当前此集合能得到的数字集合
        if len(temp_coverd) > len(best_coverd):
            best_coverd = temp_coverd
            best_coverd_key = k
    return best_coverd_key


candidate_set_list = set_list.copy()
size = len(candidate_set_list)
for i in range(size):
    want_key = find_best_candidate_set(candidate_set_list, num_need)
    best_keys.add(want_key)
    num_need = num_need - candidate_set_list.pop(want_key)
    if len(num_need) < 1:
        print("选出的集合为{}--{},已全部得到".format(want_key, set_list[want_key], num_need))
        break
    else:
        print("选出的集合为{}--{},还剩下{}未得到".format(want_key, set_list[want_key], num_need))
