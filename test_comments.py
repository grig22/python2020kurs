import pytest
from dirty import D3


def fetch_ids():
    return [post["id"] for post in D3().posts(per_page=4)]


@pytest.mark.parametrize("post_id", fetch_ids())
def test_comments_num(post_id):
    exp = D3().post(post_id)["comments_count"]
    act = len(D3().comments(post_id))
    assert act == exp
