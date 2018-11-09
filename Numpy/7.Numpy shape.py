# @Time    : 2018/11/1 21:07
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 7.Numpy shape.py

from time import clock
import numpy as np

start = clock()

a = np.arange(0, 40, 10) # [0, 40) step = 10
b = np.array([0, 1, 2])
print(a.shape, a, sep='\n', end='\n-----\n')  #

# 添加维度  维度常用技巧,添加一维, 用于加法运算
a = a[:, np.newaxis]  # adds a new axis -> 2D array

print(a)  # Numpy 维度概念
# [[ 0]
#  [10]
#  [20]
#  [30]]
print(a + b)
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]


# 矩阵扁平化和整型
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ravel())  # 扁平化, 合并为一维 [1 2 3 4 5 6]
print(a.T.ravel())  # [1 4 2 5 3 6]

print(a.shape)
b = a.ravel().reshape((2, 3))  # reshape 的参数为shape, 一个元组

print(a.reshape((2, -1)))  # (-1)表示相应的维数由程序推断

end = clock()
print('time: {:.8f}s'.format(end - start))
