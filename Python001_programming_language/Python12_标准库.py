# -*-coding: utf-8 -*-
"""
常见标准模块
 1、操作系统相关：os，常用方法
    * os.mkdir()：创建目录
    * os.removedirs("dir")：仅删除目录
    * os.rmdir(dir)：仅删除目录
    * os.remove(file)：仅删除文件
    * os.getcwd()：获取当前目录
    * os.path.exists(dir or file)：判断文件或者目录是否存在，返回True或False
    * os.listdir("path")：该目录下有哪些文件及目录
"""
import os

# 仅创建目录，文件名称重复会报错，报错则不会再继续执行剩余代码
# os.mkdir("Python12_标准库")
# 仅删除目录
# os.removedirs("Python12_标准库")
# 仅删除目录
# os.rmdir("Python12_标准库")
# 仅删除文件
# os.remove("Python12.txt")
# 获取特定路径下有哪些文件及目录，返回一个列表，文件及文件夹名称以字符串形式作为列表的元素
print("当前路径下的目录及文件有：", os.listdir("./"))
# 获取当前文件所在的绝对路径
print("当前文件所在的绝对路径为：", os.getcwd())
# 判断当前目录下是否存在"Python12_标准库"目录，存在则返回True，不存在返回False，当前目录可以带./也可以不带，上级目录../
print("当前目录下存在目录Python12_标准库吗：", os.path.exists("Python12_标准库"))
# 如果当前目录下不存在Python12_标准库这个目录
if not os.path.exists("Python12_标准库"):
    # 执行创建该目录
    os.mkdir("Python12_标准库")
    # 如果该目录下不存在python12.txt文件
    if not os.path.exists("Python12_标准库/python12.txt"):
        # 创建并打开该文件
        file = open("Python12_标准库/python12.txt", "w")
        file.write("hello Python3")
        file.close()
"""
 2、时间与日期相关：time、datatime，常用方法
    * time.asctime()：国外的时间格式
    * time.time()：时间戳
    * time.sleep(num)：强制等待多少秒
    * time.localtime()：时间戳转成时间元组
    * time.strftime()：将当前的时间戳转换成带格式的时间，比如:time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
"""
import time

print(f"国外时间格式为：{time.asctime()}")
# 从1970年1月1日0时0分0秒开始的总秒数，以秒为单位
print(f"当前时间戳为：{time.time()}")
print(f"强制等待1秒再继续执行：{time.sleep(1)}")
# time.localtime(sec)：传入秒数作为参数，时间戳就是秒数，不传默认传入当前时间的时间戳，即time.time()
print(f"当前时间戳转换成时间元组：{time.localtime()}")
# time.strftime(format,tuple)：第一个参数是格式，第二个参数必须传入一个元组
print("将当前时间戳转换成特定的时间格式：", time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
# 获取2天前的当前时间，先获取当前时间戳
now_timestamp = time.time()
# 计算得出2天前的当前时间点的时间戳
two_days_before_time = now_timestamp - 60 * 60 * 24 * 2
# 传入2天谴当前时间点的时间戳，并转换成元组
print(time.localtime(two_days_before_time))
# 两天前的时间点的时间戳转换成元组，传入time.strftime(format,tuple)转换成特定格式的2天前的时间
print(time.strftime("两天前的时间为：%Y年%m月%d日 %H:%M:%S", time.localtime(two_days_before_time)))
"""
 3、科学计算相关：常用方法
    * math.ceil(x)：返回大于等于参数x的最小整数
    * math.floor(x)：返回小于等于参与x的最大整数
    * math.sqrt(x)：返回参数x的平方根，返回float型
    * math.isqrt(x)：返回参数x的平方根，返回int型
    * 其他方法自行研究
"""
import math

# 求出不比7.9小的最小整数
print(math.ceil(7.9))
# 求出不比98.89大的最大整数
print(math.floor(98.89))
# 求81的平方根，返回float型
print(math.sqrt(81))
# 求81的平方根，返回int型，如果不能整数开平方，则只截取整数位，小数点后舍弃，而不是四舍五入
print(math.isqrt(81))
"""
 4、网络请求相关：urllib，常用方法有
  * urllib.request.urlopen("url",data)：对URL发起请求，获取response相关信息，主要是http，官方建议使用requests模块
  * urllib.response()：暂时无需了解
"""
import urllib
import urllib.request

# 对https://www.baidu.com发起请求
response = urllib.request.urlopen("http://www.baidu.com")
print(f"响应状态码为：{response.status}")
print(f"响应头信息为：\n{response.headers}")
# print(f"响应body为：\n{response.read()}")  # 数据体较大，先注释掉
"""
 5、sys、json等等等
"""
