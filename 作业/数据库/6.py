import sqlite3
conn = sqlite3.connect(r"D:\浏览器下载\school.db")
# 遍历打印数据表
SQL = '''SELECT *
         FROM Student'''
res = conn.execute(SQL)
print("查询结果")
for item in res.fetchall():
    print(item)
conn.commit()
conn.close()