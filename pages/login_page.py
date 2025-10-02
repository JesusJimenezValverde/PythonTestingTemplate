# This will have a class that contains all generic methods to navigate across the login screen.
from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_CONTAINER = (By.XPATH, "//div[contains(@class, 'error-message-container')]")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Performs the full login action using locators from this class."""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_CONTAINER).get_attribute("innerText")