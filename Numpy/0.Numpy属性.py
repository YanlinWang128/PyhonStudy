# @Time    : 2018/11/1 21:45
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0.Numpy属性.py

from time import clock
import numpy as np

start = clock()

# Numpy 包含高级代数函数
print(help(np.genfromtxt))

a = np.array([[0, 1, 2], [3, 4, 5]])
print(type(a), a.ndim, a.shape, len(a), a.size, a)

"""
type(a):    类型

# 矩阵属性
a.ndim:     维度
a.shape:    形状(元组), (各维数据个数)
a.size:     矩阵所有元素个数

# 对象属性
len(a):      对象的长度, 本例中a对象由两个列表构成,故,长度为2, 与矩阵无关的概念
count(a)     # 计算包含对象个数, 不是矩阵概念 
[1, 1, 2, 4, 1].count(1)

a.shape[0] 第一维数值
a.shape[1] 第二维,如果有的话(一位数组只有shape[0])
"""

end = clock()
print('time: {:.8f}s'.format(end - start))
