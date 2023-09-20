import tkinter as tk
import ttkbootstrap as ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('darkly')
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
frame = ttk.Frame(root, padding=10)
label = ttk.Label(frame, text='Hello, World!')
button = ttk.Button(frame, text='Click Me', command=lambda: label.config(text='Button clicked'))
frame.pack()
label.pack()
button.pack()

root.mainloop()