# @Time    : 2018/9/25 22:29
# @Author  : Yanlin Wang
# @Email   : Wangyl_a@163.com
# @File    : TempConvert.py


def temp_convert(temp_str):
    """
    华氏温度F,和摄氏温度C互相转换
    :param temp_str: 输入的温度,华氏(F)or摄氏(C)
    :return: 转换后的温度
    """
    # temp_str = input("input your temp")
    if temp_str[-1] in ['F', 'f']:
        C = (eval(temp_str[0:-1]) - 32) / 1.8  # Python 切片不包括右侧, Python小数除法
        print("摄氏温度是 {0:.2f}C".format(C))
        return C
    elif temp_str[-1] in ['c', 'C']:
        F = 1.8 * eval(temp_str[0:-1]) + 32  # string eval to number
        print("华氏温度是 {0:.2f}F".format(F))
        return F
    print("请输入带有符号的温度值:")
    return "input wrong"


if __name__ == "__main__":
    temp_str = input("input temperature: ")  # return a string
    temp_convert(temp_str)
    """
        in 配合切片,定点筛查
        not in ['n', 'N']
    """
