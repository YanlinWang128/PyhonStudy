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

        start_item = max([d1, d2, d3, d4]) + 10
        end_item = len(df2.index) - start_item - 10

        for k in range(start_item, end_item):
            K = p.dot(phi_1(k).T) * ((1 + phi_1(k).dot(p).dot(phi_1(k).T)) ** -1)
            theta = theta + K * (y_difference[k - 1] - phi_1(k).dot(theta))
            p = (np.eye(24) - K.dot(phi_1(k))).dot(p)

            # p = np.eye(24) * (10 ** 8)  # 每个文件重置一次

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
    [-0.08780512232924213, -0.11604740889584927, -0.14629506388824715, -0.1570926779801481, -0.0004572364757620897, -0.0005731055896386692, -0.001063995755046117, -0.0009729904661070823, -0.0007995613133882011, 0.006173057304574618, -0.006828011659192101, 0.0037778889764547583, 0.0011250045521910051, 0.006923926597297746, 0.004418834561410292, 0.009655341928164137, 0.00054382400185421, -0.0013384846954432898, -0.0009030995678626556, 0.004621108052490341, 0.0048104551617392565, 0.00608990561131986, -0.0036942619767968525, 0.005483244486838071]
    """
