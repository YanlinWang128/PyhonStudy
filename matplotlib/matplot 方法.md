
import matplotlib.pyplot as plt

#[]里的4个参数分别表示X轴起始点，X轴结束点，Y轴起始点，Y轴结束点
plt.axis([0,10,0,10])

# 可定义一部分,另一部分自适应
plt.xlim(0, 200)
plt.ylim(0, 100)



plt.ion()：打开交互模式
plt.ioff()：关闭交互模式
plt.clf()：清除当前的Figure对象
plt.cla()：清除当前的Axes对象
plt.pause()：暂停功能