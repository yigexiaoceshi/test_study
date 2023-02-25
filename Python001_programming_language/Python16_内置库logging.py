# -*-coding: utf-8 -*-
"""
日志的作用
    调试：获取程序运行的路径或状态
    辅助定位问题
    数据分析：数据埋点，分析用户行为等
日志的级别
    debug：细节信息，仅当诊断问题时适用
    info：确认程序按预期运行
    warning：表明有已经或即将发生的意外（例如：磁盘空间不足等）。程序仍然按照预期进行
    error：由于严重的问题，程序的某些功能已经不能正常执行
    critical：严重的错误，表明程序已经不能继续执行
日志的用法
    官方说明文档地址：https://docs.python.org/zh-cn/3/howto/logging/html
    logging.debug(msg,*args,**kwargs)：创建一条严重程度为debug的日志记录（会打印debug及更高严重程度级别的日志）
    logging.info(msg,*args,**kwargs)：创建一条严重级别为info的日志记录（会打印info及更高严重程度级别的日志）
    logging.warning(msg,*args,**kwargs)：创建一条严重级别为warning的日志记录（会打印warning、error、critical级别日志）
    logging.error(msg,*args,**kwargs)：创建一条严重级别为error的日志记录（会打印error、critical级别日志）
    logging.critical(msg,*args,**kwargs)：创建一条严重级别为critical的日志记录（会打印critical级别日志）
    logging.log(level,*args,**kwargs)：创建一条严重级别为level的日志记录
    logging.basicConfig(**kwargs)：对root logger进行一次性配置
"""
import logging

# logging 默认的日志级别为warning，只会打印warning、error和critical级别的日志
# 修改日志的级别
# logging.basicConfig(level=logging.INFO)  # 修改为INFO（INFO须大写）级别，则只有debug级别的日志不会打印
#
# logging.debug("这是一条严重程度为debug级别的日志")
# logging.info("这是一条严重程度为info级别的日志")
# logging.warning("这是一条严重程度为warning级别的日志")
# logging.error("这是一条严重程度为error级别的日志")
# logging.critical("这是一条严重程度为critical级别的日志")

# 将日志输出到文档进行保存：文件流直接写入文件，不会再进行输出，这个可以在日志处理器里进行修改是输出还是保存，可通过debug查看
# 注意：如果在指定了输出文档之前已经有日志信息输出则不会创建日志文件，可使用绝对路径拼接的方式进行创建，所以注释上面一段
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.debug("debug级别")
# logging.info("info级别")
# logging.warning("warning级别")
# logging.error("error级别")
# logging.critical("critical级别")
# 设置日志的格式，可参考官网说明文档
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('发生了错误。')
