import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.text import MIMEText     
from email.header import Header  
import time
import schedule

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

        # Check if the location is "海门区"
        if td4_data == "海门区":
            # Append the extracted data to the news list
            news.append([td1_data, td2_data, href, title, td4_data, date])

# Usage example

url = "http://ggzyjy.nantong.gov.cn/jyxx/003002/tradeInfo.html"
html = getHTMLtext(url)
news = []
parseHTML(news, html)
for item in news:
    print(item)

# selected_columns = [1,3,4,5]  # Assuming you want to select columns '序号', '链接', and '项目名称'
# selected_news = [[row[i] for i in selected_columns] for row in news]
# df = pd.DataFrame(selected_news, columns=["交易类别", "项目名称", "所在地区", "发布时间"])
# df.to_excel("trade_info.xlsx", index=False)
