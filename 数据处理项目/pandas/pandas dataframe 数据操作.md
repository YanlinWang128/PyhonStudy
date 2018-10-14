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

## dataframe标题  tolist()
print(df2.columns.values.tolist()[0])


#numpy 矩阵常用操作


