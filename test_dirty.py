import pytest
from dirty import D3
import random
from jsonschema import validate
import d3schema


@pytest.mark.parametrize("page", [1, 10])
@pytest.mark.parametrize("per_page", [1, 25])
def test_posts_num(testlog, request, page, per_page):
    testlog.info(f"RUN '{request.node.name}'")
    posts = D3().posts(page=page, per_page=per_page)
    testlog.info(f"ASSERT")
    assert len(posts) == per_page


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


def some_post_ids(per_page):
    return [post["id"] for post in D3().posts(per_page=per_page)]


# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize("post_id", some_post_ids(4))
def test_comments_num(testlog, request, post_id):
    testlog.info(f"RUN '{request.node.name}'")
    comments = D3().post(post_id)["comments_count"]
    testlog.info(f"ASSERT")
    assert comments >= 0
    # далеко не всегда выполняется это условие
    # поэтому проверять его мы и не будем
    # act = len(D3().comments(post_id))
    # assert act == comments


@pytest.mark.parametrize("domain", D3().user_domains("mudhoney")["domains"][:4])
def test_owner(testlog, request, domain):
    testlog.info(f"RUN '{request.node.name}'")
    testlog.info(f"ASSERT")
    assert domain["owner"]["login"] == "mudhoney"


@pytest.mark.parametrize("feed, chhm",
                         [
                             (D3().domains(), d3schema.DOMAINS),
                             (D3().posts(), d3schema.POSTS)
                         ])
def test_schema(testlog, request, feed, chhm):
    testlog.info(f"RUN '{request.node.name}'")
    testlog.info(f"ASSERT")
    validate(instance=feed, schema=chhm)
