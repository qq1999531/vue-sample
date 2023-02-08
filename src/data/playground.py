import datetime
import time
import json


def timePlayGround():
    tPart = datetime.date.today()
    print(tPart)
    t = "{today} 23:30:00".format(today=tPart)
    print(t)
    timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeStruct))
    print(int(time.time()))
    print(timeStamp)


def sortPlayGround():
    with open('./src/data/youtubeChannels/sortBySubs.json', 'rt', encoding="utf-8") as channels:
        temp = json.load(channels)
    rank = 1
    for i in temp:
        i.append(rank)
        rank+=1
    with open('./src/data/youtubeChannels/sortBySubs.json', 'w') as channels:
        json.dump(temp, channels, indent=2)


sortPlayGround()