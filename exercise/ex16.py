# 输出指定格式的日期

import time

print(time.time())

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
