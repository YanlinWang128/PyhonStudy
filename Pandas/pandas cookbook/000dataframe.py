# @Time    : 2018/11/5 12:15
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 000dataframe.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()


# 从字典序列,生成dataframe
d = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}
df = pd.DataFrame(d)
df1 = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

print(df, df.columns, sep='\n------\n')


data2 = [{'one': 1, 'two': 2}, {'one': 5, 'two': 10, 'three': 20}]
df = pd.DataFrame(data2)

df1 = pd.DataFrame(data2, index=['first', 'second'])
df2 = pd.DataFrame(data2, columns=['one', 'two'])  # 从已有的数据里面选择 columns,只保留指定值
print(df2)
# dataframe 计算, 两列相乘
df['three'] = df['one'] * df['two']
print(df)

# del df['two'] 删除一列数据
# three = df.pop('three')

#  新的一列
df['one_trunc'] = df['one'][:2]
df['foo'] = 'bar'

# dataframe对应位置数值相加
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

df3 = df * 5 + 2
df4 = 1 / df
df5 = df ** 4

print(df + df2)


# dataframe 支持切片和转置
df6 = df[:5].T
df7 = np.exp(df)
# 矩阵乘法
df8 = df.T.dot(df)

# 从文件中读取CSV
# baseball = pd.read_csv('data/baseball.csv')

# 随机dataframe
df = pd.DataFrame(np.random.randn(3, 12))

end = clock()
print('time: {:.8f}s'.format(end - start))