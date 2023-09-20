alist=[]
blist=[]
with open(r"D:\info.txt") as file:
    for line in file:
        columns = line.split()  
        alist.append(columns[1])
        blist.append(columns[2])
del alist[0]
del blist[0]
t=0
p=0
m=0
q=0
for i in range(len(blist)):
    if blist[i] =="男":
        t+=float(alist[i])
        p+=1
    if blist[i] =="女":
        m+=float(alist[i])
        q+=1
if (t/p)>1.75:
    print("该班男生身高为A类")
elif (t/p)>1.65:
    print("该班男生身高为B类")
else:
    print("该班男生身高为C类")
if (m/q)>1.65:
    print("该班女生身高为A类")
elif (m/q)>1.55:
    print("该班女生身高为B类")
else:
    print("该班女生身高为C类")

     