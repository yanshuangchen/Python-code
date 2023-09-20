import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning) # 忽略所有警告
data=pd.read_csv('info.csv',encoding='gb2312')
#print(data)

model= KNeighborsClassifier()
model.fit(data[['性别','身高','体重']].values, data['类型'].values)
height=int(input("请输入您的身高："))
weight=int(input("请输入您的体重："))
print('预测类型为：',model.predict([[1,height,weight]]))

