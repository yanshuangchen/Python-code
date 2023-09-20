import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# 创建样式对象
style = Style(theme='journal')
root = style.master

# 创建按钮
button = ttk.Button(root, text="Click Me")

# 设置按钮大小，调节第二个参数可以减小宽度
button.configure(width=20)
button.configure(padding=(20, 3))

# 显示按钮
button.pack()

# 进入主循环
root.mainloop()