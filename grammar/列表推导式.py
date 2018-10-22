# @Time    : 2018/10/22 10:28
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 列表推导式.py

import os

# 列表推导式,快速求所需列表,方便快速
print([x * x for x in range(1, 11)])

# for 后面可以添加if判断, 只对都偶数进行操作
print([x * x for x in range(1, 11) if x % 2 == 0])

# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])

# 列表推导式也可以使用连个变量来生成list
# 遍历字典的每一个元素
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 判断list元素是否为字符串, list中所有的字符串变成小写,
L = ['Hello', 'World', 'IBM', 'Apple', 19]
print([s.lower() for s in L if isinstance(s, str)])

