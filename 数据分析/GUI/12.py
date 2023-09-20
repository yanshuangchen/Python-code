from tkinter import Tk, Button
from tkinter import messagebox
from tkinter.colorchooser import askcolor

# 创建 Tkinter 窗口
root = Tk()

# 创建按钮
button = Button(root, text="选择颜色", command=lambda: choose_color())

# 显示按钮
button.pack()

# 定义颜色选择函数
def choose_color():
    # 获取颜色选择器的返回值
    color = askcolor(title="选择颜色")

    # 如果用户单击了取消按钮，则 askcolor 返回 None
    if color is not None:
        # 显示消息框，显示用户选择的颜色
        messagebox.showinfo("您选择的颜色是", str(color[1]))

# 运行 Tkinter 窗口
root.mainloop()
