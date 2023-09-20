import tkinter as tk

root = tk.Tk()

# 第一行控件
label1 = tk.Label(root, text="Label 1")
label1.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(root, text="Label 2")
label2.pack(side=tk.LEFT, padx=10, pady=10)

label3 = tk.Label(root, text="Label 3")
label3.pack(side=tk.LEFT, padx=10, pady=10)

# 第二行控件
button1 = tk.Button(root, text="Button 1")
button1.pack(side=tk.TOP, padx=10, pady=10)

button2 = tk.Button(root, text="Button 2")
button2.pack(side=tk.TOP, padx=10, pady=10)

button3 = tk.Button(root, text="Button 3")
button3.pack(side=tk.TOP, padx=10, pady=10)

# 第三行控件
entry1 = tk.Entry(root)
entry1.pack(side=tk.RIGHT, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.pack(side=tk.RIGHT, padx=10, pady=10)

entry3 = tk.Entry(root)
entry3.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
