import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
style = ttk.Style()
# darkly
# flatly
# litera
# lumen
# lux
# materia
# minty
# pulse
# sandstone
# simplex
# sketchy
# slate
# solar
# spacelab
# superhero
# united
# yeti
style.theme_use('solar')
frame = ttk.LabelFrame(root, text='Frame Title', padding=10)
label1 = ttk.Label(frame, text='Label 1',bootstyle=SUCCESS)
label2 = ttk.Label(frame, text='Label 2',bootstyle=WARNING)
entry = ttk.Entry(frame)
frame.pack()
label1.pack()
label2.pack()
entry.pack()

root.mainloop()