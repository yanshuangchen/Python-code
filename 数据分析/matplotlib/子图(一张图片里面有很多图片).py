import matplotlib.pyplot as plt
import numpy as np

# 创建一个 2x2 的子图
fig, axs = plt.subplots(2, 2)

# 在第一个子图中绘制正弦函数
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Sin(x)')

# 在第二个子图中绘制余弦函数
y = np.cos(x)
axs[0, 1].plot(x, y)
axs[0, 1].set_title('Cos(x)')

# 在第三个子图中绘制正切函数
y = np.tan(x)
axs[1, 0].plot(x, y)
axs[1, 0].set_title('Tan(x)')

# 在第四个子图中绘制正切函数的导数
y = 1 / np.cos(x)**2
axs[1, 1].plot(x, y)
axs[1, 1].set_title('Sec^2(x)')

# 调整子图之间的间距和边距
plt.subplots_adjust(wspace=0.3, hspace=0.3, left=0.1, right=0.9, top=0.9, bottom=0.1)

# 显示图形
plt.show()