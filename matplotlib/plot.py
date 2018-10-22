# @Time    : 2018/10/17 21:39
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : plot.py
import matplotlib.pyplot as plt
import numpy as np

# plot 可以画函数图, 可以画两点图

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
# plt.figure()

# 自定义坐标轴数值,边界
plt.xlim(-1, 2)
plt.ylim(-2, 3)
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  # 进行替换新下标

# plt.yticks([-2, -1, 1, 2, ],
#            [r'$really\ bad$', '$bad$', '$well$', '$really\ well$'])


# color, red,green, blue, skyblue
l1, = plt.plot(x, y1, color='red', linewidth=2, linestyle='--', label='linear line')
l2, = plt.plot(x, y2, label='square line')  # 进行画图

# 可以绘制特殊标注 (多加一个点和一个下划线)
x0 = 0.5
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')
# 绘制下划线, 两点之间的连线(x0, y0) -> (x0, -2)
plt.plot([x0, x0], [y0, -2], 'k--', lw=2.5)  # 连接(x0,y0)(x0,0) k表示黑色 lw=2.5表示线粗细

# 如果x坐标不重要, 则用默认索引,x可以省略
# plt.plot(y, label='square line')

# 画一条
# xycoords='data'是基于数据的值来选位置
# xytext=(+30,-30), textcoords='offset points'对于标注位置描述和xy偏差值
# arrowprops对图中箭头类型设置

plt.annotate(r'$2x0+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# 添加注视text
# (-3.7,3)表示选取text位置 空格需要用\进行转译 fontdict设置文本字体
plt.text(-0.2, 2, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

# 显示图例 legend
plt.legend(loc='best')  # 显示在最好的位置
plt.title('Test')
# ax.set_title('title test',fontsize=12,color='r')
# 保存图片
# plt.savefig("D:/demo.png")
plt.show()  # 显示图
