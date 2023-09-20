import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

# button = ttk.Button(root, text="Click me!", style="my.TButton", command=lambda: print("Button clicked."))
# button.pack(padx=20, pady=20)
button = ttk.Button(root, text="Click me!",command=lambda: print("Button clicked."))
button.pack(padx=20, pady=20)

# style = ttk.Style()
# style.configure("my.TButton", padding=10, width=20, foreground="red")

root.mainloop()