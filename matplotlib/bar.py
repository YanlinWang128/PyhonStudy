# @Time    : 2018/10/17 22:31
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : bar.py

import matplotlib.pyplot as plt
import numpy as np

# 基本图形
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1, n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 柱状图的坐标标记值
for x, y in zip(X, Y1):  # zip表示可以传递两个值
    plt.text(x + 0.15, y + 0.02, '%.2f' % y, ha='center', va='bottom')  # ha表示横向对齐 bottom表示向下对齐
for x, y in zip(X, Y2):
    plt.text(x + 0.15, -y - 0.02, '%.2f' % y, ha='center', va='top')

plt.show()
