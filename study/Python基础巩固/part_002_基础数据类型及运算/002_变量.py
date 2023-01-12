#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
变量命名规范：
1、只支持数字，字母，下划线
2、不能数字开头
3、区分大小写
4、不能以关键字命名
"""
money = 20  # 声明一个名叫money的变量，赋值为20
type(money)  # 括号内为空时，显示的阴影表明该方法必须要传参
print(money)  # 括号里面无阴影，表明语法正确，print()属于内置函数，负责输出结果，括号为空时，表明输出一个空白行
print(type(money))

money = 200  # 再次声明一个名叫money的变量，赋值为200，变量的值允许变化，值会反复覆盖
print(type(money))

money = 200.01
print(type(money))

money = 'AB'  # 字符串可以单引号
print(money)
money = "ABC"  # 字符串可以双引号
print(type(money))
money = """ABCDEFG"""  # 字符串可以三引号，三引号里的内容能够输出格式
print(money)
print(type(money))
message = "我的性别是：'男'"  # 字符串是从左至右找配对，所以单双引号交叉使用
print(message)
message = '我的性别是："男"'
print(message)
shige = """
       静夜思
            唐朝 李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
"""
print(shige)

aa = True
# print(aa)
aa = False  # 此处变量名前面的警告黄色，表明已经申明过一个相同的变量名，并且还未使用，只要使用一次，警告就会消失
print(type(aa))

a, b = 1, 2
print("a,b的值为：", a, b)
a, b = b, a
print("a和b交换位置之后的值为：", a, b)
c, d = [11, 22]
print("c和d分别从列表赋值：", c, d)
e, f = (33, 44)
print("e和f分别从元组赋值：", e, f)
g, h = {55, 66}
print("g和h分别从集合赋值：", g, h)  # 顺序不固定
k, v = {"aaa": 123, "bbb": 456}
print("k和v分别从字典赋值：", k, v)  # 仅赋值key

