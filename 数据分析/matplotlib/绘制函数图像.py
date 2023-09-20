import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def func1(x):
    return 5 * x**3 + 4 * np.sin(x)

def func2(x):
    return -x**3 + 2 * x**2 + np.cos(x)

# 生成采样点
x = np.linspace(-1.7, 1.7, 1000)
y1 = func1(x)
y2 = func2(x)

# 绘制曲线
fig, ax = plt.subplots()
ax.plot(x, y1, 'r-', label=r'$y=5x^3+4\sin(x)$')
ax.plot(x, y2, 'bo', markersize=2, label=r'$y=-x^3+2x^2+\cos(x)$')

# 添加图例
ax.legend(loc='upper left')

# 显示图像
plt.show()