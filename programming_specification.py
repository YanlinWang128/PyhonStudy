# @Time    : 2018/10/4 10:36
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : programming_specification.py
# 记录基本的编程规范

import os, sys

# 添加自建项目进入文件搜索,使可导入自定义模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

# 斜杠路径 E:/Pythoncode/东胜数据处理/Python视频书籍学习/PyhonStudy/programming_specification.py
# E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy\programming_specification.py
# E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy
"""
1. 
sys.path.append('E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy')
2. 斜杠路径和反斜杠路径

"""
