# @Time    : 2018/10/2 16:57
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : 组合数据类型.py
from random import randint


def random_list(start, stop, length):
    if length >= 0:
        length = int(length)
    else:
        print("Length is illegal!")
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(randint(start, stop))
    return random_list


# 组合数据类型
"""
1. 序列(字符串,元组,列表)
    序列类型可以用下标索引0 to (length-1), -1 to -n
2. 集合
3. 映射类型(字典)


"""
