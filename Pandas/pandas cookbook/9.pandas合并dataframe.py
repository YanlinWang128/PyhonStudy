# @Time    : 2018/11/5 9:55
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 9.pandas合并dataframe.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

rng = pd.date_range('2000-01-01', periods=6)
df1 = pd.DataFrame(np.random.randn(6, 3), index=rng, columns=['A', 'B', 'C'])
df2 = df1.copy()

# Depending on df construction, ignore_index may be needed
# 对应合并, 选择忽略索引, 标题行会自动忽略
df = df1.append(df2, ignore_index=True)


"""
横向合并
pd.merge(df, left_on=[])
"""
print(df1, df, sep='\n------\n')

end = clock()
print('time: {:.8f}s'.format(end - start))
