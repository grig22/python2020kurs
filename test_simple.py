import pytest
import dirty


@pytest.mark.parametrize("page", [1, 10])
@pytest.mark.parametrize("num", [1, 25])
def test_posts_num(page, num):
    posts = dirty.posts(page=page, per_page=num)
    assert len(posts) == num


def fetch_ids(posts):
    ids = list()
    for post in posts:
        ids.append(post["id"])
    return ids


@pytest.mark.parametrize("post_id", fetch_ids(dirty.posts(per_page=4)))
def test_comments_num(post_id):
    exp = dirty.post(post_id)["comments_count"]
    act = len(dirty.comments(post_id))
    assert act == exp
