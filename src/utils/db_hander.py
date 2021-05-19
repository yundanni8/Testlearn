# coding=utf-8
# author:yundanni
# create_time:2020/11/11 11:40
import os
import pymysql
from src.utils.yaml_read import  YamlHandle
case_name="数据库操作封装"
CURRENT_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]#将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
BASE_PATH=os.path.split(CURRENT_PATH)[0]
print ("当前文件根目录是"+BASE_PATH)
DB_FILE=os.path.join(BASE_PATH, r'config\db_config.yaml')
print ("数据库配置文件地址是"+DB_FILE)
# LOG_PATH = os.path.join(BASE_PATH, 'log\\')
# log_name="db_log"
# log_file=os.path.join(LOG_PATH, 'zhixing_log_file\\')
# mylogger = LoggerHandler(log_file,log_name).get_log()

data=YamlHandle(DB_FILE).get_yaml_data


class DbOper():
    def __init__(self,db_name):
        # 连接数据库
        try:
            self.db = pymysql.connect(
                host=data['host'],
                port=data['port'],
                user= data['username'],
                passwd=data['password'],
                db=db_name,
                charset="utf8" ,# "utf-8"会报错
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.db.cursor()

        except Exception as e:
            print('mysql connect failed , please check')
            raise e

    def select(self,table_name,table_data):
        if len(table_data) > 0:
            keys=[]
            value=[]
            for i in table_data.keys():
                keys.append(i)
                value.append(table_data[i])
            real_sql = ""
            for i in range(len(keys)):
                if i==0:
                    real_sql="select * from %s where %s= '%s' " %(table_name,keys[0],value[0])
                else:
                    real_sql +="AND %s = '%s'" % (keys[i], value[i])
                self.cursor.execute(real_sql)
                rs = self.cursor.fetchall()
            # print (type(rs))
            return (rs)

            # return (rs)


    def insert(self,table_name,table_data):
        key = ','.join(table_data.keys())
        # value = ','.join(table_data.values())#正常情况下
        value=', '.join('"' + item + '"' for item in table_data.values())#user表字段必须拼接""
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        self.cursor.execute(real_sql)
        self.db.commit()







# db = DbOper("mia_bi_plus").select("APP_MIA_PLUS_SAGE_REWARD",{"plus_sage_reward_id":"1390"})
# db = DbOper("mia_test2").insert("user_id_card",{"user_id":"220108018","id_card_id":"1","status":"1"})



# if __name__ == '__main__':
#
#     # sql = "SELECT * FROM df_goods"
#     # results = db.select(sql)
#     # db.close()
#     # print(results)