# -*- coding: utf-8 -*-

import os
import sys
import re

candidate_file_name = r'([0-9-]+?[a-zA-z]+[0-9-]+)([\u4e00-\u9fa5\u0800-\u4e00 ]+)([_\d]?)(\S+)'


def exchange_pattern(str):
    print(str)
    result = re.match(candidate_file_name, str)
    changed_str = result.group(2) + result.group(1) + result.group(3) + result.group(4)
    return changed_str


def change_file_name(path):
    for fn in os.listdir(path):
        if re.match(candidate_file_name, fn):
            new_name = exchange_pattern(fn)
            print(new_name)
            print("-----------------------------------")
            os.rename(fn, new_name)


path = sys.argv[1]
os.chdir(path)
change_file_name(path)
