import pandas as pd
a=pd.read_excel(r"C:\Users\86138\Desktop\数据.xlsx", #xlsx竟然要装一个库，笑死
            sheet_name=0, 
            #可以输入0或者表名
            header=0,
            names=None, 
            index_col=None,#使用学号作为索引或者使用空值
            usecols=None, 
            converters=None)#强制规定列的数据类型
#从1开始编号
a = a.reset_index(drop=True)
a.index += 1

# print(a)
# print(a["姓名"])
#print(a[["姓名","出生年月"]])#打多行数据竟然要打两个括号！

#读取连续行数据
# print(a[0:20])#从零开始，半包区间


#查询数据
print(a[(a["姓名"]=="孙明杰")])


#选取行
print(a.loc[1])

#选取特定行与列
print(a.loc[[1],["中学名称"]])

#选取连续行与列
print(a.loc[1:20,"学号":"中学名称"])




