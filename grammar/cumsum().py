# @Time    : 2018/11/6 9:38
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : cumsum().py

from time import clock
import numpy as np
import pandas as pd

start = clock()
# cumsum()方法, 返回累加列表累计求和
# 比如一个列表是这样[1,2,3,4,5]
# 返回是这样[1,3,6,10,15]
L1 = np.array([1, 2, 3, 4, 5])  # Numpy 里面的函数, 用于Numpy 数组
L2 = L1.cumsum()
print(L2)
"""
累加cumsum和累乘cumprod主要是用来看数据的变化趋势.

累加是通过流量得到存量，比如每天销售量的多少，得到今年的销售量总量;
累乘是通过变化率来得到存量，比如有每天的数据变动趋势，通过累乘来得到当前的数据;
累加的用法:
通过df.cumsum()   来求df的累计次数;


"""
end = clock()
print('time: {:.8f}s'.format(end - start))
