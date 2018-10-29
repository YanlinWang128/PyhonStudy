# @Time    : 2018/10/26 10:02
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 整月theta_y增量.py


import os
import numpy as np
import pandas as pd


# 第二阶段与第一阶段计算theta的区别
# 矩阵25阶换成24阶, y 真实值换成  y_difference
def theta_caculate():
    # 初始值
    p = np.eye(24) * (10 ** 8)  # 每个文件重置一次
    theta = np.zeros((24, 1))
    input_path = r'C:/Users/Frank/Desktop/08time_series/'
    d1 = d2 = d3 = d4 = 60

    for info in os.listdir(input_path):
        domain = os.path.abspath(input_path)  # 获取文件夹的路径
        path_file = os.path.join(domain, info)  # 将路径与文件名结合起来就是每个文件的完整路径
        df2 = pd.read_csv(path_file, header=0)

        print(df2.columns.values.tolist())

        y_difference = df2['y_difference'].tolist()

        u1_difference = df2['u1_difference'].tolist()
        u2_difference = df2['u2_difference'].tolist()
        u3_difference = df2['u3_difference'].tolist()
        u4_difference = df2['u4_difference'].tolist()

        # 1* 24
        def phi_1(k):
            temp = y_difference[(k - 1 - 2):(k - 4 - 2 - 1):-1]
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
            # 差值索引 - 2
            theta = theta + K * (y_difference[k - 2] - phi_1(k).dot(theta))
            p = (np.eye(24) - K.dot(phi_1(k))).dot(p)

        p = np.eye(24) * (10 ** 8)  # 每个文件重置一次

    print(theta.T.tolist())
    # print(p.shape, p)
    # a, b = np.linalg.eig(p)
    # print('--' * 10)
    # print(a)
    return theta


if __name__ == '__main__':
    theta_caculate()

    """
    8月
    [0.05159316185325485, -0.10922857036382684, -0.14436472324901706, -0.1498669840069488, -0.0009444368222509161, -0.0004519942060786499, -0.0008541718929460376, -0.0010688903224722243, -0.0013528290514800716, -0.0049229724842149115, 0.003751305990895622, -0.007965206413758766, 0.002725372598517391, -9.035943061693589e-05, 6.804195587387985e-05, 0.004414595045365892, 0.01108669220067889, 0.0011869464469076397, -0.00027937323622931825, 0.006367896271746707, 0.0033094210428302644, 0.004608977115359863, 0.00849180052290706, 0.00031829751985712414]
    """
