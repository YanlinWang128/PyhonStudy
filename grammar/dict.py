# @Time    : 2018/10/4 20:50
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : dict.py

# 字典{} ,字典不是序列, 是一种key/value 映射 (mapping)
# 可变性
D = {'food': 'Span', 'quantity': 4, 'color': 'pink'}
print(D['food'])

# 无序字典有序输出
"""
因为字典不是序列,他们并不包含任何可靠的从左到右的顺序,
    这意味着如果我们建立一个字典,并将它打印出来,它的键也许会与我们输入时不同的顺序出现

--> 常用解决办法: 通过字典的keys方法收集一个键的列表,使用列表的sort方法进行排序,
        然后使用Python的for循环逐个显示结果

"""
Ks = list(D.keys())  # keys()方法构成一个列表
Ks.sort()
for key in Ks:
    print(key, '=>', D[key] if key in D else 0)

# 字典是可迭代对象,可以用一个next返回后续的键
squares = [x ** 2 for x in range(5)]
print(squares)

## 字典注意项 : if测试 不存在的键
values = D['food'] if 'food' in D else 0  # D[key]
print(values)