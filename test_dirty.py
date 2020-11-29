import pytest
from dirty import D3
import random


@pytest.mark.parametrize("page", [1, 10])
@pytest.mark.parametrize("num", [1, 25])
def test_posts_num(testlog, request, page, num):
    testlog.info(f"RUN '{request.node.name}'")
    posts = D3().posts(page=page, per_page=num)
    testlog.info(f"ASSERT")
    assert len(posts) == num


def some_random_posts(login, num):
    posts = D3().user_posts(login)["posts"]
    random.shuffle(posts)
    return posts[:num]


@pytest.mark.parametrize("post", some_random_posts("jovan", 4))
def test_author(testlog, request, post):
    testlog.info(f"RUN '{request.node.name}'")
    if 'is_hidden' not in post.keys():
        testlog.info(f"ASSERT")
        assert post["user"]["login"] == "jovan"
    else:
        testlog.info(f"hidden post {post.items()}")


def some_post_ids(num):
    return [post["id"] for post in D3().posts(per_page=num)]


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize("post_id", some_post_ids(4))
def test_comments_num(testlog, request, post_id):
    testlog.info(f"RUN '{request.node.name}'")
    exp = D3().post(post_id)["comments_count"]
    act = len(D3().comments(post_id))
    # далеко не всегда выполняется это условие
    # очень динамичный ресурс
    testlog.info(f"ASSERT")
    assert act == exp


@pytest.mark.parametrize("domain", D3().user_domains("mudhoney")["domains"][:4])
def test_owner(testlog, request, domain):
    testlog.info(f"RUN '{request.node.name}'")
    testlog.info(f"ASSERT")
    assert domain["owner"]["login"] == "mudhoney"
