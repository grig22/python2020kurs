import pytest
from dirty import D3


@pytest.mark.parametrize("page", [1, 10])
@pytest.mark.parametrize("num", [1, 25])
def test_posts_num(page, num):
    posts = D3().posts(page=page, per_page=num)
    assert len(posts) == num
