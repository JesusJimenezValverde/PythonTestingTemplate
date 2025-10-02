import allure
import pytest
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

@allure.title("Test Successful User Login")
@allure.description("This test verifies that a user with valid credentials can log in.")
@pytest.mark.smoke
def test_login_valid_user(browser):
    browser.get(Config.BASE_URL)

    login_page = LoginPage(browser)
    login_page.login(Config.USERNAME_BASE, Config.PASSWORD_BASE)

    home_page = HomePage(browser)
    inventory_container: WebElement = browser.find_element(By.ID, "inventory_container")
    assert inventory_container.is_displayed(), "Inventory is not displayed"


@allure.title("Test Locked User Login")
@allure.description("This test verifies that a locked user is not able to log in.")
@pytest.mark.regression
def test_login_locked_user(browser):
    # Setup
    browser.get(Config.BASE_URL)
    login_page = LoginPage(browser)
    expected_error_message = "Epic sadface: Sorry, this user has been locked out."

    # Actions
    login_page.login(Config.USERNAME_LOCKED, Config.PASSWORD_BASE)
    error_message = login_page.get_error_message()

    # Assert
    assert (expected_error_message == error_message and "inventory" not in browser.current_url), "User  is not displayed"

#@pytest.mark.smoke
# def test_logout(browser):
#     browser.get(Config.BASE_URL)
#     login_page = LoginPage(browser)
#     login_page.login(Config.USERNAME_BASE, Config.PASSWORD_BASE)
#
#     # Logout
#
#     # Assert logout