import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# This file works as the central factory for your fixtures. #

# This one makes sure the browser opens and closes
# once per test file(module scope)
@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

''' ### Usual alternative ###
def get_webdriver():
    """Initializes and returns a configured WebDriver instance."""
    if Config.BROWSER.lower() == "chrome":
        chrome_options = Options()
        if Config.HEADLESS_MODE:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    # You could add elif blocks for firefox, etc.
    else:
        raise ValueError(f"Browser '{Config.BROWSER}' is not supported.")

    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver
'''