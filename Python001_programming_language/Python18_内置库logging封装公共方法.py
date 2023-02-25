# -*-coding: utf-8 -*-
import logging
import os


def get_logger():
    # 创建记录器
    logger = logging.getLogger(os.path.basename(__file__))  # 当前文件名
    logger.setLevel(logging.DEBUG)
    # 创建处理器
    ch2 = logging.StreamHandler()
    ch2.setLevel(logging.DEBUG)
    # 创建格式器，定义日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 添加格式器到处理器
    ch2.setFormatter(formatter)
    # 添加处理器到记录器
    logger.addHandler(ch2)
    return logger


logger = get_logger()
print(logger)

# 应用代码
logger.debug('这是debug级别日志')
logger.info('这是info级别日志')
logger.warning('这是warning级别日志')
logger.error('这是error级别日志')


def log_info(message):
    logger.info(message)


logger.critical('这是critical级别日志')
