import time
import pyperclip
import win32api
import win32con
import os
 
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 获取当前时间
    sent_time = '10:35:00'  # 发送时间
    if time_now == sent_time:  # 当前时间等于发送时间则执行以下程序
        def open_app(app_dir):
            os.startfile(app_dir)
 
        # 打开微信
        if __name__ == "__main__":
            app_dir = r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"  # 此处为微信的绝对路径
            open_app(app_dir)
            time.sleep(1)  
        
        #进入微信，模拟按键Ctrl+F
        win32api.keybd_event(17, 0, 0, 0)  # Ctrl
        win32api.keybd_event(70, 0, 0, 0)  # F
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
 
        # 复制需要查找的人，按回车，进入聊天输入框
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
        pyperclip.copy('下面内容由程序自动进行')  # 聊天的内容
        spam = pyperclip.paste()
        win32api.keybd_event(17, 0, 0, 0)  # Ctrl
        win32api.keybd_event(86, 0, 0, 0)  # 86→V
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)  # 确保程序只执行一次，防止重复执行
 
        pyperclip.copy('我也不知道吃什么')  # 聊天的内容
        spam = pyperclip.paste()
        win32api.keybd_event(17, 0, 0, 0)  # Ctrl
        win32api.keybd_event(86, 0, 0, 0)  # 86→V
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(3)
        
        exit() # 退出程序
 
 
 
 