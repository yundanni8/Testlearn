# coding=utf-8
# author:yundanni
# create_time:2020/11/9 14:18
import warnings

import requests
from src.utils.file_read import YamlHandle
import os
import sys
requests.packages.urllib3.disable_warnings()
from src.utils.rsa import Decript
BASE_PATH =os.path.split(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0])[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
# print ('base_path= '+BASE_PATH)
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'data')
DATA_FILE = os.path.join(BASE_PATH, r'data\zhixing_data.yaml')
from src.utils.send_ding import SendMessage


class method():
    # warnings.simplefilter('ignore', ResourceWarning)
    global s
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()

    def send_get(self, url, data):
        requests.packages.urllib3.disable_warnings()
        res = s.get(url=url, data=data,verify=False).json()
        # print (type(res))
        return res

    def send_post(self, url, data):
        requests.packages.urllib3.disable_warnings()
        res = s.post(url=url, data=data,verify=False).json()
        # SendMessage(res)
        return res

    def run_main(self, url, method,data=None):
        requests.packages.urllib3.disable_warnings()
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url,data)
        return res
#post上传文件
    def run_file(self,url,files,data):
        res=None
        res=s.post(url=url,files=files,data=data).json()
        return res
if __name__ == '__main__':
    host=YamlHandle(DATA_FILE).get_value('host')
    login_url=YamlHandle(DATA_FILE).get_value('api_path').get('Params')
    url=host+login_url
    data=None
    print (host+login_url)
    a=method()
    a.run_main(url,'GET')