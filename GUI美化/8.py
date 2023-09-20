import ttkbootstrap as ttk
from ttkbootstrap.constants import *
root = ttk.Window()
ttk.Label(root,text="标签1",bootstyle=INFO).pack(side=ttk.LEFT, padx=5, pady=10)
ttk.Label(root,text="标签2",bootstyle="inverse").pack(side=ttk.LEFT, padx=5, pady=10)
ttk.Label(root,text="标签3",bootstyle="inverse-danger").pack(side=ttk.LEFT, padx=5, pady=10)
ttk.Label(root, text="标签4", bootstyle=WARNING, font=("微软雅黑", 15), background='#94a2a4').pack(side=LEFT, padx=5, pady=10)
root.mainloop()
'''
# bootstyle colors
PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
DANGER = 'danger'
WARNING = 'warning'
INFO = 'info'
LIGHT = 'light'
DARK = 'dark'

# bootstyle types
OUTLINE = 'outline'
LINK = 'link'
TOGGLE = 'toggle'
INVERSE = 'inverse'
STRIPED = 'striped'
TOOLBUTTON = 'toolbutton'
ROUND = 'round'
SQUARE = 'square'
'''