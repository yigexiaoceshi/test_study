# -*-coding: utf-8 -*-
"""
1、Python分支机构
    * 一条条语句按照顺序执行叫做顺序结构
    * 某个判断条件下，选择其中一条分支去执行叫做分支结构
    * 关键字：if、elif、else，使用判断使代码执行分支结构必须以if开头，elif和else必须有一个或者可同时有，不可同时没有
    * 缩进：如果if、elif、else条件成立的情况系需要执行多条语句，只要保持这些语句具有相同的缩进即可
"""
import random

# 示例一：扁平化分支（if ... elif ... else ...）
a = 3
if a == 0:  # 须带判断条件
    print("a等于0")  # 满足if条件的所有语句保持相同的缩进
elif a == 1:  # 须带按断条件
    print("a等于1")
elif a == 2:  # 须带判断条件
    print("a等于2")
else:  # else表示上述条件都不满足时走else分支，不带判断条件
    print("a不等于0，a不等于1，a不等于2")  # 同理，满足else的所有语句保持相同的缩进
# 示例二：嵌套分支（例子：如果x>1，则f(x)=3x-5;如果-1<=x<=1，则f(x)=x+2；如果x<-1，则f(x)=5x+3）
x = 6
if x > 1:  # 注意比较运算符两端的数据类型是否可执行比较
    y = 3 * x - 5
else:
    if -1 <= x <= 1:
        y = x + 2
    elif x < -1:
        y = 5 * x + 3
    else:
        print("x不是正数")
print(y)
# 小结：能扁平化实现的尽量不要使用多层嵌套，可读性不高
"""
2、Python循环结构
    * 循环语句允许执行一个语句或语句组多次
    * Python提供了for循环和while循环
    a、循环语句：for ... in ...
        场景：明确知道循环次数，或对一个容易进行迭代
        range函数：range(start,end,step)
            * range可用来产生一个不变的数值序列，这个序列通常用在循环当中
            * range(101)产生0-100的整数序列（）
            * range(1,100)产生0-99的整数序列
            * range(1,100,2)产生0-99的奇数序列（因为设置了步长为2）
    b、循环语句：while 表达式
        场景：不知道循环次数，通过表达式转换出False或True来控制循环是否继续，可以和else结合使用
        注意：while True加子语句是个死循环，在循环体里要使用break跳出，否则会一直执行下去
"""
# 示例一：使用for ... in ...循环求1-100的和
sum_1_100 = 0
for i in range(101):  # range(101)相当于range(0,101,1)，起始数字默认为0可省略，步长默认为1可省略，前闭后开原则(包含起始位置，不包含结束位置)
    sum_1_100 = sum_1_100 + i
    print("sum_1_100等于：", sum_1_100)
print(sum_1_100)
# 示例二写法一：使用for ... in ...循环求1-100偶数之和
sum_ou = 0
for i in range(101):
    if i % 2 == 0:  # 除以2余数为0，过滤掉进入if语句的i全部为偶数
        print(i)
        sum_ou = sum_ou + i
    else:
        continue
print("sum_ou的值为：", sum_ou)
# 示例二写法二：使用for ... in ...循环求1-100偶数之和
sum_ou1 = 0
for i in range(2, 101, 2):  # range(0,101,2)从0到100，步长为2，即i的取值全为偶数，此时起始数字可为0也可为2，为1时求1-100奇数之和
    print(i)
    sum_ou1 = sum_ou1 + i
print("sum_ou1的值为：", sum_ou1)
# 示例二写法三：使用while循环求1-100偶数之和
i = 0
sum_ou2 = 0
while i <= 100:  # 表达式i<=100返回True时，会一直循环执行循环体里的语句，返回False时自动跳出循环，继续执行循环体外面的语句
    sum_ou2 = sum_ou2 + i
    i = i + 2  # i的初始值我0，每次累加2则在循环体里i一直是偶数，求奇数之和则i=i+1
else:
    print("循环结束啦！")
print("sum_ou2的值为：", sum_ou2)
# while 表达式里的子语句如果比较精简，可以写在一行
str_a = 1
while str_a == 1:
    str_a = str_a + 1
else:
    print("str_a不等于1.")
    print(str_a)

"""
break：
    * 用来跳出break所在的当前for和while循环体，如果是嵌套语句，break在子嵌套循环里则只会跳出子嵌套循环（当前循环的所有其他分支也不再执行），外层循环依然会执行
continue:
    * 用来跳过continue所在的当前循环模块后面的剩余语句，继续执行下一轮循环
"""
for j in range(1, 11):
    if j == 5:
        break
    print("j=", j)

for k in range(1, 11):
    if k == 5:
        continue  # k == 5时执行continue，跳过当前循环体里所有的剩余语句，不在执行print，继续执行下一轮循环，所以打印的k不包含5
    print("k=", k)
"""
练习题：猜数字
计算机出一个1-100的随机数，分别根据人输入的数字判断是否相等，猜大或猜小了给出提示，猜对了终止循环
"""
computer_number = random.randint(1, 100)  # Python自带函数random.randint(start,end)生成start到end之间的随机整数，接受2个整数入参
print(computer_number)
while True:
    person_number = input("请输入要猜的数字：")  # input("string")方法输入的内容我字符串，要和数字做比较需要int(string)转换成数字类型
    if computer_number > int(person_number):
        print("猜小了，再大一点！")
    elif computer_number < int(person_number):
        print("猜大了，再小一点！")
    else:
        print("恭喜你猜对了！")
        break
