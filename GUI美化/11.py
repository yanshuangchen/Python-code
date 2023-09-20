import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
e1 = ttk.Entry(root,show=None)
e1.insert('0',"薪酬分析系统")
e1.grid(row=5, column=1, sticky=ttk.W, padx=10,pady=10)
e2 = ttk.Entry(root,show="*",width=50,bootstyle=PRIMARY)
e2.grid(row=10, column=1, sticky=ttk.W, padx=10, pady=10)
e3_content = ttk.StringVar()
e3 = ttk.Entry(root,bootstyle='success', textvariable=e3_content).grid(row=15, column=1, sticky=ttk.W, padx=10, pady=10)
def get_entry_contetn():
    print("e1: ",e1.get())
    print("e2: ",e2.get())
    print("e3: ",e3_content.get())
ttk.Button(root,text="get_entry_contetn", bootstyle=(PRIMARY, "outline-toolbutton"),command=get_entry_contetn).grid(row=20, column=1, sticky=ttk.W, padx=10, pady=10)
root.mainloop()