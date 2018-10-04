# @Time    : 2018/9/26 10:38
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python_string.py

str = 'hello,world,frank'
"""
字符串以Unicode编码存储,因此,字符串的英文字符和中文字符都算作1个字符
split(sep = None, maxsplit = -1)  字符串分割,返回一个列表
str.replace(old,new[,count])  字符串替换前count次
str.strip([chars])   字符串格式化,在其左侧和右侧去掉chars中列出的字符
str.startwith()
str.endwith()
hex()
oct()
str.zfill()   字符串填充
"""
# split(sep = None, maxsplit = -1) 默认按照空格分割字符, 可指定分割个数
print(str.split(','))

