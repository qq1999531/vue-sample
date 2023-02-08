import requests
import json
import datetime

url = "https://api.vchama.xyz/api/v4/graph/collabs"
resp = requests.get(url)
collabResp = json.loads(resp.content)
currentDate = datetime.date.today()
with open('./src/data/youtubeChannels/channels.json', 'rt', encoding="utf-8") as channels:
    temp = json.load(channels)
for i in collabResp["channels"]:
    tempDict = temp[collabResp["channels"][i]["channel_info"]["yt_channel_id"]]
    tempDict["channelName"] = collabResp["channels"][i]["name"]
    tempDict["characterENName"] = collabResp["channels"][i]["character_name"]["en"]
    tempDict["characterJPName"] = collabResp["channels"][i]["character_name"]["jp"]
    tempDict["color"] = collabResp["channels"][i]["color"]
    tempDict["avatar_url"] = collabResp["channels"][i]["avatar_url"]
    tempDict["banner_url"] = collabResp["channels"][i]["channel_info"]["banner"]
    tempDict["subscriberCount"] = int(
        collabResp["channels"][i]["channel_info"]["yt_stats"]["subscriberCount"])
    tempDict["videoCount"] = int(
        collabResp["channels"][i]["channel_info"]["yt_stats"]["videoCount"])
    tempDict["viewCount"] = int(
        collabResp["channels"][i]["channel_info"]["yt_stats"]["viewCount"])
    tempDict["lastUpdateTime"] = currentDate.strftime("%Y-%m-%d")
    temp[collabResp["channels"][i]["channel_info"]["yt_channel_id"]] = tempDict
with open('./src/data/youtubeChannels/channels.json', 'w') as channels:
    json.dump(temp, channels, indent=2)
