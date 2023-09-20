import time
import pyperclip
import win32api
import win32con
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def getHTMLtext(url):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        }  # Browser headers
        r = requests.get(url, headers=headers, timeout=30)  # Send a GET request
        r.raise_for_status()  # Check if the request was successful, otherwise raise an exception
        r.encoding = r.apparent_encoding  # Set the encoding
        return r.text
    except:
        return ""

def parseHTML(news, html):
    soup = BeautifulSoup(html, "html.parser")  # Create a BeautifulSoup object

    # Find all <tr> elements with class "ewb-trade-tr"
    tr_elements = soup.find_all('tr', class_='ewb-trade-tr')

    for tr in tr_elements:
        td_elements = tr.find_all('td')  # Find all <td> elements within the <tr>

        # Extract data from the <td> elements
        td1_data = td_elements[0].text.strip()  # Extract the first <td> value
        td2_data = td_elements[1].text.strip()  # Extract the second <td> value
        href = "http://ggzyjy.nantong.gov.cn/" + td_elements[2].a['href']  # Extract the href attribute from the <a> within the third <td>
        title = td_elements[2].a.string.strip()  # Extract the string within the <a> within the third <td> and strip leading/trailing whitespace
        td4_data = td_elements[3].text.strip()  # Extract the fourth <td> value
        date = td_elements[4].text.strip()  # Extract the fifth <td> value     
        news.append([td1_data, td2_data, href, title, td4_data, date])

# Get the HTML content
url = "http://ggzyjy.nantong.gov.cn/jyxx/003002/tradeInfo.html"
html = getHTMLtext(url)

# Parse the HTML and extract the desired information
news = []
parseHTML(news, html)
# print(news)
# Filter the news based on specific keywords
selected_news = []

keywords = ["公安", "派出所", "执法", "警察"]

for row in news:
    for keyword in keywords:
        if keyword in row[3]:  # Check if the keyword is present in the project name
            selected_news.append(row)
            break

# Convert the selected news to a DataFrame
df = pd.DataFrame(selected_news, columns=["项目名称", "发布时间"])

# # Convert the DataFrame to a formatted string and remove the header
message = df.to_string(header=False, index=False)

# Add line breaks after each element
message = message.replace('\n', '\n\n')
message = "今日新闻\n" + message


print(message)
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # Get current time
    sent_time = '11:50:20'  # Set the sending time
    if time_now == sent_time:  # If the current time matches the sending time, execute the following code
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
        pyperclip.copy('文件传输助手')  # 联系人昵称
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
        pyperclip.copy('文件传输助手先生你好，\n本消息是由华东理工大学季爽研发的自动爬取网页并定时发送微信系统1.0自动发送，目前系统仍在测试调整中')  # 聊天的内容
        spam = pyperclip.paste()
        win32api.keybd_event(17, 0, 0, 0)  # Ctrl
        win32api.keybd_event(86, 0, 0, 0)  # 86→V
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)  # 确保程序只执行一次，防止重复执行

        # Paste the message and press Enter to send
        message = df.to_string(header=False, index=False)
        message = message.replace('\n', '\n\n')
        message="海门区近日招标情况一览\n"+message
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
