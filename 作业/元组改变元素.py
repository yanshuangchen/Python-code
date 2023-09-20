a=("chicken","beef","cola","humbuger","duck")
b=list(a)
b[1]="rice"
b[2]="dumping"
c=tuple(b)
for i in c:
    print(i)