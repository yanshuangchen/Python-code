import tkinter as tk
import ttkbootstrap as ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('darkly')
menu = ttk.Menu(root)
menu.add_command(label='Option 1')
menu.add_command(label='Option 2')
menu.add_command(label='Option 3')
menubutton = ttk.Menubutton(root, text='Menu',style="success",menu=menu)
menubutton.pack()
# default separator style

# info colored separator style - handle color
a=ttk.Separator(root,bootstyle="info")
a.pack(pady=5,fill='x')
root.mainloop()