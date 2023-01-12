# -*-coding: utf-8 -*-
"""
面向对象编程的优点：解决系统的可维护性、可扩展性、可重用性
三大特性：
    * 封装：一类事物的共性的属性和方法的定义
    * 继承：父类下可以被无限多个子类继承，所以父类里定义的属性和方法一般都须是共性的方法和属性，一般不轻易改动的，如果改动则可能对继承的子类会造成影响
    * 多态：同一个属性或方法，在子类和父类里有不同的存在形态，基于继承
"""


# 封装：
# 定义一个飞机的类
class Airplan:
    # 名字
    name = "默认名字"
    # 颜色
    color = "默认颜色"

    def set_name(self, name):
        self.name = name
        print(f"父类的set_name，飞机的名字是：{name}")

    def set_color(self, color):
        self.color = color
        print(f"父类的set_color，飞机的颜色是：{color}")


Air1 = Airplan()
print(Air1.name)
print(Air1.color)
Air1.set_name("第一驾飞机")
Air1.set_color("红色")

Air2 = Airplan()
Air2.set_name("第二驾飞机")
Air2.set_color("绿色")


# 继承：
# 定义一个民用飞机的子类，继承飞机类
class CivilAirplan(Airplan):
    name = "子类的默认名字"

    def load_person(self, num):
        print(f"子类的load_person，民用机能载人的数量为：{num}")

    # 当子类拥有和父类相同的属性或方法时，优先调用子类的，也可理解为子类覆盖父类的
    def set_name(self, name):
        print(f"子类的set_name，民用机的名字设定为：{name}")


# 子类拥有父类（飞机类）的所有属性和方法
civilAir1 = CivilAirplan()
# 子类可直接调用父类的属性
print(civilAir1.color)
# 子类和父类拥有相同的属性，调用优先子类，同一个方法或属性，在父类和子类有不同的表现形态，就叫多态，多态基于继承
print(civilAir1.name)
# 子类和父类拥有相同名称的方法，优先调用子类，同一个方法或属性，在父类和子类有不同的表现形态，就叫多态，多态基于继承
civilAir1.set_name("第一驾民用飞机")
# 子类可直接调用父类的方法
civilAir1.set_color("紫色")
# 子类也可以拥有自己的特有的属性和方法
civilAir1.load_person(100)


class JunYAirplan(Airplan):
    name = "军用机的默认名字"
    def set_name(self, name):
        print(f"军用机的set_name，军用机的名字是：{name}")


junyAir1 = JunYAirplan()
print(junyAir1.name)
junyAir1.set_name("第一架军用机")
