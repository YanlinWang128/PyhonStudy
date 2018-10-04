# @Time    : 2018/10/4 16:13
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_re.py

import re

match = re.match('hello[ \t]*(.*)world', 'hello      Pyhton-->world')
print(match.group(1))  # Pyhton--> group(0)是全匹配,group(1)是第1个括号匹配

result = re.match('/(.*)/(.*)/(.*)', '/usr/home/frank')
print(result.group(0))  # /usr/home/frank 全匹配
print(result.groups())  # ('usr', 'home', 'frank') tuple
