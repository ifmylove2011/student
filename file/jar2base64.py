# -*- coding: utf-8 -*-

import base64
import os
import sys
import subprocess

SUFFIX_JAR = '.jar'
SUFFIX_TXT = '.txt'


def java2dex(path):
    dst_path = os.path.join(file_path, file_name + "_dex" + file_ext)
    cmd = subprocess.Popen(
        "dx --dex --output {dst_path} {src_path}".format(dst_path=dst_path,
                                                         src_path=path), shell=True)
    cmd.wait()
    print("已转为dex:" + dst_path)
    return dst_path


def file2base64(file):
    with open(file, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        return base64_data


def save_base64_file(base64str):
    dst_path = os.path.join(file_path, file_name + "_dex" + SUFFIX_TXT)
    with open(dst_path, 'w+') as f:
        f.write(str(base64str, 'utf-8'))
        f.close()
    print("已转为base64:" + dst_path)


path = sys.argv[1]
print("源文件路径为:" + path)

file_path, full_name = os.path.split(path)
file_name, file_ext = os.path.splitext(full_name)

if file_ext != SUFFIX_JAR:
    print("不是jar包")
    exit()

# print(file2base64(java2dex(path)))
save_base64_file(file2base64(java2dex(path)))
