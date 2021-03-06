# @Time    : 2018/10/18 16:11
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 计算整月的theta.py


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def theta_caculate():
    # 初始值
    p = np.eye(25) * (10 ** 10)  # 每个文件重置一次
    theta = np.zeros((25, 1))
    input_path = r'C:/Users/Frank/Desktop/tongliu/mat_data_1101.csv'
    d1 = d2 = d3 = d4 = 20


    df2 = pd.read_csv(input_path, header=0)

    print(df2.columns.values.tolist())
    theta_first_value = [0]
    y_output = df2['y'].tolist()
    difference_length = len(df2.index) - 1
    print(difference_length)

    # u1_difference = df2['u_difference'].tolist()
    u1_difference = df2['u1_difference'].tolist()
    u2_difference = df2['u2_difference'].tolist()
    u3_difference = df2['u3_difference'].tolist()
    u4_difference = df2['u4_difference'].tolist()
    # u2_difference = [0] * difference_length
    # u3_difference = [0] * difference_length
    # u4_difference = [0] * difference_length
    # 1* 25
    def phi_1(k):
        temp = y_output[(k - 1 - 1):(k - 5 - 1 - 1):-1]
        return np.array(
            [[x * -1 for x in temp] + u1_difference[(k - 1 - 2):(k - 1 - 3 - d1 - 2 - 1):-1][
                                      -5:] + u2_difference[(k - 1 - 2):(k - 1 - 3 - d2 - 2 - 1):-1][
                                             -5:] + u3_difference[
                                                    (k - 1 - 2):(k - 1 - 3 - d3 - 2 - 1):-1][
                                                    -5:] + u4_difference[
                                                           (k - 1 - 2):(k - 1 - 3 - d4 - 2 - 1):-1][
                                                           -5:]])

    start_item = max([d1, d2, d3, d4]) + 7
    end_item = len(df2.index) - start_item

    for k in range(start_item, end_item):
        K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
        theta = theta + K * (y_output[k - 1] - phi_1(k).dot(theta))
        theta_first_value.append(theta.T.tolist()[0][5])
        p = (np.eye(25) - K.dot(phi_1(k))).dot(p)



    print(theta.T.tolist())
    # print(p.shape, p)
    # a, b = np.linalg.eig(p)
    # print('--' * 10)
    # print(a)

    plt.plot(theta_first_value, color='red', linewidth=2, linestyle='--', label='theta_first_value')
    # plt.legend(loc='best')  # 显示在最好的位置
    # plt.title('theta_sixth_value')
    plt.show()  # 显示图
    return theta


if __name__ == '__main__':
    theta_caculate()

# print()
"""
        # print(p, np.shape(p))
        # 控制参数d1, d2, d3, d4 初始化
        # 创建单位矩阵 np.eye(value)
        # identity_matrix_25 = np.eye(25)
        # print(P.T)
        # 转置 a.T
        # 零矩阵  np.zeros(tuple(x, y) , 参数必须为元组

        def phi(k):
            temp = y_output[(k - 1 - 1):(k - 1 - 5 - 1):-1]
            return np.array([x * -1 for x in temp] + u1_difference[(k - 1 - 1 - 1):(
                k - 1 - 1 - 4 - d1 - 1):-1] + u2_difference[(k - 1 - 1 - 1):(k - 1 - 1 - 4 - d2 - 1):-1] + u3_difference[
                                                                                                           (k - 1 - 1 - 1):(
                                                                                                               k - 1 - 1 - 4 - d3 - 1):-1] + u4_difference[
                                                                                                                                             (
                                                                                                                                                 k - 1 - 1 - 1):(
                                                                                                                                                 k - 1 - 1 - 4 - d4 - 1):-1])

8 月 不重置p theta
[-0.947811753254557, -0.1602734752309542, -0.03448030850601901, -0.005926564828329537, 0.1484914112222206, -0.0009167907050742148, -0.00044047889180056266, -0.0008603608454455753, -0.0010497972228475556, -0.0013690907990828963, -0.004879941649358138, 0.003607438592081519, -0.007032472427834018, 0.003372239159058352, 0.00011472812084576332, -0.0002654366964989808, 0.004595917416402356, 0.010732629284789675, 0.001118314301918791, -0.0012206028988971187, 0.005343735508116856, 0.003180975195237934, 0.0039830257801174605, 0.008527858527091375, 0.0009007565552914656]
8 重置p
[-0.9130166305850802, -0.16366567946942107, -0.08301533388572699, 0.06870030696574138, 0.0909940945319406, -0.0012545512051814628, 0.0014544399132686338, 0.0017666228809133226, 0.002020066524392353, -0.0037471861689967077, 0.11211277943474644, 0.01730450197080619, 0.057543236477990964, 0.17010521511462975, -0.18566320910540854, 0.03977242725122014, 0.04114835281539401, -0.02288171253603298, -0.018669013812583794, 0.04142331514598825, -0.0370400250168526, 0.020587779875055206, 0.052806452669436, 0.07321127940575609, -0.005193168334853946]
"""
