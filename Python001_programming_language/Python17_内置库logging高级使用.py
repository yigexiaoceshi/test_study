# -*-coding: utf-8 -*-
"""
日志模块logging底层运行的常见的几个组件：
    （日志记录器）loggers：提供应用程序代码直接使用的接口，例如logging.info('msg')等
    （日志处理器）handlers：用于将日志记录发送到指定的目的位置（输出到终端或保存文件流到指定目录的指定文件）
    （日志过滤器）filters：提供更细力度的日志过滤功能，用于决定输出哪些日志记录（其他的日志记录将会被忽略）
    （日志格式器）formatters：用于控制日志信息的最终输出格式
日志记录的流程
封装日志公共模块
日志配置文件
"""
import logging

# 创建日志记录器：logger，并且设置日志记录级别为DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)  # 这个有啥用？最终收集的日志信息都是按照处理器设置的级别来的？

# 创建日志处理器：handler，并且设置日志处理级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 创建日志格式器：formatter，定义好日志的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 将格式器formatter添加到创建好的处理器handler里
ch.setFormatter(formatter)
# 将设置好的处理器handler添加到记录器logger
logger.addHandler(ch)

# 可以再定义一个文件处理器，将日志文件流写入到文件里，设置处理日志的级别为INFO
ch_file = logging.FileHandler(filename='mylog.log', encoding='utf-8')
ch_file.setLevel(logging.INFO)
# 创建日志格式器：formatter，定义好日志的输出格式
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 将格式器formatter添加到创建好的处理器handler里
ch_file.setFormatter(formatter1)
# 将设置好的处理器handler添加到记录器logger
logger.addHandler(ch_file)

# 应用代码如下
logger.debug('这是DEBUG日志')
logger.info('这是INFO日志')
logger.warning('这是WARNIND日志')
logger.error('这是ERROR日志')
logger.critical('这是CRITICAL日志')
