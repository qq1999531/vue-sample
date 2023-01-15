import requests
from lxml import etree

url = "https://playboard.co/en/channel/UCAoy6rzhSf4ydcYjJw3WoVg"
resp = requests.get(url)
response = etree.HTML(resp.content, parser=etree.HTMLParser(encoding='utf-8'))
print(resp.text)
print(resp.cookies)