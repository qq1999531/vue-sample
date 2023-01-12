import requests
url = "https://api.vchama.xyz/api/stats/top"
resp = requests.get(url)
ch = resp.json()
#print(ch)
resp.close()
dic_lenth = len(ch['subscriberCount'])
for i in range(dic_lenth):
	print("频道名:"+ch['subscriberCount'][i]['channel_name']+"               "+"订阅数:"+str(ch['subscriberCount'][i]['count']))