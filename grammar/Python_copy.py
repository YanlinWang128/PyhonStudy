# @Time    : 2018/10/6 13:35
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_copy.py

import copy

Y = [1, 2, 4]
X = copy.copy(Y)  # 浅拷贝,通用复制任意类型对象

X1 = copy.deepcopy(Y)  # 深拷贝,拷贝嵌套对象(如:嵌套了一个列表的字典)的调用

