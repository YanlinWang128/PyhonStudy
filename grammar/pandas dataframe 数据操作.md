# 最快的求表长的属性
print(df.index)

# dataframe空白值处理
df1 = df.ffill() # 向前填充数据
df2 = df.bfill() # 向后填充数据
### 多行连续空白值 的 处理


# dataframe筛选数据后重设索引
df2.reset_index(drop=True)


# dataframe数据筛选
df2 = df2[(df2['JT66801A'] <= 400) & (df2['JT66801A'] >= 300)]

dfnew1 = df2[(df2.TOTFUELF > 0) & (df2.THRPRESS < 1)][['TOTFUELF', 'THRPRESS']]
dfnew1.to_csv(output_file, index=False)

# dataframe只保存需要的几列
dfnew = df[['TOTFUELF', 'THRPRESS']]


# dataframe 添加一列数据
把dataframe如df1中的一列或若干列加入另一个dataframe，如df2
思路：先把数据按列分割，然后再把分出去的列重新插入
    df1 = pd.read_csv('example.csv')
    date = df1.pop('date')  # 获取到纯数据

（2）将这一列插入到指定位置，假如插入到第一列
    df2.insert(0,'date',date)
（3）默认插入到最后一列
    df2['date'] = date

# dataframe 添加一列 列表推导式推出的列表数据
    list_temp = [x for x in range(201)]
    df['a'] = list_temp

# 两行相减(隔行相减) -- shift函数的使用
df.p['xx_1'] = df.p["xx"].shift(1) # 向下移动一位
df.p['xx'] - df.p["xx_1"]


# 删除某列
df2 = df.drop(['MonthlyIncome'],axis=1)


# dataframe 更改列名
df.rename(columns  = {'ID':'id', 'code':'编码'})
或者直接全部替换
df.columns = ['ID','hello']



# 对于匹配好工况段
现阶段的思路:确定好边界索引,遍历每个工况段,求偏差,不满足条件的标记

    df2.drop(['deviation'], inplace=True, axis=1)
    # 打印有 空值的列
    #print(df2[df2.isnull().values == True])
    格式化输出
    .to_csv(r'F:/HistoryData/08时间对/{:0>3d}.csv'.format(count), index=False)


    # 创建一个空的dataframe,用来存储数据
    df_data = pd.DataFrame(columns=["begin", "end"])
```
if (abs(df2['UNIT2:THRPRESS'][i] - sequence_mean) > deviation):
df2.loc[i, 'deviation'] = 1 
```
标记完成后,最后选择(或取补集)完成数据筛选
```
df2 = df2[df2['deviation'] != 1]
```

at方法是专门用于获取某个值的：
```
df.at[index,'begin']
df_data.loc[count, 'end'] = df2.at[end_index, '时间']
```


选择多列数据
```
df.loc[:, ['begin','end']]
```

dataframe 的切片操作，切片得到的是行数据
```
df[1:3] 选取索引1,2行的数据,行数据
df['begin'] 列数据选择
df.loc[:,['A', 'B']]
```


## dataframe 某列数据转换为列表
df2['begin'].tolist()

# 新加一列
# 第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸。
df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)

## dataframe标题  tolist()
print(df2.columns.values.tolist()[0])


## 获取DataFrame行数
我们发现速度最快的是len(df.index) 方法， 其次是len(df) 
最慢的是df['col1'].count(),因为该函数需要去除NaN

# 对于dataframe,对于整列计算, df.apply,或者逐个在指定位置添加值非常的慢
某列逐个计算数据,慢到家了
df2.loc[i, 'u2_difference'] = df2.at[i + 1, 'u2'] - df2.at[i, 'u2']


np.where 加上一些中间参数比较快


# 上下两行相减(隔行相减) -- shift 移行函数的使用
## 原始方法,逐个相减去然后赋值,现在看到原来写的代码想吐...,效率差到这个份上
df2['u1_difference'] = df2["LAECF411"].shift(1)


    #     df2.loc[i, 'u1_difference'] = df2.at[i + 1, 'LAECF411'] - df2.at[i, 'LAECF411']


# df2['u1_difference'] = (df2["LAECF411"] - df2["LAECF411"].shift(1)).shift(-1)
    
# dataframe某个值得索引
begin_index = df2[df2['时间'] == seg[0]].index.tolist()[0]


# numpy中std()和pandas中std()的区别
注意，计算得出的默认标准偏差类型在 numpy 的 .std() 和 pandas 的 .std() 函数之间是不同的。默认情况下，numpy 计算的是总体标准偏差，ddof = 0。另一方面，pandas 计算的是样本标准偏差，ddof = 1。如果我们知道所有的分数，那么我们就有了总体——因此，要使用 pandas 进行归一化处理，我们需要将“ddof”设置为 0。

如是总体,标准差公式根号内除以n, 
如是样本,标准差公式根号内除以（n-1),