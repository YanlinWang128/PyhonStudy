# @Time    : 2018/10/4 20:50
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : dict.py



# 新建字典
num_mapping = dict()
# 给字典赋值
# num_mapping[nums[i]] = i
# 字典{} ,字典不是序列, 是一种key/value 映射 (mapping)
# 可变性
D = {'food': 'Span', 'quantity': 4, 'color': 'pink'}
print(D['food'])

# 无序字典有序输出
"""
D['name'] = 'Frank',  del D['name']
len(D)
key/value
Dict.keys(), list(Dict.keys()) # 键
Dict.values(), list(Dict.values()) # 值
Dict.items(), list(Dict.items())  # 获取键+值
Dict.copy # 副本
Dict.get(key, default) # 默认

因为字典不是序列,他们并不包含任何可靠的从左到右的顺序,
    这意味着如果我们建立一个字典,并将它打印出来,它的键也许会与我们输入时不同的顺序出现

--> 常用解决办法: 通过字典的keys方法收集一个键的列表,使用列表的sort方法进行排序,
        然后使用Python的for循环逐个显示结果

"""
Ks = list(D.keys())  # keys()方法构成一个列表
Ks.sort()  # 默认升序
for key in Ks:
    print(key, '=>', D[key] if key in D else 0)

# 字典是可迭代对象,可以用一个next返回后续的键
squares = [x ** 2 for x in range(5)]
print(squares)

## 字典注意项 : if测试 不存在的键
values = D['food'] if 'food' in D else 0  # D[key]
print(values)

# 字典的格式化输出
"""
%[(name)][flags][width][.precision]typecode

flags: 左对齐(-),右对齐(+),补零(0)  ==> 宽度,用于列表显示好看
[(字典键/值)]  ==>  %(key)s, %(value)s
"""
print('%s,eggs, and %+20s and %s' % (1, 'spam!', [1, 2, 3, 4]))

values = {'name': 'Bob', 'age': 40}  # 目标字典

print('name: %(name)s, age: %(age)s' % values)

# 字典, 返回字典的键/值 列表
print(list(values.keys()))  # ['name', 'age']
print(list(values.values()))  # ['Bob', 40]

# 字典更新 update()
"""
update 方法类似于合并,但是它和从左到右的顺序无关,字典无序
update 方法将字典的键和值合并到另一个字典中,盲目地覆盖相同键的值
"""
valuesupdate = {'age': 50, 'QQ': 1195441296}
values.update(valuesupdate)
print(values)  # {'name': 'Bob', 'age': 50, 'QQ': 1195441296}

# pop('QQ') 从字典中删除一个键,并返回它的值
# del D[key]
values.pop('QQ')
print(values)  # {'name': 'Bob', 'age': 50}

# 新增/修改键
values['QQ'] = 1195441296
print(values)  # 添加 {'name': 'Bob', 'age': 50, 'QQ': 1195441296}

# in 进行成员关系测试

#

