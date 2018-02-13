# coding:utf-8
import socket

# 创建socket，绑定指定的IP和端口
# SOCK_DFRAM 指定了这个socket的类型是UDP，绑定端口9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print("Bind UDP on 9999...")
while True:
    # 直接发送数据和接收数据
    data, addr = s.recvfrom(1024)
    print("Received from %s:%s" % addr)
    s.sendto(b'Hello, %s!' % data, addr)