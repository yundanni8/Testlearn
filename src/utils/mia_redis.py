import os

import redis

from src.test.comm.logger_handler import LoggerHandler
from src.utils.yaml_read import YamlHandle
BASE_PATH =(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
casepath = os.path.join(BASE_PATH, 'src\\test\\case\\interface')
result=os.path.join(BASE_PATH, 'report\\')
log_name='redis'
log_file=os.path.join(LOG_PATH, 'zhixing_redis_file\\')
REDIS_FILE=os.path.join(BASE_PATH, r'config\redis_config.yaml')
mylogger = LoggerHandler(log_file,log_name).get_log()
redis_config=YamlHandle(REDIS_FILE).get_yaml_data
redis_host=redis_config.get("host")

class RedisOp:
    def __init__(self,host):
        try:
            self.pool = redis.ConnectionPool(host=host)
            self.r = redis.Redis(connection_pool=self.pool)
            print ("redis连接成功！")
        except Exception as e:
            print("redis连接失败！")

    def get_value(self,key):
            self.value=self.r.get(key)
            print ("key是{} ,value 是 {} ".format(key,self.value))

    def delete_value(self,key):
        if self.r.get(key)!=None:
            self.value=self.r.delete(key)
        else:
            print ("key 不存在")

# a=RedisOp(redis_host).get_value("pro_order_count_220111244")
# a=RedisOp(redis_host).delete_value("pro_order_count_220111244")



