# @Time    : 2018/11/4 14:29
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 7.dataframe的拼接.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# 逻辑条件, 返回的是 布尔型series序列
Crit1 = df.AAA <= 5.5
Crit2 = df.BBB == 10.0
Crit3 = df.CCC > -40.0
print(Crit1, Crit2, Crit3, sep='\n------\n')

AllCrit = Crit1 & Crit2 & Crit3
dfnew = df[AllCrit]
print(dfnew)

"""
如果布尔筛选条件过多,可以使用列表逐个拼接
CritList = [Crit1,Crit2,Crit3]
AllCrit = functools.reduce(lambda x,y: x & y, CritList)
df[AllCrit]
"""

# AllCrit = Crit1 & Crit2 & Crit3


end = clock()
print('time: {:.8f}s'.format(end - start))
