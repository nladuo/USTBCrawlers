import requests
from bs4 import BeautifulSoup


def parse_ip(content):
    soup = BeautifulSoup(content, "html.parser")
    print(soup.body.get_text())

resp = requests.get("http://2018.ip138.com/ic.asp")
parse_ip(resp.content.decode("gbk"))

print("\n改变ip后:")
proxies = {"http": "http://139.129.207.72:808"}   # 需要改成在西刺代理上看到的可用代理ip
resp2 = requests.get("http://2018.ip138.com/ic.asp", proxies=proxies)
parse_ip(resp2.content.decode("gbk"))
