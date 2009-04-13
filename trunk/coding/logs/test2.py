# coding:utf-8

import logging
import sys

def get_log():
    logger = logging.getLogger("test")
    hdlr = logging.FileHandler("sdjfkldsfk.log", encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    print sys.path
    hdlr2 = logging.StreamHandler(sys.stdout)
#    hdlr3 = logging.handlers.RotatingFileHandler("has_max.log", maxBytes=50, backupCount=3, encoding="utf-8")
    hdlr2.setFormatter(formatter)
#    hdlr3.setFormatter(formatter)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.addHandler(hdlr2)
#    logger.addHandler(hdlr3)
    logger.setLevel(logging.DEBUG)
    return logger


#"application" code
class testss:
    def __init__(self):
        tttt = "dff"
        self.sdf = tttt
    def fun1(self):
        logger = get_log()
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error(u"error message, 中文.")

        logger.critical("critical message")
        
        
xxx = testss()
xxx.fun1()




