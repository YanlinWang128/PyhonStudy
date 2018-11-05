# @Time    : 2018/11/5 15:53
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. Cleaning_filling missing data.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

# Filling missing values: fillna
"""
df2.fillna(0) # 固定值填充
df2['one'].fillna('missing') # 选择某列固定字符串填充


# 向前向后填充
ffill() is equivalent to fillna(method='ffill') 
bfill() is equivalent to fillna(method='bfill')
dff.fillna(dff.mean()) # 用该列的均值 填充
dff.fillna(dff.mean()['B':'C']) # 对B,C列的空值进行填充, 列均值进行填充

"""

end = clock()
print('time: {:.8f}s'.format(end - start))
