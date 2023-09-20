from datetime import datetime, date
# 不同天的时间差
time_1 = '2023-08-16 17:00:00'
time_2 = '2023-08-16 19:40:00'
time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
# 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分，没有包含天数差，total_seconds包含天数差
# 所以total_seconds两种情况都是可以用的
total_seconds = (time_2_struct - time_1_struct).total_seconds()
hour=total_seconds/3600
money=2870
print(hour)
if hour>72:
    print("支付%d"%(money*0.1))
elif 4<hour<72:
    print("支付%d"%(money*0.2))
elif hour<4:
    print("支付%d"%(money*0.4))