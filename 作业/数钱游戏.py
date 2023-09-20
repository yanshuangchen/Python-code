import datetime
startTime = datetime.datetime.now()
userDict = {}
while True:
    user = input("请输入用户名") #模拟user数了1次钞票
    curTime = datetime.datetime.now()
    timeDiff = (curTime-startTime).seconds
    if timeDiff < 5:
        print("游戏尚未开始，还有%s秒"%(5-timeDiff))
        continue
eilf timeDiff > 15:
        print("\n\n游戏已结束,排行榜为")
        tmpList = []
        for k,v in userDict.items():
            tmpList.append([k,v])
        tmpList.sort(key = lambda x: -x[1])
        for user,money in tmpList:
            print("用户%s：%d元"%(user,money))
        break
    else:
        if user not in userDict:
            userDict[user] = 100
        else:
            userDict[user] += 100
        print("用户%s:%d元"%(user,userDict[user]))
