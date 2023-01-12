#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
str.find("abc") : 从左至右找到完全匹配abc的位置，找到返回第一个字母的index，找不到返回-1，找到多个也只返回第一个
str.rfind("abc") ：从右至左查找，其他同str.find("abc")
str.index("abc") ： 其他同str.find("abc")，找不到会报错
str.rindex('ab') ： 其他同str.rfind("abc")，找不到会报错
str.count("AA") : 计算子串AA在字符串里出现的次数
"""
# 定义一个字符串
import random

image_address = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
print("*" * 20, "字符串：获取长度", "*" * 20)
print(len(image_address))

print("*" * 20, "字符串：查找文件全名(下划线到.png之间的元素，即'd9c8750bed0b3c7d089fa7d55720d6cf.png')", "*" * 20)
ele = image_address.find("_")  # str.find()从左至右查找，找到符合要求的就返回位置，有多个也不找了，无符合要求的则返回-1
image_name = image_address[ele + 1:]
print(image_name)

print("*" * 20, "字符串：查找扩展名", "*" * 20)
ele1 = image_address.rfind(".")  # str.rfind()，从右至左查找
image_extension = image_address[ele1:]
print(image_extension)

print("*" * 20, "字符串：查找一个元素出现了几次", "*" * 20)
ele_count = image_address.count(".")
print(ele_count)

print("*" * 20, "字符串：判断字符串image_name是否以什么开头，返回布尔值", "*" * 20)
print(image_name)
a = image_name.startswith("d9c87")
print(a)

print("*" * 20, "字符串：判断字符串image_name是否以什么结尾，返回布尔值", "*" * 20)
print(image_name)
b = image_name.endswith(".png")
print(b)

print("*" * 20, "练习1：上传文件格式校验", "*" * 20)
"""
练习1：模拟上传文件
1、键盘输入文件名，文件名必须大于6位，仅支持jpg，gif，png格式
2、格式不对提示"上传失败"；格式正确文件名长度不符合要求则随机生成一个6位数字的文件名，输入"XXXXXX文件上传成功"
"""
# 写法1
file = input("请输入文件全名:")
print("您输入的文件名为：", file)
file_name = file[0:file.rfind(".")]  # 左闭右开，不包含.
file_extension = file[file.rfind(".") + 1:]  # 不包含.所以+1
if file_extension not in ("JPG", "jpg", "PNG", "png", "GIF", "gif"):
    print("格式错误，上传失败！")
else:
    if len(file_name) >= 6:
        print("文件%s上传成功" % file_name)
    else:
        file_name = random.randint(100000, 999999)
        print("文件%s上传成功" % file_name)

# 写法2
file1 = input("请输入文件全名::")
file1_name = file[0:file.rfind(".")]
file1_extension = file[file.rfind("."):]  # 包含.
if file1.endswith("jpg") or file1.endswith("png") or file1.endswith("gif"):
    if len(file1_name) < 6:
        file_full_name = str(random.randint(100000, 999999)) + file1_extension
        print("文件%s上传成功" % file_full_name)
    else:
        print("文件%s上传成功！" % file1)
else:
    print("上传文件格式错误！")

print("*" * 20, "练习2：验证码校验", "*" * 20)
s = "qazwsxedcrfvtgbyhnujmikolp0123456789QWERTYUIOPLKJHGFDSAZXCVBNM"
yanzhengma = ""
print(len(s))
for x in range(1, 7):  # 产生一个6位验证码
    yanzhengma_index = random.randint(0, len(s) - 1)  # 随机取字符串s里的6个元素的索引，字符串长度62，索引范围为[0,61]
    yanzhengma += s[yanzhengma_index]  # 字符串拼接：x = "a" + "b" ------> x = "ab"
print(yanzhengma)
