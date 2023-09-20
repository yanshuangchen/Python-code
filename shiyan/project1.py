# project1.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from draw_functions import DrawFunctions

class Project1:
    def __init__(self,code,year):
        self.code=code
        self.year=year
        self.project_window = ttk.Toplevel()
        self.project_window.title("股票查询结果")
        self.project_window.geometry("400x400")

        self.btnn1 = ttk.Button(self.project_window, text="画图1", command=self.draw_picture1)
        self.btnn1.pack(padx=10, pady=10)
        # Checkbutton(bootstyle="square-toggle")

        self.btn2 = ttk.Button(self.project_window, text="画图2", command=self.draw_picture2)
        self.btn2.pack(padx=10, pady=10)
        
        self.btn3 = ttk.Button(self.project_window, text="画图3", command=self.draw_picture3)
        self.btn3.pack(padx=10, pady=10)

        self.btn4 = ttk.Button(self.project_window, text="打印\保存到本地桌面", command=self.draw_picture4)
        self.btn4.pack(padx=10, pady=10)

        self.btn5 = ttk.Button(self.project_window, text="返回",command=self.root.destroy)
        self.btn5.pack(padx=10, pady=10)

    def draw_picture1(self):
        draw_funcs = DrawFunctions(self.code,self.year)
        draw_funcs.draw_picture1()

    def draw_picture2(self):
        draw_funcs = DrawFunctions(self.code,self.year)
        draw_funcs.draw_picture2()

    def draw_picture3(self):
        draw_funcs = DrawFunctions(self.code,self.year)
        draw_funcs.draw_picture3()

    def draw_picture4(self):
        draw_funcs = DrawFunctions(self.code,self.year)
        draw_funcs.printresult()    