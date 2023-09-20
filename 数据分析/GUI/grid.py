import tkinter as tk

root = tk.Tk()

# 第一行控件
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3")
label3.grid(row=0, column=2)

# 第二行控件
button1 = tk.Button(root, text="Button 1")
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="Button 2")
button2.grid(row=1, column=1)

button3 = tk.Button(root, text="Button 3")
button3.grid(row=1, column=2)

# 第三行控件
entry1 = tk.Entry(root)
entry1.grid(row=2, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=2)

# 第四行控件
checkbox1 = tk.Checkbutton(root, text="Checkbox 1")
checkbox1.grid(row=3, column=0)

checkbox2 = tk.Checkbutton(root, text="Checkbox 2")
checkbox2.grid(row=3, column=1)

checkbox3 = tk.Checkbutton(root, text="Checkbox 3")
checkbox3.grid(row=3, column=2)

# 第五行控件
text = tk.Text(root, height=5, width=30)
text.grid(row=4, column=0, columnspan=3)

root.mainloop()
