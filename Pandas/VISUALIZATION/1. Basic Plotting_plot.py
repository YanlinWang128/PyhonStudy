# @Time    : 2018/11/6 9:45
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 1. Basic Plotting_plot.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()

# 序列的可视化
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
# plt.figure()
df.plot()  # 再次调用绘图,绘制第二张图
plt.show()

end = clock()
print('time: {:.8f}s'.format(end - start))
