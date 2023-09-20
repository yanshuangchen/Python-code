import datetime
f1= open(r"C:\Users\86138\Desktop\1.txt")
f2= open(r"字幕.srt",'w',encoding='utf-8')
#返回一个文件对象
line=f1.readline()#调用文件的readline（）方法
no=1
start_time = datetime.datetime.strptime('00:00:00','%H:%M:%S')
end_time = datetime.datetime.strptime('00:00:00','%H:%M:%S')
while line:
    line= f1.readline()
    start_time=start_time+datetime.timedelta(seconds=3)
    end_time=start_time+ datetime.timedelta(seconds=3)
    str_start_time = datetime.datetime.strftime(start_time,'%H:%M:%S')
    str_end_time  =datetime.datetime.strftime(end_time,'%H:%M:%S')
    f2.write(str(no)+'\n')
    f2.write(str_start_time+",433"+"-->"+str_end_time+",433"+'\n')
    f2.write(line+'\n')
    no=no+1
f1.close()
f2.close()
