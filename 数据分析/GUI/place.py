import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
# 第一行控件
label1 = tk.Label(root, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(root, text="Label 2")
label2.place(x=150, y=50)

label3 = tk.Label(root, text="Label 3")
label3.place(x=250, y=50)

# 第二行控件
button1 = tk.Button(root, text="Button 1")
button1.place(x=50, y=100)

button2 = tk.Button(root, text="Button 2")
button2.place(x=150, y=100)

button3 = tk.Button(root, text="Button 3")
button3.place(x=250, y=100)

# 第三行控件
entry1 = tk.Entry(root)
entry1.place(x=50, y=150, width=50)

entry2 = tk.Entry(root)
entry2.place(x=150, y=150, width=100)

entry3 = tk.Entry(root)
entry3.place(x=250, y=150, width=100)

# 第四行控件
checkbox1 = tk.Checkbutton(root, text="Checkbox 1")
checkbox1.place(x=50, y=200)

checkbox2 = tk.Checkbutton(root, text="Checkbox 2")
checkbox2.place(x=150, y=200)

checkbox3 = tk.Checkbutton(root, text="Checkbox 3")
checkbox3.place(x=250, y=200)

# 第五行控件
text = tk.Text(root, height=5, width=30)
text.place(x=50, y=250)

root.mainloop()
