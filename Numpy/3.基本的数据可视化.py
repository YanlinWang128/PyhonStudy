# @Time    : 2018/11/1 15:24
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 3.基本的数据可视化.py

from time import clock
import numpy as np
import matplotlib.pyplot as plt  # the tidy way

start = clock()

# 一维图像
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.plot(x, y, 'ro')
# plt.show()  # <-- shows the plot (not needed with interactive plots)
#

# 二维图像 (比如常见的图片):
plt.figure()  # 第二张图,新建一张空白图进行绘制

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()

plt.show()  # 最后再展示, 多个show会阻断

end = clock()
print('time: {:.8f}s'.format(end - start))

"""
Matplotlib 是一个2D的画图包
plt.plot(x, y)

plt.figure()  # 第二张图,新建一张空白图进行绘制
plt.show()
"""
