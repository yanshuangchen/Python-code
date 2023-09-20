import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.geometry('400x200')

# 创建滑块
slider = tk.Scale(root, from_=22013310, to=22013340,length=200, orient=tk.HORIZONTAL)

# 定义更新函数
def update_label(val):
    label.config(text=val)

# 创建标签
label = tk.Label(root)

# 绑定更新函数到滑块
slider.config(command=lambda val: update_label(val))

# 显示滑块和标签
slider.pack()
label.pack()
# 进入主循环
root.mainloop()
