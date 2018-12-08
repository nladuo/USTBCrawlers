#!/usr/bin/env python
# coding=utf8
import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
db = client['test']

items = db["items"]


def list_items():
    for item in items.find():
        print(item)

# 增
print("添加数据")
items.insert({"id": 1, "name": "test1"})
items.insert({"id": 2, "name": "test2"})
items.insert({"id": 3, "name": "test3"})
list_items()

items.insert({"id": 4, "no_name": "test4"})
list_items()


# 删
print("删除id为1")
items.remove({"id": 1})
list_items()

# 改
print("修改id为2的name")
items.update({"id": 2}, {
    '$set': {'name': "test2_modified"}
})
list_items()

print("修改所有数据,添加一个title字段")
items.update({}, {
    '$set': {'title': "update title"}
}, multi=True)
list_items()

# 查
print("查找id为2")
print(items.find_one({"id": 2}))


items.remove()  # 移除数据


# 最后记得要关闭数据库连接
client.close()
