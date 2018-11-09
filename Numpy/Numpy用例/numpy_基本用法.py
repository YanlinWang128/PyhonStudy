# @Time    : 2018/11/9 11:04
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : numpy_基本用法.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()

# 指定间隔序列
# 造一个矩阵, np.arrange 造序列可以造小数数列
a = np.arange(15).reshape(3, 5)
b = np.arange(0, 3, 0.2)  # arange[0, 3) 右侧不包括, 步长可以是小数
# print(a, b, sep='\n')

# 指定 长度的序列
c = np.linspace(0, 100, 100)  # [0, 100] 左右两边都闭, 指定数目
# print(c)


# 取整 np.ceil(), np.floor()
d = np.floor(10 * np.random.rand(3, 4))
# 将多维矩阵转化为  一维array
print(type(d.ravel()), d.ravel())

d.shape = (6, 2)  # 直接指定, 类似于reshape
print(d)



print('---' * 50)
# 规定类型的矩阵
matrix  = np.ones((2, 3), dtype=np.int32)
print(matrix)

end = clock()
print('time: {:.8f}s'.format(end - start))