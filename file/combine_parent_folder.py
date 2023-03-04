# -*- coding: utf-8 -*-

# 将子目录中的所有文件合并到上层目录去，并删除子目录

import os
import sys
import shutil

def merge_sub(dir):
    dir_delete = []
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            dir_delete.append(os.path.join(root,d))
        for f in files:
            src_path = os.path.join(root,f)
            dst_path = os.path.join(dir,f)
            # print(src_path)
            # print(dst_path)
            shutil.move(src_path,dst_path)
    for d in dir_delete:
        shutil.rmtree(d)
        


dir = sys.argv[1]
merge_sub(dir)