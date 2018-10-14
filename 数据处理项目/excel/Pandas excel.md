# pandas  excel 处理


## 读取excel 
**读取excel主要通过read_excel函数实现，除了pandas还需要安装第三方库xlrd。**
```python
import pandas as pd


pd.read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, parse_cols=None, parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, has_index_names=None, converters=None, dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)
 '''
 该函数主要的参数为io、sheetname、header、names、encoding。
 io:excel文件，可以是文件路径、文件网址、file-like对象、xlrd workbook;
 
 sheetname:返回指定的sheet，参数可以是字符串（sheet名）、整型（sheet索引）、list（元素为字符串和整型，返回字典{'key':'sheet'}）、none（返回字典，全部sheet）;
            sheetname=0表示第一个sheet页，sheetname=1表示第二个sheet页
 header:指定数据表的表头，参数可以是int、list of ints，即为索引行数为表头;
 names:返回指定name的列，参数为array-like对象。
 encoding:关键字参数，指定以何种编码读取。
 
 index_col=None默认,设置索引列
 该函数返回pandas中的DataFrame或dict of DataFrame对象，利用DataFrame的相关操作即可读取相应的数据。
 '''
 #代码示例:
 import pandas as pd
 excel_path = 'example.xlsx'
 d = pd.read_excel(excel_path, sheetname=None)
 print(d['sheet1'].example_column_name)
```

## 写入excel
**写入excel主要通过pandas构造DataFrame，调用to_excel方法实现。**

```python
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)
'''
该函数主要参数为:excel_writer。
excel_writer:写入的目标excel文件，可以是文件路径、ExcelWriter对象;
sheet_name:被写入的sheet名称，string类型，默认为'sheet1';
na_rep:缺失值表示，string类型;
header:是否写表头信息，布尔或list of string类型，默认为True;
index:是否写行号，布尔类型，默认为True;
encoding:指定写入编码，string类型。
'''
import pandas as pd
writer = pd.ExcelWriter('output.xlsx')
df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})


df1.to_excel(writer,'Sheet1')
writer.save()

# 一句话
DataFrame(data).to_excel("abc.xlsx",sheet_name="123",index=False,header=True)
```

# excel 常用语法
```python

df2 = df2.set_index('ID') #ID列 设置为索引

#求2015年11月的余额和，单位分转换成元


```

# excel 操作
```python
print df[df[u"交易日期"].map(lambda x: x.startswith('201511'))][u"余额"].sum()*0.01


```