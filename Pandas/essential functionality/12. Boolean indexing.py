# @Time    : 2018/11/5 15:18
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 12. Boolean indexing.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
s = pd.Series(range(-3, 4))
# 布尔值筛选
s1 = s[(s < -1) | (s > 0.5)]
s2 = s[~(s < 0)]


# 筛选 dataframe
"""
df[df['A'] > 0]

# 多条件筛选
criterion = df2['a'].map(lambda x: x.startswith('t'))
df2[criterion & (df2['b'] == 'x')]

df2[[x.startswith('t') for x in df2['a']]] # a 中元素, 以t开头的选中

"""

# s[s.isin([2, 4, 6])

end = clock()
print('time: {:.8f}s'.format(end - start))
