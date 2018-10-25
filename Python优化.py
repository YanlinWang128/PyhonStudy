# @Time    : 2018/10/6 20:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python优化.py


n, a, b = 0, 0, 1

# Numpy 数组矢量比pandas series 更快

# pandas  向量化计算,比循环 计算 效率高上千倍

"""
data = pd.read_csv("EuStockMarkets.csv")
data.head()

# 向量化计算
data['target'] = np.sin(data['DAX'].values) * 1.1

"""



# 增强语句
a += 10
print(a)
"""
增强语句,a只出现1次,只需计算一次,更加快速
"""


# Python化计算更快速


print(a, b)
a, b = b, a + b
print(a, b)

# 列表解析 比手动的for循环语句运行的快很多,列表解析的迭代在解释器内部以C语言执行
# 列表解析式配合zip
# sum([(y-m*x -b)**2 for x,y in zip(X,Y)])/len(X)

# 使用满足迭代协议 的方法: map,zip,filter迭代器

# 使用生成器,可以节省大量内存, 是超级强大的工具


# 上下两行相减(隔行相减) -- shift 移行函数的使用
"""
原始方法,逐个相减去然后赋值,现在看到原来写的代码想吐...,效率差到这个份上
逐个位置的操作,寻址,加上修改dataframe,奇慢,优化成,移行,然后行相减,速度快了一个数量级

原始代码
    df2.loc[i, 'u1_difference'] = df2.at[i + 1, 'LAECF411'] - df2.at[i, 'LAECF411']
改进代码:
    df2['u2_difference'] = (df2["u2"] - (df2["u2"].shift(1))).shift(-1)[:-1]



"""
