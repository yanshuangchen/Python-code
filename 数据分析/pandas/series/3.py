import pandas as pd
score = pd.Series([98,86,75],index=['语文','数学','英语'])
print(score)
score['物理']=100 # 增加“物理”分数
print(score)

score1=pd.Series([100,99],index=['政治','历史'])
print(score.append(score1))#通过append加入新的元素,只能使用一次，并不能刷新

print(score.drop("物理"))#删除一行数据

date=pd.Series(range(101,150))
print(date.head())#默认查看前五行数据
print(date.tail(3))#查看后几行的数据

