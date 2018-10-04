# @Time    : 2018/9/26 11:07
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : Python_time.py

import time

t = time.clock()
for i in range(100000):
    print('hello')

t = time.clock() # 单位 s , 返回在第一次调用后到现在的时间
print(type(t), t)

"""
在Windows中，time.clock()更精确；
WINDOWS中，time.clock()第一次调用，返回的是进程运行的实际时间。
而第二次之后的调用是自第一次调用以后到现在的运行时间。
(实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
"""

# time.time()  # 新纪元时间 time.gmtime(0)  到现在的秒数
"""
time.time通常用于检测Windows上的程序。
在Unix系统上，time.time的作用与Windows相同，但time.clock的意义不同。
在Unix系统上，time.clock以秒为单位返回当前处理器时间，
例如，执行当前线程所花费的CPU时间。
而在Windows上，它是以秒为单位的返回自首次调用该函数以来所流逝的系统时间。


下面是在Unix系统上运行time.time和time.clock的例子：


time.time()显示系统时间过去大概1秒
而time.clock()显示花费在当前进程上的CPU时间沁于1毫秒。
同时可以看到time.clock()的精度高于time.time()

下面是在Windows下，同样的程序返回不一样的结果：

time.time()和time.clock()显示系统时间大致过去了1秒。
与Unix不同，time.clock()不返回CPU时间，返回的是系统时间，且精度较高。

"""