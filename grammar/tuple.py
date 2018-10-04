# @Time    : 2018/10/4 21:57
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : tuple.py

# tuple(发音为'toople') 可以看作一个不可以改变的列表
tuple1 = (1, 2, 3, 'hello')  # empty tuple
print(type(tuple1))
print(len(tuple1))
print(tuple1 + (4, 5))
print(tuple1[2])
"""
1. 元组,不可变序列
    T[0] = 2 # wrong
    
2. 元组的关键是不可变性,元组提供了一种完整性的约束,这对于我们这里所编写的更大型程序是方便的

"""
