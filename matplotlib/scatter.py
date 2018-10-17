# @Time    : 2018/10/17 16:17
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : scatter.py

# 绘制散点图

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

# 绘图对应的x, y 坐标数据
height = [170, 179, 159, 160, 180, 164, 168, 174, 160, 183]
weight = [57, 62, 47, 67, 59, 49, 54, 63, 66, 80]

# 注意:一般都在ax中设置,不在plot中设置参数
ax = plt.subplot(111)

# 设置x, y轴刻度

# 设置x, y轴刻度显示值, x的倍数
ax.xaxis.set_major_locator(MultipleLocator(8))
ax.xaxis.set_minor_locator(MultipleLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(5))
# 设置刻度值显示格式
ax.xaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))

# 自定义显示网格(major, minor)
ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
# 散点图方法
plt.scatter(height, weight, s=80, c='r', marker='*')

# x轴字符串旋转(日期坐标斜着显示)
# for label in ax.get_xticklabels():
#     label.set_rotation(30)
#     label.set_horizontalalignment('right')

# plt.xlabel 设置x, y轴标签
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')

# plt.title  设置图像标题
plt.title('Test')

# 系统显示网格, 不要与自定义网格混合使用
# plt.grid()

# 显示图片
plt.show()

"""
生成散点图scatter函数原型：

plt.scatter(x, y, s=20, c='r' , marker = '*'
 ,camp=None, norm=None ,vim=None ,vmax=None ,
 alpha=None,linewidths=None,verts=None,
 edgecolors=None,hold=None,data=None,**kwargs)


x,y ：分别输入x和y轴对应数据组
s ：点的大小（面积），可选，默认值20
c ：点的颜色，可选，默认c=‘b’ 例：b→blue r→red k→black y→yellow g→green w→while

marker ：点的形状，可选，默认‘o’ (https://blog.csdn.net/mg2flyingff/article/details/53415353)
. ,  v > < *(五角星)

cmap ：一个Colormap实例或注册名称。可选，默认：None
norm ：数据亮度，float类型范围0-1，可选，默认：None 如果None，使用默认值normalize()。

vmin，vmax：vmin并且vmax与norm亮度数据的归一化结合使用。
如果是None，则使用颜色数组的最小和最大值。
注意：如果你通过一个norm实例，你的设置vmin，并vmax会被忽略。可选，默认：None


alpha ：点的透明度，范围0-1，值越小越透明。可选，默认None

linewidths ：线宽。可选，默认None。可输入标量或数组，若None，则使用lines.linewidth

verts ：（x，y）的顺序，可选，默认None。
如果marker为None，则这些顶点将用于构建标记。标记的中心位于（0,0）标准化单位。
整体标记被重新缩放s。
edgecolors ：可选，默认None。如果None，则采用‘face’，即边缘颜色和主颜色一致。


plt.grid() :显示网格



"""
