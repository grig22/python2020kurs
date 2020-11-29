# import requests
import json
from dirty import D3
from jsonschema import validate
import d3schema


def debug(st):
    re = json.dumps(st, indent=4, ensure_ascii=False)
    print(re)


# validate(instance=D3().domains(), schema=d3schema.DOMAINS)
validate(instance=D3().posts(), schema=d3schema.POSTS)


# dmns = D3().domains()
# debug(dmns)

# post_id = 2077496
# debug(D3().post(post_id))
# print("COMMENTS COUNT", D3().post(post_id)["comments_count"])
# print()
# debug(D3().comments(post_id))

# posts = D3().user_posts("jovan")
# debug(posts)
# print("LENGTHHHHH", len(posts["posts"]))

