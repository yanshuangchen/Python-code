f=open(r"C:\Users\86138\Desktop\data.csv","r")
alist=f.readlines()
clist=[]
for i in alist:
    blist=i.split(",")
    new_list = [blist[0],blist[-1][:-2]]
    print("{0:{2}<40}{1:{2}<20}".format(blist[0].strip(),blist[-1][:-2],chr(12288)))
f.close
