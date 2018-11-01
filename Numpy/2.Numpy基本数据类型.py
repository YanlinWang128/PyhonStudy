# @Time    : 2018/11/1 9:47
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2.Numpy基本数据类型.py

from time import clock
import numpy as np

start = clock()

a = np.array([1, 2, 3])
print(a.dtype)  # int32
b = np.array([1., 2., 3.])
print(b.dtype)  # float64
c = np.array([1, 2, 3], dtype=float)
print(c.dtype)  # float64
# 默认的数据类型是浮点数:
a = np.ones((3, 3))
print(a.dtype) # float64


end = clock()
print('time: {:.8f}s'.format(end - start))
"""
某些数组元素后面会跟着一个小数点 (比如 2. vs 2)。这是由于不同的数据类型所致:

不同的数据结构可以让我们更加高效地使用内存，但是通常来说我们用浮点数就够了。
Numpy会自动检测输入的数据类型, 也可以显示的指定数据类型
其他的数据类型:
复数:  d = np.array([1+2j, 3+4j, 5+6*1j])   complex128
布尔值:  e = np.array([True, False, False, True]) bool
字符串: f = np.array(['Bonjour', 'Hello', 'Hallo',]) S7
int32
int64
uint32
uint64
"""
