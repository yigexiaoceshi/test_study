# -*-coding: utf-8 -*-
"""
面向对象：Java、Python、C++等
面向过程：C
    * 什么是面向对象？
    * 类、方法、类变量的定义
    * 实例引用、实例变量的引用
"""


# 创建一个人的类别：
# 定义类使用关键字class，后面带类的名称，以冒号结尾，或者类名()加冒号
class Person:
    name = "人类的名字"  # 类变量，定义在类里面的变量，类里面的属性，类的每个实例化对象都拥有的初始属性及属性值
    age = 0
    gender = "male"
    weight = 0

    # 类里面定义的方法，用def关键字，方法名(self)：,括号里的self代表的是当前类
    def __init__(self, newname, newage):  # 构造函数是每个类自带的函数，在当前类每次被实例化的时候都会立马调用一遍
        self.name = newname  # 将传进来的值赋值给类的实例变量，类的实例变量以"self.变量名"访问，代表每个具体的实例化对象的属性值
        self.age = newage

    # def set_newname(self, newname):
    #     self.name = newname
    #     print(f"我的新名字是{self.name}")

    def eat(self):
        # 方法体里的内容必须要写在缩进的代码块里
        print("吃")

    @classmethod  # 加装饰器@classmethod后变成类方法，类可以直接访问"类名.方法名"
    def play(self):
        print("玩")

    def jump(self):
        print(f"{self.name}跳")


# 定义好类本身没有作用，只有实例化出实例对象才可以使用类的属性及方法
zhangsan = Person("张三", 20)  # 实例化类对象时，需要在类后面带括号，表明是类的一个实例
# 类的实例对象才可以使用类里面定义好的属性和方法，实例对象.下拉带出来的f标记的表示属性，m标记的表示方法，方法有(self)，还有类本身的属性和方法
print(zhangsan.name, zhangsan.age)  # 实例对象.属性
zhangsan.eat()  # 实例对象.方法名()
# 类的实例对象可以自己修改属性
# zhangsan.set_newname("张三")
# 代码从上至下运行，执行了zhangsan.set_newname("张三")后，类变量的name被改成了"张三"
print(f"zhangsan的姓名是{zhangsan.name},zhangsan的年龄是{zhangsan.age}")

# 再创建一个实例
lisi = Person("李四", 21)
print(f"lisi的姓名是{lisi.name},lisi的年龄是{lisi.age}")
lisi.jump()

# 类变量通过"类名.变量名"访问：
print(Person.name)
# 类变量的值通过"类名.变量名 = 新的值"来进行修改：
Person.name = "人类的新名字"
print(Person.name)
# 实例变量通过"实例化对象.变量名"或者"类名(参数1,参数2).变量名"访问（第二种方法一般不用，只是等同于这个意思，加深理解）：
print(zhangsan.name)
# 实例变量的值通过"实例化对象.变量名 = 新的值"来进行修改
zhangsan.name = "张三的新名字"
print(zhangsan.name)
# 同上，更改实例对象的值：
Person("王五", 22).name = "王五的新名字"
# 此时执行的Person("王五",22)和上面执行过Person("王五",22)="王五的新名字"里的Person("王五",22)已经不是同一个实例对象，所以输出的还是i"王五"
print(Person("王五", 22).name)

# 类里面的方法访问：
# Person.eat()  # 类不能直接调用类的普通方法（又叫实例方法），需要在类方法上加装饰器"@classmethod"
Person.play()  # 类里定义的实例方法play()加了装饰器"@classmethod"后成为类方法后，类可以直接访问
zhangsan.eat()  # 类的实例可以调用类的实例方法，类方法名后面默认传入self参数，意思是类的实例在调用类方法时，默认将类本身传入到参数的第一个位置
zhangsan.play()  # 类的实例也可以调用类方法
"""
小结：类方法可以被类和类的实例化对象调用，实例方法只能被类的实例化对象调用，实例方法无装饰器@classmethod，类方法有装饰器@classmethod
"""
