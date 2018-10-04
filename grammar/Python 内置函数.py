# @Time    : 2018/9/30 15:25
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python 内置函数.py


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 内置函数map()
print(list(map(sum, M))) # [6, 15, 24] Map sum over items in M

# 内置函数
"""
    all() 函数一般针对组合数据类型,如果其中每个元素都是True,则返回True,否则返回False
    注: 整数0, 空字符串"", 空列表[]等都被当做是False
    
    any() 函数与all() 函数相反,只要组合数据类型中的任何一个是True, 则返回True
    全部元素都是False时返回False
    
    hash() 函数对于能够计算哈希的数据类型返回哈希值
    
    id() 对每个数据返回唯一编号,Python将数据存储在内存中的地址作为其唯一编号
    
    reversed() 返回输入组合数据类型的逆序形式
    
    sort() 对一个序列进行排序, 默认从小到大排序
    
    type() 返回数据类型
"""
ls = [1, 2, 5, 0]
print(all(ls))

print(any(ls))

print(hash("hello, China"))

# 数值运算
"""
max(),min()
pow(x, y[, z])  # (x**y) % z  求余数
round(x[, ndigits])  # 四舍五入,保留ndigits位小数, 默认返回整数
abs(x)  # x 的绝对值
divmod(x, y)  # (x//y, x%y), 输出为二元组形式
"""
# round 四舍六入,默认是float,float是不精确类型
"""
默认数值都是float，float本来就不精确，所以python应该是只对decimal精确
"""


print(pow(3, pow(3, 999), 10000))  # 幂运算和模运算同时进行,速度快
# pow 函数第三个参数z的这个特点在运算加解密算法和科学计算中十分重要

# 与 round(x, ndigits)  对应, int(浮点数) 是截断转换
print(int(10.99))  # 10

number = eval(input("Please input your number:"))
if 12 <= number <= 78:
    print("12 <= number <=78 is right！")

# 循环
for i in range(5):
    # 循环 N 次
    pass
"""
for line in  fi:   # 遍历每一行
for c in s:  # 遍历字符串
for item in ls:  # 遍历列表

while idex < len(s):
    pass
else:
    print("")
"""