import datetime
'''t1 = datetime.datetime.strptime("2017-9-06 10:30:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.datetime.strptime("2017-9-06 12:30:00", "%Y-%m-%d %H:%M:%S")
interval_time = (t2 - t1).seconds 
total_interval_time = (t2 - t1).total_seconds() 
print(interval_time)
print(total_interval_time)'''
t1 = datetime.datetime.strptime("2017-9-06 10:30:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.datetime.strptime("2017-9-08 12:30:00", "%Y-%m-%d %H:%M:%S") 
interval_time = (t2 - t1).seconds
total_interval_time = (t2 - t1).total_seconds() 
print (interval_time)
print (total_interval_time) 
td = (t2 - t1)
print((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)
td = datetime.timedelta(6, 5, 1, 800, 12, 3)
print(td) 
print (td.seconds)
print (td.total_seconds())