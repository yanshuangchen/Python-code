import calendar
import pyttsx3
engine = pyttsx3.init()
while True:
    a=("查询Y(y)/取消N(n): ")
    engine.say(a)
    engine.runAndWait()
    m=input("查询Y(y)/取消N(n): ")
   
    if m=="Y" or m=="y":
        x=int(input("请输入年: "))
        y=int(input("请输入月: "))
        z=int(input("请输入日: "))
# 以 yyyy-mm-dd 格式的字符串为参数，计算星期几,周一到周六分别代表0-6
        weekday = calendar.weekday(x, y, z)
        zhuanhuan = {'0': '星期一', '1': '星期二', '2': '星期三','3':'星期四','4':'星期五','5':'星期六','6':'星期日'} 
#str将数值转换为字符串
        zhi=zhuanhuan[str(weekday)]
        print(zhi)
    elif m=="N" or m=="n":
        break
