#!/usr/bin/env python
# coding=utf8
""" 直接使用requests库登陆 """
import requests

# 1. 先登陆
resp1 = requests.post("http://nladuo.tech/crawler_lesson2/do_login.php", data={
    "uname": "nladuo",
    "passwd": "nladuo"
})

# 2. 保存服务器传回来的Cookie
print "Set-Cookie:", resp1.headers["set-cookie"]
cookie = resp1.headers["set-cookie"].split(";")[0]

# 3. 再通过cookie请求隐私页面
resp = requests.get("http://nladuo.tech/crawler_lesson2/private.php", headers={
    "Cookie":  cookie  # 现用浏览器或者Telnet发送Post请求登录, 把cookie粘到这里
})
print resp.content
