# -*- coding: utf-8 -*-

import os
import sys

SUFFIX_RM = '.psd'
SUFFIX_RM_CAP = '.PSD'


def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(SUFFIX_RM) or name.endswith(SUFFIX_RM_CAP):  # 指定要删除的格式，这里是jpg 可以换成其他格式
                try:
                    os.remove(os.path.join(root, name))
                    print("Delete File: " + os.path.join(root, name))
                except:
                    pass


dir = sys.argv[1]
print("源文件路径为:" + dir)
del_files(dir)
