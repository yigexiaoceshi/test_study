#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
open(path/file_name,mode="r/w/b",buffering,encoding)：

mode参数：
纯文本文件可使用rw，二进制文件可用rb或wb
r：read（读）
w：write（写）
b：binary（二进制文件：如图片，音频，视频等）
"""
# 使用open方法，创建通道，返回文件流对象，赋值给stream，mode的默认参数是rt(读取纯文本文件)
stream = open("123.txt")
# 使用read()方法，读取文件流，返回文件流的内容，赋值给container
# container = stream.read()  # 返回字符串
# print(container)

# 判断是否可读，返回bool
result = stream.readable()  # 返回bool类型
print(result)

# 每次读取一行内容，从第一行开始读取
line = stream.readline()  # 此处注意，文件流里的内容不支持反复读取，所以要注释掉上面的read()方法，不然这里读不到内容，下方readlines同
print("该行内容是：", line)

# 读取所有行
lines = stream.readlines()  # readline()方法已经读取了第一行，所以内存指针指向第二行了，从第二行开始读取
print(lines)  # 返回一个列表

# 关闭管道，释放空间
stream.close()

# 使用：with open() as 别名：加子语句块，在子语句块执行完成之后会自动关闭管道，释放空间
