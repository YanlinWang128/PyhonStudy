# @Time    : 2018/11/5 16:10
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 4. count Missing.py

from time import clock
import pandas as pd
import numpy as np
start = clock()
"""
统计 缺失值

data.isnull().sum() 列
data.isnull().sum(axis = 1) 行

"""
end = clock()
print('time: {:.8f}s'.format(end - start))