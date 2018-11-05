# @Time    : 2018/11/2 9:15
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 3. pandas if_then修改数据.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# if-then, 选择并修改值,返回的是dataframe
df.loc[df.AAA >= 5, 'BBB'] = -1
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555
df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000

# 结合np.where 新建一组数据
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')

print(df)
end = clock()
print('time: {:.8f}s'.format(end - start))
