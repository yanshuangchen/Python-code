import pandas as pd

# 创建一个DataFrame对象
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})
print(df)
# 计算C列的最大值
max_value = df['C'].max()

# 输出C列的最大值
print(max_value)