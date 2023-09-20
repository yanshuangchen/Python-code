import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.plot(x, y)
plt.annotate('最高点', xy=(1, 10), xytext=(2, 8), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
