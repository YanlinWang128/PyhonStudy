# @Time    : 2018/10/31 10:22
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : join字符串拼接.py

from math import sqrt


#  注意 join 拼接的是字符串,必须配合str(x) for x in b 转为字符串

a = {1: 1, 2: 2, 3: 3}
b = sorted(list(a.keys()))  # b.sort() 不返回列表
# 列表满足迭代协议, 逐个拼接, 逗号为指定的分隔符, 用于间隔迭代器中的元素, 第一个元素之后开始出现逗号
print(','.join([str(x) for x in b]))

# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）
# 使用join 实现间隔问题最强, 可满足最后一个数字没有空格,  注意range 左闭右开
print(' '.join([str(i) for i in range(2, 100) if 0 not in [i % j for j in range(2, int(sqrt(i)) + 1)]]))
