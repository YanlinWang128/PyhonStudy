# @Time    : 2018/11/5 10:06
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : Python_glob 选取同类型文件.py

from time import clock
import glob

start = clock()
print(glob.glob(r"D:/*.*"))  # 匹配文件
"""
Python glob 通配符
* --> 0个或多个 任意字符  *.m* 匹配所有扩展名为m开头的文件
? 任意单个字符   
[...] 方括号中列出的任意一个字符, [AEIOU]* 匹配以大写字母开头的名称
[!...] 不在方括号中出现的任意一个字符  *[!s] 匹配不以s结尾的名称

"""

""""
glob模块的主要方法就是glob,该方法返回所有匹配的文件路径列表（list）
该方法需要一个参数用来指定匹配的路径字符串（字符串可以为绝对路径也可以为相对路径）
其返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件。
glob.glob(r’c:*.txt’)
我这里就是获得C盘下的所有txt文件
glob.glob(r’E:\pic**.jpg’)
获得指定目录下的所有jpg文件
使用相对路径：
glob.glob(r’../*.py’)
import glob
glob.glob('./[0-9].*') # ['./1.gif', './2.txt']
glob.glob('*.gif') #['1.gif', 'card.gif']
glob.glob('?.gif') #['1.gif']
"""
end = clock()
print('time: {:.8f}s'.format(end - start))
