# @Time    : 2018/10/17 22:47
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 动图.py

from matplotlib import animation  # 引入新模块
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)  # 数据为0~2PI范围内的正弦曲线
line, = ax.plot(x, np.sin(x))  # line表示列表


# 构造自定义动画函数animate，用来更新每一帧上x和y坐标值，参数表示第i帧
def animate(i):
    line.set_ydata(np.sin(x + i / 100))
    return line,


# 构造开始帧函数init
def init():
    line.set_ydata(np.sin(x))
    return line,


# frame表示动画长度，一次循环所包含的帧数；interval表示更新频率
# blit选择更新所有点，还是仅更新新变化产生的点。应该选True，但mac用户选择False。
ani = animation.FuncAnimation(fig=fig, func=animate, frames=200, init_func=init, interval=20, blit=False)
plt.show()
