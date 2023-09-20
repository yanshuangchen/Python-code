import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("计算器")
        self.result = tk.StringVar()
        self.result.set("0")
        self.num1 = ""
        self.num2 = ""
        self.operation = ""

        # 创建文本框
        self.result_box = tk.Entry(self.master, font=("Helvetica", 20), textvariable=self.result, justify="right", bd=5)
        self.result_box.grid(row=0, column=0, columnspan=4, sticky="ew")

        # 创建数字按钮
        for i in range(10):
            tk.Button(self.master, text=str(i), font=("Helvetica", 16), command=lambda x=i: self.append_number(x)).grid(row=3 - i // 3, column=(i % 3))

        # 创建运算符按钮
        tk.Button(self.master, text="+", font=("Helvetica", 16), command=lambda: self.set_operation("+")).grid(row=1, column=3)
        tk.Button(self.master, text="-", font=("Helvetica", 16), command=lambda: self.set_operation("-")).grid(row=2, column=3)
        tk.Button(self.master, text="×", font=("Helvetica", 16), command=lambda: self.set_operation("*")).grid(row=3, column=3)
        tk.Button(self.master, text="÷", font=("Helvetica", 16), command=lambda: self.set_operation("/")).grid(row=4, column=3)
        tk.Button(self.master, text="±", font=("Helvetica", 16), command=self.negate).grid(row=4, column=0)
        tk.Button(self.master, text=".", font=("Helvetica", 16), command=self.decimal).grid(row=4, column=2)

        # 创建其他按钮
        tk.Button(self.master, text="C", font=("Helvetica", 16), command=self.clear).grid(row=1, column=0)
        tk.Button(self.master, text="CE", font=("Helvetica", 16), command=self.clear_entry).grid(row=1, column=1)
        tk.Button(self.master, text="⌫", font=("Helvetica", 16), command=self.backspace).grid(row=1, column=2)
        tk.Button(self.master, text="=", font=("Helvetica", 16), command=self.compute).grid(row=4, column=1)

    def append_number(self, num):
        if self.operation == "":
            self.num1 += str(num)
            self.result.set(self.num1)
        else:
            self.num2 += str(num)
            self.result.set(self.num2)

    def set_operation(self, op):
        self.operation = op

    def negate(self):
        if self.operation == "":
            self.num1 = str(float(self.num1) * -1)
            self.result.set(self.num1)
        else:
            self.num2 = str(float(self.num2) * -1)
            self.result.set(self.num2)

    def decimal(self):
        if self.operation == "":
            if "." not in self.num1:
                self.num1 += "."
                self.result.set(self.num1)
        else:
            if "." not in self.num2:
                self.num2 += "."
                self.result.set(self.num2)

    def clear(self):
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        self.result.set("0")

    def clear_entry(self):
        if self.operation == "":
            self.num1 = ""
            self.result.set("0")
        else:
            self.num2 = ""
            self.result.set(self.num1 + " " + self.operation + " ")

    def backspace(self):
        if self.operation == "":
            self.num1 = self.num1[:-1]
            self.result.set(self.num1)
        else:
            self.num2 = self.num2[:-1]
            self.result.set(self.num2)

    def compute(self):
        if self.num1 != "" and self.num2 != "" and self.operation != "":
            if self.operation == "+":
                self.num1 = str(float(self.num1) + float(self.num2))
            elif self.operation == "-":
                self.num1 = str(float(self.num1) - float(self.num2))
            elif self.operation == "*":
                self.num1 = str(float(self.num1) * float(self.num2))
            elif self.operation == "/":
                self.num1 = str(float(self.num1) / float(self.num2))
            self.num2 = ""
            self.operation = ""
            self.result.set(self.num1)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()