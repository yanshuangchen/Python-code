#控件布局
# from tkinter import *
# root = Tk()
# lbred = Label(root, text="Red", fg="red",relief=GROOVE)
# lbred.pack()
# lbgreen = Label(root, text="绿色", fg="green",relief=GROOVE)
# lbgreen.pack()
# lbblue = Label(root, text="蓝", fg="blue",relief=GROOVE)
# lbblue.pack()
# root.mainloop()
from tkinter import *
root = Tk()
lbred = Label(root, text="Red", fg="red",cursor='star',relief=GROOVE)
lbred.pack()
lbgreen = Label(root, text="绿色", fg="green",relief=GROOVE)
lbgreen.pack(side=BOTTOM)
lbblue = Label(root, text="蓝", fg="blue",relief=GROOVE)
lbblue.pack(fill=BOTH)
root.mainloop()
#用fill与side进行样式的填充