import matplotlib.pyplot as plt
import numpy as np

# 准备数据
labels = ['A', 'B', 'C', 'D', 'E'] # 类别标签
men_means = [20, 35, 30, 35, 27]   # 男性平均值
women_means = [25, 32, 34, 20, 25] # 女性平均值

x = np.arange(len(labels))  # x轴坐标

width = 0.35  # 条形图宽度

# 绘制条形图
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# 设置图例和标签
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()