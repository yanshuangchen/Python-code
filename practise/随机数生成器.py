import numpy as np
import pandas as pd

# 设置随机种子，以保证结果可复现
np.random.seed(0)

# 生成随机数据
data = np.random.randint(0, 100, size=(5, 3))  # 生成一个5行3列的随机整数数组

# 对每一列的数据进行限制范围
min_values = [10, 20, 30]
max_values = [50, 60, 70]
data = np.clip(data, min_values, max_values)  # 将数据限制在[min_values, max_values]范围内

# 创建数据表格
df = pd.DataFrame(data, columns=['A', 'B', 'C'])  # 使用随机数组创建数据表格，指定列名

# 打印数据表格
print(df)