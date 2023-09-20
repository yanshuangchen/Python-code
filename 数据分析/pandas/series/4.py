import pandas as pd
score = pd.Series([98,86,75],index=['语文','数学','英语'])
print(score.reindex(['数学','语文','英语','物理']))#不能新建原索引中没有的索引
#重建索引