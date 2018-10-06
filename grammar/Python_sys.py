# @Time    : 2018/10/6 14:34
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_sys.py
import sys

X = 42
Y = 42  # 不是共享引用,是不同的值,两个不同的对象
print(X == Y)  # 值相同
print(X is Y)  # True, 共享内存了,是同一对象,一个内存块


# 内存回收与缓存复用(小整数和小字符串)--> 查看被引用多少次
print(sys.getrefcount(42))  # 查看42被引用了多少次
