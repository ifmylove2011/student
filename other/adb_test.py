# -*- coding: UTF-8 -*-
import os
import subprocess

result = subprocess.call('ping -n 1 -w 100 ' + '192.168.33.85')
print(result)


result = subprocess.call('adb connect ' + '192.168.33.85:5555')
print(result)