# @Time    : 2018/10/22 10:13
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 迭代.py


"""
迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。
每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。

如果给定一个list或tuple
我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）

在Python中，迭代是通过for ... in来完成的
而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：

for (i=0; i<list.length; i++) {
    n = list[i];
}


字典也可作为迭代对象
for key in d:
for value in d.itervalues()
for k, v in d.iteritems()
字符串也是可迭代对象
for ch in 'ABC'


任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
只要符合迭代条件，就可以使用for循环
"""
# 对list实现下标循环
# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print('---' * 20)
# 在 for循环里面同时引用连个变量,在Python里面很常见,多多使用
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
