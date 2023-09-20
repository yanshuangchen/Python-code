import pandas as pd
import os
#下面这句是包含excel文件的位置
dir = r"C:\Users\86138\Desktop\试验"
filenames = os.listdir(dir)
index = 0
dfs = []
for name in filenames:
    print(index)
#sheet_name=3指的是excel中第4个sheet页，如果只有一个sheet，改成0即可，也可改成sheet页的名字
    dfs.append(pd.read_excel(os.path.join(dir,name),sheet_name=0))
    index += 1 #为了查看合并到第几个表格了
df = pd.concat(dfs)
#列1，列2，列3是你要查找的列名，如果要合并全表就省略这步
# df=df[['列1','列2','列3']]
df=df.dropna(axis=0, how='all')
df=pd.DataFrame(df)
#保存到桌面的文件名
df.to_excel(r'C:\Users\86138\Desktop\合并.xlsx')
df

