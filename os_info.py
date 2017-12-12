# -*- coding:UTF-8 -*-
def get_os_info():
    with open('/etc/issue') as fd:
        for line in fd:
            osver = line.strip()
            break
    return{'osver':osver}
print(get_os_info())