# @Time    : 2018/10/6 16:18
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 函数式编程.py

# 函数式编程
"""
map,reduce,列表推导式
"""
# map(function, iter1, iter2...)
list1 = [-1, -3, 8, -7, 9, -2]
L1 = list(map(abs, list1))
print(L1)  # [1, 3, 8, 7, 9, 2]
L2 = list(map(lambda x: x + 1, list1))
print(L2)
L3 = list(map(lambda x, y: x * y, list1, list1))
print(L3)  # [1, 9, 64, 49, 81, 4]
