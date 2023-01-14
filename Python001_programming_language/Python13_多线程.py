# -*-coding: utf-8 -*-
import threading
import multiprocessing
import time

import requests

"""
线程：计算机中可以被CPU调度的最小单元（最终真正执行任务）
进程：计算机资源分配的最小单元（为线程工作提供资源），一个进程中可以有多个线程在工作，同一个进程中的多个线程共享该进程的资源
创建一个py文件，相当于创建一个程序，在程序被执行时，相当于创建一个进程，也可以理解为在内存中分配出一个空间，空间里创建一个线程去执行该py文件里的内容
"""
# 示例题：需要下载url_list里的三个抖音视频，创建一个ura_list变量
url_list = [("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
            ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
            ("罗斯MVP.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")]

"""
一、单线程直接下载
"""
# print("单线程直接下载三个视频")
# print(f"单线程下载开始时间为：{time.time()}")
# for name1, url1 in url_list:
#     response1 = requests.get(url1)
#     with open(name1, mode='wb') as file1:
#         file1.write(response1.content)
# # 打印该线程执行完成的时间，即视频下载完成的时间
# print(f"下载完成的时间为：", time.time())  # 差不多2秒


"""
二、一个进程里开启多个线程分别下载三个视频
"""

# 定义一个下载视频的方法
# def task(name, url):
#     # 获取每个视频文件的文件流
#     response2 = requests.get(url)
#     # 创建本地文件，以传入的name参数进行命名，以别名file2打开
#     with open(name, mode='wb') as file2:
#         # 将获取到的视频文件的文件流写入到本地文件"name"当中
#         file2.write(response2.content)
#     # 打印每次视频下载完成的时间
#     print(f"视频 {name} 下载完成的时间为：{time.time()}")  # 3个线程全部执行完成总共差不多0.5秒左右；3个进程几乎是同一时间下载完3个视频


# print("一个进程里开启多个子线程分别下载三个视频")
# print(f"多线程下载开始时间为：{time.time()}")
# for name2, url2 in url_list:
#     # 每次循环创建一个子线程：threading.Thread(target=方法名或函数名,args=(参数1,参数2))，创建一个线程并将执行target里的方法作为任务分配给该线程
#     thread = threading.Thread(target=task, args=(name2, url2))
#     # 线程启动，调用task方法执行
#     thread.start()
# """
# 结束时间为什么不能放在这，因为程序开始运行时，系统会自动创建一个进程，进程里创建一个主线程，由主线程自上而下按顺序执行代码，
# 遇到子线程创建并且执行任务时，主线程会继续向下执行，并不会停下等待子线程执行完成，而是执行完所有代码之后才会等子线程执行结束，
# 此时程序才算是全部执行完成并且终止程序执行，从程序执行的结果里可以看到
# """
# print(f"end_time为：{time.time()}")  # 创建线程并启动线程的循环执行完成后，立马会执行该print，此时子线程还没执行完成

"""
三、开启三个进程分别下载三个视频
"""
"""
为什么创建进程的代码块放到if __name__ = "__main__":里执行，这是Python内部对于不同的操作系统创建进程的机制不一样，
Linux系统基于fork创建进程，Windows系统基于spawn创建进程，而MacOS系统2这都支持(python3.8默认设置为spawn),
而使用spawn创建进程就必须要求放到if __name__ = "__main__":里执行，不然就会报错，比如Linux基于fork创建进程就可以直接在for ... in ...里执行，
如果Mac和Windows里不放在if __name__ = "__main__":里执行则需要将创建继承的模式改为fork：multiprocessing.set_start_method('fork')
如下即可：
multiprocessing.set_start_method('fork')  # 最好写在import语句下面
for name3,url3 in url_list:
    process = multiprocessing.Process(target=task,args=(name3,url3))
    process.start()
"""
# if __name__ == "__main__":
#     # 记录视频开始下载的时间
#     print(f"开始下载视频的时间为：{time.time()}")
#     for name3, url3 in url_list:
#         # 每次循环创建一个进程(每个进程会自动创建一个线程，由线程来执行target里的方法)
#         process = multiprocessing.Process(target=task, args=(name3, url3))
#         # 启动进程里的线程开始执行task方法
#         process.start()

"""
小结：
通过多线程或多进程都能提升效率，多进程对于系统资源的消耗更大，至于什么场景下使用多进程，什么场景下使用多线程，须了解Python的GIL锁机制
"""
"""
GIL锁(全局解释器锁：Global Interpreter Lock)，是CPython解释器特有的一个东西，让一个进程同一时刻只能有一个线程可以被CPU调用
    * 如果想利用计算机CPU的多核优势，让CPU同时处理一些任务，适合用多进程开发（即使资源消耗较大），GIL锁不住进程之间的并发能力
    * 如果程序不利用计算机的多核优势，适合用多线程开发
常见的程序开发中，计算操作需要使用CPU的多核优势，IO操作不需要利用CPU的多核优势：
    * 计算密集型，用多进程开发，例如：大量的数据计算（累加计算示例）
    * IO密集型，用多线程开发，例如：文件读写、爬虫、网络数据传输（下载抖音视频示例）
"""


# 累加计算示例（计算密集型）
# 1、串行处理
# start = time.time()
# result = 0
# for i in range(100000000):
#     result += i
# print(f"result等于：{result}")
# end_time = time.time()
# print(f"计算耗时为：", end_time - start)  # 总消耗的时间为15.8秒


# 2、使用多进程处理
# def task1(start_num, end_num, queue):
#     result0 = 0
#     for j in range(start_num, end_num):
#         result0 += j
#     queue.put(result0)
#
#
# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     start_time = time.time()
#     process1 = multiprocessing.Process(target=task1, args=(0, 50000000, queue))
#     process1.start()
#     process2 = multiprocessing.Process(target=task1, args=(50000000, 100000000, queue))
#     process2.start()
#     result1 = queue.get(block=True)
#     result2 = queue.get(block=True)
#     print("一亿数字累加的结果为：", result1 + result2)
#     end_time = time.time()
#     print("一亿数字累加执行的总时长为：", end_time - start_time)  # 约为5.06秒

# 在程序开发过程中，多线程和多进程是可以相互结合使用，比如创建2个进程（进程数建议和CPU核心个数相同），每个进程创建3个线程
def thread_task():
    pass


def task2(start, end):
    thread1 = threading.Thread(target=thread_task)
    thread1.start()
    thread2 = threading.Thread(target=thread_task)
    thread2.start()
    thread3 = threading.Thread(target=thread_task)
    thread3.start()


if __name__ == "__main__":
    start_time1 = time.time()
    process3 = multiprocessing.Process(target=task2, args=(0, 50000000))
    process3.start()
    process4 = multiprocessing.Process(target=task2, args=(50000000, 100000000))
    process4.start()
    end_time1 = time.time()
    print("一亿数字累加执行的总时长为：", end_time1 - start_time1)  # 基本都在0.03秒内
