# @Time    : 2018/10/25 10:43
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 模型测试.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 第二阶段与第一阶段计算theta的区别
# 矩阵25阶换成24阶, y 真实值换成  y_difference

def theta_caculate():
    # 初始值
    p = np.eye(9) * (10 ** 8)
    # p = np.eye(9) * (10 ** 8)  # 每个文件重置一次
    theta = np.zeros((9, 1))
    input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_10_30.csv'
    d1 = 20

    theta_first_value = [0]
    df2 = pd.read_csv(input_path, header=0)

    print(df2.columns.values.tolist())

    # 最后一个 shift的 NAN 去掉
    y_output = df2['y_difference'].tolist()[:-1]

    u1_difference = df2['u_difference'].tolist()[:-1]
    # u2_difference = [0] * len(y_output)
    # u3_difference = [0] * len(y_output)
    # u4_difference = [0] * len(y_output)
    print(len(y_output), len(u1_difference))

    # 1* 24
    def phi_1(k):
        temp = y_output[(k - 1 - 2):(k - 4 - 2 - 1):-1]
        return np.array(
            [[x * -1 for x in temp] + u1_difference[(k - 1 - 2):(k - 1 - 3 - d1 - 2 - 1):-1][-5:] ])

    start_item = d1 + 7
    end_item = len(df2.index) - start_item

    for k in range(start_item, end_item):
        K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
        # 差值索引 - 2
        theta = theta + K * (y_output[k - 2] - phi_1(k).dot(theta))
        # print('--' * 10)
        theta_first_value.append(theta.T.tolist()[0][4])
        # print(theta.T.tolist())
        p = (np.eye(9) - K.dot(phi_1(k))).dot(p)


    print(theta.T.tolist())

    print(len(theta_first_value))

    plt.plot(theta_first_value, color='red', linewidth=2, linestyle='--', label='theta_first_value')
    # plt.legend(loc='best')  # 显示在最好的位置
    plt.title('theta_first_value')
    plt.show()  # 显示图
    # print(p.shape, p)
    # a, b = np.linalg.eig(p)
    # print(a)
    return theta
print('--' * 10)



if __name__ == '__main__':
    theta_caculate()
    # theta = [- 3.805,  5.429,- 3.443 , 0.8187,3.539e-007,1.416e-006, 2.123e-006 , 1.416e-006, 3.539e-007,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
    # print(len(theta))

    """
    8月
    [0.05159316185325485, -0.10922857036382684, -0.14436472324901706, -0.1498669840069488, -0.0009444368222509161, -0.0004519942060786499, -0.0008541718929460376, -0.0010688903224722243, -0.0013528290514800716, -0.0049229724842149115, 0.003751305990895622, -0.007965206413758766, 0.002725372598517391, -9.035943061693589e-05, 6.804195587387985e-05, 0.004414595045365892, 0.01108669220067889, 0.0011869464469076397, -0.00027937323622931825, 0.006367896271746707, 0.0033094210428302644, 0.004608977115359863, 0.00849180052290706, 0.00031829751985712414]
    """
