# coding=utf-8
# author:yundanni
# create_time:2020/11/12 18:06
import sys
import unittest
import HTMLTestRunnerCN
import os, time
sys.path.append(sys.path[0]+'\..')
# from mail import SendMail
# result = "..\\report\\"
# casepath = "..\\case\\"
#不写下面这句，jenkins会报no module named
sys.path.append(r'D:\自动化测试\interface-auto_test')
from src.test.comm.logger_handler import LoggerHandler
BASE_PATH =os.path.split(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0])[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
casepath = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],'case\\')
result=os.path.join(BASE_PATH, 'report\\')
log_name='suite'
log_file=os.path.join(BASE_PATH, 'zhixing_log_file\\')
print (LOG_PATH,casepath,log_file)
mylogger = LoggerHandler(log_file,log_name).get_log()


class CreatSuite():
    def creatsuite(self):
        # 创建线程数组
        threads = []
        suite = unittest.TestSuite()
        # 定搜索用例文件的方法
        discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)
        # 将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
        for test_case in discover:
            suite.addTests(test_case)
        # print suite
        return suite
        # 获取系统当前时间

    def run_suite(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        # 定义单个测试报告的存放路径，支持相对路径
        tdresult = result + day

        # 若已经存在以当天日期为名称的文件夹的情况，则直接将测试报告放到这个文件夹之下
        if os.path.exists(tdresult):
            filename = tdresult + "\\" + now + "_result.html"
            # 以写文本文件或写二进制文件的模式打开测试报告文件
            fp = open(filename, 'wb')
            # 定义测试报告#
            runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'接口自动化自动化测试报告', description=u'用例执行情况如下：')
            # 运行测试用例
            runner.run(all_case)
            # 关闭报告文件#
            fp.close()
        else:  #
            # 不存在以当天日期为名称的文件夹的情况，则建立一个以当天日期为名称的文件夹
            os.mkdir(tdresult)  #
            # 以写文本文件或写二进制文件的模式打开测试报告文件
            filename = tdresult + "\\" + now + "_result.html"
            fp = open(filename, 'wb')
            # 定义测试报告
            runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
            # 运行测试用例
            runner.run(all_case)
            # 关闭报告文件
            fp.close()
            mylogger.info(u'构建成功')


if __name__ == "__main__":
    # 所有的用例集合
    cresuite = CreatSuite()
    all_case = cresuite.creatsuite()
    run_case = cresuite.run_suite()
    # mail=SendMail()
    # mail.sendmail()



