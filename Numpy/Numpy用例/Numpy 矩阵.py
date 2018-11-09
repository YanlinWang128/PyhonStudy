# @Time    : 2018/11/9 13:11
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Numpy 矩阵.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()
a = 10 * np.random.rand(1, 4)
b = 10 * np.random.rand(4, 1)

# 矩阵的转置  a.T
# 矩阵对应乘, 或者直接乘   *

# 矩阵乘法
print(a.dot(b))



end = clock()
print('time: {:.8f}s'.format(end - start))