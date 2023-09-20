import sqlite3
conn=sqlite3.connect("D:\浏览器下载\school.db")
while True:
    dept=input("请输入查询学院代号：（输入0退\出程序）\n")
    if dept=='0':
        break
    SQL="SELECT *  from student where DeptID='%s'" %dept
    cur=conn.execute(SQL)
    list1=cur.fetchall()
    print("{0:{3}<6}{1:{3}<10}{2:{3}<5}".format('学号','姓名', \
      '学院',chr(12288)))
    for rec in list1:
        print('{0:{3}<10}{1:{3}<10}{2:{3}<10}'.format(rec[0]  \
           ,rec[1],rec[6],chr(12288)))
conn.close()