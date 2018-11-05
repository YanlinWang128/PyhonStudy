# @Time    : 2018/11/5 14:09
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 5. Function application.py

from time import clock
import pandas as pd
import numpy as np

start = clock()
tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'], index=pd.date_range('1/1/2000', periods=10))

# 应用函数对数据进行操作, dataframe 和 series 均可
tsdf1 = tsdf.transform(lambda x: x.abs())  # 返回一个新的列表
# tsdf1 = tsdf.transform(np.abs)

# 可以应用多个函数
tedf2 = tsdf.A.transform([np.abs, lambda x: x + 1])
# 可以对每列应用不同操作
tedf3 = tsdf.transform({'A': np.abs, 'B': lambda x: x + 1})

print(tsdf1)
end = clock()
print('time: {:.8f}s'.format(end - start))
