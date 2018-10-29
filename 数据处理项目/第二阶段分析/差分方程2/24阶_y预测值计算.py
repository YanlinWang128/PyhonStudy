# @Time    : 2018/10/29 12:54
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 24阶_y预测值计算.py

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

# import sys
# # 修改 递归深度,指标不治本,TODO
# sys.setrecursionlimit(1000000) #例如这里设置为一百万
# 最原始的数据打开有中文,按照gbk打开
input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_10_29.csv'

df2 = pd.read_csv(input_path, header=0)
print(df2.columns.values.tolist())
y_difference = df2['y_difference'].tolist()[:-1]
y_real = df2['y'].tolist()

# print(y_real)
print('---' * 10)

u1_difference = df2['u_difference'].tolist()[:-1]
# print(len(y_difference), y_difference)
# print('---' * 10)

u2_difference = [0] * len(u1_difference)
u3_difference = [0] * len(u1_difference)
u4_difference = [0] * len(u1_difference)
print(u2_difference)
print(len(y_real), len(y_difference), len(u1_difference), len(u2_difference))
# 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
# p = np.full((25, 25), 10 ** 8)
d1 = d2 = d3 = d4 = 20

# p = np.eye(25) * (10 ** 8)
# print(p, type(p))

# p重置 8月
theta = [-2.2570328402518958, 0.8701593980149103, 1.0361096609980656, -0.6490337085632232, -1.409490634127119e-06,
         -1.1743495557162837e-06, 1.5947983150841266e-06, 5.520506935285596e-06, 6.5048692196787466e-06, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
print('{:.10f}'.format(1.416e-006))
print('hello---', theta, max(theta), min(theta))

# print(y_k, y_output[19], y_k - y_output[19])

start_item = max([d1, d2, d3, d4]) + 7
end_item = len(df2.index) - start_item
# start_item = 20

# y(k)--->  y_index_5 = start_item
y_dif = [(y_difference[start_item - 4 - 2]), (y_difference[start_item - 3 - 2]), (y_difference[start_item - 2 - 2]),
         (y_difference[start_item - 1 - 2])]


def y_predict(k, y_dif):
    # 迭代使用增量
    b = k - start_item
    y_k = -theta[0] * y_dif[3 + b] - theta[1] * y_dif[b + 2] - theta[2] * y_dif[b + 1] - theta[3] * y_dif[
        b + 0] + theta[4] * u1_difference[k - 1 - (d1 - 1) - 2] + theta[5] * u1_difference[
        k - 1 - d1 - 2] + theta[6] * u1_difference[k - 1 - (d1 + 1) - 2] + theta[7] * u1_difference[
        k - 1 - (d1 + 2) - 2] + theta[8] * u1_difference[k - 1 - (d1 + 3) - 2] + theta[9] * u2_difference[
        k - 1 - (d2 - 1) - 2] + theta[10] * u2_difference[
        k - 1 - (d2) - 2] + theta[11] * u2_difference[k - 1 - (d2 + 1) - 2] + theta[12] * u2_difference[
        k - 1 - (d2 + 2) - 2] + theta[13] * u2_difference[k - 1 - (d2 + 3) - 2] + theta[14] * u3_difference[
        k - 1 - (d3 - 1) - 2] + theta[15] * u3_difference[
        k - 1 - (d3) - 2] + theta[16] * u3_difference[k - 1 - (d3 + 1) - 2] + theta[17] * u3_difference[
        k - 1 - (d3 + 2) - 2] + theta[18] * u3_difference[k - 1 - (d3 + 3) - 2] + theta[19] * u4_difference[
        k - 1 - (d4 - 1) - 2] + theta[20] * u4_difference[
        k - 1 - (d4) - 2] + theta[21] * u4_difference[k - 1 - (d4 + 1) - 2] + theta[22] * u4_difference[
        k - 1 - (d4 + 2) - 2] + theta[23] * u4_difference[k - 1 - (d4 + 3) - 2]
    print(y_k)
    y_dif.append(y_k)
    return y_k


# print(y_predict(20, y))
# print(y_dif)
for item in range(start_item, end_item):
    y_predict(item, y_dif)
# print(max(y_dif), min(y_dif), y_dif)

temp = y_real[start_item - 1 - 1]

y_predicted_value = []

for k in range(start_item, end_item):
    print(k)
    # start_item 时刻对应 y_dif 索引4
    temp = y_dif[k - start_item + 4] + temp
    y_predicted_value.append(temp)

print(y_predicted_value)

#
# # 计算 误差(均方误差)
# #  c = [a[i] - b[i] for i in range(len(a))]
# # sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)


# 误差分析区
predict_value = y_predicted_value

primary_value = y_real[start_item - 1:end_item - 1]
print(len(predict_value), len(primary_value))
error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))

print(error_value)

# x = np.linspace(1, end_item - start_item, end_item - start_item)
# print(x)

# 绘图区
ax = plt.subplot(111)
plt.plot(predict_value, color='red', linewidth=2, linestyle='--', label='predicted value')

plt.plot(primary_value, label='real value')  # 进行画图
print('---' * 10)
print(primary_value)

print(max(predict_value))

# plt.xlim(start_item, end_item)
# ax.xaxis.set_major_locator(MultipleLocator(100))
plt.title('2')
plt.legend(loc='best')
plt.show()
