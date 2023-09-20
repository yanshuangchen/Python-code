from tkinter import Tk, Button, simpledialog
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Label

# 创建 Tkinter 窗口
root = Tk()

# 创建标签和 StringVar
label = Label(root, text="输入您的名字：")
name_var = StringVar()

# 创建按钮
button = Button(root, text="输入", command=lambda: input_dialog())

# 显示标签和按钮
label.pack()
button.pack()

# 定义输入对话框
def input_dialog():
    name = simpledialog.askstring("输入您的名字", "请输入您的名字：", parent=root)

    # 检查用户是否单击了取消按钮
    if name is not None:
        # 将用户输入的值设置为 StringVar 的值
        name_var.set(name)

        # 显示消息框，显示用户输入的值
        messagebox.showinfo("欢迎", "欢迎，" + name + "！")

# 运行 Tkinter 窗口
root.mainloop()
