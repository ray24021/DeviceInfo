# -*- coding:UTF-8 -*-
import  socket

local_ip= socket.gethostbyname(socket.gethostname())
print('local ip:%s'%local_ip)

ip_list = socket.gethostbyname_ex(socket.gethostname())
for i in ip_list:
    if i != local_ip:
        print('external IP:%s'%i)