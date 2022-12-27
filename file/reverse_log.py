# -*- coding: utf-8 -*-

import base64
import os
import sys

list = []

def read_content(file):
    with open(file, 'r+', encoding='utf-8') as f:
        cache = ""
        while True:
            str = f.readline()
            if len(str) == 0:
                break
            if str.startswith("20"):
                list.append(cache)
                cache = ""
            cache = cache + str
        # print(list)
        f.seek(0)
        list.reverse()
        f.writelines(list)

path = sys.argv[1]
print("源文件路径为:" + path)
read_content(path)
