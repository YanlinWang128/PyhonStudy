# @Time    : 2018/10/19 10:14
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : y预测值计算.py


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
input_file = 'C:/Users/Frank/Desktop/08time_series/002.csv'

df2 = pd.read_csv(input_file, header=0)
print(df2.columns.values.tolist())
y_difference = df2['y_difference'].tolist()
y_real = df2['T12A041A'].tolist()

u1_difference = df2['u1_difference'].tolist()
u2_difference = df2['u2_difference'].tolist()
u3_difference = df2['u3_difference'].tolist()
u4_difference = df2['u4_difference'].tolist()
# 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
# p = np.full((25, 25), 10 ** 8)
d1 = d2 = d3 = d4 = 60

# p = np.eye(25) * (10 ** 8)
# print(p, type(p))

# p重置 8月
theta = [0.00564013680068839, -0.17202757669162672, -0.21932053445642546, -0.13976595527008898, -0.0016980855170703457,
         0.0016988105455841489, 0.0009205114018056489, 0.0016186526527214957, -0.0030253265514904554,
         0.06967370258663634, 0.06090075229699723, 0.09336501131149037, 0.204699850000585, -0.1543592650265404,
         0.031119321176905145, 0.022526701011747828, -0.033988854338333666, -0.021118486971936627, 0.039133552076544065,
         -0.043123934685590073, -0.0028152349562239006, 0.08060445846927022, 0.03775065925979137, 0.025325018902505925]

# print(theta)



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
    y_dif.append(y_k)
    return y_k


# print(y_predict(20, y))
print(y_dif)
for item in range(start_item, end_item):
    y_predict(item, y_dif)
print(y_dif, max(y_dif), min(y_dif))

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

plt.xlim(start_item, end_item)
# ax.xaxis.set_major_locator(MultipleLocator(100))
plt.title('2')
plt.legend(loc='best')
plt.show()

# 时刻关系对应, start_item 的预测值索引是y5
# print(y[13], y_output[20 -1], y[13]-y_output[20 -1])
"""
[[-1.01575681 -0.19002532 -0.05443981  0.09605609  0.16415831 -0.00205784
   0.00405411  0.00217475  0.00519341  0.00390873  0.31140836  0.08590223
   0.18611989 -0.25154623  0.26859639  0.08872846  0.04026616  0.01721728
   0.01538795 -0.00243144  0.01539683 -0.01631048  0.00823702 -0.07188604
   0.04221205]]
   


for k in range(20, 1001):
    K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
    # print(k, K)
    theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
    print(k-19, theta.T)
    p = (np.eye(25) - K.dot(phi_1(k))).dot(p)

"""
