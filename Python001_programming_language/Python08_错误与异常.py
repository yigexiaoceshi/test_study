# -*-coding: utf-8 -*-
"""
1、语法错误与定位
    错误：
        * 语法错误：编写的Python语法不正确，程序编译失败，报错 SyntaxError:invalid syntax
        * 逻辑错误：语法不报错，但是逻辑不合理，比如判断条件和该条件下的逻辑不合理
        * 系统错误：系统层面，比如内存泄漏等
    异常：
        * 程序执行过程中出现的未知错误，比如定义一个相除的方法，传参的时候分母传0，就会报ZeroDivisionError:division by zero
        * 语法和逻辑都是正常的
        * 程序业务逻辑不完善引起的程序漏洞（bug）
    错误和异常的区别：
        * 异常可以被捕获和处理
        * 错误一般是编码错误、逻辑错误、系统错误
    异常类型：https://docs.python.org/3/library/exceptions.html#bltin-exceptions
    常见异常类型：除零异常、名称异常、索引异常、键异常、值异常、属性异常、导入异常等等
2、异常捕获和异常处理
3、自定义异常
"""

# 除零异常：
# def div(a, b):
#     print(a / b)
#
#
# div(1, 0)  # 报错 ZeroDivisionError: division by zero
# 名称异常:
# num = 1
# if nun == 1:  # 报错 NameError: name 'nun' is not defined
#     print("num等于1")
# 索引异常：
# list_a = [1, 2, 3]
# print(list_a[3])  # 列表索引越界，报错 IndexError: list index out of range
# 键异常：
# dict_a = {"name":"Tom"}
# print(dict_a["age"])  # 不存在的键，报错 KeyError: 'age'
# 值异常：
# num_01 = "zzz"
# print(int(num_01))  # 字符串不支持转整型，报错 ValueError: invalid literal for int() with base 10: 'zzz'
# 属性异常：一般一些常量会有一些特定的属性，操作更新这些属性值的时候就会报属性异常
"""
异常的捕获及处理
"""


def div(a, b):
    return a / b


file = open("picture.png")

try:
    # 异常1
    print(div(1, 0))  # 在执行到这一行时，已经报异常并且被捕获到了，会直接执行对应的except语句块，当前模块剩余的语句就不会再执行了
    # 异常2
    list_b = [1, 2, 3]  # try语句块里的异常，只会捕获首个异常
    print(list_b[3])
    # 异常3
    print(file.readlines())  # 假如文件读取异常，则不会再执行file.close()，这时可以将file.close()写进finally语句块
    # file.close()
# 系统内置的异常都是继承自Exceptions类，Exceptions继承自BaseException，所以这里的异常可以直接用Exceptions或BaseException进行捕获
except ZeroDivisionError as e:  # ZeroDivisionError可以用Exceptions或BaseException替代，写一个except语句就足够了
    print(f"这里有一个异常：{e}，分母不能为零")
except IndexError as ee:  # 如果每个except都指定具体的异常类型进行捕获，则对应的异常会进入对应的except语句块
    print(f"这里有一个异常：{ee}，索引越界了")
except Exception as eee:  # 除上面2种异常之外的其他异常
    print(f"这里有个异常：{eee}")
else:  # 发生异常时try进入except，不会进入else，最后进入finally
    print("没有异常时，执行try后执行else语句块，然后进入finally")
finally:
    file.close()  # 先执行try，如果有异常则进入对应的except进行处理，处理完进入finally语句块，没有异常则会执行完try后进入finally语句块

# 手动抛出异常
# def set_age(num):
#     if num <= 0 or num > 200:
#         raise ValueError  # 自定义异常不一定是系统内置存在的异常类型，可以随意，比如：raise f"年龄设置错误{num}"
#     else:
#         print(f"设置的年龄为：{num}")
#
#
# set_age(-1)  # 抛出自定义异常：raise ValueError
# set_age(20)  # 只要是相同语句块的前面跑出了异常，后面的语句都不会再执行
"""
自定义异常：
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
"""


# 自定义一个异常的类，继承自Exception
class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常，{msg}")


name = "123"
if name != "li":
    raise MyException(f"姓名不正确")
