alist=['柳','唐','颜','慕容','叶','沈','杜','凌','花','莫']
blist=['蓝' , '芊' , '碧' , '无' , '双' , '吟' , '玉' , '琪' , '竹' , '香' , '依' , '若' ]
clist=['(无)' ,'月', '雪' , '晨',  '宁' , '萍' , '落' , '楹' , '秋' , '溪'  ]
newlist=[]
newlist.append(alist[2])
newlist.append(blist[4])
newlist.append(clist[3])
#print(newlist)
my_string = ' '.join(newlist)
my_string = my_string.replace(' ', '')
print(my_string)