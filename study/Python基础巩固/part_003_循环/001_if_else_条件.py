#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
if
if...else
if...elif...elif...elif...else
"""
import random

# 例子1
int_num = random.randint(1, 10)
int_num1 = random.randint(1, 10)
print(int_num, int_num1)
if int_num + int_num1 > 8 and abs(int_num1 - int_num) <= 3:  # 内置函数abs(a-b)求绝对值
    print("success,两个随机数之和大于8，两个随机数之差小于或等于3")
else:
    print("fail")

# 例子2
# 消费总金额0-500，为lv1级别：随机赠送3张金额为1-10的优惠券
# 消费总金额500-2000，为lv2级别：赠送2张50元优惠券，如果充值则额外赠送充值金额的10%，不充值不赠送
# 消费总金额>2000，为lv3级别：赠送2张100元优惠券，如果充值则额外赠送充值金额的15%，不充值不赠送
username = "李勇"
total = 1500  # 消费总金额
money = 0  # 初始金额为0
coupon = 0  # 优惠券总金额，初始值为0
print("%s,nihao" % username)
# 根据总金额判断级别
if 0 < total <= 500:  # lv1级别，随机赠送3张金额为1-10的优惠券
    coupon1 = random.randint(1, 11)
    coupon2 = random.randint(1, 11)
    coupon3 = random.randint(1, 11)
    coupon += coupon1 + coupon2 + coupon3
elif 500 < total <= 2000:
    coupon += 2 * 50
    recharge = input("%s,请输入y/n确定是否需要充值，充值额外赠送百分之十呢\n" % username)
    try:
        if recharge == "y":
            recharge_money = int(input("%s，请输入充值金额：\n"))  # 如何捕捉这个异常，一个try模块里2个同样类型的错
            coupon -= recharge_money
            print(coupon)
            money = recharge_money * 1.1
            print(money)
        elif recharge == "n":
            print(coupon)
            print(money)
        elif recharge != "y" and recharge != "n":
            raise ValueError("输入的不是y或者n")
        else:
            pass
    except(ValueError,"输入的不是y或者n啊"):
        print("请输入y或者n")
elif total > 2000:
    coupon += 2 * 100
    recharge = input("%s,请输入y/n确定是否需要充值，充值额外赠送百分之十呢\n" % username)
    if recharge == "y":
        recharge_money = int(input("%s，请输入充值金额：\n"))
        coupon -= recharge_money
        money = recharge_money * 1.15
    elif recharge == "n":
        pass
