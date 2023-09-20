from pdf2docx import parse

# 指定输入的PDF文件路径和输出的Word文件路径
input_file = r"C:\Users\86138\Desktop\3_22级计算机大类和智机试验班拔尖计划选拔使用 成绩和排名情况公布.pdf"
output_file = r"C:\Users\86138\Desktop\3_22级计算机大类和智机试验班拔尖计划选拔使用 成绩和排名情况公布.docx"

# 执行转换
parse(input_file, output_file)
