# import requests
import json
from dirty import D3


def debug(st):
    re = json.dumps(st, indent=4, ensure_ascii=False)
    print(re)


# post_id = 2077496
# debug(D3().post(post_id))
# print("COMMENTS COUNT", D3().post(post_id)["comments_count"])
# print()
# debug(D3().comments(post_id))

debug(D3().user_posts("jovan"))

