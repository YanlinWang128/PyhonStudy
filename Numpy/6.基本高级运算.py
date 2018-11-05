# @Time    : 2018/11/1 20:52
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 6.基本高级运算.py

from time import clock
import numpy as np

start = clock()

# 求和 np.sum(x)
x = np.array([1, 2, 3, 4])
print(np.sum(x))

# 按行、列分别求和：
x = np.array([[1, 1], [2, 2]])
x.sum(axis=0)  # 按列求和（第一维）
x.sum(axis=1)  # 按行求和（第二维）

# 找到具体的某一行,列
print(x[0, :].sum(), x[1, :].sum())
print(x[:, 0].sum(), x[:, 1].sum())

# 极值：最大最小值,及其索引
x = np.array([1, 3, 2])
print(x.min(), x.argmin())  # 最小值及最小值对应的索引
print(x.max(), x.argmax())

# 逻辑运算,用于各种数据判断 np.all(), np.any()
print(np.all([True, True, False]))  # 全部满足
print(np.any([True, True, False]))  # 存在满足

a = np.zeros((100, 100))
print(np.any(a != 0))
print(np.all(a == a))

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
# 判断数组间的组合逻辑是否满足
print(((a <= b) & (b <= c)).all())

# 统计运算
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
# 均值
print(x.mean())

# 中位数
print(np.median(x))
print(np.median(y, axis=-1))  # last axis

# 整体标准差
print(x.std()) # numpy 标准差默认有偏估计
"""
& 与运算: 两位同时为“1”，结果才为“1”，否则为0
| 或运算: 参加运算的两个对象只要有一个为1，其值为1。
"""
end = clock()
print('time: {:.8f}s'.format(end - start))
