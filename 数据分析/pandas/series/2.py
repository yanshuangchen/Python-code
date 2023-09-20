import pandas as pd
a = pd.Series([13,26,39])
print(a)#不填写索引列参数,数据列与索引列
print(a[2])#通过索引确定数据

b = pd.Series([1000,2000,3000],index=['库存现金','银行库存','其他货币资金'])
print(b)
print(b["库存现金"])#通过标签索引读取数据
print(b["银行库存":"其他货币资金"])#通过标签索引输出区间数据
print(b[1:2])#不包含末端数据

print(pd.Series(range(1,1000,200)))