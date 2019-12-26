import requests

resp = requests.get("http://nladuo.cn/crawler_lesson7/ip.php")
print(resp.content.decode("utf8"))

print("\n改变ip后:")
proxies = {"http": "http://163.204.240.10:9999"}   # 需要在网上找一个的可用代理ip
resp2 = requests.get("http://nladuo.cn/crawler_lesson7/ip.php", proxies=proxies)
print(resp2.content.decode("utf8"))
