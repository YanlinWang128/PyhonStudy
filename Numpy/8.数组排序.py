# @Time    : 2018/11/1 21:23
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 8.数组排序.py

from time import clock
import numpy as np

start = clock()

a = np.array([[4, 3, 5], [1, 2, 1]])
# 原地排序, 不改变维度
b = np.sort(a, axis=1)


# 排序与数组索引技巧结合：
a = np.array([4, 3, 1, 2])
j = np.argsort(a)  # [2, 3, 1, 0] 返回排序后元素的实际索引

print(a[j]) # 只能运算, 迭代 内矩阵, 得到真实的排序后值

# 找出极大、极小值对应的元素索引：
a = np.array([4, 3, 1, 2])
j_max = np.argmax(a)  # 最大值对应的索引
j_min = np.argmin(a)
print(j_max, j_min)

end = clock()
print('time: {:.8f}s'.format(end - start))
