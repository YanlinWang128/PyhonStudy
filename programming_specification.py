# @Time    : 2018/10/4 10:36
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : programming_specification.py
# 记录基本的编程规范

import os, sys

# python  斜杠目录

# 添加自建项目进入文件搜索,使可导入自定义模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

# 斜杠路径 E:/Pythoncode/东胜数据处理/Python视频书籍学习/PyhonStudy/programming_specification.py
# E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy\programming_specification.py
# E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy
"""
--- sys.path.append
    1.当我们试图加载一个模块时Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
        默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
        搜索路径存放在sys模块的path变量中,列表变量
    2. 如果我们要添加自己的搜索目录,可以直接修改sys.path,添加搜索目录
        这种方式是运行时候修改,运行结束后失效


--- 不用绝对路径,全部改成相对路径
    sys.path.append('E:\Pythoncode\东胜数据处理\Python视频书籍学习\PyhonStudy')
--- __file__ 斜杠路径,可能相对也可能绝对,包含文件名
    1. 如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！
    2. 如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！
--- os.path.abspath(__file__)  
    返回当前路径的绝对路径,包含文件名
--- os.path.dirname(os.path.abspath(__file__))
    返回文件路径,不包含文件名,用于设置搜索路径,使得自定义模块能够被搜索引用

"""

# 作为模块调用时不执行
if __name__ == "__main__":
    print("作为模块调用时候不执行")


# 命名规范
"""
函数名:    一律小写，如有多个单词，用下划线隔开
变量名:    小写, 如有多个单词，用下划线隔开

类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头

"""



# 对文件的操作规范
"""
不许覆盖原始文件,另存备份
"""

# 代码规范
"""
不许硬编码, 参数外设
__file__, len 

# 获取上级目录, 转换目录斜杠
output_path = os.path.abspath(os.path.join(dir_path, "..")).replace('\\', '/')
"""