# -*-coding: utf-8 -*-
"""
程序调试：将编写好的程序投入实际运行前，用手工或者编译程序等方式进行测试，修正"语法错误和逻辑错误"的过程
常用方法：
    * 对应位置使用print或者logging打印日志信息
    * 启用断点模式debug调试
"""
import logging

# 设置日志级别为：INFO
logging.basicConfig(level=logging.INFO)
name = "fang"
age = 20
print("her name is " + name + "，age is " + str(age))  # 字符串不能和数字拼接，需要将数字转换为字符串类型s：tr(）

# 需求：a = 1 时，flag = True
a = 1
b = 2
if a == 1:
    flag = False
    # print(f"当a == 1时，flag = {flag}")  # 方式1：通过print输出关键信息的方式
    logging.info(f"当a == 1时，flag = {flag}")  # 方式2：通过logging输出相关日志信息
else:
    flag = True
    # print(f"else，flag = {flag}")  # 方式1：通过print输出关键信息的方式
    logging.info(f"else，flag = {flag}")  # 方式2：通过logging输出相关日志信息
# 方式3：debug
"""
1、在需要暂停执行的位置启用断点，然后点击右键选择debug或者点击页面上方的小虫子图标
2、在执行debug过程中，Debugger栏的左侧的Frames里展示的是程序执行过程中的一些堆栈的信息，右侧的Variables里显示的是程序执行过程中的一些变量信息
3、如果有相应的输出信息的话，在Console里可以看到，debug的几个图标含义理解如下：
    * Step Over：当前文件从上到下按顺序一步步执行，不会进入到子函数，碰到当前调用的函数也不会进入函数体内
    * Step Into：遇见方法进入方法，查看方法及子方法的具体执行过程
    * Step Out：从方法或字方法跳出到当前代码的下一步继续执行
    * Step Into My Code：进入我们自己编写的代码行（一般是查看方法或字方法已经得知想要的信息，不需要继续查看但又还没有执行完成时）
    * Run to Cursor：执行光标所在行
    * Force Step Into：遇见方法时强制进入方法或子方法
"""

