# @Time    : 2018/10/25 22:04
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 测试.py

from glob import glob
import re
import os


def twoSum_60ms(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_mapping = dict()

    for i in range(len(nums)):
        other = target - nums[i]
        if other in num_mapping:
            return [num_mapping[other], i]
        num_mapping[nums[i]] = i


def columns_replace():
    columns_we_need = ['时间', 'UNIT2:LAECF411', 'UNIT2:HBKCT101', 'UNIT2:HBKCT201', 'UNIT2:T12A041A', 'UNIT2:JT66801A',
                       'UNIT2:THRPRESS', 'UNIT2:HHL517CG', 'UNIT2:HHL527CG', 'UNIT2:HHL617CG', 'UNIT2:HHL627CG',
                       'UNIT2:LABCT301', 'UNIT2:LABCT302', 'UNIT2:HAG10T01', 'UNIT2:HAG10T02', 'UNIT2:HAG10T03',
                       'UNIT2:HAG10T04', 'UNIT2:HAG10T05', 'UNIT2:HAG10T06', 'UNIT2:HAG10T16', 'UNIT2:HAG10T17',
                       'UNIT2:HAG10T18', 'UNIT2:HAG10T13', 'UNIT2:HAG10T14', 'UNIT2:HAG10T15', 'UNIT2:AIRFLOW',
                       'UNIT2:TOTFUELF', 'UNIT2:MSTMFLOW', 'UNIT2:T10A042A', 'UNIT2:TOTFWFLW', 'UNIT2:FWFLOWD', ]

    columns = columns_we_need[:1] + [x[6:] if x.startswith('UNIT2:') else x for x in columns_we_need[1:]]
    print(columns)


if __name__ == '__main__':
    # num_mapping = dict()
    # print(type(num_mapping))
    path = r"F:\HistoryData\08new"
    pattern = '\*_p*.csv'

    files = sorted(glob(path + pattern), key=lambda items: int(re.findall(r'p(\d+).csv', items)[0]))
    # path = r'F:\BAT\*.*'
    # # pattern =
    # files = sorted(glob(path))
    for i in files:

     print(os.path.abspath(i))
