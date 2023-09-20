import sqlite3
conn = sqlite3.connect('D:/test.db')
# 新建列表
conn.execute('''CREATE TABLE base
       (学号    TEXT(10)    PRIMARY KEY     NOT NULL,
        姓名    TEXT(10)    NOT NULL,
        性别    TEXT(1)      NOT NULL,
        专业    TEXT(6),
        生源    TEXT(6),
        身高    INTEGER,
        电话    TEXT(6) );''')