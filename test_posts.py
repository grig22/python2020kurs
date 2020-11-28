import pytest
from dirty import D3
import random


@pytest.mark.parametrize("page", [1, 10])
@pytest.mark.parametrize("num", [1, 25])
def test_posts_num(page, num):
    posts = D3().posts(page=page, per_page=num)
    assert len(posts) == num


def some_random_posts(login, num):
    posts = D3().user_posts(login)["posts"]
    random.shuffle(posts)
    return posts[:num]


@pytest.mark.parametrize("post", some_random_posts("jovan", 4))
def test_author(post):
    assert post["user"]["login"] == "jovan"
