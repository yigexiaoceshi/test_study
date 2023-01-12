#!/usr/bin/python3
# -*- coding:utf-8 -*-

city = "杭州"
weather = 39
a = 1231231
# 方法1：%s或%d占位，%变量占位
print("1.%s的天气真热啊，气温有%d度" % (city, weather))

# 方法2：{}占位，str.format(a)方法填充
print('2.{}的天气真热啊，气温有{}度'.format(city, weather, a))  # 填充的变量可以比占位数多
print('3.{0}的天气真热啊，气温有{1}度，广州气温也是{1}度'.format(city, weather, a))  # {}里可以使用索引读取填充值，0开始
print('4.{city}的天气真热啊，气温有{weather}度，广州气温也是{weather}度'.format(city="杭州", weather=37))  # 使用{变量名}占位，须用关键字参数填充值
print("5.{}身高{}米,家住{}".format("山鸡", 1.8, "铜锣湾"))

# 方法3：f-str写法，str里用{变量}占位并填充
print(f"6.{city}的天气真热啊，气温有{weather}度")
