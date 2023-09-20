import pandas as pd
profitStatement = pd.read_html('http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_ProfitSt\
atement/stockid/600000/ctrl/part/displaytype/4.phtml')
print(profitStatement)