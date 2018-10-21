# @Time    : 2018/10/21 21:22
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : 非固定参数函数.py

def sud(name, age, *args, **kwargs):
    """
    *args 会把多传入的参数变成一个元组形式显示；
    **kwargs 会把多传入的参数变成一个字典的形式显示
    
    
    通过 args 元组, kwargs字典可以对传入的多参数进行识别调用
    """
    print(name, age, args, kwargs)
    return


sud("zhangsan", 20, "beijing", "shanghai", year="2018", date="0102")

# 执行结果：
#('zhangsan', 20, ('beijing', 'shanghai'), {'date': '0102', 'year': '2018'})
