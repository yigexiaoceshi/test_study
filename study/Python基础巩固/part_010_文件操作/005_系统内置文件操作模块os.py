#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

"""
OS模块：主要对文件和目录进行操作
常用方法：
os.mkdir()：创建目录
os.removedirs()：删除目录或文件
os.getcwd()：获取当前目录
os.path.exists(dir or file)：判断文件或目录是否存在
os.path.dirname(__file__)：返回当前文件所在目录的绝对路径
os.path.join(str1,str2)：字符串拼接
os.path.isabs("路径")：是否绝对路径，返回bool类型（当前目录可以直接写；../表示当前目录的上级目录；../../表示当前目录的上上级目录，类推）
"""
# 获取当前文件所在目录的完整路径，返回一个字符串
print("当前文件所在目录：",os.path.dirname(__file__))

# 获取当前目录
print("当前文件所在目录：",os.getcwd())

# 在当前目录创建文件夹"testdir"，再次执行会报错，提示文件已存在
# os.mkdir("/Users/liyong/Desktop/1")

# 参数为目录，列出当前目录或指定目录所有的文件和文件夹，返回一个列表
print(os.listdir("/Users/liyong/Desktop/"))  # ./ 代表当前目录

# 删除空目录，同理再次执行会报错，提示文件不存在
# os.removedirs("/Users/liyong/Desktop/1/2/3")

# 删除空目录，同理再次执行会报错，提示文件不存在
# os.rmdir("/Users/liyong/Desktop/1")

# os.remove("/Users/liyong/Desktop/1.txt")

# if not os.path.exists("b"):  # 判断当前目录是否存在目录b
#     os.mkdir("b")  # 不存在则创建

# if not os.path.exists("b/test.txt"):  # 如果目录b下没有test.txt
#     file = open("b/test.txt", "w")  # 则创建并打开test.txt，文件权限为w时理解为打开b目录下的test.txt文件，不存在则新建一个
#     file.write("你好，我是test.txt文件")  # 往文件test.txt里写入字符串

# 将目录123.jpg文件复制到当前文件所在目录，建立两个文件流，分别链接2个文件，一个读取原文件内容，一个将内容写入目标文件
# with open("/Users/liyong/Downloads/123.jpg", "rb") as stream2:
#     content1 = stream2.read()
#     # 获取文件名
#     name = stream2.name
#     file_name = name[name.rfind("\\")+1:]  # str.rfind("str")从右至左查找str，返回当前index，加1一直截取到末尾，得到文件名
#     path = os.path.dirname(__file__)  # 获取当前文件所在目录的绝对路径，返回字符串
#     full_path = os.path.join(path, file_name)  # os.path.join(str1,str2)，路径拼接方法，得到文件的完整路径
#     with open(full_path, "wb") as stream3:
#         stream3.write(content1)
#
# print("完成文件复制")


# 返回当前文件所在目录的绝对路径
path = os.path.dirname(__file__)
path1 = os.getcwd()
print("当前文件所在目录是：", path)
print("当前文件所在目录是：", path1)

# 通过文件相对路径获取文件绝对路径，返回字符串
path = os.path.abspath("001_读取文本文件.py")
print("文件'001_读取文本文件.py'的绝对路径是：", path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print("当前文件所在目录是：", path)

# 已知当前文件绝对路径，获取当前目录绝对路径和文件名：os.path.split('文件绝对路径')，目录绝对路径和文件名分别为2个元素，返回一个元组
path = '/Users/liyong/Desktop/study/Python基础巩固/part_010_文件操作/005_系统内置文件操作模块os.py'
result = os.path.split(path)
print("目录的路径，文件名分别为：", result)

result = os.path.splitext(path)  # 返回一个列表，将path分割为2个元素"path/文件名"和"文件扩展名"
print("目录绝对路径/文件名，扩展名分别是：", result)

result = os.path.getsize(path)
print("当前文件的大小是：", result, "字节")

result = os.path.join(os.getcwd(), "file", "file1", "1.txt")
print(result)

# 切换目录，改参数
# os.chdir('/Users/liyong/Downloads')  # 相当于cd命令切换目录
print(os.getcwd())

