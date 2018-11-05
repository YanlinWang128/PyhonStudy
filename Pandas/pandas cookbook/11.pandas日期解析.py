# @Time    : 2018/11/5 10:47
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 11.pandas日期解析.py

from time import clock
import pandas as pd
import numpy as np
start = clock()

i = pd.date_range('20000101',periods=10000)
df = pd.DataFrame(dict(year = i.year, month = i.month, day = i.day))
print(df.head())

ds = df.apply(lambda x: "%04d%02d%02d" % (x['year'],x['month'],x['day']),axis=1)

print(ds.head())

end = clock()
print('time: {:.8f}s'.format(end - start))