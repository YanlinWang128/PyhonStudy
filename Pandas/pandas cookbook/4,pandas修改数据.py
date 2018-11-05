# @Time    : 2018/11/4 14:05
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 4,pandas修改数据.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()

# 修改指定位置
df = pd.DataFrame(np.random.randn(6, 1), index=pd.date_range('2013-08-01', periods=6, freq='B'), columns=list('A'))

# 修改指定值, df.index 绝对索引值
df.loc[df.index[3], 'A'] = np.nan

# 重设索引,空白值向前填充
df1 = df.reindex(df.index[::-1]).ffill()

print(df, df1, sep='\n------\n')

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# 筛选出小于5, 大于5 的行, 返回的仍是dataframe结构
dflow = df[df.AAA <= 5]
dfhigh = df[df.AAA > 5]

# 选择某一列满足条件的序列, 返回的是series列, 无标题
# without assignment returns a Series
newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']  # [0]series序列支持索引
newseries1 = df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA']
print(newseries)

# with assignment modifies the DataFrame
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555
df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1
end = clock()
print('time: {:.8f}s'.format(end - start))
