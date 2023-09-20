import tkinter as tk
import random
class jiandan:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.correct_count = 0
        self.incorrect_list = []
        self.question_count = 0  # 添加题目计数器

        # 设置窗口大小和位置
        self.master.geometry("400x155+100+100")  # 修改窗口高度
        self.master.title("简单模式")
        # 创建GUI界面，调用函数
        self.create_widgets()

        # 生成第一个问题，调用函数
        self.generate_question()

    def create_widgets(self):
        
        # 添加提示标签
        self.hint_label = tk.Label(self.master, text="这里是简单模式！")
        self.hint_label.pack(pady=2)

        # 添加问题计数器标签
        self.question_count_label = tk.Label(self.master, text="第{}题".format(self.question_count + 1))
        self.question_count_label.pack(pady=2)

        # 添加问题标签
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        # 添加答案输入框
        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        # 添加提交按钮
        self.submit_button = tk.Button(self.master, text="提交", command=self.check_answer)
        self.submit_button.place(x=145,y=105,width=50)

        #添加退出标签
        self.quit_button = tk.Button(self.master, text="退出", command=self.master.destroy)
        self.quit_button.place(x=205,y=105,width=50)

    def generate_question(self):
        # 生成两个随机数
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        # 显示问题
        self.question_label.configure(text="{} + {} =".format(self.num1, self.num2))

        # 更新问题计数器
        self.question_count += 1
        self.question_count_label.configure(text="第{}题".format(self.question_count))

    def check_answer(self):
        # 获取答案
        answer = self.answer_entry.get()

        # 检查答案是否正确，并更新得分和提示信息
        if answer == str(self.num1 + self.num2):
            self.score += 10
            self.correct_count += 1
            self.hint_label.configure(text="回答正确！得分：{}".format(self.score))
        else:
            self.incorrect_list.append("{} + {} = {}".format(self.num1, self.num2, answer))
            self.hint_label.configure(text="回答错误！得分：{}".format(self.score))

        # 清空答案输入框
        self.answer_entry.delete(0, tk.END)

        # 生成下一个问题
        if len(self.incorrect_list) + self.correct_count < 10:
            self.generate_question()
        else:
            accuracy = self.correct_count / 10 * 100
            self.hint_label.configure(text="正确率：{}%".format(accuracy))
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()
            self.question_label.pack_forget()

class MyButton1:
    #第一个大按钮
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master, text="简单题目",
                                bg='red',
                                fg='yellow',
                                font=("Aa半糖奶咖 (非商业使用)",20),
                                width=20,
                                height=2,
                                command=self.open_window)
        self.button.pack(pady=10)

    def open_window(self):
        new_window = tk.Toplevel(self.master)
        my_window = jiandan(new_window)

class zhongdeng:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.correct_count = 0
        self.incorrect_list = []
        self.question_count = 0  # 添加题目计数器

        # 设置窗口大小和位置
        self.master.geometry("400x155+100+100")  # 修改窗口高度
        self.master.title("中等模式")
        # 创建GUI界面，调用函数
        self.create_widgets()

        # 生成第一个问题，调用函数
        self.generate_question()

    def create_widgets(self):
        
        # 添加提示标签
        self.hint_label = tk.Label(self.master, text="这里是中等模式！")
        self.hint_label.pack(pady=2)

        # 添加问题计数器标签
        self.question_count_label = tk.Label(self.master, text="第{}题".format(self.question_count + 1))
        self.question_count_label.pack(pady=2)

        # 添加问题标签
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        # 添加答案输入框
        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        # 添加提交按钮
        self.submit_button = tk.Button(self.master, text="提交", command=self.check_answer)
        self.submit_button.place(x=145,y=105,width=50)

        #添加退出标签
        self.quit_button = tk.Button(self.master, text="退出", command=self.master.destroy)
        self.quit_button.place(x=205,y=105,width=50)

    def generate_question(self):
        # 生成两个随机数
        self.num1 = random.randint(1, 100)
        self.num2 = random.randint(1, 100)

        # 显示问题
        self.question_label.configure(text="{} + {} =".format(self.num1, self.num2))

        # 更新问题计数器
        self.question_count += 1
        self.question_count_label.configure(text="第{}题".format(self.question_count))

    def check_answer(self):
        # 获取答案
        answer = self.answer_entry.get()

        # 检查答案是否正确，并更新得分和提示信息
        if answer == str(self.num1 + self.num2):
            self.score += 10
            self.correct_count += 1
            self.hint_label.configure(text="回答正确！得分：{}".format(self.score))
        else:
            self.incorrect_list.append("{} + {} = {}".format(self.num1, self.num2, answer))
            self.hint_label.configure(text="回答错误！得分：{}".format(self.score))

        # 清空答案输入框
        self.answer_entry.delete(0, tk.END)

        # 生成下一个问题
        if len(self.incorrect_list) + self.correct_count < 10:
            self.generate_question()
        else:
            accuracy = self.correct_count / 10 * 100
            self.hint_label.configure(text="正确率：{}%".format(accuracy))
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()
            self.question_label.pack_forget()

class MyButton2:
    #第二个大按钮
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master, text="中等题目",
                   bg='blue',\
                   fg='white',\
                   font=('Aa半糖奶咖 (非商业使用)',20),\
                   width=20,\
                   height=2,
                   command=self.open_window)
        self.button.pack(pady=10)

    def open_window(self):
        new_window = tk.Toplevel(self.master)
        my_window = zhongdeng(new_window)
        
class kunnan:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.correct_count = 0
        self.incorrect_list = []
        self.question_count = 0  # 添加题目计数器

        # 设置窗口大小和位置
        self.master.geometry("400x155+100+100")  # 修改窗口高度
        self.master.title("困难模式")
        # 创建GUI界面，调用函数
        self.create_widgets()

        # 生成第一个问题，调用函数
        self.generate_question()

    def create_widgets(self):
        
        # 添加提示标签
        self.hint_label = tk.Label(self.master, text="这里是困难模式！")
        self.hint_label.pack(pady=2)

        # 添加问题计数器标签
        self.question_count_label = tk.Label(self.master, text="第{}题".format(self.question_count + 1))
        self.question_count_label.pack(pady=2)

        # 添加问题标签
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        # 添加答案输入框
        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        # 添加提交按钮
        self.submit_button = tk.Button(self.master, text="提交", command=self.check_answer)
        self.submit_button.place(x=145,y=105,width=50)

        #添加退出标签
        self.quit_button = tk.Button(self.master, text="退出", command=self.master.destroy)
        self.quit_button.place(x=205,y=105,width=50)

    def generate_question(self):
        # 生成两个随机数
        self.num1 = random.randint(1, 1000)
        self.num2 = random.randint(1, 1000)

        # 显示问题
        self.question_label.configure(text="{} + {} =".format(self.num1, self.num2))

        # 更新问题计数器
        self.question_count += 1
        self.question_count_label.configure(text="第{}题".format(self.question_count))

    def check_answer(self):
        # 获取答案
        answer = self.answer_entry.get()

        # 检查答案是否正确，并更新得分和提示信息
        if answer == str(self.num1 + self.num2):
            self.score += 10
            self.correct_count += 1
            self.hint_label.configure(text="回答正确！得分：{}".format(self.score))
        else:
            self.incorrect_list.append("{} + {} = {}".format(self.num1, self.num2, answer))
            self.hint_label.configure(text="回答错误！得分：{}".format(self.score))

        # 清空答案输入框
        self.answer_entry.delete(0, tk.END)

        # 生成下一个问题
        if len(self.incorrect_list) + self.correct_count < 10:
            self.generate_question()
        else:
            accuracy = self.correct_count / 10 * 100
            self.hint_label.configure(text="正确率：{}%".format(accuracy))
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()
            self.question_label.pack_forget()

class MyButton3:
    #第三个大按钮
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master, text="困难题目",
                                bg='yellow',\
                                fg='black',\
                                font=('Aa半糖奶咖 (非商业使用)',20),\
                                width=20,\
                                height=2,\
                                command=self.open_window)
        self.button.pack(pady=10)

    def open_window(self):
        new_window = tk.Toplevel(self.master)
        my_window = kunnan(new_window)           
# 创建主窗口
root = tk.Tk()
root.geometry("300x345")
root.title("计算题练习")

# 创建按钮1
my_button1= MyButton1(root)

#创建按钮2
my_button2= MyButton2(root)

#创建按钮3
my_button3= MyButton3(root)

# 启动主循环
root.mainloop()
