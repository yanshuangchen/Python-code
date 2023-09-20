# primary：主要按钮，通常用于突出重要的操作。
# secondary：次要按钮，通常用于次要的操作，或者作为 primary 按钮的替代品。
# success：成功按钮，通常用于表示操作已成功完成。
# danger：危险按钮，通常用于表示操作可能会有危险或者删除操作。
# warning：警告按钮，通常用于表示操作可能会有风险或警告。
# info：信息按钮，通常用于表示一些提示性信息或者帮助信息。
# light：轻按钮，通常用于表示次要的或者普通的操作。
# dark：暗按钮，通常用于表示重要的操作或者突出的信息。
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# 创建样式对象
style = Style(theme='journal')

root=style.master
root.geometry("400x400")

# 创建窗口和按钮
button1 = ttk.Button(root, text="Primary", style="primary.TButton")
# 智能设置宽度
button1.configure(width=20)
button2 = ttk.Button(root, text="Secondary", style="secondary.TButton")
button2.configure(width=20)
button3 = ttk.Button(root, text="Success", style="success.TButton")
button4 = ttk.Button(root, text="Danger", style="danger.TButton")
button5 = ttk.Button(root, text="Warning", style="warning.TButton")
button6 = ttk.Button(root, text="Info", style="info.TButton")
button7 = ttk.Button(root, text="Light", style="light.TButton")
a=ttk.Separator(root,bootstyle="info")
a.pack(pady=5,fill='x')
button8 = ttk.Button(root, text="Dark", style="dark.TButton")

# 显示按钮
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()

# 进入主循环
root.mainloop()