# @Time    : 2018/11/5 16:03
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 2, Drop Missing.py

from time import clock
import pandas as pd
import numpy as np
start = clock()

"""
df.dropna(axis=0) 删除有空值的行, 默认为 0 
            df.dropna(inplace=True) 设置inplace = True 可以直接修改, 不然都是返回
df.dropna(axis=1) 删除有空值的列


data.dropna(subset=["C"]) # 删除某列含有空白值的行
 data.dropna(thresh=2)  # 删除行的缺失值个数大于指定阈值的行
 data.dropna(how="all") # 删除全为空值的行
"""

end = clock()
print('time: {:.8f}s'.format(end - start))