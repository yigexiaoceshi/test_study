#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
读取图片/音频/视频，mode参数不能使用默认的rt，要使用rb(read,binary)，mode参数决定通道类型(文件类型和操作类型)
"""
stream = open("/Users/liyong/Downloads/123.jpg", "rb")
print("文件流stream为：", stream)
container = stream.read()
print("读取的二进制文件为：", container)
stream.close()