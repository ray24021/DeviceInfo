#!/usr/bin/env/ python

from __future__ import  print_function
from collections import OrderedDict

def meminfo():

    meminfo = OrderedDict()

    with open('/proc/meminfo') as fd:
        for line in fd:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo
if __name__ == '__main__':
    meminfo = meminfo()
    print('Total memory:{0}'.format(meminfo['MemTotal']))
    print('Free memory:{0}'.format(meminfo['MemFree']))
