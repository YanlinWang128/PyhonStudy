# @Time    : 2018/11/5 10:14
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 10.pandas 存取csv.py

from time import clock

start = clock()

"""
df2 = pd.read_csv(path_file, header=0, encoding='gbk')
header: 指定行数用来作为列名, 如果文件中没有列名，则默认为0
sep:指定分隔符, 如果不指定参数，则会尝试使用逗号分隔
names:用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None
index_col:用作行索引的列编号或者列名
skiprows:需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）
nrows : int, default None 需要读取的行数（从文件头开始算起）
skip_blank_lines : boolean, default True 如果为True，则跳过空行；否则记为NaN。
parse_dates:解析时间
encoding : str, default None, 指定字符集类型，通常指定为'utf-8', 中文则指定'gbk'
data_parser

dfnew.to_csv(output_path_file, index=False)
"""



end = clock()
print('time: {:.8f}s'.format(end - start))