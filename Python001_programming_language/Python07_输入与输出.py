# -*-coding: utf-8 -*-
"""
知识大纲：
    * 字面量打印与格式化
    * 文件读取
    * JSON格式转换
"""
"""
1、字面量(literal)定义：是以变量或者常量给出的原始数据。在程序中可以直接使用
2、类型：
    * 数值
    * 字符串
    * 布尔类型
    * 字面量集合：列表list、元组tuple、字典dict、集合set
    * 特殊字面量：None
3、字面量插值：将变量、常量以及表达式插入的一种技术，可以避免字符串拼接的问题，很多语言支持了该功能，字面量插值有以下几种常见的方法：
    * 格式化输出：%的用法，转换说明符如下
        %d 和 %i：转换为带符号的十进制整数
        %o：转换为带符号的八进制整数
        %x 和 %X：转换为带符号的十六进制整数
        %e：转换为科学计数法表示的浮点数（e小写）
        %E：转换为科学计数法表示的浮点数（E大写）
        %f 和 %F：转换为十进制浮点数
        %g：智能选择使用 %f 或 %e 格式
        %G：智能选择使用 %F 或 %E 格式
        %c：格式化字符及其ASCII码
        %r：使用repr()函数将表达式转换为字符串
        %s：使用str()函数将表达式转换为字符串
    * 通过string.format()方法拼接：不填入索引时，传入参数的数量必须大于或等于定义的变量
    * formatted string literals，字符串格式化机制（Python版本>=3.6）
"""
name = "小红"
age = 22
high = 1.62
list_person = ["小美", 20, 1.73]
tuple_person = ("小花", 21, 1.61)
dict_person = {"name": "小芳", "age": 23, "high": 1.61}
set_person = {"小邹", 20, 1.58}
# 字面量插值方法一：格式化输出
print("方法1：", "her name is %s,her age is %d,her high is %.2f" % (name, age, high))  # %f默认小数点后6位，如需精确到小数点后2位，可写%.2f

# 字面量插值方法二：string.format()方法
print("方法2：", "her name is {},her age is {},her high is {}".format(name, age, high))  # string.format()方法默认小数点后2位
# string.format()里的参数有索引，可填入索引到{}中，打乱默认插入的顺序，也可以多次调用
print("方法2：", "her name is {2},her age is {1},her high is {0}{1}{2}".format(age, name, high))
# string.format()方法里的参数支持字符串、列表、元组、字典、集合、常量
print("方法2：", "her name is {},her age is {},her high is {}".format("小李", 20, 1.65))  # 支持字符串，数字
# 支持列表、元组、字符串、字典等所有数据类型作为参数,支持参数索引
print(
    "my list is{},my tuple is {},my dict is {},my set is {}".format(list_person, tuple_person, dict_person, set_person))
# 支持字符串解包，支持字符串索引值传入{}，默认按顺序取
print("方法2_string：", "her name is {2},her age is {5},her high is {6}".format(*"abcdefg"))
# 支持列表解包，支持索引，不输入索引值默认按顺序取
print("方法2_list：", "her name is {0},her age is {1},her high is {2}".format(*list_person))
# 支持元组解包，支持索引，不输入索引值默认按顺序取
print("方法2_tuple：", "her name is {0},her age is {1},her high is {2}".format(*tuple_person))
# 支持字典解包，字典解包为2个星号**，传入字典的key到{}则会获取对应的value
print("方法2_dict：", "her name is {name},her age is {age},her high is {high}".format(**dict_person))
# 如果字典解包使用一个*，则默认传入字典的所有key，支持索引传key
print("方法2_dict：", "her name is {2},her age is {1},her high is {0}".format(*dict_person))
# 集合也支持用星号*解包，只是元素无序，无索引概念，即使填入索引也没有效果
print("方法2_set：", "her name is {},her age is {},her high is {}".format(*set_person))

# 字面量插值方法三：formatted string literals，F-strings，字符串格式化机制
print("方法3：", f"her name is {name},her age is {age},her high is {high}")  # 默认小数点后2位，该方法最为简单
# 注意：在引用字典的key时，用单引号，为了和外层string的双引号区分开
print("方法3：", f"her name is {tuple_person[0]},her age is {list_person[1]},her high is {dict_person['high']}")
# {}里支持函数
print(f"her name is {list_person[0].upper()}")
# {}里支持表达式，不支持转义符和冒号，如果出现则需要用括号括起来
print(f"her age is {(lambda x: x * 9)(2)}")

"""
文件操作：
    * 打开文件，获取文件描述符：open(file,mode="r",buffering=None,encoding=None,errors=None,newline=None,closefd=True,opener=None)
        file：文件名称（字符串）
        mode：打开方式，只读为r(read)，写入w(write)，以可写方式打开并且在文件末尾追加内容a，默认为只读r
        buffering：寄存区缓存
            0：不寄存
            1：访问文件时会寄存
            >1：寄存区的缓冲大小
            负值：寄存区的缓冲大小则为系统默认
    * 操作文件描述符（读、写）
    * 关闭文件：文件读写操作完成后，应该及时关闭
"""
# 普通的文本文件读取，mode使用默认的rt即可，wt(w为写入)
print(open("Python07_data.txt", "r"))  # 获取的是一个IO对象
file = open("Python07_data.txt", "r")
# 读取文件里所有内容
# print(file.read())  # 缺点：文件内容较大时，大于内存时，会造成资源不够而阻塞
# 文件是否可读，可读返回True，反之返回False
print(file.readable())
# 每执行一次读取一行(包括行的结束符，\n)，返回一个字符串，参数为数量，表示读取首行的几个字符
print(file.readline(3))
# 读取文件所有行，每一行以字符串格式作为元素返回一个列表。这里因为上面readline()方法已经读取了第一行，内存指针指向第二行，所以是从第二行开始读取
print(file.readlines())
# 关闭文件流管道，释放系统资源
file.close()

# with open("file") as file_name:方法的语句块里也可以对文件进行读写操作，操作完自动关闭文件，无需手动关闭
with open("Python07_data.txt") as f:
    print(f.readlines())  # 因为上面执行过file.close()再重新打开的，新打开的文件指针默认在第一行的首位，所以此处是从第一行的首位开始读取

with open("Python07_data.txt") as file_name:
    while True:
        file_first_line = file_name.readline()  # 获取第一行
        if file_first_line:  # 如果第一行有数据（返回True)
            print(file_first_line, end="")  # 打印第一行，并且将末尾的换行符去掉，文件里本身带了换行，每执行一次print也会换行，所以去掉一次
        else:  # 如果第一行为空（返回False)
            break  # 跳出循环

# 如果读取的是一个图片，则需要指定其module为rb，二进制文件
with open("picture.png", "rb") as picture:
    print("\n", picture.read())

"""
JSON格式转化：
JSON（属于字典dict类型）：
    * 轻量级的数据存储、交换格式
    * 友好，易读写（比xml、protobuf要好）
    * 对机器友好，易于解析和生成
    * 由列表和字典组成
JSON使用场景：
    * 生成：将对象生成为字符串，存入文件、数据库，在网络传输等
    * 解析：解析来自文件、数据库、网络传输的字符串成Python对象
    * 跨语言的数据交换：比如Python和C、C++、Java、JavaScripts的数据交换
JSON常用方法（JSON为Python自带的标准库，import json即可）：
    json.dumps(python_object)：把数据类型转换成字符串
    json.loads(json_string)：把字符串转换成JSON
    json.dump()：把数据类型转换成字符串并储存在文件中
    json.load(file_stream)：把文件打开，把里面的字符转换成JSON数据类型
"""
import json

# 定义一个字典格式的数据
data = {
    "name": ["Jerry", "Tom", "Lily"],
    "age": 6,
    "gender": "female"
}
print("data的数据类型为：", type(data))
# 将JSON的dict类型转化为字符串类型
str_data = json.dumps(data)
print("str_data的数据类型为：", type(str_data), "\n", "str_data为：", str_data)
# 使用str()方法也可以将data转化为str类型，只是里头的数据结构不能保持，无法通过json.loads(str_data1)再转回JSON格式：
str_data1 = str(data)
print("str_data1的数据类型为：", type(str_data1), "\n", "str_data1为：", str_data1)
# 再将字符串类型转化为JSON类型
json_data = json.loads(str_data)
print("json_data的数据类型为：", type(json_data), "\n", "json_data为：", json_data)