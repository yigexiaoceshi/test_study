#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
停车计费系统：
1、进入停车场记录进入时间，离开记录离开时间，停车时间为离开时间减去进入时间
2、停车场数据结构：{'车牌':[进入时间，0],'车牌':[进入时间，离开时间],...}
3、15分钟1元，1小时4元
4、停车场变量为全局变量
"""
import random
import time

#  目前暂不使用真实时间做例题
s = time.time()  # 时间戳，，以纪元(1970年1月1日0时0分0秒)为单位以来的时间(以秒为单位)，称为Unix时间,float格式
print("当前时间戳：", s)
ss = time.localtime(s)  # 时间戳转换成时间元组
print("时间戳转换成元组：", ss)
sss = time.asctime()  # 国外时间格式
print("国外时间格式", sss)
ssss = time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime(time.time()))
print("自定义时间格式：", ssss)

car_park = []


def go_in():
    print("******欢迎进入XXX停车场******")
    car = {}
    car_number = input("请输入车牌号码：")
    # 进入时间此处默认为0
    car[car_number] = [0]
    car_park.append(car)
    print("车牌{}已进场".format(car_number))


def go_out():
    car_number = input("请输入车牌号码：")
    for car in car_park:
        if car_number in car:
            #  记录离开时间
            leave_time = random.randint(0, 24)
            # car[car_number] = [0, leave_time]
            # car_park.append(car)
            #  上面2行也可以这样写：
            time_record = car.get(car_number)  # 时间记录，即为子元素字典car的car_number对应的value值，也就是那个列表
            time_record.append(leave_time)
            #  计算停车费
            total_money = leave_time * 4
            print("车牌{}一共停车{}小时，停车费总计为{}元".format(car_number, leave_time, total_money))
            print(car_park)
            break
    else:
        print("未找到该车辆进场记录！")


go_in()
go_in()
go_in()
go_in()
go_out()
