# -*-coding: utf-8 -*-
import logging.config
# 引用logging.conf文件
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("main")
logger.debug("这是debug日志")