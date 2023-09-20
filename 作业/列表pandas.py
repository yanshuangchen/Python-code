import pandas as pd

# 指定文件编码方式和分隔符，不指定列名（当有列名时，header=0）
df = pd.read_csv(r"C:\Users\86138\Desktop\上证指数.txt", encoding='UTF-8', sep=',', header=0)
max_value = df['收盘价'].max()
#能够计算出某行最大的数

#计算出某列最大的数在哪一行
max_index = df['收盘价'].idxmax()

# df.loc[row_label, column_label]
#查询某行某列数据
print("%s上证指数收盘价最高点记录为%.2f"%(df.loc[max_index,"日期"],max_value))
