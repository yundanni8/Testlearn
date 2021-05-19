# coding=utf-8
# author:yundanni
# create_time:2021/1/6 15:57
import paramiko


class Monitor(object):
    def __init__(self, server_ip, user, pwd):
        """ 初始化ssh客户端 """
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client = client
            print('------------开始连接服务器(%s)-----------' % server_ip)
            self.client.connect(server_ip, 22, username=user, password=pwd, timeout=4)
            print('------------认证成功!.....-----------')
        except Exception:
            print(f'连接远程linux服务器(ip:{server_ip})发生异常!请检查用户名和密码是否正确!')

    def link_server(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        content = stdout.read().decode('gbk')
        print(content)
        """连接服务器发送命令"""
        # try:
        #     stdin, stdout, stderr = self.client.exec_command(cmd)
        #     content = stdout.read().decode('gbk')
        #     print (content)
        # except Exception as e:
        #     print('link_server-->返回命令发生异常,内容:', e)
        # finally:
        #     self.client.close()
a=Monitor('172.16.96.217','root','1234qwer')
a.link_server("/opt/php/bin/php /opt/webroot/plus/current/Server/htdocs/www/bin/sh.php /cron/cron_personal_payment/create_personal_payment_by_table_id /2021-01")