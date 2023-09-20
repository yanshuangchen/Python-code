import pandas as pd
Balance = pd.DataFrame([['1001','库存现金',5215,1010],
['1002','银行存款',1595236,254582],
['1012','其他货币资金',160000,50000]],
columns=['科目编码','会计科目','期初余额','本期发生额'],
index=[1,2,3])
Balance .drop(3)
print(Balance)
