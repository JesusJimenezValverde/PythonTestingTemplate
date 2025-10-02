# This will have a class that contains all generic methods to navigate across the login screen.
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePage:
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_LIST = (By.XPATH, "//div[@class='inventory_item']")
    HAMBURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_LINK = (By.ID, "shopping_cart_container")
    TITLE = (By.XPATH, "//span[@data-test='title']")

    def __init__(self, driver):
        self.driver = driver

    def add_first_to_cart(self):
        inventory = self.driver.find_elements(*self.INVENTORY_LIST)
        element = inventory.pop()
        element.find_element(By.TAG_NAME, "button").click()
        return element.find_element(By.XPATH, "//div[@class='inventory_item_name ']").get_attribute("innerText")


    # def select_item_by_title(self, title):
    #     first_item_name = self.inventory[0].find_element.INVENTORY_LIST
    #     time.sleep(1)
    #     return first_item_name

    def go_to_cart(self):
        """Performs the full login action using locators from this class."""
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def log_out(self):
        self.driver.find_element(*self.HAMBURGER_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()
