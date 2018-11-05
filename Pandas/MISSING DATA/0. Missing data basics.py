# @Time    : 2018/11/5 15:45
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0. Missing data basics.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

# 产生缺失值
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
df['four'] = 'bar' # 新建定值列
df['five'] = df['one'] > 0 # 新建布尔列

# 重新索引, 出现空列, 即空值
df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# df2['one'] 选取一列
"""
NAN 非数,空值 Likewise, datetime containers will always use NaT.
pd.isna(df2['one'])  判断是否是空值
df2['four'].notna()
df2.isna()

s.loc[0] = None
s.loc[1] = np.nan

"""


end = clock()
print('time: {:.8f}s'.format(end - start))
