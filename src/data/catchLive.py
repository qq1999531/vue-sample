import requests
from lxml import etree
import json
import datetime
import time


def crawlVstatRealtime():
    tempList = []
    url = "https://www.vstats.jp/realtime"
    resp = requests.get(url)
    response = etree.HTML(
        resp.content, parser=etree.HTMLParser(encoding='utf-8'))
    for i in range(3, 23):
        tempDict = {}
        if response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[2]/a/@href'.format(id=i)) and i != 13 and i != 34:
            tempDict["channelKey"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[2]/a/@href'.format(id=i))[0].replace("/channels/1:", "").replace("/overall", "")
            tempDict["videoKey"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[1]/a/@href'.format(id=i))[0].replace("/video/", "")
            tempDict["videoName"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[1]/a/text()'.format(id=i))[0].replace("\n", "").strip()
            tempDict["startDate"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[3]/span[1]/span[2]/text()'.format(id=i))[0]
            tempDict["lastingTime"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[3]/span[2]/text()'.format(id=i))[1].replace(",", "").replace("\n", "").strip()
            tempDict["liveViewerCount"] = int(response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[1]/div[1]/div[2]/div[2]/span/span/text()'.format(id=i))[0].replace(",", ""))
            tempStr = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[4]/span[1]/span[2]/text()'.format(id=i))[0].replace(",", "").split("/")
            tempDict["avgLiveViewerCount"] = int(
                tempStr[0].replace("avg:", "").strip())
            tempDict["maxLiveViewerCount"] = int(
                tempStr[1].replace("max:", "").strip())
            tempDict["playCount"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[4]/span[2]/text()'.format(id=i))[1].replace(",", "").replace("\n", "").strip()
            tempDict["likeCount"] = response.xpath(
                '/html/body/main/div[2]/div/div[{id}]/div[2]/div/div[2]/div[2]/div[4]/span[3]/text()'.format(id=i))[1].replace(",", "").replace("\n", "").strip()
            if tempDict["likeCount"] != "---":
                tempDict["likeCount"] = int(tempDict["likeCount"])
            if tempDict["playCount"] != "---":
                tempDict["playCount"] = int(tempDict["playCount"])
            tempList.append(tempDict)

    resp.close()
    with open('./src/data/youtubeChannels/realtime.json', 'w') as realtime:
        json.dump(tempList, realtime, indent=2)


# 入口程序
currentTimeStamp = int(time.time())
deadline = int(time.mktime(time.strptime("{today} 23:30:00".format(
    today=datetime.date.today()), "%Y-%m-%d %H:%M:%S")))
while currentTimeStamp < deadline:
    crawlVstatRealtime()
    print(currentTimeStamp)
    time.sleep(1800)
    currentTimeStamp = int(time.time())
