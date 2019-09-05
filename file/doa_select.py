# -*- coding: utf-8 -*-

# 死或生的DLC添加......

import os
import re
import shutil

# 备份



# 需要写入的内容
file_src_path = "H:/Games/Dead or Alive 5 Last Round/3DMGAME.ini";
file_path = "H:/Games/Dead or Alive 5 Last Round/DLC"
file_dst_path = "H:/Games/Dead or Alive 5 Last Round/3DMGAME01.ini"

file_src_list = os.listdir(file_path)

shutil.copy(file_src_path, "H:/Games/Dead or Alive 5 Last Round/3DMGAME.ini.bak")

file_content = ''
for i in range(1, len(file_src_list) + 1):
    file_content += "DLC" + str(i).zfill(3) + "=" + file_src_list[i - 1] + '\r\n'

print(file_content)

file_all_content = []

with open(file_src_path, 'r', encoding="utf-8") as file_dst:
    # text = file_dst.read()
    # info = re.findall(r'DLC\d{3}=\d+',text)
    # print(info)
    text_lines = file_dst.readlines()
    focus_list = []
    for ii in text_lines:
        # 需要替换内容的行数
        if re.search(r'DLC\d{3}=\d+', ii) is not None:
            focus_list.append(text_lines.index(ii))

    # 替换内容与原内容拼接
    for ii in text_lines[0:focus_list[0]]:
        file_all_content.append(ii)
    file_all_content.append(file_content)
    for ii in text_lines[focus_list[len(focus_list) - 1] + 1:]:
        file_all_content.append(ii)

with open(file_dst_path, 'a', encoding="utf-8") as file_dst:
    for ii in file_all_content:
        file_dst.write(ii)
