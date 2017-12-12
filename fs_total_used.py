#!/usr/bin/env python

def disk_stat():
    import os
    hd = {}
    disk = os.statvfs('/')
    hd['available'] = disk.f_bsize * disk.f_bavail
    hd['total'] = disk.f_bsize * disk.f_blocks
    hd['used'] = disk.f_bsize * disk.f_bfree
    return hd
print(disk_stat())
