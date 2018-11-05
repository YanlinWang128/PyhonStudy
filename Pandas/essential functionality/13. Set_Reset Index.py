# @Time    : 2018/11/5 15:26
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 13. Set_Reset Index.py

from time import clock
import pandas as pd
import numpy as np

start = clock()


"""
data.reset_index(drop = True)



"""
end = clock()
print('time: {:.8f}s'.format(end - start))