import json

# 读取summary数据
with open('./src/data/output.json', 'rt', encoding="utf-8") as channels:
    temp = json.load(channels)
# 创建临时字典
rawSubsSortData = {}
for i in temp:
    rawSubsSortData[i] = temp[i]["subscriberCount"]
# 排序
sortedSubsSortData = sorted(rawSubsSortData.items(),
                            key=lambda x: x[1], reverse=True)
with open('./src/data/youtubeChannels/sortBySubs.json', 'w') as channels:
    json.dump(sortedSubsSortData, channels, indent=2)
