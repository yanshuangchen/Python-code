from tkinter import *
root = Tk()
lbred = Label(root, text="Red", fg="red",relief=GROOVE)
lbred.grid(column=2,row=0)
lbgreen = Label(root, text="绿色", fg="green",relief=GROOVE)
lbgreen.grid(column=0,row=1)
lbblue = Label(root, text="蓝", fg="blue",relief=GROOVE)
lbblue.grid(column=1,columnspan=2,ipadx=20,row=2)
root.mainloop()
#用grid排列标签