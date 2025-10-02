import pytest
import time
from selenium.webdriver.common.by import By

from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_add_item_to_cart(browser):
    # Setup
    browser.get(Config.BASE_URL)
    login_page = LoginPage(browser)
    login_page.login(Config.USERNAME_BASE, Config.PASSWORD_BASE)

    # Actions
    home_page = HomePage(browser)
    first_element_name = home_page.add_first_to_cart()
    home_page.go_to_cart()
    time.sleep(2)


    # Assert that element in the cart has same name as element added