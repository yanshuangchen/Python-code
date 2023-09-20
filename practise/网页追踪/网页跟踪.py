import requests
from lxml import etree
import time
import os
from sendemail import email

while True:
    url = "http://www.yhjbox.com/"   #目标跟踪网页
    content = requests.get(url).content 
    html = etree.HTML(content)
    title = html.xpath("/html/body/section/div[2]/div/article[1]/header/h2/a/@title")[0]
    #获取第一篇文章标题    
    print("当前的标题为:%s"%title)
    #屏幕打印获取的第一篇文章标题

    if not os.path.isfile("E:\\title_temp.txt"):
    #判断title_temp.txt文件是否存在，不存在则创建，并写入获取的第一篇文章标题
        f = open("E:\\title_temp.txt", "w")
        f.write(title)
        print("将当前标题记录在E:\title_temp.txt中，等待检测")  
        f.close()
    else:
    #title_temp.txt文件存在的话，提取里面标题，和获取的标题对比
        with open("E:\\title_temp.txt", "r+") as f:
            old_title = f.read()
            if old_title !=title:
            #如果读取内容和获取的网站第一篇文章标题不一致，则表明网站更新
                email()#发送qq邮件
                f.seek(0)
                f.truncate()                             
                print("网站有更新，需通知")
                f.write(title)
                #写入最新的标题内容，方便下一次比对
                break
                #退出循环                
            else:
            #否则的话，表明网站没有更新                
                print("网站暂时没有更新\n")
                break
    time.sleep(5)
    #检测网页内容时间间隔，单位为秒（s）