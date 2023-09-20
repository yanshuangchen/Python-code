import sqlite3
# 连接数据库
conn =sqlite3.connect(r"D:\浏览器下载\school.db")
while True:
    id=input('请输入新生学号：（输入0退出程序）\n')
    if id=='0':
        break
    name=input('请输入新生姓名：\n')
    gender=input('请输入新生性别：\n')
    # 格式化构建SQL字符串
    SQL='''insert into student
       (Sno,Sname,Ssex)
       values ('%s','%s','%s')''' %(id,name,gender)
    conn.execute(SQL)
    conn.commit()
conn.close()