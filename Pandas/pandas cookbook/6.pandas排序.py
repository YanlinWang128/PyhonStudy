# @Time    : 2018/11/4 14:26
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 6.pandas排序.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
aValue = 43.0
# 按照指定规则进行排序
dfnew = df.loc[(df.CCC - aValue).abs().argsort()]
print(dfnew)

end = clock()
print('time: {:.8f}s'.format(end - start))
