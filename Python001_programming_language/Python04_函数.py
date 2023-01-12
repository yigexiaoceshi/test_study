# -*-coding: utf-8 -*-
"""
函数：组织好的、可重复使用的，用来实现单一或者相关联功能的代码段
    * 函数代码块以def关键字声明，后面接函数名称及()
    * 冒号起始
    * 函数内容注意缩进
    * 圆括号()中定义参数
    * 函数说明：文档字符串
    * return 表达式：结束函数，选择性的返回一个值给调用方，不带表达式的return或者不写return的函数，默认返回None
函数的作用：提高应用的模块性，提高代码重复利用率，使代码更加简洁，可读性更高
"""


# 定义一个无参数无返回值函数
def function_01():
    print("这是一个无入参无返回值的函数：function_01")


function_01()  # 函数体里的语句只有在调用函数的时候才会执行
print(function_01())  # 返回值为None


# 定义一个有入参无返回值的函数
def function_02(a, b, c):  # 定义多个位置参数在函数体中被使用到会高亮显示，没有使用到的参数置灰显示，但并不会报错
    """
    函数的说明文档
    :param a:参数a的说明
    :param b:参数b的说明
    :param c:参数c的说明
    :return:没有返回值
    """
    print("这是一个有入参无返回值的函数：function_02，参数有：", a, b)


func_02 = function_02(1, 2, 3)  # 调用函数时，位置参数为必传，且一定按照顺序对应，a对应1，b对应2，c对应3
print(func_02)  # 返回值为None


# 定义一个有无入参有返回值的函数
def function_03():
    return "string_return"  # return不写/return/return None的效果是一样的，都是返回None


func_03 = function_03()  # 函数名(参数1,参数2)即可完成调用，如果有返回值则需要赋值给一个变量，让变量去接收
print(func_03)


# 定义一个有入参有返回值的函数
def function_04(A, B, C):
    print("当前函数有三个参数哦：", A, B, C)
    return A, B, C, "DEFG"


func_04 = function_04(11, 22, 33)
print(func_04)
"""
函数的入参：
    位置参数：直接使用参数名定义"def func_01(参数a,参数b,参数c)"，调用时参数为必传，且必须按照顺序传
    默认参数：定义函数时使用key=value的方式定义，传入key=new_value则使用new_value，不传则使用默认值value
    关键字参数：定义和位置参数一致，调用时使用key=value的方式，关键字参数必须跟随在位置参数的后面
    指定关键字参数传参：在定义必须要使用关键字传参的参数前面加一个特殊参数符号*，比如 def function_07(a,b,c,d,*,e):
    特殊参数：*args 和 **kwargs
"""


# 位置参数：必传，且必须按照顺序传
def function_05(a, b):
    print("函数function_05的位置参数：", a, b)


function_05("a", "b")


# 默认参数：声明函数时使用key=value进行定义，可传可不传
def function_06(a="default"):
    print("函数function_06的默认参数a：", a)


function_06()  # 默认参数不传，则参数传入默认值
function_06("new_value")  # 默认参数传入值，则不传入默认值


# 关键字参数：必传；必须全部跟在位置参数后面(在位置参数里有一个关键字传参，则该参数后面的所有参数都必须关键字传参)；关键字参数部分不需要按照先后顺序传参
def function_07(aa, bb, cc, dd, *, ee):  # 如果要求参数ee必须用关键字传参，则在ee前面加一个,*号即可，不常用，了解即可
    print("函数function_07的参数为：", aa, bb, cc, dd, ee)


function_07(bb=2, cc=3, aa=1, ee=5, dd=4)  # 可全部使用关键字传参进行调用，在位置参数后面的关键字参数部分可以不按照顺序
function_07(11, 22, 33, 44, ee=55)  # 关键字传参必须全部都在位置参数后面
function_07(111, 222, dd=444, ee=555, cc=333)  # 关键字参数必须全部都在位置参数后面，dd使用关键字传参，则ee也必须使用关键字传参，dd和ee先后顺序随意
"""
Lambda表达式：变量 = lambda 参数1,参数2 参数1+参数2
    * 用lambda关键字创建一个小的匿名函数
    * lambda表达式的主题是一个表达式，而不是一个代码块。仅能在lambda表达式中封装有限的逻辑
"""


function_08 = lambda x, y: x ** y  # 定义2个参数x和y，返回x的y次方
# 等同于：
# def function_08(x, y):
#     return x ** y


func_08 = function_08(3, 3)
print(func_08)
