from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from selenium_examples.logger import logger


def open_page(browser, page):
    browser.get(page)


def conditional_commands(browser, page):
    """
    is_displayed()
    is_enabled()
    is_selected() - for checkboxes and radio buttons
    """
    open_page(browser, page)
    username_element = browser.find_element_by_id("username")
    assert username_element.is_displayed()
    assert username_element.is_enabled()

    password_element = browser.find_element_by_id("password")
    assert password_element.is_displayed()
    assert password_element.is_enabled()

    username_element.send_keys("tomsmith")
    password_element.send_keys("SuperSecretPassword!")

    browser.find_element_by_id("submit").click()

    # Validate that the page title is correct by presence of button with href logout
    logout_button = browser.find_element_by_xpath("//a[@href='/logout']")
    assert logout_button.is_displayed()


if __name__ == "__main__":
    url = "https://the-internet.herokuapp.com/"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        logger.info("Start.......................................")
        logger.info(f"Test file name: {__file__}")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Your code goes here
        conditional_commands(driver, url+"login/")

        logger.info("Successfully done.......................................")
    except Exception as e:
        logger.error("Exception raised: {}".format(e))
    finally:
        driver.quit()  # close the browser window, close() is also available, close only window
        logger.info("End.........................................")
