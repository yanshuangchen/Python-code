import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
ttk.Button(root, text="Button 1", bootstyle=SUCCESS).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 3", bootstyle=(PRIMARY, "outline-toolbutton")).pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 4", bootstyle="link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 5", bootstyle="success-link").pack(side=LEFT, padx=5, pady=10)
ttk.Button(root, text="Button 6", state="disabled").pack(side=LEFT, padx=5, pady=10) #在禁用状态下创建按钮
root.mainloop()