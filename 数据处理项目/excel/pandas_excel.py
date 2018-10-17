# @Time    : 2018/10/12 11:26
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : pandas_excel.py

import pandas as pd
import xlrd


def main():
    data = xlrd.open_workbook('0111.xls')  # 读取Excel数据 并提取出所需量x和y
    table = data.sheets()[0]
    y = table.col_values(3)   # 读取列数据
    x = table.col_values(1)


if __name__ == "__main__":
    main()
