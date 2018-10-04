# @Time    : 2018/10/2 17:01
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : randomList.py

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
