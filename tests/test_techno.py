
import pytest

from pages.techno import Technologies


@pytest.mark.smoke
def test_techno(page):
    tec =  Technologies(page)
    tec.click_ecom_option()


@pytest.mark.smoke
def test_mobappdevlopment(page):
    mobapp = Technologies(page)
    mobapp.click_Mobappdev_option()

@pytest.mark.smoke
def test_artificial(page):
    art = Technologies(page)
    art.click_artificial_option()