import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from selenium_examples.logger import logger


def find_number_of_input_boxes(browser):
    input_boxes = browser.find_elements(By.CLASS_NAME, 'text_field')
    assert len(input_boxes) == 6
    return len(input_boxes)


def send_input_to_first_name(browser):
    assert browser.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
    browser.find_element(By.ID, 'RESULT_TextField-1').send_keys('Rustam')
    assert browser.find_element(By.ID, 'RESULT_TextField-1').get_attribute('value') == 'Rustam'


def send_input_to_last_name(browser):
    assert browser.find_element(By.ID, 'RESULT_TextField-2').is_displayed()
    browser.find_element(By.ID, 'RESULT_TextField-2').send_keys('Zokirov')
    assert browser.find_element(By.ID, 'RESULT_TextField-2').get_attribute('value') == 'Zokirov'


def send_input_to_phone_number(browser):
    assert browser.find_element(By.ID, 'RESULT_TextField-3').is_displayed()
    browser.find_element(By.ID, 'RESULT_TextField-3').send_keys('970001010')
    assert browser.find_element(By.ID, 'RESULT_TextField-3').get_attribute('value') == '970001010'


if __name__ == "__main__":
    url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        logger.info("Start.......................................")
        logger.info(f"Test file name: {__file__}")
        driver.maximize_window()
        driver.get(url)

        len_of_input_boxes_before_filling = find_number_of_input_boxes(driver)
        print(f"Number of input boxes before filling: {len_of_input_boxes_before_filling}")

        send_input_to_first_name(driver)
        send_input_to_last_name(driver)
        send_input_to_phone_number(driver)

        logger.info("Successfully done.......................................")
    except Exception as e:
        logger.error("Exception raised: {}".format(e))
    finally:
        time.sleep(3)
        driver.quit()
        logger.info("End.........................................")
