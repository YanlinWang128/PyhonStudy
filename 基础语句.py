# @Time    : 2018/9/25 22:21
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : 基础语句.py

print("hello,world")

# 同步赋值
x = 1
y = 2
print("x is {0}, y is {1}".format(x, y))

x, y = y, x
print("x is {0}, y is {1}".format(x, y))

# input,   return a string, use function eval();

"""
TempStr = input("Please input your number: ")
"""

# eval() 函数
"""
eval(<字符串>) 函数是Python 语言中一个重要的函数
    它能够以Python表达式的方式解析并执行字符串,并将返回结果输出
	将输入的字符串变成Python语句
	x = 1
	eval("x + 1")   #  2

	eval("1.1 + 2.2")	#  3.3    解析并执行语句

	TempStr = "102C"
	eval(TempStr[0:-1])   # 102  去掉最后一个字符,结果执行为一个数字

	eval("hello")	# 默认将字符串执行为 变量  name 'hello' not defined


"""
# 命名规范
"""
    文件名,包:全部小写,可使用下划线
    函数名,变量名全部小写,myfunction, my_example
    类: 首字母大写单词串 MyTime
    常量名所有字母大写
"""

# Python  格式化输出  {}.format()

"""
Python格式化输出和C真是非常的相似

1. 打印字符串

>>> a='AAAA'
>>> b='BBBB'
>>> print('a=%s b=%s' %(a,b));
a=AAAA b=BBBB

2.打印整数
>>> a=10
>>> b=20
>>> print('a=%d b=%d' %(a,b));
a=10 b=20
>>> 

3.打印浮点数
>>> a=1.1234
>>> b=3.14159;
>>> print('a=%d b=%d' %(a,b));
a=1 b=3
>>> print('a=%f b=%f' %(a,b));
a=1.123400 b=3.141590
>>> 
python2.5  python3.5默认浮点数都保留6位小数
4.打印浮点数（指定保留小数点位数）

>>> a=1.1234
>>> b=3.14159;
>>> print('a=%.2f b=%.3f' %(a,b));
a=1.12 b=3.142
%f里指定保留小数位数时具有自动四舍五入的功能，比如b=3.14159  使用%.3f格式化之后输出的结果变成了b=3.142


5.指定占位符宽度

>>> a='ABC'
>>> b='DEFF'
>>> print('a=%4s b=%6s' %(a,b));
a= ABC b=  DEFF
还可以指定特定的占位符

>>> a='ABC'
>>> b='DEFF'
>>> d=125
>>> print('a=%4s b=%6s d=%04d' %(a,b,d));
a= ABC b=  DEFF d=0125
指定输出d使用4个字符宽度，如果不够在前面补零,输出字符串时，默认右对齐，其实可以调整的
6.指定占位符宽度，指定对其方式

>>> a='ABC'
>>> b='DEFF'
>>> d=125
>>> print('a=%-4s b=%-6s d=%-06d' %(a,b,d));
a=ABC  b=DEFF   d=125   


"""

"""
Python format
print "{:.2f}".format(3.1415926) #3.14,保留小数点后两位
print "{:+.2f}".format(3.1415926) #+3.14 带符号保留小数点后两位
print "{:+.2f}".format(-10) #-10.00 带符号保留小数点后两位
print "{:+.0f}".format(-10.00) #-10  不带小数
print "{:0>2d}".format(1) #01 数字补零 (填充左边, 宽度为2)
print "{:x<2d}".format(1) #1x 数字补x (填充右边, 宽度为4)
print "{:x<4d}".format(10) #10xx 数字补x (填充右边, 宽度为4)
print "{:,}".format(1000000) #1,000,000 以逗号分隔的数字格式
print "{:.2%}".format(0.12) #12.00% 百分比格式
print "{:.2e}".format(1000000) #1.00e+06 指数记法
print "{:<10d}".format(10) #10 左对齐 (宽度为10)
print "{:>10d}".format(10) #        10 右对齐 (默认, 宽度为10)
print "{:^10d}".format(10) #    10 中间对齐 (宽度为10)

1.格式符
‘f’表示浮点数 
‘d’表示十进制整数. 将数字以10为基数进行输出 
‘%’表示百分数. 将数值乘以100然后以fixed-point(‘f’)格式打印, 值后面会有一个百分号 
‘e’表示幂符号. 用科学计数法打印数字, 用’e’表示幂.

2.对齐与填充
^、<、>分别是居中、左对齐、右对齐，后面带宽度 
:后面带填充字符，只能是一个字符，不指定的话默认就是空格。

"""