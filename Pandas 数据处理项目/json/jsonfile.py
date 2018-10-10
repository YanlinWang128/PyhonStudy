# @Time    : 2018/10/9 20:35
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : jsonfile.py

import json


def export_json(path_dir_name, json_str):
    """
    将字典导出到新建的json里面,  w 模式
    :param path_dir_name: 字符串类型,可为绝对路径 + 文件名
    :param json_str: json内容,可为一个字典,函数内自带解析
    :return: no
    """
    with open(path_dir_name, 'w') as dump_f:
        json.dump(json.loads(json.dumps(json_str)), dump_f)
    print('export ' + path_dir_name + ' success!')


if __name__ == "__main__":
    path_dir_name = 'a.json'  # 可改为绝对路径
    temp_str = []
    json_str = {'seg_detail': temp_str}
    print('seg', json_str)

    export_json(path_dir_name, json_str)