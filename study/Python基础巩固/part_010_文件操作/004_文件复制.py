#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
with open() as 别名：
    pass
"""
# 将桌面的demo.json文件复制到Downloads目录，并重命名为demo1.json
with open("/Users/liyong/Desktop/demo.json", "rb") as stream:  # 二进制可读方式建立和demo.json文件的通道
    content = stream.read()  # 读取demo.json文件内容
    with open("/Users/liyong/Downloads/demo.json", "wb") as stream1:  # 二进制可写文件打开demo.json，没有该文件会新增并建立通道
        stream1.write(content)  # 将读取到的demo.json的内容写入新增的目标文件

print("完成文件复制以及重命名")

# 将目录123.jpg文件复制到桌面，建立两个文件流，分别链接2个文件，一个读取原文件内容，一个将内容写入目标文件
with open("/Users/liyong/Downloads/123.jpg", "rb") as stream2:
    content1 = stream2.read()
    with open("/Users/liyong/Desktop/123.jpg", "wb") as stream3:
        stream3.write(content1)

print("完成文件复制")

# 批量复制：open()方法，必须定位到文件，该方法不支持对目录进行操作
# 批量复制借助一个系统内置模块os，下一个py文件