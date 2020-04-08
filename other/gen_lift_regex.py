# -*- coding: utf-8 -*-


import re

core_regex = r'L(\d+)F([B0-9]?[0-9]+)D(\d)S(\w{2})'

cmd_up_1 = "C2L1F01D3SFFL2FB1D3SFF"

m1 = re.search(core_regex, cmd_up_1)

print(m1.group(1))
print(m1.group(2))
print(m1.group(3))
print(m1.group(4))
