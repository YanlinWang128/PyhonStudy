# @Time    : 2018/10/4 14:33
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : crawler1.py

from urllib import request
import re


class Crawler():
    url = "https://www.panda.tv/cate/lol"  # 类变量, 目的网页
    """
        root_pattern = '<div class="video-info">[\s\S]*?</div>'
        # 非贪婪模式匹配最近的一组<div>
        # 这种匹配方法,匹配的内容包括 左右两侧的定界内容
        # 可以使用元字符()消除
        root_pattern = '<div class="video-info">([\s\S]*?)</div>'
        # 加上括号之后,匹配的内容就只包括定界中间的括号中的内容
    """

    root_pattern = '<div class="video-info">([\s\S]*?)</div>'  # 非贪婪模式匹配最近的一组<div>
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):  # 获取网页内容
        result = request.urlopen(Crawler.url)  # 类变量的使用
        htmls = result.read()  # 读取请求的结果, 字节码格式,一对数字
        htmls = str(htmls, encoding='utf-8')  # 解码成可操作格式
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Crawler.root_pattern, htmls)  # 返回一个结果列表
        anchors = []  # 存放每一组数据
        for html in root_html:  # 在结果列表中遍历操作
            name = re.findall(Crawler.name_pattern, html)
            # 注意这个返回的是一个列表,虽然只有一个值,使用的时候用name[0]
            number = re.findall(Crawler.number_pattern, html)
            anchor = {'name': name, 'number': number}  # 将这一组数据拼成一个字典
            anchors.append(anchor)  # 添加新节点
        # 处理完数据,将数据返回即可
        return anchors

    def __refine(self, anchors):
        """
        对数据进行处理,去除姓名周围的空格,
        :param anchors:  爬取的结果字典
        """
        result = lambda anchor: {  # lambda表达式对字典内容进行操作
            'name': anchor['name'][0].strip(),  # 修改键值,改成去除空格的字符串
            'number': anchor['number'][0]  # 修改键值,改成字符串
            # 此时键对应的值不再是findall对应的列表,而是里面的字符串
        }

        """
            字符串去空格有内置函数, strip()
            re.findall()函数返回的姓名和数字结果是列表格式   []
            构造lambda表达式将其去除空格,改成键对应字符串

            map() 
            第一个参数是函数,对列表中的每个元素执行函数
            第二个参数是一个列表,此处列表每一个元素都是字典,字典对应的键值还是列表
        """
        return list(map(result, anchors))  # map对象转成列表返回

    def __sort(self, anchors):
        # filter 对数据进行处理,过滤
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        """
        第一个参数,传入的待排序参数 --> 一个字典列表
        第二个参数key, 传入一个函数, 参数为第一个参数(省略不写)
        第二个参数用来确定排序的具体参数, 清洗好具体参数
        默认从小到大,从大到小  reverse = True
        """
        return anchors

    def __sort_seed(self, anchor):  # 确定用来排序的参数
        result = re.findall('\d*', anchor['number'])  # 返回的是一个列表
        number = float(result[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        """
            for anchor in anchors:
            print(anchor['name'] + "----" + anchor['number'])
            对比两种for in ,序号调用和非序号调用
        """
        for rank in range(0, len(anchors)):  # 带序号rank
            print('rank ' + str(rank + 1)
                  + ': ' + anchors[rank]['name'] + "----"
                  + anchors[rank]['number'])

    def go(self):  # 入口函数,多写平级函数,少写嵌套
        htmls = self.__fetch_content()  # 调用私有方法
        anchors = self.__analysis(htmls)  # 接收返回的数据
        anchors = self.__refine(anchors)  # 返回的精炼数据
        anchors = self.__sort(anchors)
        self.__show(anchors)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.go()

    # 缺点: 代码复用性差,写出防御性代码的路程还有很长