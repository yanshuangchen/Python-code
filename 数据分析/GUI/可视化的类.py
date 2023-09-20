import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("计算器")

        # 创建屏幕
        self.screen = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # 创建数字按钮
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('0', 4, 0)

        # 创建运算符按钮
        self.create_button('+', 1, 3)
        self.create_button('-', 2, 3)
        self.create_button('*', 3, 3)
        self.create_button('/', 4, 3)

        # 创建其他按钮
        self.create_button('C', 4, 1)
        self.create_button('←', 4, 2)
        self.create_button('=', 5, 3)

        # 初始化状态
        self.reset()

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                           command=lambda:self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text.isdigit():
            if self.new_number:
                self.screen.delete(0, tk.END)
                self.new_number = False
            self.screen.insert(tk.END, text)
        elif text in ['+', '-', '*', '/']:
            self.operation = text
            self.first_number = float(self.screen.get())
            self.new_number = True
        elif text == 'C':
            self.reset()
        elif text == '←':
            self.screen.delete(len(self.screen.get())-1, tk.END)
        elif text == '=':
            if self.operation:
                second_number = float(self.screen.get())
                if self.operation == '+':
                    result = self.first_number + second_number
                elif self.operation == '-':
                    result = self.first_number - second_number
                elif self.operation == '*':
                    result = self.first_number * second_number
                elif self.operation == '/':
                    result = self.first_number / second_number
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, str(result))
                self.operation = None
                self.new_number = True

    def reset(self):
        self.screen.delete(0, tk.END)
        self.operation = None
        self.first_number = 0
        self.new_number = True

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()