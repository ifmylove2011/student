# -*- coding: utf-8 -*-

# 替换CLIP描述文件前缀

import os
import re
import sys

SUFFIX_TXT = '.txt'
NEW_DESC = 'cn idol'

def modifies_clip_files(path, index, word):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(SUFFIX_TXT):
                full_path = os.path.join(root,f)
                modifies_clip_content(full_path, index, word)

def modifies_clip_content(path, index, word):
    with open(path, 'r+', encoding="utf-8") as clip_f:
        old_content = clip_f.readline()
        print(old_content)
        print(index)
        # 已经有就不写入了
        if old_content.find(word) >=0 :
            return
        if len(old_content) == 0:
            return
    with open(path, 'w+', encoding="utf-8") as clip_f:
        list = old_content.split(' ')
        print(list)
        list[int(index)] = word
        new_content = ' '.join(list)
        clip_f.write(new_content)

dir = sys.argv[1]
print("源文件路径为:" + dir)
index = sys.argv[2]
word = sys.argv[3]
modifies_clip_files(dir, index, word)