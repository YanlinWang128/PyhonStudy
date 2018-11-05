# @Time    : 2018/11/5 11:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 00.series.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()

# series pandas 数据结构
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print(s.index, s, sep='\n------\n')

# 随机序列
s1 = pd.Series(np.random.randn(5))

# 从字典生成序列
d = {'b': 1, 'a': 0, 'c': 2}
s3 = pd.Series(d)
s4 = pd.Series(d, index=['b', 'c', 'd', 'a'])

# 定值序列
s6 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])

### 序列的 特性
# 索引切片属性
print(s[0], s[:3], s[[4, 3, 1]])

# 筛选属性
print(s[s > s.median()])

# 计算属性
s11 = np.exp(s)
s12 = s + s  # 两序列相加
s13 = s * 2 # 序列数乘

s14 = s[1:] + s[:-1] # 切片实现序列错位计算

# Name attribute
s = pd.Series(np.random.randn(5), name='something')
print(s.name)
s2 = s.rename("different")


# 序列的字典属性
print(s['a'])
s['e'] = 12.  # 赋值

print('e' in s)

end = clock()
print('time: {:.8f}s'.format(end - start))
