from ttkbootstrap import Style
from tkinter import ttk

style = Style(theme = "solar") # 使用的主题名称
# light
# cosmo - flatly - journal - literal - lumen - minty - pulse - sandstone - united - yeti
# dark
# cyborg - darkly - solar - superhero

window = style.master
window.geometry("300x200")

ttk.Button(window, text="Submit", style='primary.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
window.mainloop()
