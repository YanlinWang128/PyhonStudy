# @Time    : 2018/11/6 18:25
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 修改dataframe.py

from time import clock

start = clock()

# columns_we_need = [1, 2, 3]

"""

columns = ['date'] + [x[6:] for x in columns_we_need[1:]]
"""


end = clock()
print('time: {:.8f}s'.format(end - start))