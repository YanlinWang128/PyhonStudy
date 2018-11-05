# @Time    : 2018/11/5 16:19
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 0. Concatenating objects.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

"""
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)

frames = [ process_your_file(f) for f in files ]
result = pd.concat(frames)

result = pd.concat([df1, df4], ignore_index=True) # 原来的所有忽略
"""
end = clock()
print('time: {:.8f}s'.format(end - start))
