# @Time    : 2018/9/26 9:51
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : 基本运算.py

# 数值运算
"""
max(),min()
pow(x, y[, z])  # (x**y) % z  求余数
round(x[, ndigits])  # 四舍五入,保留ndigits位小数, 默认返回整数
abs(x)  # x 的绝对值
divmod(x, y)  # (x//y, x%y), 输出为二元组形式
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
