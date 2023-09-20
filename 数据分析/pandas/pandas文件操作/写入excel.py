import pandas as pd
data=[['张三',100,89,94],
['李四',88,75,96],
['王五',95,86,94]]
df = pd.DataFrame(data,columns=['姓名','语文','数学','英语'],index=[1,2,3])
# 指定目录和文件名，输出结果。
# 生成文件“成绩表1.xlsx”
df.to_excel('成绩表1.xlsx')
#写的时候可以加上r代表路径
with pd.ExcelWriter('成绩表1.xlsx', mode = 'a', engine = 'openpyxl') as writer:
    df.to_excel(writer, sheet_name = '语文成绩表', index = False,columns=['姓名','语文'] )
    df.to_excel(writer, sheet_name = '数学成绩表', index = False,columns=['姓名','数学'] )
    df.to_excel(writer, sheet_name = '英语成绩表', index = False,columns=['姓名','英语'] )

