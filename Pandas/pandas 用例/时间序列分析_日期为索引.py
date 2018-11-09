# @Time    : 2018/11/7 23:04
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 时间序列分析_日期为索引.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()
df = pd.read_csv(r'D:/all08_.csv', parse_dates=True, index_col=0)  # 时间列为索引
df['JT66801A'].plot()  # 默认索引为时间, 画图时的横坐标
plt.show()
end = clock()
print('time: {:.8f}s'.format(end - start))