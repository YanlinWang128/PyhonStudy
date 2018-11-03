# @Time    : 2018/11/02 10:26
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
# # 修改 递归深度,指标不治本,
# sys.setrecursionlimit(1000000) #例如这里设置为一百万
# 最原始的数据打开有中文,按照gbk打开
input_file = r'C:/Users/Frank/Desktop/tongliu/mat_data_1101.csv'

df2 = pd.read_csv(input_file, header=0)
print(df2.columns.values.tolist())

y_output = df2['y'].tolist()

difference_length = len(df2.index) - 1  # difference 长度
print(difference_length)

# u1_difference = df2['u_difference'].tolist()
#
# u2_difference = [0] * difference_length
# u3_difference = [0] * difference_length
# u4_difference = [0] * difference_length
u1_difference = df2['u1_difference'].tolist()
u2_difference = df2['u2_difference'].tolist()
u3_difference = df2['u3_difference'].tolist()
u4_difference = df2['u4_difference'].tolist()

# 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
# p = np.full((25, 25), 10 ** 8)
d1 = d2 = d3 = d4 = 20


# p重置 8月
theta = [-1.812024541833067, 0.10404043999009101, 0.749915335797866, 0.43910059080110575, -0.48103182804632805, -4.494698487992597e-08, 0.031511426041795625, 0.004809593049759339, -0.017665898738567946, -0.015715561403758568, -4.508851257469083e-08, 0.03151142620377016, 0.004809559294596981, -0.017665899861469457, -0.015715581577695245, -4.505243987549534e-08, 0.0315114260619676, 0.0048095666365651595, -0.01766588648695774, -0.01571553040440604, -4.483687900132392e-08, 0.0315114260075615, 0.00480962190695222, -0.017665894070616535, -0.015715582352740943]
print(len(theta))




# print(y_k, y_output[19], y_k - y_output[19])

start_item = max([d1, d2, d3, d4]) + 7
end_item = len(df2.index) - start_item
# end_item = 1000

# start_item = 20

# y(k)--->  y_index_5 = start_item
y = [(y_output[start_item - 6]), (y_output[start_item - 5]), (y_output[start_item - 4]), (y_output[start_item - 3]),
     (y_output[start_item - 2])]


def y_predict(k, y):
    b = k - start_item
    y_k = -theta[0] * y[4 + b] - theta[1] * y[b + 3] - theta[2] * y[b + 2] - theta[3] * y[
        b + 1] - theta[4] * y[b] + theta[5] * u1_difference[k - 1 - (d1 - 1) - 2] + theta[6] * u1_difference[
        k - 1 - (d1) - 2] + theta[7] * u1_difference[k - 1 - (d1 + 1) - 2] + theta[8] * u1_difference[
        k - 1 - (d1 + 2) - 2] + theta[9] * u1_difference[k - 1 - (d1 + 3) - 2] + theta[10] * u2_difference[
        k - 1 - (d2 - 1) - 2] + theta[11] * u2_difference[
        k - 1 - (d2) - 2] + theta[12] * u2_difference[k - 1 - (d2 + 1) - 2] + theta[13] * u2_difference[
        k - 1 - (d2 + 2) - 2] + theta[14] * u2_difference[k - 1 - (d2 + 3) - 2] + theta[15] * u3_difference[
        k - 1 - (d3 - 1) - 2] + theta[16] * u3_difference[
        k - 1 - (d3) - 2] + theta[17] * u3_difference[k - 1 - (d3 + 1) - 2] + theta[18] * u3_difference[
        k - 1 - (d3 + 2) - 2] + theta[19] * u3_difference[k - 1 - (d3 + 3) - 2] + theta[20] * u4_difference[
        k - 1 - (d4 - 1) - 2] + theta[21] * u4_difference[
        k - 1 - (d4) - 2] + theta[22] * u4_difference[k - 1 - (d4 + 1) - 2] + theta[23] * u4_difference[
        k - 1 - (d4 + 2) - 2] + theta[24] * u4_difference[k - 1 - (d4 + 3) - 2]
    y.append(y_k)
    return y_k


# print(y_predict(20, y))
# print(y)
# print(end_item -start_item, )
for item in range(start_item, end_item):
    y_predict(item, y)
# print(y)
print(y[5:10])
# 够不到,所以全部取了数据
# print(len(y[5:]), y[5:])
# print(len(y_output[start_item - 1:end_item - 1]), y_output[start_item - 1:end_item - 1])

# 计算 误差(均方误差)
#  c = [a[i] - b[i] for i in range(len(a))]
# sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)
predict_value = y[5:]
primary_value = y_output[start_item - 1:end_item - 1]

print(len(predict_value), len(primary_value))
def error_caculate(primary_value, predict_value):
    return 1 - (np.std(np.array(predict_value[1:]) - np.array(primary_value[:-1]) -(np.array(primary_value[1:] - np.array(primary_value[:-1]))),  ddof = 1) /np.std(np.array(primary_value[1:])- np.array(primary_value[:-1]),  ddof = 1))
    # error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))
print(error_caculate(primary_value, predict_value))








# x = np.linspace(1, end_item - start_item, end_item - start_item)
# print(x)

ax = plt.subplot(111)
plt.plot(predict_value, color='red', linewidth=2, linestyle='--', label='predicted value')
plt.plot(y_output[start_item - 1:end_item - 1], label='real value')  # 进行画图

# plt.xlim(0, end_item - start_item)
# ax.xaxis.set_major_locator(MultipleLocator(100))
# plt.title('2')
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
