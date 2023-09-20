import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("简单计算器")

        # 创建GUI元素
        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        # 创建按钮
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=4, height=2,
                               font=('Arial', 16), command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "错误")
        else:
            self.display.insert(tk.END, text)

# 创建主窗口
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
