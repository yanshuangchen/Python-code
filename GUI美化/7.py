import ttkbootstrap as ttk
#实例化创建应用程序窗口,其实大部分命令与tkinter相似
root = ttk.Window(
        title="窗口名字",        #设置窗口的标题
        themename="litera",     #设置主题
        size=(1066,600),        #窗口的大小
        position=(100,100),     #窗口所在的位置
        minsize=(0,0),          #窗口的最小宽高
        maxsize=(1920,1080),    #窗口的最大宽高
        resizable=None,         #设置窗口是否可以更改大小
        alpha=1.0,              #设置窗口的透明度(0.0完全透明）
        )
root.place_window_center()    #让显现出的窗口居中
root.resizable(False,False)   #让窗口不可更改大小
root.wm_attributes('-topmost', 1)#让窗口位置其它窗口之上
root.mainloop()