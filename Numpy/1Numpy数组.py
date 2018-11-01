# @Time    : 2018/10/31 22:43
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1Numpy数组.py

from time import clock
import numpy as np

start = clock()

# Numpy 数组
a = np.array([0, 1, 2, 3])  # 列表 --> Numpy数组
print(type(a), a)

a = np.arange(100)  # Numpy 固定元素个数数组, n 个元素, [0, n)
print(type(a))

# 创建 Numpy 数组
## 1. 手动建立数组
a = np.array([0, 1, 2, 3])  # 一维数组
print(type(a), a.ndim, a.shape, len(a), a)

b = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array # 二维数组
print('-----' * 10)
"""
type(a), a.ndim, a.shape, len(a):  类型, 维度, 形状, 元素个数
关于形状返回一个元组, 可取维度值(行列值)
a.shape[0] 第一维
a.shape[1] 第二维,如果有的话(一位数组只有shape[0])
"""

## 2.用函数创建数组
### 2.1 等间距分布的数组:
a = np.arange(10)  # [0, n-1) (!!!attentions)
print(type(a), a)

b = np.arange(1, 9, 2)  # start, end (exclusive), step
print(type(b), b)

### 2.2 指定数量(长度)的数组:
c = np.linspace(0, 1, 6)  # [start, end], num-points
print(type(c), c)  # [0.  0.2 0.4 0.6 0.8 1. ] 包括边界产生6个数
d = np.linspace(0, 1, 5, endpoint=False)
print(d)  # [ 0. ,  0.2,  0.4,  0.6,  0.8] 不包括边界生成5个数

### 2.3 常用的数组:
a = np.ones((3, 3))  # 全1矩阵 reminder: (3, 3) is a tuple 参数为 shape, 元组
b = np.zeros((2, 2))  # 全0矩阵
c = np.eye(3)  # 单位矩阵, 参数为 ndim
d = np.diag(np.array([1, 2, 3, 4]))  # 对角矩阵,参数为 对角元素列表

### 2.4 随机数矩阵 (梅森旋转算法):
a = np.random.rand(4, 2)  # 随机样本 uniform in [0, 1), 参数为 n个逗号相隔的数字, 或者 a, 不是元组

# 生成正态分布矩阵
b = np.random.randn(4)  # Gaussian 从具有标准正态分布 的数据里面返回一个或一组样本，

"""
标准正态分布—-standard normal distribution
标准准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布，记为N（0，1）

np.random.randn()  # 当没有参数时，返回单个数据
2.5 * np.random.randn(2, 4) + 3 #生成2行4列的符合（3,2.5^2）正态分布矩阵 其中均值u=3 标准差σ=2.5
从 分布里面随机返回数据, 返回的数据不具有标准正态
"""
np.random.seed(1234)  # Setting the random seed, 在每次生成随机数之前记得设置随机数种子
"""
seed( ) 用于指定随机数生成时所用算法开始的整数值
如果使用相同的seed( )值，则每次生成的随即数都相同
如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同
设置的seed()值仅一次有效
"""
print(a, b, sum(b))

## 3. 基本数据类型

end = clock()
print('time: {:.8f}s'.format(end - start))
