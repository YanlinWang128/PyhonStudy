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
input_file = 'C:/Users/Frank/Desktop/08time_series/010.csv'

df2 = pd.read_csv(input_file, header=0)
print(df2.columns.values.tolist())
y_output = df2['T12A041A'].tolist()

u1_difference = df2['u1_difference'].tolist()
u2_difference = df2['u2_difference'].tolist()
u3_difference = df2['u3_difference'].tolist()
u4_difference = df2['u4_difference'].tolist()
# 新建指定尺寸,全为 10**8 值得列表np.full(tuple(x, y), value)
# p = np.full((25, 25), 10 ** 8)
d1 = d2 = d3 = d4 = 60

# p = np.eye(25) * (10 ** 8)
# print(p, type(p))
# theta = [-1.01575681, -0.19002532, -0.05443981, 0.09605609, 0.16415831, -0.00205784, 0.00405411, 0.00217475, 0.00519341,
#          0.00390873, 0.31140836, 0.08590223, 0.18611989, -0.25154623, 0.26859639, 0.08872846, 0.04026616, 0.01721728,
#          0.01538795, -0.00243144, 0.01539683, -0.01631048, 0.00823702, -0.07188604, 0.04221205]

# p不重置theta
# theta = [-0.947811753254557, -0.1602734752309542, -0.03448030850601901, -0.005926564828329537, 0.1484914112222206,
#          -0.0009167907050742148, -0.00044047889180056266, -0.0008603608454455753, -0.0010497972228475556,
#          -0.0013690907990828963, -0.004879941649358138, 0.003607438592081519, -0.007032472427834018,
#          0.003372239159058352, 0.00011472812084576332, -0.0002654366964989808, 0.004595917416402356,
#          0.010732629284789675, 0.001118314301918791, -0.0012206028988971187, 0.005343735508116856, 0.003180975195237934,
#          0.0039830257801174605, 0.008527858527091375, 0.0009007565552914656]

# p重置 8月
theta = [-0.9648316320082286, -0.1764996517983543, -0.041078553428172376, 0.0716756301123777, 0.11073054445846547,
         -0.0027792193428227033, -0.0002919923550244909, 0.0018055779929440673, 0.001814446780724785,
         0.0008521408197959341, 0.19229203767432215, 0.05710577944281584, 0.03176724235467315, 0.05486480797998442,
         0.23746538078352436, -0.008069747231573141, 0.032545630720906285, 0.02894162912977465, -0.043983633378221004,
         -0.04533933224782832, 0.004952484793004483, -0.03711545374217406, 0.010212119204492118, 0.08337310150688759,
         0.03426697699059536]

# theta = [-0.9029480111671384, -0.16503698879737178, -0.03424944594539166, 0.07284690911381228, 0.02938588806486347,
#          -0.0014456847406357379, 0.002115590437710819, 0.0010846521986086497, 0.0008478601902866012,
#          -0.002130105791762442, 0.012999753427970972, -0.05422752155261134, -0.015329473306421218, 0.2042414983329011,
#          -0.21055033554233857, 0.040480245562364986, 0.03543423061205737, -0.024597124147032152, -0.022184427493531455,
#          0.048293656763363814, -0.017177130563323994, 0.024175591833472104, 0.08195463940153712, 0.022963894800442405,
#          0.026008763881279533]
# print(theta)



# print(y_k, y_output[19], y_k - y_output[19])

start_item = max([d1, d2, d3, d4]) + 10
end_item = len(df2.index) - start_item - 10
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
print(y)
for item in range(start_item, end_item):
    y_predict(item, y)
print(y)

# 够不到,所以全部取了数据
print(len(y[5:]), y[5:])
print(len(y_output[start_item - 1:end_item - 1]), y_output[start_item - 1:end_item - 1])

# 计算 误差(均方误差)
#  c = [a[i] - b[i] for i in range(len(a))]
# sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)
predict_value = y[5:]
primary_value = y_output[start_item - 1:end_item - 1]
error_value = math.sqrt(sum([(y - x) ** 2 for x, y in zip(predict_value, primary_value)]) / len(predict_value))

print(error_value)

x = np.linspace(1, end_item - start_item, end_item - start_item)
print(x)

ax = plt.subplot(111)
plt.plot(x, y[5:], color='red', linewidth=2, linestyle='--', label='predicted value')
plt.plot(x, y_output[start_item - 1:end_item - 1], label='real value')  # 进行画图

plt.xlim(0, end_item - start_item)
ax.xaxis.set_major_locator(MultipleLocator(100))
plt.title('1')
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
