"""
Learning objective:
    * How to use the CheckBox and RadioButton elements and conditional statements
    * Create custom parametrized marks
    * Create custom parametrized fixtures
"""

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

radio_button_ids = ["RESULT_RadioButton-7_0",
                    "RESULT_RadioButton-7_1"]
radio_button_label_xpath = ["//*[@id='q26']/table/tbody/tr[1]/td/label",
                            "//*[@id='q26']/table/tbody/tr[2]/td/label"]
checkboxes_ids = [f"RESULT_CheckBox-8_{i}" for i in range(7)]
checkboxes_xpath = [f"//*[@id='q15']/table/tbody/tr[{i}]/td/label" for i in range(1, 8)]


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.maximize_window()
    yield driver
    driver.quit()  # close the browser window, close() is also available, close only window


@pytest.fixture(scope="session")
def url():
    return "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"


# Custom parametrized fixture
@pytest.fixture(params=checkboxes_ids)
def checkbox_id(request):
    return request.param


@pytest.fixture(params=checkboxes_xpath)
def checkbox_xpath(request):
    return request.param


@pytest.mark.parametrize("radio_button_xpath", radio_button_label_xpath)
def test_radio_button_selected(driver, url, radio_button_xpath):
    driver.get(url)
    status = driver.find_element_by_id(radio_button_xpath).is_selected()
    assert status is False


@pytest.mark.parametrize("radio_button", radio_button_ids)
def test_radio_button_click(driver, url, radio_button):
    driver.get(url)
    driver.find_element_by_xpath(radio_button).click()
    status = driver.find_element_by_id(radio_button).is_selected()
    assert status is True


def test_checkbox_selected(driver, url, checkbox_id):
    driver.get(url)
    status = driver.find_element_by_id(checkbox_id).is_selected()
    assert status is False


def test_checkbox_click(driver, url, checkbox_xpath):
    driver.get(url)
    driver.find_element_by_xpath(checkbox_xpath).click()
    status = driver.find_element_by_id(checkbox_xpath).is_selected()
    assert status is True
