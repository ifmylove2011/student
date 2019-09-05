import os

# try:
#     f = open(r'E:/soft/java.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with语句会自动调用close
# with open(r'E:/soft/java.txt', 'r') as f:
#     for r in f.readlines():
#         print(r.strip())
# print(f.read(24))

# with open(r'E:/studying/IMG_20160216_1817161.jpg','rb') as f:
#     print(f.read())

import os

print(os.name)

print(os.environ)
print(os.environ.get('PATH'))

import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

print(get_mac_address())

import socket
#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)

print(myname,myaddr)

addrs = socket.getaddrinfo(socket.gethostname(),None)

for item in addrs:
    print(item)