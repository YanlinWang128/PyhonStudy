# @Time    : 2018/11/5 14:41
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 8. WORKING WITH TEXT DATA.py

from time import clock
import pandas as pd
import numpy as np

start = clock()

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

"""
# 对序列进行操作
s.str.lower()
s.str.upper()
s.str.len()  # 字符串操作
s.str.strip() # 删除序列字符串前后的空格
idx.str.rstrip()
idx.str.lstrip()  # 删除序列左右的空格
"""

df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '], index=range(3))
"""
dataframe进行操作

    df.columns.str.strip()
"""
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df.head())


end = clock()
print('time: {:.8f}s'.format(end - start))
