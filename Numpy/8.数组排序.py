# @Time    : 2018/11/1 21:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 8.数组排序.py

from time import clock
import numpy as np
start = clock()

a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)




end = clock()
print('time: {:.8f}s'.format(end - start))