# @Time    : 2018/10/18 11:14
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 3D图_Axes3D.py

# 导入pyplot包，并简写为plt
import matplotlib.pyplot as plt

# 导入3D包
from mpl_toolkits.mplot3d import Axes3D

# 将绘画框进行对象化
fig = plt.figure()

# 将绘画框划分为1个子图，并指定为3D图
ax = fig.add_subplot(111, projection='3d')

# 定义X,Y,Z三个坐标轴的数据集(四个点)
X = [1, 1, 2, 2]
Y = [3, 4, 4, 3]
Z = [1, 100, 1, 1]

# 用函数填满4个点组成的三角形空间
ax.plot_trisurf(X, Y, Z)
plt.show()
