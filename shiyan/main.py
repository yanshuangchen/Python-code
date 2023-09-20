import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from firstttk import First
from project2 import Project2

class MainWindow:
    def __init__(self):
        self.root = ttk.Window()
        self.root.geometry("300x230")
        self.root.title("窗口示例")

        self.btn1 = ttk.Button(self.root, text="项目一\n财务指标可视化分析", 
                                bootstyle=PRIMARY,
                                command=self.open_window1)
        self.btn1.pack(padx=10, pady=10)
        self.btn1.configure(width=20)

        self.btn2 = ttk.Button(self.root, text="项目二",
                               bootstyle=(INFO, OUTLINE),
                              command=self.open_window2)
        self.btn2.pack(padx=10, pady=10)
        self.btn2.configure(width=20)

        self.root.mainloop()

    def open_window1(self):
        self.first = First()

    def open_window2(self):
        self.project2 = Project2()

if __name__ == "__main__":
    app = MainWindow()