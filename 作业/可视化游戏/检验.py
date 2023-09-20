import tkinter as tk
import random

class MyWindow:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.correct_count = 0
        self.incorrect_list = []
        self.question_count = 0 

        # 设置窗口大小和位置
        self.master.geometry("400x175+100+100")

        # 创建GUI界面，调用函数
        self.create_widgets()

        # 生成第一个问题，调用函数
        self.generate_question()

    def create_widgets(self):
        # 创建一个Frame控件
        frame = tk.Frame(self.master)
        frame.pack(side="top", fill="both", expand=True)

        # 添加问题计数器标签
        self.question_count_label = tk.Label(frame, text="第{}题".format(self.question_count))
        self.question_count_label.pack()

        # 添加分数标签
        self.score_label = tk.Label(frame, text="得分：{}".format(self.score))
        self.score_label.pack()

        # 添加计时器标签
        self.timer_label = tk.Label(frame, text="时间：60")
        self.timer_label.pack()

        # 添加问题标签
        self.question_label = tk.Label(frame, text="")
        self.question_label.pack()

        # 添加输入框和确认按钮
        self.answer_entry = tk.Entry(frame)
        self.answer_entry.pack()
        self.answer_entry.focus_set() # 让输入框获得焦点
        self.confirm_button = tk.Button(frame, text="确认", command=self.check_answer)
        self.confirm_button.pack()

        # 将所有控件居中排列
        frame.pack_propagate(0)
        frame.pack(side="top", fill="both", expand=True)

    def generate_question(self):
        # 生成两个随机数
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # 生成问题字符串
        question_str = "{} + {} = ?".format(num1, num2)

        # 更新问题标签文本
        self.question_label.config(text=question_str)

        # 更新问题计数器标签文本
        self.question_count += 1
        self.question_count_label.config(text="第{}题".format(self.question_count))

    def check_answer(self):
        # 获取用户输入的答案
        user_answer = self.answer_entry.get()

        # 如果输入为空，则不做任何操作
        if not user_answer:
            return

        # 将用户输入的答案转换为整数
        try:
            user_answer = int(user_answer)
        except ValueError:
            # 如果用户输入的不是整数，则清空输入框并返回
            self.answer_entry.delete(0, tk.END)
            return

        # 获取问题的正确答案
        num1, num2 = map(int, self.question_label.cget("text").split("+"))
        correct_answer = num1 + num2

        # 检查用户输入的答案是否正确
        if user_answer == correct_answer:
            # 更新分数和正确计数器
            self.score += 10
            self.correct_count += 1

            # 更新分数标签文本
            self.score_label.config(text="得分：{}".format(self.score))

            # 生成下一个问题
            self.generate_question()

            # 清空输入框
            self.answer_entry.delete(0, tk.END)

        else:
            # 如果答案错误，则将错误的问题添加到错误列表中
            self.incorrect_list.append(self.question_label.cget("text"))

            # 生成下一个问题
            self.generate_question()

            # 清空输入框
            self.answer_entry.delete(0, tk.END)

root = tk.Tk()
app = MyWindow(root)
root.mainloop()
