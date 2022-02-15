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
    url = "https://www.expedia.com/?pwaLob=wizard-flight-pwa/"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        logger.info("Start.......................................")
        logger.info(f"Test file name: {__file__}")
        driver.maximize_window()
        driver.get(url)

        # Your code here

        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/div[1]/button").send_keys(
            "SFO")
        driver.find_element(By.XPATH, "//*[@id='location-field-leg1-destination-menu']/div[1]/div[1]/button").send_keys(
            "NYC")

        driver.find_element(By.XPATH, "//*[@id='d1-btn']").clear()
        driver.find_element(By.XPATH, "//*[@id='d1-btn']").send_keys("01/03/2022")

        driver.find_element(By.XPATH, "//*[@id='d2-btn']").clear()
        driver.find_element(By.XPATH, "//*[@id='d2-btn']").send_keys("04/03/2022")

        driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

        wait = WebDriverWait(driver, 10)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-layer-base']/div[2]/div[3]/div["
                                                         "1]/aside/fieldset/fieldset[1]/div[2]/div[1]/div["
                                                         "1]"))).click()
        element.click()

        logger.info("Successfully done.......................................")
    except Exception as e:
        logger.error("Exception raised: {}".format(e))
    finally:
        time.sleep(3)
        driver.quit()
        logger.info("End.........................................")

"""
# 1. Find the flight tab
# 2. Click on the flight tab
# 3. Find the flight origin input box
# 4. Enter the origin
# 5. Find the flight destination input box
# 6. Enter the destination
# 7. Find the departure date input box
# 8. Enter the departure date
# 9. Find the return date input box
# 10. Enter the return date
# 11. Find the search button
# 12. Click on the search button
# 13. Find the flight results
# 14. Verify the flight results
# 15. Find the flight price
# 16. Verify the flight price
# 17. Find the flight duration
# 18. Verify the flight duration
# 19. Find the flight departure time
# 20. Verify the flight departure time
# 21. Find the flight arrival time
# 22. Verify the flight arrival time
# 23. Find the flight departure airport
# 24. Verify the flight departure airport
# 25. Find the flight arrival airport
# 26. Verify the flight arrival airport
# 27. Find the flight airline
# 28. Verify the flight airline
# 29. Find the flight number
# 30. Verify the flight number
# 31. Find the flight stops
# 32. Verify the flight stops
# 33. Find the flight layover
# 34. Verify the flight layover
# 35. Find the flight layover duration
# 36. Verify the flight layover duration
# 37. Find the flight layover airport
# 38. Verify the flight layover airport
# 39. Find the flight layover city
# 40. Verify the flight layover city
# 41. Find the flight layover state
# 42. Verify the flight layover state
# 43. Find the flight layover country
# 44. Verify the flight layover country
# 45. Find the flight layover time
# 46. Verify the flight layover time
# 47. Find the flight layover timezone
# 48. Verify the flight layover timezone
# 49. Find the flight layover timezone offset
# 50. Verify the flight layover timezone offset
# 51. Find the flight layover timezone offset hours
# 52. Verify the flight layover timezone offset hours
"""
