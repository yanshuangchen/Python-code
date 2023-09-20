import tkinter as tk
import random
def jiandan():
    MathQuiz(window)
#     root=tk.Tk()
#     root.title("简单题目")
#     root.geometry("300x300")
# #Label的L是大写的
#     # lb=tk.Text(root,text='我是一个标签',\
#     #           bg='#4885E9',\
#     #           fg='red',\
#     #           font=('华文新魏',32),\
#     #           width=20,\
#     #           height=2,\
#     #           )#注意逗号
#     # lb.pack()
#     entry = tk.Entry(root)
    
#     # 获取文本框中的值
#     value = entry.get()
#     print(value)
#     entry.pack()
#     root.mainloop()
class MathQuiz:
    def __init__(self, master):
        self.master = master
        self.score = 0

        # 创建GUI界面
        self.create_widgets()

        # 生成第一个问题
        self.generate_question()

    def create_widgets(self):
        # 添加问题标签
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        # 添加答案输入框
        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        # 添加提交按钮
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        # 添加提示标签
        self.hint_label = tk.Label(self.master, text="")
        self.hint_label.pack()

    def generate_question(self):
        # 生成两个随机数
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        # 更新问题标签
        self.question_label.config(text="What is {} + {}?".format(self.num1, self.num2))

    def check_answer(self):
        # 获取用户输入的答案
        try:
            answer = int(self.answer_entry.get())
        except ValueError:
            self.hint_label.config(text="Please enter a number!")
            return

        # 检查答案是否正确
        if answer == self.num1 + self.num2:
            self.score += 1
            self.hint_label.config(text="Correct! Your score is {}".format(self.score))
            self.generate_question()
        else:
            self.hint_label.config(text="Incorrect. Try again.")



#建立特定窗口
window = tk.Tk()

# 设置窗口标题
window.title("数字闯关游戏")

# 设置窗口大小
window.geometry("300x360")

# 添加按钮控件
button1= tk.Button(window,text="简单题目",
                   bg='red',\
                   fg='yellow',\
                   font=("Aa半糖奶咖 (非商业使用)",20),\
                   width=20,\
                   height=2,\
                   command=jiandan
                  )
button1.pack(pady=20)
button2= tk.Button(window,text="中等题目",
                   bg='blue',\
                   fg='white',\
                   font=('Aa半糖奶咖 (非商业使用)',20),\
                   width=20,\
                   height=2,\
                  )
button2.pack()
button3= tk.Button(window,text="困难题目",
                   bg='yellow',\
                   fg='black',\
                   font=('Aa半糖奶咖 (非商业使用)',20),\
                   width=20,\
                   height=2,\
                  )
button3.pack(pady=20)
# 运行窗口应用程序
window.mainloop()
