import tkinter as tk

class MyWindow:
    def __init__(self, master):
        self.master = master

        # 创建控件,command中含有命令在下一个函数中
        self.label = tk.Label(self.master, text="请选择景点：")
        self.label.pack()
        
        # 创建 IntVar 变量
        self.choice = tk.IntVar()

        # 创建三个 Radiobutton 控件
        self.radio1 = tk.Radiobutton(self.master, text="东方明珠", variable=self.choice, value=160)
        self.radio2 = tk.Radiobutton(self.master, text="野生动物馆", variable=self.choice, value=130)
        self.radio3 = tk.Radiobutton(self.master, text="科技馆", variable=self.choice, value=60)

        # 布局控件
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()

        # 标题框
        self.label = tk.Label(self.master, text="请输入购票张数：")
        self.label.pack()

        # 输入框
        self.empty_entry = tk.Entry(self.master)
        self.empty_entry.pack()

        # 命令按钮，并触发命令
        self.button = tk.Button(self.master, text="计算",command=self.jisuan)
        self.button.pack()

        # 创建多行文本框
        self.text = tk.Text(self.master)
        self.text.pack()   


    def jisuan(self):
        # 获取输入框中的购票张数
        number = self.empty_entry.get()

        # 判断输入是否合法
        if not number.isdigit():
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "请输入有效的数字！")
            return

        # 将购票张数转换为整数
        number = int(number)

        # 判断购票张数是否合法
        if number <= 0:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "购票数量必须大于0！")
            return

        # 根据选择的景点名称，确定门票单价
        if self.choice.get() == 160:
            price = 160
            name = "东方明珠"
        elif self.choice.get() == 130:
            price = 130
            name = "野生动物园"
        elif self.choice.get() == 60:
            price = 60
            name = "科技馆"
        else:
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "请选择景点！")
            return

        # 计算门票总价
        if number >= 50:
            total_price = price * number * 0.8
        elif number >= 20:
            total_price = price * number * 0.95
        else:
            total_price = price * number

        # 在多行文本框中显示门票信息
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, f"景点名称：{name}\n")
        self.text.insert(tk.END, f"门票张数：{number}\n")
        self.text.insert(tk.END, f"门票总价：{total_price:.2f}元")  

if __name__=='__main__':
    root = tk.Tk()
    root.geometry("400x400")
    my_window = MyWindow(root)