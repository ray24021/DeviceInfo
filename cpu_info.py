#_*_coding:utf-8_*_

# 获取cpu的型号和核心数
def get_cpu():
    num = 0
    with open ('/proc/cpuinfo') as fd:
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].strip().split()
                cpu_model = cpu_model[0] + ' '+ cpu_model[2]+' '+cpu_model[-1]
    return {'cpu_num':num,'cpu_model':cpu_model}
print(get_cpu())