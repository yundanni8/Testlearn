# coding=utf-8
# author:yundanni
# create_time:2020/11/10 17:50
import json
import unittest
import requests
from src.test.comm.logger_handler import LoggerHandler
import os
from src.test.comm.form_data import Post_data
from src.test.comm.request_method import method
import warnings
from src.utils.send_ding import SendMessage
requests.packages.urllib3.disable_warnings()

BASE_PATH =os.path.split(os.path.split(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0])[0])[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
log_name='live_detail'
log_file=os.path.join(LOG_PATH, 'zhixing_log_file\\')
print ("log_path"+LOG_PATH,"log_file"+log_file)
mylogger = LoggerHandler(log_file,log_name).get_log()
case_name="live_detail"


class Testlive(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        #定义接口请求url和post data
        self.post_url=Post_data().post_url(case_name)
        self.post_data=Post_data().post_data(case_name)

    def test_live(self):
        mylogger.info("测试用例%s开始执行" % case_name)
        self.res = method().send_post(self.post_url, self.post_data)
        self.jres=json.dumps(self.res, sort_keys=True, indent=4, separators=(',', ':'))
        # print (self.jres)
        # self.assertEqual(self.res.get('msg'),'success',msg='测试失败')
        self.assertEqual(self.res.get('msg'),'success',SendMessage("%s 接口测试失败,返回msg 是 %s" %(case_name,self.res.get('msg'))))
        mylogger.info("响应内容为%s" % self.jres)
        print(u"*" * 80)

    def tearDown(self) :
        pass
if __name__=='__main__':
    unittest.main()
# Testlive().test_live()
