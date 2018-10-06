# @Time    : 2018/10/4 16:25
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : list.py


# List 可变类型
List = [1, 2, "345", [2, 3]]  # 类表无无固定约束类型
print(List, len(List))

# List.sort() 不支持随机格式

List.reverse()
print(List)
"""
1. 列表支持: 索引,切片,类似字符串
    List.sort(reverse = True)  # 默认升序排列 supported between instances of 'str' and 'int'
    List.reverse() # 对列表翻转
    List(reversed(L))# 对列表翻转
    Len(List)
    List[i], List[i][j]
"""

# 列表解析表达式(list comprehension expression) []括起来
# 列表生成器(list, tuple, dict)
"""
列表解析,配合函数map filter reduce 函数式编程思想
    Python中有许多高级工具,列表解析是一个可选的特性,比较方便,且有速度优势
    同样,它也可以在Python的任何序列类型中发挥作用,甚至一些非列表类型


"""

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 取上述矩阵第二列
col2 = [row[1] for row in M]  # Collect the items in column 2
print(col2)
print([row[1] + 1 for row in M])  # Add 1 to each item in column 2
print([row[1] for row in M if row[1] % 2 == 0])  # Filter out odd items

print("---" * 10)

diag = [M[i][i] for i in [0, 1, 2]]  # Collect a diagonal from matrix
print(diag)

doubles = [c * 2 for c in 'spam']  # ['ss', 'pp', 'aa', 'mm'] Repeat characters in a string
print(doubles)

# 内置函数map()
print(list(map(sum, M)))  # [6, 15, 24] Map sum over items in M

# 在Python3中, 解析语法也可以用来创建集合和字典
print({sum(row) for row in M})  # {24, 6, 15} Creat a set of row sums

print({i: sum(M[i]) for i in range(3)})  # Creates key/value table of row sums

print([ord(x) for x in 'Frank'])
print({ord(x) for x in 'Frank'})
print({x: ord(x) for x in 'Frank'})

# 对于生成器,还需要多多学习

# join 字符串方法join(), 将列表合并成一个字符串
L = ['a', 'b', 'c']  # 字符列表,可以合并成字符串, 数字列表不可以
S = ''.join(L)
print(S)
S = 'wyl'.join(L)  # 字符串中间填充拼接
print(S)
