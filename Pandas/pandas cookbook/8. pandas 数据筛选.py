# @Time    : 2018/11/4 14:44
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 8. pandas 数据筛选.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# 注意,按照条件筛选    索引是筛选前的索引, 可以重设索引
df1 = df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))]
df2 = df1.reset_index(drop=True)
# 反向条件筛选 inverse operator (~)
df3 = df[~((df.AAA <= 6) & (df.index.isin([0, 2, 4])))]

# 重设索引

print(df1, df2, df3, sep='\n------\n')

# 按照索引筛选df.iloc[1:3]和df.loc[1:3] 区分
"""
df.iloc[1:3] # 面向绝对逻辑位置(0-n), 左闭右开, 不可用于布尔索引
df1 = df.loc['bar':'kar']  # df.loc 面向设置的索引值, 完全匹配, 左右皆闭,两端都包括, 可用于布尔值
df.loc[1:3]  # 面向索引值,两端都包括
"""
df3 = df.loc[1:]

# 自定义索引类似
data = {'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]}
df = pd.DataFrame(data=data, index=['foo', 'bar', 'boo', 'kar'])
print(df, sep='\n------\n')
df1 = df.loc['bar':'kar']  # df.loc 面向索引值, 完全匹配, 左右皆闭,两端都包括, 可用于布尔值
df2 = df.iloc[0:3]  # df.iloc[1:3] 面向逻辑位置, 左闭右开, 不可用于布尔索引

end = clock()
print('time: {:.8f}s'.format(end - start))
