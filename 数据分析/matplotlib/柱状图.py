# import matplotlib.pyplot as plt
# # 准备数据
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 3, 1, 5]

# # 绘制柱状图
# plt.bar(x, y)

# # 添加标题和坐标轴标签
# plt.title("可视化界面")
# plt.xlabel("x")
# plt.ylabel("y")

# # 显示图表
# plt.show()
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 1, 5]

# 设置中文字符的字体
font = FontProperties(fname=r"C:\Users\86138\Desktop\ppt讲义\Aa半糖奶咖.ttf", size=30)

# 绘制柱状图
plt.bar(x, y)

# 添加标题和坐标轴标签
plt.title("可视化界面", fontproperties=font)
plt.xlabel("x")
plt.ylabel("y")

# 显示图表
plt.show()
