# -*- coding: UTF-8 -*-

import os
from tkinter import *
import tkinter.filedialog
import socket
import threading

# 获取本机电脑名
current_name = socket.getfqdn(socket.gethostname())
# 获取本机ip
current_host = socket.gethostbyname(current_name)
# 获取本机局域网
host_net = current_host[0:current_host.rfind('.') + 1]

print("本机局域网为：" + host_net)
host_start = 150
host_end = 201
port = ":5555"

# hosts = [
#     # "192.168.52.169:5555",
#     # "192.168.52.184:5555",
#     "192.168.52.189:5555",
#     # "192.168.52.198:5555",
#     "192.168.52.200:5555",
#     # "192.168.52.170:5555",
#     # "192.168.52.190:5555",
#     "192.168.52.191:5555",
#     "192.168.52.194:5555",
#     "192.168.52.176:5555",
#     # "192.168.52.197:5555",
#     # "192.168.52.196:5555",
#     # "192.168.52.188:5555",
#     # "192.168.52.179:5555",
#     # "192.168.52.195:5555",
#     "192.168.52.174:5555",
#     # "192.168.52.182:5555",
#     # "192.168.52.171:5555",
# ]


hosts = []

for num in range(host_start, host_end):
    host = host_net + str(num)
    result = os.system('ping -n 1 -w 100 ' + host)
    if result == 0:
        hosts.append(host + port)

print(hosts)

# apk_path = "E:/Projects/Gateway/app/build/outputs/apk/jinxin/debug/BeoneGateway_V1.0.1_debug.apk"
apk_path = "E:/Projects/Gateway/app/jinxin/release/BeoneGateway_V1.0.1_jinxin.apk"
apk_intent = "com.jinxin.gateway2/com.jinxin.gateway.presentation.activity.MainActivity"
apk_package = "com.jinxin.gateway2"

root_dir = "E:/工作进度/大网关2.0/cmd"


def ping(host):
    result = os.system('ping -n 1 -w 100 ' + host)
    if result == 0:
        hosts.append(host)


def gen_connect_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb connect {host}\n".format(host=host)
        content = content + "echo ---------------\n"
    content = content + "pause"
    with open(os.path.join(root_dir, "connect.bat"), "w") as f:
        f.write(content)


def gen_install_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} install -r -t {file} \n".format(host=host, file=apk_path)
        # content = content + "adb -s {host} install -r {file} \n".format(host=host, file=apk_path)
        content = content + "echo ----------{host} install success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "install.bat"), "w") as f:
        f.write(content)


def gen_start_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} shell am start -n {intent}\n".format(host=host, intent=apk_intent)
        content = content + "echo ----------{host} start success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "start.bat"), "w") as f:
        f.write(content)


def gen_kill_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} shell am force-stop {package}\n".format(host=host, package=apk_package)
        content = content + "echo ----------{host} stop success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "kill.bat"), "w") as f:
        f.write(content)


def gen_uninstall_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} uninstall {package}\n".format(host=host, package=apk_package)
        content = content + "echo ----------{host} uninstall success\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "uninstall.bat"), "w") as f:
        f.write(content)


def gen_reboot_bat():
    content = "@echo off\n"
    for host in hosts:
        content = content + "adb -s {host} reboot\n".format(host=host)
    content = content + "pause"
    with open(os.path.join(root_dir, "reboot.bat"), "w") as f:
        f.write(content)


# print(os.getcwd())
gen_connect_bat()
gen_install_bat()
gen_start_bat()
gen_kill_bat()
gen_uninstall_bat()
gen_reboot_bat()

# def main():
#     window = Tk()
#     window.title('生成adb相关bat')
#     window.geometry('300x600')

#     def delete(event):
#         listbox_hosts.delete(listbox_hosts.curselection())

#     def select_file():
#         filename = tkinter.filedialog.askopenfilename()
#         file_v.set(filename)

#     def select_dir():
#         dir = tkinter.filedialog.askdirectory()
#         dir_v.set(dir)

#     def add():
#         hosts.insert(0,entry_host.get())
#         hosts_v.set(hosts)

#     lable_host = Label(window, text='地址:', width = 4, height = 1)
#     lable_host.grid(row=0, column=0,sticky=N+S)
#     entry_host = Entry(window)
#     entry_host.grid(row=0, column=1,columnspan=6,sticky=N+S)
#     button_add_host = Button(window, text = "+", command = add)
#     button_add_host.grid(row=0,column=8,padx = 10,sticky=N+S)

#     hosts_v = StringVar()
#     listbox_hosts = Listbox(window, listvariable = hosts_v)
#     listbox_hosts.grid(row=1,column=0,columnspan=6)
#     listbox_hosts.bind('<Button-3>',delete)
#     hosts_v.set(hosts)

#     def gen():
#         gen_connect_bat()
#         gen_install_bat()
#         gen_start_bat()
#         gen_kill_bat()
#         gen_uninstall_bat()
#         print(messagebox.showinfo(title = 'info', message = '生成成功'))#提示信息对话窗

# button_add = Button(window, text = "+", width = 2,height=1, command = add)
# button_add.place(x=260,y=10)


# lable_file = Label(window, text='路径:', width = 4, height = 1)
# lable_file.place(x=10,y=430)
# entry_file = Entry(window)
# entry_file.place(x=60,y=430)
# button_file = Button(window, text = "APK路径", width = 30, command = select_file)
# button_file.place(x=10,y=430)

# button_dir = Button(window, text = "CMD目录", width = 30, command = select_dir)
# button_dir.place(x=10,y=500)

# dir_v = StringVar()
# lable_dir = Label(window, text='目录:', width = 30, height = 1, textvariable = dir_v)
# lable_dir.place(x=10,y=540)

# button_gen = Button(window, text = "生成bat", width = 30, height = 1, command = gen).pack(side='bottom')

#     window.mainloop()

# if __name__ == '__main__':
#     main()
