# -*- coding:UTF-8 -*-
import time
def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(get_time())