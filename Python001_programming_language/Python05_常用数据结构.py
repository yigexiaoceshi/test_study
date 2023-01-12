# -*-coding: utf-8 -*-
"""
列表[list]：
    * 通过组合一些值得到多种复合数据类型
    * 最常用的数据结构
    * 通过[]括起，里面元素用逗号分割的一组值
    * 一个列表可包含各种不用类型的元素，但是通常使用的时候都是相同类型的元素
    * 序列化数据类型（tuple、list、range都是），支持排序，支持切片操作
    * 可变数据类型
列表的特性（常见的内置的方法）：
    list.append(x)；在列表的末尾添加一个元素，相当于定义最后一个元素，即list[len(list):]=[x]
    list.insert(i,x)：在指定下标i的位置插入一个元素x，i为0时插在列表最前面，list.insert(len(list),x)插在列表末尾，等同于list.append(x)
    list.remove(x)：移除列表中第一个值等于x的元素，如果不存在x元素，则抛出ValueError异常
    list.pop([i])：删除列表中下标为i的元素并返回该元素值；如果没有指定i，list.pop()将会删除列表最后一个值并返回该值
    list.sort(key=None,reverse=False)：对列表中的元素进行排序（参数可用于自定义排序，解释参考sorted()方法）,reverse默认值为False，即升序排列
    list.reverse()：翻转列表的元素
    list.clear()：删除列表所有元素，相当于del list[:]
    list.extend(iterable)：将可迭代对象iterable里迭代处的元素添加到列表，相当于list[len(list):]=iterable
    list.index(x[,start[,end]])：返回列表第一个值为x的元素的从0开始的索引，没有则抛出ValueError异常；可选参数start和end是切片符号，用于指定搜索的列表的子序列，返回的索引是相对整个序列开始计算的，而不是start参数开始计算
    list.count(x)：返回元素x在列表中出现的次数
    list.copy()：返回列表的一个浅拷贝，相当于list[:]
注意：
    1、insert/remove/sort方法，仅修改列表，没有打印返回值，默认返回None。这是Python所有可变数据结构的通用设计原则
    2、并非所有的元素类型都可以排序或比较(如字符串和数字不可比较)
    3、insert方法索引越界不会报错，索引越出最左侧则等同于0，越出最右侧最默认插在列表末尾
    4、pop方法索引越界会报错：pop index out of range
"""
list_a = [10, 2, 3, 8, 1, 2, 5, 9, 0]
list_a[0] = 99
print("修改第一个元素的值为99：", list_a)
list_a.append(4)  # 返回值为None
print(list_a)
list_a.insert(1, "hello Python")  # 下标一的元素前面添加元素"a"，或者说将元素"a"插入下标为一的位置，原来下标一的元素往后挪到下标为二的位置，返回值为None
print(list_a)
list_a.remove(3)  # 删除列表中第一个值为3的元素，不存在则抛出ValueError异常，返回值为None
print(list_a)
a_pop = list_a.pop(1)  # 删除列表中索引为1的值并返回该值，赋值操作是先执行右边的表达式，得出结果后赋值给左边定义的变量来接收
print("被删除的元素是：", a_pop)
print(list_a)
list_a.sort()  # 等同于list_a.sort(reverse=False)，reverse默认为False，即升序排列
print(list_a)
list_a.reverse()  # 翻转列表，不论排序
print(list_a)
b_count = list_a.count(2)  # 获取元素2在列表list_a中出现的次数，并返回该整数型数值
print("元素2出现的次数为：", b_count)
list_a.extend(range(20, 25))  # list.extend(iterable)参数为可迭代对象，将可迭代对象里迭代出的值依次添加到列表的末尾
print(list_a)
c_index = list_a.index(5)
print(c_index)
d_index = list_a.index(5)
"""
列表推导式：简单的创建列表的方法。常见用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或通过满足某些特定条件的元素来创建子序列
    * 写法：list_square = [带参数的返回值表达式 带参数的可迭代对象]，如list_square=[x for x in range(1,5)]
    * 注意：可迭代对象里可以加入嵌套循环、if条件判断等
"""
# 使用for ... in ...循环生成平方列表
list_square1 = []
for i in range(1, 11):
    list_square1.append(i ** 2)
print("for...in...循环生成的平方列表list_b为：", list_square1)
# 使用列表推导式生成平方列表
list_square2 = [j ** 2 for j in range(1, 11)]
print("列表推导式生成的平方列表list_square2为：", list_square2)
# 列表推导式生成列表，支持嵌套循环即if条件判断
list_square3 = [i * j for i in range(1, 6) if i != 5 for j in range(6, 11) if
                j != 10]  # i为1到4四次大循环，i!=5的条件写在大循环，每次大循环里头嵌套j的6到9四次小循环，j!=10条件写在小循环
print("列表推导式生成的列表，加入嵌套循环：", list_square3)
print(list_square3.__len__())
# 上面列表推导式加嵌套循环和if判断的写法等同于（去掉了冒号和缩进，写在了一行）:
list_square4 = []
for i in range(1, 6):
    if i != 5:
        for j in range(6, 11):
            if j != 10:
                list_square4.append(i * j)
print("使用for ... in ...嵌套循环加条件判断生成的列表list_square4为：", list_square4)
print(list_square4.__len__())

"""
元组（tuple）：
    * 使用()来定义，也可不加，仅有一个元素时，该元素后面须加逗号；定义空元组时则必须加括号
    * 序列化数据类型，支持索引和切片
    * 不可变数据类型，可以通过解包和索引来访问，不可变数据类型指的是元组里的所有元素指向的内存空间不可被修改，比如数字和字符串不可修改，但是列表、集合和字典可修改
"""
# 两种定义方式（括号可加可不加）
tuple_a = (1, 2, 3)
tuple_b = 1, 2, 3
print(type(tuple_a), type(tuple_b), tuple_a, tuple_a)
# 使用推导式：生成的是生成器对象，而不是一个元组，该对象可转换成元组或列表
tuple_y = (i * 3 for i in tuple_a)
print("使用推导式生成的元组为一个生成器对象：", type(tuple_y), "推导式生成的元组为：", tuple_y)
print("使用推导式生成的生成器对象转换成列表：", list(tuple_y), "使用推导式生成的生成器对象转换成元组：", tuple(tuple_y))
tuple_c = 1,  # 注：因为创建元组的方式可以不加括号，所以仅有一个元素的时候一定要在后面加个逗号，即tuple_c=(1,)，否则会相当于单个元素直接复制
print("tuple_c的数据类型为：", type(tuple_c), "tuple_c：", tuple_c)
tuple_d = ()
print("tuple_d的数据类型为：", type(tuple_d), "tuple_d：", tuple_d)
# 元组的不可变
list_b = [1, 2, 3]  # 定义一个列表
tuple_e = (1, "abc", list_b)  # 将列表作为元组的一个元素
print("tuple_e为：", tuple_e)
list_b.append(4)  # 修改列表里的值，因为列表是可变数据类型，修改列表的值不会需改该列表指向的内存空间地址，所以当前元组理解为未发生改变
print("修改元素列表的值后，tuple_e为：", tuple_e)
print("tuple_e的内存地址为：", id(tuple_e))
tuple_e[2][3] = "4ABC"  # 将元组的索引为2的元素，即列表list_b的索引为1的元素修改为111
print("修改元素列表的值后，tuple_e为：", tuple_e)
print("修改元素列表里的值后，tuple_e的内存地址为：", id(tuple_e))  # 该元组指向的内存空间地址并未发生改变
"""
元组的内置函数：
    tuple.count(a)：计算元组tuple里元素a出现的次数
    tuple.index(a)：得出元组tuple里元素a第一次出现的索引
"""
tuple_f = (1, 2, 2, 3, 4, "aa")
print("元组tuple_f里元素2出现的次数为：", tuple_f.count(2))
print("元组tuple_f里元素2的索引为：", tuple_f.index(2))  # 多个重复元素时，取最近一个元素的索引
"""
集合{1,2,"a"}：
    * 元素不重复（自动去重），无序，所以无法切片和排序，不能通过索引访问
    * 基本用法：元素检测，元素去重
    * 可以使用{}或set()函数创建集合，使用{}创建时，没有任何元素时为字典，而不是集合，空集合只能使用set()创建，set()方法也只能创建空集合
"""
# 使用{}创建集合
set_a = {1, 2, 3, 3, 4, 5, 6}
print("集合set_a的数据类型为：", type(set_a), "集合set_a为：", set_a)  # 元素3被去重
# 使用set()函数创建集合
set_b = set()
print("集合set_b的数据类型为：", type(set_b), "集合set_b为：", set_b, "集合set_b的长度为", set_b.__len__())
# 使用集合推导式创建集合
set_c = {i * j for i in range(1, 6) if i != 5 for j in range(6, 11) if j != 10}
print("使用推导式创建的集合set_c为：", set_c)  # 元素去重，顺序随机
set_c1 = {i for i in "fjsaofhsoafhodasufewfw0 ouf wjo;jsfosaofsjaoj923bub492yrnoj"}
print("使用推导式创建的集合set_c1为：", set_c1)  # 元素去重，顺序随机，后续生成随机数字和大小写字母验证码的场景会用到
print(list(set_c1))
print(tuple(set_c1))
str_a = ""
for i in set_c1:
    print(type(i), i)
    str_a = str_a + i
    print("遍历集合set_c1的元素拼接成字符串：", str_a)
"""
集合的内置函数
"""
set_d = {1, 2, 3, 4, 5}
set_e = {4, 5, 6, 7, 8}
# 求2个集合的并集(2个集合元素相加之后去重)
print("集合set_d和set_e的并集为：", set_d.union(set_e))
# 求2个集合的交集(2个集合共同的元素)
print("集合set_d和set_e的交集为：", set_d.intersection(set_e))
# 求2个集合的差集
print("集合set_d和set_e的差集为：", set_d.difference(set_e))  # set_d.difference(set_e)指set_d存在，set_e不存在的元素
# 添加元素：默认添加在最末尾
set_d.add("a")
print("添加元素之后的set_d为：", set_d)

"""
字典{key1:value1,key2:value2}：
    * 以关键字为索引，即key
    * 关键字是任意不可变数据类型，通常是字符串或数字；如果一个元组里的元素全部都是不可变数据类型(string/number/tuple)，那么该元组也可以作为关键字，即key
    * 布尔值也为不可变数据类型，也可以用作key，只是不常用
"""
# 使用{}定义字典：dict = {key1:value2,key2:value2}
dict_01 = {"a": 1, "b": 2}
print("字典dict_01的数据格式是：", type(dict_01), "字典dict_01为：", dict_01)
# 定义空字典：dict = {}
dict_02 = {}
print("字典dict_02的数据格式是：", type(dict_02), "字典dict_02为：", dict_02)
# 使用dict()函数定义字典：dict = dict(key1=value1,key2=value2)
dict_03 = dict(a=1, b=2)
print("字典dict_03的数据格式是：", type(dict_03), "字典dict_03为：", dict_03)
# 使用推导式生成字典
dict_04 = {x: y for x in range(1, 4) for y in "abc"}
print("使用推导式生成的字典dict_04为：", dict_04)  # 结果为{1: 'c', 2: 'c', 3: 'c'}，因为一次大循环为一个key只能对应一个value，也就是小循环最后一个值
"""
字典常用内置函数
"""
# 定义一个字典
dict_05 = {"a": 1, "b": 2, "c": 3, "d": 4, 5: "e", (1, 2, 3): [1, 2, 3], "c": 6}  # key一般不允许重复，如果多个key则默认取最后一个value
# 获取字典所有的key，返回一个元素全部都是key的列表
print("字典dict_05所有的key是：", dict_05.keys())
# 获取字典所有的value，返回一个元素全部都是value的列表
print("字典dict_05所有的value是：", dict_05.values())
# 根据指定的key获取对应的value
print("字典dict_05的key为c对应的value是：", dict_05.get("c"))  # 一个key只能对应一个value，同一个key对应多个不同的value默认取最后一个
# dict.pop(key)，根据该key删除该键值对，并且返回该key对应的value，如果key重复对应不同的value，则会删除所有相同的key的键值对并返回最后一个对应的value
print("删除字典dict_05中key为c的键值对，并返回该value：", dict_05.pop("c"))
print("删除字典dict_05中key为c的键值对后：", dict_05)
# dict.popitem(),随机删除dict里的一个键值对，并返回一个元组，元组里的元素为被删除的键值对的key和value
print("随机删除dict_05里的一个键值对，并返回一个元素为被删除键值对的key和value的元组：", dict_05.popitem())
# dict.fromkeys(iterable,value1,value2),第一个参数为序列化对象,如字符串、列表、元组等，里面的元素按照索引依次作为dict的key，后面的value可以为一个或多个
dict_06 = {}
print(dict_06.fromkeys([1, 2, 3], "test_value01"))  # 第一个参数可为列表，value可为任意字符
print(dict_06.fromkeys((11, 22, 33), False))
print(dict_06.fromkeys("abc", [1, 2, 3]))
print(dict_06.fromkeys("efg", {1, 2, 3}))
