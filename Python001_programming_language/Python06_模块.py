# -*-coding: utf-8 -*-
"""
项目的目录结构
    1、Python的程序结构包含：package(包)、module(模块)、function(方法)
模块定义
    1、模块就是包含Python定义和语句的以.py结尾的Python文件，能作为脚本运行
    2、模块内一般都定义一些变量/类/方法等
    3、模块分为：系统内置模块(time、sys、re、os、json等，无需安装)、第三方的开源模块(须安装，pip install 模块名)、自定义模块
文件引用
    import 包目录.模块名称：调用则需要带模块名"包目录.模块名.方法名()"
    from 模块名称 import 对应模块里的方法/变量/类：调用"方法名()"即可，多个变量、方法、类可以使用逗号隔开，导入一次即可
    from 模块名称 import *：调用"方法名()"
    注意：同一个模块写多次，被import多次，只会被导入一次；一般import放在代码的最顶端
"""
# 系统内置模块
import sys  # 建议单独导入
import os, re, json, time  # 在当前模块里没有引用到导入模块里的任意方法、变量、类等等的时候就会是置灰状态

from Python001_programming_language.Python04_函数 import function_01  # 自定义模块的导入，从最上层的包目录导入，即package

# 获取当前模块执行import时的所有查找路径，按照查找顺序返回一个列表，从结果可以看到查找顺序为：当前目录>当前项目>当前虚拟环境>系统环境
print("当前模块执行import的查找路径为：", sys.path)  # 所以如果当前项目或当前目录下有和系统模块相同命名的模块时，默认导入当前项目或当前目录下的模块

print(os.times())

print(re.purge())

time.sleep(1)  # 执行到该语句时，强行等待1秒后继续执行
# 第三方开源模块：需要"pip install 模块名"或"pip install 模块名==固定版本"进行安装，然后才可以导入使用
import yaml

# 自定义模块：属于自己编写的模块，对某些逻辑或某些函数进行封装后提供给其他模块调用
function_01()
# import Python001_programming_language.Python04_函数  # 直接导入"包目录.模块名"也可以
# Python001_programming_language.Python04_函数.function_01()  # 导入的时候带了包目录，调用时也需要带包目录"包目录.模块名.方法名()"
# import Python04_函数  # 调用模块和被调用模块在同级目录下时，可直接导入模块名称
# Python04_函数.function_01()  # 同级目录下导入的模块名，在调用时不需要带包目录"模块名.方法名()"
"""
模块里常用的方法（定位问题的时候常用一下2个方法）：
    dir()：找出当前模块定义或引用的对象，包括当前模块和导入的模块定义的类、方法、函数、变量等
    dir(sys)：找出sys模块定义的对象，包括定义的类、变量、方法、函数等
"""
print(dir())
print(dir(sys))
"""
编码模块化的好处：
    1、代码可维护性提高
    2、编码效率提高
    3、函数名称可重复（尽量避免和系统模块重名）
"""