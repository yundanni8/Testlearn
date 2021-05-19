# coding=utf-8
# author:yundanni
# create_time:2020/11/11 14:06

import os
import yaml
import sys
BASE_PATH =os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
print (BASE_PATH)
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
sys.path.append(BASE_PATH)
sys.path.append(UTILS_PATH)
DATA_PATH = os.path.join(BASE_PATH, r'config')
MAIL_FILE = os.path.join(BASE_PATH, r'config\redis_config.yaml')
db_config = {
        'host':'172.16.104.185'
            }






# 写入到yaml文件
# if DATA_FILE exist:
#
with open(MAIL_FILE, "w", encoding="utf-8") as f:
    # yaml.dump(desired_caps, f)
    yaml.dump(db_config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)