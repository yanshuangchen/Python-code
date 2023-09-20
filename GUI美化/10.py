import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
#为按钮添加点击事件
#法一
def button1():
    print("Button1点击了一下！")
ttk.Button(root,text="Button1", bootstyle=(PRIMARY, "outline-toolbutton"),command=button1).pack(side=LEFT, padx=5, pady=10)
#法二
def button2(event): #这里要加一个参数，不然会报错
    print("Button2点击了一下！")
    button_text = event.widget["text"] #得到按钮上的文本
    print(button_text)
b = ttk.Button(root,text="Button2", bootstyle=(PRIMARY, "outline-toolbutton"))
b.pack(side=LEFT, padx=5, pady=10)
b.bind("<Button-1>", button2) #<Button-1>鼠标左键
root.mainloop()