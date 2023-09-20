#输入三位参加的嘉宾并打印名称
alist=['蔡','徐','坤']
print("第一次来的有:")
for i in alist:
    print(i)


#移除嘉宾“坤”，加入嘉宾“鸡”，打印第二次来的嘉宾名称
alist.remove('坤')
alist.append('鸡')
print("第二次来的有:")
for i in alist:
    print(i)


#加入三位嘉宾“你”“太”“美”，并打印第三次来的嘉宾名称
alist.append('你')
alist.insert(0,'太')
a=round(len(alist))
alist.insert(a,'美')
print("第三次来的有:")
b=len(alist)
for i in range(0,b):
    print(alist[i])


#删除嘉宾并通知抱歉，并通知仍参加的嘉宾
while len(alist) > 2:
    element = alist.pop(0)
    print("很遗憾%s,不能和您进行晚餐了"%element)
while len(alist) > 0:
    element = alist.pop(0)
    print("%s,您仍在邀请之列"%element)

    

