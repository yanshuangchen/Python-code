import numpy as np
import pandas as pd   
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.read_excel(r"C:\Users\86138\Desktop\code\无监督学习-学生成绩聚类\Stu_score.xls","Sheet1",index_col=0)
X = data.loc[:,["数学", "总分"]] #读出数据

estimator = KMeans(n_clusters=3,n_init="auto")#模型初始化


estimator.fit(X) #模型学习
label_pred = estimator.labels_ #获取聚类标签
#print(label_pred)
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]

plt.rcParams['font.sans-serif'] = ['Simhei']

plt.scatter(x0['数学'], x0['总分'], c = "green", marker='^', label='B')
plt.scatter(x1['数学'], x1['总分'], c = "blue", marker='*', label='C')
plt.scatter(x2['数学'], x2['总分'], c = "red", marker='o', label='A')
plt.xlabel('数学')
plt.ylabel('总分')
plt.legend(loc=2)
plt.show()

'''
FutureWarning: The default value of `n_init` will change from 10 to ‘auto‘ in 1.4.
由于sklearn的版本问题，可能会出现如上警告，添加n_init="auto"即可
'''
