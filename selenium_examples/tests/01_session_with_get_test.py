import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium_examples import config


# Fixture to create a driver instance
@pytest.fixture(scope="session")
def driver():
    print("\n\nSetting up the driver...")
    driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)  # ChromeDriverManager().install()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()  # close the browser window, close() is also available, close only window
    print("\n\nClosing the driver...")


# Fixture to return the website url
@pytest.fixture(scope="session")
def url():
    return "https://the-internet.herokuapp.com/"


def test_driver_title(driver, url):
    driver.get(url)
    assert "The Internet" in driver.title


def test_current_url_after_moving_to_another_page(driver, url):
    driver.get(url)
    assert "The Internet" in driver.title

    driver.get("https://www.google.com/")
    assert driver.current_url == "https://www.google.com/"
    # print(browser.page_source)
