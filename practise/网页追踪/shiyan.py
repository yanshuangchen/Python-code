import requests
from lxml import etree
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def main():
    while True:
        url = "https://jwc.ecust.edu.cn/"  # 目标跟踪网页
        content = requests.get(url).content 
        html = etree.HTML(content)
        title = html.xpath("//td[@class='pan7']/table//td[@align='left']/a/text()")[0]
        new_url = html.xpath("//td[@class='pan7']/table//td[@align='left']/a/@href")[0]
        result_url = "https://jwc.ecust.edu.cn/" + new_url
        # 获取第一篇文章标题并且打印
        print("当前的标题为: %s" % title)
        print("当前的链接为: %s" % result_url)        

        if not os.path.isfile("C:\\Users\\python\\txt_temp.txt"):
            # 判断title_temp.txt文件是否存在，不存在则创建，并写入获取的第一篇文章标题
            with open("C:\\Users\\python\\txt_temp.txt", "w", encoding="utf-8") as f:
                f.write(title)
                print("将当前标题记录在D:\\title_temp.txt中，等待检测")  
        else:
            # title_temp.txt文件存在的话，提取里面标题，和获取的标题对比
            with open("C:\\Users\\python\\txt_temp.txt", "r+", encoding="utf-8") as f:
                old_title = f.read()
                if old_title != title:
                    email(title, result_url)  # 发送qq邮件，并传递标题和链接作为参数
                    f.seek(0)
                    f.truncate()                             
                    print("网站有更新，需通知")
                    f.write(title)
                    # 写入最新的标题内容，方便下一次比对
                    break
                    # 退出循环
                                
                else:
                    # 否则的话，表明网站没有更新                
                    print("网站暂时没有更新\n")
                    break
        time.sleep(5)
        # 检测网页内容时间间隔，单位为秒（s）

def email(title, result_url):
    HOST = "smtp.163.com"
    SUBJECT = "网页更新"
    TO = "669042387@qq.com"
    FROM = "13862810574@163.com"
    text = "您好，请注意新的讯息:<br>%s<br>详情请见链接:<br><a href='%s'>点击此处访问</a>" % (title, result_url)
    msg = MIMEText(text, 'html', 'utf-8')
    msg['From'] = Header(FROM, 'utf-8')
    msg['To'] = Header(TO, 'utf-8')
    msg['Subject'] = Header(SUBJECT, 'utf-8')
    server = smtplib.SMTP()
    server.connect(HOST, 25)
    server.login(FROM, "TEXBTZHUUHIHXGOS")
    server.set_debuglevel(1)
    server.sendmail(FROM, [TO], msg.as_string())
    server.quit()

main()