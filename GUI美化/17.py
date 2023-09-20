from tkinter import *
import ttkbootstrap as ttk

root = Tk()
root.geometry("400x300")

sizegrip = ttk.Sizegrip(bootstyle="info")
sizegrip.pack(side=BOTTOM, anchor=SE)

root.mainloop()