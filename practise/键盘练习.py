import tkinter as tk
import random
import time

class TypingTest:
    def __init__(self, master):
        self.master = master
        master.title("Typing Test")

        self.word_label = tk.Label(master, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 24))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.result_label = tk.Label(master, text="", font=("Arial", 18))
        self.result_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", font=("Arial", 18), command=self.start)
        self.start_button.pack(pady=10)

        self.words = ["apple", "banana", "orange", "pear", "peach", "grape", "lemon", "lime", "cherry", "strawberry"]
        self.word = ""

        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.correct_count = 0
        self.incorrect_count = 0

    def start(self):
        self.word = random.choice(self.words)
        self.word_label.config(text=self.word)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()

    def check_word(self, event):
        self.end_time = time.time()
        self.total_time += self.end_time - self.start_time

        if self.entry.get() == self.word:
            self.result_label.config(text="Correct!")
            self.correct_count += 1
        else:
            self.result_label.config(text="Incorrect!")
            self.incorrect_count += 1

        self.start()

    def get_speed(self):
        speed = round((len(self.words) / self.total_time) * 60)
        return speed

    def get_accuracy(self):
        accuracy = round((self.correct_count / (self.correct_count + self.incorrect_count)) * 100)
        return accuracy

root = tk.Tk()
typing_test = TypingTest(root)
root.mainloop()
