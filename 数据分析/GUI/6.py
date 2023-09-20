from tkinter import *
root = Tk()
root.geometry('320x240')
msg1 = Message(root,
text='''
我的水平起始位置相对窗体0.2，垂直起始位置为绝对位置80像素，我的高度是窗体高度的0.4，宽度是200像素
''', 
relief=GROOVE)  #这里使用3引号，是就不需要使用换行符
msg1.place(relx=0.2,y=80,relheight=0.4,width=200)

root.mainloop()
