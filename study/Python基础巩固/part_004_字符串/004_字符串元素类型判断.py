#!/usr/bin/python3
# -*- coding:utf-8 -*-
print("*" * 20, "str.isalpha()：判断字符串是否【全为字母】", "*" * 20)
a = "234dcvdfDSGDds"
result = a.isalpha()
print(result)

print("*" * 20, "str.isdigit()：判断字符串是否【全为数字】", "*" * 20)
b = '234234'
result = b.isdigit()
print(result)

print("*" * 20, "str.isalnum()：判断字符串是否为【数字或字母】", "*" * 20)
c = '123dsFDSFd123'
result = c.isalnum()
print(result)

print("*" * 20, "str.isspace()：判断字符串是否【全为且至少有一个空格】", "*" * 20)
d = '    '
result = d.isspace()
print(result)

print("*" * 20, "str.isupper()：判断字符串是否【字母全为大写字母】，可以有字母以外的字符", "*" * 20)
e = ' 234234   GDSGDF '  # 只要字母都是大写就行，非字母不管
result = e.isupper()
print(result)

print("*" * 20, "str.islower()：判断字符串是否【字母全为小写字母】，可以有字母以外的字符", "*" * 20)
f = ' 234234    gdfg '  # 只要字母都是小写就行，非字母不管
result = f.islower()
print(result)

print("*" * 20, "示例1：", "*" * 20)
# 用户名或者手机号 + 密码，登录
# 用户名：全部小写，首字母不能是数字，长度必须6位以上（目前写死：admin123）
# 手机号码：纯数字，长度11（目前写死：00000000000）
# 要求输入玩用户名输入框立即验证，验证通过才允许输入密码
# 密码：必须6位数字（目前写死：000000）
# 符合以上条件，则进入下层验证：判断用户名/手机号+密码是否正确
hello = True
while hello:
    name = input("请输入登录用户名/手机号：")
    if (name.isdigit() and len(name) == 11) or ((name.islower()) and (not name[0].isdigit()) and (len(name) > 6)):
        print("用户名格式正确！")
        while True:
            passwd = input("用输入登录密码：")
            if passwd.isdigit() and len(passwd) == 6:
                print("password格式是正确的！")
                if (name == "admin123" or name == "00000000000") and passwd == "000000":
                    print("登录成功！")
                    hello = False  # 控制外层循环
                    break  # 此时不能跳出外层循环，所以外层循环不要写死while True，而是通过变量的方式控制外层循环
                else:
                    print("用户名密码输入错误！")
                    break
            else:
                print("登录密码必须是6位数字！")
    else:
        print("登录用户名或者手机号格式错误！")
