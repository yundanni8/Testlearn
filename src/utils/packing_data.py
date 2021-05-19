# coding=utf-8
# author:yundanni
# create_time:2020/11/24 10:41
from util.db_handler import DbOper
class PackData():
    def __init__(self):
        self.db=DbOper("mia_bi_plus")
        self.data=self.db.select("APP_MIA_PLUS_SAGE_REWARD",{"plus_sage_reward_id":"1390"})

    def to_list(self,key_data):
        #适用于select语句返回的数据处理
        """
        [{'plus_id_0': 220109411},
        {'plus_id_1': 220107664},
        :return:
        """
        data=self.data
        new_data2=[]
        for i in range (len(data)):
            """
            #必须在for循环内声明字典，要不然得出的就是下面这种了
            [{'plus_id_0': 220109411,'plus_id_1': 220107664}]
            """
            new_dict = {}
            for i in range(len(key_data)):
                new_dict[key_data[i]]=data[i][key_data[i]]
                new_data2.append(new_dict)
        return(new_data2)


a=["plus_id","sale_amt"]
b=PackData().to_list(a)
print (b[0]["plus_id"])