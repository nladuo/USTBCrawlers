import requests
from bs4 import BeautifulSoup


def parse_ip(content):
    soup = BeautifulSoup(content, "html.parser")
    print(soup.body.get_text())

resp = requests.get("http://1212.ip138.com/ic.asp")
parse_ip(resp.content.decode("gbk"))

print("改变ip后:")
proxies = {"http": "http://175.155.25.77:808"}
resp2 = requests.get("http://1212.ip138.com/ic.asp", proxies=proxies)
parse_ip(resp2.content.decode("gbk"))
