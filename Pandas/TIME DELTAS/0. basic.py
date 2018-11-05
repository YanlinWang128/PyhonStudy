# @Time    : 2018/11/5 22:02
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0. basic.py

from time import clock

start = clock()
# Timedeltas are differences in times, expressed in difference units
# e.g. days, hours, minutes, seconds
end = clock()
print('time: {:.8f}s'.format(end - start))