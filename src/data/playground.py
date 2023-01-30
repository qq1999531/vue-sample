import datetime
import time

tPart = datetime.date.today()
print(tPart)
t = "{today} 23:30:00".format(today=tPart)
print(t)
timeStruct = time.strptime(t,"%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeStruct))
print(int(time.time()))
print(timeStamp)