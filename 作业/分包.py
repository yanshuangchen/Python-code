import tkinter
class ticket_expense(object):
    def __init__(self,root:tkinter.Tk):
        self.root=root
        self.num=0
        self.unitprice=0
        self.expense=0
        self.lb1=tkinter.Label(self.root,text='请选择景点')
        self.lb2=tkinter.Label(self.root,text='请选择购票张数')
        self.var=tkinter.IntVar()#获得变化参数
        self.rd1=tkinter.Radiobutton(self.root,text='东方明珠',variable=self.var,value=0,command=self.unit_price)
        self.rd2=tkinter.Radiobutton(self.root,text='野生动物园',variable=self.var,value=1,command=self.unit_price)
        self.rd3=tkinter.Radiobutton(self.root,text='科技馆',variable=self.var,value=2,command=self.unit_price)
        self.entry=tkinter.Entry(self.root)
        self.bt1=tkinter.Button(self.root,text='计算',command=self.calculate)
        self.text=tkinter.Text(self.root)

    def unit_price(self):
        a=self.var.get()
        if a==0:
            self.unitprice=160
        elif a==1:
            self.unitprice=130
        else:
            self.unitprice=60   

    def calculate(self):
        self.unit_price()
        num=int(self.entry.get())
        if num>=50:
            self.expense=num*self.unitprice*0.8
        elif num>=20:
            self.expense=num*self.unitprice*0.95
        else:
            self.expense=num*self.unitprice
        self.text.insert(tkinter.END,"票的价格为"+str(self.expense)+'元'+'\n')
        
    def begin(self):
        self.lb1.pack()
        self.rd1.pack()
        self.rd2.pack()
        self.rd3.pack()
        self.lb2.pack()
        self.entry.pack()
        self.bt1.pack()
        self.text.pack()
        self.root.mainloop()
            
def main():
    root=tkinter.Tk()
    root.title('景点购票')
    me=ticket_expense(root)
    me.begin()

if __name__=='__main__':
    main()