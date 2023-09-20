#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author： Smly
# @datetime： 2021/12/4 19:44
# @Version： 1.0
import tkinter as tk

RED = (255, 0, 0)
BLUE = (0, 0, 255)


def use_rgb(rgb):
    """
    将rgb转十六进制
    Args:
        rgb: rgb颜色
    Returns: 十六进制
    """
    rgb = str(rgb)
    RGB = rgb.replace('(', '').replace(")", '').split(',')  # 将RGB格式划分开来
    color = '#'
    for i in RGB:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0')
    return color


# 先初始化tkinter组件，创建窗口对象
window = tk.Tk()
# 设置窗口的标题，长宽
window.title("title")
window.geometry("800x600")
# 使用canvas
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()
a1, a2, a3, b1, b2, b3 = RED[0], RED[1], RED[2], BLUE[0], BLUE[1], BLUE[2]
# 相差的rgb
r, g, b = (b1 - a1), (b2 - a2), (b3 - a3)
print(r, g, b)
h = 200
for i in range(200):
    x1 = 100 + i
    y1 = 100
    t = (x1 - 100) / (300 - 100)
    rgb = (int(a1 + r * t), int(a2 + g * t), int(a3 + b * t))
    print(rgb)
    canvas.create_line((x1, y1), (x1, y1 + h), fill=use_rgb(rgb))
window.mainloop()
