#!/usr/bin/env python
# coding=utf8
""" 使用request.session进行登录 """
import requests

# 1. 创建一个Session
session = requests.session()
# 2. 登陆
session.post("http://nladuo.cn/crawler_lesson2/do_login.php",
             data={"uname": "nladuo", "passwd": "nladuo"})
# 3. 访问隐私页面
resp = session.get("http://nladuo.cn/crawler_lesson2/private.php")
print resp.content
