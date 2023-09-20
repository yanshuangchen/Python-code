import tkinter as tk
import random

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

# 创建主窗口
root = tk.Tk()

# 创建计算练习程序
math_quiz = MathQuiz(root)

root.mainloop()

