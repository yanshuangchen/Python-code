from tkinter import *
root=Tk()
#Label的L是大写的
lb=Label(root,text='我是一个标签',\
              bg='#4885E9',\
              fg='red',\
              font=('华文新魏',32),\
              cursor='man',
              width=20,\
              height=2,\
              relief=SUNKEN)#注意逗号
lb.pack()
root.mainloop()