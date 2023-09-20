import tkinter as tk

# 创建一个窗口对象
window = tk.Tk()

# 设置窗口标题
window.title("数字闯关游戏")

# 设置窗口大小
window.geometry("400x400")

# 添加标签控件
label = tk.Label(text="Hello, World!")
label.pack()

# 添加按钮控件
button = tk.Button(text="确定")
button.pack()
button = tk.Button(text="取消")
button.pack()

# 运行窗口应用程序
window.mainloop()
