#!/usr/bin/env python
# coding=utf8
import requests
session = requests.session()

session.post("http://123.206.86.230/crawler_lesson2/do_login.php",
             data={"uname": "nladuo", "passwd": "nladuo"})  # 登陆
resp = session.get("http://123.206.86.230/crawler_lesson2/private.php")
print resp.content
