# @Time    : 2018/10/24 16:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : plot_liu.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

input_file = r'C:/Users/Frank/Desktop/HDL181016_160904.csv'
df2 = pd.read_csv(input_file, header=0)

print(df2.columns.values.tolist())

y = df2['tongliu'].tolist()

plt.plot(y, color='blue', linewidth=2)

plt.title('tongliu')
plt.show()
