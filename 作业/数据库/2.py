import sqlite3
# 选择绝对地址
conn = sqlite3.connect("D:\浏览器下载\school.db")
SQL = '''
INSERT
INTO Student(Sno,Sname,Ssex,Sbirth,age)
VALUES('22013310','季爽','男','2002/05/04',20)
'''
conn.execute(SQL)
conn.commit()
conn.close