
a=int(input("请输入一个数字："))
b=input("请输入加减乘除符号：")
c=int(input("请输入另一个数字"))
blist=['+','-','*','/']
if b in blist:
    
    if b=="+":
        print(a+c)
    elif b=="-":
        print(a-c)
    elif b=="*":
        print(a*c)
    elif b=="/":
        if c==0:

            print("除数不能为零")
        else:
            print(a/c)
else:
    print("符号输入错误")
