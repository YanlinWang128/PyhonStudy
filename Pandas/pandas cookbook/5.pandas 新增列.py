# @Time    : 2018/11/4 14:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 5.pandas 新增列.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

df = pd.DataFrame({'AAA': [1, 2, 1, 3], 'BBB': [1, 1, 2, 2], 'CCC': [2, 1, 3, 1]})

# 直接新建一列
df['Test_1'] = df['AAA'] - 1

# 结合np.where 新建一组数据
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')

# 根据原始数据新增多列
source_cols = df.columns
new_cols = [str(x) + "_cat" for x in source_cols]
# 数据映射关系
categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie', 'low': 'hello'}
# 根据映射关系新建多列数据
df[new_cols] = df[source_cols].applymap(categories.get)
print(df)

"""
   AAA  BBB  CCC logic  AAA_cat BBB_cat  CCC_cat logic_cat
0    1    1    2   low    Alpha   Alpha     Beta     hello
1    2    1    1   low     Beta   Alpha    Alpha     hello
2    1    2    3   low    Alpha    Beta  Charlie     hello
3    3    2    1   low  Charlie    Beta    Alpha     hello
"""
end = clock()
print('time: {:.8f}s'.format(end - start))
