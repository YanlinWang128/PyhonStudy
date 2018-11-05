# @Time    : 2018/11/5 10:03
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : _多文件合并.py.py

from time import clock
import pandas as pd
import numpy as np
from glob import glob  # read all files matching a pattern

start = clock()

for i in range(3):
    data = pd.DataFrame(np.random.randn(10, 4))
    data.to_csv('file_{}.csv'.format(i), index=False)  # to_csv index = False, 不要行索引

# files = ['file_0.csv', 'file_1.csv', 'file_2.csv']
files = glob(r'file_*.csv')
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
result.to_csv('all.csv', index=False)  # index = False, 不要行索引,输出的列标题还是有的

end = clock()
print('time: {:.8f}s'.format(end - start))
