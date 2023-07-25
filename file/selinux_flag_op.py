# -*- coding: utf-8 -*-

"""
selinux权限的添加与删除
权限修改一般发生在以下文件中
sepolicy
    --prebuilts
        --28.0
        --32.0
        --33.0
            --private
                --service_contexts
                --untrust_app_all.te
                --system_server.te
            --public
                --service.te
    --private
        --service_contexts
        --untrust_app_all.te
        --system_server.te
    --public
        --service.te
"""

import os
import sys

# 需要添加的服务名称，须与Context.java中设置的常量保持一致
service_key = "kit"
service_name = "kit_service"

# 添加在.../private/service_context中
private_service_contexts = "{0}                                      u:object_r:{1}:s0\n".format(service_key,
                                                                                                 service_name)
# 添加在.../private/untrust_app_all.te中
private_untrust = "allow untrusted_app_all {0}:service_manager find;\n".format(service_name)
# 添加在.../public/service.te中
public_service = "type {0}, app_api_service, ephemeral_app_api_service, system_server_service, " \
                 "service_manager_type;\n".format(service_name)
# 添加在...private/system_server.te
private_system = "allow system_server {0}:service_manager find;\n".format(service_name)

# 用于定位的内容，在此行内容的下一行添加新增的服务权限内容
pre_str_public_service_te = "type activity_service"
pre_str_private_untrust_app_all_te = "cameraserver_service"
pre_str_private_service_contexts = "activity_service"
pre_str_private_system_server_te = "allow system_server cameraserver_service"

# 需要修改的权限文件
file_untrust = "untrusted_app_all.te"
file_contexts = "service_contexts"
file_service = "service.te"
file_system = "system_server.te"

# 需要修改的目录，大多服务只需要更改private目录下的权限即可
file_public = "public"
file_private = "private"


def find_selinux_file(selinux_dir, operation):
    for root, dirs, files in os.walk(selinux_dir):
        for file in files:
            parent_dir = os.path.split(root)[1]
            current_dir = os.path.join(root, file)
            operation = int(operation)
            # public目录下的service.te
            if parent_dir == file_public and file == file_service:
                if operation == 0:
                    content_del(current_dir)
                if operation == 1:
                    content_insert(current_dir, pre_str_public_service_te, public_service)
            # private目录下的service_contexts
            if parent_dir == file_private and file == file_contexts:
                if operation == 0:
                    content_del(current_dir)
                if operation == 1:
                    content_insert(current_dir, pre_str_private_service_contexts, private_service_contexts)
            # private目录下的untrust_app_all.te
            if parent_dir == file_private and file == file_untrust:
                if operation == 0:
                    content_del(current_dir)
                if operation == 1:
                    content_insert(current_dir, pre_str_private_untrust_app_all_te, private_untrust)
            # private目录下的system_server.te
            if parent_dir == file_private and file == file_system:
                if operation == 0:
                    content_del(current_dir)
                if operation == 1:
                    content_insert(current_dir, pre_str_private_system_server_te, private_system)


def content_insert(file_name, pre_str, insert_content):
    text_lines = []
    with open(file_name, 'r', encoding="ascii") as file_dst:
        text_lines = file_dst.readlines()
        if insert_content in text_lines:
            return
        index = 0
        for text in text_lines:
            # print(text)
            # 需要替换内容的行数
            index = index + 1
            if text.find(pre_str) > -1:
                break
        text_lines.insert(index, insert_content)
        print(file_name)
        print(text_lines[index - 1:index + 1])
    with open(file_name, 'w', encoding="ascii") as file_dst:
        file_dst.writelines(text_lines)


def content_del(file_name):
    text_lines = []
    with open(file_name, 'r', encoding="ascii") as file_dst:
        text_lines = file_dst.readlines()
        index = -1
        for text in text_lines:
            index = index + 1
            if text.find(service_name) > -1:
                break
        print(file_name)
        print(text_lines[index])
        del text_lines[index]
    with open(file_name, 'w', encoding="ascii") as file_dst:
        file_dst.writelines(text_lines)


# 指定目录
dst_dir = sys.argv[1]
# 指定操作，0为删除，1为添加
op = sys.argv[2]
# find_selinux_file("E:\\repository\\Share\\sepolicy", 0)
find_selinux_file(dst_dir, op)
# content_insert('service.te', pre_str_public_service_te, public_service)
# content_del('service.te')
# content_del("E:\\repository\\Share\\sepolicy\\public\\service.te")