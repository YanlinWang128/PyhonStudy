# @Time    : 2018/11/1 19:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 4.Numpy 索引切片拷贝.py

from time import clock
import numpy as np

start = clock()

a = np.arange(10)
b = a[::-1]  # 支持切片, 但是与Python 切片不同, numpy 切片为原始数据的
print(a, b, a[0], a[2], a[-1])  # Numpy 数组支持索引

c = np.diag(np.arange(3))
print(c[1, 1])  # 多维矩阵的索引

print(np.may_share_memory(a, b))  # True 检查是否共享内存

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
Numpy 的矩阵数组, 支持切片和索引

与 Python 序列容器不同，Numpy array 上的索引和切片只是原数据的一个视图（view）或引用，而非拷贝。
因此对索引或切片的任何更改都会反映到原始数据上。如果需要复制，用 array 的 copy 方法。
此外，可以用 
np.may_share_memory(a, b) 函数检查两个变量是否共享内存。
Numpy 中 切片会导致共享内存  b = a[::-1]

c = a[::2].copy()  # force a copy  正确的矩阵赋值,copy()函数
"""
