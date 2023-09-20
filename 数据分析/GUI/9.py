from tkinter import *
from tkinter import filedialog

# 创建 Tkinter 窗口
root = Tk()

# 隐藏 Tkinter 窗口
root.withdraw()

# 打开文件选择对话框
file_path = filedialog.askopenfilename()

# 打印所选文件的路径
print(file_path)
