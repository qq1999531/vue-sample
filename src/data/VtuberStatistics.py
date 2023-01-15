import requests
from lxml import etree
import json
import datetime

#输入channel id扒取channel信息

def crawlPBSummary(channel,currentDate) :
    url = "https://playboard.co/en/channel/"+channel["channelPBKey"]
    resp = requests.get(url)
    response = etree.HTML(resp.content, parser=etree.HTMLParser(encoding='utf-8'))
    tempChannel = {"channelUserName":channel["channelUserName"],"channelName":channel["channelName"],"channelPBKey":channel["channelPBKey"],"videoCount":channel["videoCount"]}
    tempChannel["videoCount"] = int(response.xpath('//*[@id="app"]/div[1]/div/main/article/header/div/div/div[3]/div[4]/ul/li[2]')[0].text.strip().replace(",",""))
    tempChannel["channelName"] = response.xpath('//*[@id="app"]/div[1]/div/main/article/header/div/div/div[2]/a/span/text()')[0]
    tempChannel["lastUpdateTime"] = currentDate
    resp.close()
    print(tempChannel["channelName"] + "  :success")
    return tempChannel

#入口函数
#temp = crawlPBSummary('UCJFZiqLMntJufDCHc6bQixg')
currentDate = datetime.date.today()
with open('./src/data/output.json','rt',encoding="utf-8") as channels:
    temp = json.load(channels)
for i in range(len(temp)):
    if (currentDate>datetime.datetime.date(datetime.datetime.strptime(temp[i]["lastUpdateTime"],"%Y-%m-%d"))):
        temp[i] = crawlPBSummary(temp[i],currentDate.strftime("%Y-%m-%d"))
        with open('./src/data/output.json','w') as channels:
	        json.dump(temp,channels,indent=2)