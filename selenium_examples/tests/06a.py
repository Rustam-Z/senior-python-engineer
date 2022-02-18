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


if __name__ == "__main__":
    url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        logger.info("Start.......................................")
        logger.info(f"Test file name: {__file__}")
        driver.maximize_window()
        driver.get(url)

        driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td/label').click()
        status = driver.find_element_by_id('//*[@id="q15"]/table/tbody/tr[1]/td/label').is_selected()

        logger.info("Successfully done.......................................")
    except Exception as e:
        logger.error("Exception raised: {}".format(e))
    finally:
        time.sleep(3)
        driver.quit()
        logger.info("End.........................................")
