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
def task(name, url):
    # 获取每个视频文件的文件流
    response2 = requests.get(url)
    # 创建本地文件，以传入的name参数进行命名，以别名file2打开
    with open(name, mode='wb') as file2:
        # 将获取到的视频文件的文件流写入到本地文件"name"当中
        file2.write(response2.content)
    # 打印每次视频下载完成的时间
    print(f"视频 {name} 下载完成的时间为：{time.time()}")  # 3个线程全部执行完成总共差不多0.5秒左右；3个进程几乎是同一时间下载完3个视频


# print("一个进程里开启多个线程分别下载三个视频")
# print(f"多线程下载开始时间为：{time.time()}")
# for name2, url2 in url_list:
#     # 每次循环创建一个线程：threading.Thread(target=方法名或函数名,args=(参数1,参数2))，创建一个线程并将执行target里的方法作为任务分配给该线程
#     thread = threading.Thread(target=task, args=(name2, url2))
#     # 线程启动，调用task方法执行
#     thread.start()
# """
# 结束时间为什么不能放在这，因为三次循环会迅速启动三个线程并执行，在start()之后会立马执行下面的print，
# 而主线程则会等待三个子线程完全执行完成之后，程序才算是全部执行完成，从程序执行的结果里可以看到
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
if __name__ == "__main__":
    # 记录视频开始下载的时间
    print(f"开始下载视频的时间为：{time.time()}")
    for name3, url3 in url_list:
        # 每次循环创建一个进程(每个进程会自动创建一个线程，由线程来执行target里的方法)
        process = multiprocessing.Process(target=task, args=(name3, url3))
        # 启动进程里的线程开始执行task方法
        process.start()

"""
小结：
通过多线程或多进程都能提升效率，多进程对于系统资源的消耗更大，至于什么场景下使用多进程，什么场景下使用多线程，须了解Python的GIL锁机制
"""
# GIL锁
