# import requests
import json
import dirty

posts = dirty.posts()
# print("222", json.dumps(posts, indent=4, ensure_ascii=False))
# print(len(posts["posts"]))

ids = list()
for post in posts:
    ids.append(post["id"])

print(ids)