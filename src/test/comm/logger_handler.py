# coding=utf-8
# author:yundanni
# create_time:2020/11/10 15:36
import logging
import os.path
import time
# sys.setdefaultencoding('gbk')
BASE_PATH =os.path.split(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0])[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
# print (BASE_PATH,LOG_PATH)



class LoggerHandler(object):

    def __init__(self,logger_file,logger_name):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        now = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        tdresult = logger_file + day
        logger_file=os.path.join(logger_file, logger_file)
        # print (tdresult)
        if os.path.exists(logger_file):
            filename = logger_file + "\\" + now + "_log.log"
            fh = logging.FileHandler(filename,encoding="utf-8")
        else:
            # 不存在以当天日期为名称的文件夹的情况，则建立一个以当天日期为名称的文件夹
            os.mkdir(logger_file)
            filename = logger_file + "\\" + now + "_log.log"
            fh = logging.FileHandler(filename,encoding="utf-8" )
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
# a=LoggerHandler('test','test_demo')
# # a.get_log("2222222222222")
