# @Time    : 2018/11/6 9:52
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2. bar.py

from time import clock
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start = clock()

df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar()
df2.plot.bar(stacked=True)

plt.show()

end = clock()
print('time: {:.8f}s'.format(end - start))