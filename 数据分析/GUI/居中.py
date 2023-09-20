import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
# 创建一个Frame控件，并将其居中排列
frame = tk.Frame(root)
frame.pack(pady=50)

# 创建多个控件，并将它们放置在Frame控件中
label1 = tk.Label(frame, text="Label 1")
label1.pack(side="left", padx=10)

label2 = tk.Label(frame, text="Label 2")
label2.pack(side="left", padx=10)

button1 = tk.Button(frame, text="Button 1")
button1.pack(side="left", padx=10)

button2 = tk.Button(frame, text="Button 2")
button2.pack(side="left", padx=10)

root.mainloop()