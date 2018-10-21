# @Time    : 2018/10/21 20:20
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 文件操作.py

# 内置的open()函数打开文件

f = open('D:/a.txt', 'w')
f.close()

# 写文件a:追加写模式
with open('D:/a.txt', 'a') as f:
    f.write('Hello, world!\nhello, file\n')

# 读文件f.read([count]) # 读整个文件,或者指定个字符
# f.readlines(),读出所有行，也就是读出整个文件的信息
with open('D:/a.txt', 'r') as file1:
    # 小文件直接全部读取到内存
    print(file1.read())

    # 有读操作,文件指针位置移动
    # 查看文件指针位置 f.tell()
    # f.seek(offset[,where]) 把文件指针移动到相对于where的offset位置。
    # where为0表示文件开始处，这是默认值 ；1表示当前位置；2表示文件结尾。
    print(file1.tell())

    # 文件指针重置为开始位置
    file1.seek(0)
    print(file1.tell())

    # 不确定大小,反复调用read(size),读取指定个字符
    # 注意每次调用读,光标都会移动,如果已经读取完毕,无数据可读
    print(file1.read(10))

    # 配置文件用用readlines() 按行读取最方便
    for line in file1.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
"""
读写模式(默认是r):
r: 读模式,文件不存在,报错
w: 写模式, 文件不存在则创建,存在则覆盖,不可以写
a: 追加写模式,文件不存在则创建, 文件存在则追加, 不可读

二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
要读取二进制文件，比如图片、视频等等，用'rb,wb,ab'模式打开文件即可

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
print(f.read()) # '测试'

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
最简单的方式是直接忽略：

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

由于文件读写时都有可能产生IOError
一旦出错，后面的f.close()就不会调用。
为了保证无论是否出错都能正确地关闭文件
Python引入了with语句来自动帮我们调用close()方法,一种保险方法：
    with open('/path/to/file', 'r') as f:
        print(f.read())
        
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险       
        


"""
