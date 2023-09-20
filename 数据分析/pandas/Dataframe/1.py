import pandas as pd
score=pd.DataFrame([['1001','库存现金',5215],
            ['1002','银行存款',1595236],
            ['1012','其他货币资金',160000]],
            columns=['科目编码','会计科目','期初余额']
            ,index=[1,2,3])
#data参数,columns列索引，index行索引
print(score)
#通过列表创建数据
score['期末余额']=[6225,1849818,210000]
print(score)
#增加新的列数据数据
score.loc[4] = ['1014','应收账款',350000,140000] 
print(score)
#调用drop删除数据(删除行)
print(score.drop(3))
#用del删除列
del score["会计科目"]
print(score)
#del(score)删除列表

print(score.head(2))
#查看开头或者结尾几组数据head或者tail
print(score.T)
#转置，后面加上一个.T