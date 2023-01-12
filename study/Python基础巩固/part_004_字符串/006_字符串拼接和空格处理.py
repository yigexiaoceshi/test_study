#!/usr/bin/python3
# -*- coding:utf-8 -*-

print("*" * 20, "str.strip()：取消字符串前后空格", "*" * 20)
username = "  admin    "  # 不小心输入了空格，前面2个，后面4个，去掉前后空格
print(username.strip())
print(len(username.strip()))

print("*" * 20, "str.lstrip()：取消字符串前面空格", "*" * 20)
username1 = "  admin    "  # 去掉前面空格
print(username1.lstrip())
print(len(username1.lstrip()))

print("*" * 20, "str.rstrip()：取消字符串后面空格", "*" * 20)
username2 = "  admin    "  # 去掉后面空格
print(username2.rstrip())
print(len(username2.rstrip()))

print("*" * 20, "str.center()：添加空格，使得字符串居中", "*" * 20)
username3 = "  ad min    "
print(username3.center(30))  # 定义字符串整个长度为30，username3处于中间位置
print(len(username3.center(30)))

print("*" * 20, "str.ljust()：添加空格，使得字符串左对齐", "*" * 20)
username4 = "  ad min    "
print(username4.ljust(30))  # 定义字符串整个长度为30，username4处于左侧(注意：username4本身的空格不会计算到对齐里)
print(len(username4.ljust(30)))

print("*" * 20, "str.rjust()：添加空格，使得字符串右对齐", "*" * 20)
username5 = "  ad min    "
print(username5.rjust(30))  # 定义字符串整个长度为30，username4处于右侧(注意：username4本身的空格不会计算到对齐里)
print(len(username5.rjust(30)))

print("*" * 20, "str.join(str/list/tuple)：字符串拼接，参数的元素与元素之间插入该str，返回一个str", "*" * 20)
username6 = ("你好", "国庆节", "要放假了", "我很高兴啊")
username7 = "123"
username8 = "admin"
print(username8.join(username6))  # 传入的参数可以是字符串，可以是list或者tuple或者set或者dictionary
print(username8.join(username7))  # 用字符串username8连接username7里的所有元素
print("###".join("aabb"))
print("$$".join(["40", "50", "60"]))
print("".join(["40", "50", "60"]))
