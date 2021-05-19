# coding=utf-8
# author:yundanni
# create_time:2021/1/6 15:27
import redis

pool = redis.ConnectionPool(host='172.16.96.82', port=6379)
conn = redis.Redis(connection_pool=pool)
conn.set('zhixing_plus_to_sign_up_list', '220111040')
print(conn.get('name'))
#
# if conn.exists('2'):
#     print ('success')
# else:
#     print ('fail')

# conn.set('name', 'fentiao', 3)
# conn.set('age', 10 , 3)
# conn.set('scores', 100 , 3)
# print(conn.get('name'))
# print(conn['name'])
#
#
# # 获取所有的key值
# print(conn.keys())
# print(len(conn.keys()))
#
#
# # 当前redis数据库中数据条数;
# print(conn.dbsize())
#
#
# # 删除指定key-value值
# conn.delete('scores')
# print("正在删除key......")
# print(conn.get('scores'))
#
#
#
# # 将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
# conn.save()
#
#
#
# print("清除前:", conn.keys())
# # 清楚redis里面所有的key-value值
# conn.flushall()
#
# print("清除后:", conn.keys())
