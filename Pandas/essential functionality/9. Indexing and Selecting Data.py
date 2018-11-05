# @Time    : 2018/11/5 14:51
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 9. Indexing and Selecting Data.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
"""
df.where(df < 0, -df) == np.where(df < 0, df, -df)
df2[ df2[1:4] > 0] = 3

df[(df.a < df.b) & (df.b < df.c)]

"""
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

df[['B', 'A']] = df[['A', 'B']]  # 两列数据交换

# df.loc[:,['B', 'A']] = df[['A', 'B']]  # 无作用
df.loc[:, ['B', 'A']] = df[['A', 'B']].values  # 交换两列的值

# 时间索引也可以切片
# dfl.loc['20130102':'20130104']


df1 = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))

df2 = df1.loc[:, df1.loc['a'] > 0] # 选择任意行, 指定列
df3 = df1.loc[['a', 'b', 'd'], :] # 选择任意列, 指定行
df4 = df1.loc['d':, 'A':'C']

end = clock()
print('time: {:.8f}s'.format(end - start))
