# @Time    : 2018/11/9 11:24
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 9. np_random.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()
# print(help(np.random.randn))
a = np.random.randn(3, 4)
b = np.random.random((3, 4))  # 最常用, 返回[0, 1) 之间的随机数
c = np.random.rand(3, 4)
print(a, b, c, sep='\n---\n')
end = clock()
print('time: {:.8f}s'.format(end - start))
