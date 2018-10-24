# @Time    : 2018/10/24 21:44
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 批量对文件进行重命名.py

import os


def file_rename_to_sort(path, save_path):
    """
    对图片进行排序
    :param path: 需要改名的文件夹
    :param save_path: 要保存的文件位置
    :return: 
    """
    # 遍历该路径下的所有文件,文件夹名称
    filelist = os.listdir(path)
    print(filelist)
    number = 1
    # # 默认保存为原路径
    # save_path = path
    if (not os.path.exists(save_path)):
        os.mkdir(save_path)

    for file in filelist:
        # 判断该路径下的文件是否为图片
        # file = 'hello' + file
        if file.lower().endswith('.jpg'):
            # 原始图片的绝对路径,包括文件名
            old_name = os.path.join(os.path.abspath(path), file)
            # 保存处的绝对路径,包括文件名(001,jpg开始)
            new_name = os.path.join(os.path.abspath(save_path), 'a{:0>3}.jpg'.format(str(number)))
            # 重命名
            os.rename(old_name, new_name)
            print(old_name, ' ---> ', new_name)
            number += 1
    return


if __name__ == '__main__':
    # 图片路径
    path = r'D:/照片'
    file_rename_to_sort(path)
