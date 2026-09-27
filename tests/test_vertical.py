




import pytest

from pages.vertical import verticals


@pytest.mark.smoke
def test_trading(page):
    trade = verticals(page)
    trade.click_trading_option()


@pytest.mark.smoke
def test_RetailEcomers(page):
    retailEco = verticals(page)
    retailEco.click_RetailEcomers_option()

@pytest.mark.smoke
def test_Healthcare(page):
    health = verticals(page)
    health.click_Healthcare_option()

@pytest.mark.smoke
def test_Fintech(page):
    fintech = verticals(page)
    fintech.click_Fintech_option()