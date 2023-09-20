import time
import webbrowser
import os
 
# 浏览器运行目录
edgePath = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
 
# 注册浏览器
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))
 
# 获取浏览器并打开指定地址
webbrowser.get('edge').open('https://www.bilibili.com/v/life/daily/?spm_id_from=333.5.b_6c6966655f6461696c79.2#/', new=1, autoraise=True)
 
# 睡眠5秒
time.sleep(5)
 
# 关闭chrome浏览器
os.system('taskkill /F /IM edge.exe')

