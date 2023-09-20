import pandas as pd

df = pd.read_csv(r"C:\Users\86138\Desktop\score.csv", encoding='GB2312', sep=',', header=0)
my_list = df['姓名'].tolist()
yuwen = df['语文'].tolist()
shuxue = df['数学'].tolist()
yingyu = df['英语'].tolist()