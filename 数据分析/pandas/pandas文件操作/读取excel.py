import pandas as pd
a=pd.read_excel(r"C:\Users\86138\Desktop\数据.xlsx", #xlsx竟然要装一个库，笑死
            sheet_name=0, 
            #可以输入0或者表名
            header=0,
            names=None, 
            index_col=0,#使用学号作为索引
            usecols=None, 
            converters=None)#强制规定列的数据类型
print(a)
