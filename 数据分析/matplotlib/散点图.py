import matplotlib.pyplot as plt
# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 1, 5]

# 绘制散点图
plt.scatter(x, y)

# 添加标题和坐标轴标签
plt.title("Scatter Chart")
plt.xlabel("x")
plt.ylabel("y")

# 显示图表
plt.show()
