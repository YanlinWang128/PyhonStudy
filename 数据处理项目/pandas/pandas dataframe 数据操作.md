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
    #     df2.loc[i, 'u2_difference'] = df2.at[i + 1, 'u2'] - df2.at[i, 'u2']
    #     df2.loc[i, 'u3_difference'] = df2.at[i + 1, 'u3'] - df2.at[i, 'u3']
    #     df2.loc[i, 'u4_difference'] = df2.at[i + 1, 'TOTFUELF'] - df2.at[i, 'TOTFUELF']

    df2['u1_difference'] = df2["LAECF411"].shift(1)
    df2['u1_difference'] = df2["LAECF411"] - df2['u1_difference']
    df2['u1_difference'] = df2['u1_difference'].shift(-1)
    
# dataframe某个值得索引
begin_index = df2[df2['时间'] == seg[0]].index.tolist()[0]