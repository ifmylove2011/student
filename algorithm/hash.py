# -*- coding: UTF-8 -*-
from collections import deque
import random

book = dict()

book['apple'] = 0.9
book['pear'] = 0.3

print(book)

# 现在9个集合，各有几个10以内的自然数，现要求尽量用到少的集合凑齐1-10的数

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
    while len(v) < random.randint(3, 5):
        v.add(random.randint(1, 10))

for k, v in set_list.items():
    print(k, v)

best_key_set = set()
num_need = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num_coverd = set()


# 每次需要拿到最多的‘可用’数字

def find_best_candidate_set():
    best_coverd = set()
    best_coverd_key = None
    for k, v in set_list.items():
        temp_coverd = num_need & v
        if len(temp_coverd) > len(best_coverd):
            best_coverd = temp_coverd
            best_coverd_key = k
    return best_coverd_key


size = len(set_list)
for i in range(size):
    want_key = find_best_candidate_set()
    best_key_set.add(want_key)
    print(set_list.pop(want_key))
