# @Time    : 2018/9/26 10:13
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python_math.py

import math

# math 库包括4个数学常数,也包括16个数值表示常数
"""
    math.pi
    math.e
    math.inf  # 正无穷大, 负无穷大  -math.inf 
    math.nan  # 非浮点数标记, NAN(Not a Number)
    
    math.ceil(x)    # 向上取整,返回不小于x的最小整数
    math.floor(x)   # 向下取整,返回不大于x的最大整数
    
    math.factorial(x)   # 返回x的阶乘,如果x是小数或者负数,返回ValueError
    math.gcd(a,b)       # 返回a与b的最大公约数
    math.sqrt(x)        # 返回平方根
    math.pow(x, y)      # math.pow(x, 1/3)  
    
    math.isnan(x)       # 判断是否是非数
    
    
"""

# 涉及浮点数运算时候,建议使用math库提供的函数,而不使用Python提供的函数
# math库函数会控制精度, 内置函数round()可以提供帮助,但是对5不四舍五入不精确
"""
四舍五入是基于十进制的，在二进制无法精确表示的时候是会有误差的。
任何需要十进制运算的地方，都需要用 decimal.Decimal 取代 float：
"""
print(round(math.sqrt(85), 3))

# math.fsum([x, y, z...]) 浮点数精确求和,区别于Python自带的非精度求和
a = math.fsum([0.123, 23.4, 34, 555])
print(a)  # 612.523

# 最大公约数
b = math.gcd(72, 36)
print(b)

# 阶乘
c = math.factorial(20)
print(c)
