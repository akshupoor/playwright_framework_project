import pytest

from pages.Tblog import Blogs


@pytest.mark.smoke
def test_bogs(page):
    tblogs =  Blogs(page)
    tblogs.click_blog_option()

