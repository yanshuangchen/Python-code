#创建画布 中心为原点 绘制图形
import matplotlib.pyplot as plt
import numpy as np

def plot_figure():
    wh=3 
    hh=3
    plt.figure(figsize=(6, 6))
    p = plt.plot([-wh, wh], [0, 0], c='r')
    p = plt.plot([0, 0], [-hh, hh], c='r')
    t = np.arange(0, 4 * np.pi, 0.01)
    x = (wh / 4) * (np.sin(2 * t) + 2 * np.cos(t))
    y = (hh / 4) * (np.cos(2 * t) + 2 * np.sin(t))
    p = plt.plot(x, y, c='b')
    plt.show()


