# @Time    : 2018/10/14 23:16
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 绘制方波.py

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys
# (1) 我们从初始化t和k开始，并将函数值初始化为0
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(100))
k = 2 * k - 1
f = np.zeros_like(t)
# (2) 接下来，直接使用sin和sum函数进行计算：
for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i])/k)
f = (4 / np.pi) * f
# (3) 绘制波形的代码和前面的教程中几乎一模一样
plot(t, f)
show()
