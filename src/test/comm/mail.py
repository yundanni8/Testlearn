# coding=utf-8
# author:yundanni
# create_time:2020/11/9 18:11
# encoding: utf-8
import os,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.test.comm.logger_handler import LoggerHandler
from src.utils.file_read import YamlHandle
BASE_PATH =os.path.split(os.path.split((os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]))[0])[0] #将path分割成目录和文件名二元组返回  D:\测试\zhixing_test
print (BASE_PATH)
LOG_PATH = os.path.join(BASE_PATH, 'log\\')
print (LOG_PATH)
casepath = os.path.join(BASE_PATH, 'src\\test\\case\\interface')
result=os.path.join(BASE_PATH, 'report\\')
# print (BASE_PATH,LOG_PATH,casepath,result)
log_name='mail'
log_file=os.path.join(LOG_PATH, 'zhixing_mail_file\\')
# print (log_file)
MAIL_FILE=os.path.join(BASE_PATH, r'config\mail_config.yaml')
mylogger = LoggerHandler(log_file,log_name).get_log()
data=YamlHandle(MAIL_FILE).get_yaml_data




class SendMail():
    global subject,mail_to_i,mail_from_i,mail_to_text
    subject=data["subject"]
    mail_to_i=data["mail_to_i"]
    mail_from_i=data["mail_from_i"]
    mail_to_text=data["mail_to_text"]
    def sendmail(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        tdresult = result + day
        # 读取文件
        filename = tdresult + "\\"
        # print filename
        try:
            lists = os.listdir(filename)
            lists.sort(
                key=lambda fn: os.path.getmtime(filename + "\\" + fn) if not os.path.isdir(filename + "\\" + fn) else 0)
            print(u'最新测试生成的报告:' + lists[-1])
            file_new = os.path.join(filename, lists[-1])
            mylogger.info(u'最新文件路径为是：%s' % (file_new))
            # 发送邮件
            # 构建邮件
            msg = MIMEMultipart()
            txt = '<html><body>自动化测试报告！ </br>测试组：贠丹妮 </br></body></html>'
            att1 = MIMEText(txt, 'html', 'utf-8')
            msg.attach(att1)
            # 构建附件
            att2 = MIMEText(open(file_new, "rb").read(), "base64", "utf-8")
            att2["Content-Type"] = 'application/octet-stream'
            att2[
                "Content-Disposition"] = 'attachment; filename="interface_test_report.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            msg.attach(att2)
            # 构建邮件发送区域文字
            msg['to'] = mail_to_text
            msg['from'] = mail_from_i
            msg['Subject'] = subject
            msg['date'] = time.strftime('%Y/%m/%d %H:%M:%S')
            # 设置发送地址
            smtp = smtplib.SMTP()
            mail_from = mail_from_i
            mail_to = mail_to_i
            # 连接服务器
            try:
                smtp.connect('smtp.exmail.qq.com')
                smtp.login('yundanni@mia.com', '187927Ydn')
                smtp.sendmail(mail_from, mail_to, msg.as_string())
                smtp.quit()
                mylogger.info(u'邮件发送成功！')
            except:
                mylogger.info(u'邮件发送失败！')
        except:
            mylogger.info(u'没有任何文件！')


if __name__=='__main__':
    mail=SendMail()
    mail.sendmail()







