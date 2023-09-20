# 注意连接好网络，登录好微信
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pyperclip
import win32api
import win32con
import os

def getHTMLtext(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        }  # 浏览器请求头
        r = requests.get(url, headers=headers, timeout=30)  # 获取连接
        r.raise_for_status()  # 测试连接是否成功，若失败则报异常
        r.encoding = r.apparent_encoding  # 解析编码
        return r.text
    except:
        return ""

def parseHTML(news, html):
    soup = BeautifulSoup(html, "html.parser")  # Create a BeautifulSoup object
    tr_elements = soup.find_all('tr', class_='ewb-trade-tr')

    for tr in tr_elements:
        td_elements = tr.find_all('td')
        td1_data = td_elements[0].text.strip()
        td2_data = td_elements[1].text.strip()
        href = "http://ggzyjy.nantong.gov.cn/" + td_elements[2].a['href']
        title = td_elements[2].a.string.strip()
        td4_data = td_elements[3].text.strip()
        date = td_elements[4].text.strip()
        news.append([td1_data, td2_data, href, title, td4_data, date])

def processURLs(urls):
    all_news = []

    for url in urls:
        html = getHTMLtext(url)
        news = []
        parseHTML(news, html)
        all_news.extend(news)

    selected_columns = [3, 4, 5]
    selected_news = [[row[i] for i in selected_columns] for row in all_news]
    
    resultnews = []
    keywords = ["公安", "派出所", "执法", "警察","法院","政府"]

    for row in selected_news:
        for keyword in keywords:
            if keyword in row[0]:  # Check if the keyword is present in the project name
                resultnews.append(row)
                break

    df = pd.DataFrame(resultnews, columns=["项目名称", "所在地区", "发布时间"])
    message = df.to_string(header=False, index=False)
    message = message.replace('\n', '\n\n')
    message = "今日新闻\n" + message
    print(message)
    return message

# 示例URL列表
urls = ["http://ggzyjy.nantong.gov.cn/jyxx/003002/tradeInfo.html"]

for i in range(2, 7):
    urls.append(f"http://ggzyjy.nantong.gov.cn/jyxx/003002/{i}.html")

message = processURLs(urls)


# while True:
#     time_now = time.strftime("%H:%M:%S", time.localtime())  # Get current time
#     sent_time = ['14:54:30', '16:08:00', '16:21:00']
#     if time_now in sent_time:  # If the current time matches the sending time, execute the following code
def open_app(app_dir):
    os.startfile(app_dir)

# Open WeChat
if __name__ == "__main__":
    app_dir = r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"  # Replace with the absolute path of WeChat on your system
    open_app(app_dir)
    time.sleep(1)

# Enter WeChat and simulate pressing Ctrl+F
win32api.keybd_event(17, 0, 0, 0)  # Ctrl
win32api.keybd_event(70, 0, 0, 0)  # F
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)

# Copy the contact name, press Enter to enter the chat input box
pyperclip.copy('吴群')  # 联系人昵称
spam = pyperclip.paste()
win32api.keybd_event(17, 0, 0, 0)  # Ctrl
win32api.keybd_event(86, 0, 0, 0)  # 86→V;
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
win32api.keybd_event(13, 0, 0, 0)  # 13→Enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)

#聊天输入框复制聊天内容，然后按回车发送消息
pyperclip.copy('妈妈好，好妈妈，你好，\n本消息是由华东理工大学季爽研发的自动爬取网页并定时发送微信系统1.0自动发送，目前系统仍在测试调整中')  # 聊天的内容
spam = pyperclip.paste()
win32api.keybd_event(17, 0, 0, 0)  # Ctrl
win32api.keybd_event(86, 0, 0, 0)  # 86→V
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)  # 确保程序只执行一次，防止重复执行

# Paste the message and press Enter to send
pyperclip.copy(message)
spam = pyperclip.paste()
win32api.keybd_event(17, 0, 0, 0)  # Ctrl
win32api.keybd_event(86, 0, 0, 0)  # V
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
win32api.keybd_event(13, 0, 0, 0)  # Enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(3)
exit() # 退出程序


