# 暂停一秒输出，并格式化当前时间。

import datetime
import time

for i in range(10):
    time.sleep(1)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # t = time.time()
    # nowTime = lambda: int(round(t * 1000))
    # print(nowTime())
    print(datetime.datetime.now())
