import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
text = ttk.Text(root,)
text.pack(padx=10,pady=10,fill=BOTH)
text.insert('insert','text-content 1') #插入内容
text.delete("0.0",'end') #删除内容
text.insert('insert','text-content 2\npy')
text.see(ttk.END) #光标跟随着插入的内容移动
root.mainloop()