# 导入相应的库
import tkinter as tk
from colour import Color

# 创建一个窗口对象
window = tk.Tk()

# 创建渐变色
gradient = tuple(colour.Color("red").range_to(colour.Color("yellow"), 20))
# 添加按钮控件并设置背景色为渐变色
button1 = tk.Button(window, text="简单题目",
                    bg=gradient[0].hex, fg='yellow', 
                    font=('Aa半糖奶咖（非商业使用）', 20),
                    width=20, height=2)
button1.pack(pady=20)

button2 = tk.Button(window, text="中等题目",
                    bg=gradient[5].hex, fg='white', 
                    font=('Aa半糖奶咖（非商业使用）', 20),
                    width=20, height=2)
button2.pack(pady=20)

button3 = tk.Button(window, text="困难题目",
                    bg=gradient[10].hex, fg='black', 
                    font=('Aa半糖奶咖（非商业使用）', 20),
                    width=20, height=2)
button3.pack(pady=20)

# 运行窗口应用程序
window.mainloop()


