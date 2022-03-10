import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from selenium_examples.logger import logger


def open_page(browser, page):
    browser.get(page)
    browser.implicitly_wait(10)


def get_info_from_page(browser, page):
    """Used to get the title, url, and page source of a page"""
    open_page(browser, page)
    logger.info(f"Browser title: {browser.title}")
    logger.info(f"Browser current url: {browser.current_url}")
    logger.info(f"Browser page source: {browser.page_source[:100]}")


def click_button(browser, page):
    open_page(browser, page)
    browser.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()


def navigation(browser, *pages):
    """Used to go to the previous page or forward
    browser.back()
    browser.forward()

    Args:
        browser ([type]): [description]
    """

    open_page(browser, pages[0])
    logger.info("Navigating to page: {}".format(pages[0]))
    assert browser.current_url == pages[0]

    open_page(browser, pages[1])
    logger.info("Navigating to page: {}".format(pages[1]))
    assert browser.current_url == pages[1]

    browser.back()
    logger.info("Navigating back to page: {}".format(pages[0]))
    assert browser.current_url == pages[0]

    browser.forward()
    logger.info("Navigating forward to page: {}".format(pages[1]))
    assert browser.current_url == pages[1]


if __name__ == "__main__":
    url = "http://demo.automationtesting.in/"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        logger.info("Start.......................................")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # open_page(driver, url)
        # get_info_from_page(driver, url)
        # click_button(driver, url)
        navigation(driver, url+"Windows.html", url+"Register.html")

        logger.info("Successfully done.......................................")
    except Exception as e:
        logger.error("Exception raised: {}".format(e))
    finally:
        driver.quit()  # close the browser window, close() is also available, close only window
        logger.info("End.........................................")
