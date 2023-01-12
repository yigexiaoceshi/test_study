#!/usr/bin/python3
# -*- coding:utf-8 -*-

#  默认参数读取
stream1 = open("123.txt")
container = stream1.writable()
print("文件是否可读：", container)
stream1.close()  # 关闭管道，释放资源

# 给与文件"写"的权限，注：一次文件流里，首次w都会清空所有内容再进行写入，直到执行close()方法关闭该文件流前都可连续写入
stream = open("123.txt", "w")  # 以"w"的方式打开文件，先清空文件里所有内容
container = stream.writable()
print("文件是否可读：", container)

# 默认从光标处往后写入
stream.write("""
            静夜思
                    李白
           床前明月光，
           疑是地上霜。
           举头望明月，
           低头思故乡
""")
stream.write("我是:\n   中国人。\n")  # 添加换行符

# writelines()方法不会自动换行，支持传入iterable，循环读取元素并写入
stream.writelines("我是中国人，\n我是湖南人，\n我是岳阳人。\n")
stream.writelines(["AAA", "BBB", "CCC", "DDD"])

# 如果mode以"a"(append)模式打开，则不会清空，在原来的内容上追加写入
