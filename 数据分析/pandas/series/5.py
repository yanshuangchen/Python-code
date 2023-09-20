import pandas as pd
score = pd.Series([98,86,75],index=['语文','数学','英语'])
print(score.reindex(['数学','语文','英语','物理'],fill_value=0)) # 设置缺失的值
score["数学"]=99
#修改某一索引的值
print(score)
