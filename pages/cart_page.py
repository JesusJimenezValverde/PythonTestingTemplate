from selenium.webdriver.common.by import By

class CartPage:
    #Class Variables

    # Functions inside the page
    def __init__(self, driver):
        self.driver = driver #Instance Variable (created 1 per object)

    def go_to_home(self):
        # Go to home page
        self.driver.find_element().click()

    def count_added_items(self):
        self.driver.find_element(By.CSS_SELECTOR, ".count-item").click()
